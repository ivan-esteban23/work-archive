const tabs = await (await fetch('http://127.0.0.1:9228/json/list')).json();
console.log(tabs.map(t => ({title:t.title,type:t.type})));
const tab = tabs.find(t => t.type === 'page');
if (!tab) process.exit(1);
const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise(resolve => ws.onopen = resolve);
const replies = new Map();
ws.onmessage = event => {
  const message = JSON.parse(event.data);
  if (message.id) replies.get(message.id)?.(message);
};
let id = 0;
async function run(expression) {
  const current = ++id;
  const promise = new Promise(resolve => replies.set(current, resolve));
  ws.send(JSON.stringify({id:current,method:'Runtime.evaluate',params:{expression,awaitPromise:true,returnByValue:true}}));
  return await promise;
}
const expression = `JSON.stringify({vault:app.vault.getName(),enabled:app.plugins.isEnabled(),mapLoaded:!!app.plugins.plugins['obsidian-map-view'],methods:Object.getOwnPropertyNames(Object.getPrototypeOf(app.plugins)).filter(x=>/enable|loadManifests|setEnable/i.test(x))})`;
console.log(JSON.stringify(await run(expression)));
ws.close();
