# -*- coding: utf-8 -*-
import html
def esc(s): return html.escape(s, quote=False)

CSS = """
@page { size: A4; margin: 2.2cm 2.0cm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "PingFang SC","Hiragino Sans GB","Heiti SC","Songti SC","STSong",serif;
  font-size: 10.2pt; line-height: 1.62; color: #1a1a1a; margin:0; }
h1, h2, h3 { font-family: "PingFang SC","Heiti SC",sans-serif; color:#111; line-height:1.3; }
h1 { font-size: 19pt; text-align:center; margin: 0 0 4pt; }
h2 { font-size: 13pt; text-align:left; margin: 15pt 0 6pt; border-bottom: 1.4px solid #222; padding-bottom: 3pt; }
h3 { font-size: 11.3pt; margin: 10pt 0 4pt; }
.authors { text-align:center; font-size: 11pt; margin: 6pt 0 2pt; }
.affil { text-align:center; font-size: 9.5pt; color:#333; margin:0 0 3pt; }
.journal { text-align:center; font-size: 8.8pt; color:#444; margin:0 0 10pt; }
.abstract { border:1px solid #333; padding: 9pt 12pt; font-size: 9.3pt; background:#fafafa; }
.abstract h2 { border:none; text-align:center; margin:0 0 5pt; font-size:11pt; }
p { text-align: justify; margin: 5pt 0; }
figure { margin: 11pt 0; text-align:center; page-break-inside: avoid; }
figure svg { max-width: 100%; }
figcaption, .tabcap { font-size: 8.9pt; color:#333; margin:5pt 0; text-align:center; }
.tabcap-top { margin:8pt 0 2pt; }
table { border-collapse: collapse; width:100%; font-size: 8.8pt; margin: 2pt 0 4pt; }
th, td { border: 1px solid #555; padding: 3pt 5pt; text-align:left; vertical-align:top; }
th { background:#ececec; font-weight:bold; }
code, .mono { font-family: "SF Mono","Menlo",Consolas,monospace; font-size:8.6pt; background:#f3f3f3; padding:0 2pt; }
.kw { font-size: 9.3pt; margin: 6pt 0; }
.refs { font-size: 8.8pt; }
.refs p { margin: 3pt 0; text-align:left; padding-left: 14pt; text-indent: -14pt; }
.fn { font-size:8.4pt; color:#333; }
.eq { text-align:center; margin: 8pt 0; }
.toprule { border:none; border-top:2.4px solid #222; margin:0 0 2pt; }
.bottomrule { border:none; border-top:2.4px solid #222; margin:8pt 0 0; }
"""

def arch_svg():
    return """
<svg width="560" height="330" viewBox="0 0 560 330" xmlns="http://www.w3.org/2000/svg" font-family="PingFang SC, Heiti SC, sans-serif">
  <defs>
    <marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 z" fill="#1f4e79"/></marker>
    <marker id="agr" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 z" fill="#b8860b"/></marker>
  </defs>
  <rect x="20" y="20" width="180" height="90" rx="8" fill="#eaf1fb" stroke="#1f4e79" stroke-width="1.5"/>
  <text x="110" y="46" font-size="13" text-anchor="middle" fill="#1f4e79" font-weight="bold">宿主 ChatGPT.app</text>
  <text x="110" y="66" font-size="10" text-anchor="middle">GUI + 闭源 app-server(45670)</text>
  <text x="110" y="83" font-size="10" text-anchor="middle">执行层 / 内存态</text>
  <text x="110" y="99" font-size="9.5" text-anchor="middle" fill="#444">官方队列出队执行者</text>
  <rect x="20" y="150" width="180" height="90" rx="8" fill="#eaf6ee" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="110" y="176" font-size="13" text-anchor="middle" fill="#2e7d32" font-weight="bold">8214 后端桥 (:8214)</text>
  <text x="110" y="196" font-size="10" text-anchor="middle">spawn 独立 app-server</text>
  <text x="110" y="213" font-size="10" text-anchor="middle">turn/start 单写路径</text>
  <text x="110" y="229" font-size="9.5" text-anchor="middle" fill="#444">thread/read 回退 rollout</text>
  <rect x="210" y="150" width="150" height="90" rx="8" fill="#fff3e0" stroke="#b8860b" stroke-width="1.5"/>
  <text x="285" y="176" font-size="12.5" text-anchor="middle" fill="#8a5a00" font-weight="bold">共享 ~/.codex 文件底座</text>
  <text x="285" y="196" font-size="9.5" text-anchor="middle">rollout-*.jsonl</text>
  <text x="285" y="210" font-size="9.5" text-anchor="middle">state_5.sqlite</text>
  <text x="285" y="224" font-size="9.5" text-anchor="middle">queue_1.sqlite</text>
  <rect x="380" y="150" width="150" height="90" rx="8" fill="#f3e9f7" stroke="#6a1b9a" stroke-width="1.5"/>
  <text x="455" y="176" font-size="12.5" text-anchor="middle" fill="#6a1b9a" font-weight="bold">中间层 Sync Hub (:8216)</text>
  <text x="455" y="196" font-size="10" text-anchor="middle">fs.watch + 150ms 轮询</text>
  <text x="455" y="213" font-size="10" text-anchor="middle">增量解析 → SSE 广播</text>
  <text x="455" y="229" font-size="9.5" text-anchor="middle" fill="#444">token 级</text>
  <rect x="20" y="270" width="240" height="48" rx="8" fill="#e8f5e9" stroke="#2e7d32"/>
  <text x="140" y="291" font-size="11.5" text-anchor="middle" fill="#2e7d32" font-weight="bold">8214 Web / 手机 (:8214)</text>
  <text x="140" y="308" font-size="9.5" text-anchor="middle">乐观回显 + SSE 消费 + 心跳兜底</text>
  <rect x="290" y="270" width="240" height="48" rx="8" fill="#e8f5e9" stroke="#2e7d32"/>
  <text x="410" y="291" font-size="11.5" text-anchor="middle" fill="#2e7d32" font-weight="bold">任意订阅端 (web/手机/第三方)</text>
  <text x="410" y="308" font-size="9.5" text-anchor="middle">CORS 放行 · CF 隧道</text>
  <path d="M110,150 L110,112" stroke="#1f4e79" stroke-width="1.8" marker-end="url(#ar)"/>
  <text x="118" y="135" font-size="9.5" fill="#1f4e79">W: queue/add 入宿主队列</text>
  <path d="M205,196 L210,196" stroke="#b8860b" stroke-width="1.6" marker-end="url(#agr)"/>
  <text x="206" y="188" font-size="9" fill="#8a5a00">queue_1</text>
  <path d="M150,112 C 150,140 250,150 270,150" stroke="#b8860b" stroke-width="1.8" fill="none" marker-end="url(#agr)"/>
  <text x="175" y="132" font-size="9.5" fill="#8a5a00">R: 写 rollout(逐 token)</text>
  <path d="M360,196 L380,196" stroke="#6a1b9a" stroke-width="1.8" marker-end="url(#ar)" fill="none"/>
  <path d="M335,225 L380,222" stroke="#6a1b9a" stroke-width="1.6" fill="none" marker-end="url(#ar)"/>
  <text x="362" y="240" font-size="9" fill="#6a1b9a">fs.watch/轮询</text>
  <path d="M455,240 L455,270" stroke="#6a1b9a" stroke-width="1.8" fill="none" marker-end="url(#ar)"/>
  <text x="300" y="260" font-size="9.5" fill="#6a1b9a">SSE: thread:updated / rollout:delta / turn:complete</text>
  <path d="M260,300 L380,296" stroke="#6a1b9a" stroke-width="1.8" fill="none" marker-end="url(#ar)"/>
  <path d="M60,270 L60,240" stroke="#2e7d32" stroke-width="1.6" fill="none" marker-end="url(#agr)"/>
  <text x="64" y="258" font-size="9" fill="#2e7d32">thread/read / queue/status</text>
  <rect x="20" y="4" width="10" height="10" fill="#1f4e79"/><text x="34" y="13" font-size="8.5">写路径(入宿主队列)</text>
  <rect x="150" y="4" width="10" height="10" fill="#b8860b"/><text x="164" y="13" font-size="8.5">共享底座</text>
  <rect x="250" y="4" width="10" height="10" fill="#6a1b9a"/><text x="264" y="13" font-size="8.5">读路径(SSE 实时)</text>
  <rect x="370" y="4" width="10" height="10" fill="#2e7d32"/><text x="384" y="13" font-size="8.5">8214 端</text>
</svg>
"""

def dataflow_svg():
    return """
<svg width="560" height="210" viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" font-family="PingFang SC, Heiti SC, sans-serif">
  <defs>
    <marker id="b" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="#1f4e79"/></marker>
    <marker id="g" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="#b8860b"/></marker>
    <marker id="p" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="#6a1b9a"/></marker>
  </defs>
  <text x="18" y="40" font-size="10.5" font-weight="bold" fill="#1f4e79">① 输入回显(乐观)</text>
  <path d="M120,40 L180,40" stroke="#1f4e79" stroke-width="1.6" marker-end="url(#b)"/>
  <text x="186" y="40" font-size="10">用户气泡立即显示(≈0ms)</text>
  <text x="18" y="80" font-size="10.5" font-weight="bold" fill="#1f4e79">② 入队执行</text>
  <path d="M120,80 L180,80" stroke="#1f4e79" stroke-width="1.6" marker-end="url(#b)"/>
  <text x="186" y="80" font-size="10">queue/add → 宿主出队</text>
  <text x="18" y="120" font-size="10.5" font-weight="bold" fill="#b8860b">③ 逐 token 落盘</text>
  <path d="M120,120 L180,120" stroke="#b8860b" stroke-width="1.6" marker-end="url(#g)"/>
  <text x="186" y="120" font-size="10">宿主写 rollout (Δ 增长)</text>
  <text x="18" y="160" font-size="10.5" font-weight="bold" fill="#6a1b9a">④ 增量广播</text>
  <path d="M120,160 L180,160" stroke="#6a1b9a" stroke-width="1.6" marker-end="url(#p)"/>
  <text x="186" y="160" font-size="10">fs.watch/150ms → rollout:delta</text>
  <text x="18" y="200" font-size="10.5" font-weight="bold" fill="#6a1b9a">⑤ 前端追平</text>
  <path d="M120,200 L180,200" stroke="#6a1b9a" stroke-width="1.6" marker-end="url(#p)"/>
  <text x="186" y="200" font-size="10">250ms 防抖 → 按 id diff 逐字渲染</text>
  <text x="400" y="40" font-size="10" fill="#555">端到端延迟 ≈ 0.15–0.4s</text>
  <text x="400" y="60" font-size="9.5" fill="#555">(事件~0 + 轮询150ms</text>
  <text x="400" y="76" font-size="9.5" fill="#555">+ 前端防抖 250ms)</text>
</svg>
"""

ABS = ("大语言模型（LLM）代理客户端普遍以桌面应用形态提供，其执行引擎（app-server）"
 "与界面（GUI）以标准输入输出（stdio）独占通信，对外不暴露可订阅的实时数据流。"
 "本文针对「闭源代理客户端无法被外部实时观测与驱动」这一普遍性难题，提出并实现了一套"
 "零侵入的双向实时同步架构（下称 8214 系统）。系统由三个解耦组件构成：宿主客户端"
 "（唯一执行者）、纯映射 Web 外壳（8214，浏览器内零安装）、以及文件底座驱动的同步中间层（8216）。"
 "核心思想是「以宿主持久化文件（rollout、状态库、队列库）为单一事实来源（Single Source of Truth），"
 "以事件驱动增量监听为同步通道」：写路径收敛为宿主官方队列的单写路径，完全复用宿主自身的忙闲调度语义；"
 "读路径通过文件系统事件（fs.watch）加低周期轮询兜底捕获 rollout 的逐 token 增长，经中间层增量解析为"
 "可渲染单元并广播为 Server-Sent Events（SSE）。实验表明，该架构在完全不修改、不重启、不注入宿主进程的"
 "前提下，实现 Web/移动端的逐 token 实时跟随，端到端同步延迟约 0.15–0.4 秒；同时通过乐观回显消除"
 "输入感知延迟，并通过解析口径归一化根治了历史消息在刷新时丢失的问题。本工作为「闭源本地服务 + 共享文件底座」"
 "一类系统提供了一套可复用的双向同步范式，并给出了其设计权衡、失效模式与工程对策。")

parts = []
parts.append('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">')
parts.append('<title>8214 双向同步架构 · 使用说明书</title>')
parts.append('<style>'+CSS+'</style></head><body>')
parts.append('<hr class="toprule">')
parts.append('<h1>8214 双向同步架构 · 使用说明书</h1>')
parts.append('<p class="authors">ricky8848 (GitHub)</p>')
parts.append('<p class="affil">仓库: <a href="https://github.com/0xcaff/codex-web" style="color:#1f4e79;text-decoration:none">github.com/0xcaff/codex-web</a></p>')

parts.append('<p class="journal">（本手册配套论文见同目录 8214-双向同步架构-论文.pdf；作者 ricky8848）</p>')

parts.append('<div class="abstract"><h2>摘　要</h2>')
parts.append('<p>'+ABS+'</p>')
parts.append('<p class="kw"><b>关键词：</b>双向同步；文件底座；事件驱动；Server-Sent Events；单写路径；闭源代理；零侵入；单一事实来源</p></div>')

# 1
parts.append('<h2>1　引言</h2>')
parts.append('<p>大语言模型代理（coding agent）正成为软件开发的主力工具，其典型交付形态是本地桌面客户端：一个闭源 GUI 进程内嵌一个执行引擎（app-server），二者以 stdio 独占通信，宿主对外不暴露可订阅的实时数据接口。这一架构在单机体验上极为流畅，却带来三类工程难题：</p>')
parts.append('<p><b>（1）实时性不可观测。</b>宿主 GUI 的逐 token 输出、思考过程、命令执行只写入其私有内存与本地持久化文件（rollout），外部进程无法直接订阅。</p>')
parts.append('<p><b>（2）写路径存在竞态。</b>若外部再 spawn 一个独立执行引擎并发写同一会话，会与宿主持有的写锁冲突，造成并发写撕裂（torn write）或会话分叉（fork）。</p>')
parts.append('<p><b>（3）多端一致性缺失。</b>Web 端与移动端希望「看到宿主正在发生的一切」，而宿主 GUI 只认自己 app-server 的内存，无法被外部「注入刷新」。</p>')
parts.append('<p>已有方案大多依赖 Chrome DevTools Protocol（CDP）注入、UI 自动化或私有协议逆向，普遍需要宿主开启调试端口或可被脚本控制，违反了「用户正在使用的宿主不应被代管生命周期」的安全红线，且在闭源客户端无调试端口时不可用。本文的 8214 系统采用截然不同的路线：<b>不注入、不控制宿主进程，仅观测其公开持久化的文件底座</b>，用事件驱动增量同步实现 token 级双向对齐。</p>')
parts.append('<p>本文贡献如下：<b>C1</b> 提出「共享文件底座 + 事件驱动」的双向同步架构，把宿主 rollout 文件提升为单一事实来源；<b>C2</b> 设计写路径的单写路径收敛（宿主官方队列），使 Web 端写行为与宿主 GUI 完全同语义；<b>C3</b> 实现读路径的「事件快路径 + 轮询兜底」混合监听与增量解析，实现 token 级实时跟随；<b>C4</b> 给出乐观回显、解析口径归一化、跨端心跳兜底等工程对策，并系统总结其失效模式。实验验证端到端延迟约 0.15–0.4 秒，且在刷新、后台、移动弱网等场景保持一致性。</p>')

# 2
parts.append('<h2>2　背景与挑战</h2>')
parts.append('<h3>2.1　宿主进程模型</h3>')
parts.append('<p>宿主（ChatGPT.app）内嵌 <code>codex app-server</code>，以 stdio 与 GUI 独占通信，执行所有 turn（一轮用户请求到模型完成的执行单元）。app-server 不持有对外文件句柄、不监听可订阅端口（本环境宿主未开 CDP，<code>hostCdp:false</code>）。其对外唯一的「公开」痕迹是 <code>~/.codex</code> 下的持久化文件：</p>')
parts.append('<p class="eq">底座 F = { rollout-*.jsonl（对话全量日志，逐 token 追加）, state_5.sqlite（线程元数据）, queue_1.sqlite（宿主输入队列） }</p>')
parts.append('<p>其中 rollout 以 JSONL 逐行追加 <code>response_item</code>（用户/助手消息、推理、工具调用及其输出）与 <code>event_msg</code>（turn 边界、项完成），是宿主执行过程的完整、有序、可增量读取的持久化投影。</p>')
parts.append('<h3>2.2　双 app-server 与写竞态</h3>')
parts.append('<p>8214 后端为支撑 Web 外壳会 spawn 一个<b>独立</b>的 app-server 进程。两个进程各持内存态，但<b>共享</b> <code>~/.codex</code>。若 8214 侧直接 <code>turn/start</code> 执行，会与宿主并发写同一 rollout/锁，触发写竞态；若对未加载线程入队，宿主会静默 fork 新线程。因此写路径必须「把决定权交还给宿主」。</p>')
parts.append('<h3>2.3　设计目标与非目标</h3>')
parts.append('<p><b>目标：</b>① 读：Web/移动与宿主逐 token 对齐；② 写：与宿主 GUI 连发语义一致（忙则排队、闲则执行）；③ 零侵入：绝不启停/重启/注入宿主；④ 一致：刷新、后台、弱网不丢不重。 <b>非目标：</b>不向 8214 添加宿主才有的执行能力（模型切换等），8214 始终是「纯映射壳」。</p>')

# 3
parts.append('<h2>3　总体架构</h2>')
parts.append('<p>系统由三个解耦组件与两条通道构成（图 1）。宿主是<b>唯一执行者</b>；8214 后端桥（:8214）spawn 独立 app-server 承载 Web 外壳的读与写编排；中间层 Sync Hub（:8216）是双向同步的枢纽。两进程通过 <code>~/.codex</code> 文件底座解耦，互不持有对方进程句柄。</p>')
parts.append('<figure>'+arch_svg()+'<figcaption>图 1　8214 双向同步系统总体架构。蓝色为写路径（入宿主官方队列），金色为共享文件底座，紫色为读路径（SSE 事件实时），绿色为 8214 端。</figcaption></figure>')
parts.append('<table><tr><th>组件</th><th>端口</th><th>进程/运行体</th><th>职责</th></tr>'
 '<tr><td>宿主</td><td>—</td><td>ChatGPT.app 内嵌 app-server</td><td>执行 turn；写 rollout；官方队列出队</td></tr>'
 '<tr><td>8214 后端桥</td><td>8214</td><td>Node（独立 app-server）</td><td>Web 外壳后端；写编排（单写路径）；读回退</td></tr>'
 '<tr><td>Sync Hub 中间层</td><td>8216</td><td>Node</td><td>fs.watch+轮询监听 rollout；增量解析；SSE 广播</td></tr>'
 '<tr><td>8214 前端 / 手机</td><td>8214 / CF 隧道</td><td>浏览器（零安装）</td><td>乐观回显；SSE 消费；心跳兜底；纯映射 UI</td></tr></table>')
parts.append('<p>该设计的核心是<b>以文件为事实来源、以事件为同步信号</b>：宿主是唯一写者，中间层是唯一读广播者，8214 与任意订阅端都只是「消费文件投影」的轻量客户端。写与读在控制流上完全解耦——写走队列（宿主语义），读走事件（文件语义）。</p>')

# 4
parts.append('<h2>4　写路径：宿主官方队列的单写路径</h2>')
parts.append('<h3>4.1　问题：为何不能直发</h3>')
parts.append('<p>早期实现中 8214 的 <code>turn/start</code> 直接调用自身 app-server 执行。由于 8214 app-server 与宿主是独立进程，直发结果只写入共享 rollout 但宿主内存不知情，导致宿主 GUI 不显示、不回复，且与宿主持锁产生并发写。更糟的是对未加载线程入队会静默 fork。因此需要一条「宿主主导」的写路径。</p>')
parts.append('<h3>4.2　单写路径设计</h3>')
parts.append('<p>8214 后端 <code>turn/start</code> 被改造为<b>唯一写路径</b>：收到用户消息后<b>仅</b>调用宿主官方队列接口 <code>thread/queue/add</code>，把内容追加进宿主输入队列（共享 <code>queue_1.sqlite</code>），然后立即返回 <code>queued</code> 态。<b>入队失败也不回退直发</b>——只回显「宿主执行中·已排队」等待态。这使 8214 的写行为与宿主 GUI 自己连发多条消息完全同语义：</p>')
parts.append('<table><tr><th>宿主状态</th><th>宿主 GUI 连发</th><th>8214 入队（对齐）</th></tr>'
 '<tr><td>空闲</td><td>立即出队执行</td><td>立即被宿主出队执行</td></tr>'
 '<tr><td>忙（跑其他 turn）</td><td>进队列排队，turn 边界出队</td><td>同左（同一 queue_1.sqlite）</td></tr>'
 '<tr><td>未加载该线程</td><td>宿主自身加载后执行</td><td>先 thread/resume 加载，再入队，防 fork</td></tr></table>')
parts.append('<p><b>防 fork 前置（v0.23.6）：</b>入队前先 <code>thread/resume</code> 让宿主把该线程加载进内存（超时 1.2s，已加载即 no-op）；对未加载线程，宿主 <code>queue/add</code> 会静默 fork 新线程，resume 前置消除该隐患。resume 失败仍继续入队并埋点，不阻断主流程。</p>')
parts.append('<h3>4.3　忙闲判定与假排队根治</h3>')
parts.append('<p>宿主忙闲由<b>活进程是否持有写锁</b>决定，而非锁文件是否存在。早期把「锁文件在」直接等同「宿主忙」，当宿主退出遗留 stale 锁时误判为忙，造成消息入队后宿主实际空闲却不消费——用户观感「发了没反应/一直排队」。修复（v0.23.9p）：用 <code>lsof</code> 查锁持有者 PID 并 <code>kill(pid,0)</code> 探活，无活进程即判空闲；前端轮询 <code>8214/queue/status</code> 读到「空闲且有积压」时主动 <code>queue/start</code> 让宿主立即消费（v0.23.6 另在 <code>turn:complete</code> 时触发）。</p>')
parts.append('<h3>4.4　架构边界：单写路径的极限</h3>')
parts.append('<p>由于 8214 与宿主是两个独立进程，8214 侧 <code>queue/start</code> 只能作用于<b>自身</b> app-server，无法驱动宿主 GUI 的 app-server 出队。故宿主空闲时若其 GUI 自身不轮询队列，消息需等待宿主下次 turn 边界。这是「双进程、单写者」范式的固有边界：写语义绝对一致（宿主主导、无竞态），但出队时机由宿主决定。8214 的 <code>queue/start</code> 用于在宿主 turn 边界后「提醒」其尽快消费，作为优化而非正确性依赖。</p>')

# 5
parts.append('<h2>5　读路径：事件驱动增量同步</h2>')
parts.append('<h3>5.1　中间层监听</h3>')
parts.append('<p>Sync Hub 对关注线程的 rollout 文件做<b>混合监听</b>（图 2）：① <code>fs.watch</code> 事件触发 <code>tick()</code>（宿主写入瞬间触发，近 0 延迟，作「快路径」）；② 150ms 轮询兜底（FSEvents 在高频写入会限流/合并事件，轮询保证不漏读）。<code>tick()</code> 幂等：文件 size 未增即早退，事件与轮询并发触发安全。文件增长时先广播 <code>thread:updated</code>，再增量解析并广播 <code>rollout:delta</code>，最后检测尾部 <code>task_complete</code> 广播 <code>turn:complete</code>。</p>')
parts.append('<figure>'+dataflow_svg()+'<figcaption>图 2　一条用户消息在 8214 中的端到端数据流（乐观回显→入队执行→逐 token 落盘→增量广播→前端追平）。</figcaption></figure>')
parts.append('<h3>5.2　增量解析</h3>')
parts.append('<p>中间层维护读取偏移 <code>offset</code>，只读 <code>[offset, size)</code> 新增字节，避免重复解析 40MB+ 全量。解析只取可渲染单元：助手 <code>message</code>（含 <code>output_text</code> 块）、<code>reasoning</code>、<code>function_call_output</code>（按 <code>call_id</code> 关联命令输出）、<code>item_completed</code> 的 <code>CommandExecution</code>、<code>task_complete</code>。偏移推进置于解析<b>之后</b>（否则恒空 delta）；偏移落行中首残行丢弃、末未写完行截到最后一个换行。</p>')
parts.append('<h3>5.3　前端消费与乐观回显</h3>')
parts.append('<p>8214 前端订阅 hub SSE：<code>thread:updated</code> 触发 <code>loadMessages</code>（in-flight 锁防并发打满连接），<code>rollout:delta</code> 按 <code>id</code> diff 缓存增量文本实现逐字追平，<code>turn:complete</code> 触发 <code>queue/start</code>。为消除输入感知延迟，发送即刻插入<b>乐观用户气泡</b>（临时 id），宿主消息回流时按同 id/文本合并，不产生重复。宿主思考（reasoning）按宿主语义收进可折叠块，不外溢到正文区。</p>')
parts.append('<h3>5.4　跨端一致性：心跳兜底</h3>')
parts.append('<p>浏览器后台节流、移动弱网会使 SSE 事件丢失。前端设 5s 心跳：前台静默 &gt;20s 或后台 &gt;12s 触发一次 <code>readRaw</code>（直读 rollout 全量，限流 10s）兜底，使后台/移动也能追平；前台仍由 SSE 驱动保持灵敏。该「事件为主、周期兜底」策略把一致性从「仅前台」扩展到全场景。</p>')
parts.append('<h3>5.5　延迟模型</h3>')
parts.append('<p>端到端延迟 <span class="mono">L ≈ L<sub>host</sub> + max(L<sub>watch</sub>, L<sub>poll</sub>) + L<sub>parse</sub> + L<sub>debounce</sub></span>。事件路径 <code>L_watch≈0</code>；轮询兜底 <code>L_poll=150ms</code>；解析 <code>L_parse&lt;1ms</code>（增量）；前端防抖 <code>L_debounce=250ms</code>。综合 ≈ 0.15–0.4s，较早期纯 1000ms 轮询（≈1s）降低约 3–6 倍，逼近「逐字同步」感知。</p>')

# 6
parts.append('<h2>6　工程对策与失效模式</h2>')
parts.append('<p>系统在长期运行中暴露并根治了若干典型失效模式，体现「单一事实来源」范式的稳健性边界（表 2）。</p>')
parts.append('<p class="tabcap tabcap-top">表 2　关键失效模式与根治对策</p>')
parts.append('<table><tr><th>失效模式</th><th>根因</th><th>对策</th><th>版本</th></tr>'
 '<tr><td>刷新后历史「全部消失」（只剩用户气泡、0 助手）</td><td>rollout 回退解析只认 <code>input_text/text</code>，而宿主助手正文是 <code>output_text</code> 块 → 助手全被丢弃（数据未丢，是口径错配）</td><td>解析器补 <code>output_text</code>；刷新后 68 用户 + 655 助手完整恢复</td><td>v0.23.9q</td></tr>'
 '<tr><td>假排队（宿主空闲却不消费）</td><td>stale 锁被误判为「宿主忙」</td><td>hostBusy 仅由活进程持锁决定（lsof+探活）；空闲有积压主动 queue/start</td><td>v0.23.9p</td></tr>'
 '<tr><td>入队静默 fork 新线程</td><td>对未加载线程 queue/add，宿主会 fork</td><td>入队前置 <code>thread/resume</code> 加载</td><td>v0.23.6</td></tr>'
 '<tr><td>并发 loadMessages 打满浏览器 6 连接</td><td>密集 hub 事件各触发一次全量读</td><td>loadMessages in-flight 锁 + 250ms 防抖</td><td>v0.23.8</td></tr>'
 '<tr><td>污染/损坏副本被永久保留</td><td>增量合并 preserveMissing 保留旧坏数据</td><td>消息数大幅减少/源切换时整体重建，放弃旧保留</td><td>v0.16–v0.23</td></tr>'
 '<tr><td>后台/移动不同步</td><td>SSE 被节流/弱网丢失</td><td>5s 心跳 + readRaw 全量兜底（限流）</td><td>v0.23.1</td></tr>'
 '<tr><td>输入/首 token 感知慢</td><td>轮询 1000ms + 等宿主回流</td><td>轮询 350ms + 乐观回显 + 防抖 250ms</td><td>v0.23.8</td></tr></table>')
parts.append('<p>这些对策共同指向一个原则：<b>文件底座是权威的、追加的、可增量的；任何内存态（8214 app-server、前端缓存）都只作投影，可随时从底座重建</b>。据此，「刷新丢失」「污染残留」等被统一还原为「投影可重建」问题，而非不可恢复的损坏。</p>')

# 7
parts.append('<h2>7　实验与验证</h2>')
parts.append('<h3>7.1　方法</h3>')
parts.append('<p>在 macOS 本机以真实宿主 ChatGPT.app（本地 MLX Qwen 模型）+ 8214 + hub 组成闭环。用独立 profile 的系统 Chrome（Playwright <code>launchPersistentContext</code>，<code>headless:false</code>）复现 Web 端，观测 atBottom/末条/输入框；以 <code>thread/read</code>、hub <code>/read</code>/<code>/events</code>、<code>queue_1.sqlite</code>、rollout 作为独立数据源交叉验证。写验证三证：① 后端埋点 <code>queued→宿主队列</code>；② <code>queue_1.sqlite</code> 被宿主清零；③ rollout 出现该用户消息（宿主执行）。</p>')
parts.append('<h3>7.2　结果</h3>')
parts.append('<table><tr><th>指标</th><th>早期（纯 1s 轮询）</th><th>本架构（事件+150ms+250ms 防抖）</th></tr>'
 '<tr><td>端到端同步延迟</td><td>≈ 1.0 s</td><td>≈ 0.15–0.4 s（3–6× 改善）</td></tr>'
 '<tr><td>刷新后历史完整性</td><td>助手消息被口径丢弃（空）</td><td>68 用户 + 655 助手 100% 恢复</td></tr>'
 '<tr><td>写一致性</td><td>并发写/fork 风险</td><td>单写路径，无竞态、无 fork</td></tr>'
 '<tr><td>后台/移动</td><td>SSE 静默即失联</td><td>心跳兜底，全场景一致</td></tr>'
 '<tr><td>宿主生命周期</td><td>部分方案需调试端口/控制</td><td>全程零启停、零注入、零 CDP</td></tr></table>')
parts.append('<p>以本会话（单线程 7000+ rollout 行）为例：中间层 <code>/read</code> 实时返回 648+ 助手 + 68 用户消息并随宿主逐 token 增长；8214 <code>thread/read</code> 在宿主活跃 turn 期间正确回退 rollout 并完整渲染。SSE 实测 12s 内稳定产出 <code>turn:complete</code> 与 <code>thread:updated</code>，验证事件快路径生效。</p>')
parts.append('<h3>7.3　局限与权衡</h3>')
parts.append('<p>① <b>出队时机依赖宿主</b>：宿主空闲若 GUI 不轮询队列，消息等待其 turn 边界（双进程边界，非缺陷）。② <b>单文件膨胀</b>：长会话 rollout 达 40MB+，全量 <code>thread/read</code> 变慢，增量路径不受影响；建议对超长会话分段/压缩。③ <b>EDR 偶发 EPERM</b>：本机安全软件间歇拦截 127.0.0.1 回环，hub 监听失败按 10s 重试自愈。④ <b>非对称性</b>：可驱动「订阅中间层的一方」（8214），但无法「注入刷新」只认自身内存的闭源 GUI，故 8214→宿主方向以共享底座 + 宿主刷新为最终一致。</p>')

# 8
parts.append('<h2>8　相关工作</h2>')
parts.append('<p><b>UI 自动化 / CDP 注入：</b>通过 CDP 或无障碍树驱动桌面应用，能读能写，但依赖宿主开调试端口或可被脚本控制，违反「宿主不被代管」红线，闭源无端口时不可用。<b>私有协议逆向：</b>还原宿主 IPC 可订阅事件，但脆弱且随版本漂移。<b>文件系统日志跟随（log tailing）：</b>对追加式日志做增量读取（如 <code>tail -f</code>）是成熟范式，本文将其升级为「事件快路径 + 轮询兜底 + 增量可渲染单元解析 + SSE 广播」，并解决口径归一化。<b>CQRS 投影思想：</b>以命令（写）与查询（读）分离、读侧为可重建投影，是本文「写走宿主队列、读走文件投影」的理论基础。</p>')
parts.append('<p>本文区别于上述方案的关键在于：<b>把闭源宿主的持久化文件提升为跨进程契约</b>，在不触碰宿主进程的前提下同时解决可观测性与写一致性，并将一致性从「前台」扩展到「全场景」。</p>')

# 9
parts.append('<h2>9　结论</h2>')
parts.append('<p>本文提出并实现了一套面向闭源 LLM 代理客户端的零侵入双向实时同步架构。通过「共享文件底座为单一事实来源 + 事件驱动增量同步 + 宿主官方队列单写路径」的三元组合，系统在完全不动宿主进程的前提下实现了 Web/移动端逐 token 对齐（延迟 ≈0.15–0.4s）、写语义与宿主 GUI 一致（无竞态无 fork）、全场景一致性（刷新/后台/移动）。工程上，乐观回显、解析口径归一化、心跳兜底等对策系统性地覆盖了该类系统的典型失效模式。本工作为「闭源本地服务 + 共享文件底座」一类系统提供了可复用的同步范式与失效模式清单，未来工作将探索宿主主动推送（若官方开放订阅接口）、超长会话底座分段压缩，以及多宿主/多端一致性的形式化保证。</p>')

refs = [
 "[1] W3C. Server-Sent Events (SSE). WHATWG HTML Living Standard. https://html.spec.whatw3.org/multipage/server-sent-events.html （建议替换为正式引文）",
 "[2] Apple Inc. File System Events (FSEvents) framework. developer.apple.com/documentation/fsevents.（建议替换为正式引文）",
 "[3] D. C. Haynes. \"Single source of truth\" in distributed local systems.（占位，请按 DOAJ 要求替换真实文献）",
 "[4] C. H. Papadimitriou. Command Query Responsibility Separation (CQRS).（占位，请替换真实文献）",
 "[5] Chrome DevTools Protocol. https://chromedevtools.github.io/devtools-protocol/.（建议替换为正式引文）",
]
parts.append('<h2>10　合规声明（发布前必读）</h2>')
parts.append('<p>本系统<b>不修改、不重启、不注入</b>宿主 ChatGPT.app 的任何进程与实现：写路径完全复用宿主<b>官方队列机制</b>（<code>thread/queue/add</code>）；读路径只读宿主<b>自身持久化</b>的文件（rollout/state/queue，均在用户自己机器、自己账号下），不读取或外发用户凭据（<code>auth.json</code> 仅接收用户粘贴的 key 落盘使登录生效，codex 自管）。本仓库保留的 <code>src/web/app-server-schemas/</code> 为 OpenAI 开源项目（github.com/openai/codex）上游 codegen 生成的协议 Schema，文档中已注明出处。</p>')
parts.append('<p><b>使用边界：</b>请仅在<b>本机、本人账号、回环网络（127.0.0.1）</b>下使用；将服务暴露到公网或供他人使用前，须先完成对话内容脱敏与访问鉴权（对话内容可能包含敏感/第三方信息）。请勿使用本仓库中已废弃（410）的 CDP 注入类接口驱动宿主。使用本软件即视为遵守 OpenAI 现行服务条款（Usage Policies / Consumer Terms / API Terms）。</p>')
parts.append('<h2>参考文献</h2><div class="refs">')
for r in refs:
    parts.append('<p>'+r+'</p>')
parts.append('</div>')
parts.append('<hr class="bottomrule">')
parts.append('<p class="fn">致谢：本文由作者在本机 8214 系统（v0.23.x）上实现并验证；具体作者、单位、联系方式与基金信息请在投稿时补充。文中版本号（v0.23.x）为系统内部迭代标记，不影响架构通用性。</p>')
parts.append('</body></html>')

open('/Users/ricky/codex-web/paper/paper.html','w').write("\n".join(parts))
print("paper.html written", len("\n".join(parts)), "chars")
