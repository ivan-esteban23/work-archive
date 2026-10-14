import fs from 'node:fs';
import {call,ev,until,shot,ws} from './browser.mjs';
await call('Page.reload',{ignoreCache:true});await until("typeof setLocale==='function'");await ev("setLocale('en',false);document.documentElement.style.scrollBehavior='auto'");await call('DOM.enable');await call('CSS.enable');
const report=[];
for(const scheme of ['light','dark']){
 await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-color-scheme',value:scheme}]});
 const checks=await ev(`(()=>{const cs=getComputedStyle(document.documentElement);const v=n=>cs.getPropertyValue('--'+n).trim();const L=c=>{let x=c.replace('#','');let a=[0,2,4].map(i=>parseInt(x.slice(i,i+2),16)/255);return a.map(z=>z<=.04045?z/12.92:((z+.055)/1.055)**2.4).reduce((n,z,i)=>n+z*[.2126,.7152,.0722][i],0)};const ratio=(a,b)=>{let [x,y]=[L(a),L(b)].sort((a,b)=>a-b);return (y+.05)/(x+.05)};const results=[];for(const fg of ['ink','muted','link'])for(const bg of ['page','surface','soft'])results.push({fg,bg,ratio:ratio(v(fg),v(bg)),min:4.5});for(const bg of ['page','surface','soft'])for(const fg of ['focus','control-line'])results.push({fg,bg,ratio:ratio(v(fg),v(bg)),min:3});for(const bg of ['strong','accent'])results.push({fg:'on-strong',bg,ratio:ratio(v('on-strong'),v(bg)),min:4.5});return {palette:Object.fromEntries(['page','surface','ink','muted','line','accent','soft','control-line','focus','link','strong','on-strong'].map(n=>[n,v(n)])),results};})()`);
 if(checks.results.some(x=>x.ratio<x.min))throw Error(scheme+' '+JSON.stringify(checks));
 const boundary=await ev("getComputedStyle(document.querySelector('#search')).borderTopColor");if(boundary!=='rgb(141, 130, 116)')throw Error('Control boundary '+boundary);
 const {root}=await call('DOM.getDocument');const {nodeId}=await call('DOM.querySelector',{nodeId:root.nodeId,selector:'.filters button[aria-pressed=true]'});await call('CSS.forcePseudoState',{nodeId,forcedPseudoClasses:['hover']});
 const selected=await ev("(()=>{const c=getComputedStyle(document.querySelector('.filters button[aria-pressed=true]'));return {color:c.color,background:c.backgroundColor,countOpacity:getComputedStyle(document.querySelector('.filters button[aria-pressed=true] .filter-count')).opacity}})()");
 const rgb=h=>'rgb('+[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)).join(', ')+')';if(selected.color!==rgb(checks.palette['on-strong'])||selected.background!==rgb(checks.palette.accent)||selected.countOpacity!=='1')throw Error('Selected hover '+JSON.stringify(selected));await call('CSS.forcePseudoState',{nodeId,forcedPseudoClasses:[]});
 for(const width of [390,1440]){
 await call('Emulation.setDeviceMetricsOverride',{width,height:1100,deviceScaleFactor:1,mobile:width===390});await ev('scrollTo(0,0)');await shot(new URL(`cover-${width}-${scheme}.png`,import.meta.url).pathname);await ev("document.querySelector('.grid').scrollIntoView()");await shot(new URL(`cards-${width}-${scheme}.png`,import.meta.url).pathname);
 }
 report.push({scheme,...checks,selectedHover:selected});
}
fs.writeFileSync(new URL('./contrast-results.json',import.meta.url),JSON.stringify(report,null,2));console.log('34 palette contrast pairings and selected-hover/count checks passed in light/dark mode.');ws.close();
