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

def matte(rgb, bg_mode='interp', thr=(7,9)):
    a=rgb.astype(np.float32); H,W,_=a.shape
    if bg_mode=='poly':
        yy,xx=np.mgrid[0:H,0:W]; xn=xx/W-0.5; yn=yy/H-0.5
        frame=np.zeros((H,W),bool); mx,my=int(W*0.08),int(H*0.08); frame[:my,:]=True; frame[-my:,:]=True; frame[:,:mx]=True; frame[:,-mx:]=True
        F=np.stack([np.ones_like(xn),xn,yn,xn*xn,yn*yn,xn*yn],axis=-1); sel=frame.ravel(); Fs=F.reshape(-1,6)[sel]
        bg=np.zeros_like(a)
        for c in range(3):
            coef,_,_,_=np.linalg.lstsq(Fs,a[...,c].ravel()[sel],rcond=None); bg[...,c]=(F.reshape(-1,6)@coef).reshape(H,W)
    elif bg_mode=='rows':
        m=max(16,W//40); row=(np.median(a[:,:m,:],axis=1)+np.median(a[:,-m:,:],axis=1))/2
        row=cv2.GaussianBlur(row.reshape(H,1,3).astype(np.float32),(0,0),9).reshape(H,3)
        bg=np.repeat(row[:,None,:],W,axis=1)
    else:
        top=np.median(a[:12],axis=0); bot=np.median(a[-12:],axis=0)
        t=np.linspace(0,1,H)[:,None,None]; bg=top[None]*(1-t)+bot[None]*t
    bg=cv2.GaussianBlur(bg.astype(np.float32),(0,0),25)
    lab=cv2.cvtColor(np.clip(a,0,255).astype(np.uint8),cv2.COLOR_RGB2LAB).astype(np.float32)
    labbg=cv2.cvtColor(np.clip(bg,0,255).astype(np.uint8),cv2.COLOR_RGB2LAB).astype(np.float32)
    dL=lab[...,0]-labbg[...,0]; dC=np.sqrt((lab[...,1]-labbg[...,1])**2+(lab[...,2]-labbg[...,2])**2)
    product=(dC>thr[0])|(dL<-38)|(dL>thr[1])
    shadow=(~product)&(dL<-3)&(dC<7)
    m=product.astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((3,3),np.uint8)); m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8))
    n,lab_,stats,_=cv2.connectedComponentsWithStats(m,8); keep=np.zeros_like(m)
    for i in range(1,n):
        if stats[i,cv2.CC_STAT_AREA]>0.003*H*W: keep[lab_==i]=1
    ff=np.pad(keep,1); h,w=ff.shape; mask=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,mask,(0,0),2)
    keep[(ff[1:-1,1:-1]!=2)]=1
    alpha=cv2.GaussianBlur(keep.astype(np.float32),(0,0),1.1)
    band=cv2.dilate(keep,np.ones((91,91),np.uint8)).astype(np.float32)
    sh=np.clip((-dL-6)/40.0,0,1)*shadow*band; sh=cv2.GaussianBlur(sh.astype(np.float32),(0,0),6)*(1-alpha)
    al=alpha[...,None]; col=np.where(al>0.03,(a-(1-al)*bg)/np.maximum(al,0.03),a); col=np.clip(col,0,255)
    return col, alpha, sh

def matte_gc(rgb, init='mask', bg_mode='poly', thr=(7,9), grow=31):
    col0,alpha0,sh0=matte(rgb,bg_mode=bg_mode,thr=thr)
    H,W,_=rgb.shape; bgr=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)
    rough=(alpha0>0.5).astype(np.uint8)
    n,lab_,stats,_=cv2.connectedComponentsWithStats(rough,8)
    if n>1:
        amax=stats[1:,cv2.CC_STAT_AREA].max(); rough=np.isin(lab_,[i for i in range(1,n) if stats[i,cv2.CC_STAT_AREA]>=0.05*amax]).astype(np.uint8)
    cv2.setRNGSeed(7); bgd=np.zeros((1,65),np.float64); fgd=np.zeros((1,65),np.float64)
    if init=='rect':
        ys,xs=np.where(rough>0); pad=int(0.10*max(xs.max()-xs.min(),ys.max()-ys.min()))
        x0,y0,x1,y1=max(1,xs.min()-pad),max(1,ys.min()-pad),min(W-2,xs.max()+pad),min(H-2,ys.max()+pad)
        mask=np.zeros((H,W),np.uint8); cv2.grabCut(bgr,mask,(x0,y0,x1-x0,y1-y0),bgd,fgd,6,cv2.GC_INIT_WITH_RECT)
    else:
        core=cv2.erode(rough,np.ones((25,25),np.uint8)); near=cv2.dilate(rough,np.ones((21,21),np.uint8)); far=cv2.dilate(rough,np.ones((71,71),np.uint8))
        mask=np.full((H,W),cv2.GC_BGD,np.uint8); mask[far==1]=cv2.GC_PR_BGD; mask[near==1]=cv2.GC_PR_FGD; mask[core==1]=cv2.GC_FGD
        cv2.grabCut(bgr,mask,None,bgd,fgd,6,cv2.GC_INIT_WITH_MASK)
    m=((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD)).astype(np.uint8)
    if grow: m=m*cv2.dilate(rough,np.ones((grow,grow),np.uint8))   # GrabCut ne peut qu'affiner le masque grossier, pas s'en éloigner
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((5,5),np.uint8)); m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
    n,lab_,stats,_=cv2.connectedComponentsWithStats(m,8); keep=np.zeros_like(m)
    if n>1:
        amax=stats[1:,cv2.CC_STAT_AREA].max()
        for i in range(1,n):
            if stats[i,cv2.CC_STAT_AREA]>=0.05*amax: keep[lab_==i]=1
    ff=np.pad(keep,1); h,w=ff.shape; mk=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,mk,(0,0),2); keep[(ff[1:-1,1:-1]!=2)]=1
    alpha=cv2.GaussianBlur(keep.astype(np.float32),(0,0),1.2)
    a=rgb.astype(np.float32)
    inv=(1-keep).astype(np.float32); num=cv2.blur(a*inv[...,None],(41,41)); den=cv2.blur(inv,(41,41))[...,None]+1e-3; bg=num/den
    al=alpha[...,None]; col=np.where(al>0.03,(a-(1-al)*bg)/np.maximum(al,0.03),a); col=np.clip(col,0,255)
    sh=sh0*(1-alpha)
    return col,alpha,sh

def compose(rgb, W, H, width_frac=0.78, y_shift=0.04, method='interp'):
    col,alpha,sh=matte_gc(rgb,'rect','rows') if method=='gc_rect_r' else matte_gc(rgb,'rect','interp') if method=='gc_rect_i' else matte_gc(rgb,'rect','poly',thr=(6,6),grow=0) if method=='gc_rect' else matte_gc(rgb,'mask','poly') if method=='gc_mask' else matte(rgb,'interp')
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
    METHOD={'neck-01':'gc_rect_r','cover-neck':'gc_rect_r','family-set':'gc_rect_r','for-two':'gc_rect_r','neck-01-cover-set':'gc_rect_r','sleep-set':'gc_rect_r','side-sleeper-set':'gc_rect_r','side-01':'gc_rect','cover-side':'gc_rect','lounge-01':'gc_rect_i','evening-set':'gc_rect_i'}
    SKIP_FILES={'somnila_sleep-set_packshot-black-2_1x1_v1.jpg','somnila_sleep-set_packshot-blue-3_1x1_v1.jpg','somnila_side-sleeper-set_packshot-night-2_1x1_v1.jpg','somnila_side-01_packshot-dark-grey-3_1x1_v1.jpg','somnila_contour-01_packshot-stone-9_1x1_v1.jpg','somnila_body-01_packshot-ice-5_1x1_v1.jpg'}
    SKIP_HANDLES={'body-01','cover-body','mask-01','quiet-01','quiet-night','throw-01'}
    done=[]
    for r in rows:
        if r['usage']!='packshot' or r['handle'] in SKIP_HANDLES or r['file'] in SKIP_FILES: continue
        if only and r['handle'] not in only: continue
        f=r['file']; v2=f.replace('_v1.jpg','_v2.jpg')
        path=f'{SRC}/{v2}' if os.path.exists(f'{SRC}/{v2}') else f'{SRC}/{f}'
        if not os.path.exists(path): print('absent',path); continue
        rgb=np.array(Image.open(path).convert('RGB'))
        base=os.path.basename(path).replace('.jpg','').replace('_1x1','').replace('_4x5','')
        for tag,(W,H) in {'1x1':(1200,1200),'4x5':(1200,1500)}.items():
            out=compose(rgb,W,H,method=METHOD.get(r['handle'],'interp'))
            if out is None: print('échec matte',path); break
            Image.fromarray(out).save(f'{OUT}/{base}_sky_{tag}.jpg',quality=90,subsampling=0)
        done.append(base)
    print(len(done),'packshots composés')
