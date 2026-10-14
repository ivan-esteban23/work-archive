import {call,ev,sleep,shot,ws} from './browser.mjs';
await call('Emulation.setDeviceMetricsOverride',{width:320,height:900,deviceScaleFactor:1,mobile:false});await ev("document.documentElement.style.fontSize='32px';setLocale('es',false);document.activeElement.blur();document.querySelector('#search').scrollIntoView({behavior:'instant',block:'start'})");await sleep(200);await shot('visual-edit-accessibility-20261014/zoom-controls.png');
await ev("cards[0].scrollIntoView({behavior:'instant',block:'start'})");await shot('visual-edit-accessibility-20261014/zoom-card.png');ws.close();
