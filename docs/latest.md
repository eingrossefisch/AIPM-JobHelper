# 🚀 2026 AIPM 暑期实习求职小助手 (PDT: 2026-03-12)

## 1️⃣ 岗位雷达
| 公司 | 职位名称 | 地点 | 开放时间/状态 | 投递链接 |
| :--- | :--- | :--- | :--- | :--- |
| **字节跳动** | AI产品经理实习生-国际化广告创意与品牌 (ByteIntern) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7591364235553343797?recomId=c4b28953-ee0e-11f0-94fe-fa163e53fcf3&sourceJobId=7591364983463250181&spread=B3RU5SF) |
| **字节跳动** | AI产品实习生-TRAE (AI编程产品) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593017196742314293?recomId=3afd1d45-eda1-11f0-b848-2ed66db3bf64&sourceJobId=7530995069861939463) |
| **字节跳动** | AI产品实习生-火山方舟 (一站式大模型服务平台) | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7600376032197708037?recomId=afbebd60-10b8-11f1-83f4-043f72dbbff8&sourceJobId=7530995069861939463&utm_device=pc&utm_keyword=qz2024pc008&utm_source=SEMbaidu) |
| **字节跳动** | AI产品实习生-开发者服务 | Unknown | ✅ 热招中 | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593021539598928133?recomId=773ae9e9-f5b3-11f0-b31f-08c0eb92e9e4&referral_code=65V7M7W&sourceJobId=7591505987386362117) |
| **字节跳动** | Software Engineer Intern (Inference Infrastructure) | Global/Unknown | ✅ 2026 Summer | [点击投递](https://jobs.bytedance.com/en/position/7556514441468020999/detail) |
| **腾讯** | 2026实习生招聘 (含青云计划/AI专项) | 全国 | ✅ 3月5日启动 | [官网投递](https://join.qq.com/index.html) |
| **百度** | AIDU计划 / PSIG个人超级智能 (含产品/技术类) | 北京/上海/深圳 | ✅ 进行中 | [官网投递](https://talent.baidu.com/jobs/) |
| **阿里云** | 项目制实习生 (含通义千问/MaaS方向) | 杭州/北京等 | ✅ 进行中 | [官网投递](https://careers.aliyun.com/campus/home) |
| **小红书** | 2026届暑期校园招聘实习生 | Unknown | ✅ 已开启 | [官网投递](https://job.xiaohongshu.com/campus/position?positionName=%E3%80%902026%E6%A0%A1%E6%8B%9B%E3%80%91&workplaces=4201) |

---

## 2️⃣ 面经收集
| 公司 | 职位方向 | 来源/时间 | 真题摘要 | 详情链接 |
| :--- | :--- | :--- | :--- | :--- |
| **百度** | 文心一言-大模型产品 | 牛客 / 2025-09 | 1. **RAG**：解释其原理，并说明如何平衡“检索到的外部知识”与“模型自身生成能力”以确保答案可信。<br>2. **评测指标**：评估 AI 总结质量时，**ROUGE/BLEU** 等客观指标的局限性是什么？如何结合主观感受构建评价体系？<br>3. **Agent**：其与“问答式”助手的核心区别？预测其在企业服务或个人办公场景的落地优先级。<br>4. **决策框架**：在“高质慢速昂贵”的大模型与“中质快速廉价”的小模型间，如何构建上线决策框架？ | [查看详情](https://www.nowcoder.com/discuss/797110591704879104) |
| **网易互娱** | 大模型产品经理 | 牛客 / 2025-Q3 | 1. **幻觉防范**：在使用大模型进行观点总结时，从产品和技术维度如何防范 **Hallucination (幻觉)**？<br>2. **Prompt**：如何从文本长度、意图明确性、领域跨度等维度去定义并量化一个 **Prompt** 的复杂度？<br>3. **产品体验**：一个强大的基础模型是否等同于一个好的 AI 产品？请论证模型能力与产品体验的关系。<br>4. **提示词工程**：如何设计产品功能（而非手动撰写）来帮助普通用户通过 **Prompt Engineering** 释放模型潜力？ | [查看详情](https://www.nowcoder.com/feed/main/detail/8ccd8e0875af4fa98778ca0cd4807f4b) |

---

## 3️⃣ 八股背诵
| 领域 | 问题 (Q) | PM解答 (A) | 考察点 |
| :--- | :--- | :--- | :--- |
| **模型评测 (Evaluation)** | 项目上线后如何评估效果？算法指标和业务指标分别关注什么？ | **核心思路**：算法指标衡量“模型行不行”，业务指标衡量“产品是否有用”。<br>**算法指标**：侧重于 RAG 或生成质量，如 **Recall@K**（检索召回率）、**Answer Relevance**（答案相关性）及 **Faithfulness**（忠实度/幻觉控制）。<br>**业务指标**：侧重于降本增效，如 **人工采纳率**（AI 生成结果被用户直接使用的比例）、**任务完成耗时 (TAT)**、以及 **单位 Token 成本产生的商业 GMV**。 | 考察 PM 能否将技术参数转化为商业价值，避免“陷入技术自嗨”。 |
| **能力边界 (Troubleshooting)** | 当 AI 输出效果不好时，你如何判断是 Prompt 问题、工程问题还是模型边界？ | **排查路径**：按“低成本到高成本”原则进行四步诊断：<br>1. **Prompt 问题**：输入是否模糊？增加 **Few-shot**（示例）或 **CoT**（思维链）能否立即改善？<br>2. **工程/RAG 问题**：上下文是否过长导致遗忘？检索回来的片段是否包含了正确答案？（通过 Badcase 溯源检索环节）。<br>3. **流程设计问题**：任务是否太复杂？是否需要拆解为 **Multi-stage** 或 **Agent 工作流**？<br>4. **模型边界**：如果以上均无解，且模型在逻辑推理上反复报错，则判定为模型选型或微调 (SFT) 的必要性。 | 考察产品经理对技术链路的诊断能力及对研发资源的分配优先级。 |
| **工具调用 (Tool Use)** | 让 LLM 进行 Tool Call (函数调用) 和写代码执行 (Code Interpreter) 有什么区别？ | **原理区别**：Tool Call 是模型输出 JSON 格式指令，由**外部系统**执行；Code Interpreter 是模型直接写 Python 代码并在**沙箱环境**运行。<br>**PM 权衡**：<br>1. **Tool Call**：更安全、结果更标准，适用于查库存、调 API 等确定性业务逻辑。<br>2. **Code Interpreter**：更灵活，擅长处理复杂的数学计算、大规模数据清洗或自动化绘图，但存在代码执行安全风险及更高的 Token 消耗。 | 考察对 LLM 交互范式的深层理解，以及在特定业务场景下的架构方案选型。 |

---
AI生成，仅供参考，不保证准确性和实时性