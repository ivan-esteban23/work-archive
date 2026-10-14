import fs from 'node:fs/promises';
const root='/home/ivanaguilera/Work/pinterest-alternatives-update-20261013';
const targets=await(await fetch('http://127.0.0.1:9229/json/list')).json();
const ws=new WebSocket(targets.find(t=>t.url==='app://obsidian.md/index.html').webSocketDebuggerUrl);
await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let id=0;const pending=new Map();
ws.addEventListener('message',e=>{const d=JSON.parse(e.data);if(pending.has(d.id)){pending.get(d.id)(d);pending.delete(d.id);}});
const call=(method,params={})=>new Promise(r=>{pending.set(++id,r);ws.send(JSON.stringify({id,method,params}));});
const evaluate=async expression=>{const d=await call('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});if(d.result?.exceptionDetails)throw new Error(JSON.stringify(d.result.exceptionDetails));return d.result?.result?.value;};
await evaluate(`(async()=>{const f=app.vault.getAbstractFileByPath('Attachments/Pinterest Alternatives/Pinterest Alternatives — Visual Research and Moodboarding.html');if(!f)throw Error('Missing HTML');await app.workspace.getLeaf(false).openFile(f);return true;})()`);
await evaluate(`(()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');if(w)w.reload();return true;})()`);
await new Promise(r=>setTimeout(r,1500));
const probe=`(()=>{const visible=()=>[...document.querySelectorAll('.source')].filter(c=>!c.hidden).length;const s=document.querySelector('#search'),r=document.querySelector('#region');const results={all:visible(),title:document.title};s.value='PureRef';s.dispatchEvent(new Event('input'));results.search=visible();s.value='';s.dispatchEvent(new Event('input'));r.value='Japan';r.dispatchEvent(new Event('change'));results.japan=visible();r.value='All';r.dispatchEvent(new Event('change'));document.querySelector('[data-filter="Collect & organize"]').click();results.collect=visible();s.value='no-such-source-xyz';s.dispatchEvent(new Event('input'));results.empty=!document.querySelector('#empty').hidden;s.value='';document.querySelector('[data-filter="All"]').click();results.reset=visible();results.horizontalOverflow=document.documentElement.scrollWidth>innerWidth;window.scrollTo(0,0);return results;})()`;
const results=await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');if(!w)throw Error('Not HTML view');return await w.executeJavaScript(${JSON.stringify(probe)});})()`);
if(results.all!==52||results.search!==1||results.japan!==4||results.collect!==12||!results.empty||results.reset!==52||results.horizontalOverflow)throw Error(JSON.stringify(results));
const images=await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');return await w.executeJavaScript("(()=>({logos:document.querySelectorAll('.brand-logo').length,broken:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.alt)}))()");})()`);
if(images.logos!==52||images.broken.length)throw Error(JSON.stringify(images));
results.images=images;
const fontProbe=`(async()=>{await document.fonts.ready;return {serif:document.fonts.check('48px "Instrument Serif"'),sans:document.fonts.check('16px "Source Sans 3"'),faces:[...document.fonts].map(f=>({family:f.family,status:f.status}))}})()`;
const fonts=await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');return await w.executeJavaScript(${JSON.stringify(fontProbe)});})()`);
if(!fonts.serif||!fonts.sans||fonts.faces.some(f=>f.status!=='loaded'))throw Error(JSON.stringify(fonts));results.fonts=fonts;

const finishProbe=`(()=>{const routes=[...document.querySelectorAll('.research-route')],before=routes.map(d=>d.open);window.dispatchEvent(new Event('beforeprint'));const printExpanded=routes.every(d=>d.open);window.dispatchEvent(new Event('afterprint'));const printRestored=routes.every((d,i)=>d.open===before[i]);const skip=document.querySelector('.skip-link');skip.focus();return {reviews:document.querySelectorAll('.review-date time[datetime="2026-10-13"]').length,printExpanded,printRestored,skipFocused:document.activeElement===skip,focusVisible:getComputedStyle(skip).transform==='matrix(1, 0, 0, 1, 0, 0)'};})()`;
const finish=await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');return await w.executeJavaScript(${JSON.stringify(finishProbe)});})()`);
if(finish.reviews!==52||!finish.printExpanded||!finish.printRestored||!finish.skipFocused)throw Error(JSON.stringify(finish));
const mobile=await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');const prior=w.getAttribute('style');w.style.setProperty('width','390px','important');w.style.setProperty('max-width','390px','important');w.style.setProperty('min-width','390px','important');w.style.setProperty('flex','none','important');await new Promise(r=>setTimeout(r,300));const result=await w.executeJavaScript("(()=>({width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth,columns:getComputedStyle(document.querySelector('.grid')).gridTemplateColumns.split(' ').length,filterScroll:document.querySelector('.filters').scrollWidth>document.querySelector('.filters').clientWidth}))()");if(prior===null)w.removeAttribute('style');else w.setAttribute('style',prior);return result;})()`);
if(mobile.width!==390||mobile.overflow||mobile.columns!==1||!mobile.filterScroll)throw Error(JSON.stringify(mobile));
results.finish=finish;results.mobile=mobile;

const navigationProbe=`(()=>{const s=document.querySelector('#search'),r=document.querySelector('#region'),count=f=>+([...document.querySelectorAll('[data-filter]')].find(b=>b.dataset.filter===f).querySelector('.filter-count').textContent);const result={labels:document.querySelectorAll('.comparison').length,initial:count('Collect & organize')};s.value='PureRef';s.dispatchEvent(new Event('input'));result.searchCount=count('Collect & organize');r.value='Japan';r.dispatchEvent(new Event('change'));document.querySelector('#reset').click();result.reset=[...document.querySelectorAll('.source')].filter(c=>!c.hidden).length===52&&s.value===''&&r.value==='All';document.querySelector('.grid').scrollIntoView();result.sticky=getComputedStyle(document.querySelector('.directory-tools')).position==='sticky';return result;})()`;
const navigation=await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');return await w.executeJavaScript(${JSON.stringify(navigationProbe)});})()`);
if(navigation.labels!==52||navigation.initial!==12||navigation.searchCount!==1||!navigation.reset||!navigation.sticky)throw Error(JSON.stringify(navigation));
results.navigation=navigation;

const editorial=await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');return await w.executeJavaScript("(()=>{const d=[...document.querySelectorAll('.research-route')];d[0].querySelector('summary').click();const opened=d[0].open;d[0].querySelector('summary').click();const closed=!d[0].open;return {picks:document.querySelectorAll('.editor-pick').length,routes:d.length,opened,closed,links:[...document.querySelectorAll('.editor-pick a,.route-sources a')].every(a=>a.href.startsWith('https://'))}})()");})()`);
if(editorial.picks!==8||editorial.routes!==4||!editorial.opened||!editorial.closed||!editorial.links)throw Error(JSON.stringify(editorial));
results.editorial=editorial;

await evaluate(`(async()=>{const w=app.workspace.getMostRecentLeaf().view.containerEl.querySelector('webview');await w.executeJavaScript("window.scrollTo({top:0,behavior:'instant'});void 0");return true;})()`);
await new Promise(r=>setTimeout(r,300));
const shot=await call('Page.captureScreenshot',{format:'png'});
await fs.writeFile(root+'/typography-hero-preview.png',Buffer.from(shot.result.data,'base64'));
await fs.writeFile(root+'/viewer-results.json',JSON.stringify(results,null,2));
console.log(JSON.stringify(results));ws.close();
