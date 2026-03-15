# 🚀 2026 AIPM 暑期实习求职小助手 (PDT: 2026-03-15)

## 1️⃣ 岗位雷达
| 公司 | 职位名称 | 地点 | 开放时间/状态 | 投递链接 |
| :--- | :--- | :--- | :--- | :--- |
| **字节跳动** | AI产品经理实习生-国际化广告创意与品牌 (ByteIntern) | Unknown | ✅ ByteIntern 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7591364235553343797) |
| **字节跳动** | AI产品实习生-开发者服务 (ByteIntern) | Unknown | ✅ ByteIntern 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593021539598928133) |
| **字节跳动** | AI产品经理（多维表格）-飞书 | 北京 | ✅ 进行中 | [点击投递](https://jobs.bytedance.com/campus/position/detail/7532445955419212040) |
| **字节跳动** | AI产品实习生（AM智能运营）-TikTok Shop (ByteIntern) | Unknown | ✅ ByteIntern 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7615148164682647813) |
| **字节跳动** | AI产品实习生-TRAE (ByteIntern) | Unknown | ✅ ByteIntern 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593017196742314293) |
| **字节跳动** | AI产品实习生-风控 (ByteIntern) | Unknown | ✅ ByteIntern 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7592520840450181429) |
| **字节跳动** | AI产品设计（创意工程方向）实习生-TikTok (ByteIntern) | Unknown | ✅ ByteIntern 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7611744228109289781) |
| **字节跳动** | 云与AI解决方案实习生-火山引擎 (ByteIntern) | Unknown | ✅ ByteIntern 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7612569660920023349) |

---

## 2️⃣ 面经收集
| 公司 | 职位方向 | 来源/时间 | 真题摘要 | 详情链接 |
| :--- | :--- | :--- | :--- | :--- |
| **百度** | 文心一言-AI产品经理 | 牛客 / 2025-09 | 1. **指标评测**：如何利用 **ROUGE**、**BLEU** 指标评估“AI总结”质量？（答案：ROUGE侧重召回，评估参考文本在生成文本中的覆盖程度；BLEU侧重精确度，评估生成文本的流畅性；PM需结合主观评测解决“事实性幻觉”问题）<br>2. **RAG 架构**：解释 **RAG** 原理并平衡“外部检索”与“模型生成”的关系。（答案：通过向量检索找到最相关知识片段作为 Context 喂给模型；平衡点在于置信度阈值：高置信度外部知识优先，通用逻辑由 LLM 自行补全）<br>3. **决策框架**：如何在“大模型/高成本/高质量”与“小模型/低成本/一般质量”间做灰度选型？ | [查看详情](https://www.nowcoder.com/discuss/797110591704879104) |
| **字节跳动** | AI产品-智能客服 | 牛客 / 2025-03 | 1. **能力整合**：如何重构整合 **ASR/TTS/LLM** 与知识库的语音客服交互？（答案：核心在于降低端到端 Latency，增加语音打断机制，并在 ASR 转写阶段加入业务词库纠偏）<br>2. **Agent 赛道**：如何拆解 **Agent** 平台的对标维度？（答案：从模型底座能力、工具调用 (Tool-use) 丰富度、私有化部署成本、合规安全风险、开发者生态五个维度进行拆解）<br>3. **业务深挖**：针对直播/抖音场景，如何设计 AI 功能提升用户留存或转化。 | [查看详情](https://www.nowcoder.com/feed/main/detail/6d63a7164a0641aabf3fc4e724b9a43a) |

---

## 3️⃣ 八股背诵
| 领域 | 问题 (Q) | PM解答 (A) | 考察点 |
| :--- | :--- | :--- | :--- |
| **知识库/RAG** | 业务落地时，如何决定用 RAG (检索增强生成) 还是微调 (Fine-tuning)？ | **结论**：优先 RAG，除非需要改变模型的基础技能或输出风格。<br>**对比**：RAG 相当于给模型配“外挂字典”，解决数据实时性、私有化安全及“幻觉”溯源问题，开发成本低；微调相当于“让模型考证”，适合学习特定行业黑话、复杂指令遵循或固定输出格式，但更新慢且数据成本极高。<br>**Trade-off**：知识实时性选 RAG，特定任务表现（如语气转换）选微调。 | 考察对技术路径的选择能力，平衡成本、开发周期与业务收益。 |
| **评估体系 (Eval)** | 如何科学评测一个 AI 产品的上线标准？如何量化“幻觉”？ | **方案**：构建多维“评估漏斗”。<br>**1. 客观评估**：针对确定性任务（如提取信息），用准确率、召回率、R-Judge 指标。<br>**2. 模型评估 (LLM-as-a-judge)**：用更强的模型（如 GPT-4o）对候选项进行打分或排序。<br>**3. 人工评估**：金标准，进行双盲 A/B Test。<br>**治理幻觉**：设置召回置信度阈值，低于阈值则返回“无法回答”或提示“参考信息不足”。 | 考察对不可预测性系统（Probabilistic System）的质量管理与风险防控。 |
| **Agentic Workflow** | 为什么在 B 端场景中，Agent 建议采用“SOP 编排”而非“全自主规划”？ | **原因**：全自主 Agent（如 AutoGPT）在复杂任务中不可控，容易产生逻辑幻觉或死循环，且 Token 成本极高。<br>**逻辑**：B 端强调确定性，PM 需将复杂任务拆解为标准的 SOP（标准作业程序），通过“工作流编排”锁定关键路径，AI 仅在特定节点负责内容生成或分类。这属于“人在回路（Human-in-the-loop）”的半自动治理。 | 考察对 Agent 落地确定性（Deterministic）与灵活性（Flexible）的博弈思维。 |

---
AI生成，仅供参考，不保证准确性和实时性