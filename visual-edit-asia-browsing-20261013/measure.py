import re,collections,json,subprocess
from pathlib import Path
root=Path(__file__).parent

def metrics(p):
 s=p.read_text();css=re.search(r'<style>(.*?)</style>',s,re.S).group(1);clean=re.sub(r'url\([^)]*\)','url(ASSET)',css);clean=re.sub(r'/\*.*?\*/','',clean,flags=re.S);rules=[]
 def scan(t,context='base'):
  pos=0
  while pos<len(t):
   i=t.find('{',pos)
   if i<0:break
   pre=t[pos:i].strip();j=i+1;depth=1
   while j<len(t) and depth:depth+=(t[j]=='{')-(t[j]=='}');j+=1
   content=t[i+1:j-1]
   if pre.startswith('@media'):scan(content,pre)
   elif not pre.startswith('@'):rules.append((pre,context))
   pos=j
 scan(clean);counts=collections.Counter(sel.strip() for pre,ctx in rules for sel in pre.split(','));scoped=collections.Counter((ctx,sel.strip()) for pre,ctx in rules for sel in pre.split(','))
 return {'file_bytes':p.stat().st_size,'stylesheet_bytes':len(css.encode()),'style_rules':len(rules),'duplicated_selectors_all_contexts':sum(v>1 for v in counts.values()),'duplicated_selectors_same_context':sum(v>1 for v in scoped.values()),'media_blocks':len(re.findall(r'@media',css)),'print_blocks':len(re.findall(r'@media\s+print',css))}
m={'before':metrics(root/'backup/index.html'),'after':metrics(root/'index.html')};assert m['after']['duplicated_selectors_same_context']==0
print(json.dumps(m,indent=2));(root/'implementation-metrics.json').write_text(json.dumps(m,indent=2))
r=subprocess.run(['git','diff','--no-index','--stat',str(root/'backup/index.html'),str(root/'index.html')],text=True,capture_output=True);print(r.stdout);(root/'diff-stat.txt').write_text(r.stdout)
