# 8214 双向同步架构 — 论文发布版（中英双语）

**Zero-intrusion bidirectional real-time synchronization of a closed-source LLM agent desktop client**

8214 与闭源桌面宿主（ChatGPT.app）共享同一持久层（`~/.codex`）作为单一事实源：读 = 宿主自持久化的追加日志跨进程增量跟随（token 级）；写 = 宿主官方输入队列单写路径（宿主唯一执行者）。零逆向、零注入、零进程代管。

## 文档

| 文件 | 语言 | 说明 |
|------|------|------|
| `8214-bidirectional-sync-thesis-CN.pdf` | 中文 | 论文：理论（Thesis 1–3）+ 架构 + 实现独到性 + OpenAI 标准完备性审计 + 理论验证数据（9 页） |
| `8214-thesis-EN.pdf` | 英文 | 同内容英译（10 页），DOI 主发版 |
| `8214-8214双向同步架构-使用说明书.pdf` | 中文 | 用户使用说明（独立文档，非论文） |

## 作者

**ricky8848** — ORCID [0009-0002-6382-0711](https://orcid.org/0009-0002-6382-0711) · GitHub [github.com/ricky8848](https://github.com/ricky8848)

法律/合规事务请联系：[github.com/0xcaff/codex-web issues](https://github.com/0xcaff/codex-web/issues)

## 构建与审计

- `build_thesis.py` / `build_thesis_en.py` / `build_paper.py` — HTML 生成器（PDF 由 `print_pdfs.mjs` 打印）
- `audit_publish.sh` — 发布前全量法律/合规审计（宿主控制残留 / 密钥泄漏 / 引用声明 / 暴露面）
- `publish.sh` — 发布流程：审计 → 重新生成 → 打包
- `README-PUBLISH.md` — 发布者清单

## 法律声明

本论文为理论描述与验证工作，不修改、不主张所有权 OpenAI 专有宿主应用。OpenAI、ChatGPT、Codex 为 OpenAI, Inc. 商标，此处为名义引用。系统仅用于本机、单用户、回环部署；不读取/传输凭据，不修改或控制宿主进程。公网或多租户部署前须先完成对话内容脱敏与访问鉴权。开源组件（openai/codex 协议 schema）依上游许可证使用并注明出处。
