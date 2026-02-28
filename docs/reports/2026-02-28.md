# 🚀 2026 AIPM 暑期实习求职小助手 (PDT: 2026-02-28)

## 1️⃣ 岗位雷达
| 公司 | 职位名称 | 地点 | 开放时间/状态 | 投递链接 |
| :--- | :--- | :--- | :--- | :--- |
| **字节跳动** | AI产品经理实习生-国际化广告创意与品牌 (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7591364235553343797?recomId=c4b28953-ee0e-11f0-94fe-fa163e53fcf3&sourceJobId=7591364983463250181&spread=B3RU5SF) |
| **字节跳动** | AI产品实习生-开发者服务 (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593021539598928133?recomId=773ae9e9-f5b3-11f0-b31f-08c0eb92e9e4&referral_code=65V7M7W&sourceJobId=7591505987386362117) |
| **字节跳动** | AI产品实习生-火山方舟 (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7600376032197708037?recomId=afbebd60-10b8-11f1-83f4-043f72dbbff8&sourceJobId=7530995069861939463&utm_device=pc&utm_keyword=qz2024pc008&utm_source=SEMbaidu) |
| **字节跳动** | AI产品实习生-TRAE (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593017196742314293?recomId=3afd1d45-eda1-11f0-b848-2ed66db3bf64&sourceJobId=7530995069861939463) |
| **字节跳动** | AI产品实习生-Data AML (ByteIntern) | 北京 | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7472624703070554386?recomId=6f85819d-f00f-11ef-99fb-00163e3cc94f&sourceJobId=7423752694421113126) |
| **字节跳动** | AI大模型产品实习生-飞书 (ByteIntern) | 北京 | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7600295644015921461?recomId=19f238a2-094f-11f1-9e5f-c286d9dfe25b&sourceJobId=7542736778987800839) |
| **字节跳动** | AI产品实习生-风控 (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7592520840450181429?recomId=827029f8-ee0d-11f0-9968-fa163e8e3500&referral_code=T3HGV9F&sourceJobId=7532038758469716231) |

---

## 2️⃣ 面经收集
| 公司 | 职位方向 | 来源/时间 | 真题摘要 | 详情链接 |
| :--- | :--- | :--- | :--- | :--- |
| **百度** | 文心一言-AI产品经理 | 牛客 / 2025-09-15 | 1. **技术评测**：如何利用 **ROUGE**、**BLEU** 指标评估“AI总结”质量？（答案：这些指标基于 n-gram 重合度，优势是客观高效，局限是无法识别语义等价性，需配合人工 Eval 评估准确性、信息密度与幻觉）。<br>2. **RAG应用**：设计“AI搜索”时，如何平衡外部知识与模型生成能力？（答案：采用 **Context Injection**。检索端负责“证据提供”并标注来源，模型端负责“语义对齐与降噪”，通过设定系统提示词强制模型优先参考证据，若冲突则提示未知）。<br>3. **Agent 架构**：Agent 形态与传统“问答式”AI 的核心区别？（答案：核心在于 **Planning** 自主规划与 **Tool-use** 动作执行能力，Agent 具备闭环解决复杂任务的能力而非仅生成文本）。 | [查看详情](https://www.nowcoder.com/discuss/797110591704879104) |
| **理想汽车** | 智能座舱-AI产品 | 牛客 / 2025-09-10 | 1. **模型决策框架**：如何在“大而慢”和“小而快”的模型间做业务权衡？（答案：构建基于场景频次的决策树。高频简单需求用小模型降低成本与响应时延；长尾复杂需求路由至大模型；针对那 20% 的不佳表现，需建立 **Guardrails** 兜底策略或人工干预机制）。<br>2. **数据评测**：大模型数据评测的核心指标及获取方式？（答案：关注 **Pass@k**、**Human Preference (RLHF方向)** 及业务相关指标如 **Correctness** 和 **Hallucination Rate**。通过标注平台进行 A/B Test 或构建金标准测试集获取）。<br>3. **机器学习原理**：请解释有监督与无监督学习的区别及应用。（答案：**Supervised** 需标签数据，用于分类/回归；**Unsupervised** 处理无标签数据，用于聚类/降维。AI 产品中常见于数据清洗与用户画像分群）。 | [查看详情](https://www.nowcoder.com/discuss/795292887301824512) |

---

## 3️⃣ 八股背诵
| 领域 | 问题 (Q) | PM解答 (A) | 考察点 |
| :--- | :--- | :--- | :--- |
| **RAG 落地** | 在知识库场景下，如何决定使用 RAG（检索增强生成）还是微调 (Fine-tuning)？ | **结论**：首选 RAG，只有在需要模型学习特定“语气”或“深层垂直领域逻辑”时才考虑微调。<br>**原理**：RAG 相当于给模型配了一个“实时图书馆”，解决事实性错误（幻觉）效果立竿见影；微调相当于让模型“闭卷重学”，数据更新慢且成本极高。<br>**PM权衡**：RAG 建设成本低、数据可追溯且支持秒级更新；微调则能缩短 Prompt 长度节省 Token，但无法保证事实准确。 | 考察对 LLM 幻觉治理、数据时效性与落地成本的权衡决策能力。 |
| **Agent 设计** | 为什么大模型 Agent 会陷入“复读”或死循环？如何从产品侧优化？ | **结论**：核心是“规划 (Planning)”能力的失效，模型在反思环节无法识别任务已陷入僵局。<br>**PM解法**：<br>1. **逻辑前置**：将复杂的“黑盒”决策拆解为标准的 SOP 流程图（Workflow）；<br>2. **强制熔断**：在工程侧设置最大执行轮数（Max Iterations）和人工介入点（Human-in-the-loop）；<br>3. **反馈增强**：提供更明确的“失败反馈”，告诉 Agent 哪些路径是走不通的。 | 考察对 Agent 自主性风险的预见性，以及对复杂流程（Task Planning）的控制力。 |
| **模型评测** | 作为一个 AIPM，你如何构建一套评估大模型表现的“金标准”？ | **结论**：拒绝盲目依赖公开榜单，必须建立业务私有的“黄金评测集（Golden Dataset）”。<br>**构建要点**：<br>1. **覆盖度**：从用户真实日志中抽取 500-1000 条典型 Query，覆盖各种边界 case；<br>2. **多维打分**：引入准确性（Factuality）、流畅度（Fluency）和业务转化指标（如点击率）；<br>3. **自动化 vs 人工**：先用更强模型（如 GPT-4o）作为裁判初步打分，关键环节引入专家人工审核。 | 考察对 AI 产品质量确定性的把控手段，避免研发“盲目调优”。 |

---
AI生成，仅供参考，不保证准确性和实时性