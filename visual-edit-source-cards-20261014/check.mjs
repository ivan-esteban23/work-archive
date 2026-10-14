import fs from 'node:fs';
import {call,ev,until,ws} from './browser.mjs';
await call('Page.reload',{ignoreCache:true});
const errors=[];ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.method==='Runtime.exceptionThrown')errors.push(m.params.exceptionDetails.text)});
await until("document.querySelectorAll('.source').length===58 && typeof setLocale==='function'");
const names=await ev("cards.map(c=>c.querySelector('h3 a').textContent.replace('↗','').trim())");
const expected=[...names].sort((a,b)=>a.normalize('NFKD').toLowerCase()<b.normalize('NFKD').toLowerCase()?-1:1);
if(JSON.stringify(names)!==JSON.stringify(expected))throw Error('Directory is not alphabetical');
if(!await ev("cards.every((c,i)=>c.querySelector('.card-meta>span').textContent===String(i+1).padStart(2,'0'))"))throw Error('Card numbering');
if(!await ev("cards.every(c=>{const names=[...c.children].map(e=>e.className);return names.join('|')==='brand-row|source-purpose|source-metadata|source-details|source-actions' && c.querySelector('.brand-row h3') && c.querySelector('.source-metadata .comparison')})"))throw Error('Card hierarchy');
const result=[];await ev("document.querySelectorAll('.source-details,.research-route').forEach(d=>d.open=true)");
await ev('document.fonts.ready');

for(const width of [320,390,640,768,1000,1200,1440]){
 await call('Emulation.setDeviceMetricsOverride',{width,height:900,deviceScaleFactor:1,mobile:width===390});
 for(const locale of ['en','es','zh-Hans','zh-Hant','ja','ko']){
 await ev(`setLocale('${locale}',false); document.querySelector('#reset').click();`);
 const r=await ev(`({width:innerWidth,locale:document.documentElement.lang,total:cards.length,visible:cards.filter(c=>!c.hidden).length,overflow:document.documentElement.scrollWidth>innerWidth,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).length,layout:{columns:getComputedStyle(document.querySelector('.grid')).gridTemplateColumns.split(' ').length,gridX:document.querySelector('.grid').getBoundingClientRect().x,headingX:document.querySelector('#directory .section-top').getBoundingClientRect().x,controlsX:document.querySelector('.directory-tools').getBoundingClientRect().x},alignedActions:cards.slice(0,innerWidth<640?1:innerWidth<1200?2:3).every(c=>Math.abs(c.querySelector('.source-actions').getBoundingClientRect().bottom-cards[0].querySelector('.source-actions').getBoundingClientRect().bottom)<1),type:{body:parseFloat(getComputedStyle(document.body).fontSize),cover:parseFloat(getComputedStyle(document.querySelector('.hero h1')).fontSize),section:parseFloat(getComputedStyle(document.querySelector('h2')).fontSize),title:parseFloat(getComputedStyle(document.querySelector('.source h3')).fontSize)},newText:cards.find(c=>c.querySelector('h3 a').textContent.includes('Booooooom')).querySelector('.source-purpose').textContent})`);
 if(r.layout.columns!==(width<640?1:width<1200?2:3)||r.layout.gridX!==r.layout.headingX||r.layout.gridX!==r.layout.controlsX)throw Error('Grid alignment '+JSON.stringify(r));
 if(r.type.body<16||r.type.body>18||r.type.cover<48||r.type.cover>88||r.type.section<32||r.type.section>48||r.type.title<20||r.type.title>24)throw Error('Type scale '+JSON.stringify(r));
 if(!r.alignedActions)throw Error('Action alignment '+JSON.stringify(r));
 if(r.total!==58||r.visible!==58||r.overflow||r.brokenImages)throw Error(JSON.stringify(r));result.push(r);
 }
}
await ev("setLocale('en',false); search.value='Rijksmuseum'; update();");if(await ev("cards.filter(c=>!c.hidden).length")!==1)throw Error('Search');
await ev("document.querySelector('#reset').click(); countryFilter.value='Germany'; update();");if(await ev("cards.filter(c=>!c.hidden).length")!==2)throw Error('Country filter');
await ev("document.querySelector('#reset').click(); const b=cards.find(c=>c.querySelector('h3 a').textContent.includes('Colossal')).querySelector('.favorite-source');if(b.getAttribute('aria-pressed')!=='true')b.click();");if(!await ev("favoriteKeys.has('https://www.thisiscolossal.com/')"))throw Error('Favorite');
await call('Page.reload');await until("typeof cards!=='undefined' && cards.length===58");if(!await ev("favoriteKeys.has('https://www.thisiscolossal.com/')"))throw Error('Favorite persistence');
if(errors.length)throw Error(JSON.stringify(errors));fs.writeFileSync(new URL('./qa-results.json',import.meta.url),JSON.stringify({cases:result,search:true,countryFilter:true,favorites:true,errors},null,2));console.log('Type scale, alphabetical ordering, 42 viewport/language cases, filters, and favorites passed.');ws.close();
