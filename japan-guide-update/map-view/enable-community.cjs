const {app, BrowserWindow, protocol} = require('electron');
app.setName('obsidian');
app.setPath('userData','/home/ivanaguilera/.config/obsidian');
protocol.registerSchemesAsPrivileged([{scheme:'app',privileges:{standard:true,secure:true,supportFetchAPI:true}}]);
app.whenReady().then(async () => {
  protocol.handle('app', () => new Response('<!doctype html><title>Plugin activation</title>'));
  const window = new BrowserWindow({show:false,webPreferences:{nodeIntegration:false,contextIsolation:true}});
  await window.loadURL('app://obsidian.md/index.html');
  const result = await window.webContents.executeJavaScript(`(() => {
    const key = 'enable-plugin-8a68d1bfae31fe54';
    const before = localStorage.getItem(key);
    localStorage.setItem(key,'true');
    return {before, after:localStorage.getItem(key)};
  })()`);
  console.log(JSON.stringify(result));
  window.destroy();
  app.quit();
}).catch(error => {console.error(error);app.exit(1);});
