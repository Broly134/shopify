// QA : parcourt les pages du thème Somnila derrière le mot de passe, via fetch, et vérifie titres, meta, H1, erreurs Liquid, résidus français / marques tierces / chinois, liens internes.
const BASE='https://liyan.shop'; const THEME='157447585949'; const PW=process.env.PW;
const jar={}; const UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36';
function cookieHeader(){return Object.entries(jar).map(([k,v])=>`${k}=${v}`).join('; ');}
function storeCookies(r){const sc=r.headers.getSetCookie?r.headers.getSetCookie():[]; for(const line of sc){const pair=line.split(';')[0]; const i=pair.indexOf('='); if(i>0) jar[pair.slice(0,i).trim()]=pair.slice(i+1).trim();}}
async function get(path,opts={}){const r=await fetch(BASE+path,{method:opts.method||'GET',headers:{'user-agent':UA,'accept-language':'en-US,en;q=0.9','cookie':cookieHeader(),...(opts.headers||{})},body:opts.body,redirect:'manual'}); storeCookies(r); return r;}
(async()=>{
  await get('/password'); await get('/password',{method:'POST',headers:{'content-type':'application/x-www-form-urlencoded'},body:new URLSearchParams({form_type:'storefront_password',utf8:'✓',password:PW}).toString()});
  let r=await get('/?preview_theme_id='+THEME+'&_ab=0&_fd=0&_sc=1'); let hops=0; while([301,302,303].includes(r.status)&&hops++<4){const l=new URL(r.headers.get('location'),BASE); r=await get(l.pathname+l.search);}
  const products=['neck-01','contour-01','side-01','body-01','lounge-01','throw-01','mask-01','quiet-01','cover-neck','cover-contour','cover-side','cover-body','neck-01-cover-set','sleep-set','for-two','side-sleeper-set','contour-for-two','evening-set','family-set','quiet-night'];
  const urls=['/','/collections/memory-foam-pillows','/collections/sets','/collections/accessories','/collections/covers','/collections/shop-all','/collections','/pages/about','/pages/faq','/pages/contact','/pages/shipping-delivery','/pages/returns-warranty','/cart','/search?q=pillow','/blogs/notes','/this-page-does-not-exist','/policies/refund-policy','/policies/shipping-policy','/policies/terms-of-service','/policies/privacy-policy',...products.map(p=>'/products/'+p)];
  const FR=/\b(Ajouter au panier|Panier|Livraison|Rechercher|Accueil|Boutique|Voir tout|Découvrir|Nos produits|Se connecter|Politique|Conditions|Passer la commande|Sous-total|Quantité|Rupture|Épuisé|Vous|Votre|Nous)\b/;
  const BRANDS=/PORTANCE|LIYAN|Liyan|Derila|Cloudii|Snuggi|iMeBoBo|Pilloway/; const CJK=/[一-鿿]/;
  const links=new Set(); const out=[];
  for(const u of urls){
    let r=await get(u); let hops=0; let finalUrl=u;
    while([301,302,303,307,308].includes(r.status)&&hops++<4){const l=new URL(r.headers.get('location'),BASE); finalUrl=l.pathname+l.search; r=await get(finalUrl);}
    const html=await r.text();
    const text=html.replace(/<script[\s\S]*?<\/script>/g,'').replace(/<style[\s\S]*?<\/style>/g,'').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ');
    const title=(html.match(/<title>([^<]*)<\/title>/)||[])[1]||''; const desc=(html.match(/<meta name="description" content="([^"]*)"/)||[])[1]||'';
    const h1=[...html.matchAll(/<h1[^>]*>([\s\S]*?)<\/h1>/g)].map(m=>m[1].replace(/<[^>]+>/g,'').replace(/\s+/g,' ').trim());
    const liquid=(html.match(/Liquid error[^<]{0,120}/g)||[]).slice(0,3);
    const fr=(text.match(FR)||[]).slice(0,3); const brands=(text.match(BRANDS)||[]).slice(0,3); const cjk=CJK.test(text);
    const noimg=(html.match(/no-image|placeholder-svg|product-apparel/g)||[]).length;
    for(const m of html.matchAll(/href="(\/[^"#?][^"]*)"/g)){const h=m[1].split('?')[0]; if(!/\.(js|css|png|jpg|svg|ico|json|xml)$/.test(h)&&!h.startsWith('/cdn/')&&!h.startsWith('/password')) links.add(h);}
    out.push({u,status:r.status,finalUrl,title,desc:desc.slice(0,90),h1,liquid,fr,brands,cjk,noimg,bytes:html.length});
    console.log(r.status,u,'|',title.slice(0,60),'| h1:',JSON.stringify(h1).slice(0,70),'|',liquid.length?'LIQUID':'',fr.length?'FR:'+fr.join(','):'',brands.length?'BRAND:'+brands.join(','):'',cjk?'CJK':'',noimg?'placeholder:'+noimg:'');
  }
  // liens internes : statut
  const bad=[]; const all=[...links].filter(l=>!urls.includes(l)).sort();
  for(const l of all){let r=await get(l); let hops=0; while([301,302,303,307,308].includes(r.status)&&hops++<3){const loc=new URL(r.headers.get('location'),BASE); r=await get(loc.pathname+loc.search);} if(r.status>=400) bad.push(l+' -> '+r.status);}
  console.log('liens internes testés:',all.length,'cassés:',bad.length); bad.forEach(b=>console.log('  ',b));
  require('fs').writeFileSync('preview/qa-report.json',JSON.stringify({pages:out,links:all,bad},null,1));
})();
