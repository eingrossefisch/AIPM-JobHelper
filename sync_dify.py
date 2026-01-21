# -*- coding: utf-8 -*-
"""
sync_dify.py
------------------------------------------------------------
用途：
1) 通过 Dify Workflow Run API 触发一个 Workflow（使用 streaming 避免 blocking 超时）
2) 轮询查询 workflow_run_id 的执行结果，直到 succeeded/failed/stopped
3) 从 outputs 中提取 Markdown 文本，保存到：
   - reports/YYYY-MM-DD.md
   - README.md（覆盖更新）

安全性：
- 不在代码中硬编码 API Key
- 通过环境变量 DIFY_API_KEY 读取（本地可临时 set，GitHub Actions 用 Secrets 注入）

环境变量（必需/可选）：
- 必需：
  - DIFY_API_KEY: Dify 应用的 API Key（以 app- 开头）
- 可选：
  - DIFY_USER: 传给 Dify 的 user 字段（默认 github-action）
  - DIFY_INPUTS_JSON: Workflow inputs 的 JSON 字符串（默认 {}）
  - DIFY_MAX_WAIT_SEC: 最长等待秒数（默认 900）
  - DIFY_POLL_INTERVAL_SEC: 轮询间隔秒数（默认 3）
------------------------------------------------------------
"""

import os
import json
import time
import datetime
import requests


# -----------------------------
# Dify API endpoints（Cloud）
# -----------------------------
DIFY_RUN_URL = "https://api.dify.ai/v1/workflows/run"
DIFY_DETAIL_URL = "https://api.dify.ai/v1/workflows/run/{workflow_run_id}"


def env(name: str, default: str = "") -> str:
    """读取环境变量的小工具，统一 strip。"""
    return os.getenv(name, default).strip()


def build_headers(api_key: str, accept: str = "application/json") -> dict:
    """构造请求头。"""
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": accept,
    }


def parse_inputs_json(raw: str) -> dict:
    """
    解析 DIFY_INPUTS_JSON（字符串 -> dict）。
    如果为空或解析失败，则返回 {}。
    """
    if not raw:
        return {}
    try:
        obj = json.loads(raw)
        return obj if isinstance(obj, dict) else {}
    except json.JSONDecodeError:
        return {}


def start_workflow_streaming(session: requests.Session, api_key: str, inputs: dict, user: str) -> str:
    """
    用 streaming 启动 workflow，尽快拿到 workflow_run_id。
    这样不会卡在 blocking 模式的 Cloudflare 超时里。
    """
    payload = {
        "inputs": inputs or {},
        "response_mode": "streaming",
        "user": user,
    }

    headers = build_headers(api_key, accept="text/event-stream, application/json")

    print("🚀 Start workflow (streaming)...")

    # timeout=(connect_timeout, read_timeout)
    with session.post(DIFY_RUN_URL, headers=headers, json=payload, stream=True, timeout=(10, 120)) as r:
        r.raise_for_status()

        workflow_run_id = None

        # SSE: 每行常见格式 "data: {...}"
        for raw_line in r.iter_lines(decode_unicode=True):
            if not raw_line:
                continue

            line = raw_line.strip()
            if not line.startswith("data:"):
                continue

            data_str = line[len("data:"):].strip()
            if data_str == "[DONE]":
                break

            try:
                evt = json.loads(data_str)
            except json.JSONDecodeError:
                continue

            workflow_run_id = (
                evt.get("workflow_run_id")
                or evt.get("data", {}).get("workflow_run_id")
                or evt.get("data", {}).get("id")
                or workflow_run_id
            )

            event_name = evt.get("event")
            if event_name and workflow_run_id:
                print(f"🧩 event={event_name} run_id={workflow_run_id}")

            if workflow_run_id:
                return workflow_run_id

    raise RuntimeError("❌ Failed to get workflow_run_id from streaming events.")


def poll_workflow_result(session: requests.Session, api_key: str, workflow_run_id: str,
                         max_wait_sec: int, interval_sec: int) -> dict:
    """
    轮询 GET /workflows/run/{workflow_run_id} 直到结束。
    返回最终 payload（兼容 data 包裹）。
    """
    url = DIFY_DETAIL_URL.format(workflow_run_id=workflow_run_id)
    headers = build_headers(api_key)

    deadline = time.time() + max_wait_sec

    while time.time() < deadline:
        r = session.get(url, headers=headers, timeout=(10, 30))
        r.raise_for_status()
        j = r.json()

        payload = j.get("data", j)  # 兼容有些返回包在 data 里
        status = payload.get("status") or j.get("status")

        if status in ("succeeded", "failed", "stopped"):
            print(f"✅ finished: status={status}")
            return payload

        print("⏳ status=running ...")
        time.sleep(interval_sec)

    raise TimeoutError(f"❌ Poll timeout: workflow_run_id={workflow_run_id}")


def extract_text_from_outputs_raw(outputs_raw) -> str:
    """
    从 outputs_raw 中提取最终 Markdown 文本。
    outputs_raw 可能是：
    - dict: {"output": "..."}
    - str: 纯 markdown
    - str: JSON 字符串："{\"output\": \"# ...\"}"（你当前就是这种）
    """
    if outputs_raw is None:
        return ""

    # A) dict
    if isinstance(outputs_raw, dict):
        for k in ("output", "text", "result", "content"):
            v = outputs_raw.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
        for v in outputs_raw.values():
            if isinstance(v, str) and v.strip():
                return v.strip()
        return ""

    # B) str
    if isinstance(outputs_raw, str):
        s = outputs_raw.strip()
        if not s:
            return ""

        # 尝试按 JSON 字符串解析
        try:
            obj = json.loads(s)
            if isinstance(obj, dict):
                for k in ("output", "text", "result", "content"):
                    v = obj.get(k)
                    if isinstance(v, str) and v.strip():
                        return v.strip()
                for v in obj.values():
                    if isinstance(v, str) and v.strip():
                        return v.strip()
                return ""
            # JSON 但不是 dict，就当普通文本
            return s
        except json.JSONDecodeError:
            # 不是 JSON，就当普通文本
            return s

    # C) 其他类型
    return str(outputs_raw).strip()


def get_outputs_raw(detail_payload: dict):
    """兼容 outputs / output 字段命名差异。"""
    if "outputs" in detail_payload:
        return detail_payload.get("outputs")
    if "output" in detail_payload:
        return detail_payload.get("output")
    return ""


def save_report(text: str):
    """
    保存报告：
    - reports/YYYY-MM-DD.md
    - README.md（覆盖）
    """
    text = (text or "").strip()
    if not text:
        print("❌ 内容为空，不保存。")
        return

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    os.makedirs("reports", exist_ok=True)

    report_path = os.path.join("reports", f"{today}.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(text)

    with open("README.md", "w", encoding="utf-8") as f:
        header = f"# 🚀 2026 AIPM 暑期实习求职小助手\n\n> 📅 最后更新: {today}\n\n---\n\n"
        f.write(header + text)

    print(f"✅ 保存成功：{report_path}")
    print("✅ README 已更新：README.md")


def main():
    # 1) 从环境变量读取关键配置（GitHub Actions 用 Secrets 注入 DIFY_API_KEY）
    api_key = env("DIFY_API_KEY")
    if not api_key:
        raise RuntimeError("❌ Missing DIFY_API_KEY. Please set it as env var / GitHub Secret.")

    user = env("DIFY_USER", "github-action")
    inputs = parse_inputs_json(env("DIFY_INPUTS_JSON", ""))

    max_wait_sec = int(env("DIFY_MAX_WAIT_SEC", "900"))
    interval_sec = int(env("DIFY_POLL_INTERVAL_SEC", "3"))

    # 2) Session：忽略系统代理，避免 Windows/公司代理导致卡顿
    session = requests.Session()
    session.trust_env = False

    # 3) 启动 + 轮询
    run_id = start_workflow_streaming(session, api_key, inputs, user)
    detail = poll_workflow_result(session, api_key, run_id, max_wait_sec, interval_sec)

    # 4) 提取 outputs 并解析为 Markdown 文本
    outputs_raw = get_outputs_raw(detail)

    print(f"📦 outputs_raw type = {type(outputs_raw)}")
    preview = str(outputs_raw)[:300].replace("\n", "\\n")
    print(f"📦 outputs_raw preview = {preview}")

    text = extract_text_from_outputs_raw(outputs_raw)

    print(f"📦 text length = {len(text)}")
    print(f"📦 text head = {text[:120].replace(chr(10), ' ')}")

    # 5) 保存
    save_report(text)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ 出错: {e}")
        raise
