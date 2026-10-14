import fs from 'node:fs';import {call,ev,until,sleep,shot,ws} from './browser.mjs';
await call('Page.reload',{ignoreCache:true});await until("typeof cards!=='undefined'&&cards.length===58");
const results=[];
for(const width of [320,390,768,1440]){
 await call('Emulation.setDeviceMetricsOverride',{width,height:900,deviceScaleFactor:1,mobile:width<640});
 for(const locale of ['en','es','zh-Hans','zh-Hant','ja','ko']){
  await ev(`setLocale('${locale}',false);document.querySelectorAll('.research-route').forEach(x=>x.open=true)`);
  const r=await ev(`({width:innerWidth,locale:document.documentElement.lang,overflow:document.documentElement.scrollWidth>innerWidth,namesFirst:[...document.querySelectorAll('.editor-pick')].every(x=>x.firstElementChild.tagName==='H3'),picks:[...document.querySelectorAll('.editor-pick h3')].map(x=>parseFloat(getComputedStyle(x).fontSize)),routeSteps:[...document.querySelectorAll('.route-body ol')].map(x=>x.children.length),workflow:document.querySelector('.workflow').children.length})`);
  if(r.overflow||!r.namesFirst||r.routeSteps.some(n=>n!==3)||r.workflow!==5)throw Error(JSON.stringify(r));
  for(const id of ['copy-dialog','app-dialog','sections-menu']){
   await ev(`document.getElementById('${id}').showModal()`);
   const d=await ev(`(()=>{const d=document.getElementById('${id}');const r=d.getBoundingClientRect();return {id:d.id,overflow:d.scrollWidth>d.clientWidth+1,left:r.left,right:r.right,width:innerWidth}})()`);
   if(d.overflow||d.left<0||d.right>d.width)throw Error(JSON.stringify(d));await ev(`document.getElementById('${id}').close()`);
  }results.push(r);
 }
}
await ev("setLocale('en',false);document.activeElement.blur()");
for(const theme of ['light','dark']){
 await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-color-scheme',value:theme}]});
 await call('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
 await ev("document.querySelector('#editors').scrollIntoView({block:'start',behavior:'instant'})");await sleep(150);await shot(`visual-edit-editorial-20261014/picks-${theme}.png`);
}
await call('Emulation.setDeviceMetricsOverride',{width:390,height:900,deviceScaleFactor:1,mobile:true});await ev("document.querySelector('.research-route').scrollIntoView({block:'start',behavior:'instant'})");await sleep(150);await shot('visual-edit-editorial-20261014/route-mobile.png');
await ev("document.querySelector('#copy-dialog').showModal()");await shot('visual-edit-editorial-20261014/dialog-mobile.png');await ev("document.querySelector('#copy-dialog').close()");
fs.writeFileSync('visual-edit-editorial-20261014/editorial-results.json',JSON.stringify(results,null,2));console.log('24 editorial viewport/language cases and 72 dialog checks passed.');ws.close();
