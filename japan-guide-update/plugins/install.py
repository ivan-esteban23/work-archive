from pathlib import Path
import json,shutil,hashlib,subprocess,datetime
stage=Path('/home/ivanaguilera/Work/japan-guide-update/plugins')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
config=vault/'.obsidian/community-plugins.json'
backup=stage/('backup-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'));backup.mkdir()
def version(v):return tuple(int(x) for x in v.split('.')[:3])
sources=[]
for src in sorted(stage.glob('*/source.json')):
 info=json.loads(src.read_text());m=info['manifest']
 assert version(m.get('minAppVersion','0.0.0'))<=version('1.14.4'),m
 assert m['id'] and '/' not in m['id']
 result=subprocess.run(['node','--check',str(src.parent/'main.js')],capture_output=True,text=True)
 assert result.returncode==0,(m['name'],result.stderr)
 for name,digest in info['files'].items():assert hashlib.sha256((src.parent/name).read_bytes()).hexdigest()==digest
 sources.append((src.parent,info))
assert len(sources)==7
shutil.copy2(config,backup/config.name)
enabled=json.loads(config.read_text());assert isinstance(enabled,list)
report=[]
for folder,info in sources:
 m=info['manifest'];dest=vault/'.obsidian/plugins'/m['id']
 if dest.exists():shutil.copytree(dest,backup/m['id'])
 dest.mkdir(parents=True,exist_ok=True)
 for name,digest in info['files'].items():
  shutil.copy2(folder/name,dest/name)
  assert hashlib.sha256((dest/name).read_bytes()).hexdigest()==digest
 if m['id'] not in enabled:enabled.append(m['id'])
 report.append({'name':m['name'],'id':m['id'],'version':m['version'],'source':info['url']})
config.write_text(json.dumps(enabled,indent=2)+'\n')
assert 'obsidian-map-view' in enabled
assert len(enabled)==len(set(enabled))
report={'installed':report,'enabled':enabled,'backup':str(backup),'verified':['minimum app versions','JavaScript syntax','copied file SHA256 hashes','enabled plugin registry']}
(stage/'install-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
