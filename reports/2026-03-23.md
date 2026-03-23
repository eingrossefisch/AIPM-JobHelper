# 🚀 2026 AIPM 暑期实习求职小助手 (PDT: 2026-03-23)

## 1️⃣ 岗位雷达
| 公司 | 职位名称 | 地点 | 开放时间/状态 | 投递链接 |
| :--- | :--- | :--- | :--- | :--- |
| **字节跳动** | AI产品经理（多维表格）- 飞书 | 北京 | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/position/detail/7532445955419212040) |
| **字节跳动** | AI产品经理实习生-国际化广告创意与品牌 (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7591364235553343797?recomId=c4b28953-ee0e-11f0-94fe-fa163e53fcf3&sourceJobId=7591364983463250181&spread=B3RU5SF) |
| **字节跳动** | AI产品经理实习生（内容生态识别方向）- TikTok (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7618057384311752965?recomId=5b962de8-2487-11f1-b8f3-043f72a6392c&sourceJobId=7538717848903485703) |
| **字节跳动** | AI产品实习生-开发者服务 (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593021539598928133?recomId=773ae9e9-f5b3-11f0-b31f-08c0eb92e9e4&referral_code=65V7M7W&sourceJobId=7591505987386362117) |
| **字节跳动** | AI产品实习生-风控 (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7592520172445747461?recomId=cefac3a8-edc2-11f0-b31f-08c0eb92e9e4&sourceJobId=7533577581754484999) |
| **字节跳动** | AI产品实习生-TRAE (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593017196742314293?recomId=77d0580c-ee0e-11f0-9cc3-043f72b42e20&sourceJobId=7591373199684061493&spread=B3RU5SF) |
| **字节跳动** | AI产品实习生-Data AML (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7472624703070554386?recomId=6f85819d-f00f-11ef-99fb-00163e3cc94f&sourceJobId=7423752694421113126) |
| **字节跳动** | AI产品设计（创意工程方向）实习生- TikTok (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7611744228109289781?recomId=bf59beb2-1e29-11f1-b6eb-00163e075c0f&sourceJobId=7547989395987613970) |
| **字节跳动** | 云与AI解决方案实习生-火山引擎 (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7612569660920023349?recomId=cc9d7f39-1a8f-11f1-8a4f-fa163ef1de73&referral_code=EPDMFRJ&sourceJobId=7530995069509503239) |

---

## 2️⃣ 面经收集
| 公司 | 职位方向 | 来源/时间 | 真题摘要 | 详情链接 |
| :--- | :--- | :--- | :--- | :--- |
| **字节跳动** | AI产品-智能体 (Agent) | 牛客 / 2025-03-04 | 1. **竞品对比**：**Agent** 与 Siri 等传统语音助手的核心差异（关键点：自主性、规划能力、长期记忆）。<br>2. **逻辑编排**：在跨场景规划中，如何设定工具调用的优先级（如“订票”优于“约饭”的权重逻辑）？<br>3. **异常处理**：设计 **Agent** 执行任务失败（如无票、接口报错）时的兜底方案。<br>4. **落地场景**：针对 **飞书** 办公场景，设计三个核心 AI 功能并论证价值。 | [查看详情](https://www.nowcoder.com/feed/main/detail/74d1e53e3c3649cdaf6ecd3a60d8fec5) |
| **百度** | AI产品-生成式应用 | 牛客 / 2025-03-04 | 1. **模型评估**：如何对模型输出进行测试和评分？（答案：采用 **ELO评分**、**人类反馈 (RLHF)** 或构建标准测试集体系）。<br>2. **产品优化**：AI 生成 PPT 场景中，有哪些可优化的体验点？（答案：多模态对齐、大纲结构的逻辑校验、**Prompt** 自动补全）。<br>3. **提示词工程**：在学术或生产场景下，如何系统性优化 **Prompt** 以提升复杂任务的成功率？ | [查看详情](https://www.nowcoder.com/feed/main/detail/422a0c5438504804b33885f00929e20e) |

---

## 3️⃣ 八股背诵
| 领域 | 问题 (Q) | PM解答 (A) | 考察点 |
| :--- | :--- | :--- | :--- |
| **RAG vs. SFT** | 针对企业私有知识库问答，你会选择 RAG（检索增强生成）还是 SFT（微调）？ | **一句话解释**：RAG 是给模型看“参考书”开卷考试，SFT 是让模型把知识“背下来”闭卷考试。<br>**成本与性能**：RAG 成本低、知识更新快（秒级）、有出处可查，但受限于上下文长度；SFT 成本高、需持续训练、无法解决实时性问题，但能让模型学到特定的语气和复杂格式。<br>**决策逻辑**：知识频繁更新选 RAG；需改变模型回复风格或学习特定领域思维逻辑选 SFT。 | 考察对知识更新效率、成本控制及“幻觉”治理手段的权衡能力。 |
| **幻觉治理** | 如何在产品层面降低 LLM 的“幻觉”问题，确保输出的准确性？ | **原理逻辑**：幻觉源于模型是基于概率预测下一个词，而非基于事实检索。<br>**产品手段**：1. **RAG 约束**：强制模型仅根据检索到的片段回答，不准发挥；2. **设置拒答**：通过 Prompt 明确要求“不知道就说不知道”；3. **自验证逻辑**：利用双模型校验，一个生成结果，一个负责审核。4. **Citations**：在 UI 界面标注引用来源，由用户最终校验。 | 考察对 LLM 底层局限性的理解及在不可靠技术上构建可靠产品的能力。 |
| **Agent / Workflow** | 为什么当前企业级 AI 应用更倾向于“Workflow (工作流)”而非纯粹的“Autonomous Agent (自主智能体)”？ | **核心痛点**：纯 Agent（如 AutoGPT）在复杂任务中存在“规划失效”和“死循环”风险，不可控性极高，导致业务侧无法交付。<br>**产品解法**：Workflow 将复杂任务拆解为标准 SOP（标准作业程序），将 LLM 嵌入到确定的节点中。<br>**Trade-off**：Workflow 牺牲了一定的灵活性换取了高确定性（Deterministic），更符合 B 端业务对结果稳定性的要求。 | 考察对业务确定性（Reliability）与 AI 自主性（Autonomy）之间的边界把控。 |

---
AI生成，仅供参考，不保证准确性和实时性