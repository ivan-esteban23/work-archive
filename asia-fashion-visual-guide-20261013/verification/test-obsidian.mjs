import fs from 'node:fs/promises';
const root = '/home/ivanaguilera/Work/asia-fashion-visual-guide-20261013/verification';
const targets = await (await fetch('http://127.0.0.1:9229/json/list')).json();
const target = targets.find(t => t.url === 'app://obsidian.md/index.html');
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise(resolve => ws.addEventListener('open', resolve, {once:true}));
let id = 0;
const pending = new Map();
ws.addEventListener('message', event => {const d=JSON.parse(event.data); if(pending.has(d.id)){pending.get(d.id)(d);pending.delete(d.id);}});
const call = (method,params={}) => new Promise(resolve => {const n=++id;pending.set(n,resolve);ws.send(JSON.stringify({id:n,method,params}));});
const evaluate = async expression => {
 const d=await call('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});
 if(d.result?.exceptionDetails) throw new Error(JSON.stringify(d.result.exceptionDetails));
 return d.result?.result?.value;
};
console.log(JSON.stringify(await evaluate(`(async()=>{
 const path='Asia Fashion — Visual Guide/fashion-visual-companion.html';
 const file=app.vault.getAbstractFileByPath(path);
 if(!file) throw new Error('HTML not found in vault');
 const plugin=app.plugins.plugins['local-html-view'];
 if(!plugin) throw new Error('HTML viewer not loaded');
 await app.workspace.getLeaf(false).openFile(file);
 return {plugin:plugin.manifest.version,file:path};
})()`)));
await new Promise(resolve=>setTimeout(resolve,3000));
console.log(JSON.stringify(await evaluate(`(()=>{
 const leaf=app.workspace.getMostRecentLeaf();
 const frame=leaf.view.containerEl.querySelector('webview,iframe');
 return {viewType:leaf.view.getViewType(),frame:frame?.tagName,src:frame?.getAttribute('src'),text:leaf.view.containerEl.innerText.slice(0,200)};
})()`)));
const probe = `(()=>({title:document.title,width:innerWidth,images:[...document.images].map(i=>({alt:i.alt,loaded:i.complete&&i.naturalWidth>0})),cards:document.querySelectorAll('.outfit-image').length,background:getComputedStyle(document.body).backgroundColor,crops:[...document.querySelectorAll('.outfit-image')].map(e=>({width:e.clientWidth,height:e.clientHeight,overflow:getComputedStyle(e).overflow}))}))()`;
console.log(JSON.stringify(await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');return await w.executeJavaScript(${JSON.stringify(probe)});})()`)));
await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');w.setZoomFactor(0.65);await w.executeJavaScript("document.querySelector('#korea').scrollIntoView();void 0");return true;})()`);
await new Promise(resolve=>setTimeout(resolve,600));
const screenshot=await call('Page.captureScreenshot',{format:'png'});
await fs.writeFile(root+'/obsidian-html.png',Buffer.from(screenshot.result.data,'base64'));
console.log('Screenshot saved: '+root+'/obsidian-html.png');
await evaluate(`(()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');w.setZoomFactor(1);return true;})()`);
ws.close();
