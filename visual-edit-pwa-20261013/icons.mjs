import fs from 'node:fs';import {ev,ws} from './browser.mjs';
const root='/home/ivanaguilera/Work/visual-edit-pwa-20261013/staged/dist';fs.mkdirSync(root+'/icons',{recursive:true});
const original=fs.readFileSync(root+'/favicon.svg','utf8');
for(const [name,size,maskable] of [['icon-192',192,false],['icon-512',512,false],['apple-touch-icon',180,false],['maskable-512',512,true]]){
 const svg=maskable?`<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><rect width="512" height="512" fill="#302923"/><svg x="96" y="96" width="320" height="320" viewBox="0 0 64 64">${original.replace(/^<svg[^>]*>/,'').replace(/<\/svg>$/,'')}</svg></svg>`:original;
 const data=await ev(`(async()=>{const i=new Image();i.src=${JSON.stringify('data:image/svg+xml;base64,'+Buffer.from(svg).toString('base64'))};await i.decode();const c=document.createElement('canvas');c.width=c.height=${size};c.getContext('2d').drawImage(i,0,0,${size},${size});return c.toDataURL('image/png').split(',')[1];})()`);
 fs.writeFileSync(root+'/icons/'+name+'.png',Buffer.from(data,'base64'));
}
console.log('Exported four PNG icons from the existing VE monogram');ws.close();
