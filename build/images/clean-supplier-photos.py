import numpy as np, cv2, os
from PIL import Image
SRC='clean'; OUT='clean/out'; CHK='clean/check'
def load(n): return cv2.cvtColor(np.array(Image.open(f'{SRC}/{n}.jpg').convert('RGB')),cv2.COLOR_RGB2BGR)
def save(n,img): cv2.imwrite(f'{OUT}/{n}.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,92])
def check(n,orig,mask,res):
    ov=orig.copy(); ov[mask>0]=(0.4*ov[mask>0]+0.6*np.array([0,0,255])).astype(np.uint8)
    both=np.hstack([ov,res]); cv2.imwrite(f'{CHK}/{n}.jpg',cv2.resize(both,(1200,600)),[cv2.IMWRITE_JPEG_QUALITY,85])
def inpaint(img,mask,r=7): return cv2.inpaint(img,mask,r,cv2.INPAINT_TELEA)

# 1. Contour 01 : bande de badges remplie par interpolation verticale colonne par colonne (fond uni avec vignette)
for n in ['somnila_contour-01_packshot-night_1x1_v1','somnila_contour-01_packshot-cloud-6_1x1_v1','somnila_contour-01_packshot-blush-7_1x1_v1','somnila_contour-01_packshot-stone-8_1x1_v1','somnila_contour-01_packshot-blue-10_1x1_v1']:
    im=load(n).astype(np.float32); H,W,_=im.shape; y0,y1=105,312
    top=cv2.GaussianBlur(im[y0-6:y0,:,:].mean(axis=0,keepdims=True),(0,0),9)[0]; bot=cv2.GaussianBlur(im[y1:y1+6,:,:].mean(axis=0,keepdims=True),(0,0),9)[0]
    res=im.copy()
    for y in range(y0,y1):
        t=(y-y0)/(y1-y0); res[y]=top*(1-t)+bot*t
    # léger grain pour éviter l'aplat trop lisse
    noise=np.random.default_rng(1).normal(0,1.2,(y1-y0,W,1)).astype(np.float32); res[y0:y1]+=noise
    res=np.clip(res,0,255).astype(np.uint8); mask=np.zeros((H,W),np.uint8); mask[y0:y1,:]=255
    save(n,res); check(n,im.astype(np.uint8),mask,res)

# 2. Neck 01 : caractère chinois en bas à gauche, inpainting sur fond dégradé
for n in ['somnila_neck-01_packshot-night-3_1x1_v1','somnila_neck-01_packshot-stone-4_1x1_v1']:
    im=load(n); H,W,_=im.shape; mask=np.zeros((H,W),np.uint8); mask[600:735,80:215]=255
    res=inpaint(im,mask,9); save(n,res); check(n,im,mask,res)

# 3. Side 01 : étiquette couleur, cotes et flèches
def side_mask(H,W):
    m=np.zeros((H,W),np.uint8)
    cv2.rectangle(m,(440,30),(775,115),255,-1)      # étiquette couleur en haut à droite
    cv2.rectangle(m,(8,190),(100,245),255,-1)       # 10cm
    cv2.rectangle(m,(22,240),(58,368),255,-1)       # flèche verticale
    cv2.rectangle(m,(160,520),(255,575),255,-1)     # 60cm
    cv2.rectangle(m,(695,520),(790,575),255,-1)     # 33cm
    cv2.line(m,(26,405),(492,640),255,22)           # cote 60cm
    cv2.line(m,(492,640),(792,442),255,22)          # cote 33cm
    cv2.rectangle(m,(20,395),(40,420),255,-1); cv2.rectangle(m,(482,625),(502,655),255,-1); cv2.rectangle(m,(780,430),(798,455),255,-1)
    return m
for n in ['somnila_side-01_packshot-blue_1x1_v1','somnila_side-01_packshot-dark-grey-2_1x1_v1','somnila_side-01_packshot-red-4_1x1_v1']:
    im=load(n); H,W,_=im.shape; mask=side_mask(H,W)
    res=inpaint(im,mask,9); save(n,res); check(n,im,mask,res)

# 4. Quiet 01 : surimpressions effacées, boîte de marque retirée par recadrage sur l'étui
def quiet(n):
    im=load(n); H,W,_=im.shape
    mask=np.zeros((H,W),np.uint8)
    cv2.rectangle(m:=mask,(5,35),(275,125),255,-1); cv2.rectangle(mask,(600,40),(790,120),255,-1)   # iMeBoBo / 4枚装
    cv2.rectangle(mask,(140,635),(655,750),255,-1)                                                  # bandeau du bas
    cv2.rectangle(mask,(335,245),(450,290),255,-1)                                                  # iMeBoBo sur la face du dessus, vu à travers le couvercle
    im2=inpaint(im,mask,9)
    # recadrage sur l'étui (la boîte imprimée reste hors champ) puis remise au carré sur fond échantillonné
    crop=im2[240:600,212:800]; bg=np.median(im2[5:30,300:500].reshape(-1,3),axis=0)
    ch,cw=crop.shape[:2]; scale=690/cw; crop=cv2.resize(crop,(690,int(ch*scale)),interpolation=cv2.INTER_LANCZOS4)
    canvas=np.full((800,800,3),bg,np.uint8); y=(800-crop.shape[0])//2+20; x=(800-690)//2
    # fondu des bords du recadrage vers le fond
    alpha=np.ones(crop.shape[:2],np.float32); f=28
    alpha[:f,:]*=np.linspace(0,1,f)[:,None]; alpha[-f:,:]*=np.linspace(1,0,f)[:,None]; alpha[:,:f]*=np.linspace(0,1,f)[None,:]; alpha[:,-f:]*=np.linspace(1,0,f)[None,:]
    region=canvas[y:y+crop.shape[0],x:x+690].astype(np.float32); canvas[y:y+crop.shape[0],x:x+690]=(crop*alpha[...,None]+region*(1-alpha[...,None])).astype(np.uint8)
    save(n,canvas); check(n,im,mask,canvas)
for n in ['somnila_quiet-01_packshot-blue_1x1_v1','somnila_quiet-01_packshot-green-2_1x1_v1','somnila_quiet-01_packshot-butter-3_1x1_v1','somnila_quiet-01_packshot-blush-4_1x1_v1']: quiet(n)
print(sorted(os.listdir(OUT)))
