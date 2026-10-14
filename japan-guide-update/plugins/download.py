from pathlib import Path
import urllib.request,urllib.error,json,concurrent.futures,hashlib
root=Path('/home/ivanaguilera/Work/japan-guide-update/plugins')
repos=['chhoumann/quickadd','st3v3nmw/obsidian-spaced-repetition','scambier/obsidian-omnisearch','RyotaUshio/obsidian-pdf-plus','mProjectsCode/obsidian-meta-bind-plugin','pyrochlore/obsidian-tracker','Sergei-Korneev/obsidian-local-images-plus']
def get(url):
 return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ObsidianPluginSetup/1.0','Accept':'application/vnd.github+json'}),timeout=60).read()
def download(repo):
 target=root/repo.split('/')[-1];target.mkdir(exist_ok=True)
 try:
  release=json.loads(get('https://api.github.com/repos/'+repo+'/releases/latest'))
  urls={a['name']:a['browser_download_url'] for a in release['assets']}
  if 'main.js' not in urls or 'manifest.json' not in urls:raise ValueError('Release missing required plugin assets: '+str(list(urls)))
  provenance={'repo':repo,'release':release['tag_name'],'url':release['html_url']}
 except urllib.error.HTTPError as e:
  if e.code!=404 or repo!='Sergei-Korneev/obsidian-local-images-plus':raise
  prefix='https://raw.githubusercontent.com/'+repo+'/main/obsidian_local_images_plus_latest/'
  urls={n:prefix+n for n in ['main.js','manifest.json','styles.css']}
  provenance={'repo':repo,'release':'author-published distribution','url':'https://github.com/'+repo+'/tree/main/obsidian_local_images_plus_latest'}
 for name in ['manifest.json','main.js','styles.css']:
  if name in urls:
   try:(target/name).write_bytes(get(urls[name]))
   except urllib.error.HTTPError as e:
    if name!='styles.css' or e.code!=404:raise
 manifest=json.loads((target/'manifest.json').read_text())
 provenance.update(manifest=manifest,files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in target.iterdir() if p.name in ['main.js','manifest.json','styles.css']})
 (target/'source.json').write_text(json.dumps(provenance,indent=2))
 return {'name':manifest['name'],'id':manifest['id'],'version':manifest['version'],'minimum':manifest.get('minAppVersion'),'distribution':provenance['release']}
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 futures={pool.submit(download,r):r for r in repos}
 for f in concurrent.futures.as_completed(futures):
  try:result=f.result();results.append(result);print(json.dumps(result),flush=True)
  except Exception as e:print('ERROR',futures[f],repr(e),flush=True)
(root/'download-results.json').write_text(json.dumps(results,indent=2))
assert len(results)==7,'Some plugins could not be downloaded'
