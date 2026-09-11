# Phase 5 — visuels Somnila composés à partir des packshots détourés : bannières de collection, pubs statiques, en-tête email, réseaux, image de partage.
import numpy as np, cv2, os, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
exec(open('build/images/site/sky-packshots.py').read().split("if __name__=='__main__':")[0])
OUT='build/images/site'
NIGHT=(30,42,58); CLOUDc=(247,249,252); MISTc=(220,232,242); DAWNc=(240,183,155); SLATE=(107,125,144)
FR='build/brand/fonts/Fraunces-var.ttf'; MR='build/brand/fonts/Manrope-var.ttf'
def font(path,size,axes=None):
    f=ImageFont.truetype(path,size)
    if axes:
        try:
            names=[a['name'] if isinstance(a['name'],str) else a['name'].decode() for a in f.get_variation_axes()]
            vals=[axes.get(n, a['default']) for n,a in zip(names,f.get_variation_axes())]
            f.set_variation_by_axes(vals)
        except Exception as e: print('axes',path,e)
    return f
def serif(size): return font(FR,size,{'Optical Size':min(144,max(9,size/2)),'Weight':400,'Softness':100,'Wonky':0})
def sans(size,w=500): return font(MR,size,{'Weight':w})
def cutout(path, method):
    rgb=np.array(Image.open(path).convert('RGB'))
    col,alpha,sh=(matte_gc(rgb,'rect','rows') if method=='rows' else matte_gc(rgb,'rect','poly',thr=(6,6),grow=0) if method=='side' else matte(rgb,'interp'))
    ys,xs=np.where(alpha>0.5); pad=int(0.04*max(xs.max()-xs.min(),ys.max()-ys.min()))
    box=(max(0,xs.min()-pad),max(0,ys.min()-pad),min(rgb.shape[1],xs.max()+pad),min(rgb.shape[0],ys.max()+pad))
    c=col[box[1]:box[3],box[0]:box[2]]; a=alpha[box[1]:box[3],box[0]:box[2]]; s=sh[box[1]:box[3],box[0]:box[2]]
    return Image.fromarray(np.dstack([c,a*255]).astype(np.uint8),'RGBA'), Image.fromarray((s*255).astype(np.uint8),'L')
def skyimg(W,H,cx=0.6,cy=0.45,a=0.22): return Image.fromarray(np.clip(sky(W,H,cx,cy,a),0,255).astype(np.uint8),'RGB')
def place(canvas, cut, shadow, cx, cy, w, shadow_a=0.42):
    scale=w/cut.width; c=cut.resize((w,int(cut.height*scale)),Image.LANCZOS); s=shadow.resize(c.size,Image.LANCZOS)
    x,y=int(cx-c.width/2),int(cy-c.height/2)
    dark=Image.new('RGB',c.size,NIGHT); m=Image.fromarray((np.asarray(s).astype(np.float32)*shadow_a).astype(np.uint8),'L').filter(ImageFilter.GaussianBlur(6))
    canvas.paste(dark,(x,y),m); canvas.paste(c,(x,y),c); return canvas
def text_block(draw, x, y, lines, fnt, fill, spacing=1.12, anchor='la'):
    for ln in lines:
        draw.text((x,y),ln,font=fnt,fill=fill,anchor=anchor); y+=int(fnt.size*spacing)
    return y
def wrap(txt, fnt, maxw, draw):
    words=txt.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if draw.textlength(t,font=fnt)<=maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines
def wordmark(canvas, x, y, h, dark=True):
    lg=Image.open('build/brand/'+('somnila-logo-light.png' if dark else 'somnila-logo-dark.png')).convert('RGBA') if os.path.exists('build/brand/somnila-logo-light.png') else None
    if lg is None:
        for cand in ['build/brand/logo/somnila-logo-light.png','build/brand/logo/somnila-logo-dark.png']:
            if os.path.exists(cand): lg=Image.open(cand).convert('RGBA'); break
    if lg is None: return
    if not dark:
        for cand in ['build/brand/somnila-logo-dark.png','build/brand/logo/somnila-logo-dark.png']:
            if os.path.exists(cand): lg=Image.open(cand).convert('RGBA'); break
    s=h/lg.height; lg=lg.resize((int(lg.width*s),h),Image.LANCZOS); canvas.paste(lg,(x,y),lg)

neck,neck_sh=cutout('build/images/shopify/somnila_neck-01_packshot-cloud_1x1_v1.jpg','rows')
neck_night,neck_night_sh=cutout('build/images/shopify/somnila_neck-01_packshot-night-3_1x1_v2.jpg','rows')
contour,contour_sh=cutout('build/images/shopify/somnila_contour-01_packshot-night-2_1x1_v1.jpg','interp')
side,side_sh=cutout('build/images/shopify/somnila_side-01_packshot-blue_1x1_v2.jpg','side')
lounge,lounge_sh=cutout('build/images/shopify/somnila_lounge-01_packshot-stone-and-sand_4x5_v1.jpg','interp')
neck.save(f'{OUT}/neck-01-cloud-cutout-v2.png'); contour.save(f'{OUT}/contour-01-night-cutout.png'); side.save(f'{OUT}/side-01-blue-cutout.png'); lounge.save(f'{OUT}/lounge-01-cutout.png')

# 1. Bannières de collection 2400x800 (image de collection Shopify et en-tête de page)
banners={'memory-foam-pillows':('Pillows','Five shapes, one job each.',neck,neck_sh,0.34),'sets':('Sets','Two or three pieces, priced below the sum.',contour,contour_sh,0.34),'accessories':('Accessories','Mask 01, Quiet 01, Throw 01.',lounge,lounge_sh,0.20),'covers':('Covers','A spare for the wash day.',side,side_sh,0.34),'shop-all':('Everything','Pillows, sets, covers, accessories.',neck_night,neck_night_sh,0.34)}
for h,(title,sub,cut,sh,wf) in banners.items():
    W,H=2400,800; im=skyimg(W,H,0.72,0.5,0.2); place(im,cut,sh,int(W*0.74),int(H*0.55),int(W*wf)); d=ImageDraw.Draw(im)
    d.text((140,H//2-30),title,font=serif(150),fill=NIGHT,anchor='ls'); d.text((146,H//2+60),sub,font=sans(44),fill=SLATE,anchor='ls')
    im.save(f'{OUT}/banners/somnila_collection_{h}_3x1.jpg',quality=90,subsampling=0)

# 2. Pubs statiques : 3 messages x 3 formats. Textes réels uniquement (pas de prix : ils varient par marché).
ADS=[('sleep-well','Sleep well.','Neck 01. Memory foam with two heights, shaped around the way you actually lie.',neck,neck_sh),
     ('thirty-nights','Thirty nights to decide.','Sleep on it at home. If it isn\'t right, one email and we refund the pillow.',neck_night,neck_night_sh),
     ('two-heights','Two heights, one pillow.','13 cm on one side, 11 cm on the other. Turn it over until your head lies level.',contour,contour_sh)]
FORMATS={'1x1':(1080,1080),'4x5':(1080,1350),'9x16':(1080,1920)}
for slug,head,body,cut,sh in ADS:
    for tag,(W,H) in FORMATS.items():
        im=skyimg(W,H,0.55,0.38,0.24); d=ImageDraw.Draw(im); m=int(W*0.08)
        pw={'1x1':0.58,'4x5':0.72,'9x16':0.80}[tag]; cy={'1x1':0.33,'4x5':0.37,'9x16':0.38}[tag]
        place(im,cut,sh,W//2,int(H*cy),int(W*pw))
        wordmark(im,m,m,int(W*0.055),dark=True)
        hf=serif(int(W*(0.095 if tag=='1x1' else 0.105))); lines=wrap(head,hf,W-2*m,d); y={'1x1':0.57,'4x5':0.63,'9x16':0.60}[tag]*H
        y=text_block(d,m,int(y),lines,hf,NIGHT,1.02)
        bf=sans(int(W*(0.032 if tag=='1x1' else 0.036))); y=text_block(d,m,y+int(W*0.02),wrap(body,bf,W-2*m,d),bf,NIGHT,1.35)
        d.text((m,H-m),'Free shipping · 30-night trial · Ships in 6–10 days',font=sans(int(W*0.026),600),fill=SLATE,anchor='ls')
        im.save(f'{OUT}/ads/somnila_ad_{slug}_{tag}.jpg',quality=90,subsampling=0)

# 3. En-tête email 1200x400 (affiché 600x200) et pied
im=skyimg(1200,400,0.8,0.5,0.2); place(im,neck,neck_sh,960,210,420); wordmark(im,80,150,90,dark=True); d=ImageDraw.Draw(im); d.text((84,300),'Sleep well.',font=serif(64),fill=NIGHT,anchor='ls'); im.save(f'{OUT}/email/somnila_email_header_1200x400.jpg',quality=90,subsampling=0)
im=Image.new('RGB',(1200,300),NIGHT); wordmark(im,80,70,72,dark=False); d=ImageDraw.Draw(im); d.text((84,215),'Pillows shaped around the way you actually lie.',font=sans(28),fill=CLOUDc,anchor='ls'); im.save(f'{OUT}/email/somnila_email_footer_1200x300.jpg',quality=90,subsampling=0)

# 4. Réseaux : avatar 1024 (marque Dawn sur Night), couverture 1500x500, image de partage 1200x630
mark=None
for cand in ['build/brand/somnila-mark-dawn.png','build/brand/logo/somnila-mark-dawn.png']:
    if os.path.exists(cand): mark=Image.open(cand).convert('RGBA'); break
av=Image.new('RGB',(1024,1024),NIGHT)
if mark is not None:
    mk=mark.resize((560,int(mark.height*560/mark.width)),Image.LANCZOS); av.paste(mk,((1024-mk.width)//2,(1024-mk.height)//2),mk)
av.save(f'{OUT}/social/somnila_avatar_1024.png')
im=skyimg(1500,500,0.75,0.5,0.2); place(im,neck,neck_sh,1150,265,520); wordmark(im,100,190,110,dark=True); d=ImageDraw.Draw(im); d.text((104,360),'Sleep well.',font=serif(72),fill=NIGHT,anchor='ls'); im.save(f'{OUT}/social/somnila_cover_1500x500.jpg',quality=90,subsampling=0)
im=skyimg(1200,630,0.72,0.5,0.22); place(im,neck,neck_sh,880,330,520); wordmark(im,80,90,80,dark=True); d=ImageDraw.Draw(im)
y=text_block(d,84,250,['Sleep well.'],serif(110),NIGHT); text_block(d,86,y+10,wrap('Memory-foam pillows shaped around the way you actually lie. Cover included, 30-night trial.',sans(30),520,d),sans(30),SLATE,1.4)
im.save(f'{OUT}/social/somnila_share_1200x630.jpg',quality=90,subsampling=0)
print('ok', sum(len(f) for _,_,f in os.walk(OUT+'/ads')), 'pubs')
