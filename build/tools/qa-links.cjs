const BASE='https://liyan.shop'; const THEME='157447585949'; const PW=process.env.PW; const jar={};
const UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36';
function ch(){return Object.entries(jar).map(([k,v])=>`${k}=${v}`).join('; ');}
function sc(r){const s=r.headers.getSetCookie?r.headers.getSetCookie():[]; for(const line of s){const p=line.split(';')[0]; const i=p.indexOf('='); if(i>0) jar[p.slice(0,i).trim()]=p.slice(i+1).trim();}}
async function get(path,o={}){const r=await fetch(BASE+path,{method:o.method||'GET',headers:{'user-agent':UA,'cookie':ch(),...(o.headers||{})},body:o.body,redirect:'manual'}); sc(r); return r;}
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
  await get('/password'); await get('/password',{method:'POST',headers:{'content-type':'application/x-www-form-urlencoded'},body:new URLSearchParams({form_type:'storefront_password',utf8:'✓',password:PW}).toString()});
  let r=await get('/?preview_theme_id='+THEME); let h=0; while([301,302].includes(r.status)&&h++<4){const l=new URL(r.headers.get('location'),BASE); r=await get(l.pathname+l.search);}
  const links=JSON.parse(require('fs').readFileSync('preview/qa-report.json')).links;
  for(const l of links){ await sleep(900); let r=await get(l); let hops=0; let chain=[l];
    while([301,302,303,307,308].includes(r.status)&&hops++<3){const loc=new URL(r.headers.get('location'),BASE); chain.push(loc.pathname); r=await get(loc.pathname+loc.search); await sleep(300);}
    console.log(r.status, chain.join(' -> ')); }
})();
