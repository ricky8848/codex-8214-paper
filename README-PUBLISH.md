# 论文发布说明(2026-11-01)

## 发布物
| 文件 | 语言 | 用途 |
|------|------|------|
| `8214-双向同步架构-论文.pdf` | 中文 | 理论+架构+实现+验证+合规(9 页) |
| `8214-thesis-EN.pdf` | 英文 | 同内容英译(10 页), DOI 主发版 |
| `8214-8214双向同步架构-使用说明书.pdf` | 中文 | 用户使用说明(独立文档, 非论文) |

作者: **ricky8848** (GitHub: https://github.com/ricky8848; ORCID: https://orcid.org/0009-0002-6382-0711)
法律/合规联系: 仓库 issue tracker https://github.com/0xcaff/codex-web

## 发布前必须执行(发布者清单)
1. `bash paper/publish.sh` — 自动完成: 全量审计 → 重新生成 PDF → 打包 `paper/release.zip`。任一审计 FAIL 则中止。
2. 人工复核(脚本查不了的):
   - [ ] PDF 中无真实对话内容(论文验证数据只用行数/时延/比率, 不含对话正文)。
   - [ ] PDF 中无密钥/邮箱/手机号(联系方式仅 GitHub 用户名 + ORCID)。
   - [ ] 论文对 OpenAI 商标为名义引用(nominative use), 未声称与 OpenAI 有关联/背书。
   - [ ] 平台政策勾选: 本系统为「本机、单用户、回环」用途; 公网/多租户需先脱敏+鉴权(论文 §7.7 已声明)。
3. 上传 DOI 平台(Zenodo / DataCite / OpenAccess 等), 作者=ricky8848, 文件=`paper/release.zip` 内三份 PDF, 附 README.md。
4. 发布后把 DOI 链接回填本文件与 `paper/README.md`。

## 法律要点(论文 §7 已含完整表述)
- 对 OpenAI 闭源宿主: 只读其**自身持久化**文件 + 官方队列写; 不逆向/不注入/不代管进程(代码中已无任何此类路径, CDP 模块与 launcher 整体删除)。
- OpenAI/ChatGPT/Codex 为 OpenAI, Inc. 商标, 名义引用; 不主张所有权、不声称背书。
- 开源组件(openai/codex 协议 schema)依上游许可证使用并注明出处。
- 凭据(~/.codex/auth.json): 仅用户粘贴落盘, 不读取/不外发。
- 暴露面: 当前仅 127.0.0.1 回环; 任何公网化前必须脱敏对话内容 + 访问鉴权。

## 版本管理
- **原始版本**(源 .py 生成器 + PDF)常驻 `paper/` 目录, 随仓库提交(用户要求: 原始版本保存在工作目录)。
- `paper/release/` + `release.zip` 为发布快照; 每次发布重新生成, 不手改 PDF。
