#!/usr/bin/env bash
# publish.sh — 论文发布流程(2026-11-01)
# 1) 全量法律审计  2) 重新生成三份 PDF  3) 打包 release/  4) 打 git 版本标记
# 原始版本始终保留在 paper/ 目录(随仓库提交); release/ 为发布快照。
set -eu
cd "$(dirname "$0")/.."

echo "[1/4] 全量法律/合规审计..."
bash paper/audit_publish.sh

NODE=/Users/ricky/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node
[ -x "$NODE" ] || NODE=$(command -v node)

echo "[2/4] 重新生成 HTML + PDF(保证发布版=源码最新)..."
python3 paper/build_thesis.py
python3 paper/build_thesis_en.py
python3 paper/build_paper.py
"$NODE" paper/print_pdfs.mjs

echo "[3/4] 打包发布快照 paper/release/..."
rm -rf paper/release
mkdir -p paper/release
cp paper/8214-双向同步架构-论文.pdf paper/8214-thesis-EN.pdf paper/8214-8214双向同步架构-使用说明书.pdf paper/release/
cp paper/build_thesis.py paper/build_thesis_en.py paper/build_paper.py paper/audit_publish.sh paper/publish.sh paper/print_pdfs.mjs paper/README-PUBLISH.md paper/release/ 2>/dev/null || true
cat > paper/release/README.md <<'EOF'
# 8214 双向同步架构 — 发布版(双语)

| 文件 | 说明 |
|------|------|
| 8214-双向同步架构-论文.pdf | 中文论文(理论/架构/实现/验证/合规) |
| 8214-thesis-EN.pdf | 英文论文(同内容英译) |
| 8214-8214双向同步架构-使用说明书.pdf | 用户使用说明(独立文档) |

- 作者: ricky8848 (ORCID 0009-0002-6382-0711; GitHub: github.com/ricky8848)
- 发布前已执行全量法律/合规审计(见 build 脚本 audit_publish.sh)。
- 本包仅含论文与构建脚本; 系统源码见仓库 main 分支(未随论文发布)。
EOF
(cd paper && zip -qr release.zip release && rm -rf release)
ls -la paper/release.zip

echo "[4/4] 完成。提交发布(如需要):"
echo "  git add paper/ && git commit -m 'paper: 发布版打包(审计通过)' && git push"
echo "DOI 发布: 将 paper/release.zip 内三份 PDF 上传 DOI 平台(如 Zenodo/DataCite/OpenAccess), 作者填 ricky8848。"
