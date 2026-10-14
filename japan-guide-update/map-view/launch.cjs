const {app} = require('electron');
app.setName('obsidian');
app.setPath('userData','/home/ivanaguilera/.config/obsidian');
app.commandLine.appendSwitch('remote-debugging-port','9228');
app.setAppPath('/usr/lib/obsidian/app.asar');
process.argv = [process.argv[0], '/usr/lib/obsidian/app.asar'];
require('/usr/lib/obsidian/app.asar');
