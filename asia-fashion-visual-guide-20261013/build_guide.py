from pathlib import Path
from html import escape
import base64
import json
import re
import zipfile

ROOT = Path(__file__).parent
DATE = '2026-10-13'
COUNTRIES = [
    dict(id='china', title='China', subtitle='Heritage details · utility · playful color · dark streetwear', looks=[
        ('Xin Zhongshi', 'A stand-collar blouse with a mamianqun: look for the broad flat front panel and pleated sides. Jade and ivory keep this example quiet and wearable.', 'Contemporary heritage fusion; the generated skirt is an interpretation of mamianqun construction.'),
        ('Safaricore', 'An olive hiking jacket, cargo skirt, bucket hat, and practical sneakers. Pockets and outdoor fabrics are the main visual cues.', 'Urban utility styling, rather than an expedition outfit.'),
        ('Kidcore', 'A bright color-block knit, relaxed denim, playful hair clips, and a bag charm. The recognizable ingredient is joyful color.', 'Shown on an adult; the name describes the aesthetic.'),
        ('Opiumcore', 'Black leather, loose dark trousers, silver hardware, and chunky boots. Compare the darker mood with the other three looks.', 'One gothic streetwear interpretation; the report’s popularity figures remain unverified.')
    ], sources=[
        ('Jing Daily — China’s 2025 core aesthetics', 'https://jingdaily.com/posts/china-s-gen-z-core-trends-of-2025', 'Photo-led overview with safaricore, kidcore, and other named cores. Much of the article is behind a subscription prompt.'),
        ('People’s Daily Online via China Kongzi — Hanfu and New Chinese Style', 'https://www.chinakongzi.org/English/CulturalHighlights/202402/t20240228_571430.htm', '2024 background reference with a credited photograph of hanfu at a cultural event; distinguish that occasion from everyday fusion.')
    ]),
    dict(id='korea', title='South Korea', subtitle='Relaxed tailoring · neutral layering · casual hanbok fusion · sport mix', looks=[
        ('K-Minimal', 'An oversized trench, simple knit, and wide tailored trousers. Calm neutrals and a clean silhouette do most of the work.', 'An editorial category used in the supplied report, not a universal description of Korean fashion.'),
        ('Acubi', 'A cropped bolero, asymmetric layered top, washed-gray wide jeans, and a compact nylon bag. Focus on the layers and proportions.', 'A neutral Y2K-inspired interpretation; the supplied report’s timing claims were not independently audited.'),
        ('Hanbok fusion', 'A mint jeogori-inspired jacket with front ties, straight denim, sneakers, and a small tassel ornament. One heritage piece anchors a practical outfit.', 'Casual fusion, separate from ceremonial hanbok. Compare structure with designer photography before publication.'),
        ('Jersey chic', 'An oversized football jersey with a pleated skirt and technical sneakers. The sports top becomes everyday fashion through styling.', 'Sport mixing appears across markets; this Seoul setting does not make it uniquely Korean.')
    ], sources=[
        ('nss magazine — Seoul Fashion Week FW26 street style', 'https://www.nssmag.com/de/fashion/44219/die-besten-streetstyle-looks-von-der-seoul-fashion-week-fw-2026', 'Published 9 February 2026; photography credited to Jimin Jeon. The image gallery may require JavaScript.'),
        ('The Korea Times — Studio Hyeon designer interview', 'https://www.koreatimes.co.kr/lifestyle/20250313/designer-kwon-hye-jin-of-studio-hyeon-shares-vision-for-tomorrows-hanbok', 'Published 13 March 2025; includes credited exhibition and designer images. Some looks are artistic or formal, rather than casual denim fusion.')
    ]),
    dict(id='japan', title='Japan', subtitle='Menswear proportions · romantic grunge · ballet textures · seasonal dress', looks=[
        ("MEN’SLIKE", 'A roomy blazer and shirt, a tie, barrel-leg jeans, loafers, and a plush bag charm. Compare the structured top with the curved denim volume.', 'An androgynous styling option within a much broader Japanese fashion landscape.'),
        ('Fairy grunge', 'Lace and a soft dress under darker outerwear, finished with chunky boots. The contrast between romantic texture and heavy footwear explains the look.', 'An illustrative Harajuku hybrid; the linked Tokyo article does not establish this specific micro-style.'),
        ('Balletcore', 'A pink cardigan, tulle midi skirt, leg warmers, and ballet flats, paired with a sporty bag. The dance-inspired details are adapted for streetwear.', 'An illustrative styling idea from the report; not a claim that every pictured item is currently trending.'),
        ('Summer yukata', 'An indigo cotton robe, obi, geta, and a small drawstring bag. Lanterns place the look in a summer festival context.', 'Seasonal traditional dress. Check wrap direction and garment construction before using a generated image as a reference.')
    ], sources=[
        ('Who What Wear — Tokyo spring 2025 photo references', 'https://www.whowhatwear.com/fashion/spring/tokyo-fashion-trends-spring-2025', 'Real images of ties, plush bag charms, knee-high socks, pleated culottes, and technical sneakers. Several photographs are credited to Getty Images. It does not substantiate every Japanese micro-style listed in the report.')
    ])
]

def data_image(path):
    mime = 'image/svg+xml' if path.suffix == '.svg' else 'image/png'
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()

def build():
    lookbooks = {c['id']: ROOT/'images'/f"{c['id']}-lookbook.png" for c in COUNTRIES}
    pending = [cid for cid, path in lookbooks.items() if not path.exists()]
    sections = []
    md = ['# China, Japan & South Korea — Visual Fashion Companion', '',
          f'Created {DATE} from your Fashion Trends 2025–2026 research report.', '',
          'These outfit examples explain the report’s styling vocabulary. Where a lookbook image is shown, it is an AI-generated editorial interpretation — not a real street photograph, designer product, or evidence of trend prevalence. Real photographic references are linked separately. This is a focused starting set, not an exhaustive account of any country’s fashion.', '']
    if pending:
        md += [f'**Status: outfit image references pending.** Lookbook sheets for {", ".join(pending)} were not generated. Exact prompts are preserved in `image-generation-prompts.json`; place regenerated sheets at `images/<country>-lookbook.png` and rerun this build to embed them.', '']
    md += ['[Open the standalone visual document](fashion-visual-companion.html) · [Read the original research](asia-fashion-trends-2025-2026-research-v2.md)', '']
    for c in COUNTRIES:
        image_path = lookbooks[c['id']]
        bounds = {
            'china': [(14, 75, 364, 841), (394, 75, 368, 841), (778, 75, 365, 841), (1157, 75, 365, 841)],
            'korea': [(1, 76, 376, 830), (397, 76, 362, 830), (778, 76, 362, 830), (1161, 76, 374, 830)],
            'japan': [(25, 97, 363, 814), (402, 97, 359, 814), (776, 97, 360, 814), (1153, 97, 361, 814)],
        }[c['id']]
        card_parts = []
        for i, (name, desc, context) in enumerate(c['looks'], 1):
            photo = ''
            if image_path.exists():
                x, y, width, height = bounds[i-1]
                photo = f'<div class="outfit-image" style="aspect-ratio:{width}/{height}"><img src="{data_image(image_path)}" style="width:{1536/width*100:.6f}%;left:{-x/width*100:.6f}%;top:{-y/height*100:.6f}%" alt="AI-generated {escape(name)} outfit example"></div>'
            card_parts.append(f'<article>{photo}<span class="number">{i:02}</span><h3>{escape(name)}</h3><p>{escape(desc)}</p><p class="context">{escape(context)}</p></article>')
        cards = ''.join(card_parts)
        refs = ''.join(f'<li><a href="{escape(url, quote=True)}" target="_blank" rel="noopener">{escape(title)} ↗</a><p>{escape(note)}</p></li>' for title,url,note in c['sources'])
        if image_path.exists():
            figure_html = '<p class="context">AI-GENERATED OUTFIT EXAMPLES · Each look appears with its caption below.</p>'
        else:
            labels = ' · '.join(escape(name) for name,_,_ in c['looks'])
            figure_html = f'<figure class="pending"><h3>Outfit image references pending</h3><p>{labels}</p><figcaption>IMAGE REFERENCES NOT YET GENERATED · Exact prompts preserved in image-generation-prompts.json; regenerate and rerun this build to embed them.</figcaption></figure>'
        sections.append(f'<section id="{c["id"]}"><div class="section-title"><span>VISUAL CHAPTER</span><h2>{c["title"]}</h2><p>{escape(c["subtitle"])}</p></div>{figure_html}<div class="looks">{cards}</div><details open><summary>Real photography & source context</summary><ul class="sources">{refs}</ul><p class="context">Source pages checked {DATE}. Photography remains with its credited owners; these links do not supply magazine publication rights.</p></details></section>')
        md += [f'## {c["title"]}', '', c['subtitle'], '']
        if image_path.exists():
            md += [f'![Four AI-generated {c["title"]} outfit examples](images/{c["id"]}-lookbook.png)', '', '**AI-generated examples. Read left to right.**', '']
        else:
            md += [f'> **Outfit image references pending.** The four looks are described below; exact generation prompts are preserved in `image-generation-prompts.json`.', '']
        for name,desc,context in c['looks']:
            md += [f'### {name}', '', desc, '', f'*Context: {context}*', '']
        md += ['### Real photo references', '']
        for title,url,note in c['sources']:
            md += [f'- [{title}]({url}) — {note}']
        md += ['', f'Source pages checked {DATE}. Linked photos retain their original ownership; publication rights are not supplied.', '']
    figures = [('fig1-palette-board.svg','Palettes','Use these colors to compare the outfit examples.'),('fig2-cultural-respect-spectrum.svg','Cultural context','The supplied figure expresses editorial judgments. Pair garment names with the correct occasion.'),('fig3-price-tiers.svg','Price tiers','Original indicative ranges, not newly checked shopping prices. China uses CNY; Japan uses JPY; South Korea uses KRW.'),('fig4-platform-journey.svg','Platform journey','Original report’s platform map, retained as background research; platform claims were not re-audited.')]
    figure_html = ''.join(f'<figure class="diagram"><h3>{title}</h3><img src="{data_image(ROOT/"images"/filename)}" alt="{title} diagram from the supplied report"><figcaption>{escape(note)}</figcaption></figure>' for filename,title,note in figures)
    md += ['## Original research figures', '']
    for filename,title,note in figures:
        md += [f'### {title}', '', f'![{title}](images/{filename})', '', note, '']
    embedded = 'all three lookbooks and all four SVGs' if not pending else f'the four SVG diagrams; the {len(pending)} lookbook image sheets are pending generation and appear as labeled placeholders'
    prompt_note = 'images were produced using the built-in image generation tool' if not pending else 'the earlier image generation attempt failed, so the prompts remain ready for a future run'
    md += ['## Review scope', '', 'Twelve looks make the main silhouettes easier to recognize. The report also discusses goblincore, dirtycore, sweet lolita, Mori girl, modern gyaru, and cross-market styling; those do not yet have dedicated images here. Existing verification flags in the original research still apply.', '', f'The offline HTML embeds {embedded}. External photo references require internet access. Exact generation prompts are in [image-generation-prompts.json](image-generation-prompts.json); {prompt_note}.', '']
    css = '''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f5f2ea;color:#242820;font:16px/1.65 Georgia,serif}main{max-width:1440px;margin:auto;padding:48px 5vw}a{color:inherit;text-underline-offset:4px}header{border-top:5px solid #242820;padding:28px 0 38px}.eyebrow,.section-title>span,nav,.number,figcaption,summary,footer{font-family:Arial,sans-serif}.eyebrow,.section-title>span{font-size:12px;letter-spacing:.17em}h1{font-size:clamp(44px,7vw,92px);line-height:1.03;letter-spacing:-.04em;margin:22px 0}header p{max-width:800px}.deck{font-size:23px}.note{padding:16px 20px;background:#e7e6da;border-left:3px solid #63745c;font-size:15px}nav{display:flex;gap:24px;flex-wrap:wrap;font-size:13px;margin-top:24px}section{padding:55px 0;border-top:1px solid #b8bdad}h2{font-size:52px;line-height:1.1;margin:12px 0}h3{font-size:23px;line-height:1.25;margin:12px 0}.section-title>p{color:#5e6657}figure{margin:25px 0}.pending{border:2px dashed #b8bdad;background:#efece2;padding:24px}img{display:block;width:100%;height:auto}figcaption{font-size:11px;color:#5e6657;margin-top:12px;letter-spacing:.05em}.looks{display:grid;grid-template-columns:repeat(4,1fr);gap:26px}.number{font-size:12px;color:#5e6657}.context{font-size:13px;color:#606856}.looks p{font-size:15px}.outfit-image{position:relative;width:100%;overflow:hidden;margin-bottom:18px}.outfit-image img{position:absolute;max-width:none;height:auto}.looks article{border-top:2px solid #657b5c;padding-top:15px}details{margin-top:30px;border:1px solid #bec5b4;padding:20px}summary{font-size:13px;cursor:pointer}.sources{padding-left:20px}.sources li{margin:18px 0}.sources p{margin:4px 0;font-size:14px}.diagrams{display:grid;grid-template-columns:1fr 1fr;gap:32px}.diagram{background:white;padding:24px}.diagram figcaption{letter-spacing:0;font-size:12px}footer{border-top:1px solid #b8bdad;padding:24px 0;font-size:12px}@media(max-width:850px){.looks,.diagrams{grid-template-columns:1fr 1fr}main{padding:28px 5vw}h2{font-size:40px}}@media(max-width:500px){.looks,.diagrams{grid-template-columns:1fr}}@media print{body{background:white}main{padding:0}nav{display:none}section{break-before:page}.looks{grid-template-columns:repeat(4,1fr);gap:12px}.looks p{font-size:11px}details{font-size:11px}.diagrams{display:block}h1{font-size:56px}}'''
    html = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>China, Japan & South Korea — Visual Fashion Companion</title><style>{css}</style><main><header><div class="eyebrow">FASHION RESEARCH / VISUAL COMPANION / 13 OCTOBER 2026</div><h1>Three markets.<br>Twelve looks.</h1><p class="deck">A visual starting point for your women’s fashion magazine: China, Japan, and South Korea.</p><p>Use the pictures to recognize silhouettes, fabrics, accessories, and styling. Read each country’s four examples from left to right, then compare them with real photographic references.</p><p class="note">Outfit examples are AI-generated editorial interpretations based on your 2025–2026 report where the lookbook images are available; they do not document real people, designer products, or measured trend popularity. Each country includes original photo-source links for further review.{'' if not pending else ' Lookbook images are pending generation and appear as labeled placeholders.'}</p><nav><a href="#china">China</a><a href="#japan">Japan</a><a href="#korea">South Korea</a><a href="#figures">Research figures</a><a href="asia-fashion-trends-2025-2026-research-v2.md">Full research ↗</a></nav></header>{''.join(sections)}<section id="figures"><div class="section-title"><span>YOUR ORIGINAL FIGURES</span><h2>Color, context & commerce.</h2><p>The four supplied SVGs, preserved beside the outfit examples.</p></div><div class="diagrams">{figure_html}</div></section><footer>Created {DATE} from the supplied research v2. Focused visual selection, not exhaustive national fashion coverage. Other report aesthetics still need their own images. Original report verification flags remain unresolved. This document’s pictures and diagrams work offline; source links require internet access.</footer></main></html>'''
    (ROOT/'fashion-visual-companion.html').write_text(html)
    (ROOT/'Fashion Visual Companion.md').write_text('\n'.join(md))
    with zipfile.ZipFile(ROOT/'fashion-visual-companion.zip','w',zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(ROOT.iterdir()):
            if path.is_file() and path.suffix in ('.html','.md','.json'):
                bundle.write(path,path.name)
        for path in sorted((ROOT/'images').iterdir()):
            bundle.write(path,str(path.relative_to(ROOT)))
    for filename in ('fashion-visual-companion.html','Fashion Visual Companion.md'):
        content=(ROOT/filename).read_text()
        assert all(c['title'] in content for c in COUNTRIES)
    assert len(re.findall('<img ',html)) == 4 + 4 * sum(1 for p in lookbooks.values() if p.exists())
    for target in re.findall(r'\]\((images/[^)]+)\)', '\n'.join(md)):
        assert (ROOT/target).is_file(), target
    print('Saved and checked HTML, illustrated Markdown, and portable ZIP.')

if __name__ == '__main__':
    build()
