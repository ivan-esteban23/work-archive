import assert from 'node:assert/strict';
import http from 'node:http';
import net from 'node:net';
import {mkdtemp, readFile, rm, writeFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {browser, pause} from './browser.mjs';

const origin='https://visual-edit-ivan.greymelon66.chatgpt.site';
const hostname=new URL(origin).hostname;
const root=path.dirname(new URL(import.meta.url).pathname);
let connected=true,accepted=0,blocked=0,page;
const sockets=new Set();
const proxy=http.createServer((req,res)=>{res.writeHead(502);res.end();});
proxy.on('connect',(req,client,head)=>{
  if(!connected||req.url!==hostname+':443'){blocked++;client.destroy();return;}
  const upstream=net.connect(443,hostname);sockets.add(client);sockets.add(upstream);
  for(const socket of [client,upstream]){socket.on('error',()=>{client.destroy();upstream.destroy();});socket.on('close',()=>sockets.delete(socket));}
  upstream.once('connect',()=>{
    if(!connected){client.destroy();upstream.destroy();return;}
    accepted++;client.write('HTTP/1.1 200 Connection Established\r\n\r\n');
    if(head.length)upstream.write(head);client.pipe(upstream);upstream.pipe(client);
  });
});
await new Promise(resolve=>proxy.listen(0,'127.0.0.1',resolve));
const profile=await mkdtemp(path.join(tmpdir(),'reference-live-profile-'));
process.env.LIVE_PROXY='http://127.0.0.1:'+proxy.address().port;
process.env.LIVE_PROFILE=profile;
const results={origin,physicalDevice:false,installedApp:false,serviceWorkerBypassed:false,checks:[]};
const check=(name,detail={})=>{console.log(name);results.checks.push({name,...detail});};
async function launch(){
  await rm(path.join(profile,'DevToolsActivePort'),{force:true});
  page=await browser((req,res)=>{res.writeHead(404);res.end();});
  await page.call('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await page.call('Emulation.setTouchEmulationEnabled',{enabled:true,maxTouchPoints:1});
}
async function navigate(pathname='/',reload=false){
  const before=await page.evaluate('performance.timeOrigin'),count=page.navigations.length,start=Date.now();
  if(reload)await page.call('Page.reload');else await page.call('Page.navigate',{url:origin+pathname});
  await page.until(`performance.timeOrigin!==${before}`,'Live navigation did not commit');
  await page.until("document.readyState==='complete'&&document.querySelectorAll('.source').length===58",'Live directory did not load');
  await page.evaluate('document.fonts.ready.then(()=>true)');await pause(300);
  assert.equal(page.navigations.length,count+1,'Unexpected navigation/reload loop');
  return Date.now()-start;
}
async function state(){return page.evaluate(`({stored:{...localStorage},theme:document.documentElement.dataset.theme,lang:document.documentElement.lang,favorites:favoriteKeys.size,country:document.querySelector('#country-filter').value,controlled:!!navigator.serviceWorker.controller,cards:cards.length})`);}
let saved;
async function verify(){assert.deepEqual(await state(),saved);}
try{
  await launch();await navigate();await page.until('!!navigator.serviceWorker.controller','Live worker not controlling');
  const local=await readFile('/home/ivanaguilera/Work/visual-edit-public/dist/sw.js');
  const worker=await page.evaluate("fetch('/sw.js',{cache:'no-store'}).then(r=>r.text())");
  assert.equal(createHash('sha256').update(worker).digest('hex'),createHash('sha256').update(local).digest('hex'));
  assert.ok(await page.evaluate("(async()=>{const c=await caches.open('visual-edit-shell-mobile-ui-20261014-v3'),r=await c.match('/index.html');return !!r&&(await r.text()).includes('translateDOM();update();if(persist)')})()"));
  check('Live worker matches deployed v44 source; cached HTML includes search fix');
  for(const width of [320,390]){
    await page.call('Emulation.setDeviceMetricsOverride',{width,height:844,deviceScaleFactor:1,mobile:true});
    const layout=await page.evaluate("({width:innerWidth,document:document.documentElement.scrollWidth,controls:[...document.querySelectorAll('.theme-toggle,.language-switch')].map(e=>({left:e.getBoundingClientRect().left,right:e.getBoundingClientRect().right}))})");
    assert.ok(layout.document<=layout.width);assert.ok(layout.controls.every(e=>e.left>=0&&e.right<=layout.width));check('Live mobile viewport '+width+'px',{layout});
  }
  await page.evaluate(`(()=>{document.querySelector('.favorite-source').click();if(document.documentElement.dataset.theme==='dark')document.querySelector('[data-theme-toggle]').click();document.querySelector('[data-theme-toggle]').click();const l=document.querySelector('#language');l.value='es';l.dispatchEvent(new Event('change'));const c=document.querySelector('#country-filter');c.value='Japan';c.dispatchEvent(new Event('change'));})()`);
  saved=await state();assert.equal(saved.favorites,1);assert.equal(saved.theme,'dark');assert.equal(saved.lang,'es');
  const readiness=await page.evaluate(`new Promise(resolve=>{const m=new MessageChannel();m.port1.onmessage=e=>{m.port1.close();resolve(e.data);};navigator.serviceWorker.controller.postMessage({type:'OFFLINE_STATUS'},[m.port2]);})`);
  assert.ok(readiness.ready);assert.ok(accepted>0);check('Seven-asset live offline shell reports ready; preferences saved');
  const onlineMs=await navigate('',true);await verify();check('Live online reload preserves preferences',{durationMs:onlineMs});
  connected=false;for(const socket of sockets)socket.destroy();
  await page.call('Network.emulateNetworkConditions',{offline:true,latency:0,downloadThroughput:-1,uploadThroughput:-1});
  const offlineMs=await navigate('',true);await verify();check('Live root reload with proxy disconnected',{durationMs:offlineMs});
  await page.call('Page.navigate',{url:'about:blank'});await page.until("location.href==='about:blank'&&document.readyState==='complete'");
  await navigate('/index.html#directory?country=Japan');await verify();check('Reopen live /index.html offline after leaving app page');
  assert.deepEqual(page.exceptions,[]);await page.close();page=null;
  await launch();await page.call('Network.emulateNetworkConditions',{offline:true,latency:0,downloadThroughput:-1,uploadThroughput:-1});
  await navigate('/#directory?country=Japan');await verify();check('Full Chromium restart while disconnected retains cached page and preferences');
  assert.deepEqual(page.exceptions,[]);
  connected=true;await page.call('Network.emulateNetworkConditions',{offline:false,latency:0,downloadThroughput:-1,uploadThroughput:-1});
  await navigate('',true);await verify();check('Reconnect and reload without loops or preference loss');
  results.passed=true;results.proxy={accepted,blocked};
}catch(error){results.passed=false;results.error=error.stack;process.exitCode=1;}
finally{
  if(page)await page.close();for(const socket of sockets)socket.destroy();await new Promise(resolve=>proxy.close(resolve));await rm(profile,{recursive:true,force:true});
  await writeFile(root+'/results.json',JSON.stringify(results,null,2)+'\n');console.log(JSON.stringify(results,null,2));
}
