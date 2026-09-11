# Phase 5 — packshots Somnila : détourage des photos fournisseur (fond uni ou dégradé) et pose sur le ciel Cloud → Mist.
import csv, os, sys, glob
import numpy as np, cv2
from PIL import Image
SRC='build/images/shopify'; OUT='build/images/site/packshots'
CLOUD=np.array([247,249,252],np.float32); MIST=np.array([220,232,242],np.float32); DAWN=np.array([240,183,155],np.float32); NIGHT=np.array([30,42,58],np.float32)

def sky(W,H,halo_cx=0.55,halo_cy=0.42,halo_a=0.22):
    y=np.linspace(0,1,H)[:,None,None]; x=np.linspace(0,1,W)[None,:,None]
    g=CLOUD*(1-y)+MIST*y
    r=np.sqrt(((x-halo_cx)/0.55)**2+((y-halo_cy)/0.45)**2); halo=np.clip(1-r,0,1)**2*halo_a
    return g*(1-halo)+DAWN*halo

def matte(rgb, light_on_light=False):
    a=rgb.astype(np.float32); H,W,_=a.shape
    top=np.median(a[:12],axis=0); bot=np.median(a[-12:],axis=0)
    t=np.linspace(0,1,H)[:,None,None]; bg=top[None]*(1-t)+bot[None]*t
    # fond par ligne depuis les marges quand elles sont cohérentes (dégradés verticaux non linéaires)
    m=max(16,W//40); L=np.median(a[:,:m,:],axis=1); R=np.median(a[:,-m:,:],axis=1)
    ok=(np.abs(L-R).max(axis=1)<10)&(a[:,:m,:].std(axis=(1,))).max(axis=1).__lt__(6)&(a[:,-m:,:].std(axis=(1,))).max(axis=1).__lt__(6)
    row=(L+R)/2
    if ok.mean()>0.6:
        ys=np.where(ok)[0]; row_i=np.stack([np.interp(np.arange(H),ys,row[ys,c]) for c in range(3)],axis=1)
        bg=np.repeat(row_i[:,None,:],W,axis=1)
    bg=cv2.GaussianBlur(bg.astype(np.float32),(0,0),25)
    lab=cv2.cvtColor(np.clip(a,0,255).astype(np.uint8),cv2.COLOR_RGB2LAB).astype(np.float32)
    labbg=cv2.cvtColor(np.clip(bg,0,255).astype(np.uint8),cv2.COLOR_RGB2LAB).astype(np.float32)
    dL=lab[...,0]-labbg[...,0]; dC=np.sqrt((lab[...,1]-labbg[...,1])**2+(lab[...,2]-labbg[...,2])**2)
    product=(dC>6)|(dL<-38)|(dL>6)
    if light_on_light: product=(dC>4)|(dL<-38)|(dL>2.5)
    shadow=(~product)&(dL<-3)&(dC<7)
    m=product.astype(np.uint8)
    k=15 if light_on_light else 7
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((3,3),np.uint8)); m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((k,k),np.uint8))
    n,lab_,stats,_=cv2.connectedComponentsWithStats(m,8); keep=np.zeros_like(m)
    for i in range(1,n):
        if stats[i,cv2.CC_STAT_AREA]>0.003*H*W: keep[lab_==i]=1
    # bouchage des trous
    ff=np.pad(keep,1); h,w=ff.shape; mask=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,mask,(0,0),2)
    keep[(ff[1:-1,1:-1]!=2)]=1
    alpha=cv2.GaussianBlur(keep.astype(np.float32),(0,0),1.1)
    sh=np.clip(-dL/45.0,0,1)*shadow; sh=cv2.GaussianBlur(sh.astype(np.float32),(0,0),6)*(1-alpha)
    al=alpha[...,None]; col=np.where(al>0.03,(a-(1-al)*bg)/np.maximum(al,0.03),a); col=np.clip(col,0,255)
    return col, alpha, sh

def compose(rgb, W, H, width_frac=0.78, y_shift=0.04, light_on_light=False):
    col,alpha,sh=matte(rgb, light_on_light)
    ys,xs=np.where(alpha>0.5)
    if len(xs)<100: return None
    x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max(); pad=int(0.06*max(x1-x0,y1-y0))
    box=(max(0,x0-pad),max(0,y0-pad),min(rgb.shape[1],x1+pad),min(rgb.shape[0],y1+pad))
    c=col[box[1]:box[3],box[0]:box[2]]; a=alpha[box[1]:box[3],box[0]:box[2]]; s=sh[box[1]:box[3],box[0]:box[2]]
    tw=int(W*width_frac); scale=tw/c.shape[1]
    if c.shape[0]*scale>H*0.72: scale=H*0.72/c.shape[0]; tw=int(c.shape[1]*scale)
    th=int(c.shape[0]*scale)
    c=cv2.resize(c,(tw,th),interpolation=cv2.INTER_LANCZOS4); a=cv2.resize(a,(tw,th),interpolation=cv2.INTER_AREA); s=cv2.resize(s,(tw,th),interpolation=cv2.INTER_AREA)
    canvas=sky(W,H); ox=(W-tw)//2; oy=(H-th)//2+int(H*y_shift)
    region=canvas[oy:oy+th,ox:ox+tw]
    # ombre naturelle du fournisseur, teintée Night, + ombre de contact douce
    region=region*(1-0.55*s[...,None])+NIGHT*(0.55*s[...,None])*0.0
    region=region*(1-0.45*s[...,None])
    region=c*a[...,None]+region*(1-a[...,None])
    canvas[oy:oy+th,ox:ox+tw]=region
    return np.clip(canvas,0,255).astype(np.uint8)

if __name__=='__main__':
    rows=list(csv.DictReader(open('build/images/shopify.csv')))
    only=set(sys.argv[1:])
    done=[]
    for r in rows:
        if r['usage']!='packshot': continue
        if only and r['handle'] not in only: continue
        f=r['file']; v2=f.replace('_v1.jpg','_v2.jpg')
        path=f'{SRC}/{v2}' if os.path.exists(f'{SRC}/{v2}') else f'{SRC}/{f}'
        if not os.path.exists(path): print('absent',path); continue
        rgb=np.array(Image.open(path).convert('RGB'))
        base=os.path.basename(path).replace('.jpg','').replace('_1x1','').replace('_4x5','')
        for tag,(W,H) in {'1x1':(1200,1200),'4x5':(1200,1500)}.items():
            out=compose(rgb,W,H,light_on_light=('side-01' in base or 'cover-side' in base))
            if out is None: print('échec matte',path); break
            Image.fromarray(out).save(f'{OUT}/{base}_sky_{tag}.jpg',quality=90,subsampling=0)
        done.append(base)
    print(len(done),'packshots composés')
