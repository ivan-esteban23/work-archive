import fs from 'node:fs';
import {call,ev,until,ws} from './browser.mjs';
const errors=[];ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')errors.push(m.params.exceptionDetails.text)});
await until("document.querySelectorAll('.source').length===58 && typeof setLocale==='function'");
const names=await ev("cards.map(c=>c.querySelector('h3 a').textContent.replace('↗','').trim())");
const expected=[...names].sort((a,b)=>a.normalize('NFKD').toLowerCase()<b.normalize('NFKD').toLowerCase()?-1:1);
if(JSON.stringify(names)!==JSON.stringify(expected))throw Error('Directory is not alphabetical');
if(!await ev("cards.every((c,i)=>c.querySelector('.card-meta>span').textContent===String(i+1).padStart(2,'0'))"))throw Error('Card numbering');
const result=[];
for(const width of [390,768,1440]){
 await call('Emulation.setDeviceMetricsOverride',{width,height:900,deviceScaleFactor:1,mobile:width===390});
 for(const locale of ['en','es','zh-Hans','zh-Hant','ja','ko']){
 await ev(`setLocale('${locale}',false); document.querySelector('#reset').click();`);
 const r=await ev(`({width:innerWidth,locale:document.documentElement.lang,total:cards.length,visible:cards.filter(c=>!c.hidden).length,overflow:document.documentElement.scrollWidth>innerWidth,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).length,newText:cards.find(c=>c.querySelector('h3 a').textContent.includes('Booooooom')).querySelector('.source-purpose').textContent})`);
 if(r.total!==58||r.visible!==58||r.overflow||r.brokenImages)throw Error(JSON.stringify(r));result.push(r);
 }
}
await ev("setLocale('en',false); search.value='Rijksmuseum'; update();");if(await ev("cards.filter(c=>!c.hidden).length")!==1)throw Error('Search');
await ev("document.querySelector('#reset').click(); countryFilter.value='Germany'; update();");if(await ev("cards.filter(c=>!c.hidden).length")!==2)throw Error('Country filter');
await ev("document.querySelector('#reset').click(); const b=cards.find(c=>c.querySelector('h3 a').textContent.includes('Colossal')).querySelector('.favorite-source');b.click();");if(!await ev("favoriteKeys.has('https://www.thisiscolossal.com/')"))throw Error('Favorite');
await call('Page.reload');await until("typeof cards!=='undefined' && cards.length===58");if(!await ev("favoriteKeys.has('https://www.thisiscolossal.com/')"))throw Error('Favorite persistence');
if(errors.length)throw Error(JSON.stringify(errors));fs.writeFileSync(new URL('./qa-results.json',import.meta.url),JSON.stringify({cases:result,search:true,countryFilter:true,favorites:true,errors},null,2));console.log('Alphabetical ordering, numbering, 18 viewport/language cases, filters, and favorite persistence passed.');ws.close();
