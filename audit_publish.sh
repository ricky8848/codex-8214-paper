#!/usr/bin/env bash
# audit_publish.sh — 发布前全量法律/合规审计(2026-11-01)
# 用法: bash paper/audit_publish.sh  (任一 FAIL 则退出码 1, 禁止发布)
set -u
cd "$(dirname "$0")/.." || exit 2
R=0
ok()   { echo "PASS  $1"; }
bad()  { echo "FAIL  $1"; R=1; }
warn() { echo "WARN  $1"; }
tmpf=$(mktemp)

echo "=== A. 宿主进程控制残留(红线①) ==="
git ls-files 'src/*' 'deploy/*' > "$tmpf"
# 排除纯注释行(// #)后检测实际命令调用
if xargs -a "$tmpf" grep -hE "osascript|pkill|killall|remote-debugging" 2>/dev/null | grep -vE "^[[:space:]]*(//|#)" | grep -q .; then
  xargs -a "$tmpf" grep -nE "osascript|pkill|killall|remote-debugging" 2>/dev/null | grep -vE ":[0-9]+:[[:space:]]*(//|#)" | head -10 | sed 's/^/  HIT /'
  bad "src/ 或 deploy/ 中仍有宿主进程控制命令(osascript/pkill/killall/remote-debugging)"
else
  ok "src/ + deploy/ 无任何宿主进程控制命令(代码级)"
fi
if [ -e src/server/__8215cdp.mjs ]; then bad "__8215cdp.mjs 仍存在(应已删除)"; else ok "CDP 驱动模块 __8215cdp.mjs 已删除"; fi
if [ -e deploy/launchd/codex-host-launcher.sh ]; then bad "launcher 脚本仍存在(应已删除)"; else ok "launcher 代启脚本已删除"; fi
if [ -e deploy/launchd/com.ricky.chatgpt-cdp.plist ]; then bad "chatgpt-cdp plist 仍存在(应已删除)"; else ok "chatgpt-cdp launchd 登录项已删除"; fi

echo "=== B. 密钥/凭据泄漏(红线②) ==="
git ls-files '*.py' '*.js' '*.mjs' '*.ts' '*.vue' '*.md' '*.html' > "$tmpf"
if xargs -a "$tmpf" grep -lE "sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|xoxb-|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|EC) PRIVATE" 2>/dev/null | grep -q .; then
  xargs -a "$tmpf" grep -lnE "sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|xoxb-|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|EC) PRIVATE" 2>/dev/null | sed 's/^/  HIT /'
  bad "跟踪文件中疑似硬编码密钥"
else
  ok "git 跟踪文件无硬编码密钥/私钥"
fi

echo "=== C. 工作区卫生(防误提交) ==="
if git status --porcelain | grep -q .; then
  bad "git 工作区不干净: $(git status --porcelain | wc -l | tr -d ' ') 个未提交变更"
else
  ok "git 工作区干净"
fi

echo "=== D. 论文文件完整性 ==="
for f in paper/8214-双向同步架构-论文.pdf paper/8214-thesis-EN.pdf paper/8214-8214双向同步架构-使用说明书.pdf; do
  [ -s "$f" ] && ok "$f 存在 ($(du -h "$f" | cut -f1))" || bad "$f 缺失(需重新打印)"
done

echo "=== E. 论文引用与法律声明 ==="
grep -q "openai/codex" paper/build_thesis.py paper/build_thesis_en.py 2>/dev/null && ok "引用 [1] openai/codex 出处在位" || bad "论文缺少 openai/codex 出处引用"
grep -q "0009-0002-6382-0711" paper/build_thesis.py paper/README-PUBLISH.md && ok "中文版/发布文档含作者 ORCID(0009-0002-6382-0711)" || bad "论文版式缺 ORCID(中文 PDF 版式需补)"
grep -qi "Legal Statement" paper/thesis_en.html && ok "英文版含法律声明" || bad "英文版缺法律声明"
grep -q "ricky8848" paper/thesis_en.html && ok "英文版含作者 ricky8848 + issue tracker 联系方式" || bad "英文版缺作者联系方式"

echo "=== F. 暴露面(红线⑥) ==="
grep -q "127.0.0.1" src/server/__8215syncHub.mjs && ok "hub 绑定 127.0.0.1 回环" || bad "hub 未绑回环"

echo
rm -f "$tmpf"

if [ "$R" -eq 0 ]; then echo "AUDIT PASS — 可发布"; else echo "AUDIT FAIL — 禁止发布, 先修复上述 FAIL 项"; fi
exit $R
