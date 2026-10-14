import fs from 'node:fs/promises';
const root='/home/ivanaguilera/Work/visual-edit-design-preview-20261013';
const targets=await (await fetch('http://127.0.0.1:9238/json/list')).json();
const ws=new WebSocket(targets.find(t=>t.type==='page').webSocketDebuggerUrl);
await new Promise(r=>ws.addEventListener('open',r,{once:true}));let id=0;const pending=new Map();
ws.addEventListener('message',e=>{const d=JSON.parse(e.data);if(pending.has(d.id)){pending.get(d.id)(d);pending.delete(d.id)}});
const call=(method,params={})=>new Promise(r=>{pending.set(++id,r);ws.send(JSON.stringify({id,method,params}))});
const ev=async expression=>{const d=await call('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(d.error||d.result.exceptionDetails)throw Error(JSON.stringify(d));return d.result.result.value};
if(process.argv.includes('--close')){ws.send(JSON.stringify({id:++id,method:'Browser.close'}));await new Promise(r=>setTimeout(r,250));ws.close();process.exit(0);}
await call('Page.enable');await call('Page.navigate',{url:'file://'+root+'/index.html'});
await new Promise(r=>setTimeout(r,1200));await ev('document.fonts.ready.then(()=>true)');
if(process.argv.includes('--mobile-capture')){
 await call('Emulation.setDeviceMetricsOverride',{width:390,height:1300,deviceScaleFactor:1,mobile:false});
 for(const theme of ['light','dark']){
  await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-color-scheme',value:theme},{name:'prefers-reduced-motion',value:'reduce'}]});
  await ev("setLocale('en',false);window.scrollTo(0,0)");await new Promise(r=>setTimeout(r,150));
  const shot=await call('Page.captureScreenshot',{format:'png'});
  await fs.writeFile(root+`/preview-390-${theme}.png`,Buffer.from(shot.result.data,'base64'));
 }
 console.log('Saved both complete mobile portrait screenshots');
 ws.send(JSON.stringify({id:++id,method:'Browser.close'}));await new Promise(r=>setTimeout(r,250));ws.close();process.exit(0);
}
const results=[];
for(const width of [390,768,1440])for(const theme of ['light','dark']){
 await call('Emulation.setDeviceMetricsOverride',{width,height:1000,deviceScaleFactor:1,mobile:false});
 await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-color-scheme',value:theme},{name:'prefers-reduced-motion',value:'reduce'}]});
 await new Promise(r=>setTimeout(r,150));
 const result=await ev(`(()=>{window.scrollTo(0,0);return {width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth,cards:document.querySelectorAll('.source').length,columns:getComputedStyle(document.querySelector('.grid')).gridTemplateColumns.split(' ').length,fonts:document.fonts.status,images:[...document.images].every(i=>i.complete&&i.naturalWidth)}})()`);
 if(result.overflow||result.cards!==52||!result.images)throw Error(JSON.stringify(result));results.push({theme,...result});
 const shot=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
 await fs.writeFile(root+`/preview-${width}-${theme}.png`,Buffer.from(shot.result.data,'base64'));
 if(width===1440){await ev("document.querySelector('.grid').scrollIntoView();void 0");const cards=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});await fs.writeFile(root+`/cards-${theme}.png`,Buffer.from(cards.result.data,'base64'));}
}
for(const locale of ['en','es','zh-Hans','zh-Hant','ja','ko'])for(const width of [390,768,1440]){
 await call('Emulation.setDeviceMetricsOverride',{width,height:1000,deviceScaleFactor:1,mobile:false});
 await ev(`setLocale('${locale}',false)`);await new Promise(r=>setTimeout(r,60));
 const overflow=await ev('document.documentElement.scrollWidth>innerWidth');results.push({locale,width,overflow});if(overflow)throw Error(JSON.stringify({locale,width,overflow}));
}
await ev("setLocale('en',false)");
const interactions=await ev(`(()=>{const region=document.querySelector('#region');region.value='Japan';region.dispatchEvent(new Event('change'));const japan=[...document.querySelectorAll('.source')].filter(c=>!c.hidden).length;document.querySelector('#reset').click();document.querySelector('.favorite-source').click();document.querySelector('#favorites-view').click();const favorites=[...document.querySelectorAll('.source')].filter(c=>!c.hidden).length;const md=buildFavoriteMarkdown();document.querySelector('.favorite-source').click();document.querySelector('#reset').click();return {japan,favorites,markdown:md.includes('Are.na'),restored:[...document.querySelectorAll('.source')].filter(c=>!c.hidden).length}})()`);
await fs.writeFile(root+'/preview-checks.json',JSON.stringify({results,interactions},null,2));
console.log(JSON.stringify({layouts:6,languageLayouts:18,interactions}));ws.close();
