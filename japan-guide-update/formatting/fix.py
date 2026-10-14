from pathlib import Path
import json,re,shutil,collections
v=Path('/home/ivanaguilera/Documents/Obsidian Vault');backup=Path('/home/ivanaguilera/Work/japan-guide-update/formatting/backup');backup.mkdir(exist_ok=True)
convert={'Japan Travel Guide 2027.md':{'🔎 Official schedule check for 2027','☕ Ginza coffee and matcha cafés','📍 Matcha shopping stops'},'Japan 2027 — Travel Essentials.md':{'📲 Apps to prepare on your iPhone'}}
def fix_alias(m):return '[['+re.sub(r'(?<!\\)\|',r'\|',m.group(1))+']]'
def cells(line):return [x.strip() for x in re.split(r'(?<!\\)\|',line)[1:-1]]
def sources(s):return collections.Counter(re.findall(r'https?://[^\s<>\)]+',s))
changed=[];converted=0;normalized=0
for p in sorted(v.glob('Japan*.md')):
 before=p.read_text();ls=before.splitlines();out=[];i=0;heading='';level=2
 while i<len(ls):
  line=ls[i]
  match=re.match(r'^(#{1,6}) (.*)',line)
  if match:level=len(match[1]);heading=match[2]
  if line.startswith('|'):
   j=i
   while j<len(ls) and ls[j].startswith('|'):j+=1
   raw=ls[i:j];rows=[cells(re.sub(r'\[\[([^\]\n]+)\]\]',fix_alias,x)) for x in raw]
   assert len(rows)>=2 and all(len(x)==len(rows[0]) for x in rows),(p.name,i+1)
   assert all(re.fullmatch(r':?-+:?',x.replace(' ','')) for x in rows[1]),(p.name,i+1)
   if heading in convert.get(p.name,set()):
    headers=rows[0];replacement=[]
    for row in rows[2:]:
     label_index=1 if headers[0]=='Priority' else 0
     label=row[label_index].replace('**','').replace('\\|','|')
     replacement+=['#'*min(level+1,6)+' '+label,'']
     for index,(title,value) in enumerate(zip(headers,row)):
      if index==label_index:continue
      replacement += ['**'+title+':** '+value.replace('\\|','|'),'']
    rendered='\n'.join(replacement)
    for row in rows[2:]:
     for value in row:assert value.replace('**','').replace('\\|','|') in rendered.replace('**','')
    out+=replacement;converted+=1
   else:
    for n,row in enumerate(rows):
     if n==1:row=[':---:' if x.startswith(':') and x.endswith(':') else ':---' if x.startswith(':') else '---:' if x.endswith(':') else '---' for x in row]
     out.append('| '+' | '.join(row)+' |')
    normalized+=1
   i=j
  else:out.append(line);i+=1
 after='\n'.join(out)+'\n';assert sources(before)==sources(after),(p.name,'Source links changed')
 if before!=after:
  shutil.copy2(p,backup/p.name);p.write_text(after);changed.append(p.name)
# Open the guide in Reading view without changing other tabs.
p=v/'.obsidian/workspace.json';shutil.copy2(p,backup/'workspace.json');w=json.loads(p.read_text());views=0

def visit(x):
 global views
 if isinstance(x,dict):
  if x.get('type')=='markdown' and x.get('state',{}).get('file')=='Japan Travel Guide 2027.md':x['state']['mode']='preview';views+=1
  for child in x.values():visit(child)
 elif isinstance(x,list):
  for child in x:visit(child)
visit(w);p.write_text(json.dumps(w,indent=2)+'\n')
print(json.dumps({'changed_notes':changed,'converted_tables':converted,'compact_tables':normalized,'guide_reading_views':views,'links':'preserved','backup':str(backup)},indent=2))
