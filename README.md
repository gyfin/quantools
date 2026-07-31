# quantools

`quantools` 是一个可复现、可审计的量化研究元工作区。它不重写第三方
引擎，而是固定版本、明确职责，并通过第一方协议与适配层把研究、验证和
执行串联起来。

## 角色分工

| 组件 | 职责 |
| --- | --- |
| qmtq | A 股/QMT 协议、可信数据、run bundle、验证与安全边界 |
| Qlib | 因子、模型和机器学习研究 |
| VectorBT | 批量参数实验与快速想法筛选 |
| LEAN | 撮合、订单、组合、仿真和执行语义 |
| Paper2Quant | 从论文、研报和其他研究来源生成可审计候选方法 |
| quantools | 固定依赖版本并连接上述组件 |

核心原则：

```text
大模型提出和解释研究判断
确定性工具计算与测试
qmtq 验证和准入
人决定是否推广到生产
```

## 当前状态

- 第三方项目位于 `externals/`，以 Git submodule 固定版本。
- 第一方 Paper2Quant 位于 `packages/paper2quant`，拥有独立仓库和生命周期。
- Paper2Quant 0.2 已实现离线、确定性、证据可追溯的 PDF 到 qmtq v2
  候选包纵向切片。
- `D:\qmtq` 保持为独立兄弟仓库，不向研究代理开放实盘权限。
- Paper2Quant 已批准采用 Codex、Kimi、DeepSeek 和统一 MCP 工具面的
  AI 原生多模型目标架构；远程模型网关和 MCP 工具面仍待实现。

## 开源能力接入

quantools 采用“稳定内核、开放能力层、受控孵化”的长期原则。新的开源
项目先登记来源、许可证、固定版本、能力边界和生命周期，再经过隔离评测与
人工批准进入正式研究链。第三方 Skill、Agent 和研究方法不能绕过 qmtq
验证，也不能直接产生已接受信号或交易指令。

首批产业链瓶颈研究方法已作为 `reference_only` 能力固定在
`externals/research-methods/`。孵化规则和评估记录位于
`externals/incubator/`。

详细记录：

- [项目状态台账](docs/project-status.md)
- [第三方依赖管理](externals/README.md)
- [第三方组件清单](externals/manifest.yaml)
- [Paper2Quant 组件说明](packages/README.md)
