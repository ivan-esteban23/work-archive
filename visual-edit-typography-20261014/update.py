from pathlib import Path
import re
p=Path('visual-edit-public/dist/index.html');s=p.read_text()
changes={
"--text-body:16px;--text-small:14px;--text-label:12px;":"--text-body:clamp(1rem,.96rem + .2vw,1.125rem);--text-small:.9375rem;--text-label:.8125rem;--type-cover:clamp(3rem,2rem + 4vw,5.5rem);--type-section:clamp(2rem,1.5rem + 2vw,3rem);--type-title:clamp(1.25rem,1.15rem + .4vw,1.5rem);",
"font-size:clamp(64px,7.3vw,106px);line-height:.98;letter-spacing:-.03em":"font-size:var(--type-cover);line-height:1.04;letter-spacing:-.02em",
"font-size:clamp(32px,3.4vw,46px);line-height:1.12":"font-size:var(--type-section);line-height:1.16;letter-spacing:-.012em",
"h3{font-size:22px;line-height:1.25;font-weight:550":"h3{font-family:var(--sans);font-size:var(--type-title);line-height:1.3;font-weight:550",
"font:26px/1.1 var(--serif);letter-spacing:.06em":"font:clamp(1.625rem,1.4rem + 1vw,2.25rem)/1.15 var(--serif);letter-spacing:.01em",
".hero h1{max-width:none;font-size:60px}":".hero h1{max-width:14ch;font-size:var(--type-cover);text-wrap:balance}",
"font:23px/1.3 var(--serif)":"font:clamp(1.375rem,1.2rem + .8vw,1.75rem)/1.4 var(--serif)",
".hero .editorial-intro{font-size:12px!important;line-height:1.65}":".hero .editorial-intro{font-size:var(--text-small);line-height:1.75}",
"font-size:14px}":"font-size:var(--text-small)}",
"font-size:16px;padding:12px":"font-size:var(--text-body);padding:12px",
"font-size:13px}":"font-size:var(--text-small)}",
"#active-filters{font-size:12px":"#active-filters{font-size:var(--text-small)",
"font-size:16px}":"font-size:var(--text-body)}",
".count{font-size:12px":".count{font-size:var(--text-small)",
".asia-note{font-size:12px":".asia-note{font-size:var(--text-small)",
".card-meta{letter-spacing:.06em;text-transform:uppercase;":".card-meta{letter-spacing:0;",
".metadata-label{font-size:var(--text-label);color:var(--muted);letter-spacing:.07em}":".metadata-label{font-size:var(--text-label);color:var(--muted);letter-spacing:0}",
".source h3{margin:0 0 14px;font-size:24px;line-height:1.2}":".source h3{font-family:var(--sans);font-weight:550;margin:0 0 14px;font-size:var(--type-title);line-height:1.3;letter-spacing:0}",
".source-purpose{font-size:var(--text-body);line-height:1.7;":".source-purpose{font-size:var(--text-body);line-height:1.75;max-width:58ch;",
".comparison dt{font-size:var(--text-label);letter-spacing:.07em;text-transform:uppercase;":".comparison dt{font-size:var(--text-label);letter-spacing:0;",
".access strong{font-size:var(--text-label);letter-spacing:.07em;text-transform:uppercase}":".access strong{font-size:var(--text-small);font-weight:600;letter-spacing:0}",
".shortlist span{font-size:12px":".shortlist span{font-size:var(--text-small)",
".research-route summary strong{font-size:22px;line-height:1.25":".research-route summary strong{font-size:var(--type-title);line-height:1.3",
".route-result strong{font-size:var(--text-label);letter-spacing:.07em;text-transform:uppercase;":".route-result strong{font-size:var(--text-small);font-weight:600;letter-spacing:0;",
"#notes .editorial-intro{max-width:68ch;color:var(--muted);font-size:var(--text-small);":"#notes .editorial-intro{max-width:68ch;color:var(--muted);font-size:var(--text-body);",
".sections-heading h2{font-size:32px":".sections-heading h2{font-size:2rem",
".hero h1{max-width:none;font-size:clamp(64px,7.3vw,106px)}":".hero h1{max-width:14ch;font-size:var(--type-cover)}",
".cover-line{font-size:28px}.cover-copy>.eyebrow{font-size:11px}":".cover-line{font-size:1.75rem}.cover-copy>.eyebrow{font-size:var(--text-label)}",
}
# Only edit screen rules; retain compact print styling.
screen,printcss=s.split('@page',1)
for old,new in changes.items():
 if old not in screen: print('No match:',old)
 screen=screen.replace(old,new)
start=screen.index('html:lang(zh-Hans) h1');end=screen.index('@media(min-width:640px)',start)
cjk=''
for lang,serif,sans in [
 ('zh-Hans',"'Noto Serif CJK SC','Songti SC','SimSun',serif","'Noto Sans CJK SC','PingFang SC','Microsoft YaHei',sans-serif"),
 ('zh-Hant',"'Noto Serif CJK TC','Songti TC','PMingLiU',serif","'Noto Sans CJK TC','PingFang TC','Microsoft JhengHei',sans-serif"),
 ('ja',"'Noto Serif CJK JP','Noto Serif JP','Yu Mincho','Hiragino Mincho ProN',serif","'Noto Sans CJK JP','Noto Sans JP','Yu Gothic','Hiragino Kaku Gothic ProN',sans-serif"),
 ('ko',"'Noto Serif CJK KR','Noto Serif KR','Batang',serif","'Noto Sans CJK KR','Noto Sans KR','Malgun Gothic','Apple SD Gothic Neo',sans-serif")]:
 cjk+=f"html:lang({lang}){{--serif:{serif};--sans:'Source Sans 3',{sans}}}\n"
 cjk+=f"html:lang({lang}) :where(h1,h2,.cover-line){{letter-spacing:0;line-height:1.4;word-break:normal;overflow-wrap:break-word}}\n"
 cjk+=f"html:lang({lang}) .hero h1{{font-size:clamp(3rem,2rem + 3vw,4.5rem);max-width:14em;line-height:1.25}}\n"
 cjk+=f"html:lang({lang}) :where(.eyebrow,.section-top>span,.category,.cover-kicker,.route-outline,.route-source-label,.footer-meta){{letter-spacing:0;text-transform:none}}\n"
 if lang=='ko':cjk+="html:lang(ko) :where(p,h2,h3,.research-route summary strong){word-break:keep-all;overflow-wrap:break-word}\n"
screen=screen[:start]+cjk+screen[end:]
s=screen+'@page'+printcss;p.write_text(s)
sw=Path('visual-edit-public/dist/sw.js');sw.write_text(re.sub(r"const CACHE='[^']+'","const CACHE='visual-edit-shell-typography-20261014-v1'",sw.read_text()))
print('Typography updated; existing embedded font assets retained.')
