from pathlib import Path
import json
root=Path(__file__).parent
# Country identifies the source operator, posted editorial base or linked national edition.
rows='''
01|United States|https://www.are.na/privacy|Operator lists a New York postal address.
02|United States|https://www.cosmos.so/legal/privacy-policy|Official privacy contact is in New York.
03|Taiwan|https://www.linkedin.com/company/eagle-app|Publisher profile lists Taipei, Taiwan; Eagle identifies OGDESIGN as its developer.
04|United States|https://www.figma.com/legal/privacy|Figma Inc. lists San Francisco as its principal privacy contact.
05|Bulgaria|https://www.inoreader.com/privacy_policy|Innologica lists Sofia, Bulgaria.
06|Canada|https://github.com/linkwarden|The verified Linkwarden organization profile lists Canada.
07|Australia|https://milanote.com/legal/privacy-policy|Milanote Pty Ltd lists Melbourne, Australia.
08|Sweden|https://www.pureref.com/privacy_policy.php|Idyllic Pixel AB states it is established in Sweden.
09|Kazakhstan|https://raindrop.io/r/app/android|The publisher-linked app listing gives an Astana, Kazakhstan developer address.
10|International project|https://shaarli.readthedocs.io/en/master/|Community-maintained software; no single publisher country established from official documentation.
11|Canada|https://tineye.com/careers|TinEye lists its in-office team in Toronto, Canada.
12|United States|https://archive.org/about/terms.php|Internet Archive gives its San Francisco address; direct extraction failed, indexed official contact text corroborated.
13|United Kingdom|https://www.dazedmedia.com/privacy-policy|Dazed publisher Waddell Limited lists London, England.
14|China|https://m.dewu.com/hybird/h5other/privacy-policy-21-11-18|Dewu privacy contact lists Shanghai, China.
15|Japan|https://www.fashionsnap.com/about/terms-of-use|Japanese publication operated by Reco Orlando; Japan is the source edition and operating-country classification.
16|United States|https://www.linkedin.com/company/jing-daily|Jing Daily identifies a New York base; its editorial coverage remains China.
17|South Korea|https://help-global.musinsa.com/hc/en-us/articles/9193213797401-Act-on-Specified-Commercial-Transactions|MUSINSA Co. Ltd lists Seoul, Republic of Korea.
18|United Kingdom|https://uk.linkedin.com/company/nowness-com|Official company profile lists London; this identifies the posted operating base, not parent-company nationality.
19|Italy|https://www.nssmag.com/en/p/nss-factory|Publisher identifies Milan and Italian registration for the magazine.
20|United Kingdom|https://www.showstudio.com/contact|SHOWstudio lists Belgravia, London.
21|France|https://www.tag-walk.com/en/legal|Tagwalk head office and registration are in Paris.
22|Japan|https://tokyofashion.com/about/|Tokyo-based Japanese street-fashion publication; linked edition and source identity are Japan.
23|France|https://faq.vestiairecollective.com/hc/en-us/articles/8977357519121-Legal-Information|Publisher is a French company registered in Paris.
24|China|https://www.vogue.com.cn/|Country of the linked Vogue China national edition; not the multinational parent.
25|South Korea|https://www.vogue.co.kr/|Country of the linked Vogue Korea edition, operated by Doosan Magazine.
26|United States|https://www.vogue.com/business-corporate-masthead|American Vogue lists publication and editorial correspondence in New York.
27|China|https://www.xiaohongshu.com/|Chinese platform and national operator; country does not limit the geographic range of creator posts.
28|Germany|https://www.032c.com/pages/contact-legal|032c System GmbH identifies Berlin, Germany.
29|United Kingdom|https://www.anothermag.com/contact|AnOther Publishing Ltd lists London and UK publication.
30|United Kingdom|https://shop.i-d.co/pages/contact|Official contact identifies London, UK; country describes the linked publication, not shareholder nationality.
31|United States|https://www.printedmatter.org/|Printed Matter is the New York institution; official event FAQ corroborates its Chelsea NYC store.
32|Japan|https://sabukaru.online/about|Official about page explicitly says the magazine is based in Tokyo and its content is global.
33|France|https://system-magazine.com/|Current System masthead lists Paris, France; older London legal pages are not used as the current editorial base.
34|United Kingdom|https://thegentlewoman.co.uk/contact|Published by Fantastic Woman Ltd in London, United Kingdom.
35|France|https://www.businessoffashion.com/people/anja-aronowsky-cronberg|Editorial biography identifies Vestoj as Paris-based; founder nationality and UK academic patronage are not used as country. Secondary industry biography, corroborated by School of Visual Arts event biography.
36|United Kingdom|https://www.businessoffashion.com/legal|The Business of Fashion Limited lists a London registered office; coverage is international.
37|France|https://cn.fashionjobs.com/texte/4.html|FashionNetwork publisher legal notice gives Paris registration and address.
38|France|https://heuritech.com/careers/|Official careers page gives a Paris, France team and address.
39|China|https://luxe.co/about|Chinese business publication; the editorial market is China while it reports on international brands.
40|Spain|https://www.apartamentomagazine.com/terms-conditions/|Apartamento Publishing SL is explicitly identified as Spanish, registered in Barcelona.
41|United States|https://www.linkedin.com/company/behance-inc-|Platform company profile lists New York; this is the platform base, not its international creators' countries.
42|United States|https://www.linkedin.com/company/designspiration|Publisher company profile lists Los Angeles, United States.
43|United Kingdom|https://www.itsnicethat.com/contact|Official contact lists London.
44|South Korea|https://en.magazine-b.com/article/contact/6/441|B Media Company lists Seoul, Republic of Korea.
45|Netherlands|https://www.europeana.eu/en/contact-us|Europeana Foundation is based in The Hague, Netherlands; collections cover Europe.
46|United States|https://firstview.com/legal.php|Official legal contact gives New York, USA.
47|United States|https://www.fitnyc.edu/about/index.php|FIT is a New York institution and part of the State University of New York.
48|Japan|https://www.kci.or.jp/en/archives/|The Kyoto Costume Institute lists Kyoto, Japan.
49|United Kingdom|https://www.vam.ac.uk/info/contact-us|Victoria and Albert Museum contact is in London.
50|United States|https://vintagefashionguild.org/about/|The organization states US incorporation; membership and coverage are international.
51|United Kingdom|https://depophelp.zendesk.com/hc/en-gb/articles/360001773148-Terms-of-Service|Depop Limited is registered in England and Wales; its user marketplace is global.
52|International community|https://www.reddit.com/r/femalefashionadvice/|The source is a cross-border user community; Reddit's corporate country is not assigned to its members. Direct subreddit extraction was blocked.
'''.strip()
byid={}
for line in rows.splitlines():
 num,country,url,note=line.split('|',3);byid[num]={'country':country,'country_source':url,'country_note':note,'country_checked':'2026-10-13'}
inventory=json.loads((root/'inventory.json').read_text());assert len(byid)==len(inventory)==52
for row in inventory:row.update(byid[row['id']])
(root/'countries.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
from collections import Counter
print(Counter(row['country'] for row in inventory))
