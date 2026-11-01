import { chromium } from '/Users/ricky/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs';
const jobs = [
  ['/Users/ricky/codex-web/paper/thesis.html',   '/Users/ricky/codex-web/paper/8214-双向同步架构-论文.pdf'],
  ['/Users/ricky/codex-web/paper/thesis_en.html','/Users/ricky/codex-web/paper/8214-thesis-EN.pdf'],
  ['/Users/ricky/codex-web/paper/paper.html',    '/Users/ricky/codex-web/paper/8214-8214双向同步架构-使用说明书.pdf'],
];
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
const p = await b.newPage();
for (const [src, out] of jobs) {
  await p.emulateMedia({ media: 'print' });
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.pdf({ path: out, format: 'A4', printBackground: true, margin: { top: '16mm', bottom: '16mm', left: '15mm', right: '15mm' } });
  console.log('printed', out);
}
await b.close();
