# Phase 3 — Produits Shopify en brouillon

Date : 10 septembre 2026. Boutique `07beme-9h.myshopify.com`. Aucun produit
PORTANCE touché, aucun thème publié, rien supprimé, aucun email envoyé.

## 1. Fait

**20 produits créés en brouillon** (`status: DRAFT`, `publishedAt: null`,
vérifié après création) : 12 produits seuls et 8 packs, sous la nomenclature
du brand book § 7. 138 variantes, 58 images, toutes en état `READY`.

| Handle | Titre | Prix EUR | Variantes | Images | Collection |
|---|---|---|---|---|---|
| `neck-01` | Neck 01 — Memory-foam pillow | 69,90 | 4 coloris | 4 | Pillows |
| `contour-01` | Contour 01 — Contoured comfort pillow | 59,90 | 5 | 10 | Pillows |
| `side-01` | Side 01 — Side-sleeper pillow | 54,90 | 3 | 4 | Pillows |
| `body-01` | Body 01 — S-shaped body pillow | 69,90 | 8 | 8 | Pillows |
| `lounge-01` | Lounge 01 — Reading pillow | 54,90 | 7 | 2 | Pillows |
| `throw-01` | Throw 01 — Bubble-textured throw | 59,90 | 10 | **0** | Accessories |
| `mask-01` | Mask 01 — Contoured sleep mask | 19,90 | 7 | 6 | Accessories |
| `quiet-01` | Quiet 01 — Earplugs, 2 pairs with case | 14,90 | 4 | 4 | Accessories |
| `cover-neck` | Cover for Neck 01 | 16,90 | 4 | 1 | Covers |
| `cover-contour` | Cover for Contour 01 | 16,90 | 5 | 1 | Covers |
| `cover-side` | Cover for Side 01 | 16,90 | 3 | 1 | Covers |
| `cover-body` | Cover for Body 01 | 16,90 | 8 | 1 | Covers |
| `neck-01-cover-set` | Neck 01 + Cover | 76,90 | 4 × 2 | 1 | Sets |
| `sleep-set` | Sleep Set — Neck 01, Mask 01, Quiet 01 | 99,90 | 4 | 3 | Sets |
| `for-two` | For Two — 2 × Neck 01 | 119,90 | 4 | 2 | Sets |
| `side-sleeper-set` | Side-Sleeper Set — Neck 01 + Body 01 | 119,90 | 3 | 2 | Sets |
| `contour-for-two` | Contour for Two — 2 × Contour 01 | 99,90 | 5 | 2 | Sets |
| `family-set` | Family Set — 3 × Neck 01 | 169,90 | 4 | 3 | Sets |
| `quiet-night` | Quiet Night — Mask 01 + Quiet 01 | 29,90 | 7 | 2 | Sets |
| `evening-set` | Evening Set — Lounge 01 + Throw 01 | 94,90 | 7 × 5 | 1 | Sets |

Les identifiants Shopify (produits, collections, définitions de metafields)
sont dans `build/shopify/ids.json` et dans `build/PRODUCTS.csv` (colonnes
`handle_shopify`, `id_shopify`, `statut_shopify`).

**Sur chaque produit** : vendor `Somnila`, description en anglais simple
(dimensions cm et in côte à côte, matières du devis, poids du devis, « Ships
in 6–10 days, free shipping from €54.90 / $62.99 »), titre et description SEO,
SKU `SMN-<PRODUIT>-<COLORIS>`, coût de revient du devis sur chaque variante
(marge visible dans l'admin), stock non suivi (`tracked: false`, vente
autorisée : le fournisseur expédie), tags de rôle (`hero`, `home`, `ads`,
`catalogue`, `add-on`, `season`) qui serviront au thème en Phase 4.

**Metafields** (namespace `somnila`, définitions créées, épinglées) :
`dimensions_cm`, `dimensions_in`, `materials`, `delivery`, `includes`
(ce qui est fourni avec un produit seul), `contents` (composition d'un pack).
Le thème les affichera en Phase 4 sans retaper une donnée.

**Collections** créées, manuelles, **non publiées sur aucun canal**
(vérifié : aucune publication) : Pillows (handle `somnila-pillows`, voir
décisions), Sets, Accessories, Covers.

**Images** : 58 fichiers renommés `somnila_<produit>_<usage>_<ratio>_v1.jpg`,
alt en anglais, table de correspondance dans `build/images/shopify.csv`.
Hébergées dans le dépôt (`build/images/shopify/`) et importées par URL.

**Aucune allégation médicale** dans les 20 fiches : on parle de soutien, de
confort, de hauteur, de tenue de la mousse. Aucun avis client, aucun chiffre
de test, aucun « recommandé par ».

## 2. Décisions prises

- **Visages : exclus, sans exception.** Toutes les photos de la couverture
  montrent une personne → Throw 01 est en brouillon **sans image** (et
  l'Evening Set n'a que la photo du Lounge). Les photos du Lounge avec
  visage sont écartées aussi ; pour le Side 01, celles de la version 50 cm et
  les doublons. Phase 5 comble ces trous à partir des packshots.
- **Faux badges** sur 6 photos du Contour 01 : gardées, comme tu l'avais dit ;
  à remplacer en Phase 5.
- **Housses** : pas de photo propre dans le devis → chaque housse reprend la
  photo de son oreiller (alt explicite « shown on the pillow »).
- **Packs** : un seul produit par pack, avec options réelles. Neck 01 + Cover a
  deux options (coloris de l'oreiller, coloris de la housse de rechange). Sleep
  Set fixe le masque en Black et les bouchons en Blue pour ne pas exploser en
  4 × 7 × 4 variantes. Quiet Night propose les 7 coloris du masque, bouchons
  Blue. Evening Set croise 7 coloris de Lounge et 5 de Throw (les 5 coloris de
  couverture les plus proches de la palette), soit 35 variantes.
- **Noms de coloris** : renommés dans le vocabulaire de la marque (Night,
  Cloud, Stone, Sky, Blush, Sand, Sage, Slate…) ; correspondance avec les
  coloris du devis dans `build/shopify/products.json`.
- **Poids** : ceux du devis. Side 01 n'a pas de poids au devis, les housses
  ont un poids incertain → **aucun poids saisi** sur ces variantes plutôt
  qu'un chiffre inventé. Les tarifs de port étant forfaitaires, ça ne change
  rien au checkout.
- **Handle `pillows`** refusé par Shopify : il est réservé par une traduction
  d'une collection PORTANCE. La collection s'appelle Pillows mais son handle est
  `somnila-pillows`. À libérer en Phase 4 quand on retirera PORTANCE (l'URL
  finale sera `/collections/pillows`).
- **« 30-night trial »** : la provision retours de `PRIX.md` la suppose, mais
  je ne l'ai écrite sur aucune fiche tant que tu n'as pas confirmé la
  politique (voir § 3).
- **Prix par marché fixes (79,99 $, 59,99 £, 108,99 $ CA, 120,99 $ AU pour le
  héros, terminaison ,99 partout)** : **non appliqués, volontairement.** La
  boutique n'a aucun catalogue de marché ; en créer (Markets → catalogue
  US/UK/CA/AU → liste de prix) modifie la configuration des marchés **live**
  que PORTANCE utilise aujourd'hui — c'est l'un des cas où le brief demande
  ton « ok » explicite. Les prix sont prêts dans `PRODUCTS.csv` (`usd_fixe`,
  `gbp_fixe`, `cad_fixe`, `aud_fixe`) et dans `products.json`
  (`market_prices`). Sans eux, Shopify convertit et arrondit depuis l'EUR.

## 3. Ce qu'il me faut de toi

1. **« ok » pour la Phase 4** (thème Shrine dupliqué, non publié).
2. **« ok » pour créer les catalogues de marché** US, UK, CA, AU avec les
   listes de prix fixes ci-dessus. Ce que je ferai exactement : un catalogue
   par marché, une liste de prix en devise locale, les 138 prix fixes de
   `PRODUCTS.csv`, produits Somnila seulement. Ce que je ne toucherai pas :
   les marchés eux-mêmes, les devises, les produits PORTANCE. Si tu préfères
   attendre le retrait de PORTANCE, je le ferai en Phase 4 juste après.
3. **Politique de retour** : essai 30 nuits, oui ou non ? Elle conditionne
   les fiches, la page Shipping & Returns et la barre de réassurance.
4. **Fournisseur** : poids du Side 01 et des housses, et une photo propre
   d'une housse seule (questions déjà listées en Phase 0).

Rien d'autre n'est bloquant. Le live (thème PORTANCE, produits PORTANCE
actifs, mot de passe boutique) est exactement dans l'état où tu l'as laissé.
