import os
import requests
import datetime

# 从 GitHub Secrets 中读取
DIFY_API_KEY = os.environ.get("DIFY_API_KEY")
DIFY_URL = "https://api.dify.ai/v1/workflows/run"

def run_workflow():
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "inputs": {},
        "response_mode": "blocking",
        "user": "github-action"
    }

    print("正在请求Dify生成今日日报...")
    response = requests.post(DIFY_URL, headers=headers, json=data, timeout=300)
    response.raise_for_status()
    
    content = response.json().get('data', {}).get('outputs', {}).get('final_report', "")
    return content

def save_report(text):
    if not text:
        print("Error: 未获取到有效内容")
        return
    
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # 1. 存入历史文件夹
    os.makedirs("reports", exist_ok=True)
    with open(f"reports/{today}.md", "w", encoding="utf-8") as f:
        f.write(text)
    
    # 2. 更新主页（README 或 LATEST_REPORT）
    with open("README.md", "w", encoding="utf-8") as f:
        # 这里可以加一些固定的项目介绍头
        header = "#2026AIPM暑期实习求职小助手\n\n> 每日更新。\n\n"
        f.write(header + text)
    
    print(f"日报已成功存档：reports/{today}.md")

if __name__ == "__main__":
    try:
        report_text = run_workflow()
        save_report(report_text)
    except Exception as e:
        print(f"❌️运行出错: {e}")