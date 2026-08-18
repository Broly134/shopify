# Économie unitaire & modèle financier — marque de montres DTC, marché US, 2026

**Convention de lecture :** `[S]` = chiffre sourcé (lien en fin de document) · `[E]` = estimation raisonnée de ma part, à valider · `[C]` = calcul dérivé.

---

## 0. Le fait structurel n°1 : le dropshipping colis-par-colis depuis la Chine est cassé en 2026

Avant toute autre chose, il faut intégrer ça, parce que ça invalide 90 % des tutos "watch dropshipping" que tu trouveras :

- La franchise de minimis à 800 $ a pris fin pour la Chine le **2 mai 2025**, puis pour **tous les pays le 29 août 2025** `[S]`. 2026 est la première année complète où **chaque colis, quelle que soit sa valeur, passe en dédouanement formel et paie des droits** `[S]`.
- Conséquence : chaque colis individuel expédié de Chine vers un client US supporte non seulement les droits de douane, mais aussi des **frais de courtage / handling transporteur de 15 à 25 $ par colis** `[S]`.
- Les montres relèvent du **chapitre 91 du HTS** avec des droits *composés* (ex. 9102.21.25 = 0,75 $/montre + 6 % sur le boîtier + 2,8 % sur le bracelet), auxquels s'ajoute la Section 301 (7,5 % liste 4A ou 25 % listes 1-3 selon la ligne tarifaire) `[S]`. Les trackers spécialisés donnent un total effectif de **~17,5 % à ~26 % pour une montre mécanique chinoise** `[S]`. Le contexte macro a bougé vite : les tarifs IEEPA ont été invalidés par la Cour suprême en février 2026 et la surtaxe Section 122 a expiré le 24 juillet 2026, mais la Section 301 reste pleinement en vigueur `[S]`.
- Je modélise **22 % de droits sur la valeur produit** `[E]`, mais **fais valider ta ligne HTS 10 chiffres par un courtier en douane** avant de commander : l'écart 7,5 % vs 25 % change ta marge de 10 points.

**Impact chiffré** de ce seul point (montre à 189 $, COGS 62 $) :

| Modèle logistique | Contribution avant pub | Marge de contribution | ROAS break-even |
|---|---:|---:|---:|
| Dropship pur (colis Chine → client, courtage 18 $) | **61,66 $** | 32,6 % | **3,07x** |
| Import groupé + 3PL US (courtage amorti) | **78,98 $** | 41,8 % | **2,39x** |

Passer d'un modèle à l'autre te rend **17 $ par commande**, soit +28 % de contribution, sans toucher au prix ni à la pub. C'est le levier le plus rentable de tout ce document.

---

## 1. Structure de coût par unité

Trois configurations produit, en dropshipping/import Chine.

| Poste | Quartz Miyota (entrée) | NH35 automatique (cœur de gamme) | NH35 + saphir/céramique (premium) |
|---|---:|---:|---:|
| COGS produit usine `[S/E]` | 22–32 $ | 55–75 $ | 95–130 $ |
| Droits de douane @22 % `[E]` | 5,72 $ | 13,64 $ | 23,10 $ |
| Packaging (boîte, carte garantie, insert) `[E]` | 3–5 $ | 6–9 $ | 11–16 $ |
| **Coût rendu (landed)** | **~35,72 $** | **~82,64 $** | **~141,10 $** |
| Fulfillment 3PL US (pick&pack ~3,50 $ + port assuré) `[E]` | 11,00 $ | 12,00 $ | 14,00 $ |
| Frais paiement (2,4 % + 0,30 $ Advanced, blendé 2,7 % + 0,32 $) `[S/E]` | 2,72 $ | 5,42 $ | 9,74 $ |
| Provision retours `[E]` | 3,94 $ (12 %) | 4,60 $ (10 %) | 5,76 $ (9 %) |
| Provision litiges/chargebacks `[E]` | 1,68 $ (1,2 %) | 2,87 $ (1,0 %) | 4,04 $ (0,8 %) |
| SAV (0,2–0,3 ticket/cmd) `[E]` | 2,00 $ | 2,50 $ | 3,50 $ |

**Notes sur les provisions (les postes que tout le monde oublie) :**

- **Retours** : moyenne e-commerce 2026 = **19–20,8 %**, DTC ≈ 14 % `[S]`. Je descends à 9–12 % pour la montre : pas de problème de taille, mais motif dominant = "moins impressionnant qu'en photo". Coût d'un retour ≠ le prix : port aller + port retour (~12 $) + décote produit (~20 % du landed) + frais de paiement non restitués.
- **Litiges** : moyenne retail = **0,47–0,95 %** ; le dropshipping monte plus haut à cause des délais `[S]`. **Seuil critique : au-delà de ~0,7 %, Stripe/Shopify Payments peut geler ou mettre sous revue ton compte** `[S]`. À 0 commande d'historique, tu es en zone de surveillance dès la première dizaine de litiges. C'est le risque n°1 de mort subite d'une boutique high-ticket.
- **Frais paiement** : tu as écrit ~2,9 % + 30 c. En **plan Advanced tu es à 2,4 % + 0,30 $** en ligne `[S]` — 0,5 point que tu ne comptes pas. Mais voir §6, l'Advanced est probablement une fuite de trésorerie à ce stade.

---

## 2. CAC réaliste par canal, catégorie montre/accessoire mode, 2026

### Benchmarks d'entrée

| Métrique | Meta | TikTok Ads | Google Shopping |
|---|---|---|---|
| CPM `[S]` | 9,23 $ (apparel) / 9,36 $ (bijoux-accessoires) / 14,19–14,91 $ (moyenne plateforme) | 9,16 $ moyenne / **13,26 $ médiane e-com conversion** (+16 % YoY) | n/a (CPC) |
| CPC `[S]` | 0,45 $ (apparel) → 0,78 $ (moy.) → 1,72 $ (tous secteurs) | 0,79 $ (retail) / 1,02 $ (in-feed cross-industrie) | 0,66 $ (Shopping global) ; 4,31 $ (search apparel/bijoux) |
| CTR `[S]` | 2,19 % moyenne / **2,84 % mode-habillement** | 0,84 % e-com | — |
| CVR site `[S]` | 1,60 % moyenne plateforme | 0,46 % e-com (jusqu'à 2–3 % si bien optimisé) | 1,91 % |
| CPA médian e-com `[S]` | **38,19 $** (39 $ ; apparel 36,76 $) | — | — |
| ROAS de référence `[S]` | 1,86 médiane e-com | — | 2,5x bijoux-accessoires |

⚠️ Le CPA médian de 38 $ est calculé sur *tous* les prix, incluant du produit à 30 $. Pour une montre à 189–349 $ avec zéro preuve sociale, ton CPA réel sera **structurellement plus haut**.

### CAC implicite par scénario `[C]`

| Canal / qualité d'exécution | CPM | CTR | CVR | CPC | **CPA** |
|---|---:|---:|---:|---:|---:|
| **Meta** — créa qui marche vraiment | 10 $ | 2,80 % | 1,80 % | 0,36 $ | **~20 $** |
| **Meta** — cas central réaliste mois 2-4 | 14 $ | 1,90 % | 1,20 % | 0,74 $ | **~61 $** |
| **Meta** — lancement à froid, créa moyenne | 19 $ | 1,10 % | 0,70 % | 1,73 $ | **~247 $** |
| **TikTok Ads** — bon | 9 $ | 1,10 % | 1,20 % | 0,82 $ | **~68 $** |
| **TikTok Ads** — cas central | 13 $ | 0,80 % | 0,70 % | 1,62 $ | **~232 $** |
| **TikTok Ads** — mauvais | 17 $ | 0,50 % | 0,40 % | 3,40 $ | **~850 $** |
| **Google Shopping** non-marque (bas) | — | — | 2,00 % | 0,80 $ | **~40 $** |
| **Google Shopping** non-marque (haut) | — | — | 1,10 % | 1,80 $ | **~164 $** |
| **Google** requêtes marque (retarget de ton organique) | — | — | 11,0 % | 0,55 $ | **~5 $** |

### Lecture par canal

**Meta Ads — ton canal principal.** Fourchette de travail : **45–140 $ de CAC**, avec un plancher structurel autour de **35–45 $** que tu n'iras pratiquement jamais casser dans cette catégorie. Point critique : Meta a besoin de ~50 conversions/semaine/ad set pour sortir de la phase d'apprentissage. À 61 $ de CPA ça fait **3 050 $/semaine** `[C]` — impossible pour toi. **Solution obligatoire : optimiser sur Add-to-Cart** (~12 $/ATC) au lieu de Purchase → 600 $/semaine, soit **~2 580 $/mois** `[C]` pour qu'un ad set apprenne correctement. C'est ton vrai minimum de budget média.

**TikTok Ads — piège pour le high-ticket.** CVR e-commerce de 0,46 % `[S]` : TikTok convertit l'impulsion sous ~70 $, pas la décision réfléchie à 200 $+. À utiliser pour la **découverte + retargeting Meta/Google**, pas pour la conversion directe froide.

**TikTok organique / UGC — le seul canal où ton positionnement "fuck 9-5" a un avantage réel.** Le contenu anti-corporate performe organiquement bien mieux qu'en paid. Coût réel : ce n'est pas gratuit. Soit tu produis 3–5 vidéos/jour toi-même (≈ 25–30 h/semaine), soit tu achètes de l'UGC à **~195 $/vidéo en moyenne 2026** `[S]` (fourchette 150–500 $ TikTok). 20–40 vidéos/mois = **3 900–7 800 $/mois** `[C]`. Rendement : ultra-asymétrique. Une vidéo à 500 k vues → 1 000–3 000 clics → 1,5 % CVR → **15–45 commandes**, soit un CAC effectif de 5–15 $. Mais **le mois médian d'un débutant produit 0 vidéo à 500 k vues**. Ne construis pas ton P&L dessus ; construis-le sur Meta et traite l'organique comme un bonus qui, quand il tape, baisse ton CAC blended de 30–50 %.

**Influenceurs.** Nano (<10 k) : 75–250 $ ou gifting. Micro (10–100 k) : **200–2 500 $/post** `[S]`. Le whitelisting (diffuser des ads depuis leur compte) ajoute **+50 à +100 %** `[S]` — mais c'est souvent le meilleur ROI car ça résout ton déficit de crédibilité. Modèle gifting réaliste pour toi : montre à ~95 $ rendu + port, contre 1 post + droits d'usage perpétuels. Sur 10 envois : 3–4 postent, génèrent 0–8 ventes chacun. **CAC effectif : 40–200 $, variance énorme.** Considère ça comme un budget *contenu + preuve sociale*, pas comme un canal d'acquisition.

**Google Shopping.** En non-marque, tu te bats sur "automatic dive watch" contre Seiko, Orient, Christopher Ward, 200 microbrands installées : CPA 40–164 $ avec un taux de rebond violent. **Le vrai jeu Google, c'est la défense de marque : 5 $ de CAC** `[C]` sur les gens qui ont vu ton TikTok et tapent ton nom. Budget minuscule, ROAS énorme. À activer dès le jour 1, mais ne compte pas dessus pour scaler.

---

## 3. Trois scénarios de pricing complets

Hypothèses communes : import groupé + 3PL US, 2,7 % + 0,32 $ de frais paiement, provisions du §1.

### Scénario BAS — 89 $ (quartz Miyota, homage SKX)

| Poste | Montant | % du prix |
|---|---:|---:|
| Prix de vente | 89,00 $ | 100 % |
| Coût rendu (COGS 26 + douane 5,72 + packaging 4) | −35,72 $ | 40,1 % |
| Fulfillment | −11,00 $ | 12,4 % |
| Frais paiement | −2,72 $ | 3,1 % |
| Retours (12 %) | −3,94 $ | 4,4 % |
| Litiges (1,2 %) | −1,68 $ | 1,9 % |
| SAV | −2,00 $ | 2,2 % |
| **Contribution avant pub** | **31,94 $** | **35,9 %** |
| **ROAS break-even** | **2,79x** | |
| CAC max absolu (profit = 0) | 31,94 $ | |
| **CAC cible (60 % de la contribution)** | **19,16 $** | |
| Profit net/commande à ce CAC | 12,77 $ | |
| ROAS requis à CAC cible | **4,64x** | |

**Verdict : non viable en paid.** Un CAC de 19 $ n'existe pas dans cette catégorie en 2026 (plancher réel 35–45 $). Ce scénario perd **3 à 13 $ par commande acquise en publicité**. Il ne fonctionne qu'en 100 % organique, et même là le ROI horaire est mauvais.

### Scénario MÉDIAN — 189 $ (NH35 automatique, saphir, 316L)

| Poste | Montant | % du prix |
|---|---:|---:|
| Prix de vente | 189,00 $ | 100 % |
| Coût rendu (COGS 62 + douane 13,64 + packaging 7) | −82,64 $ | 43,7 % |
| Fulfillment | −12,00 $ | 6,3 % |
| Frais paiement | −5,42 $ | 2,9 % |
| Retours (10 %) | −4,60 $ | 2,4 % |
| Litiges (1,0 %) | −2,87 $ | 1,5 % |
| SAV | −2,50 $ | 1,3 % |
| **Contribution avant pub** | **78,98 $** | **41,8 %** |
| **ROAS break-even** | **2,39x** | |
| CAC max absolu | 78,98 $ | |
| **CAC cible (60 %)** | **47,39 $** | |
| Profit net/commande | 31,59 $ | |
| ROAS requis à CAC cible | **3,99x** | |

**Verdict : viable, mais serré.** Ton CAC cible de 47 $ tombe pile dans la fourchette Meta réaliste (45–70 $). Ça veut dire : tu es rentable *si et seulement si* tes créas sont au-dessus de la moyenne. À 61 $ de CAC (cas central), tu fais 18 $ de profit/commande — ça marche, mais tu n'as aucune marge d'erreur avant les frais fixes.

### Scénario PREMIUM — 349 $ (NH35/NH36, saphir, lunette céramique, cadran custom, coffret)

| Poste | Montant | % du prix |
|---|---:|---:|
| Prix de vente | 349,00 $ | 100 % |
| Coût rendu (COGS 105 + douane 23,10 + packaging 13) | −141,10 $ | 40,4 % |
| Fulfillment | −14,00 $ | 4,0 % |
| Frais paiement | −9,74 $ | 2,8 % |
| Retours (9 %) | −5,76 $ | 1,7 % |
| Litiges (0,8 %) | −4,04 $ | 1,2 % |
| SAV | −3,50 $ | 1,0 % |
| **Contribution avant pub** | **170,86 $** | **49,0 %** |
| **ROAS break-even** | **2,04x** | |
| CAC max absolu | 170,86 $ | |
| **CAC cible (60 %)** | **102,52 $** | |
| Profit net/commande | 68,34 $ | |
| ROAS requis à CAC cible | **3,40x** | |

**Verdict : le meilleur profil mathématique, le plus dur à exécuter.** 102 $ de CAC te donne une énorme latitude — tu peux te permettre du mauvais Meta, du TikTok, des influenceurs à 500 $. **Mais** : à 349 $, une marque inconnue avec 0 avis, un délai de livraison flou et aucune infrastructure SAV voit son CVR s'effondrer vers 0,4–0,7 % `[E]`. Et le CVR est le seul levier qui compte : à 0,4 % de CVR, ton CPA passe à 185 $ et tu ne gagnes plus rien. C'est un pari sur ta capacité à construire de la crédibilité (photo, garantie, retours 30 j, avis vidéo), pas sur ta capacité à acheter du trafic.

### Break-even en commandes/mois

Profit net par commande **après** CAC cible (60 %), contre trois niveaux de frais fixes mensuels.

| Frais fixes/mois | BAS (12,77 $/cmd) | MÉDIAN (31,59 $/cmd) | PREMIUM (68,34 $/cmd) |
|---|---:|---:|---:|
| **700 $** (Shopify Basic + apps + domaine) | 55 cmd | **22 cmd** | **10 cmd** |
| **1 200 $** (+ Klaviyo, thème, outils) | 94 cmd | **38 cmd** | **18 cmd** |
| **2 000 $** (Shopify Advanced + stack complet + VA) | 157 cmd | **63 cmd** | **29 cmd** |

À retenir : sur le scénario MÉDIAN avec un stack raisonnable, **il te faut ~38 commandes/mois pour passer au vert**, soit ~1,3/jour et ~7 200 $ de CA mensuel. C'est atteignable. Sur le scénario BAS, il t'en faut 94 — soit 3,1/jour — pour gagner zéro. C'est la démonstration chiffrée que le prix bas te condamne.

---

## 4. AOV : les leviers, chiffrés

Appliqués au scénario MÉDIAN (189 $, contribution 78,98 $). Taux de prise `[E]`, basés sur des ordres de grandeur usuels en post-purchase upsell.

| Levier | Prix | Coût réel | Taux de prise | Impact AOV | Impact contribution |
|---|---:|---:|---:|---:|---:|
| Bracelet supplémentaire (NATO / acier / cuir) | 34 $ | 5 $ | 28 % | **+9,52 $** | **+7,86 $** |
| Coffret cadeau / watch roll | 32 $ | 8 $ | 15 % | **+4,80 $** | **+3,47 $** |
| Garantie étendue 24 mois | 24 $ | 2,80 $ | 20 % | **+4,80 $** | **+4,11 $** |
| 2ᵉ montre à −15 % (offre panier) | 160 $ | 85,60 $ | 4 % | **+6,40 $** | **+2,80 $** |
| **TOTAL** | | | | **+25,52 $** | **+18,25 $** |

**Résultat : AOV 189 $ → 214,52 $ (+13,5 %), contribution 78,98 $ → 97,23 $ (+23,1 %)** `[C]`

C'est le point le plus important du document après la douane. **+13,5 % d'AOV te donne +23 % de contribution** — parce que les add-ons ne portent ni CAC, ni fulfillment marginal, ni presque de frais de paiement. Concrètement :

- ROAS break-even : **2,39x → 2,21x**
- CAC cible : **47,39 $ → 58,34 $**

Ces 11 $ de CAC supplémentaire, c'est exactement l'écart entre "Meta ne marche pas pour moi" et "Meta marche". **Ce n'est pas de l'optimisation cosmétique, c'est ce qui rend le canal payant viable.**

**Priorité d'implémentation :**
1. **Garantie étendue** — meilleur ratio effort/marge de tous. 24 $ vendus contre ~2,80 $ de coût réel espéré (si ~4 % de casse en année 2 × ~70 $ de remplacement rendu `[E]`). Marge ~88 %. Et ça résout ton problème de crédibilité en même temps. Fais-le en premier.
2. **Bracelet** — plus gros contributeur brut (+7,86 $) et parfaitement aligné avec la catégorie : dans l'univers Seiko/homage, changer de bracelet fait partie de la culture. Vends-le comme "quick-release, 20 secondes, change ta montre sans outil".
3. **Coffret** — pousse-le en Q4 uniquement, où le taux de prise monte à 30–40 %.
4. **2ᵉ montre** — faible taux de prise mais gratuit à installer.

**Un point à ne PAS faire :** ne justifie pas un CAC supérieur à ta contribution par la LTV. La montre est une catégorie à **faible réachat : ~8–15 % à 12 mois** pour une microbrand `[E]`. Les bracelets/accessoires peuvent monter ça à 15–22 %, ce qui ajoute ~10–15 % de valeur client, pas 2x. **Ton modèle doit être rentable dès la première commande.**

---

## 5. Le vrai piège : le seuil de prix sous lequel le paid devient impossible

### Le mécanisme

**Le CAC ne descend pas quand ton prix descend.** Tu achètes des impressions à 9–15 $ le mille, pas un pourcentage de ton prix. Vendre une montre à 69 $ te coûte quasiment autant en acquisition que la vendre à 249 $ — au mieux 25–35 % moins cher grâce à un meilleur CVR, jamais 70 % moins cher. Ta contribution, elle, s'effondre proportionnellement.

Cela crée un **plancher absolu de CAC de ~35–45 $** dans cette catégorie en 2026. Ta contribution par commande doit dépasser ce plancher, sinon aucun montant de travail créatif ne te sauve.

### Les seuils chiffrés `[C]`

Prix de vente minimum pour que la contribution atteigne le CAC plancher :

| Configuration produit | CAC plancher 35 $ | CAC plancher 45 $ (réaliste) | CAC plancher 60 $ (cas central Meta) |
|---|---:|---:|---:|
| Quartz (COGS 26 $) | 92 $ | **102 $** | 118 $ |
| NH35 automatique (COGS 62 $) | 144 $ | **154 $** | 170 $ |
| Premium (COGS 105 $) | 209 $ | **219 $** | 235 $ |

⚠️ Ces prix sont ceux où tu **fais exactement zéro**. Pour construire une entreprise (payer tes frais fixes, absorber une mauvaise semaine, réinvestir), ajoute **+30 à +40 %**.

### Les réponses directes

- **Seuil de mort mathématique : 120 $.** En dessous, avec n'importe quelle configuration produit crédible, une montre seule ne peut pas financer son acquisition payante. Point final.
- **Seuil pratique : 180 $.** Entre 120 et 180 $, tu es dans une zone qui ne fonctionne qu'avec des leviers AOV agressifs (§4) *et* un flux organique significatif. C'est jouable mais fragile.
- **Le mur de confiance : ~350–400 $.** Au-dessus, le problème s'inverse. Ta contribution est grasse (170 $+) mais ton CVR s'effondre de façon **non linéaire et imprévisible** : une marque sans historique, sans avis, sans SAV visible, avec des délais dropshipping, ne convertit pas à 400 $ à froid. Tu peux brûler 250 $ de budget média par commande que tu n'obtiens pas.
- **Le corridor viable : 190–320 $. Point optimal : 199–249 $.**

### Le piège dans lequel tombent 90 % des gens

La règle "j'achète 30 $, je vends 90 $, ×3 c'est bon" **était** une règle valable en 2019. Elle est morte en 2026 pour trois raisons cumulées :
1. **De minimis supprimé** → +22 à 30 % de coût rendu, plus 15–25 $ de courtage si tu expédies colis par colis `[S]`
2. **CPM en hausse dans absolument tous les secteurs en 2025, sans exception, tendance qui continue en 2026** `[S]` ; TikTok +12,3 % YoY `[S]`
3. **Livraison gratuite devenue obligatoire** → 11–14 $ réels que tu absorbes

Un ×3 sur une montre à 90 $ te laisse ~32 $ de contribution contre un plancher CAC de 40 $. **Tu perds de l'argent sur chaque vente, et plus tu scales, plus tu perds.** C'est le mode d'échec le plus courant et le plus rapide.

**Corollaire stratégique :** ton positionnement "new rich / fuck 9-5" te pousse *naturellement* vers le haut de gamme. C'est une chance : le brief et les maths pointent dans la même direction. Une montre "fuck 9-5" à 89 $ est un contresens marketing *et* un suicide financier. À 219 $, elle est cohérente sur les deux plans.

---

## 6. Budget de lancement minimum réaliste

### Correction préalable : ton plan Shopify te coûte de l'argent

Tu es en **Advanced à 399 $/mois** `[S]` avec 0 commande. L'avantage tarifaire de l'Advanced (2,4 % vs 2,9 % en Basic) ne compense son surcoût qu'à partir de `[C]` :

- **Advanced vs Basic (39 $) : 72 000 $ de GMV/mois**
- **Advanced vs Grow (105 $) : 98 000 $ de GMV/mois**

Tu es à ~2 % de ce volume. **Repasse en Basic immédiatement : 360 $/mois économisés, soit 1 080 $ sur 3 mois** — c'est-à-dire 5 vidéos UGC, ou 12 jours de test créatif. Repasse en Advanced quand tu franchis 70 k$/mois.

### Trois paliers

| Poste | Palier 0 — Organique | Palier 1 — Paid, dropship pur | Palier 2 — Paid + stock léger *(recommandé)* |
|---|---:|---:|---:|
| Échantillons (3–5 modèles : produit + express + douane + courtage) | 500 $ | 700 $ | 700 $ |
| Contenu (photo + UGC @ ~195 $/vidéo `[S]`) | 900 $ (DIY + 4 UGC) | 1 800 $ (8 UGC) | 2 400 $ (10 UGC + shoot) | 
| Store & tech (thème, apps, domaine, Shopify Basic) | 500 $ | 650 $ | 800 $ |
| Légal/ops (LLC, EIN, CGV, politique retours) | 250 $ | 350 $ | 450 $ |
| Stock initial (50 u × 62 $ + fret groupé/douane 1 100 $) | — | — | 4 200 $ |
| Budget média test | 600 $ (retarget seul) | 4 500 $ | 6 000 $ (2 cycles) |
| Réserve remboursements/litiges/casse | — | 600 $ | 1 000 $ |
| **TOTAL** | **~2 750 $** | **~8 600 $** | **~15 550 $** |

### Ce que chaque palier achète réellement

- **Palier 0 (~2 750 $)** : tu testes le positionnement sans risque financier majeur. Probabilité de construire quelque chose de significatif : faible (~10–15 % `[E]`), parce que tout repose sur ta capacité à faire du volume organique. Mais le coût de l'échec est faible et tu apprends. **C'est le bon palier si tu n'as jamais vendu en ligne.**
- **Palier 1 (~8 600 $)** : tu peux tester du paid, mais l'économie unitaire du dropship pur (contribution 61,66 $, ROAS break-even 3,07x) est trop serrée pour absorber une phase d'apprentissage ratée. **Je ne recommande pas ce palier** : c'est le pire ratio risque/rendement des trois.
- **Palier 2 (~15 550 $)** : le seul qui te donne une **vraie** chance. Import groupé → contribution 78,98 $ au lieu de 61,66 $, expédition US en 2–4 jours au lieu de 15–25 → CVR meilleur, litiges divisés par 2, avis positifs possibles. Et 6 000 $ de média = deux cycles complets de test à ~100 $/jour, ce qui permet à un ad set d'apprendre correctement (~2 580 $/mois en optimisation ATC `[C]`).

### Le budget média : pourquoi 3 000 $ n'est pas négociable

Un test de créatives sérieux, c'est **75–100 $/jour pendant 30 jours (2 250–3 000 $) par angle testé**, avec 4–6 créatives. Un seul cycle ne te dit presque rien (trop de bruit statistique à 1,2 % de CVR). **Il en faut deux : ~6 000 $.**

En dessous de 50 $/jour, tu n'as ni signal exploitable ni sortie de phase d'apprentissage — tu paies juste pour du bruit. **Si tu ne peux pas mettre 3 000 $ sur le média, ne fais pas de paid du tout** : va en Palier 0 et construis en organique jusqu'à avoir 20–30 commandes qui financent le premier test.

### Runway

Ajoute **3 à 6 mois sans profit** au budget ci-dessus. Le cycle réaliste : mois 1 = tests qui perdent de l'argent, mois 2 = première créative gagnante identifiée, mois 3–4 = scale prudent au break-even, mois 5–6 = première rentabilité. Prévois **~600–900 $/mois de frais fixes** sur cette période, en plus du budget de lancement.

---

## 7. Les 5 décisions qui découlent de tout ça

1. **Prix cible : 219 $** sur le produit héros (NH35, saphir, quick-release). Pas 89 $, pas 399 $.
2. **Repasse en Shopify Basic aujourd'hui.** 360 $/mois récupérés, 0 inconvénient à ton volume actuel.
3. **N'expédie jamais colis-par-colis depuis la Chine.** Fais valider ta ligne HTS par un courtier, importe 50 unités en groupé, stocke chez un 3PL US. +28 % de contribution, litiges divisés par deux.
4. **Installe la garantie étendue et le bracelet en upsell avant de dépenser 1 $ en pub.** +23 % de contribution, ce qui fait passer ton CAC cible de 47 $ à 58 $ — la différence entre un canal qui marche et un qui ne marche pas.
5. **Surveille ton taux de litiges comme un indicateur vital.** Au-delà de 0,7 %, le risque n'est pas une perte de marge : c'est le gel de tes fonds et la fermeture de ton compte de paiement.

---

## Sources

- [Facebook Ads Benchmarks 2026 — Influee](https://influee.co/blog/facebook-ads-benchmarks) · [Meta Ads Benchmarks eCommerce 2026 — 27five](https://27five.com/blog/meta-ads-benchmarks-ecommerce-2026/) · [Meta Ads Benchmarks Ecommerce 2026 — MHI Growth Engine](https://mhigrowthengine.com/blog/meta-ads-benchmarks-ecommerce-2026/) · [Meta Ads Benchmarks 2026 — Ryze](https://www.get-ryze.ai/blog/meta-ads-cost-benchmarks-by-industry-2026) · [Meta Ads Benchmarks — Skale Strategy](https://www.skalestrategy.com/blog/meta-ads-benchmarks-ecommerce-2026)
- [TikTok Ads Benchmarks 2026 — DigitalApplied](https://www.digitalapplied.com/blog/tiktok-ads-benchmarks-2026-cpc-cpm-cvr-industry) · [TikTok Ads Cost for Ecommerce 2026 — AI Advantage](https://aiadvantageagency.com/tiktok-ads-cost-for-ecommerce/) · [TikTok Ads Benchmarks — Lebesgue](https://lebesgue.io/tiktok-ads/tiktok-ads-benchmarks-for-ctr-cr-and-cpm)
- [Google Shopping Benchmarks 2026 — Foundry CRO](https://foundrycro.com/blog/google-shopping-benchmarks-by-category-2026/) · [Google Shopping Benchmarks — OwlClaw](https://owlclaw.com/benchmarks/google-shopping-benchmarks/) · [Apparel & Jewelry Google Ads CPC](https://ppcchief.com/google-ads-benchmarks/apparel-fashion)
- [Shopify Pricing 2026 — Style Factory](https://www.stylefactoryproductions.com/blog/shopify-fees) · [Shopify Fees 2026 — Qualimero](https://qualimero.com/en/blog/shopify-fees) · [Shopify Help Center — Pricing plans](https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/pricing-overview)
- [Jewelry E-commerce Benchmarks — Branvas](https://branvas.com/blogs/news/jewelry-ecommerce-benchmarks-conversion-rate-aov) · [Jewelry & Watches E-commerce Statistics 2026 — WisePIM](https://wisepim.com/ecommerce-industry-insights/jewelry) · [Ecommerce Conversion Rate Benchmarks 2026 — DTC Pages](https://www.dtcpages.com/blog/ecommerce-conversion-rate-benchmarks-2026)
- [Ecommerce after De Minimis Tariff Exemption — Practical Ecommerce](https://www.practicalecommerce.com/ecommerce-after-de-minimis-tariff-exemption) · [2026 Tariff Guide for E-Commerce — Northstar](https://nstarfinance.com/resources/ecommerce-tariff-guide-2026) · [$800 De Minimis Rule Ended 2026 — TariffsTool](https://www.tariffstool.com/guides/de-minimis-exemption-ended-2026) · [US Tariffs 2026: Section 301, IEEPA, 232 — Suaid Global](https://suaidglobal.com/insights/us-tariffs-2026-guide/) · [Section 301 Tariffs 2026 — Carra Globe](https://carraglobe.com/section-301-tariffs-2026/)
- [US Import Duty Rates for Clocks & Watches (HTS Ch. 91)](https://ustariffrates.com/chapter/watches) · [HTS Chapter 91 — USITC (PDF)](https://www.usitc.gov/publications/docs/tata/hts/bychapter/1000c91.pdf)
- [Ecommerce Return Rates 2026 — Richpanel](https://www.richpanel.com/learn/ecommerce-return-rates) · [Average Ecommerce Return Rate 2026 — Eightx](https://eightx.co/blog/average-ecommerce-return-rate) · [Dropshipping Chargebacks 2026 — ProductLair](https://productlair.com/blog/dropshipping-chargebacks)
- [UGC Creator Rates 2026 — JoinBrands](https://joinbrands.com/blog/ugc-creator-rates/) · [UGC Video Pricing 2026 — Influence4You](https://blogen.influence4you.com/ugc-video-pricing-in-2026-how-much-should-you-pay-content-creators/) · [Influencer Rates 2026 — Stan](https://stan.store/blog/influencer-rates/)
- [Shipping from China to USA 2026 — NextSmartShip](https://www.nextsmartship.com/blog/ship-from-china-to-us/) · [DDP Shipping Cost China–USA 2026 — Aideliv](https://aideliv.com/ddp-shipping-cost) · [NH35 Movement Watch Suppliers — Alibaba](https://www.alibaba.com/nh35-movement-watch-suppliers.html) · [Watches Dropshipping Suppliers — The Clever Business](https://thecleverbusiness.com/watches-dropshipping/)

**Fichier de calcul :** `/tmp/claude-0/-home-user-shopify/7fbeaac5-5ea4-59ab-832c-91e3bce92278/scratchpad/model.py` (script Python reproductible — modifie les hypothèses en haut pour re-simuler).