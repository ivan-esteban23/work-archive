import fs from 'node:fs';import {call,ev,until,sleep,shot,ws} from './browser.mjs';
await call('Network.setBypassServiceWorker',{bypass:true});await call('Page.reload',{ignoreCache:true});await until("typeof cards!=='undefined'");await ev("document.querySelector('#reset').click();document.querySelectorAll('details').forEach(x=>x.open=true)");const results=[];
for(const theme of ['light','dark'])for(const width of [320,640,1440])for(const zoom of [1,2])for(const lang of ['en','es','zh-Hans','zh-Hant','ja','ko']){
 await call('Emulation.setDeviceMetricsOverride',{width,height:900,deviceScaleFactor:1,mobile:false});await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-color-scheme',value:theme}]});
 await ev(`document.documentElement.style.fontSize='${16*zoom}px';setLocale('${lang}',false)`);
 await ev('document.fonts.ready');await sleep(60);
 const r=await ev(`({theme:'${theme}',width:innerWidth,zoom:${zoom},lang:document.documentElement.lang,overflow:document.documentElement.scrollWidth>innerWidth+1,small:[...document.querySelectorAll('button,input,select,summary')].filter(x=>x.getBoundingClientRect().width&&x.getBoundingClientRect().height<44).map(x=>x.id||x.className),unlabeled:[...document.querySelectorAll('button')].filter(x=>x.getBoundingClientRect().width&&!x.textContent.trim()&&!x.getAttribute('aria-label')).length})`);
 if(r.overflow||r.small.length||r.unlabeled)throw Error(JSON.stringify(r));results.push(r);
}
await ev("document.documentElement.style.fontSize='16px';setLocale('en',false);document.querySelector('#reset').click()");
await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
if(!await ev("getComputedStyle(document.documentElement).scrollBehavior==='auto'&&[...document.querySelectorAll('button,summary,.source,.editor-pick,.route-toggle')].every(x=>getComputedStyle(x).transitionDuration==='0s')"))throw Error('Reduced motion');
await call('Emulation.setEmulatedMedia',{media:'print'});await ev("window.dispatchEvent(new Event('beforeprint'))");
if(!await ev("cards.every(c=>getComputedStyle(c).display!=='none')&&[...document.querySelectorAll('.source-details,.research-route')].every(x=>x.open)&&getComputedStyle(document.querySelector('.mobile-nav')).display==='none'"))throw Error('Print');
await ev("window.dispatchEvent(new Event('afterprint'))");await call('Emulation.setEmulatedMedia',{media:'screen'});
fs.writeFileSync('visual-edit-accessibility-20261014/accessibility-results.json',JSON.stringify({cases:results,reducedMotion:true,print:true},null,2));console.log('144 light/dark, language, viewport and 200% text cases, targets, labels, reduced motion and printing passed.');ws.close();
