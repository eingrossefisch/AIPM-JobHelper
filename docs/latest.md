# 🚀 2026 AIPM 暑期实习求职小助手 (PDT: 2026-01-30)

## 1️⃣ 岗位雷达
| 公司 | 职位名称 | 地点 | 开放时间/状态 | 投递链接 |
| :--- | :--- | :--- | :--- | :--- |
| **字节跳动** | AI产品经理实习生-国际化广告创意与品牌 | 北京 | ✅ 热招中 (ByteIntern) | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7591364235553343797?recomId=c4b28953-ee0e-11f0-94fe-fa163e53fcf3&sourceJobId=7591364983463250181&spread=B3RU5SF) |
| **字节跳动** | AI产品实习生-开发者服务 (Agent平台) | 北京 | ✅ 热招中 (ByteIntern) | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593021539598928133?recomId=773ae9e9-f5b3-11f0-b31f-08c0eb92e9e4&referral_code=65V7M7W&sourceJobId=7591505987386362117) |
| **字节跳动** | AI产品实习生-风控 | 深圳 | ✅ 热招中 (ByteIntern) | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7592520172445747461?recomId=cefac3a8-edc2-11f0-b31f-08c0eb92e9e4&sourceJobId=7533577581754484999) |
| **字节跳动** | AI产品实习生-TRAE (AI编程产品) | Unknown | ✅ 已开启 (ByteIntern) | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7593017196742314293?recomId=3afd1d45-eda1-11f0-b848-2ed66db3bf64&sourceJobId=7530995069861939463) |
| **字节跳动** | AI产品实习生-Data AML (机器学习中台) | Unknown | ✅ 已开启 (ByteIntern) | [点击投递](https://jobs.bytedance.com/campus/m/position/detail/7472624703070554386?recomId=6f85819d-f00f-11ef-99fb-00163e3cc94f&sourceJobId=7423752694421113126) |
| **字节跳动** | RAG产品实习生-Data AML | 北京 | ✅ 进行中 | [官网关注](https://jobs.bytedance.com/campus/) |
| **字节跳动** | AI产品经理实习生-Coze | 深圳 | ✅ 进行中 | [官网关注](https://jobs.bytedance.com/campus/) |
| **字节跳动** | AI大模型产品实习生（飞书文档） | 深圳 | ✅ 进行中 | [官网关注](https://jobs.bytedance.com/campus/) |
| **字节跳动** | 豆包大模型产品解决方案实习生-Data AML | 深圳 | ✅ 进行中 | [官网关注](https://jobs.bytedance.com/campus/) |

---

## 2️⃣ 面经收集
| 公司 | 职位方向 | 来源/时间 | 真题摘要 | 详情链接 |
| :--- | :--- | :--- | :--- | :--- |
| **网易互娱** | 大模型产品经理 | 牛客 / 2025-09 | 1. **幻觉控制**：在大模型进行观点总结的任务中，通过什么手段防范幻觉？<br>2. **上线指标**：产品发布的评估标准是什么？**准确率**等核心指标需达到什么水平？<br>3. **落地细节**：深挖实习项目职责，要求提供可量化的产出结果及解决卡点的逻辑。 | [查看详情](https://www.nowcoder.com/feed/main/detail/8ccd8e0875af4fa98778ca0cd4807f4b) |
| **美团** | AI产品经理 | 牛客 / 2025-09 | 1. **业务场景**：在点评 App 的“搜索-浏览-决策”O2O 路径中，AI 可以在哪些节点介入以提升 **GMV**？<br>2. **指标设定**：如何设定核心数据指标来衡量 **AIGC** 功能的初步效果与用户接受度？<br>3. **平衡策略**：如何看待 **AI 产品创新探索** 与 **业务落地可行性** 之间的关系？请举出实际平衡案例。 | [查看详情](https://www.nowcoder.com/discuss/797086169958739968) |

---

## 3️⃣ 八股背诵
| 领域 | 问题 (Q) | PM解答 (A) | 考察点 |
| :--- | :--- | :--- | :--- |
| **RAG 优化** | RAG 系统上线后用户反馈“回答不准”，作为 PM 你会从哪些技术环节排查优化？ | **核心逻辑**：遵循“垃圾进，垃圾出”原则，从检索、增强、生成三个阶段拆解问题。<br>**1. 检索阶段（Retrieval）**：检查文档切片（Chunking）是否太碎导致语义丢失；Embedding 模型是否与业务领域不匹配；是否需要引入“重排序（Rerank）”来过滤无关噪声。<br>**2. 增强阶段（Augmentation）**：检查检索出来的片段是否包含答案；是否存在多个冲突知识点误导模型。<br>**3. 生成阶段（Generation）**：检查 Prompt 是否约束过严；模型是否存在幻觉或由于上下文窗口限制忽略了关键信息。 | 考察对 RAG 全链路（从数据预处理到向量检索再到生成）的工程化理解。 |
| **Agent / 插件** | 让大模型调用 API（Tool Call）和让它直接写 Python 代码执行（Code Interpreter）有什么区别？PM 如何选型？ | **核心区别**：Tool Call 是“结构化执行”，代码执行是“逻辑化推理”。<br>**1. Tool Call（工具调用）**：适合业务逻辑清晰、有标准 API 的场景（如：查天气、下单）。优点是结果可控、安全，缺点是灵活性受限于定义的 API 数量。<br>**2. Code Interpreter（代码解释器）**：适合处理复杂数据计算、图表生成。优点是能处理非预期的复杂逻辑，缺点是执行环境（沙箱）成本高、存在安全风险且过程不可控。<br>**结论**：高频、标准业务流程用 Tool Call；低频、深度数据分析用代码执行。 | 考察对任务边界（Boundary）的定义能力及对工程安全与灵活性的权衡。 |
| **模型评测指标** | 除了算法侧的准确率，PM 应该如何构建 AI 产品的“业务评测体系”？ | **核心逻辑**：算法指标不等于用户体验，需建立多维度的 Benchmark（基准测试）。<br>**1. 质量维度**：引入“采纳率（Acceptance Rate）”和“人类对齐得分（Human Eval）”，评估模型回复是否符合业务专家预期。<br>**2. 性能维度**：关注“首字延迟（TTFT）”和“每秒 Token 数（TPS）”，这直接决定了用户是否会因为断断续续而跳出。<br>**3. 成本维度**：计算“单次任务成本（Cost per Task）”，评估业务收益是否能覆盖 Token 支出。<br>**4. 稳定性维度**：测试“幻觉率”和“拒绝回答率”，确保 B 端业务的严谨性。 | 考察 PM 对模型落地成本（Cost）、性能（Efficiency）与业务效果（Effectiveness）的综合评估能力。 |

---
AI生成，仅供参考，不保证准确性和实时性