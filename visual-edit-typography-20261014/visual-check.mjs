import fs from 'node:fs';
import {call,ev,until,shot,ws} from './browser.mjs';
await until("typeof setLocale==='function'");
await call('DOM.enable');await call('CSS.enable');
await ev("document.documentElement.style.scrollBehavior='auto'");
const results=[];
for(const width of [390,1440])for(const scheme of ['light','dark']){
 await call('Emulation.setDeviceMetricsOverride',{width,height:1100,deviceScaleFactor:1,mobile:width===390});
 await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-color-scheme',value:scheme}]});
 await ev("setLocale('en',false);document.querySelector('#reset').click();scrollTo(0,0)");
 await shot(new URL(`cover-${width}-${scheme}.png`,import.meta.url).pathname);
 await ev("document.querySelector('.grid').scrollIntoView()");await shot(new URL(`directory-${width}-${scheme}.png`,import.meta.url).pathname);
 results.push(await ev("({width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth})"));
}
await call('Emulation.setEmulatedMedia',{features:[]});await call('Emulation.setDeviceMetricsOverride',{width:390,height:1100,deviceScaleFactor:1,mobile:true});
for(const locale of ['zh-Hans','zh-Hant','ja','ko']){
 await ev(`setLocale('${locale}',false);scrollTo(0,0);document.fonts.ready`);
 const {root}=await call('DOM.getDocument');const {nodeId}=await call('DOM.querySelector',{nodeId:root.nodeId,selector:'h2'});const fonts=await call('CSS.getPlatformFontsForNode',{nodeId});results.push({locale,fonts});await shot(new URL(`cover-390-${locale}.png`,import.meta.url).pathname);
}
if(results.some(r=>r.overflow))throw Error('Overflow');
fs.writeFileSync(new URL('./visual-checks.json',import.meta.url),JSON.stringify(results,null,2));console.log('Light/dark screenshots captured; actual CJK headline fonts recorded.');ws.close();
