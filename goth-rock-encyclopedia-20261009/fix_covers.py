import json,urllib.request,concurrent.futures
from pathlib import Path
root=Path(__file__).parent;covers=json.loads((root/'covers.json').read_text())
urls={3:'https://www.thecure.com/wp-content/uploads/sites/10452/2018/01/71zBTfJxkiL._SL1500_-1014x1024.jpg',4:'https://www.thecure.com/wp-content/uploads/sites/10452/2018/01/faith.jpg',6:'https://uk-decay.co.uk/heritage/wp-content/uploads/2017/04/FMMO_prod.jpg',5:'https://s3.eu-west-1.amazonaws.com/cf-cdn.beggars.com/beggars_archive/wp-content/uploads/2015/11/17130509/BBQLP2061X-Bauhaus-4000.jpg',15:'https://s3.eu-west-1.amazonaws.com/cf-cdn.beggars.com/archivebeggars/wp-content/uploads/2025/10/27171622/1x1-CD-front.jpg',16:'https://s3.eu-west-1.amazonaws.com/cf-cdn.beggars.com/beggarsarchive/wp-content/uploads/2015/11/28160722/FieldsOfTheNephilim_Elizium_LP_brick_1.jpg',10:'https://s3.eu-west-1.amazonaws.com/cf-cdn.beggars.com/beggarsarchive/wp-content/uploads/2015/11/10192557/dreamtimeweb.jpg',11:'https://s3.eu-west-1.amazonaws.com/cf-cdn.beggars.com/beggarsarchive/wp-content/uploads/2023/02/27193601/TheCultLoveWebsite.jpg'}
records=json.loads((root/'records.json').read_text())
def work(item):
 i,u=item
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as f:b=f.read();assert f.headers.get('Content-Type','').startswith('image/')
  name=f'album-{i:02d}.jpg';(root/'Attachments'/name).write_bytes(b);return str(i),{'url':u,'file':name,'source':records[i]['source']}
 except Exception as e:return str(i),{'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for i,c in ex.map(work,urls.items()):covers[i]=c
(root/'covers.json').write_text(json.dumps(covers,indent=2));print({i:c.get('error','downloaded') for i,c in covers.items() if c})
