import {ev,until,ws} from './browser.mjs';
await until("navigator.serviceWorker.controller!==null && typeof cards!=='undefined'");
await ev("cards[0].querySelector('.favorite-source').click();countryFilter.value='Germany';update()");
console.log(await ev("({cache:await caches.keys(),favorites:favoriteKeys.size,country:countryFilter.value})"));ws.close();
