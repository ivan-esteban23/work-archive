from pathlib import Path
import json,hashlib
base=Path('/home/ivanaguilera/Work/visual-edit-pwa-20261013'); dist=base/'staged/dist'; p=dist/'index.html'; s=p.read_text()
# Add the app component next to the existing dialogs, reusing their design tokens.
s=s.replace('#copy-dialog{','#copy-dialog,#app-dialog{').replace('#copy-dialog::backdrop{','#copy-dialog::backdrop,#app-dialog::backdrop{').replace('#copy-dialog button{','#copy-dialog button,#app-dialog button{')
s=s.replace('html:lang(zh-Hans) h1,','.app-entry{min-height:var(--control-height);padding:0;text-align:left;border:0;background:transparent;font-size:var(--text-small)}\n#app-dialog{max-height:85dvh;overflow:auto;padding-bottom:max(24px,env(safe-area-inset-bottom))}\n.app-heading{display:flex;align-items:start;justify-content:space-between;gap:18px}.app-heading h2{margin-top:0}.app-actions{display:flex;flex-wrap:wrap;gap:12px;margin:18px 0}.app-status{border-top:1px solid var(--line);padding-top:16px;color:var(--muted);font-size:var(--text-small)}\nhtml:lang(zh-Hans) h1,',1)
s=s.replace('#sections-menu a{','#sections-menu :where(a,.app-entry){')
s=s.replace('#copy-dialog,#empty,','#copy-dialog,#app-dialog,.app-entry,#empty,')
s=s.replace('<button class="print-guide"','<button class="app-entry" type="button" data-app-open hidden aria-haspopup="dialog" aria-controls="app-dialog">Install app</button><button class="print-guide"',1)
s=s.replace('<a href="#landscape">Reading practice</a></nav></dialog>','<a href="#landscape">Reading practice</a><button class="app-entry" type="button" data-app-open hidden aria-haspopup="dialog" aria-controls="app-dialog">Install app</button></nav></dialog>',1)
s=s.replace('<p id="copy-status"','<dialog id="app-dialog" aria-labelledby="app-title"><div class="app-heading"><h2 id="app-title"></h2><form method="dialog"><button id="app-close" type="submit"></button></form></div><p id="app-intro"></p><p id="app-instructions"></p><div class="app-actions"><button id="app-install" type="button" hidden></button><button id="app-update" type="button" hidden></button></div><p id="app-offline" class="app-status" role="status" aria-live="polite"></p><p id="app-storage" class="count"></p></dialog><p id="copy-status"',1)
s=s.replace('script,style,#language,#filter-chips,','script,style,#app-dialog,[data-app-open],#language,#filter-chips,',1)
s=s.replace('function refreshDynamicLabels(){','function refreshDynamicLabels(){window.dispatchEvent(new Event("visual-edit:languagechange"));',1)
# Manifest and icon metadata are linked only on HTTP(S), keeping the vault HTML self-contained.
s=s.replace('</head>','<meta name="theme-color" content="#f4f0e8" media="(prefers-color-scheme:light)"><meta name="theme-color" content="#191715" media="(prefers-color-scheme:dark)"><meta name="apple-mobile-web-app-title" content="The Visual Edit"><script>if(/^https?:$/.test(location.protocol)){for(const [rel,href] of [["manifest","/manifest.webmanifest"],["apple-touch-icon","/icons/apple-touch-icon.png"]]){const link=document.createElement("link");link.rel=rel;link.href=href;document.head.append(link);}}</script></head>',1)
# Added app strings in all six supported languages; dynamic UI does not participate in the static text walker.
messages={
'en':['Install app','The Visual Edit app','Close','Keep the directory close. Open it from your home screen or desktop in its own window.','On iPhone or iPad, open the Share menu, choose Add to Home Screen, then enable Open as Web App if shown.','On Mac, open this site in Safari and choose File → Add to Dock. In Chrome or Edge, use the browser’s install option.','Use your browser’s menu or address-bar install icon. If installation is unavailable, open this site in Chrome, Edge, or Safari.','Install The Visual Edit','Preparing offline access…','Offline ready: the directory, fonts, and cover are saved on this device. External source websites need internet.','Offline access could not be prepared. Reconnect and reopen the app to try again.','App settings','Update available','Update now','A new edition is ready. Update when convenient; your saved sources stay in this browser.','Saved sources are stored in this browser or app on this device. They do not sync between devices; export your collection to keep a copy.','Installation was not completed. You can try again from the browser menu.','Updating…'],
'es':['Instalar app','La app de The Visual Edit','Cerrar','Ten el directorio a mano. Ábrelo desde la pantalla de inicio o el escritorio en su propia ventana.','En iPhone o iPad, abre Compartir, elige Añadir a pantalla de inicio y activa Abrir como app web si aparece.','En Mac, abre este sitio en Safari y elige Archivo → Añadir al Dock. En Chrome o Edge, usa la opción de instalación del navegador.','Usa el menú del navegador o el icono de instalación de la barra de direcciones. Si no está disponible, abre el sitio en Chrome, Edge o Safari.','Instalar The Visual Edit','Preparando el acceso sin conexión…','Disponible sin conexión: el directorio, las fuentes y la portada están guardados en este dispositivo. Los sitios externos necesitan internet.','No se pudo preparar el acceso sin conexión. Reconecta y abre de nuevo la app para reintentar.','Opciones de la app','Actualización disponible','Actualizar ahora','Hay una nueva edición. Actualiza cuando te convenga; tus fuentes guardadas permanecen en este navegador.','Las fuentes guardadas se almacenan en este navegador o app de este dispositivo. No se sincronizan entre dispositivos; exporta tu colección para conservar una copia.','La instalación no se completó. Puedes reintentarlo desde el menú del navegador.','Actualizando…'],
'zh-Hans':['安装应用','The Visual Edit 应用','关闭','将目录留在身边。从主屏幕或桌面在独立窗口中打开。','在 iPhone 或 iPad 上打开分享菜单，选择添加到主屏幕；如显示“作为网页 App 打开”，请启用。','在 Mac 的 Safari 中打开本站，选择文件 → 添加到程序坞。在 Chrome 或 Edge 中使用浏览器安装选项。','使用浏览器菜单或地址栏中的安装图标。如无法安装，请在 Chrome、Edge 或 Safari 中打开本站。','安装 The Visual Edit','正在准备离线访问…','离线内容已就绪：目录、字体和封面已保存在此设备上。外部网站仍需联网。','无法准备离线访问。请重新联网并再次打开应用以重试。','应用设置','有可用更新','立即更新','新版已就绪。方便时更新；已收藏的来源将保留在此浏览器中。','收藏保存在此设备的浏览器或应用中，不会跨设备同步；请导出收藏以保留副本。','安装未完成。可从浏览器菜单重试。','正在更新…'],
'zh-Hant':['安裝應用程式','The Visual Edit 應用程式','關閉','隨時使用目錄。從主畫面或桌面在獨立視窗中開啟。','在 iPhone 或 iPad 開啟分享選單，選擇加入主畫面；如顯示「以網頁 App 開啟」，請啟用。','在 Mac 的 Safari 開啟本站，選擇檔案 → 加入 Dock。在 Chrome 或 Edge 使用瀏覽器安裝選項。','使用瀏覽器選單或網址列的安裝圖示。如無法安裝，請在 Chrome、Edge 或 Safari 開啟本站。','安裝 The Visual Edit','正在準備離線存取…','離線內容已就緒：目錄、字型和封面已儲存在此裝置。外部網站仍需要網路。','無法準備離線存取。請重新連線並再次開啟應用程式以重試。','應用程式設定','有可用更新','立即更新','新版已就緒。方便時更新；已收藏的來源將保留在此瀏覽器。','收藏儲存在此裝置的瀏覽器或應用程式，不會跨裝置同步；請匯出收藏以保留副本。','安裝未完成。可從瀏覽器選單重試。','正在更新…'],
'ja':['アプリをインストール','The Visual Edit アプリ','閉じる','ディレクトリをいつでも手元に。ホーム画面やデスクトップから独立したウィンドウで開けます。','iPhone・iPadでは共有メニューから「ホーム画面に追加」を選び、表示される場合は「Webアプリとして開く」を有効にしてください。','MacではSafariでこのサイトを開き、「ファイル」→「Dockに追加」を選びます。Chrome・Edgeではブラウザのインストール機能を使います。','ブラウザのメニューかアドレスバーのインストールアイコンを使ってください。利用できない場合はChrome、Edge、Safariで開いてください。','The Visual Edit をインストール','オフライン利用を準備中…','オフライン準備完了：ディレクトリ、フォント、表紙をこの端末に保存しました。外部サイトにはインターネット接続が必要です。','オフライン利用を準備できませんでした。接続を確認してアプリを開き直してください。','アプリ設定','更新があります','今すぐ更新','新しい版を利用できます。都合のよいときに更新してください。保存した情報源はこのブラウザに残ります。','保存した情報源はこの端末のブラウザまたはアプリに保存されます。端末間で同期されません。コレクションをエクスポートして控えを残せます。','インストールは完了していません。ブラウザのメニューから再試行できます。','更新中…'],
'ko':['앱 설치','The Visual Edit 앱','닫기','디렉터리를 가까이 두세요. 홈 화면이나 데스크톱에서 독립된 창으로 열 수 있습니다.','iPhone 또는 iPad에서 공유 메뉴를 열고 홈 화면에 추가를 선택하세요. 웹 앱으로 열기가 표시되면 활성화하세요.','Mac의 Safari에서 이 사이트를 열고 파일 → Dock에 추가를 선택하세요. Chrome 또는 Edge에서는 브라우저 설치 기능을 사용하세요.','브라우저 메뉴나 주소 표시줄의 설치 아이콘을 사용하세요. 설치할 수 없다면 Chrome, Edge 또는 Safari에서 이 사이트를 여세요.','The Visual Edit 설치','오프라인 이용 준비 중…','오프라인 준비 완료: 디렉터리, 글꼴, 표지가 이 기기에 저장되었습니다. 외부 웹사이트에는 인터넷이 필요합니다.','오프라인 이용을 준비하지 못했습니다. 다시 연결한 후 앱을 다시 열어 재시도하세요.','앱 설정','업데이트 가능','지금 업데이트','새 버전이 준비되었습니다. 편할 때 업데이트하세요. 저장한 소스는 이 브라우저에 유지됩니다.','저장한 소스는 이 기기의 브라우저 또는 앱에 보관됩니다. 기기 간 동기화되지 않습니다. 컬렉션을 내보내 사본을 보관하세요.','설치가 완료되지 않았습니다. 브라우저 메뉴에서 다시 시도할 수 있습니다.','업데이트 중…']}
js='''
// App installation and offline readiness enhance the hosted page only.
(()=>{
 if(!/^https?:$/.test(location.protocol)||!isSecureContext)return;
 const messages=MESSAGES,dialog=document.querySelector('#app-dialog'),entries=[...document.querySelectorAll('[data-app-open]')],install=document.querySelector('#app-install'),updateButton=document.querySelector('#app-update');
 let deferredPrompt=null,registration=null,offlineState='preparing',installed=false,installDismissed=false,applyingUpdate=false;
 const standalone=matchMedia('(display-mode:standalone)'),appleMobile=/iPad|iPhone|iPod/.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
 const msg=i=>(messages[activeLocale]||messages.en)[i];
 function render(){
  const waiting=!!registration?.waiting;const appMode=installed||standalone.matches||navigator.standalone===true;
  entries.forEach(b=>{b.hidden=false;b.textContent=msg(waiting?12:appMode?11:0);});
  document.querySelector('#app-title').textContent=msg(1);document.querySelector('#app-close').textContent=msg(2);document.querySelector('#app-intro').textContent=msg(3);
  const instructions=document.querySelector('#app-instructions');instructions.hidden=appMode&&!waiting;instructions.textContent=waiting?msg(14):installDismissed?msg(16):appleMobile?msg(4):/Mac/.test(navigator.platform)?msg(5):msg(6);
  install.hidden=appMode||!deferredPrompt;install.textContent=msg(7);updateButton.hidden=!waiting;updateButton.textContent=msg(applyingUpdate?17:13);updateButton.disabled=applyingUpdate;
  document.querySelector('#app-offline').textContent=msg(offlineState==='ready'?9:offlineState==='failed'?10:8);document.querySelector('#app-storage').textContent=msg(15);
 }
 entries.forEach(button=>button.addEventListener('click',()=>{const menu=document.querySelector('#sections-menu');if(menu.open)menu.close();render();dialog.showModal();document.querySelector('#app-close').focus();}));
 window.addEventListener('visual-edit:languagechange',render);standalone.addEventListener('change',render);
 window.addEventListener('beforeinstallprompt',event=>{event.preventDefault();deferredPrompt=event;installDismissed=false;render();});
 window.addEventListener('appinstalled',()=>{installed=true;deferredPrompt=null;render();});
 install.addEventListener('click',async()=>{const prompt=deferredPrompt;if(!prompt)return;deferredPrompt=null;install.disabled=true;try{await prompt.prompt();const choice=await prompt.userChoice;installDismissed=choice.outcome!=='accepted';}catch(e){installDismissed=true;}finally{install.disabled=false;render();}});
 updateButton.addEventListener('click',()=>{if(!registration?.waiting)return;applyingUpdate=true;render();registration.waiting.postMessage({type:'ACTIVATE_UPDATE'});});
 navigator.serviceWorker?.addEventListener('controllerchange',()=>{if(applyingUpdate)location.reload();});
 function checkOffline(){const worker=navigator.serviceWorker.controller||registration?.active;if(!worker)return;const channel=new MessageChannel();channel.port1.onmessage=event=>{offlineState=event.data?.ready?'ready':'failed';channel.port1.close();render();};worker.postMessage({type:'OFFLINE_STATUS'},[channel.port2]);}
 function observe(reg){registration=reg;render();checkOffline();reg.addEventListener('updatefound',()=>{const worker=reg.installing;worker?.addEventListener('statechange',()=>{if(worker.state==='installed'){render();if(!navigator.serviceWorker.controller)navigator.serviceWorker.ready.then(checkOffline);}if(worker.state==='redundant'&&!reg.active){offlineState='failed';render();}});});}
 render();
 if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js',{scope:'/',updateViaCache:'none'}).then(observe).catch(()=>{offlineState='failed';render();});navigator.serviceWorker.ready.then(reg=>{registration=reg;checkOffline();render();});window.addEventListener('online',()=>{registration?.update().catch(()=>{});checkOffline();});document.addEventListener('visibilitychange',()=>{if(!document.hidden){registration?.update().catch(()=>{});checkOffline();}});}else{offlineState='failed';render();}
})();
'''.replace('MESSAGES',json.dumps(messages,ensure_ascii=False))
s=s.replace('</script></body>',js+'</script></body>',1);p.write_text(s)
manifest={'id':'/','name':'The Visual Edit','short_name':'Visual Edit','description':'An editorial directory for visual research and moodboarding.','lang':'en','start_url':'/','scope':'/','display':'standalone','background_color':'#f4f0e8','theme_color':'#302923','icons':[{'src':f'/icons/icon-{n}.png','sizes':f'{n}x{n}','type':'image/png','purpose':'any'} for n in [192,512]]+[{'src':'/icons/maskable-512.png','sizes':'512x512','type':'image/png','purpose':'maskable'}],'shortcuts':[{'name':'Source directory','url':'/#directory'},{'name':'Browse countries','url':'/#asia-browse'}]}
(dist/'manifest.webmanifest').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
version=hashlib.sha256(s.encode()).hexdigest()[:12]
sw='''// Version the offline shell whenever index.html or its app assets change.
const CACHE='visual-edit-shell-VERSION';
const SHELL=['/index.html','/manifest.webmanifest','/favicon.svg','/icons/icon-192.png','/icons/icon-512.png','/icons/maskable-512.png','/icons/apple-touch-icon.png'];
self.addEventListener('install',event=>{event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(SHELL)));});
self.addEventListener('activate',event=>{event.waitUntil((async()=>{for(const name of await caches.keys()){if(name.startsWith('visual-edit-shell-')&&name!==CACHE)await caches.delete(name);}await self.clients.claim();})());});
self.addEventListener('fetch',event=>{
 const request=event.request,url=new URL(request.url);if(request.method!=='GET'||url.origin!==self.location.origin)return;
 if(request.mode==='navigate'&&(url.pathname==='/'||url.pathname==='/index.html')){event.respondWith((async()=>{const cache=await caches.open(CACHE);return await cache.match('/index.html')||fetch(request);})());return;}
 if(SHELL.includes(url.pathname)){event.respondWith((async()=>{const cache=await caches.open(CACHE);return await cache.match(url.pathname)||fetch(request);})());}
});
self.addEventListener('message',event=>{
 if(event.data?.type==='ACTIVATE_UPDATE'){self.skipWaiting();return;}
 if(event.data?.type==='OFFLINE_STATUS'&&event.ports[0]){event.waitUntil((async()=>{const cache=await caches.open(CACHE);const entries=await Promise.all(SHELL.map(path=>cache.match(path)));event.ports[0].postMessage({ready:entries.every(Boolean)});})());}
});
'''.replace('VERSION',version)
(dist/'sw.js').write_text(sw)
print('Staged PWA; HTML bytes',p.stat().st_size,'version',version)
