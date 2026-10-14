import {call,ev,sleep,shot,ws} from './browser.mjs';
await call('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
await ev("document.activeElement.blur();document.documentElement.dataset.theme='light';document.querySelector('#search').scrollIntoView({block:'start'});window.scrollBy(0,-30)");await sleep(250);await shot('visual-edit-navigation-20261014/controls.png');
console.log(await ev("({labels:[...document.querySelectorAll('.filter-panel-body label')].map(x=>x.textContent),targets:[...document.querySelectorAll('#reset,#filter-toggle,#category-filter')].map(x=>({id:x.id,height:x.getBoundingClientRect().height}))})"));ws.close();
