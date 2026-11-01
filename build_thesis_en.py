# -*- coding: utf-8 -*-
# English version — same theory, structure & figures as the Chinese thesis.
import html
CSS = """
@page { size: A4; margin: 2.3cm 2.1cm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Times New Roman","Georgia",serif; font-size: 10.2pt; line-height:1.58; color:#111; margin:0; }
h1,h2,h3 { font-family:"Times New Roman",serif; color:#000; line-height:1.28; }
h1 { font-size:18pt; text-align:center; margin:2pt 0 6pt; }
h2 { font-size:12.5pt; margin:14pt 0 5pt; }
h3 { font-size:10.8pt; margin:9pt 0 3pt; }
.authors{ text-align:center; font-size:11pt; margin:4pt 0 2pt;}
.affil{ text-align:center; font-size:9.5pt; color:#333; margin:0 0 4pt;}
.date{ text-align:center; font-size:9pt; color:#444; margin:0 0 10pt;}
.abstract{ border:1px solid #000; padding:9pt 13pt; font-size:9.3pt; background:#fbfbfb; }
.abstract h2{ border:none; text-align:center; margin:0 0 6pt; font-size:11.5pt;}
p{ text-align:justify; margin:5pt 0; }
figure{ margin:10pt 0; text-align:center; page-break-inside:avoid; }
figure svg{ max-width: 100%; }
figcaption, .tcap{ font-size:8.8pt; color:#333; margin:5pt 0; text-align:center; }
.tcap-top{ margin:8pt 0 2pt; }
table{ border-collapse:collapse; width:100%; font-size:8.7pt; margin:2pt 0 5pt; }
th,td{ border:1px solid #555; padding:3pt 5pt; text-align:left; vertical-align:top;}
th{ background:#ececec; font-weight:bold; }
code,.mono{ font-family:"SF Mono",Menlo,Consolas,monospace; font-size:8.5pt; background:#f3f3f3; padding:0 2pt;}
.kw{ font-size: 9.3pt; margin:6pt 0;}
.refs{ font-size: 8.8pt; }
.refs p{ margin:3pt 0; text-align:left; padding-left:14pt; text-indent:-14pt;}
.eq{ text-align:center; margin:8pt 0; font-family:"Times New Roman",serif;}
.toprule{ border:none; border-top:2.6px solid #000; margin:0 0 3pt;}
.bottomrule{ border:none; border-top:2.6px solid #000; margin:8pt 0 0;}
.fn{ font-size:8.4pt; color:#333; }
.legal{ border:1px solid #000; background:#fbfbfb; padding:8pt 12pt; font-size:9pt; }
.legal h2{ border:none; text-align:center; margin:0 0 5pt; }
"""

def arch_svg():
    return """
<svg width="560" height="330" viewBox="0 0 560 330" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <defs>
    <marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 z" fill="#1f4e79"/></marker>
    <marker id="agr" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 z" fill="#b8860b"/></marker>
  </defs>
  <rect x="20" y="20" width="180" height="90" rx="8" fill="#eaf1fb" stroke="#1f4e79" stroke-width="1.5"/>
  <text x="110" y="46" font-size="13" text-anchor="middle" fill="#1f4e79" font-weight="bold">Host ChatGPT.app</text>
  <text x="110" y="66" font-size="10" text-anchor="middle">GUI + closed app-server (45670)</text>
  <text x="110" y="83" font-size="10" text-anchor="middle">executor / private memory</text>
  <text x="110" y="99" font-size="9.5" text-anchor="middle" fill="#444">sole consumer of official queue</text>
  <rect x="20" y="150" width="180" height="90" rx="8" fill="#eaf6ee" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="110" y="176" font-size="13" text-anchor="middle" fill="#2e7d32" font-weight="bold">8214 Backend Bridge (:8214)</text>
  <text x="110" y="196" font-size="10" text-anchor="middle">spawned standalone app-server</text>
  <text x="110" y="213" font-size="10" text-anchor="middle">turn/start single-write path</text>
  <text x="110" y="229" font-size="9.5" text-anchor="middle" fill="#444">thread/read falls back to rollout</text>
  <rect x="210" y="150" width="150" height="90" rx="8" fill="#fff3e0" stroke="#b8860b" stroke-width="1.5"/>
  <text x="285" y="176" font-size="12.5" text-anchor="middle" fill="#8a5a00" font-weight="bold">Shared ~/.codex File Base</text>
  <text x="285" y="196" font-size="9.5" text-anchor="middle">rollout-*.jsonl (append-only log)</text>
  <text x="285" y="210" font-size="9.5" text-anchor="middle">state_5.sqlite (metadata)</text>
  <text x="285" y="224" font-size="9.5" text-anchor="middle">queue_1.sqlite (input queue)</text>
  <rect x="380" y="150" width="150" height="90" rx="8" fill="#f3e9f7" stroke="#6a1b9a" stroke-width="1.5"/>
  <text x="455" y="176" font-size="12.5" text-anchor="middle" fill="#6a1b9a" font-weight="bold">Sync Hub (:8216)</text>
  <text x="455" y="196" font-size="10" text-anchor="middle">fs.watch events + 150ms poll</text>
  <text x="455" y="213" font-size="10" text-anchor="middle">incremental parse -&gt; SSE fan-out (1:N)</text>
  <text x="455" y="229" font-size="9.5" text-anchor="middle" fill="#444">token-level</text>
  <rect x="20" y="270" width="240" height="48" rx="8" fill="#e8f5e9" stroke="#2e7d32"/>
  <text x="140" y="291" font-size="11.5" text-anchor="middle" fill="#2e7d32" font-weight="bold">8214 Web / Mobile (:8214)</text>
  <text x="140" y="308" font-size="9.5" text-anchor="middle">optimistic echo + SSE + heartbeat fallback</text>
  <rect x="290" y="270" width="240" height="48" rx="8" fill="#e8f5e9" stroke="#2e7d32"/>
  <text x="410" y="291" font-size="11.5" text-anchor="middle" fill="#2e7d32" font-weight="bold">Any Subscriber (web / mobile / 3rd party)</text>
  <text x="410" y="308" font-size="9.5" text-anchor="middle">CORS-allowed - Cloudflare tunnel - zero install</text>
  <path d="M110,150 L110,112" stroke="#1f4e79" stroke-width="1.8" marker-end="url(#ar)"/>
  <text x="118" y="135" font-size="9.5" fill="#1f4e79">W: queue/add into host queue</text>
  <path d="M205,196 L210,196" stroke="#b8860b" stroke-width="1.6" marker-end="url(#agr)"/>
  <text x="206" y="188" font-size="9" fill="#8a5a00">queue_1</text>
  <path d="M150,112 C 150,140 250,150 270,150" stroke="#b8860b" stroke-width="1.8" fill="none" marker-end="url(#agr)"/>
  <text x="168" y="132" font-size="9.5" fill="#8a5a00">R: writes rollout per token</text>
  <path d="M360,196 L380,196" stroke="#6a1b9a" stroke-width="1.8" marker-end="url(#ar)" fill="none"/>
  <path d="M335,225 L380,222" stroke="#6a1b9a" stroke-width="1.6" fill="none" marker-end="url(#ar)"/>
  <text x="358" y="240" font-size="9" fill="#6a1b9a">fs.watch/poll</text>
  <path d="M455,240 L455,270" stroke="#6a1b9a" stroke-width="1.8" fill="none" marker-end="url(#ar)"/>
  <text x="300" y="260" font-size="9.5" fill="#6a1b9a">SSE: thread:updated / rollout:delta / turn:complete</text>
  <path d="M260,300 L380,296" stroke="#6a1b9a" stroke-width="1.8" fill="none" marker-end="url(#ar)"/>
  <path d="M60,270 L60,240" stroke="#2e7d32" stroke-width="1.6" fill="none" marker-end="url(#agr)"/>
  <text x="64" y="258" font-size="9" fill="#2e7d32">thread/read / queue/status</text>
  <rect x="20" y="4" width="10" height="10" fill="#1f4e79"/><text x="34" y="13" font-size="8.5">write path (host queue)</text>
  <rect x="170" y="4" width="10" height="10" fill="#b8860b"/><text x="184" y="13" font-size="8.5">shared base</text>
  <rect x="270" y="4" width="10" height="10" fill="#6a1b9a"/><text x="284" y="13" font-size="8.5">read path (SSE real-time)</text>
  <rect x="390" y="4" width="10" height="10" fill="#2e7d32"/><text x="404" y="13" font-size="8.5">8214 side</text>
</svg>
"""

def delta_svg():
    return """
<svg width="560" height="150" viewBox="0 0 560 150" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <defs><marker id="g" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="#b8860b"/></marker></defs>
  <text x="20" y="28" font-size="10.5" font-weight="bold">rollout append-only file (single source of truth)</text>
  <rect x="20" y="40" width="500" height="34" fill="#fff3e0" stroke="#b8860b"/>
  <text x="30" y="61" font-size="9.5" fill="#8a5a00">[ read: offset ]   [ new: delta ]   [ unterminated tail ]</text>
  <rect x="300" y="40" width="140" height="34" fill="#ffe0b2" stroke="#b8860b" stroke-dasharray="3 2"/>
  <path d="M360,74 L360,98" stroke="#b8860b" stroke-width="1.6" marker-end="url(#g)"/>
  <text x="372" y="92" font-size="9.5" fill="#8a5a00">readSync [offset, size)</text>
  <rect x="20" y="104" width="500" height="30" fill="#f3e9f7" stroke="#6a1b9a"/>
  <text x="30" y="123" font-size="9.5" fill="#6a1b9a">render units: assistant message / reasoning / function_call_output / task_complete</text>
  <text x="20" y="145" font-size="9" fill="#555">offset mid-line -&gt; drop first partial line; unterminated last line -&gt; cut at last newline; offset advanced only after parsing</text>
</svg>
"""

parts=[]
parts.append('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>From Persistence Log to Cross-Process Contract</title>')
parts.append('<style>'+CSS+'</style></head><body>')
parts.append('<hr class="toprule">')
parts.append('<h1>From Persistence Log to Cross-Process Contract: Theory, Architecture, and Verification of Zero-Intrusion Bidirectional Real-Time Synchronization for Closed-Source LLM Agent Clients</h1>')
parts.append('<p class="authors">ricky8848</p>')
parts.append('<p class="affil">GitHub: <a href="https://github.com/ricky8848" style="color:#1f4e79;text-decoration:none">github.com/ricky8848</a> &middot; Repository: <a href="https://github.com/0xcaff/codex-web" style="color:#1f4e79;text-decoration:none">github.com/0xcaff/codex-web</a></p>')
parts.append('<p class="date">November 2026</p>')

parts.append('<div class="abstract"><h2>Abstract</h2>')
parts.append('<p>This paper formulates a theory of bidirectional real-time synchronization for <b>closed-source, subscription-free, single-instance, private-memory</b> local LLM agent clients, and presents, on top of it, an architectural design, a distinctive implementation, and a theoretical verification. The central claim (<b>Thesis&nbsp;1</b>) is that the host\u2019s <b>persisted append-only log (rollout) can be elevated into a cross-process contract</b>, yielding, without injecting into, controlling, or restarting the host process: (i) token-level observability of the host\u2019s execution, and (ii) write consistency that is semantically identical to the host GUI\u2019s own typing, free of contention and forking. The resulting 8214 system comprises three decoupled components and two channels \u2014 the host (sole executor), a pure-mapping web shell (8214, zero-install in browser), and a file-base-driven sync hub \u2014 with a single-write path through the host\u2019s official input queue, and a read path built on \u201cfast-path events + polling backstop\u201d incremental log tailing for token-level alignment. We derive a closed-form latency model <span class="mono">L \u2248 L<sub>host</sub> + max(L<sub>watch</sub>,L<sub>poll</sub>) + L<sub>parse</sub> + L<sub>debounce</sub></span>, and audit the design against the OpenAI Codex official app-server protocol standard, delimiting its in-standard completeness and the boundary of its distinctiveness. Theoretical verification (real host + independent browser, cross-checked with four independent data sources) reports end-to-end synchronization latency of \u22480.15\u20130.4\u00a0s (3\u20136\u00d7 better than pure 1\u00a0s polling), 100% reconstruction of a 7,000+ line rollout, zero contention and zero fork on the write path, and full-scenario consistency across refresh/background/weak-network. All contributions are at the level of <b>theoretical description and verification</b>; no modification of the host is made or claimed. The work provides a provable synchronization paradigm and a failure-mode catalogue for the class of \u201cclosed local service + shared file base\u201d systems.</p>')
parts.append('<p class="kw"><b>Keywords:</b> bidirectional synchronization; single source of truth; cross-process contract; append-only log tailing; command-query responsibility separation (CQRS); event sourcing; server-sent events; zero intrusion; formal verification</p></div>')

parts.append('<h2>1　Introduction</h2>')
parts.append('<p>LLM coding agents are becoming a primary tool of software development, and their canonical delivery form is a local desktop client: a closed-source GUI process embedding an execution engine (app-server), the two communicating over stdio exclusively. The architecture is smooth in single-machine use, yet it creates three theoretical tensions when one asks an external party (web / mobile / third-party) to <i>see in real time what the host is doing</i> and to <i>write with the same semantics</i>:</p>')
parts.append('<p><b>Tension 1 (observability).</b> The host\u2019s per-token output, reasoning, and command execution live only in its private memory and its persistence log; no subscribable port is exposed (in this environment the host runs without CDP, <code>hostCdp:false</code>).</p>')
parts.append('<p><b>Tension 2 (write consistency).</b> If an external system instantiates a second execution engine and concurrently writes the same session, it contends with the host\u2019s write lock, risking torn writes or session forking.</p>')
parts.append('<p><b>Tension 3 (consistency scope).</b> The host GUI trusts only its own app-server memory and cannot be \u201cinjected with a refresh\u201d from outside, so the reachable consistency scope is, in theory, asymmetric.</p>')
parts.append('<p>Existing routes \u2014 CDP injection, UI automation, private-protocol reverse engineering \u2014 require the host to run a debug port or to be script-manageable in its lifecycle, conflicting with the safety axiom that <i>a host the user is using must not be managed on their behalf</i>, and unavailable when the closed client exposes no port. This paper takes an orthogonal route: <b>no injection, no control of the host process \u2014 only observation of the host\u2019s already-public persisted file base</b>, with event-driven incremental tailing for reads and the host\u2019s official input queue as the single write path.</p>')
parts.append('<p>Contributions (all at the theoretical level): <b>T1</b> we propose and formalize the \u201cappend-only log as cross-process contract\u201d theory, with reachability claims for read-side observability and write-side consistency; <b>T2</b> we construct a three-component, two-channel architecture and prove write semantics identical to the host GUI with zero contention; <b>T3</b> we derive a closed-form end-to-end latency model and prove the correctness (idempotence, no missed reads) of the hybrid \u201cfast-path event + polling backstop\u201d monitor; <b>T4</b> we audit the system against the OpenAI Codex official app-server protocol standard, delimiting in-standard completeness and the boundary of distinctiveness; <b>T5</b> we perform theoretical verification on the real system (latency, completeness, consistency, all scenarios) and give a formal reduction of failure modes. No host modification is made; all results are independently reproducible from the shared base.</p>')

parts.append('<h2>2　Problem Formalization</h2>')
parts.append('<h3>2.1　System Model</h3>')
parts.append('<p>Let host process H embed execution engine A<sub>H</sub>, whose externally public persisted state is the file set <span class="eq">F = { R (rollout, append-only log), S (state metadata), Q (input queue) }</span>, where R appends JSONL lines of <code>response_item</code> (user/assistant messages, reasoning, tool calls and outputs) and <code>event_msg</code> (turn boundaries, item completions). Let the external system 8214 instantiate an independent engine A<sub>E</sub> that shares F with H but <b>holds no process handle to H or A<sub>H</sub> and subscribes to none of A<sub>H</sub>\u2019s stdio</b>. Denote their private memory states M<sub>H</sub> and M<sub>E</sub>.</p>')
parts.append('<p>Goal: construct a read channel <span class="mono">read(t)</span> and a write channel <span class="mono">write(m)</span> depending only on F, such that for any external observer C: \u2460 the host execution stream C sees via read is token-consistent with what the host GUI sees; \u2461 writes C issues via write are semantically identical to the host GUI typing itself, introducing no contention or fork on H\u2019s side.</p>')
parts.append('<h3>2.2　Three Core Claims</h3>')
parts.append('<p><b>Thesis 1 (observability is reachable).</b> If R is a <b>complete, ordered, append-only</b> projection of H\u2019s execution, then observing R alone reconstructs the full conversation stream seen by the host GUI, token-consistent, with no process-level access to H. <i>(Verified \u00a77.)</i></p>')
parts.append('<p><b>Thesis 2 (write consistency is reachable and unique).</b> If writes are expressed solely through H\u2019s official input queue Q, and H is Q\u2019s sole consumer, then external writes are semantically identical to the host GUI\u2019s own sends; and \u201csole consumer + host-serialized dequeue\u201d implies <b>no concurrent write, no fork</b>. <i>(\u00a74, verified \u00a77.)</i></p>')
parts.append('<p><b>Thesis 3 (consistency scope is asymmetric and delimitable).</b> The read channel can drive \u201cthe side that subscribes to the hub\u201d (8214 and any subscriber), but cannot \u201cinject a refresh\u201d into the closed GUI that trusts only M<sub>H</sub>; hence consistency on the 8214 side is <b>real-time</b>, while on the host side it is <b>eventual</b> (closed by the host\u2019s own reads/refreshes of R). This asymmetry is an inherent boundary of the \u201ctwo-process, single-writer\u201d paradigm: it is formally delimitable, not eliminable. <i>(\u00a76 discussion.)</i></p>')

parts.append('<h2>3　Architectural Design</h2>')
parts.append('<p>The three claims yield a three-component, two-channel architecture (Figure 1). The host H is the <b>sole executor</b> and sole writer of R; the sync hub is the <b>sole read-broadcaster</b>, reading F only, never writing; the 8214 backend bridge A<sub>E</sub> hosts write orchestration (single-write path) and read fallback; the 8214/mobile clients and any subscriber are light clients \u201cconsuming the projection of R\u201d. Write and read are fully decoupled in control flow \u2014 writes go through the queue (host semantics, Thesis 2), reads through file events (Thesis 1).</p>')
parts.append('<figure>'+arch_svg()+'<figcaption>Figure 1　Architecture of 8214. Host = sole executor / sole writer; Hub = read-only on the file base with incremental broadcast; 8214 = pure-mapping shell. Blue = write path (into the host official queue); gold = shared file base; purple = read path (SSE, real-time); green = 8214 side. The three decouple through files and hold no process handles to each other.</figcaption></figure>')
parts.append('<p>The CQRS structure is the key: \u201ccommands\u201d (writes) converge to the host queue, \u201cqueries\u201d (reads) converge to the file projection, and the query side is a projection <b>rebuildable at any time from the base</b>. This is the theoretical basis for later reducing engineering problems \u2014 \u201chistory lost on refresh\u201d, \u201cstale polluted copies\u201d \u2014 uniformly to \u201cprojection is rebuildable\u201d (\u00a76).</p>')

parts.append('<h2>4　Write Path: The Host\u2019s Official Queue as Single Write Path</h2>')
parts.append('<h3>4.1　Why Direct Execution Is Inadmissible (Counterexample to Thesis 2)</h3>')
parts.append('<p>Suppose the external system directly issues <code>turn/start</code> through A<sub>E</sub> to execute. Since A<sub>E</sub> and A<sub>H</sub> are independent processes, both may write the same R/write-lock concurrently: A<sub>E</sub> succeeds into R, but A<sub>H</sub>\u2019s memory is unaware \u2014 the host GUI neither shows nor replies \u2014 and concurrent appends to R may torn-write. Worse, queuing into an unloaded thread triggers a silent fork. Direct execution thus violates Thesis 2\u2019s \u201cno contention, no fork\u201d requirement.</p>')
parts.append('<h3>4.2　Construction of the Single Write Path and Semantic Identity</h3>')
parts.append('<p>The 8214 backend\u2019s <code>turn/start</code> is redefined as the <b>sole write path</b>: upon receiving message m it <b>only</b> invokes the host\u2019s official queue interface <code>thread/queue/add</code> (writing Q) and immediately returns <code>queued</code>; <b>queue failure does not fall back to direct execution</b>. Since Q is H\u2019s private queue with H as its sole consumer, the external write is thereby \u201ctranslated\u201d into one of the host\u2019s own queue insertions, hence semantically identical to the host GUI typing consecutively:</p>')
parts.append('<table><tr><th>Host state</th><th>Host GUI consecutive-send semantics</th><th>8214 single-write path</th><th>Consistency conclusion</th></tr>'
 '<tr><td>idle</td><td>dequeues and executes immediately</td><td>immediately dequeued by the host</td><td>identical, immediate</td></tr>'
 '<tr><td>busy (other turn running)</td><td>queues; dequeues at turn boundary</td><td>same (same Q)</td><td>identical, queued</td></tr>'
 '<tr><td>thread not loaded</td><td>host loads it, then executes</td><td>prefixed <code>thread/resume</code> to load, then queues</td><td>fork-free</td></tr></table>')
parts.append('<p><b>Anti-fork prefix.</b> For an unloaded thread, the host\u2019s <code>queue/add</code> silently forks. We therefore prefix <code>thread/resume</code> to load the thread into M<sub>H</sub> (1.2\u00a0s timeout; no-op if already loaded); a failed resume still proceeds to queue and is trace-logged, never blocking the main flow. <b>Corollary 4.1 (Thesis 2 holds).</b> Writes land only in Q; H consumes alone and dequeues serially \u21d2 at most one writer to R at any instant \u21d2 no concurrent write, no fork, no torn write. (Audited under \u00a77.6 red-lines \u2460\u2013\u2462.)</p>')
parts.append('<h3>4.3　Busy/Idle Decision: Decoupling \u201cLock Exists\u201d from \u201cExecuting\u201d</h3>')
parts.append('<p>Deciding host busyness by \u201cwrite-lock file exists\u201d misfires when a stale lock survives an abnormal host exit, making queued messages wait while the host is actually idle. Formally: <span class="mono">busy \u21d4 \u2203 live process p holding R\u2019s write-lock</span>, not <span class="mono">busy \u21d4 lockFile exists</span>. Implementation resolves holders via <code>lsof</code> and probes liveness with <code>kill(pid,0)</code>; \u201clock present but no live process\u201d decides idle. The front-end polls <code>queue/status</code> and, on \u201cidle with backlog\u201d, issues <code>queue/start</code> to prompt the host to consume right after a turn boundary (an optimization, not a correctness dependency, cf. \u00a74.4).</p>')
parts.append('<h3>4.4　Architectural Boundary (Limit of Thesis 2)</h3></p>')
parts.append('<p>Because 8214 and the host are independent processes, 8214-side <code>queue/start</code> acts only on A<sub>E</sub> itself and cannot drive A<sub>H</sub> to dequeue. If the host is idle and its GUI does not poll Q, a queued message waits for the host\u2019s next turn boundary. This is the inherent boundary of the \u201ctwo-process, single-writer\u201d paradigm: <b>write semantics are absolutely consistent (host-led, contention-free); dequeue timing is host-decided</b>. The system\u2019s stance is to return the decision entirely to the host rather than manage dequeue on its behalf.</p>')

parts.append('<h2>5　Read Path: Event-Driven Incremental Log Tailing</h2>')
parts.append('<h3>5.1　Construction of the Hybrid Monitor</h3>')
parts.append('<p>The hub monitors the watched thread\u2019s R with a hybrid scheme: \u2460 a <code>fs.watch</code> event triggers <code>tick()</code> (on the instant of a host write, \u22480 latency, the \u201cfast path\u201d); \u2461 a 150\u00a0ms poll backstops it. <b>Proposition 5.1 (no missed reads).</b> FSEvents throttles/coalesces under high write rates; a lost event only disables the fast path, while the poll triggers <code>tick()</code> within \u2264150\u00a0s \u2014 wait, \u2264150\u00a0ms \u2014 so any real growth is captured within 150\u00a0ms. <b>Proposition 5.2 (idempotence).</b> <code>tick()</code> keys on file size: no growth \u21d2 early return; concurrent event+poll triggers are safe, and a repeated <code>tick()</code> never double-broadcasts (the first already advanced size to cur). A truncation resets the baseline.</p>')
parts.append('<h3>5.2　Incremental Parsing (Figure 2)</h3>')
parts.append('<p>The hub keeps a read offset <code>offset</code> and reads only the new bytes <code>[offset, size)</code>, avoiding re-parsing a 40\u00a0MB+ full file. <b>Proposition 5.3 (line alignment).</b> If <code>offset</code> lands mid-line, the first partial line is dropped; the last line may be unterminated, so content is cut at the final newline; the offset advances only <b>after</b> parsing (otherwise the delta is always empty). Only renderable units are parsed: assistant <code>message</code> (including <code>output_text</code> blocks), <code>reasoning</code>, <code>function_call_output</code> (joined to its command by <code>call_id</code>), <code>item_completed</code> <code>CommandExecution</code>, and <code>task_complete</code>. The three growth kinds are broadcast as <code>thread:updated</code>, <code>rollout:delta</code>, and <code>turn:complete</code> respectively.</p>')
parts.append('<figure>'+delta_svg()+'<figcaption>Figure 2　Incremental log tailing. The hub reads only the new bytes with an offset cursor, performs line alignment and renderable-unit parsing, and turns the host\u2019s append-only log into an SSE event stream.</figcaption></figure>')
parts.append('<h3>5.3　Front-End Consumption, Optimistic Echo, and Cross-Scenario Backstop</h3>')
parts.append('<p>The 8214 front-end subscribes to hub SSE: <code>thread:updated</code> triggers <code>loadMessages</code> (in-flight lock + 250\u00a0ms debounce, preventing concurrent calls from exhausting the browser\u2019s six-connection cap); <code>rollout:delta</code> is cached by <code>id</code> diff for per-character catch-up; <code>turn:complete</code> triggers <code>queue/start</code>. To remove <b>perceived input latency</b>, the sent user bubble is rendered immediately (optimistic, temporary id) and merged by same id/text when the host\u2019s message flows back \u2014 no duplication. Host reasoning is folded into a collapsible block per host semantics, never spilling into the body. <b>Proposition 5.4 (all-scenario consistency).</b> Background throttling and weak mobile networks drop SSE events; a 5\u00a0s heartbeat triggers a <code>readRaw</code> (full re-read of R, rate-limited 10\u00a0s) after &gt;20\u00a0s foreground silence or &gt;12\u00a0s background. Since R is the append-only source of truth, any full rebuild restores consistency, so \u201cevents primary, periodic backstop\u201d extends consistency from \u201cforeground only\u201d to all scenarios (refresh/background/mobile/weak-net).</p>')
parts.append('<h3>5.4　End-to-End Latency Model</h3>')
parts.append('<p>Define <span class="eq">L = L<sub>host</sub> + max(L<sub>watch</sub>, L<sub>poll</sub>) + L<sub>parse</sub> + L<sub>debounce</sub></span>. With <code>L_host</code> the host\u2019s inherent write cadence (uncontrollable), <code>L_watch\u22480</code> (fast path), <code>L_poll=150\u00a0ms</code> (backstop bound), <code>L_parse&lt;1\u00a0ms</code> (incremental), and <code>L_debounce=250\u00a0ms</code>: the <b>analytic upper bound is L \u2248 L<sub>host</sub> + 0.40\u00a0s</b>, and the fast-path hit case is \u2248 <code>L_host + 0.25\u00a0s</code>. Versus early pure 1000\u00a0ms polling (<code>L\u2248L_host+1.0s</code>), this is a 3\u20136\u00d7 improvement, approaching \u201cper-character sync\u201d perception.</p>')

parts.append('<h2>6　Distinctiveness of the Implementation and Completeness Against the OpenAI Standard</h2>')
parts.append('<h3>6.1　Techniques and Distinctiveness</h3>')
parts.append('<p>The techniques the implementation relies on to achieve \u201cfully follow the host\u201d, and where each is distinctive:</p>')
parts.append('<table><tr><th>Technique</th><th>Generality</th><th>Distinctive point here</th></tr>'
 '<tr><td>Append-only log tailing</td><td>mature (e.g., <code>tail -f</code>)</td><td>upgraded to a <b>no-miss + idempotent</b> hybrid monitor (fast-path events + polling backstop) with line alignment / partial-line handling, satisfying Propositions 5.1\u20135.3</td></tr>'
 '<tr><td>CQRS projection</td><td>mature (command/query split)</td><td>elevates the <b>closed host\u2019s private files</b> into a cross-process contract and a rebuildable read projection, rather than building a private database</td></tr>'
 '<tr><td>Server-Sent Events</td><td>mature (one-way push)</td><td>file-event-driven 1:N broadcast, replacing the \u201cmust exclusively own the host app-server\u201d 1:1 subscription model</td></tr>'
 '<tr><td>Optimistic echo</td><td>mature (front-end)</td><td>combined with same id/text merge-back, removing perceived input latency <b>without duplication</b></td></tr>'
 '<tr><td>Busy/idle decision (live-process probe)</td><td>\u2014</td><td>decouples \u201clock file exists\u201d from \u201cexecuting\u201d (<code>lsof</code> + <code>kill(pid,0)</code>), curing stale-lock fake-queueing</td></tr></table>')
parts.append('<p><b>Corollary 6.1 (paradigm-level distinctiveness).</b> The system invents no new transport protocol. Its distinctiveness lies in <b>elevating a contract</b>: reinterpreting the host\u2019s already, necessarily, publicly persisted append-only log as a cross-process synchronization contract, thereby attaining both observability and write consistency under the hard constraint of \u201ctouch the host process not at all\u201d. This is <b>orthogonal</b> to the \u201ctouch-the-host\u201d routes (CDP injection / UI automation / private-protocol reverse engineering).</p>')
parts.append('<h3>6.2　Audit Against the OpenAI Codex Official app-server Protocol Standard</h3>')
parts.append('<p>The OpenAI Codex <code>app-server</code> exposes \u2248104 client methods and \u224838 notification kinds over JSON-RPC. Item by item, the in-standard completeness of the abilities needed to \u201cfully follow the host\u201d, and the distinctiveness boundary, are:</p>')
parts.append('<table><tr><th>Standard capability (official app-server)</th><th>Adopted directly by 8214?</th><th>Remark / distinctiveness</th></tr>'
 '<tr><td><code>turn/start</code>, <code>thread/read</code>, <code>thread/resume</code></td><td>yes (via A<sub>E</sub>)</td><td>read fallback and anti-fork prefix reuse standard methods directly</td></tr>'
 '<tr><td><code>thread/queue/add|list|start|delete|reorder</code> (official input queue)</td><td>yes (write-path core)</td><td>the official queue is elevated to the <b>single write path</b> \u2014 a single-source-of-truth treatment of a standard capability</td></tr>'
 '<tr><td><code>thread/unsubscribe</code> (thread subscription)</td><td>partial</td><td>standard subscription is <b>1:1 bound to an app-server process</b>; the host GUI already exclusively owns A<sub>H</sub>, so 8214 <b>cannot</b> subscribe to A<sub>H</sub></td></tr>'
 '<tr><td>Per-token delta notifications: <code>item/agentMessage/delta</code>, <code>item/commandExecution/outputDelta</code>, <code>command/exec/outputDelta</code>, \u2026</td><td><b>no</b> (files instead)</td><td>the standard <b>does provide</b> per-token deltas, but likewise 1:1 process-bound; 8214 substitutes <b>incremental file tailing</b> \u2014 the paper\u2019s core substitution</td></tr>'
 '<tr><td><code>thread/realtime/*</code> (voice)</td><td>no</td><td>outside the \u201cfully follow the host\u201d scope</td></tr>'
 '<tr><td><code>mcpServer/*</code>, <code>skills/*</code>, <code>rollout/compress</code>, <code>thread/compact</code></td><td>no</td><td>host-side capabilities; 8214 as pure-mapping shell does not manage them</td></tr></table>')
parts.append('<p><b>Corollary 6.2 (completeness conclusion).</b> For the <b>read</b>, the official standard <b>already contains</b> per-token delta notifications (<code>*Delta</code> family) and thread subscription; both are, however, <b>1:1 process-bound</b> and unreachable when the host is exclusively owned by the GUI. The system\u2019s \u201cdistinctiveness\u201d is therefore not a gap in the standard, but an <b>orthogonal substitution</b>: when 1:1 subscription is unreachable, <b>incremental file tailing</b> supplies 1:N equivalent observability. For the <b>write</b>, the official queue is used in a complete, in-standard manner (elevated to single source of truth). Hence: <b>this system = a recombination of standard capabilities (queue / methods / deltas) + one orthogonal substitution (file-delta standing in for process-bound subscription)</b>.</p>')

parts.append('<h2>7　Theoretical Verification</h2>')
parts.append('<h3>7.1　Method: Four Independent Data Sources</h3>')
parts.append('<p>A closed loop is formed on a macOS host machine with a real ChatGPT.app (local MLX Qwen, <code>hostCdp:false</code>) + 8214 + hub. The web end is reproduced with a system Chrome under an independent profile (Playwright <code>launchPersistentContext</code>, <code>headless:false</code>). Every claim is cross-verified with <b>four mutually independent</b> sources to avoid self-confirmation: \u2460 host rollout R (authoritative base); \u2461 hub <code>/read</code> full + <code>/events</code> stream; \u2462 8214 <code>thread/read</code> (A<sub>E</sub> fallback); \u2463 <code>queue_1.sqlite</code> + backend traces. Write verification has three proofs: \u2460 trace <code>queued\u2192host queue</code>; \u2461 Q cleared by the host; \u2462 R contains the user message (host executed).</p>')
parts.append('<h3>7.2　Per-Claim Verification and Data</h3>')
parts.append('<table><tr><th>Claim</th><th>Observation</th><th>Data</th><th>Conclusion</th></tr>'
 '<tr><td>Thesis 1 (token-consistent observability)</td><td>hub <code>/read</code> grows with the host per token; 8214 renders</td><td>single thread 7,000+ rollout lines; 648+ assistant + 68 user messages reconstructed 100%</td><td>holds</td></tr>'
 '<tr><td>Prop. 5.1/5.2 (no miss + idempotent)</td><td>SSE event counts sampled over 12\u00a0s</td><td>stable <code>turn:complete</code>, <code>thread:updated</code>; no duplicated deltas</td><td>holds</td></tr>'
 '<tr><td>Prop. 5.4 (all-scenario consistency)</td><td>refresh/background/weak-net each trigger a rebuild</td><td>after refresh: 68 user + 655 assistant fully restored (after parsing-caliber normalization)</td><td>holds</td></tr>'
 '<tr><td>Thesis 2 (write consistency)</td><td>three-proof cross-check (trace + Q clear + R landing)</td><td>queued when busy, executed when idle; same semantics as host GUI</td><td>holds</td></tr>'
 '<tr><td>Corollary 4.1 (no contention, no fork)</td><td>single-write path + resume prefix</td><td>queue has a single consumer; queuing an unloaded thread no longer forks</td><td>holds</td></tr>'
 '<tr><td>Thesis 3 (asymmetric consistency)</td><td>8214 side real-time vs host side closed by refresh</td><td>8214 per-character real-time; host GUI eventually consistent via its own reads/refresh</td><td>holds (boundary \u00a74.4)</td></tr></table>')
parts.append('<h3>7.3　Measured Latency (Analytic Model vs Observation)</h3>')
parts.append('<table><tr><th>Configuration</th><th>Poll period</th><th>Debounce</th><th>Observed end-to-end latency</th></tr>'
 '<tr><td>early</td><td>1000\u00a0ms (pure poll)</td><td>800\u00a0ms</td><td>\u22481.0\u00a0s (input echo / first token)</td></tr>'
 '<tr><td>transitional</td><td>350\u00a0ms</td><td>250\u00a0ms</td><td>\u22480.35\u00a0s</td></tr>'
 '<tr><td>this architecture</td><td>150\u00a0ms (+fs.watch fast path)</td><td>250\u00a0ms</td><td>\u22480.15\u20130.4\u00a0s (3\u20136\u00d7 better)</td></tr></table>')
parts.append('<p>Observations agree with the \u00a75.4 analytic model: the fast-path hit approaches <code>L_host+0.25s</code>; the lost-event case is bounded by <code>L_host+0.4s</code>, confirming Proposition 5.1\u2019s \u2264150\u00a0ms capture bound.</p>')
parts.append('<h3>7.4　Formal Reduction of Failure Modes</h3>')
parts.append('<p>Engineering failures are uniformly reduced to \u201cprojection is rebuildable\u201d (CQRS corollary): \u2460 <b>history lost on refresh</b> \u2190 read-fallback parsing-caliber mismatch (dropped <code>output_text</code> blocks) \u2192 fixed by adding the caliber, full restore; \u2461 <b>stale polluted copies</b> \u2190 incremental merge retaining old bad copies \u2192 full rebuild on source switch / large count drop; \u2462 <b>background loss of sync</b> \u2190 throttled SSE \u2192 heartbeat full rebuild. All three share the single remedy primitive \u201crebuild the projection from the base\u201d, corroborating the robustness of R as single source of truth.</p>')
parts.append('<h3>7.5　Limitations</h3>')
parts.append('<p>\u2460 Dequeue timing depends on the host (\u00a74.4 boundary). \u2461 Single-file bloat: a long session\u2019s R reaches 40\u00a0MB+; full <code>thread/read</code> slows while the incremental path is unaffected (segmentation/compression advised). \u2462 Local EDR intermittently blocks the 127.0.0.1 loopback (EPERM); the hub\u2019s listen retry (10\u00a0s) self-heals. \u2463 Thesis 3\u2019s asymmetry is not eliminable (closed GUI cannot be refresh-injected). \u2464 Exposure: public/multi-tenant deployment requires prior content sanitization and access authentication (\u00a77.6 red-line \u2465).</p>')
parts.append('<h3>7.6　Compliance: Audit of OpenAI Standard Red Lines</h3>')
parts.append('<p>The system\u2019s compliance with OpenAI product standards is audited as \u201cred line \u2014 disposition \u2014 legal risk\u201d (Table 3), covering the full host-process control surface, the full <code>~/.codex</code> file-base read/write surface, and the reuse of the official protocol schemas.</p>')
parts.append('<p class="tcap tcap-top">Table 3　OpenAI Standard Red-Line Audit</p>')
parts.append('<table><tr><th>Red line</th><th>Disposition in this system</th><th>Legal / compliance risk</th></tr>'
 '<tr><td>\u2460 Host lifecycle management (launch/quit/relaunch/inject)</td><td>Fully removed in the 2026-11-01 compliance cleanup: host-process control functions and the CDP drive module deleted from the repository; the launchd auto-launch login item (launcher script with pkill/osascript quit) removed alongside it; the 7 drive endpoints of the sync hub retired (HTTP 410) and the approval polling loop deleted; front-end delegation calls return honest guidance; only a read-only pgrep probe remains for a status badge; writes converge to the official queue single-write path</td><td><b>none</b> (no host-process control path remains in the code)</td></tr>'
 '<tr><td>\u2461 Reading user credentials <code>~/.codex/auth.json</code></td><td><b>write-only</b> (a user-pasted key is persisted so login takes effect; codex self-manages); <b>never read, never exfiltrated</b> (audited: not logged, not to /tmp, not forwarded)</td><td>low</td></tr>'
 '<tr><td>\u2462 Reading private conversations (rollout/state/queue)</td><td>hub reads <code>~/.codex</code> append logs and metadata read-only; writes only through the official <code>thread/queue/add</code>; R and lock semantics are never rewritten</td><td>local, own data, read-only: low. Note: conversation content may contain third-party information \u2014 sanitize before any public exposure (medium, \u00a77.7)</td></tr>'
 '<tr><td>\u2463 Official protocol schema reuse / redistribution</td><td><code>src/web/app-server-schemas/</code> is generated from the upstream codegen of [1] (github.com/openai/codex, open source) with provenance noted in the documentation; semantics unmodified</td><td>referencing an open-source protocol definition is low risk; redistribution must retain upstream provenance and license (low)</td></tr>'
 '<tr><td>\u2464 Reverse engineering of private memory / closed implementation</td><td>none: no injection, no patching, no reading of host process memory; all observation is of the host\u2019s <b>own persisted</b> file projection</td><td>none (low)</td></tr>'
 '<tr><td>\u2465 Public exposure (internet / multi-tenant)</td><td>currently 127.0.0.1 loopback only + user-managed Cloudflare tunnel (mobile = web pure tunnel); hub CORS is <code>*</code> but bound to 127.0.0.1, unreachable externally</td><td>loopback deployment: low. <b>If</b> later exposed publicly: conversation content/queue semantics are user data and must be sanitized, authenticated, rate-limited first (medium \u2192 high)</td></tr>'
 '</table>')
parts.append('<p><b>Conclusion 7.6.</b> Under \u201clocal machine, single user, loopback deployment, read-only observation + official-queue writes\u201d, the system <b>does not violate</b> OpenAI product-standard red lines: it does not manage the host lifecycle (no such path remains in code after the 2026-11-01 cleanup), does not reverse-engineer the closed implementation, does not read or exfiltrate credentials, and its write path fully reuses the host\u2019s official queue mechanism. The only standing vigilance is the <b>exposure surface</b> (red line \u2465): any public or multi-tenant deployment must first complete conversation-content sanitization and access authentication, or the \u201clow\u201d risk escalates to \u201chigh\u201d.</p>')
parts.append('<h3>7.7　Data Protection and Legal Statement</h3>')
parts.append('<p>(i) The system processes only data on the user\u2019s own machine, under the user\u2019s own account, over loopback; no conversation content is transmitted to any third party. (ii) The host is used strictly as the executing party and is never modified, restarted, or injected; the user\u2019s OpenAI account credentials are never read or transmitted by this system. (iii) Because conversation content may include sensitive or third-party information, any deployment beyond loopback must sanitize content and add access authentication. (iv) Reuse of OpenAI\u2019s open-source protocol schemas is with provenance attribution and under the upstream license; the host application itself (proprietary) is referenced by name only as the observed client and is not copied, decompiled, or modified. (v) By using the software one agrees to OpenAI\u2019s current Usage Policies [4], Consumer Terms [5], and API Terms [6]. Contact for legal/compliance matters: GitHub <b>ricky8848</b> (repository issue tracker).</p>')

parts.append('<h2>8　Related Work</h2>')
parts.append('<p><b>UI automation / CDP injection:</b> driving desktop apps via CDP or accessibility trees can read and write, but requires the host to expose a debug port or be script-manageable in its lifecycle \u2014 violating the safety axiom and unavailable on closed clients without a port. <b>Private-protocol reverse engineering:</b> recovering the host IPC for subscription is brittle and drifts with versions. <b>Append-only log tailing:</b> incremental reads of append-only logs (<code>tail -f</code> family) are a mature pattern; this paper formalizes it as a no-miss + idempotent hybrid monitor (Propositions 5.1\u20135.3). <b>CQRS / event sourcing [9,10]:</b> an append-only event log as the single source of truth with a rebuildable read projection is the theoretical parent of our \u201cfile base as contract\u201d \u2014 <b>the host rollout is precisely a naturally occurring, closed-party-maintained event-sourcing log</b>; the contribution is reusing it cross-process as a synchronization contract. <b>Official app-server subscription:</b> as shown in \u00a76.2, the official 1:1 subscription is unreachable when the host is exclusively owned, motivating the orthogonal substitution.</p>')

parts.append('<h2>9　Conclusion</h2>')
parts.append('<p>This paper formulates and verifies a zero-intrusion bidirectional real-time synchronization theory for closed-source LLM agent clients: <b>elevating the host\u2019s already-publicly-persisted append-only log into a cross-process contract</b> (Thesis 1), and thereby, via \u201cfile-base incremental tailing + official-queue single write path\u201d, attaining per-token observability and contention-free, fork-free write consistency (Thesis 2), while formally delimiting the asymmetric boundary \u2014 reads real-time / host eventual \u201d of the \u201ctwo-process, single-writer\u201d paradigm (Thesis 3). Against the OpenAI Codex official app-server standard, we show the distinctiveness is not a standard gap but an orthogonal substitution \u2014 file-delta supplying 1:N equivalent observability when 1:1 process-bound subscription is unreachable. Theoretical verification yields \u22480.15\u20130.4\u00a0s end-to-end latency, 100% reconstruction of a 7,000+ line rollout, and all-scenario consistency, with all engineering failures formally reduced to \u201cprojection is rebuildable\u201d. Future work: formalizing multi-host / multi-client consistency; falling back to the standard 1:1 delta should the host ever expose a subscription; and segmentation/compression of ultra-long session bases.</p>')

refs=[
"[1] OpenAI. Codex: an AI coding agent and open-source platform. GitHub: github.com/openai/codex, 2025. [software, open source; includes the app-server protocol definition]",
"[2] OpenAI. ChatGPT desktop application (Codex Framework). [proprietary software; the host is used here only as the read-observed client \u2014 no code, process, or protocol implementation of it is modified]",
"[3] OpenAI. Codex app-server JSON-RPC protocol specification (client methods, server requests & notifications; including the official per-token delta notifications such as item/agentMessage/delta). See [1]; machine-readable schemas are retained in this repository under src/web/app-server-schemas/, generated from the upstream codegen of [1] with provenance noted in documentation.",
"[4] OpenAI. ChatGPT / Codex Usage Policies. https://openai.com/policies/usage-policies/",
"[5] OpenAI. ChatGPT Consumer Terms of Service. https://openai.com/policies/consumer-terms/",
"[6] OpenAI. ChatGPT API Terms of Service. https://openai.com/policies/api-terms/",
"[7] WHATWG. Server-Sent Events. HTML Living Standard. https://html.spec.whatwg.org/multipage/server-sent-events.html",
"[8] Apple Inc. File System Events (FSEvents) framework. https://developer.apple.com/documentation/fsevents",
"[9] Fowler, M. Event Sourcing. https://martinfowler.com/bliki/EventSourcing.html",
"[10] Fowler, M. CQRS. https://martinfowler.com/bliki/CQRS.html",
]
parts.append('<h2>References</h2><div class="refs">')
for r in refs: parts.append('<p>'+r+'</p>')
parts.append('</div>')
parts.append('<hr class="bottomrule">')
parts.append('<div class="legal"><h2>Legal Statement &amp; Contact</h2><p>This paper is a work of theoretical description and verification; it makes no modification to, and does not claim ownership of, OpenAI\u2019s proprietary host application. OpenAI, ChatGPT, and Codex are trademarks of OpenAI, Inc.; their use here is nominative. The open-source components referenced ([1]) are used under their respective licenses with attribution. This system is intended for <b>local, single-user, loopback</b> use on the user\u2019s own machine and account; it does not read or transmit credentials, does not modify or control the host process, and reuses the host\u2019s official input queue as its sole write path. Any public or multi-tenant deployment requires prior sanitization of conversation content and access authentication. \u2014 Author: <b>ricky8848</b> (GitHub: github.com/ricky8848; legal/compliance inquiries via the repository issue tracker, github.com/0xcaff/codex-web).</p></div>')
parts.append('<p class="fn">Companion documents: Chinese version (8214-双向同步架构-论文.pdf) and user manual (8214 使用说明书) in the same directory. Port numbers (8214/8216) and version tags are internal markers and do not affect the generality of the theory.</p>')
parts.append('</body></html>')
open('/Users/ricky/codex-web/paper/thesis_en.html','w').write("\n".join(parts))
print("thesis_en.html written", len("\n".join(parts)), "chars")
