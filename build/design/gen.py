# Génère les artboards du canevas de design Somnila (maquettes du thème Shrine).
import json, html
NIGHT='#1E2A3A'; CLOUD='#F7F9FC'; MIST='#DCE8F2'; DAWN='#F0B79B'; SLATE='#6B7D90'
FONTS='https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,300..600,100&family=Manrope:wght@400;500;600&display=swap'
BASE_CSS = f"""
    body {{ margin: 0; background: {CLOUD}; color: {NIGHT}; font-family: 'Manrope', system-ui, -apple-system, 'Segoe UI', sans-serif; font-size: 16px; line-height: 1.6; -webkit-font-smoothing: antialiased; }}
    a {{ color: {NIGHT}; text-decoration: none; }} a:hover {{ color: {SLATE}; }}
    h1, h2, h3 {{ font-family: 'Fraunces', Georgia, 'Times New Roman', serif; font-weight: 400; letter-spacing: -0.015em; margin: 0; line-height: 1.1; text-wrap: balance; }}
    .serif {{ font-family: 'Fraunces', Georgia, serif; font-weight: 400; }}
    .label {{ font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; font-weight: 500; color: {SLATE}; }}
    .btn {{ display: inline-flex; align-items: center; justify-content: center; height: 48px; padding: 0 26px; border-radius: 999px; background: {NIGHT}; color: {CLOUD}; font-weight: 500; font-size: 15px; }}
    .btn.outline {{ background: transparent; color: {NIGHT}; border: 1px solid {NIGHT}; }}
    .tile {{ background: {MIST}; border-radius: 20px; padding: 18px 20px; }}
    .card {{ background: {CLOUD}; border-radius: 28px; overflow: hidden; box-shadow: 0 20px 46px -20px rgba(30,42,58,0.30); }}
    .horizon {{ display: block; width: 56px; height: 2px; border-radius: 2px; background: linear-gradient(90deg, {DAWN}, rgba(240,183,155,0)); }}
    .price {{ font-variant-numeric: tabular-nums; }}
    .sky {{ background: linear-gradient(180deg, {CLOUD} 0%, {MIST} 100%); }}
    .ico {{ width: 20px; height: 20px; stroke: {NIGHT}; fill: none; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; flex: 0 0 auto; }}
"""
def ico(name, size=20, color=NIGHT):
    P={'truck':'<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"></path><circle cx="6.5" cy="17.5" r="1.5"></circle><circle cx="17.5" cy="17.5" r="1.5"></circle>',
       'clock':'<circle cx="12" cy="12" r="8.5"></circle><path d="M12 7.5V12l3 2"></path>',
       'moon':'<path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5z"></path>',
       'wash':'<rect x="4" y="3" width="16" height="18" rx="3"></rect><circle cx="12" cy="13" r="4.5"></circle><path d="M8 6.5h.01M11 6.5h.01"></path>',
       'check':'<circle cx="12" cy="12" r="8.5"></circle><path d="M8.5 12.2l2.3 2.3 4.7-4.8"></path>',
       'bag':'<path d="M5 8h14l-1 12H6z"></path><path d="M9 8V6a3 3 0 0 1 6 0v2"></path>',
       'search':'<circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l4 4"></path>',
       'menu':'<path d="M4 7h16M4 12h16M4 17h16"></path>',
       'plus':'<path d="M12 6v12M6 12h12"></path>',
       'arrow':'<path d="M5 12h14M13 6l6 6-6 6"></path>',
       'box':'<path d="M4 8l8-4 8 4-8 4z"></path><path d="M4 8v8l8 4 8-4V8M12 12v8"></path>',
       'undo':'<path d="M9 14l-4-4 4-4"></path><path d="M5 10h9a5 5 0 0 1 0 10h-3"></path>',
       'globe':'<circle cx="12" cy="12" r="8.5"></circle><path d="M3.5 12h17M12 3.5c3 3 3 14 0 17M12 3.5c-3 3-3 14 0 17"></path>',
       'chev':'<path d="M6 9l6 6 6-6"></path>'}
    return f'<svg class="ico" viewBox="0 0 24 24" style="width: {size}px; height: {size}px; stroke: {color};">{P[name]}</svg>'

def head(title, extra_css=''):
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="{FONTS}">
  <style>{BASE_CSS}{extra_css}</style>
</helmet>
"""
FOOT = "</x-dc>\n</body>\n</html>\n"

def announcement(items, width, one=False):
    if one: items=items[1:2]
    cells=''.join(f'<div style="display: flex; align-items: center; gap: 8px;">{ico(i,14,NIGHT)}<span class="label" style="color: {NIGHT};">{t}</span></div>' for i,t in items)
    return f'<div style="background: {MIST}; height: 36px; display: flex; align-items: center; justify-content: center; gap: 48px; padding: 0 24px;">{cells}</div>'
ANN=[('truck','<b>Free shipping</b> on every pillow'),('clock','Ships in <b>6–10 days</b>, tracked'),('moon','<b>30-night trial</b> on every pillow')]

def header_desktop():
    nav=''.join(f'<a href="#" style="font-size: 15px; font-weight: 500;">{t}</a>' for t in ('Shop','Neck 01','Our story','Help'))
    return f"""<div style="height: 76px; display: flex; align-items: center; justify-content: space-between; padding: 0 56px; background: {CLOUD}; border-bottom: 1px solid rgba(30,42,58,0.08);">
  <div style="display: flex; align-items: center; gap: 40px;"><img src="logo.svg" alt="Somnila" style="width: 150px; height: 34px; display: block;"><nav style="display: flex; gap: 28px;">{nav}</nav></div>
  <div style="display: flex; align-items: center; gap: 20px;">{ico('search',22)}{ico('bag',22)}</div>
</div>"""
def header_mobile():
    return f"""<div style="height: 60px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; background: {CLOUD}; border-bottom: 1px solid rgba(30,42,58,0.08);">{ico('menu',22)}<img src="logo.svg" alt="Somnila" style="width: 118px; height: 27px; display: block;">{ico('bag',22)}</div>"""

def hero_desktop():
    return f"""<div style="position: relative; height: 680px; background: url(./hero.jpg) center / cover no-repeat;">
  <div style="position: absolute; left: 56px; top: 0; bottom: 0; display: flex; flex-direction: column; justify-content: center; gap: 22px; width: 560px;">
    <h1 style="font-size: 96px; font-variation-settings: 'opsz' 120, 'SOFT' 100; line-height: 1;">Sleep well.</h1>
    <span class="horizon"></span>
    <p style="margin: 0; font-size: 20px; line-height: 1.5; max-width: 480px;">Neck 01 is a memory-foam pillow with two heights, shaped around the way you actually lie. Ships in 6–10 days. Thirty nights to decide.</p>
    <div style="display: flex; gap: 12px;"><a class="btn" href="#">Shop Neck 01</a><a class="btn outline" href="#">All pillows</a></div>
  </div>
</div>"""
def hero_mobile():
    return f"""<div style="position: relative; height: 560px; background: url(./hero-m.jpg) center / cover no-repeat;">
  <div style="position: absolute; left: 20px; right: 20px; bottom: 28px; display: flex; flex-direction: column; gap: 14px;">
    <h1 style="font-size: 56px; font-variation-settings: 'opsz' 120, 'SOFT' 100; line-height: 1;">Sleep well.</h1>
    <span class="horizon"></span>
    <p style="margin: 0; font-size: 16px; line-height: 1.5;">A memory-foam pillow with two heights, shaped around the way you actually lie. Ships in 6–10 days. Thirty nights to decide.</p>
    <div style="display: flex; flex-direction: column; gap: 10px;"><a class="btn" href="#">Shop Neck 01</a><a class="btn outline" href="#">All pillows</a></div>
  </div>
</div>"""
TRUST=[('truck','Free shipping','On every pillow and every set, to the US, Canada, the UK, Europe and Australia.'),('clock','6–10 days, tracked','Tracking number by email the day it ships.'),('moon','30-night trial','Sleep on it. If it isn\'t right, one email and we refund it.'),('wash','Cover included','Removable and machine washable, on every pillow.')]
def trust(cols=4, pad='32px 56px'):
    tiles=''.join(f'<div class="tile" style="display: flex; gap: 12px; align-items: flex-start;">{ico(i,22)}<div><div style="font-weight: 600; font-size: 15px;">{t}</div><div style="font-size: 13.5px; color: {SLATE}; line-height: 1.45; margin-top: 2px;">{x}</div></div></div>' for i,t,x in TRUST)
    return f'<div style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); gap: 12px; padding: {pad};">{tiles}</div>'
def swatches(sel='Cloud'):
    cols=[('Night',NIGHT),('Cloud','#F7F9FC'),('Stone','#C4C2BD'),('Sky','#A9C8E8')]
    dots=''.join(f'<span title="{n}" style="width: 32px; height: 32px; border-radius: 50%; background: {c}; box-shadow: inset 0 0 0 1px rgba(30,42,58,0.15){", 0 0 0 2px "+CLOUD+", 0 0 0 3.5px "+NIGHT if n==sel else ""};"></span>' for n,c in cols)
    return f'<div style="display: flex; flex-direction: column; gap: 10px;"><span style="font-size: 14px;">Colour · <b>{sel}</b></span><div style="display: flex; gap: 12px;">{dots}</div></div>'
def bullets(items):
    return '<div style="display: flex; flex-direction: column; gap: 8px;">'+''.join(f'<div style="display: flex; gap: 10px; align-items: flex-start; font-size: 15px;">{ico("check",18)}<span>{t}</span></div>' for t in items)+'</div>'
def reassure(items):
    return '<div style="display: flex; gap: 22px; padding-top: 4px;">'+''.join(f'<div style="display: flex; align-items: center; gap: 8px; font-size: 13.5px;">{ico(i,20)}<span>{t}</span></div>' for i,t in items)+'</div>'
NECK_B=['Two heights on one pillow: 13 cm and 11 cm (5.1 / 4.3 in)','Memory foam that holds its shape through the night','Cool-touch cover included, machine washable']
REAS=[('moon','30-night trial'),('truck','Free shipping'),('wash','Washable cover')]
def featured(mobile=False):
    if mobile:
        return f"""<div style="padding: 32px 20px; display: flex; flex-direction: column; gap: 20px;">
  <img src="neck.jpg" alt="Neck 01 in Cloud" style="width: 100%; border-radius: 24px; display: block;">
  <h2 style="font-size: 34px;">Neck 01 — Memory-foam pillow</h2>{bullets(NECK_B)}<div class="price" style="font-size: 22px; font-weight: 500;">€69.90</div>{swatches()}<a class="btn" href="#" style="height: 52px;">Add to bag</a>{reassure(REAS)}
</div>"""
    return f"""<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 56px; padding: 56px 56px; align-items: center;">
  <img src="neck.jpg" alt="Neck 01 in Cloud" style="width: 100%; border-radius: 28px; display: block;">
  <div style="display: flex; flex-direction: column; gap: 18px; max-width: 520px;">
    <h2 style="font-size: 44px;">Neck 01 — Memory-foam pillow</h2>{bullets(NECK_B)}<div class="price" style="font-size: 24px; font-weight: 500;">€69.90</div>{swatches()}<a class="btn" href="#" style="height: 54px; font-size: 16px;">Add to bag</a>{reassure(REAS)}
  </div>
</div>"""
WHY=[('Two heights, one pillow','13 cm on one side, 11 cm on the other. Turn it over until your head lies level with your shoulders. Most people know after two nights.'),('Foam that holds','Memory foam takes the shape of your neck and keeps it, instead of flattening under your head by three in the morning.'),('A cover you can wash','The cool-touch cover comes with the pillow. Unzip it, machine wash it, put it back. A spare is €16.90.')]
def why(cols=3, pad='48px 56px', items=WHY, title='Why it <em>holds</em>.', bg=None, card=MIST):
    cards=''.join(f'<div style="background: {card}; border-radius: 28px; padding: 32px; display: flex; flex-direction: column; gap: 10px;"><h3 style="font-size: 24px;">{t}</h3><p style="margin: 0; font-size: 15px; line-height: 1.55;">{x}</p></div>' for t,x in items)
    return f'<div style="padding: {pad}; {"background: "+bg+";" if bg else ""} display: flex; flex-direction: column; gap: 28px;"><h2 style="font-size: 44px;">{title}</h2><div style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); gap: 24px;">{cards}</div></div>'
def materials():
    return f"""<div style="padding: 0 56px;"><div style="background: {MIST}; border-radius: 48px; padding: 56px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 56px; align-items: center;">
  <img src="contour-bed.jpg" alt="Contour 01 on a bed" style="width: 100%; border-radius: 28px; display: block;">
  <div style="display: flex; flex-direction: column; gap: 18px;"><span class="label">Materials</span><h2 style="font-size: 44px;">Memory foam. <em>Cool-touch cover.</em> Nothing else.</h2><p style="margin: 0; font-size: 16px; line-height: 1.6;">Every Somnila pillow is a memory-foam core with a removable cover. Neck 01 and Contour 01 come with a cooling cover; Body 01 with a breathable cotton one. Dimensions and weight are on every product page, in centimetres and inches.</p><div><a class="btn outline" href="#">See all pillows</a></div></div>
</div></div>"""
RANGE=[('neck.jpg','Neck 01','Memory-foam pillow','€69.90'),('contour.jpg','Contour 01','Contoured comfort pillow','€59.90'),('side.jpg','Side 01','Side-sleeper pillow','€54.90'),('body.jpg','Body 01','S-shaped body pillow','€69.90'),('lounge.jpg','Lounge 01','Reading pillow','€54.90')]
def pcard(img,name,sub,price):
    return f'<div class="card" style="display: flex; flex-direction: column;"><div style="aspect-ratio: 1 / 1; background: {MIST};"><img src="{img}" alt="{name}" style="width: 100%; height: 100%; object-fit: cover; display: block;"></div><div style="padding: 18px 20px 22px; display: flex; flex-direction: column; gap: 4px;"><div style="font-weight: 600; font-size: 16px;">{name}</div><div style="font-size: 14px; color: {SLATE};">{sub}</div><div class="price" style="font-size: 15px; margin-top: 4px;">{price}</div></div></div>'
def range_(cols=3, n=3, pad='48px 56px', title='Five pillows, <em>one job each</em>.', desc='Named like objects, numbered like versions. Each one has a height and a shape for one way of lying.', items=None):
    items=items or RANGE[:n]
    cards=''.join(pcard(*i) for i in items)
    return f'<div style="padding: {pad}; display: flex; flex-direction: column; gap: 24px;"><div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 24px;"><div style="display: flex; flex-direction: column; gap: 8px; max-width: 640px;"><h2 style="font-size: 44px;">{title}</h2><p style="margin: 0; font-size: 16px;">{desc}</p></div><a href="#" style="font-weight: 500; text-decoration: underline; text-underline-offset: 0.2em; white-space: nowrap;">View all</a></div><div style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); gap: 24px;">{cards}</div></div>'
FAQ=[('How long does delivery take?','6 to 10 days, tracked, to the United States, Canada, the United Kingdom, Europe and Australia. You get the tracking number by email the day it ships.'),('Is shipping free?','On every pillow and every set, yes. Only accessories bought on their own pay shipping.'),('How does the 30-night trial work?','Sleep on the pillow for up to 30 nights from delivery. If it isn\'t right, send us an email with your order number and we refund the price of the pillow.'),('Which height should I choose?','Neck 01 has both: 13 cm on one side, 11 cm on the other. Start with the higher side; if your head tilts up, turn the pillow over.'),('Can I wash the cover?','Yes. Unzip it and machine wash it cold on a gentle cycle, then dry it flat.')]
def faq(items=FAQ, pad='48px 56px', openfirst=True, title='Before you <em>order</em>.'):
    rows=''
    for i,(q,a) in enumerate(items):
        op = openfirst and i==0
        ans = ('<p style="margin: 0; font-size: 15px; color: '+SLATE+'; max-width: 640px;">'+a+'</p>') if op else ''
        rows+=f'<div style="border-top: 1px solid rgba(30,42,58,0.12); padding: 18px 0; display: flex; flex-direction: column; gap: 8px;"><div style="display: flex; justify-content: space-between; align-items: center; gap: 16px;"><span style="font-weight: 600; font-size: 16px;">{q}</span>{ico("plus",20)}</div>{ans}</div>'
    return f'<div style="padding: {pad}; display: flex; flex-direction: column; gap: 20px;"><span class="label">FAQ</span><h2 style="font-size: 44px;">{title}</h2><div style="background: {MIST}; border-radius: 28px; padding: 8px 32px;">{rows}</div></div>'
SETS=[('neck.jpg','Neck 01 + Cover','Pillow and a spare cover','€76.90'),('neck-night.jpg','Sleep Set','Neck 01, Mask 01, Quiet 01','€99.90'),('neck-sky.jpg','For Two','2 × Neck 01','€119.90'),('neck.jpg','Family Set','3 × Neck 01','€169.90')]
def sets():
    return f'<div style="background: {MIST};">{range_(4,4,"56px 56px","Sets, <em>priced honestly</em>.","Two or three pieces together cost less than apart. The saving is on the price tag, not in a fake strike-through.",SETS)}</div>'
def newsletter(pad='64px 56px'):
    return f'<div style="padding: {pad}; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 16px;"><h2 style="font-size: 40px;">Notes from the workshop</h2><p style="margin: 0; max-width: 520px; font-size: 16px;">One email a month at most: what we are making, what we refused to make. No countdowns, no fake sales.</p><div style="display: flex; gap: 8px; width: min(420px, 100%);"><div style="flex: 1; height: 48px; border: 1px solid rgba(30,42,58,0.3); border-radius: 999px; display: flex; align-items: center; padding: 0 20px; color: {SLATE}; font-size: 15px;">Email</div><span class="btn" style="width: 48px; padding: 0;">{ico("arrow",20,CLOUD)}</span></div></div>'
def footer(mobile=False):
    col=lambda h,items: f'<div style="display: flex; flex-direction: column; gap: 10px;"><div class="label" style="color: rgba(247,249,252,0.7);">{h}</div>'+''.join(f'<a href="#" style="color: {CLOUD}; font-size: 14.5px;">{i}</a>' for i in items)+'</div>'
    cols=col('Shop',['Pillows','Sets','Accessories','Covers','Shop all'])+col('Help',['FAQ','Shipping & delivery','Returns & 30-night trial','Our story','Contact'])+col('Legal',['Privacy policy','Terms of service','Refund policy','Shipping policy'])
    brand=f'<div style="display: flex; flex-direction: column; gap: 12px; max-width: 320px;"><img src="logo-dark.svg" alt="Somnila" style="width: 150px; height: 34px; display: block;"><div class="serif" style="font-size: 22px; color: {CLOUD};">Sleep well.</div><p style="margin: 0; font-size: 14px; color: rgba(247,249,252,0.75); line-height: 1.55;">Pillows and sleep accessories shaped around the way you actually lie. Foam that holds its shape, covers you can wash, 30 nights to decide.</p></div>'
    grid = f'<div style="display: grid; grid-template-columns: 1.6fr 1fr 1fr 1fr; gap: 40px;">{brand}{cols}</div>' if not mobile else f'<div style="display: flex; flex-direction: column; gap: 32px;">{brand}<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px;">{cols}</div></div>'
    pay=''.join(f'<span style="height: 24px; padding: 0 8px; border-radius: 4px; background: rgba(247,249,252,0.12); font-size: 10px; letter-spacing: 0.06em; display: inline-flex; align-items: center; color: {CLOUD};">{p}</span>' for p in ('VISA','MC','AMEX','PAYPAL','APPLE PAY','G PAY','SHOP'))
    bottom=f'<div style="display: flex; {"flex-direction: column; gap: 16px;" if mobile else "justify-content: space-between; align-items: center;"} padding-top: 28px; border-top: 1px solid rgba(247,249,252,0.15);"><div style="display: inline-flex; align-items: center; gap: 8px; height: 40px; padding: 0 16px; border: 1px solid rgba(247,249,252,0.35); border-radius: 999px; color: {CLOUD}; font-size: 14px; width: fit-content;">{ico("globe",18,CLOUD)}United States · USD ${ico("chev",16,CLOUD)}</div><div style="display: flex; gap: 6px; flex-wrap: wrap;">{pay}</div><div style="font-size: 13px; color: rgba(247,249,252,0.6);">© 2026 Somnila</div></div>'
    return f'<div style="background: {NIGHT}; color: {CLOUD}; padding: {"48px 20px 32px" if mobile else "64px 56px 32px"}; display: flex; flex-direction: column; gap: 36px;">{grid}{bottom}</div>'

# ---------- Main (home desktop)
main = head('Somnila — Home') + f'<div style="width: 1440px; background: {CLOUD};">' + announcement(ANN,1440) + header_desktop() + hero_desktop() + trust() + featured() + why() + materials() + range_() + faq() + sets() + newsletter() + footer() + '</div>' + FOOT
open('Main.dc.html','w').write(main)

# ---------- Home mobile
mob = head('Somnila — Home mobile') + f'<div style="width: 390px; background: {CLOUD};">' + announcement(ANN,390,True) + header_mobile() + hero_mobile() + trust(2,'20px 20px') + featured(True) + why(1,'32px 20px') + f'<div style="padding: 0 20px;"><div style="background: {MIST}; border-radius: 32px; padding: 28px 24px; display: flex; flex-direction: column; gap: 14px;"><span class="label">Materials</span><h2 style="font-size: 30px;">Memory foam. <em>Cool-touch cover.</em> Nothing else.</h2><img src="contour-bed.jpg" alt="Contour 01 on a bed" style="width: 100%; border-radius: 20px; display: block;"><p style="margin: 0; font-size: 15px;">A memory-foam core with a removable cover, on every pillow. Dimensions and weight on every product page, in cm and inches.</p></div></div>' + range_(2,2,'32px 20px') + faq(FAQ[:3],'32px 20px') + newsletter('40px 20px') + footer(True) + '</div>' + FOOT
open('HomeMobile.dc.html','w').write(mob)

# ---------- Product page desktop
def acc(t, open_=False, body=''):
    inner = ('<p style="margin: 0; font-size: 14.5px; color: '+SLATE+';">'+body+'</p>') if open_ else ''
    return f'<div style="border-top: 1px solid rgba(30,42,58,0.12); padding: 16px 0; display: flex; flex-direction: column; gap: 8px;"><div style="display: flex; justify-content: space-between; align-items: center;"><span style="font-weight: 600; font-size: 15px;">{t}</span>{ico("plus",18)}</div>{inner}</div>'
thumbs=''.join(f'<div style="width: 72px; height: 72px; border-radius: 16px; overflow: hidden; background: {MIST}; {"box-shadow: 0 0 0 2px "+NIGHT+";" if i==0 else ""}"><img src="{im}" alt="" style="width: 100%; height: 100%; object-fit: cover; display: block;"></div>' for i,im in enumerate(['neck.jpg','neck-night.jpg','neck-sky.jpg','neck.jpg']))
upsell=''.join(f'<div style="display: flex; align-items: center; gap: 12px; background: {MIST}; border-radius: 16px; padding: 10px 14px;"><span style="width: 18px; height: 18px; border-radius: 5px; border: 1.5px solid {NIGHT};"></span><img src="{im}" alt="" style="width: 40px; height: 40px; border-radius: 10px; object-fit: cover;"><div style="flex: 1; font-size: 14px;"><b>{n}</b> · {d}</div><div class="price" style="font-size: 14px;">+ {p}</div></div>' for im,n,d,p in (('mask.jpg','Mask 01','contoured sleep mask','€19.90'),('neck-sky.jpg','Quiet 01','earplugs, 2 pairs','€14.90')))
specs=f"""<div style="display: flex; flex-direction: column; gap: 6px;"><span class="label">Dimensions</span><table style="border-collapse: collapse; font-size: 14.5px; font-variant-numeric: tabular-nums;"><tr><th style="text-align: left; font-weight: 500; color: {SLATE}; padding: 3px 24px 3px 0;">Metric</th><td>62 × 42 × 13/11 cm</td></tr><tr><th style="text-align: left; font-weight: 500; color: {SLATE}; padding: 3px 24px 3px 0;">Imperial</th><td>24.4 × 16.5 × 5.1/4.3 in</td></tr><tr><th style="text-align: left; font-weight: 500; color: {SLATE}; padding: 3px 24px 3px 0;">Weight</th><td>1.4 kg (3.1 lb)</td></tr></table><span class="label" style="margin-top: 8px;">Materials</span><span style="font-size: 14.5px;">Memory foam. Cooling cover.</span><span class="label" style="margin-top: 8px;">Delivery</span><span style="font-size: 14.5px;">Ships in 6–10 days, tracked.</span></div>"""
ACCS = acc("30-night trial & returns",True,"Sleep on it for up to 30 nights from delivery. If it isn't right, email us with your order number and we refund the price of the pillow. You don't need to send it back.")+acc("Shipping")+acc("Care")
buybox=f"""<div style="display: flex; flex-direction: column; gap: 18px;">
  <h1 style="font-size: 44px; font-variation-settings: 'opsz' 96, 'SOFT' 100;">Neck 01 — Memory-foam pillow</h1>
  {bullets(['Ships in 6–10 days, tracked','30-night trial, refund by email','Removable cover included, machine washable'])}
  <div class="price" style="font-size: 26px; font-weight: 500;">€69.90</div>
  {swatches()}
  <div style="display: flex; flex-direction: column; gap: 8px;"><span class="label">Complete the night</span>{upsell}</div>
  <a class="btn" href="#" style="height: 56px; font-size: 16px;">Add to bag</a>
  <div style="display: flex; gap: 6px;">{''.join(f'<span style="height: 22px; padding: 0 7px; border-radius: 4px; background: {MIST}; font-size: 9.5px; letter-spacing: 0.06em; display: inline-flex; align-items: center;">{p}</span>' for p in ('VISA','MC','AMEX','PAYPAL','APPLE PAY','G PAY','SHOP'))}</div>
  <div style="display: flex; gap: 10px; align-items: center; font-size: 14px;">{ico('truck',20)}<span>Ships in 6–10 days, tracked. Estimated delivery <b>Tue Sep 16</b> to <b>Sat Sep 20</b>.</span></div>
  {reassure(REAS)}
  <div style="height: 1px; background: rgba(30,42,58,0.12);"></div>
  <p style="margin: 0; font-size: 15px; line-height: 1.6;">Neck 01 is our contoured memory-foam pillow. Two heights, one on each side, so you choose the one that fits the way you lie. The foam holds its shape through the night instead of flattening under your head. The cover is included. It has a cool-touch surface and goes in the washing machine.</p>
  {specs}
  <div>{ACCS}</div>
</div>"""
band=f'<div style="background: {NIGHT}; color: {CLOUD}; padding: 64px 56px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 16px;"><h2 style="font-size: 44px; color: {DAWN};">Thirty nights to decide.</h2><p style="margin: 0; max-width: 560px; font-size: 16px; color: rgba(247,249,252,0.85);">You sleep on it at home, on your real nights. If it isn\'t right, one email with your order number and we refund the pillow. No form, nothing to send back.</p><a class="btn outline" href="#" style="color: {CLOUD}; border-color: rgba(247,249,252,0.5);">How the trial works</a></div>'
WHYP=[('Shaped for one position','Each Somnila pillow is cut for one way of lying, with a height and a contour to match. Not a block, not a bag of fibre.'),('Foam that holds','Memory foam takes the shape of your neck and keeps it through the night instead of flattening.'),('A cover you can wash','Removable and machine washable. It comes with the pillow, and a spare is €16.90.')]
PFAQ=[('How long does delivery take?','6 to 10 days, tracked. You get the tracking number by email the day it ships.'),('What if it isn\'t right for me?','Email us within 30 nights of delivery with your order number. We refund the pillow; you don\'t need to send it back.'),('Does the foam smell when new?','New foam can have a light smell for the first hours. Air the pillow uncovered for half a day before the first night.'),('How do I wash it?','The cover goes in the machine, cold, gentle cycle, dried flat. The foam takes a damp cloth only.')]
GOES=[('neck-night.jpg','Cover for Neck 01','Cooling replacement cover','€16.90'),('mask.jpg','Mask 01','Contoured sleep mask','€19.90'),('neck-sky.jpg','Neck 01 + Cover','Pillow and a spare cover','€76.90'),('body.jpg','Side-Sleeper Set','Neck 01 + Body 01','€119.90')]
prod = head('Somnila — Neck 01') + f'<div style="width: 1440px; background: {CLOUD};">' + announcement(ANN,1440) + header_desktop() + f"""
<div style="padding: 20px 56px 0; font-size: 13px; color: {SLATE};">Home · Pillows · <span style="color: {NIGHT};">Neck 01</span></div>
<div style="display: grid; grid-template-columns: 88px 1fr 520px; gap: 32px; padding: 20px 56px 56px; align-items: start;">
  <div style="display: flex; flex-direction: column; gap: 10px;">{thumbs}</div>
  <div style="border-radius: 28px; overflow: hidden; background: {MIST}; aspect-ratio: 1 / 1;"><img src="neck.jpg" alt="Neck 01 in Cloud" style="width: 100%; height: 100%; object-fit: cover; display: block;"></div>
  {buybox}
</div>""" + why(3,'56px 56px',WHYP,'What you are <em>buying</em>.',MIST,CLOUD) + band + faq(PFAQ,'56px 56px') + range_(4,4,'48px 56px','Goes with it','',GOES) + footer() + '</div>' + FOOT
open('Product.dc.html','w').write(prod)

canvas={"artboards":[
  {"file":"Main.dc.html","title":"Home · desktop","x":0,"y":0,"w":1440,"h":4300,"expand":"fit"},
  {"file":"HomeMobile.dc.html","title":"Home · mobile","x":1560,"y":0,"w":390,"h":3900,"expand":"fit"},
  {"file":"Product.dc.html","title":"Neck 01 · product page","x":2080,"y":0,"w":1440,"h":3700,"expand":"fit"}],
 "annotations":[
  {"id":"note-brief","x":0,"y":-190,"w":520,"text":"Maquettes du thème Shrine « Somnila — build v1 » (Phase 4).\nMêmes textes, prix et images que dans Shopify. Palette Cloud / Mist / Night / Dawn, Fraunces Soft + Manrope.\nVisuel hero provisoire (packshot fournisseur détouré sur ciel) : remplacé en Phase 5."},
  {"id":"note-reviews","x":560,"y":-190,"w":420,"text":"Pas de section avis sur la maquette : elle existe dans le thème mais reste désactivée tant qu'il n'y a pas de vrais avis."},
  {"id":"note-mobile","x":1560,"y":-120,"w":390,"text":"Mobile : hero 4:5, texte en bas, boutons pleine largeur, tuiles confiance en 2 × 2."}],
 "launch":{"view":"canvas"}}
json.dump(canvas,open('canvas.json','w'),indent=1)
print('artboards written', len(main), len(mob), len(prod))
