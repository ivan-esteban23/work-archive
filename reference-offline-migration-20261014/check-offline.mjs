import {execFileSync,spawn} from 'node:child_process';
import {mkdtemp,readFile,writeFile,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import path from 'node:path';
import http from 'node:http';
const repo='/home/ivanaguilera/Work/visual-edit-public',root='/home/ivanaguilera/Work/reference-offline-migration-20261014';
const git=(...args)=>execFileSync('git',['-C',repo,...args],{maxBuffer:30*1024*1024});
const old='228912190b90435c10a9acbc12b99f068e33c6bf';
const assets=new Map();for(const p of git('ls-files','dist/').toString().trim().split('\n'))assets.set('/'+p.slice(5),await readFile(repo+'/'+p));
const oldHTML=git('show',old+':dist/index.html'),oldSW=git('show',old+':dist/sw.js');
const oldCache=oldSW.toString().match(/const CACHE='([^']+)'/)[1],newCache=assets.get('/sw.js').toString().match(/const CACHE='([^']+)'/)[1];
let version='old',mode='online',requests=[];
const server=http.createServer((req,res)=>{
 const p=new URL(req.url,'http://localhost').pathname;
 requests.push({path:p,version,mode});
 if(mode==='broken-install'&&p==='/icons/icon-512.png'){res.writeHead(503);res.end('Unavailable icon');return;}
 if(mode==='error'&&(p==='/'||p==='/index.html')){res.writeHead(503);res.end('Unavailable');return;}
 if(mode==='slow'&&p==='/'){setTimeout(()=>{if(!res.destroyed){res.writeHead(200,{'Content-Type':'text/html'});res.end(assets.get('/index.html'));}},6500);return;}
 if(p==='/index.html'){res.writeHead(302,{Location:'/'});res.end();return;}
 const key=p==='/'?'/index.html':p;
 const body=version==='old'&&key==='/index.html'?oldHTML:version==='old'&&key==='/sw.js'?oldSW:assets.get(key);
 if(!body){res.writeHead(404);res.end();return;}
 res.setHeader('Cache-Control','no-store');res.setHeader('Content-Type',key.endsWith('.html')?'text/html; charset=utf-8':key.endsWith('.js')?'text/javascript':key.endsWith('.svg')?'image/svg+xml':key.endsWith('.webmanifest')?'application/manifest+json':'image/png');res.end(body);
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
const origin='http://127.0.0.1:'+server.address().port,profile=await mkdtemp(path.join(tmpdir(),'reference-offline-'));
const chrome=spawn('/usr/bin/chromium',['--headless','--no-sandbox','--disable-dev-shm-usage','--disable-gpu','--no-first-run','--no-default-browser-check','--remote-debugging-port=0','--user-data-dir='+profile,'about:blank'],{stdio:'ignore'});
const pause=ms=>new Promise(r=>setTimeout(r,ms));const assert=(ok,label)=>{if(!ok)throw Error(label);};let ws,phase='startup';const results={oldCache,newCache,cases:[],serviceWorkerBypassed:false};
try{
 let port;for(let n=0;n<200;n++){try{port=(await readFile(path.join(profile,'DevToolsActivePort'),'utf8')).split('\n')[0];break;}catch{await pause(50);}}assert(port,'Chromium did not start');
 const tabs=await(await fetch('http://127.0.0.1:'+port+'/json/list')).json();ws=new WebSocket(tabs.find(x=>x.type==='page').webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
 let id=0;const pending=new Map(),exceptions=[];
 ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id){pending.get(m.id)?.(m);pending.delete(m.id);}else if(m.method==='Runtime.exceptionThrown')exceptions.push(m.params.exceptionDetails.text);});
 const call=(method,params={})=>new Promise((resolve,reject)=>{const n=++id,timer=setTimeout(()=>{pending.delete(n);reject(Error('CDP timeout: '+method));},20000);pending.set(n,m=>{clearTimeout(timer);m.error?reject(Error(JSON.stringify(m.error))):resolve(m.result);});ws.send(JSON.stringify({id:n,method,params}));});
 const ev=async expression=>{const r=await call('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
 const until=async(expression,label)=>{for(let n=0;n<200;n++){try{if(await ev(expression))return;}catch(e){if(!/context|navigat/i.test(e.message))throw e;}await pause(75);}throw Error(label);};
 const mark=async p=>{phase=p;console.log(p);await writeFile(root+'/offline-progress.json',JSON.stringify({phase}));};
 await call('Page.enable');await call('Runtime.enable');await call('Network.enable');
 await call('Page.navigate',{url:origin+'/'});await until("document.readyState==='complete'&&document.querySelectorAll('.source').length===58",'Old page did not load');
 await until("!!navigator.serviceWorker.controller",'Old worker did not claim page');
 await until(`caches.open(${JSON.stringify(oldCache)}).then(c=>c.match('/index.html')).then(Boolean)`,'Old shell missing');
 await mark('seed-old-user-state');
 const saved=await ev(`(()=>{document.querySelector('.favorite-source').click();document.querySelectorAll('.source')[2].querySelector('.favorite-source').click();document.querySelector('[data-theme-choice=dark]').click();const l=document.querySelector('#language');l.value='es';l.dispatchEvent(new Event('change'));return {...localStorage};})()`);
 assert(JSON.parse(saved['visual-edit-favorites-v1']).length===2&&saved['visual-edit-language']==='es'&&saved['visual-edit-theme']==='dark','State seeding failed: '+JSON.stringify(saved));
 await ev("caches.open('unrelated-project-cache').then(c=>c.put('/unrelated',new Response('keep'))) ");
 await mark('interrupted-update-keeps-old-worker');version='new';mode='broken-install';
 const rejected=await ev(`new Promise(async(resolve,reject)=>{const r=await navigator.serviceWorker.getRegistration();const previous=r.active;const t=setTimeout(()=>reject(Error('Failed install test timed out')),15000);r.addEventListener('updatefound',()=>{const worker=r.installing;worker.addEventListener('statechange',()=>{if(worker.state==='redundant'){clearTimeout(t);resolve({previousStillActive:r.active===previous,oldCache:null});}});},{once:true});await r.update();})`);
 assert(rejected.previousStillActive,'Failed install replaced active worker');assert(await ev(`caches.keys().then(k=>k.includes(${JSON.stringify(oldCache)}))`),'Failed install removed old shell');results.cases.push({case:phase,previousStillActive:true,oldCacheRetained:true});
 await mark('install-new-worker');mode='online';
 await ev(`new Promise(async(resolve,reject)=>{const r=await navigator.serviceWorker.getRegistration();const previous=r.active;const t=setTimeout(()=>reject(Error('Upgrade timed out')),15000);navigator.serviceWorker.addEventListener('controllerchange',()=>{clearTimeout(t);resolve(true);},{once:true});await r.update();if(r.active!==previous&&navigator.serviceWorker.controller===r.active){clearTimeout(t);resolve(true);}})`);
 await until(`caches.keys().then(keys=>keys.includes(${JSON.stringify(newCache)})&&!keys.includes(${JSON.stringify(oldCache)}))`,'Cache migration failed');
 await mark('prepare-offline-first-navigation');
 const navigate=async(url,reload=false)=>{const prior=await ev('performance.timeOrigin');const start=Date.now();if(reload)await call('Page.reload');else await call('Page.navigate',{url:origin+url});await until('performance.timeOrigin!=='+prior,'Navigation did not commit');await until("document.readyState==='complete'&&document.querySelectorAll('.source').length===58&&!!document.querySelector('.language-code')",'New page did not finish loading');return Date.now()-start;};
 const verify=async label=>{const state=await ev(`({stored:{...localStorage},theme:document.documentElement.dataset.theme,lang:document.documentElement.lang,favorites:favoriteKeys.size,controlled:!!navigator.serviceWorker.controller,cards:document.querySelectorAll('.source').length})`);assert(JSON.stringify(state.stored)===JSON.stringify(saved)&&state.theme==='dark'&&state.lang==='es'&&state.favorites===2&&state.controlled&&state.cards===58,label+': state changed');return state;};
 await call('Network.emulateNetworkConditions',{offline:true,latency:0,downloadThroughput:-1,uploadThroughput:-1});
 await mark('offline-first-reload-after-upgrade');let duration=await navigate('/',true);results.cases.push({case:phase,durationMs:duration,state:await verify(phase)});
 await call('Network.emulateNetworkConditions',{offline:false,latency:0,downloadThroughput:-1,uploadThroughput:-1});await mark('online-reload-after-upgrade');duration=await navigate('/',true);results.cases.push({case:phase,durationMs:duration,state:await verify(phase)});
 await mark('redirected-index-online');duration=await navigate('/index.html');results.cases.push({case:phase,durationMs:duration,state:await verify(phase)});
 for(const test of ['error','slow','offline']){
  await mark(test+'-navigation');mode=test==='offline'?'online':test;
  if(test==='offline')await call('Network.emulateNetworkConditions',{offline:true,latency:0,downloadThroughput:-1,uploadThroughput:-1});
  for(const target of test==='offline'?['/','/index.html']:['/']){duration=await navigate(target);assert(duration<10000,'Fallback took too long');results.cases.push({case:phase,path:target,durationMs:duration,state:await verify(phase)});}
 }
 const cacheState=await ev(`(async()=>{const keys=await caches.keys();const c=await caches.open(${JSON.stringify(newCache)});const paths=await c.keys();const ready=await new Promise(resolve=>{const m=new MessageChannel();m.port1.onmessage=e=>resolve(e.data.ready);navigator.serviceWorker.controller.postMessage({type:'OFFLINE_STATUS'},[m.port2]);});return {keys,paths:paths.map(r=>new URL(r.url).pathname),ready};})()`);
 assert(cacheState.ready&&cacheState.paths.length===7&&cacheState.keys.includes('unrelated-project-cache')&&!cacheState.keys.includes(oldCache),'Offline shell/cache isolation failed');assert(exceptions.length===0,'Runtime exceptions');
 results.cacheState=cacheState;results.exceptions=exceptions;results.passed=true;await writeFile(root+'/offline-results.json',JSON.stringify(results,null,2)+'\n');console.log(JSON.stringify(results,null,2));
}catch(error){results.passed=false;results.phase=phase;results.error=error.message;results.requests=requests;await writeFile(root+'/offline-results.json',JSON.stringify(results,null,2)+'\n');throw error;}
finally{ws?.close();chrome.kill('SIGTERM');server.closeAllConnections();await new Promise(r=>server.close(r));await pause(250);await rm(profile,{recursive:true,force:true}).catch(()=>{});}
