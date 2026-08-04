# quantools 项目状态台账

更新时间：2026-08-04

本文记录当前已经落地的成果、已经批准的目标设计，以及仍处于评估阶段的
候选项目。它是阶段性事实快照，不把设计目标写成已经实现的功能。

## 一、总体架构已经明确

项目形成了稳定的职责分工：

```text
Qlib      = 大脑：因子、模型和机器学习研究
VectorBT  = 高速实验室：批量参数实验和快速筛选
LEAN      = 交易发动机：撮合、订单、组合、仿真和执行
qmtq      = A 股/QMT 协议层：可信数据、安全边界、run bundle 和 AI 审计
Paper2Quant = 研究转化层：把论文、研报和事件材料转为可验证候选
quantools = 元工作区：固定依赖并连接各组件
```

系统采用统一的权责原则：

```text
AI-native orchestration
+ deterministic evidence and computation
+ human-controlled production promotion
```

大模型可以阅读、提取、提出假设、生成代码和解释结果，但不能自行验证因子、
修改 qmtq 已接受状态、取得 QMT 实盘凭据或下单。

## 二、仓库和依赖治理已经落地

已经完成：

- `externals/` 不再整体忽略，新增项目和版本变化对 Git 可见。
- 第三方源码统一作为 Git submodule 管理，由根仓库固定精确提交。
- `.gitmodules` 保存上游地址，`externals/manifest.yaml` 保存角色和信任分类。
- 依赖采用单项目、经评审升级，不进行无审查的批量跟随更新。
- OSkhQuant 已从根目录问题位置整理到 `externals/oskhquant`。
- Paper2Quant 已拆分到 `gyfin/Paper2Quant` 独立仓库，并由
  `packages/paper2quant` 作为第一方 submodule 引入。
- `D:\qmtq` 继续作为独立兄弟仓库，保持协议和实盘安全边界。

## 三、已纳入的开源能力

### 量化研究与执行

| 项目 | 当前定位 |
| --- | --- |
| Qlib | 因子、模型和 ML 研究 |
| VectorBT | 向量化参数扫描和候选筛选 |
| LEAN | 高保真撮合、组合、订单和执行仿真 |
| Kronos | 金融时间序列基础模型研究参考 |
| QuantsPlaybook | A 股因子、券商研报复现和策略案例库 |
| OSkhQuant | MiniQMT/A 股集成参考实现 |

### 研究转化参考

| 项目 | 当前定位 |
| --- | --- |
| cangjie-skill | 仓颉式研究提取、核验和知识组织方法 |
| Paper2Agent | 从论文构建可调用代理的参考流程 |
| paper2code | 从论文生成和验证代码的参考流程 |
| RD-Agent | 自动化研究、实验和迭代参考 |

### 大模型工作台与代理宿主

| 项目 | 当前定位 |
| --- | --- |
| Codex Desktop | 主要交互研究台、人工审阅和批准入口 |
| Codex CLI | 批处理、回归、定时任务和结构化审计入口 |
| kimi-cli / kimi-code | 可选中文长上下文和编码代理宿主 |
| Open Science | 可选本地研究工作台，共享 Paper2Quant MCP 契约 |

### 开源研究方法

| 项目 | 当前定位 |
| --- | --- |
| BestSerenitySkillFromAT | 产业链瓶颈方法综合、模板与市场适配参考 |
| serenity-bottleneck-hunter | 供应链逆向追踪和瓶颈发现方法参考 |

Open Science 与两个 Serenity 方法库均已固定为 Git submodule。Serenity
方法处于 `incubating`、`reference_only` 状态，不能直接生成已接受信号。

### 股票研究代理与平台

| 项目 | 当前定位 |
| --- | --- |
| qilihei/StockAgent | A 股工作流、数据/新闻、因子、回测和工具模式参考 |
| MingyuJ666/Stockagent | LLM 投资者行为与市场仿真方法参考；许可证缺失阻断代码使用 |
| ValueCell | 代理注册、编排、A2A、持久化和应用外壳参考；交易能力排除在外 |

三个项目均已固定为 `incubating`、`reference_only` 和 `pending_review`。
当前 manifest v1 只是库存清单，不是批准目录。它们没有被安装、启动或连接
至 qmtq，也没有启用任何凭据或交易路径。

## 四、Paper2Quant 当前成果

### 已实现的 0.2 确定性纵向切片

Paper2Quant 当前能够：

- 接受显式提供的原生文本 PDF 和版本化 `SourceSpec`；
- 保留页、文本块、阅读顺序和坐标级证据；
- 通过固定 Provider 响应生成证据、主张与实验候选；
- 生成 qmtq `research-source v2` 候选包和独立 `ValidationRequest`；
- 保证运行尝试不可变，记录内容哈希与相对产物引用；
- 通过来源范围、证据绑定和文档类型声明门禁防止越权采纳。

当前版本仍不会搜索互联网、调用远程大模型、执行第三方代码、运行回测、
访问 QMT、写入 qmtq `research_cache`、批准实验或生成已接受交易信号。

### 已批准但尚未实现的目标

AI 原生多模型架构已经批准并记录，目标包括：

- Codex Desktop 与 Codex CLI 共享项目规则和工具契约；
- Paper2Quant MCP 提供窄而稳定的研究工具面；
- Model Gateway 按能力接入 Kimi、DeepSeek、Codex、OpenAI 或本地模型；
- 多模型独立提取、结构化比较、分歧裁决和按难度升级；
- 证据、公式、变量、时点、代码、测试、引擎结果和人工编辑全程留痕；
- qmtq 负责确定性验证和准入，人工负责最终推广。

对应设计位于：

`packages/paper2quant/docs/superpowers/specs/2026-07-26-ai-native-multi-model-architecture-design.md`

该设计及 0.2 实现已经推送至 Paper2Quant `main`，当前固定提交为
`beaacc161bab96616f1090b20a4402d14b256e59`。

## 五、开源能力持续接入机制

系统采用“稳定内核、开放能力层、受控孵化”的原则：

```text
发现 -> 登记 -> 固定版本 -> 隔离评测 -> 人工批准 -> 接入或退出
```

已完成基础治理：

- `.gitmodules` 固定上游和精确提交；
- `externals/manifest.yaml` 记录角色、信任等级、生命周期和接入方式；
- `externals/incubator/` 保存评测规则和候选项目记录；
- 新项目默认不能访问实盘凭据或绕过 qmtq；
- Serenity 两个方法库作为首批 `reference_only` 试点。
- 三个股票研究代理与平台候选已固定版本并记录差异，但仍全部处于
  `pending_review`，固定版本不等于批准接入。

## 六、新闻、舆情与情景推演方向

BettaFish 与 MiroFish 已完成初步评估，但尚未克隆或登记为 quantools
submodule。

官方项目关系表明二者属于同一作者名下的互补链路：

```text
BettaFish = 多源新闻、社交媒体和舆情采集分析
MiroFish  = 基于材料构建多智能体社会模拟与情景推演
```

在本项目中的目标链路为：

```text
新闻、公告、研报、社交媒体
  -> BettaFish-like 新闻与舆情雷达
  -> EventEvidenceBundle
  -> Paper2Quant 候选假设
  -> MiroFish scenario_hypothesis
  -> qmtq 时点、证据和准入检查
  -> Qlib / VectorBT 验证
  -> LEAN 执行仿真
```

拟定边界：

- BettaFish 仅作为多源采集、去重、事件聚类、主体映射和舆情分析参考。
- MiroFish 只生成情景假设，不直接生成已接受信号或交易指令。
- 新闻证据必须保存原始链接、内容哈希、发布时间、首次获取时间和修订时间。
- 研究必须避免未来信息、删帖幸存偏差、重复转载和实体映射错误。
- BettaFish 的仓库许可文件混合了多种许可文本和非商业限制，在澄清前只能
  标记为 `reference_only` 与 `license_review_required`。
- MiroFish 的 AGPL-3.0 义务需要在部署或改造前单独评审。

候选存储位置：

```text
externals/intelligence-engines/bettafish
externals/simulation-engines/mirofish
```

上游资料：

- <https://github.com/666ghj/BettaFish>
- <https://github.com/666ghj/MiroFish>
- <https://raw.githubusercontent.com/666ghj/BettaFish/main/LICENSE>
- <https://raw.githubusercontent.com/666ghj/MiroFish/main/LICENSE>

## 七、当前状态矩阵

| 工作流 | 状态 |
| --- | --- |
| quantools 元工作区和职责边界 | 已完成 |
| 第三方源码分层与固定版本 | 已完成 |
| Qlib、VectorBT、LEAN 等核心项目纳入 | 已完成 |
| Paper2Quant 独立仓库 | 已完成 |
| Paper2Quant 0.1.0 离线暂存基线 | 已完成 |
| Open Science 纳入 | 已完成并固定版本 |
| Paper2Quant 0.2 确定性纵向切片 | 已实现并通过测试 |
| Paper2Quant AI 原生多模型架构 | 已批准并记录，远程模型部分尚未实现 |
| Kimi / DeepSeek Model Gateway | 尚未实现 |
| Paper2Quant MCP | 尚未实现 |
| qmtq 与三类量化引擎适配器 | 契约已明确，尚未实现 |
| 开源能力登记与孵化基础治理 | 已完成 |
| Serenity 方法库固定与初步边界评估 | 已完成，处于孵化状态 |
| StockAgent 与 ValueCell 受控源码纳入 | 已固定并记录评估，仅供参考、仍待审 |
| BettaFish / MiroFish 价值与边界评估 | 已完成 |
| BettaFish / MiroFish 版本固定与集成 | 尚未执行 |

## 八、建议的下一阶段

1. 为 Serenity 方法建立历史主题评测集和第一方输出契约。
2. 完成 BettaFish 许可审查，再决定是否仅固定源码供参考。
3. 实现 Paper2Quant Model Gateway 与窄 MCP 工具面。
4. 实现 qmtq 与 Qlib、VectorBT、LEAN 的第一方适配器。
5. 用一个 A 股政策或公司事件完成研究、验证、回测和审计的端到端试点。
