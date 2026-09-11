# SOMNILA — DOSSIER COMPLET

Généré le 11 septembre 2026 depuis le dépôt `IsaacPolignac/shopify`, branche
`claude/pilloway-shopify-shrine-bwge6y`. Ce fichier concatène **tout** : la
synthèse, la méthode, la passation, les sept rapports de phase, le brand book,
les prix, les prompts, le kit de lancement, les pages et politiques, les
données produit, les fichiers du thème, les scripts, et l'inventaire des
images. Les images elles-mêmes sont dans le dépôt.

Mot de passe de la boutique, jetons et identifiants de connexion n'y figurent
pas, volontairement. Le fichier `theme/config/settings_data.json` contient le
jeton de licence du thème Shrine : ne pas le modifier.

## Sommaire

1. PARTIE 1 — SYNTHÈSE DE A À Z
2. PARTIE 2 — LA MÉTHODE
3. PARTIE 3 — PASSATION ET ACTIONS
4. PARTIE 4 — RAPPORTS DE PHASE
5. PARTIE 5 — MARQUE, PRIX, PROMPTS
6. PARTIE 6 — KIT DE LANCEMENT
7. PARTIE 7 — PAGES ET POLITIQUES (HTML, en anglais)
8. PARTIE 8 — DONNÉES PRODUIT
9. PARTIE 9 — THÈME (fichiers envoyés au thème Somnila — build v1)
10. PARTIE 10 — SCRIPTS
11. PARTIE 11 — INVENTAIRE DES IMAGES



# ══════ PARTIE 1 — SYNTHÈSE DE A À Z ══════


---

# ▶ Somnila — de A à Z

_Fichier : `build/SOMNILA_DE_A_A_Z.md`_

# Somnila — de A à Z

État au 11 septembre 2026, à lire en premier. Tout ce qui a été fait, tout
ce qui reste à faire, y compris ce que je ne peux pas faire moi-même. Les
rapports détaillés de chaque phase sont dans `build/PHASE0.md` … `PHASE7.md`,
la liste d'actions manuelles dans `build/HANDOFF.md`.

---

## 0. Où on en est, en dix lignes

- La marque **Somnila** (nom, brand core, identité visuelle, logo, polices,
  brand book) est définie et validée.
- La boutique Shopify `07beme-9h.myshopify.com` (domaine actuel `liyan.shop`)
  contient **20 produits actifs**, 5 collections, 4 menus, 5 pages, un blog
  avec 3 articles en brouillon, un profil d'expédition, et un thème complet
  **« Somnila — build v1 »**, **non publié**.
- La boutique est **derrière un mot de passe** ; le site se voit en entier via
  `https://liyan.shop/?preview_theme_id=157447585949`.
- Les visuels (packshots sur ciel Somnila, bannières, pubs, email, réseaux)
  et le kit de lancement (emails, pubs, réseaux, plan) sont livrés dans le
  dépôt.
- Une QA de 41 URL et du parcours d'achat est passée ; les défauts trouvés
  sont corrigés.
- **Il reste 16 actions manuelles** dans l'admin (§ 4A), une dizaine hors
  Shopify (§ 4B), et quelques décisions à prendre (§ 4D). Le thème se
  publie en dernier, par toi.

---

## 1. Le cadre

**Le brief** : construire de A à Z une marque internationale de produits de
sommeil sur la boutique existante, en huit phases (0 Découverte → 1 Nom et
brand core → 2 Identité visuelle → 3 Produits en brouillon → 4 Thème et
structure → 5 Visuels → 6 Kit de lancement → 7 QA et handoff), une phase à
la fois, un rapport court par phase, ton « ok » avant la suivante.

**Les règles, toutes respectées** :

1. Données réelles uniquement (devis fournisseur, zip de 56 photos, tes
   réponses). Rien d'inventé : ni avis, ni chiffre de test, ni délai.
2. Zéro promesse médicale : on dit *support, comfort, posture, shape,
   height*, jamais *pain, orthopedic, cervical, treats, doctor recommended*.
3. Tout passe par le système de marque ; aucun visage sur aucun visuel.
4. Périmètre : aucun paiement, mot de passe, domaine, compte, pixel ou clé
   touché par moi ; rien supprimé du live, aucun thème publié, aucun email
   envoyé. Travail sur un thème non publié, puis produits activés derrière
   le mot de passe sur ton accord.
5. Boutique 100 % anglais ; rapports et fichiers de synthèse en français.
6. International : US d'abord, puis CA, UK, EU, AU, reste du monde ; unités
   métriques et impériales côte à côte ; devises converties par Markets.
7. Budget serré : natif Shopify, polices libres, visuels composés à partir
   des photos, aucune app ni crédit payant sans ton accord.

**Tes décisions au fil du projet** : nom SOMNILA ; DA « nuit et aube » à la
place de la DA chaude du brief ; un seul catalogue de prix EUR converti par
marché (pas de prix fixes par pays) ; essai 30 nuits confirmé ; infos
fournisseur « plus tard » ; mot de passe boutique activé ; retrait des
photos à faux badges et texte chinois ; Phases 5, 6, 7 lancées ; adresse
`support@somnila.com`.

---

## 2. Ce qui a été fait, phase par phase

### Phase 0 — Découverte (10 septembre)

- Inventaire des fichiers : devis fournisseur (12 références, prix d'achat,
  dimensions, poids, délai 6–10 jours) et zip de 56 photos, classées dans
  `build/images/source/` avec `manifest.csv` (produit, coloris, angle,
  défaut).
- Constat clé : le brief parlait de coussins d'assise, les fichiers d'une
  gamme sommeil. Construit sur les fichiers (règle 1).
- Audit de la boutique : nom « boutique », forfait Advanced, thème LIYAN
  publié, 7 produits PORTANCE actifs, français principal + 5 langues,
  6 marchés avec « Reste du monde » en principal, profil d'expédition avec
  des délais incompatibles avec le fournisseur.
- Tableau maître `build/PRODUCTS.csv` ; données manquantes listées
  (poids Side 01, composition de mousse, coloris incohérents).
- Fichiers : `build/PHASE0.md`, `build/devis_fournisseur.txt`,
  `build/PRODUCTS.csv`, `build/images/manifest.csv`.

### Phase 1 — Nom et brand core

- 36 candidats testés (domaines par RDAP, voisinage de marques). Constat :
  plus aucun nom de deux syllabes avec `.com` libre ; **SOMNILA** retenu
  (`.com`, `.co`, `.store` libres au 10 septembre), Dormela en second,
  Aplomb écarté.
- Brand core : positionnement (le soutien nocturne comme objet de design),
  promesse *Feel it tonight. Keep it for years.*, valeurs, archétype
  Créateur, ennemi (l'oreiller « orthopédique » bleu, le bloc à 15 $, le
  faux −50 %), taglines *Sleep well.* / *Support, redesigned.* / *Held all
  night.*, histoire du fondateur à partir de tes trois réponses.
- Nomenclature : Neck 01, Contour 01, Side 01, Body 01, Lounge 01,
  Throw 01, Mask 01, Quiet 01, Cover — …, sept packs.
- Grille de prix raisonnée sur ce qui reste par commande après un CAC de
  25 € : héros à 69,90 €, packs avec remise réelle 11–19 %, accessoires
  jamais en pub seuls. Fichiers : `build/PHASE1_NOM.md`, `build/PRIX.md`,
  `build/ANALYSE_PRIX.md`.

### Phase 2 — Identité visuelle

- Système « nuit et aube » : palette Cloud `#F7F9FC` / Mist `#DCE8F2` /
  Night `#1E2A3A` / Dawn `#F0B79B` / Slate `#6B7D90` ; dégradé de ciel ;
  Fraunces Soft (titres) et Manrope (texte), libres et auto-hébergées ;
  formes arrondies, ombres teintées ; règles photo faceless ; checklist.
- Logo : wordmark « somnila » bas de casse, le « o » est une lune Dawn ;
  proposition générée sur ton prompt, validée par toi, reconstruite en
  vecteur. 22 fichiers (light, dark, on-night, une couleur, marque seule,
  favicons, avatars, icône d'app) dans `build/brand/logo/`.
- Fichiers : `build/BRAND_BOOK.md`, `build/PROMPTS.md`, `build/brand/`.

### Phase 3 — Produits en brouillon

- 20 produits créés (12 seuls, 8 packs), 138 variantes, SKU
  `SMN-<PRODUIT>-<COLORIS>`, coût de revient sur chaque variante, stock non
  suivi (le fournisseur expédie), descriptions anglaises avec cm et in,
  titres et descriptions SEO, tags de rôle.
- Metafields `somnila.*` : dimensions cm / in, matières, délai, contenu,
  fourni avec.
- 4 collections manuelles, 58 images renommées et importées avec alt.
- Décisions : photos avec visage exclues ; housses illustrées par la photo
  de leur oreiller ; noms de coloris de marque ; aucun poids inventé.
- Fichiers : `build/PHASE3.md`, `build/shopify/products.json`,
  `build/shopify/ids.json`, `build/images/shopify.csv`.

### Phase 4 — Thème Shrine et structure du site

- Thème Shrine PRO dupliqué par l'API en « Somnila — build v1 », 15 fichiers
  réécrits : réglages (palette, formes, logo, favicon, panier), en-tête
  (barre d'annonce à 3 messages réels, menu, polices injectées par une
  section Liquid), pied (4 colonnes, newsletter, sélecteur de pays),
  accueil (hero, tuiles, produit vedette, bénéfices, matières, gamme, FAQ,
  packs, newsletter ; avis désactivés faute d'avis réels), 3 gabarits
  produit (oreiller / pack / accessoire, avec tableau des dimensions lu dans
  les metafields, livraison estimée, accordéons, bouton sticky),
  collection, panier, pages, 404, recherche, blog.
- 5 pages créées (Our story, FAQ, Contact avec formulaire, Shipping &
  delivery, Returns & 30-night trial), 4 menus, profil d'expédition
  « Somnila » (6 zones, 6–10 jours, offert dès 54,90 €), 4 politiques
  rédigées (non écrites : droit manquant), maquettes de design publiées.
- Passe design après ton retour : hero refait, typographie unifiée,
  alignements, matières, descriptions sans doublon, collection renommée
  `memory-foam-pillows` (collision avec une URL PORTANCE), traductions
  héritées supprimées.
- Après ton mot de passe : 20 produits activés et publiés, photos
  fournisseur nettoyées (faux badges, cotes, caractères chinois, boîte de
  marque tierce), langues de/es/it/nl dépubliées.
- Fichiers : `build/PHASE4.md`, `build/theme/`, `build/pages/`,
  `build/preview/`, `build/design/`.

### Phase 5 — Visuels

- 29 packshots détourés et posés sur le ciel Somnila (Neck, Contour, Side,
  Lounge, housses, packs), remplacés dans les galeries de 14 produits.
- Throw 01 : les 10 photos avec mannequin recadrées sur la couverture
  seule, un détail par coloris.
- 5 bannières de collection (posées sur les collections), 9 pubs statiques
  (3 messages × 3 formats), en-tête et pied d'email, avatar, couverture,
  image de partage.
- Sans crédits de génération : pas de scène lifestyle ni de vidéo.
- Fichiers : `build/PHASE5.md`, `build/images/site/` (scripts
  `sky-packshots.py`, `gen-visuals.py`, `clean-supplier-photos.py`).

### Phase 6 — Kit de lancement

- `build/launch/EMAILS.md` (bienvenue ×3, panier abandonné, notifications,
  post-achat, avis), `ADS.md` (Meta, TikTok, Google, conformité),
  `SOCIAL.md` (bios, 12 posts, 4 scripts vidéo sans visage, réponses),
  `PLAN.md` (checklist, J−14 → J+30, indicateurs, service client).
- Blog « Notes from the workshop » avec 3 articles en brouillon.
- Fichiers : `build/PHASE6.md`, `build/launch/`.

### Phase 7 — QA et passation

- 41 URL et 59 liens vérifiés, parcours panier testé, corrections (pied de
  panier sans bouton de paiement, H1 de l'accueil, contact avec l'adresse,
  gabarits blog).
- `build/HANDOFF.md` (actions manuelles ordonnées), `build/PHASE7.md`,
  fichiers racine du dépôt pointés vers Somnila.

---

## 3. Inventaire

### 3.1 Dans Shopify (`07beme-9h.myshopify.com`)

| Objet | Identifiant | État |
|---|---|---|
| Thème Somnila — build v1 | `OnlineStoreTheme/157447585949` | non publié, complet |
| Thème PORTANCE (précédent, non publié) | `157230071965` | intact |
| Thème LIYAN publié (live) | `157007184029` | intact, derrière mot de passe |
| Produits Somnila (20) | `Product/9042360369309` (Neck 01) … `9042362761373` (Evening Set) — liste dans `build/shopify/ids.json` | actifs, publiés Boutique en ligne |
| Collections | memory-foam-pillows `348677243037`, sets `348677275805`, accessories `348677308573`, covers `348677341341`, shop-all `348677832861` | publiées, images posées |
| Menus | somnila-main `253644374173`, somnila-shop `253644439709`, somnila-help `253644472477`, somnila-legal `253644505245` | en place |
| Pages | about `122788348061`, shipping-delivery `122788380829`, returns-warranty `122788413597`, faq `122788446365`, contact `122788479133` | publiées |
| Blog | `Blog/101191712925` (`/blogs/notes`), articles `577753809053`, `577753841821`, `577753874589` | brouillons |
| Profil d'expédition Somnila | `DeliveryProfile/109282361501` | 6 zones |
| Canal Boutique en ligne | `Publication/218511016093` | |
| Profil de checkout | `CheckoutProfile/6613401757` | branding manuel |
| Fichiers | logos, favicon, polices woff2, hero v2, image matières, image de partage, en-tête email | Contenu → Fichiers |
| Langues | fr principal, en publié ; de, es, it, nl dépubliées | |
| Marchés | US, CA, UK, AU, Europe, Reste du monde (principal, à changer) | |

### 3.2 Dans le dépôt (`IsaacPolignac/shopify`, branche `claude/pilloway-shopify-shrine-bwge6y`)

```
build/
  SOMNILA_DE_A_A_Z.md   ce document
  HANDOFF.md            actions manuelles ordonnées
  PHASE0.md … PHASE7.md rapports de phase
  BRAND_BOOK.md, PHASE1_NOM.md, PRIX.md, ANALYSE_PRIX.md, PROMPTS.md
  PRODUCTS.csv, devis_fournisseur.pdf/.txt
  brand/                logo (svg/png), favicons, polices, planche
  theme/                config, sections, templates du thème Somnila
  pages/                5 pages + policies/ (4 textes à coller)
  shopify/              products.json, ids.json
  images/source/        56 photos du zip, manifest.csv
  images/shopify/       photos produit v1 et v2 nettoyées, shopify.csv
  images/site/          hero, packshots ciel, bannières, pubs, email, social, scripts
  launch/               EMAILS.md, ADS.md, SOCIAL.md, PLAN.md
  design/               maquettes (canvas de design)
  preview/              captures de vérification
```

Maquettes en ligne : https://claude.ai/code/artifact/aa518baf-804a-4a9a-8835-7b4bb9ed2e1f

---

## 4. Ce qu'il reste à faire

### 4A. Toi, dans l'admin Shopify — dans cet ordre

| # | Action | Où | Pourquoi |
|---|---|---|---|
| 1 | Renommer la boutique **Somnila** (pas SOMNILA) | Paramètres → Détails de la boutique | titres d'onglet en double, pied de page |
| 2 | Email de contact et d'expéditeur **support@somnila.com** + authentification du domaine d'envoi | Paramètres → Détails / Notifications | emails, politiques, processeurs de paiement |
| 3 | Titre et méta-description de l'accueil (textes dans `HANDOFF.md`) | Boutique en ligne → Préférences | l'accueil porte encore le titre PORTANCE |
| 4 | Coller les 4 politiques de `build/pages/policies/` et remplir les champs entre crochets | Paramètres → Politiques | liens du pied en 404, exigé par Google Shopping et Meta |
| 5 | Langue par défaut → anglais, puis me le dire | Paramètres → Langues | boutique 100 % anglais |
| 6 | Marché principal → États-Unis | Paramètres → Marchés | règle 6 |
| 7 | Shopify Payments + PayPal, commande test remboursée | Paramètres → Paiements | rien ne se vend sans |
| 8 | Branding du checkout (logo, Cloud, Night, Manrope) | Paramètres → Paiement → Personnaliser | API réservée au plan Plus |
| 9 | Domaine `somnila.com` acheté, connecté, principal ; `liyan.shop` redirigé | Paramètres → Domaines | |
| 10 | Ancien catalogue : me dire « ok » (je le retire du canal) ou l'archiver toi-même | Produits, Collections | visible dans la recherche et `/collections` |
| 11 | Pixels et canaux : Facebook & Instagram, TikTok, Google & YouTube, Search Console | Canaux de vente / apps | mesure |
| 12 | Shopify Email : en-tête, pied, automatisations de `launch/EMAILS.md` | Marketing → Automatisations | |
| 13 | Réseaux : profils, bios, premiers posts (`launch/SOCIAL.md`) | hors Shopify | |
| 14 | Lire et publier les 3 articles | Boutique en ligne → Articles de blog | |
| 15 | **Publier le thème « Somnila — build v1 »** | Boutique en ligne → Thèmes | en dernier ; retour arrière en un clic |
| 16 | Retirer le mot de passe le jour J | Boutique en ligne → Préférences | |

Optionnel mais recommandé : forfait **Advanced → Basic** (~360 $/mois
économisés, rien dans le projet n'exige Advanced) ; vérifier si les apps
payantes **AutoDS** et **QSTOMY** servent encore ; bannière cookies aux
couleurs Somnila (Paramètres → Confidentialité des clients).

### 4B. Toi, hors Shopify

- **Entité légale** : raison sociale, forme, adresse, immatriculation, TVA,
  pays du siège (les politiques les attendent).
- **Dépôt de marque** : recherche d'antériorité SOMNILA, classes 20, 24, 35
  (voisinage SOMNIA en classe 5 à faire regarder), puis dépôt.
- **Domaine et emails** : `somnila.com`, boîte `support@somnila.com`.
- **Fournisseur** : emballage neutre pour Quiet 01 (boîte « iMeBoBo »),
  composition et densité de la mousse, poids et dimensions de Side 01,
  poids des housses, circuit des numéros de suivi, photos de la couverture
  à plat, confirmation du 6–10 jours et du processus de remboursement sans
  retour.
- **Comptes** : Meta Business, TikTok for Business, Google Ads / Merchant
  Center, Pinterest, Instagram, TikTok (handle `@somnila` à réserver).
- **Budget** : enveloppe pub des deux premières semaines (règles d'arrêt
  dans `launch/ADS.md`) ; crédits de génération d'images si tu veux des
  scènes lifestyle et des vidéos sans visage.
- **Avis** : app d'avis gratuite quand dix avis réels existent ; la section
  avis de l'accueil est désactivée jusque-là.

### 4C. Moi, sur ton signal

- Retirer les 7 produits PORTANCE et les 10 anciennes collections du canal
  Boutique en ligne (réversible, rien supprimé).
- Retirer la langue française une fois l'anglais en langue par défaut.
- Créer le code **WELCOME10** si tu dis oui.
- Remplacer les photos de Throw 01 si tu en obtiens de meilleures ; refaire
  les scènes lifestyle et les vidéos si des crédits arrivent.
- Après tes réglages : re-vérifier titres d'onglet, politiques, checkout,
  puis une dernière passe avant que tu publies.
- Ajouter à la FAQ toute question posée trois fois au service client.

### 4D. Décisions ouvertes

| Question | Ma recommandation |
|---|---|
| WELCOME10, 10 % sur la première commande (oreillers et packs) | oui si tu veux accélérer les premiers avis ; ~7 € par commande héros |
| Crédits de génération (lifestyle, UGC) | attendre les 30 premières commandes ; les packshots sur ciel suffisent au lancement |
| Prix fixes par marché (79,99 $, 59,99 £…) au lieu de la conversion | non pour le lancement ; à revoir avec les premières données |
| Forfait Advanced | passer à Basic |
| Throw 01 et Evening Set | garder, photos détail acceptables ; meilleures photos si le fournisseur en a |

---

## 5. Risques et points d'attention

- **Allégations** : tout texte futur (pubs, posts, réponses) reste dans le
  vocabulaire autorisé du brand book § 4. Une seule phrase « soulage la
  douleur » expose la boutique et les comptes pub.
- **Données fournisseur** : composition de mousse et densité absentes ;
  poids Side 01 et housses absents ; Quiet 01 livré dans une boîte de marque
  tierce. À régler avant les premières commandes.
- **Photos** : galeries sur ciel pour les oreillers ; Mask 01, Quiet 01,
  Body 01 restent en photos fournisseur nettoyées ; Throw 01 en détails
  recadrés à 700 px de source.
- **Prix** : conversion automatique par Markets, donc des montants non
  arrondis (81,03 $) ; les arrondis par marché existent dans `PRODUCTS.csv`
  si tu changes d'avis.
- **Livraison** : 6–10 jours partout, offert sur oreillers et packs ; le
  profil général (PORTANCE) coexiste, à supprimer quand l'ancien catalogue
  part.
- **Aperçu produit** : le lien *Aperçu* d'un produit change à chaque
  modification ; toujours le reprendre depuis la fiche.
- **Ancien catalogue** : tant qu'il est publié, il apparaît dans la
  recherche et `/collections`.

---

## 6. Comment reprendre le travail

- Ouvrir une session sur le dépôt, branche
  `claude/pilloway-shopify-shrine-bwge6y`, lire ce fichier puis
  `build/HANDOFF.md`.
- Le connecteur Shopify permet : produits, collections, menus, pages, blog,
  fichiers, metafields, thèmes non publiés, expédition, langues (hors langue
  par défaut), publications. Il ne permet pas : publier un thème, supprimer
  un fichier de thème, écrire les politiques, le checkout hors Plus, le nom
  et l'email de la boutique, le titre SEO de l'accueil, paiements, domaine,
  pixels, mot de passe.
- Scripts utiles : `build/images/site/sky-packshots.py` (détourage et
  ciel), `gen-visuals.py` (bannières, pubs, email, social),
  `clean-supplier-photos.py` (nettoyage des photos fournisseur) ; le rendu
  du site derrière le mot de passe se fait avec un navigateur sans
  interface (Playwright) et un relais réseau, script `render.cjs` dans
  l'espace de travail de la session.
- Toute modification du thème se fait dans `build/theme/` puis est envoyée
  au thème `157447585949` par `themeFilesUpsert` ; le jeton de licence
  Shrine dans `settings_data.json` ne se régénère jamais.




# ══════ PARTIE 2 — LA MÉTHODE ══════


---

# ▶ La méthode, pas à pas

_Fichier : `build/METHODE.md`_

# Somnila — la méthode, pas à pas

Comment chaque chose a été faite, avec quels outils et quelles opérations,
pour qu'une autre personne ou un autre outil puisse refaire, corriger ou
prolonger le travail. Complète `SOMNILA_DE_A_A_Z.md` (le quoi) et
`HANDOFF.md` (le reste à faire).

## 1. Les outils

- **Connecteur Shopify** relié à `07beme-9h.myshopify.com` : requêtes et
  mutations **GraphQL Admin API**. Toute écriture dans la boutique passe par
  là. Limites rencontrées : pas de publication de thème, pas de suppression
  de fichier de thème, pas d'écriture des politiques
  (`write_legal_policies` absent), branding du checkout réservé au plan
  Plus, pas de changement du nom, de l'email, de la langue par défaut ni du
  titre SEO de l'accueil.
- **Dépôt Git public** `IsaacPolignac/shopify` : source de vérité de tout ;
  les images y sont poussées puis importées par Shopify depuis l'URL brute
  GitHub (`fileCreate`, `productCreateMedia`, `collectionUpdate.image.src`).
- **Python 3** avec Pillow, OpenCV, NumPy, fontTools : nettoyage et
  détourage des photos, compositing, bannières et pubs, sous-ensembles de
  polices.
- **Node + Playwright (Chromium)** pour rendre le site : le proxy de
  l'environnement coupe les tunnels navigateur, donc chaque requête du
  navigateur est relayée par `fetch` avec un pot de cookies (script
  `render.cjs`). Le mot de passe boutique est passé par un POST sur
  `/password`, le thème par `?preview_theme_id=…`.
- **Aucun agent parallèle, aucune app payante, aucun crédit de génération
  d'images** (solde Higgsfield 0,2).

## 2. Phase 0 — Découverte

1. Extraction du texte du devis PDF (`pdftotext`) → `devis_fournisseur.txt`.
2. Dézippage des 56 photos, classement à la main par produit / coloris /
   angle / défaut → `images/source/<produit>/` + `manifest.csv`.
3. Audit de la boutique par requêtes GraphQL : `shop`, `themes`,
   `products`, `collections`, `shopLocales`, `markets`,
   `deliveryProfiles`, apps installées.
4. Tableau maître `PRODUCTS.csv` : une ligne par référence, coût, dimensions
   cm et in, poids, coloris, délai, photos utilisables, données manquantes.

## 3. Phase 1 — Nom

1. Liste de 36 candidats, test de disponibilité `.com/.co/.store` par RDAP
   (registres Verisign, .co, .store), redirections suivies.
2. Voisinage de marques par recherche web (les bases EUIPO/USPTO refusent
   les requêtes automatisées d'ici).
3. Recommandation argumentée, brand core écrit à partir des trois réponses
   du fondateur, nomenclature produit, grille de prix calculée sur le reste
   par commande après un CAC de 25 € (`PRIX.md`, `ANALYSE_PRIX.md`).

## 4. Phase 2 — Identité

1. Palette, typographie, formes, lumière, composition, checklist :
   `BRAND_BOOK.md`.
2. Logo : prompt écrit pour un générateur d'images (`PROMPTS.md`), image
   validée par le fondateur, puis **reconstruction en vecteur** (tracés
   mesurés pixel par pixel, lune construite géométriquement) → SVG et PNG
   dans `brand/logo/`, favicons, avatars.
3. Polices : Fraunces instanciée en Soft (axe SOFT=100, WONK=0) avec
   fontTools `instancer`, puis sous-ensemble latin en woff2 (73 Ko) ;
   Manrope sous-ensemble (28 Ko). Hébergées dans Fichiers Shopify.

## 5. Phase 3 — Produits

1. `shopify/products.json` : source de chaque produit (titre, handle,
   description HTML, SEO, options, variantes avec prix, SKU, coût, poids,
   metafields, images avec alt).
2. Création par l'API : produit, options et variantes, coût de revient sur
   l'article d'inventaire, stock non suivi, définitions de metafields
   `somnila.*` (dimensions_cm, dimensions_in, materials, delivery,
   includes, contents), images importées depuis le dépôt avec alt,
   collections manuelles et affectation. Identifiants dans
   `shopify/ids.json`.
3. Vérification après création : statut DRAFT, images READY, nombre de
   variantes.

## 6. Phase 4 — Thème et structure

1. `themeDuplicate` du Shrine PRO installé → « Somnila — build v1 », non
   publié. Téléchargement des fichiers utiles par `theme.files` pour lire
   les schémas de sections (réglages disponibles, pas, options).
2. Édition **locale** des JSON (`theme/config/settings_data.json`,
   `sections/header-group.json`, `footer-group.json`,
   `templates/*.json`) puis envoi par `themeFilesUpsert` (contenu JSON
   minifié passé en variable). Règles apprises : un réglage inconnu est
   ignoré en silence ; un `range` hors pas est rejeté ; le jeton de licence
   Shrine dans `settings_data.json` ne se régénère jamais.
3. Polices non présentes dans la bibliothèque Shopify : réglage
   `sans_serif_n4` côté thème, et une section `custom-liquid` dans le
   groupe d'en-tête (`somnila-styles`) qui injecte `@font-face` et
   redéfinit `--font-heading-family` / `--font-body-family`, plus toute la
   CSS de marque (rayons, ombres, tailles, tuiles, pied). La section est
   réduite à zéro hauteur ; elle porte aussi le H1 masqué de l'accueil.
4. Accueil, 3 gabarits produit (`product.json`, `product.set.json`,
   `product.accessory.json`), collection, panier, pages, 404, recherche,
   blog. Le tableau des dimensions est un bloc `custom_liquid` qui lit les
   metafields et convertit le poids en livres.
5. Pages : `pageCreate` avec metafields `global.title_tag` /
   `global.description_tag`. Menus : `menuCreate`. Livraison :
   `deliveryProfileCreate` avec zones, tarifs et conditions de prix
   (`priceConditionsToCreate`). Gabarit par produit : `productUpdate`
   `templateSuffix`.
6. Piège : le duplicata héritait des **traductions** du thème précédent
   (clés `section.*` par langue) qui écrasaient mes textes →
   `translationsRemove` sur en/de/es/it/nl. Piège : le handle `pillows`
   était pris par la traduction anglaise d'une collection PORTANCE →
   collection renommée `memory-foam-pillows`.
7. Vérification : rendu Playwright de chaque page (desktop 1440, mobile
   390), découpe en bandes, lecture visuelle, corrections, re-rendu. Les
   produits en brouillon ne se rendent pas dans l'aperçu public ; le lien
   d'aperçu produit (`preview_key`) change à chaque modification.
8. Après activation du mot de passe par le fondateur : `productUpdate`
   status ACTIVE ×20, `publishablePublish` sur le canal Boutique en ligne
   (produits et collections), `shopLocaleUpdate published:false` pour
   de/es/it/nl.

## 7. Phase 5 — Visuels

1. **Nettoyage des photos fournisseur** (`images/site/…/clean-supplier-photos.py`) :
   badges effacés par interpolation verticale du fond ; caractères et
   cotes effacés par masques + `cv2.inpaint` (Telea) ; bouchons recadrés
   sur l'étui. Fichiers `_v2`, remplacement des médias
   (`productCreateMedia` depuis GitHub, attente `READY`, `fileDelete` des
   anciens, `productReorderMedia`).
2. **Packshots sur ciel** (`sky-packshots.py`) : estimation du fond selon
   la famille (interpolation haut/bas pour les fonds unis à vignette ;
   médiane des marges par ligne pour les dégradés verticaux ; surface
   quadratique ajustée sur le cadre), distance en Lab → masque grossier,
   affinage **GrabCut** (init rectangle, RNG fixée, résultat contraint au
   masque grossier dilaté), bouchage des trous, dé-mélange des bords, ombre
   du fournisseur conservée dans une bande autour de l'objet, pose sur le
   dégradé Cloud → Mist avec halo Dawn, sorties 1:1 et 4:5. Une méthode par
   famille de produit, choisie en regardant des planches de contrôle.
3. **Bannières, pubs, email, réseaux** (`gen-visuals.py`) : mêmes
   détourages, Fraunces Soft / Manrope via les axes des polices variables
   (noms d'axes « Optical Size », « Weight », « Softness », « Wonky »),
   grilles de mise en page par format.
4. Throw 01 : recadrage des photos avec mannequin sur la zone basse du lit,
   un détail par coloris ; Lounge 01 : texte effacé. Images de collection
   par `collectionUpdate`.

## 8. Phase 6 — Kit de lancement

1. Textes écrits à partir du brand book et des données produit, dans le
   vocabulaire autorisé ; pas de prix dans les pubs (conversion par
   marché) ; règles d'arrêt calculées depuis `PRIX.md`.
2. Blog `blogCreate` + `articleCreate` (brouillons), gabarits blog/article
   réécrits.

## 9. Phase 7 — QA

1. `qa-crawl.cjs` : connexion par mot de passe, cookie d'aperçu, parcours
   de 41 URL en `fetch`, extraction titre / description / H1 / erreurs
   Liquid / résidus français / marques tierces / caractères chinois /
   images manquantes / liens internes ; puis test des 59 liens avec un
   délai (Shopify renvoie 429 sans délai).
2. Parcours d'achat : `POST /cart/add.js` dans le contexte du navigateur
   puis rendu de `/cart`.
3. Corrections envoyées au thème, re-rendu, captures dans `preview/`.

## 10. Ordre des opérations si tout était à refaire

Devis et photos → nom et prix → brand book et logo → produits en brouillon
→ thème dupliqué et réglé → pages, menus, livraison → mot de passe puis
activation → nettoyage et packshots → kit → QA → réglages manuels de
l'admin → publication du thème → retrait du mot de passe.




# ══════ PARTIE 3 — PASSATION ET ACTIONS ══════


---

# ▶ Passation

_Fichier : `build/HANDOFF.md`_

# Somnila — passation

Date : 11 septembre 2026. Ce document est la liste exacte de ce qui reste
à faire **à la main** avant et après la mise en ligne, avec où cliquer.
Tout ce qui pouvait être fait par l'API l'a été. Rien n'a été publié,
supprimé ni envoyé sans ton accord ; le thème Somnila n'est pas publié.

## 1. Ce qui existe dans la boutique `07beme-9h.myshopify.com`

| Objet | État | Où |
|---|---|---|
| Thème **« Somnila — build v1 »** (Shrine PRO 1.2.3) | complet, **non publié** | Boutique en ligne → Thèmes |
| 20 produits Somnila | actifs, publiés sur la Boutique en ligne, galeries sur ciel Somnila | Produits (filtre vendeur Somnila) |
| 5 collections : `memory-foam-pillows`, `sets`, `accessories`, `covers`, `shop-all` | publiées, image de collection posée | Produits → Collections |
| 4 menus : `somnila-main`, `somnila-shop`, `somnila-help`, `somnila-legal` | en place | Boutique en ligne → Navigation |
| 5 pages : `/pages/about`, `faq`, `contact`, `shipping-delivery`, `returns-warranty` | publiées, en anglais | Boutique en ligne → Pages |
| Blog « Notes from the workshop » | 3 articles **en brouillon** | Boutique en ligne → Articles de blog |
| Profil d'expédition « Somnila » | 6 zones, 6–10 jours, offert dès 54,90 € | Paramètres → Expédition |
| Fichiers : logos, favicon, polices, hero, packshots, image de partage, en-tête email | dans Fichiers | Contenu → Fichiers |
| Langues de, es, it, nl | dépubliées | Paramètres → Langues |
| Mot de passe boutique | actif | Boutique en ligne → Préférences |

Le dépôt `IsaacPolignac/shopify`, branche `claude/pilloway-shopify-shrine-bwge6y`,
dossier `build/`, contient la source de tout : thème (`theme/`), produits
(`shopify/products.json`), pages et politiques (`pages/`), images
(`images/`), kit de lancement (`launch/`), rapports `PHASE0` à `PHASE7`.

## 2. Avant la mise en ligne — dans l'ordre

1. **Nom de la boutique → `Somnila`** (pas en capitales). Paramètres →
   Détails de la boutique. Aujourd'hui « SOMNILA » : il s'affiche dans les
   titres d'onglet (« … | Somnila – SOMNILA ») et le pied de page ; avec
   « Somnila » le doublon disparaît de lui-même.
2. **Email de contact et d'expéditeur → `support@somnila.com`**. Paramètres
   → Détails de la boutique (email de contact) et Paramètres →
   Notifications → Email de l'expéditeur. Vérifier l'authentification du
   domaine d'envoi (SPF/DKIM) que Shopify propose au même endroit.
3. **Titre et description de l'accueil**. Boutique en ligne → Préférences →
   Titre et méta-description : titre *Somnila — Memory-foam pillows shaped
   around the way you lie*, description *Memory-foam pillows with a cover
   you can wash and thirty nights to decide. Neck 01, Contour 01, Side 01,
   Body 01, Lounge 01. Free shipping, 6–10 days.* Aujourd'hui l'accueil
   porte encore le titre PORTANCE.
4. **Politiques**. Paramètres → Politiques : coller les 4 textes de
   `build/pages/policies/` (refund, shipping, terms, privacy). Les champs
   entre crochets restent à remplir : raison sociale, forme juridique,
   adresse, immatriculation, TVA, pays du siège. Tant qu'elles ne sont pas
   créées, les liens Refund / Terms / Shipping du pied renvoient une 404.
5. **Langue par défaut → anglais**. Paramètres → Langues → « Modifier la
   langue par défaut ». Dis-le-moi ensuite : je retire le français.
6. **Marché principal → États-Unis**. Paramètres → Marchés (aujourd'hui
   « Reste du monde »). Les prix restent en EUR convertis.
7. **Paiements**. Shopify Payments (ou autre) et PayPal, puis une commande
   test avec une vraie carte, remboursée.
8. **Checkout**. Paramètres → Paiement → Personnaliser : logo
   `somnila-logo-light.png`, fond `#F7F9FC`, texte et boutons `#1E2A3A`,
   police Manrope si proposée.
9. **Domaine `somnila.com`** : achat, connexion, domaine principal ;
   `liyan.shop` en redirection.
10. **Anciens produits PORTANCE et LIYAN**. 7 produits PORTANCE sont encore
    actifs (Appui, Aplomb, taies, bandelettes) et 10 anciennes collections
    (tétines, biberons, éveil & dentition, coffrets, ancienne gamme, best
    sellers, oreillers, taies & housses, respiration & sommeil, page
    d'accueil) sont publiées : ils apparaissent dans la recherche et sur
    `/collections`. Sur ton « ok » je les retire de la Boutique en ligne
    (réversible) ; tu peux aussi les archiver toi-même.
11. **Pixels et canaux** : app Facebook & Instagram (pixel + API de
    conversions), app TikTok, canal Google & YouTube, Search Console.
12. **Shopify Email** : importer l'en-tête et le pied
    (`build/images/site/email/`), créer les automatisations depuis
    `build/launch/EMAILS.md`.
13. **Réseaux** : profils avec `build/images/site/social/`, bios dans
    `build/launch/SOCIAL.md`.
14. **Lire et publier les 3 articles** du blog.
15. **Publier le thème** « Somnila — build v1 » (Boutique en ligne → Thèmes
    → … → Publier). L'API me l'interdit ; l'ancien thème reste en retour
    arrière.
16. **Retirer le mot de passe** le jour J.

## 3. À demander au fournisseur

- Emballage neutre pour Quiet 01 (boîte « iMeBoBo » sur les photos).
- Composition et densité de la mousse (les fiches disent « memory foam »
  sans chiffre).
- Poids et dimensions exactes de Side 01 ; poids réel des housses.
- Comment les numéros de suivi te parviennent, pour l'email d'expédition.
- Photos de la couverture à plat, sans personne, si possible.

## 4. Décisions encore ouvertes

- **WELCOME10** (10 % première commande, oreillers et packs) : non créé.
- **Crédits de génération d'images** : sans eux, pas de scènes lifestyle
  ni d'UGC vidéo ; le site vit avec les packshots sur ciel.
- **Retrait du français** une fois l'anglais en langue par défaut.

## 5. Comment vérifier le site

Aperçu complet derrière le mot de passe :
`https://liyan.shop/?preview_theme_id=157447585949`. Le lien *Aperçu* d'un
produit change à chaque modification : le reprendre depuis la fiche.
Captures de référence dans `build/preview/`.

## 6. Ce que le connecteur ne peut pas faire (pour la prochaine session)

Publier un thème, supprimer un fichier de thème, écrire les politiques
(`write_legal_policies`), le branding du checkout hors plan Plus, changer
le nom, l'email ou la langue par défaut de la boutique, le titre SEO de
l'accueil, activer paiements, domaine, pixels.




# ══════ PARTIE 4 — RAPPORTS DE PHASE ══════


---

# ▶ PHASE0

_Fichier : `build/PHASE0.md`_

# Phase 0 — Découverte

Date : 10 septembre 2026. Aucune écriture dans Shopify pendant cette phase.

## 1. Fichiers — reçus le 10 septembre, inventoriés

`devis_fournisseur.pdf` (9 pages, 12 références) et `ImagesShopifyphotosmisesajour.zip`
(56 photos). Texte du devis extrait dans `build/devis_fournisseur.txt`, photos
classées par produit dans `build/images/source/<produit>/` avec `manifest.csv`
(index, produit, coloris, angle, défaut).

### Ce que les fichiers disent — et ce que le brief disait

**Le brief parle de coussins d'assise. Les fichiers parlent de sommeil.** Le devis
contient cinq oreillers (cervical, contour, latéral, corporel en S, lecture au
lit), quatre housses, une couverture, un masque et des bouchons d'oreilles. Pas
un coussin d'assise, pas de Seat 01 ni de Lumbar 01. Règle 1 : je construis sur
les fichiers. Le système de marque du brief (positionnement objet de design,
DA chaude, faceless, zéro promesse médicale) s'applique tel quel à une gamme
sommeil — seule la nomenclature change, elle sera proposée en Phase 1.

### Tableau maître — `build/PRODUCTS.csv`

Douze références, toutes avec prix de revient, dimensions cm et in, poids,
coloris, délai fournisseur (**6–10 jours partout**), images disponibles, angles
manquants, données manquantes. Les deux colonnes `PROPOSITION_*` sont des
propositions de prix de vente, pas des données : le devis ne contient que des
prix d'achat.

| # | Produit (nom fournisseur) | Coût | Poids | Photos utilisables |
|---|---|---|---|---|
| 09 | Oreiller cervical (« Derila ») | 25,00 € | 1,4 kg | 2 sur 4 |
| 12 | Oreiller contour (« Cloudii ») | 19,00 € | 1,1 kg | 5 sur 11 |
| 10 | Oreiller latéral (« Derila ») | 20,00 € | **absent** | 0 sur 6 |
| 11 | Oreiller corporel en S (« Snuggi ») | 24,00 € | 1,8 kg | 8 sur 8 |
| 01 | Oreiller lecture au lit | 19,50 € | 1,1 kg | 1 sur 6 |
| 02 | Couverture effet fourrure 200 × 230 | 19,00 € | 3,2 kg | 0 sur 10 |
| 03 | Masque de sommeil 3D | 6,00 € | 0,07 kg | 6 sur 7 |
| 04 | Bouchons d'oreilles, 2 paires | 6,00 € | 0,02 kg | 0 sur 4 |
| 05–08 | Quatre housses | 3,00 € | incohérent | 0 dédiée |

### Les photos : 22 utilisables sur 56, et quatre problèmes

- **Six photos de l'oreiller contour portent de faux badges** « The Rated
  Pillow · Best Pillow 2025 · Innovation Sleep Award ». Ce sont des visuels
  fournisseur, pas des distinctions. Les publier serait une allégation
  trompeuse : elles ne sortent pas du dossier source.
- **Les bouchons d'oreilles arrivent dans une boîte de marque tierce
  (« iMeBoBo »)**, en chinois. Une marque premium ne peut pas livrer un produit
  dans l'emballage d'une autre. Soit le fournisseur a une version neutre, soit
  la référence sort de la gamme.
- **Les dix photos de la couverture montrent un visage** ; la trame est
  utilisable en recadrage macro, rien d'autre.
- Le reste porte des cotes en chinois, des vignettes avec mannequins, un décor
  enfantin. Ce sont des références de forme pour la Phase 5, pas des visuels
  de boutique. Le brief l'avait prévu : tout est regénéré à partir des
  détourages.

### Données manquantes ou contradictoires — à demander au fournisseur

1. Poids de l'oreiller latéral 60 cm : absent.
2. Housses annoncées à 0,8–1,8 kg : c'est le poids d'un oreiller, pas d'une
   housse. À confirmer avant de paramétrer l'expédition.
3. Oreiller latéral : 60 × 35 (devis) ou 60 × 33 (photos).
4. Oreiller corporel : 120 cm retenu, 105 × 30 lisibles sur la photo.
5. Composition exacte et densité de mousse : aucune référence ne les donne.
   Sans elles, les fiches diront « memory foam » sans chiffre — le brief
   demande des chiffres.
6. Coloris : le devis liste des coloris « fournisseur » qui ne correspondent
   pas aux photos (cervical : « violet, marron, noir » au devis, « blanc, bleu
   clair » en photo). Seuls les coloris confirmés seront créés.

### Délais : le devis contredit le profil d'expédition

Le fournisseur annonce **6–10 jours** sur toutes les références. Le profil
d'expédition de la boutique affiche EU 3–5 j, US 5–8 j, UK 4–7 j. Si
l'expédition part du fournisseur (AutoDS est installée, l'adresse
d'expédition est à Albuquerque), les délais affichés sont intenables. Phase 4
alignera la barre d'annonce, les fiches et la page Livraison sur 6–10 jours
plus préparation, sauf indication contraire de ta part.

### Marques tierces dans le devis

« Derila », « Cloudii », « Snuggi » sont les noms de marques concurrentes que
le fournisseur utilise pour désigner les formes. Ils n'apparaîtront nulle part
dans la boutique, ni dans un nom, ni dans une balise, ni dans un alt.

## 1 bis. Ce que je n'avais pas trouvé d'ici avant l'envoi

Ce que tu lis tourne dans un conteneur Linux distant, pas sur ton Mac :
`mdfind` et les tags Finder n'existent pas ici. J'ai cherché aux trois endroits
auxquels j'ai accès :

| Où | Résultat |
|---|---|
| Dépôt git `IsaacPolignac/shopify` | aucun `.zip`, `.csv`, `.xlsx`, `.pdf` ; aucune mention de coussin d'assise |
| Gmail (pièces jointes, 120 derniers jours + mots-clés coussin / cushion / fournisseur / prix) | rien de lié au projet — factures IONOS, candidatures, OUIGO |
| Notion | aucune page ne contient « coussin » |

Le tableau maître `build/PRODUCTS.csv` est prêt avec les colonnes du brief, et le
dossier `build/images/source/` attend le zip. Rien ne peut être écrit sans ces
données : c'est la règle 1, données réelles uniquement.

## 2. Audit de la boutique — `07beme-9h.myshopify.com` → `liyan.shop`

| Élément | État constaté |
|---|---|
| Nom de la boutique | **« boutique »** — jamais renommé, visible dans les titres d'onglet |
| Forfait | **Advanced** (~399 $/mois) — surdimensionné pour un lancement, voir décisions |
| Devise de base | EUR |
| Unités | **impérial / livres** (adresse de facturation : Albuquerque, États-Unis) |
| Mot de passe boutique | **désactivé — la boutique est publique** |
| Thème publié (MAIN) | « LIYAN — v3 (France) », l'ancien projet puériculture |
| Thème non publié | **Shrine PRO v1.2.3 (186 sections)** — installé, c'est le thème de travail actuel |
| Produits | 11 : 4 LIYAN (3 archivés, 1 brouillon), 7 PORTANCE actifs (2 oreillers, 3 taies, 2 bandelettes), stock 0 partout |
| Collections | 10, dont 5 héritées de LIYAN (tétines, biberons…) toujours en ligne |
| Langues | français **principal** ; en, de, es, it, nl publiées |
| Marchés | 6 : US, CA, UK, AU, Europe (32 pays, 6 langues), **Reste du monde = marché principal** et ne contient que FR/BE/LU |
| Devises par marché | US→USD, CA→CAD, UK→GBP, AU→AUD, EU→EUR + devises locales (CHF, DKK, SEK, PLN…) |
| Livraison (profil général, tarifs en EUR) | EU 4,90 (3–5 j, offert ≥ 60) · UK 5,90 (4–7 j, offert ≥ 60) · US 5,90 (5–8 j, offert ≥ 60) · CA 7,90 (6–10 j, offert ≥ 80) · AU 9,90 (7–12 j, offert ≥ 90) · reste du monde 14,90 (10–20 j) |
| Emplacement d'expédition | 1209 Mountain Road Pl NE, Albuquerque — expédie et exécute les commandes |
| Apps | Messaging, connecteurs ChatGPT et Claude, **AutoDS** (dropshipping, payante), **QSTOMY** |
| Domaine | liyan.shop (contrats IONOS d'après Gmail) — ne correspondra pas au nouveau nom |
| E-mail de contact | isaacpolignac@gmail.com — adresse personnelle |

### Correction sur mon propre travail

Le 1er septembre j'ai retiré la barre « livraison offerte » du panier en écrivant
qu'« aucun tarif n'est créé ». C'était faux : les tarifs existent dans le profil
d'expédition, ce sont les *pages* Livraison qui portaient des `[À COMPLÉTER]`.
Le retrait reste justifié — le seuil de 60 ne se convertissait pas d'un marché
à l'autre alors que le vrai seuil est 80 au Canada et 90 en Australie — mais le
motif était mal formulé. Les délais réels par zone sont ceux du tableau ci-dessus,
et ils serviront tels quels au brief (barre d'annonce, fiches, page Livraison),
sauf si tes fichiers en donnent d'autres.

## 3. Décisions prises seul

- **Même boutique, thème séparé.** Je travaillerai sur un duplicata non publié
  de Shrine (« [NOM] — build v1 »), et sur des produits en brouillon. Le thème
  LIYAN publié et les produits PORTANCE actifs ne sont pas touchés. → Règle 4.
- **Le système DA du brief remplace le registre bleu poudre.** Bone / Stone /
  Graphite / Clay, Fraunces + Inter, aucun dégradé : c'est l'inverse de ce que
  j'ai construit la semaine dernière pour PORTANCE. Ce travail reste sur le
  thème actuel ; le nouveau thème repart du Shrine d'origine. → Cohérence, règle 3.
- **Le marché principal devra passer à US** (aujourd'hui « Reste du monde »
  avec la France dedans) et **la langue principale à l'anglais** (aujourd'hui
  français). Les deux sont des réglages Admin que l'API ne modifie pas ; ils
  iront dans ta checklist de Phase 4. → Règle 6.
- **Forfait Advanced à questionner.** Rien dans le brief n'exige Advanced ; Basic
  suffit à un lancement et économise environ 360 $/mois. Décision à toi, je la
  note. → Règle 7.
- **AutoDS et QSTOMY** sont des apps payantes déjà installées. Je ne les touche
  pas ; je te demande si elles servent au nouveau projet. → Règle 7.
- Le nom « Aplomb » est **déjà un nom de produit** dans la boutique (Oreiller
  Aplomb). Ce n'est pas bloquant — un produit se renomme — mais Phase 1 en
  tiendra compte.

## 4. Ce qu'il me faut de toi — trois questions, toutes bloquantes

1. **Les fichiers.** Dépose-les dans le dépôt (`build/images/source/` pour le
   zip, `build/` pour le tableau des prix, dimensions et délais) ou envoie-les
   dans la conversation. Sans eux, Phase 0 reste ouverte et rien ne s'écrit.
2. **La boutique.** C'est bien `07beme-9h.myshopify.com` / liyan.shop, forfait
   Advanced ? C'est la seule à laquelle le connecteur est relié.
3. **PORTANCE.** Les oreillers et bandelettes font-ils partie de « le reste de
   la gamme » de la nouvelle marque, ou est-ce un projet séparé à archiver ?
   La réponse change la nomenclature (Seat 01, Lumbar 01… et quoi pour un
   oreiller ?), les collections et la navigation.

Les trois questions sur l'histoire du fondateur viendront en Phase 1, avec le nom.


---

# ▶ PHASE1_NOM

_Fichier : `build/PHASE1_NOM.md`_

# Phase 1 — Nom et brand core

Date : 10 septembre 2026. Aucune écriture dans Shopify.

> **Fermée le 10 septembre : SOMNILA validé par le fondateur.** Réponses aux
> trois questions : réveils douloureux le matin ; prix trop élevé, look
> d'hôpital, mauvaise qualité ; « la plupart des gens dorment mal ». Reprises
> dans `BRAND_BOOK.md` § 3, sans rien y ajouter.

## 1. Ce qui a été vérifié

**Domaines** — 36 candidats de deux syllabes passés au RDAP (registres
Verisign, .co, .store), redirections suivies :

| Candidat | .com | Note |
|---|---|---|
| **Aplomb** (brief, n° 1) | pris | `.co` libre, `.store` pris |
| Sedra, Kern, Ossa (brief) | pris | `.co` libres |
| Somna, Nocta, Dorma, Calmo, Somnia, Levea, Oreva, Nuvia, Lumeo, Alvea | pris | mots ou quasi-mots de 5 lettres |
| Aplom, Ploma, Plomba, Plombe, Somla, Somva, Nocla, Noctel, Noctal, Dormi, Dormel, Dormar, Nuca, Nucal, Posla, Serna, Osla, Silna, Talma, Morla, Somnu, Somnel, Somnar, Somtal, Calmi, Calmen, Sernel, Levia, Ovela, Plomi, Altena, Nuvela, Levena, Somvela | pris | noms forgés, 5 et 6 lettres |
| **Somnila** | **libre** (.com, .co, .store) | 3 syllabes |
| **Dormela** | **libre** (.com, .co, .store) | 3 syllabes |
| Nucaila, Alignisa | libres | 3–4 syllabes, réserves déjà documentées |

Conclusion nette : **un nom de deux syllabes avec son `.com` libre n'existe
plus**, ni en mot réel ni en nom forgé de cinq ou six lettres. Le critère
« deux syllabes » et le critère « .com libre » sont incompatibles en 2026. Il
faut en lâcher un. Le leader de la catégorie, Derila, a trois syllabes : c'est
le critère « deux syllabes » qu'on lâche.

**Marques** — les bases EUIPO, USPTO et TMview refusent les requêtes
automatisées depuis cet environnement (403, 405, 503). Les recherches web ne
remontent aucune marque de literie nommée Aplomb, Somnila ou Dormela. Deux
voisinages à signaler pour Somnila : **SOMNIA**, marque américaine de
préparations pharmaceutiques pour le sommeil (classe 5, NaturalCare
Pharmaceuticals), et « SLV Somnila », une référence de luminaire d'un fabricant
allemand (classe 11). Classes différentes des nôtres, mais à faire regarder.

**Réseaux** — Instagram renvoie une page de connexion et TikTok une page
générique quelle que soit la requête : non vérifiable d'ici. À faire à la main.

## 2. Recommandation : SOMNILA

| | Somnila | Dormela | Aplomb |
|---|---|---|---|
| Sens | *somnus*, le sommeil — lisible dans les six langues (somnolent, Somnologie, sonno) | *dormir*, lisible dans les langues latines ; « dorm » ≈ dortoir en anglais et allemand | équilibre, assurance — parle aux francophones et aux anglophones lettrés, pas aux autres |
| Prononciation | som-NI-la, identique partout | dor-ME-la, identique partout | a-PLOM ; le « b » muet piège l'allemand, l'espagnol, l'italien |
| Registre | clinique sans promesse, comme demandé au départ | doux, proche de la catégorie | design, posture — pensé pour un coussin d'assise, pas pour le sommeil |
| `.com` | **libre** | **libre** | **pris** — vivre sur `.co` avec le `.com` chez un tiers, c'est laisser fuir une partie du trafic pour toujours |
| Risque | voisinage SOMNIA (pharma) à faire vérifier | **rime avec Derila** : même rythme, même finale -la — on aura l'air de la copie du leader | mot courant, déjà porté par des cabinets et boutiques sans rapport |
| Verdict | **retenu** | second choix | écarté, sauf si tu tiens au nom et acceptes le `.co` |

Somnila coche tout ce que le brief demande sauf le nombre de syllabes, et le
brief lui-même prend pour référence une marque de trois syllabes.

## 3. Ce que le nom déclenche — à faire à la main avant tout dépôt

1. **Recherche d'antériorité** sur le nom retenu, classes **20** (oreillers,
   coussins), **24** (couvertures, linge), **35** (vente au détail) :
   - EUIPO eSearch plus : https://euipo.europa.eu/eSearch/
   - USPTO Trademark Search : https://tmsearch.uspto.gov/
   - UK IPO : https://www.gov.uk/search-for-trademark
   - IP Australia : https://search.ipaustralia.gov.au/trademarks/search/quick
   - INPI (France) : https://data.inpi.fr/
   Un nom identique ou très proche dans ces classes = on passe au suivant.
2. **Réserver** `somnila.com` (puis `.co` et `.store` en protection) — je ne
   manipule pas d'achat, règle 4.
3. **Réserver** `@somnila` sur Instagram et TikTok.

## 4. Brand core — transposé à la gamme réelle (sommeil)

Le brief a été écrit pour un coussin d'assise. Voici la même colonne
vertébrale, portée sur des oreillers. Rien d'autre ne change : palette, typo,
lumière, faceless, zéro promesse médicale.

- **Positionnement** : Somnila fait du soutien nocturne un objet de design —
  la tenue d'un fauteuil de designer, dans un oreiller.
- **Promesse** : *Feel it tonight. Keep it for years.*
- **Valeurs** : Précision (chaque courbe, hauteur et densité a une raison
  anatomique) · Retenue (un oreiller qui disparaît dans la chambre, aucun
  gadget) · Durabilité (mousse qui tient, housse lavable incluse, essai
  30 nuits — l'inverse du confort jetable).
- **Archétype** : Créateur en principal, Protecteur en secondaire. Persona
  faceless : « l'artisan silencieux » — mains, atelier, chambre au petit
  matin, voix off à la première personne.
- **Ennemi** : l'oreiller « orthopédique » bleu qui crie « j'ai mal au cou »,
  le bloc de mousse à 15 $ qui s'écrase en trois mois, et le **faux « −50 %
  » permanent** du leader.
- **Taglines** : *Sleep well.* (signature, miroir de *Sit well.*) ·
  *Support, redesigned.* (pubs) · *Somnila. Held all night.* (accroche).
- **Ton** : phrases courtes, verbes physiques (sink, hold, cradle, lift),
  chiffres concrets (hauteur, dimensions, poids), calme, première personne du
  fondateur. Jamais *orthopedic, cervical pain, relief, treats, doctor
  recommended*. Le mot « cervical » lui-même sort du vocabulaire client : on
  dit *neck*.

**Nomenclature — objets de design, par fonction** (les noms fournisseur
Derila, Cloudii, Snuggi n'apparaissent nulle part) :

| Réf. devis | Nom de marque | Pourquoi |
|---|---|---|
| 09 oreiller cervical — héros | **Neck 01** | la fonction, sans le mot médical |
| 12 oreiller contour | **Contour 01** | la forme |
| 10 oreiller latéral | **Side 01** | la position |
| 11 oreiller corporel en S | **Body 01** | l'objet |
| 01 oreiller de lecture au lit | **Lounge 01** | l'usage — pas « phone pillow » |
| 02 couverture | **Throw 01** | l'objet de design, pas « blanket » |
| 03 masque | **Mask 01** | |
| 04 bouchons | **Quiet 01** | l'effet, sans décibels annoncés |
| 05–08 housses de rechange | **Cover — Neck / Contour / Side / Body** | |
| Packs | **Neck 01 + Cover** · **Sleep Set** · **For Two** · **Side-Sleeper Set** · **Family Set** · **Evening Set** · **Quiet Night** | |

**Coloris** : seuls ceux de l'annexe photos, nommés par la matière quand la
correspondance est honnête — blanc → *Bone*, gris → *Stone*, bleu marine →
*Ink*, bleu clair → *Sky*, rose → *Blush*. Pas de *Clay* ni d'*Olive* sur un
produit qui n'existe pas dans cette teinte.

## 5. Trois questions pour l'histoire du fondateur

L'About et le persona faceless en dépendent ; rien ne sera inventé.

1. **Le déclic.** Quelle nuit, ou quel matin, t'a fait chercher un oreiller
   comme celui-là ? Un moment précis, pas une généralité.
2. **L'agacement.** Dans ce qui se vendait déjà, qu'est-ce qui t'a le plus
   énervé : le look d'hôpital, le « −50 % » permanent, la mousse qui
   s'affaisse, autre chose ?
3. **Un détail vrai.** Un objet, un chiffre, un lieu, une habitude — quelque
   chose de concret et vérifiable de ta vie qui peut ancrer la page About
   (où tu dors, ce que tu as essayé, combien d'oreillers tu as jetés…).

## 6. Ce qu'il te faut décider pour fermer la Phase 1

- **Le nom** : Somnila (recommandé), Dormela, ou Aplomb sur `.co`.
- **Les recherches d'antériorité** ci-dessus, sur le nom retenu — je ne peux
  pas les faire d'ici, et déposer sans les faire serait une faute.
- **Les trois réponses** sur ton histoire.

Dès le nom validé : Phase 2, identité visuelle (wordmark Fraunces, système DA,
BRAND_BOOK.md).


---

# ▶ PHASE3

_Fichier : `build/PHASE3.md`_

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


---

# ▶ PHASE4

_Fichier : `build/PHASE4.md`_

# Phase 4 — Thème Shrine et structure du site

Date : 10 septembre 2026. Thème de travail : **« Somnila — build v1 »**
(`gid://shopify/OnlineStoreTheme/157447585949`), **non publié**. Le thème
LIYAN publié, le thème PORTANCE et les produits PORTANCE actifs n'ont pas
été touchés. Rien supprimé (sauf une collection vide que j'avais créée par
erreur en Phase 3, voir décisions), rien publié, aucun email envoyé.

## 1. Fait

**Thème.** Shrine PRO dupliqué en « Somnila — build v1 » par l'API, puis
15 fichiers réécrits (réglages, en-tête, pied, 12 gabarits). Les fichiers
font foi dans le dépôt : `build/theme/`.

- **Réglages globaux** (`config/settings_data.json`) : palette Cloud
  `#F7F9FC` / Mist `#DCE8F2` / Night `#1E2A3A` / Slate `#6B7D90`, Dawn
  `#F0B79B` réservé au halo, au liseré et au bandeau ; boutons en pastille,
  champs 22 px, cartes et médias 28 px, ombres teintées Night 10 % ; logo
  final (`somnila-logo-light.png`), favicon, jeton de licence Shrine
  conservé tel quel ; badges promo et compte à rebours désactivés ; tiroir
  panier en anglais sans minuteur.
- **Polices** : Fraunces Soft (instance SOFT 100, axes opsz + graisse) et
  Manrope, sous-ensemble latin en woff2 (73 + 28 Ko), hébergées dans
  Fichiers Shopify et injectées par une section `custom-liquid` du groupe
  d'en-tête (`somnila-styles`) qui redéfinit les variables de police du
  thème. Aucune police Shopify chargée en plus.
- **En-tête** : barre d'annonce à 3 messages réels (livraison offerte sur
  chaque oreiller · 6–10 jours suivis · essai 30 nuits), logo à gauche, menu
  `somnila-main` à 4 entrées (Shop ▾, Neck 01, Our story, Help), recherche,
  panier tiroir.
- **Accueil** (`templates/index.json`) : hero (image mère provisoire, titre
  *Sleep well.*, une phrase, CTA *Shop Neck 01*) → bandeau confiance à 4
  tuiles (chiffres réels) → Neck 01 en produit vedette avec achat direct →
  *Why it holds* en 3 bénéfices → matières et photo sur lit → gamme des 5
  oreillers → avis **désactivés** (blocs de garde, jamais de faux avis) →
  FAQ 5 questions → packs → newsletter.
- **Fiches produit** : 3 gabarits. `product.json` (oreillers) : galerie,
  titre, 3 puces, prix, pastilles de couleur nommées, ajout *Complete the
  night* (Mask 01, Quiet 01), bouton d'ajout, badges de paiement, date de
  livraison estimée (6–10 jours), réassurance, description, **tableau des
  dimensions cm + in et poids lu dans les metafields** (bloc Liquid),
  accordéons essai 30 nuits / livraison / entretien, bouton sticky ; puis
  3 bénéfices, bandeau « Thirty nights to decide », FAQ, produits liés.
  `product.set.json` (packs : deux sélecteurs, contenu du pack) et
  `product.accessory.json` (accessoires : retours 14 jours, pas d'essai
  30 nuits). Les 20 produits pointent vers le bon gabarit.
- **Collection, panier, pages, 404, recherche** : gabarits propres, en
  anglais, sans filtre inutile ; page contact avec formulaire (nom, email,
  numéro de commande, message).
- **Pages créées** (publiées, en anglais, titre et meta description SEO) :
  `/pages/about` (histoire du fondateur, 1re personne, sans promesse
  médicale), `/pages/shipping-delivery`, `/pages/returns-warranty`,
  `/pages/faq`, `/pages/contact`. Textes dans `build/pages/`.
- **Menus Somnila** créés à part (les menus PORTANCE du live restent
  intacts) : `somnila-main`, `somnila-shop`, `somnila-help`, `somnila-legal`.
- **Collections** : `memory-foam-pillows` (5), `sets` (8), `accessories` (3), `covers`
  (4), `shop-all` (20). Aucune publiée sur un canal.
- **Livraison** : profil d'expédition **« Somnila »** séparé, 138 variantes,
  6 zones (US, CA, UK, Europe 29 pays, AU, reste du monde), 6–10 jours
  partout, **offert dès 54,90 €**, sinon 4,90 / 5,90 / 5,90 / 7,90 / 9,90 €
  et 14,90 € reste du monde. Le profil général (PORTANCE) n'est pas modifié.
- **Prix** : un seul catalogue, conversion automatique par Markets
  (ta décision) ; la ligne livraison des 20 descriptions est devenue
  « Ships in 6–10 days. Free shipping. » (accessoires : « … Free shipping
  on orders from €54.90. »).
- **Maquettes** : canevas de design (accueil desktop, accueil mobile, fiche
  Neck 01) avec les vrais textes, prix et images —
  https://claude.ai/code/artifact/aa518baf-804a-4a9a-8835-7b4bb9ed2e1f.
  Sources dans `build/design/`.
- **Politiques** rédigées en anglais dans `build/pages/policies/`
  (remboursement, livraison, CGV, confidentialité) avec les champs légaux
  entre crochets — **non écrites dans Shopify** (elles remplaceraient les
  politiques du live).
- **Vérification** : aperçu rendu en navigateur (relais réseau, captures
  dans `build/preview/`) sur l'accueil desktop et mobile, la collection, les
  pages About / FAQ / Contact, le panier et trois fiches (Neck 01, Sleep Set,
  Mask 01, via le lien d'aperçu produit de l'admin). Polices Somnila Serif /
  Sans chargées, palette et logo en place, aucune erreur Liquid sur les
  fiches, tableau des dimensions cm + in + kg/lb lu dans les metafields.
  Pour voir l'aperçu : Boutique en ligne → Thèmes → « Somnila — build v1 »
  → Aperçu, ou `https://liyan.shop/?preview_theme_id=157447585949`.

### 1 bis. Passe design du 10 septembre au soir (après ton retour « moche, mal aligné »)

Tout est dans le thème « Somnila — build v1 » et dans `build/theme/`.

- **Hero v2** : coussin détouré plus grand (78 % de la largeur), halo Dawn
  plus doux, texte à gauche sur 56 rem, titre *Sleep well.* en 5,2–9,6 rem
  selon l'écran. Version mobile 4:5 dédiée.
- **Typographie** : titres de section sur une seule échelle (3,8 rem),
  titre produit 3,6 rem ; tuiles de confiance, cartes produit, accordéons,
  en-têtes du pied de page et icônes de réassurance en Manrope 500/600 (le
  serif reste pour les titres) ; en-têtes de colonnes du pied en capitales
  espacées ; boutons pleine largeur à 5,4 rem.
- **Alignements** : FAQ centrée et élargie (96 rem), gamme des 5 oreillers
  sur 5 colonnes fixes sans carrousel, packs sur 4, tuiles sur 4, bouton
  sticky « Add to cart », section matières image à gauche / texte à droite
  sans chevauchement.
- **Image de la section matières** : le packshot fournisseur avait un fond
  lavande hors charte ; Contour 01 Night est maintenant détouré et posé sur
  le ciel Cloud → Mist Somnila (`somnila_contour-01_materials_1x1_v1.jpg`,
  source dans `build/images/site/`).
- **Fiches produit** : les 4 puces de la description faisaient doublon
  avec le tableau Dimensions / Materials / Included / Delivery lu dans les
  metafields ; les 20 descriptions gardent leurs deux paragraphes et
  perdent les puces (`build/shopify/products.json` mis à jour).
- **Galerie Contour 01** : l'image « packshot-stone-9 » était en fait un
  masque de sommeil gris mal nommé chez le fournisseur ; retirée de la
  galerie (le fichier reste dans le dépôt).
- **Vérifié** dans le navigateur après chaque envoi : accueil desktop et
  mobile, collection, Neck 01 desktop et mobile (captures dans
  `build/preview/`). À savoir : le lien *Aperçu* d'un produit en brouillon
  (`preview_key`) change à chaque modification du produit, et l'ancien lien
  continue d'afficher l'ancienne version — toujours reprendre le lien depuis
  la fiche dans l'admin.

**Ce que l'aperçu montre encore et qui ne dépend pas du thème :**

- les cartes « Example product title », le « Sold out $19.99 » et l'erreur
  Liquid du produit vedette sur l'accueil, le « 0 products » de la
  collection : ce sont les **produits en brouillon**, invisibles dans
  l'aperçu public ; l'accueil sera complet dès qu'ils seront actifs
  (mot de passe boutique d'abord, voir § 3) ;
- la bannière « Cookie consent » grise : c'est la bannière native de
  Shopify (Paramètres → Confidentialité des clients), réglage boutique
  hors thème, active sur le live ; ses couleurs se règlent au même endroit ;
- les vignettes de Neck 01 avec « 蓝 » / « 灰 », les packshots Contour 01
  avec faux badges (« Top Rated Pillow », « Chiropractor approved », « Best
  pillow 2025 » : promesse médicale et récompenses inventées, contraires aux
  règles 1 et 2) et le packshot bleu de Side 01 annoté en chinois : photos
  fournisseur gardées en Phase 3 sur ta consigne ; je recommande de les
  retirer des galeries (il reste 3 à 5 photos propres par produit). Un
  « ok » suffit.

## 2. Décisions prises

- **Aperçu et produits en brouillon.** Les produits restent en brouillon,
  donc invisibles dans l'aperçu public du thème : l'accueil affiche ses
  sections mais les blocs produit sont vides tant qu'ils ne sont pas actifs.
  Les fiches se prévisualisent une à une depuis l'admin (bouton *Aperçu*
  du produit). Pour un aperçu complet avant mise en ligne, le chemin propre
  est : mot de passe boutique activé (toi), puis produits en actif (moi).
- **Photos des packs** : les galeries des packs reprennent les packshots
  des produits qui les composent ; celle du Sleep Set contient la photo
  fournisseur des bouchons avec du texte chinois sur l'emballage (accepté
  en Phase 0, mais hors charte). À remplacer en Phase 5.
- **Hero provisoire** : le packshot fournisseur de Neck 01 détouré et posé
  sur le ciel Cloud → Mist avec halo Dawn, faute de crédits de génération.
  Phase 5 le remplace par l'image mère validée.
- **Pastilles de couleur** : liste nominative globale (Night, Cloud, Stone,
  Sky, Blush…) avec des teintes approchées pour l'interface ; les noms de
  coloris restent ceux des produits.
- **Collection des oreillers** : la première tentative de Phase 3 avait
  bien créé une collection `pillows` malgré l'erreur affichée ; la
  collection provisoire `somnila-pillows` (créée par moi, vide après
  transfert) a été supprimée, et la collection définitive porte le handle
  `memory-foam-pillows` (voir collision d'URL ci-dessous).
- **Traductions héritées retirées.** Le duplicata avait copié les
  traductions PORTANCE du thème (en, de, es, it, nl : 270 clés × 5 langues)
  qui **écrasaient mes textes** dans l'aperçu (barre d'annonce, puces,
  FAQ, pied de page). Je les ai supprimées sur le thème Somnila uniquement ;
  le thème PORTANCE garde les siennes.
- **Collision d'URL `/collections/pillows`.** En langue anglaise, cette
  adresse renvoyait vers la collection PORTANCE « Oreillers » (son handle
  traduit en anglais est `pillows`). Plutôt que de toucher à PORTANCE, la
  collection Somnila s'appelle maintenant **`memory-foam-pillows`**
  (`/collections/memory-foam-pillows`) ; menus, hero, section matières et
  404 pointent dessus. Rien à faire de ton côté.
- **Sélecteur de langue masqué** dans le pied (boutique 100 % anglais) ;
  les 5 locales PORTANCE existent toujours au niveau boutique (voir § 3).
- **Fichiers de contexte de marché** (`*.context.international.json`) : le
  connecteur refuse toute suppression de fichier de thème ; ils sont vides
  (`"sections": {}`) et sans effet.
- **Délai de réponse au contact** : « usually within one to two business
  days » sur la page Contact — engagement opérationnel à confirmer.
- **Retours accessoires** : 14 jours, non utilisés, dans l'emballage — règle
  standard posée faute de consigne ; à confirmer.

## 3. Ce qu'il me faut de toi

1. **« ok » pour la Phase 5** (visuels : image mère du hero, packshots,
   lifestyle, éditorial, pubs, UGC faceless, header email).
2. **Un seul « ok » pour trois écritures côté boutique** que la règle 4
   m'interdit sans toi, parce qu'elles touchent le live :
   politiques (Paramètres → Politiques, textes dans `build/pages/policies/`),
   branding du checkout (logo, Night / Cloud, Manrope), retrait des 5
   langues PORTANCE (de, es, fr, it, nl) pour une boutique 100 % anglais.
3. **Aperçu complet** : si tu veux voir l'accueil avec les produits,
   active le mot de passe de la boutique (Boutique en ligne → Préférences)
   et dis-le-moi : je passe les 20 produits en actif, ils restent invisibles
   du public. C'est la seule façon de juger l'accueil et la collection tels
   qu'ils seront.
4. **« ok » pour retirer des galeries** les photos fournisseur à faux
   badges (Contour 01), à texte chinois (Neck 01 Night vue 3, Side 01 Blue)
   et l'emballage des bouchons dans le Sleep Set.
5. **Checklist manuelle** (elle ne bouge pas) : Shopify Payments / PayPal,
   domaine `somnila.com`, marché principal = États-Unis et langue principale
   = anglais (Paramètres → Marchés / Langues), pixels Meta / GA4 / TikTok,
   adresse d'expéditeur `hello@somnila.com` (ou autre) dans Paramètres →
   Notifications, réseaux sociaux (liens à me donner), publication du thème,
   retrait du mot de passe. Détail dans `HANDOFF.md` en Phase 7.

## 4. Suite du 11 septembre — après ton « mdp : … , ok, ok »

**Fait.**

- **Mot de passe boutique** vérifié actif (liyan.shop renvoie vers /password).
  Les **20 produits sont passés en actif** et publiés sur le canal Boutique en
  ligne avec les 5 collections : l'accueil, la collection et les fiches se
  rendent maintenant complets derrière le mot de passe (captures dans
  `build/preview/`). Le public ne voit rien.
- **Photos fournisseur nettoyées** (script `build/images/clean-supplier-photos.py`,
  fichiers `_v2` dans `build/images/shopify/`) : faux badges effacés sur les
  5 packshots Contour 01 ; caractères « 蓝 » / « 灰 » effacés sur Neck 01 ;
  étiquettes couleur et cotes 10/60/33 cm effacées sur les 3 packshots
  Side 01 ; bouchons Quiet 01 recadrés sur l'étui, surimpressions et marque
  « iMeBoBo » retirées. 21 médias remplacés dans les galeries de Contour 01,
  Neck 01, Side 01, Quiet 01, Sleep Set, Quiet Night, Contour for Two,
  Side-Sleeper Set, Family Set, Cover Side, Cover Contour ; ordre conservé.
  Retirée aussi : la 3e photo de Side 01 (« dark grey, side view »), qui
  montrait un traversin lisse bleu clair, pas Side 01.
- **Pastilles de couleur** du produit vedette de l'accueil : elles étaient
  vides (réglage « image_alt ») ; passées sur la liste nominative, comme la
  fiche.
- **Langues** : de, es, it, nl **dépubliées** (réversible, traductions
  conservées). `fr` reste la langue principale : l'API ne permet pas de la
  changer, c'est manuel (voir plus bas). `en` reste publié.

**Bloqué côté API, à faire à la main (5 minutes).**

1. **Politiques** : le connecteur n'a pas le droit `write_legal_policies`.
   Paramètres → Politiques : colle les 4 textes de `build/pages/policies/`
   (refund, shipping, terms, privacy) et remplace les champs entre crochets :
   raison sociale, forme juridique, adresse, numéro d'immatriculation,
   numéro de TVA, pays du siège, email de contact. Seule la politique de
   confidentialité existait (modèle Shopify en français), les trois autres
   étaient vides.
2. **Branding du checkout** : l'API `checkoutBranding` est réservée aux
   plans Plus. Paramètres → Paiement → Personnaliser : logo
   `somnila-logo-light.png`, fond `#F7F9FC`, texte `#1E2A3A`, boutons
   `#1E2A3A` / texte `#F7F9FC`, police Manrope si la bibliothèque la propose,
   sinon la police système.
3. **Langue principale** fr → en : Paramètres → Langues → « Modifier la
   langue par défaut ». Ensuite je peux supprimer `fr` si tu veux.

**Phase 5 démarre** (tu as dit ok). Crédits Higgsfield disponibles : 0,2,
donc aucune génération d'image possible sans recharge ; je pars sur le
compositing à partir des photos fournisseur nettoyées (gratuit) : packshots
sur ciel Somnila, hero définitif, bannières, visuels pubs, en-tête email.
Les vidéos UGC sans visage attendront une décision sur les crédits.


---

# ▶ PHASE5

_Fichier : `build/PHASE5.md`_

# Phase 5 — Visuels

Date : 11 septembre 2026. Tout est composé à partir des photos fournisseur
nettoyées, sans génération d'image (0,2 crédit Higgsfield disponible, aucun
achat sans ton accord), sans visage, dans la charte Somnila (Cloud, Mist,
Night, Dawn ; Fraunces Soft, Manrope). Sources et scripts dans
`build/images/site/`.

## 1. Fait

- **Packshots sur ciel Somnila** (`packshots/`, 29 visuels en 1:1 1200 px et
  4:5 1200×1500) : Neck 01 ×4, Contour 01 ×6, Side 01 ×2, Lounge 01 ×2, les
  3 housses, les 7 packs qui reprennent ces oreillers. Détourage par
  estimation du fond + GrabCut, ombre du fournisseur conservée et teintée,
  pose sur le dégradé Cloud → Mist avec halo Dawn (`sky-packshots.py`).
  **Posés dans les galeries Shopify** à la place des packshots fournisseur
  (14 produits, ordre conservé, textes alternatifs repris). Restent en photo
  fournisseur nettoyée : Side 01 gris foncé (cotes trop proches du produit),
  Mask 01, Quiet 01, Body 01 (photos sur lit ou sur forme de présentation,
  pas détourables proprement), et les 3 photos « sur lit » de Contour 01.
- **Galeries corrigées au passage** : Body 01 perdait une photo « Ice » qui
  montrait un autre produit avec des cotes en chinois ; Lounge 01 bleu
  débarrassé de son texte « MULTICOLOURED / 美学设计 » ; Side 01 gris foncé
  renettoyé.
- **Bannières de collection** (`banners/`, 2400×800) : Pillows, Sets,
  Accessories, Covers, Everything. Posées comme image de chaque collection
  (listes, partage) ; le gabarit collection n'affiche pas l'image en bannière
  pour ne pas doubler le titre.
- **Pubs statiques** (`ads/`, 1080 en 1:1, 4:5 et 9:16) : trois messages,
  tous réels — *Sleep well.* (Neck 01), *Thirty nights to decide.*, *Two
  heights, one pillow.* — avec la ligne « Free shipping · 30-night trial ·
  Ships in 6–10 days ». Pas de prix dans les pubs : ils sont convertis par
  marché.
- **Email** (`email/`) : en-tête 1200×400 (dans Fichiers Shopify) et pied
  1200×300 sur fond Night.
- **Réseaux** (`social/`) : avatar 1024 (lune Dawn sur Night), couverture
  1500×500, image de partage 1200×630 (dans Fichiers Shopify).
- **Hero** : la v2 de la Phase 4 reste l'image mère (même famille visuelle
  que les packshots).
- Vérifié dans le navigateur derrière le mot de passe : accueil, collection
  oreillers, collection packs, fiches Neck 01 et Contour 01.

## 2. Décisions prises

- **Compositing seulement.** Sans crédits de génération, pas de scènes
  lifestyle ni d'UGC vidéo : les seules photos « sur lit » sont celles du
  fournisseur pour Contour 01 (posters et peluche dans le décor), gardées en
  fin de galerie faute de mieux.
- **Throw 01** (la couverture effet fourrure, 200 × 230 cm) : ses 10 photos
  du zip montrent une mannequin dans un intérieur de stock, donc écartées en
  Phase 3 (aucun visage). Elles sont maintenant **recadrées sur la
  couverture seule** (bas de l'image, 1200×900, un peu douces : source
  700 px) et posées dans la fiche, un détail par coloris. L'Evening Set
  reçoit le détail Cream en 2e image.
- **Mask 01** : les photos fournisseur montrent le masque sur une forme
  blanche ; gardées telles quelles, sans détourage.
- Les fichiers `_v1` d'origine restent dans `build/images/shopify/` ; rien
  n'est perdu.

## 3. Ce qu'il me faut de toi

1. Si tu as de meilleures photos de la couverture (à plat, sans personne),
   elles remplaceront les détails recadrés ; sinon ça tient.
2. **Crédits de génération** (Higgsfield ou autre) si tu veux des scènes
   lifestyle et des UGC sans visage ; sinon on reste sur ces visuels.
3. Toujours en attente de la Phase 4 : politiques à coller (champs entre
   crochets à remplir), branding du checkout, langue principale → anglais.
4. **Shopify Email** : importer `email/somnila_email_header_1200x400.jpg` et
   le pied dans le modèle (Marketing → Shopify Email → modèle de marque).
5. **« ok » pour la Phase 6** (kit de lancement : emails, textes pubs, plan
   de lancement, réseaux).


---

# ▶ PHASE6

_Fichier : `build/PHASE6.md`_

# Phase 6 — Kit de lancement

Date : 11 septembre 2026. Tout le contenu client est en anglais, dans la
voix du brand book (phrases courtes, chiffres réels, aucune promesse
médicale, pas de fausse urgence). Les prix cités sont les prix EUR de la
grille, convertis par marché au paiement. Dossier : `build/launch/`.

## 1. Fait

- **`EMAILS.md`** — série de bienvenue en trois notes (ce qu'on fait, quel
  oreiller est le vôtre, comment marchent les trente nuits), panier abandonné
  (un seul email, sans remise), trois lignes à modifier dans les notifications
  Shopify, note post-achat à J+12, demande d'avis à J+21 sans contrepartie.
  En-tête et pied d'email dans `build/images/site/email/`.
- **`ADS.md`** — Meta : quatre concepts (Sleep well · Thirty nights · Two
  heights · Sets) avec textes courts, moyens, longs, titres et descriptions,
  structure de campagne et règles d'arrêt calées sur `PRIX.md` (seuil de
  rentabilité ≈ 39 € par commande sur Neck 01). TikTok : trois textes.
  Google : 15 titres, 4 descriptions, mots-clés et exclusions, notes
  Shopping. Checklist de conformité avant diffusion.
- **`SOCIAL.md`** — bios Instagram / TikTok / Pinterest / Facebook, cadence,
  les douze premiers posts avec visuel et légende, quatre scripts vidéo sans
  visage (la pression de la mousse, la housse, le matin, les trente nuits),
  cinq réponses types.
- **`PLAN.md`** — checklist avant J0 (boutique, suivi, contenu,
  fournisseur), calendrier J−14 → J+30, indicateurs et règles de décision,
  cinq réponses de service client, ce qui est volontairement exclu.
- **Blog « Notes from the workshop »** créé dans Shopify (`/blogs/notes`)
  avec trois articles **en brouillon** : *Which height should I choose?*,
  *How the thirty-night trial works*, *The cover: unzip, wash, put back*.
  Même contenu que les fiches et la FAQ, développé ; rien d'inventé.

## 2. Décisions prises

- **Pas de prix dans les publicités** : ils sont convertis par marché, un
  prix fixe dans l'image serait faux quelque part.
- **La publicité ne pousse que Neck 01, Body 01 et les packs**, jamais un
  accessoire seul : règle de `PRIX.md`, un masque ou des bouchons en
  première commande perdent de l'argent.
- **Pas de remise de lancement écrite** : proposée en option
  (`EMAILS.md` § 6, WELCOME10 à 10 % sur la première commande, oreillers et
  packs) ; créée seulement sur ton « ok ».
- **Un seul email de panier abandonné**, sans remise, fidèle à « pas de
  fausse urgence ».
- **Pas d'influence ni d'app payante en mois un** : les premiers avis
  viennent de clients payants.

## 3. Ce qu'il me faut de toi

1. **Lire les trois articles** dans Boutique en ligne → Articles de blog et
   les publier (ou me dire quoi changer).
2. **« ok » ou « non » pour WELCOME10.**
3. **Adresse email d'expéditeur** (`hello@somnila.com` ou autre) : elle
   entre dans les emails, les politiques et les réponses.
4. Toujours ouverts : politiques à coller, branding du checkout, langue
   principale, crédits de génération pour les vidéos.
5. **« ok » pour la Phase 7** (QA complète et handoff : `HANDOFF.md` avec la
   checklist manuelle finale, vérification de chaque page et de chaque
   fiche, tests de commande, publication du thème sur ton signal).


---

# ▶ PHASE7

_Fichier : `build/PHASE7.md`_

# Phase 7 — QA et passation

Date : 11 septembre 2026. La liste de ce qui reste à faire à la main est
dans `build/HANDOFF.md` ; ce rapport dit ce qui a été vérifié et corrigé.

## 1. Vérifié

- **41 URL parcourues** derrière le mot de passe, thème « Somnila — build
  v1 » : accueil, 5 collections, la liste des collections, 20 fiches,
  5 pages, panier, recherche, blog, 404, 4 politiques. Pour chacune :
  statut HTTP, titre, méta-description, H1, erreurs Liquid, résidus de
  français, noms de marques tierces, caractères chinois, images
  manquantes. Résultat : aucune erreur Liquid, aucun résidu français ni
  caractère chinois, aucune image manquante, un H1 par page, une
  méta-description sur chaque fiche, collection et page.
- **59 liens internes testés** : aucun lien Somnila cassé. Les 404 restants
  sont les trois politiques que tu n'as pas encore collées (refund,
  shipping, terms).
- **Parcours d'achat** : ajout au panier de Neck 01 (Night), page panier
  avec l'article, la quantité et le total, tiroir panier, bouton de
  paiement (voir correction ci-dessous). Le paiement lui-même attend
  Shopify Payments.
- **Rendu** desktop et mobile de l'accueil, du panier, de la page À propos ;
  desktop des pages Contact, FAQ, Livraison, Retours, de la liste des
  collections. Captures dans `build/preview/`.
- **Contenus** : titres SEO et descriptions des 20 fiches présents ; textes
  alternatifs sur toutes les images ; gabarits blog et article passés sur
  la newsletter Somnila (ils citaient « exclusive offers »).

## 2. Corrigé pendant la QA

- **Page panier sans bouton de paiement** : la section pied de panier
  existait sans ses blocs. Blocs *subtotal* et *buttons* ajoutés ; la page
  affiche maintenant le sous-total et le bouton Check out.
- **Accueil sans H1** : le hero du thème rend un H2. Un H1 masqué
  visuellement (« Somnila memory-foam pillows shaped around the way you
  actually lie ») est injecté sur l'accueil seulement.
- **Page Contact** : l'adresse `support@somnila.com` est écrite dans le
  texte, à côté du formulaire. Même adresse dans les 4 politiques, le kit
  emails et le plan.
- **Titres d'onglet** en double (« … | Somnila – SOMNILA ») : cause = le nom
  de boutique en capitales. Se règle en renommant la boutique « Somnila »
  (§ HANDOFF, point 1).

## 3. Ce que la QA a trouvé et qui dépend de toi

- **L'accueil porte encore le titre « PORTANCE — The art of sleep »** :
  réglage boutique (Préférences → titre et méta-description), texte proposé
  dans `HANDOFF.md`.
- **L'ancien catalogue est visible** dans la recherche (32 résultats pour
  « pillow », dont les taies Appui) et sur `/collections` (Biberons,
  Tétines, Ancienne gamme, Page d'accueil…) : 7 produits PORTANCE actifs et
  10 anciennes collections publiées. Sur ton « ok » je les retire du canal
  Boutique en ligne, sans rien supprimer.
- **Politiques**, **checkout**, **langue par défaut**, **paiements**,
  **domaine**, **pixels** : liste ordonnée dans `HANDOFF.md`.
- **Bannière cookies** grise de Shopify : ses couleurs se règlent dans
  Paramètres → Confidentialité des clients.

## 4. Ce qu'il me faut de toi

1. **« ok »** pour retirer les 7 produits PORTANCE et les 10 anciennes
   collections du canal Boutique en ligne.
2. Renommer la boutique **Somnila** et poser le titre de l'accueil (deux
   minutes, dans l'admin).
3. Les points 2 à 16 de `HANDOFF.md`, dans l'ordre ; le thème se publie en
   dernier, quand tout le reste est fait.




# ══════ PARTIE 5 — MARQUE, PRIX, PROMPTS ══════


---

# ▶ BRAND_BOOK

_Fichier : `build/BRAND_BOOK.md`_

# SOMNILA — Brand book

Version 2, 10 septembre 2026. Ce document prime sur tout autre texte de marque.

## 1. Le nom

**Somnila** — som-NI-la. Racine *somnus*, le sommeil en latin, lisible dans
les six langues de la boutique (somnolent, Somnologie, sonno, somnífero).
Trois syllabes, consonne-voyelle en alternance, finale -la : le registre
d'une marque de catégorie, pas d'un gadget. Évoque le sommeil sans annoncer
d'effet. `somnila.com`, `.co`, `.store` libres au 10 septembre 2026 ;
recherche d'antériorité classes 20, 24, 35 à faire avant dépôt.

S'écrit **Somnila** en texte courant, **somnila** en bas de casse dans le
wordmark uniquement. Jamais en capitales.

## 2. Brand core

- **Positionnement** — Somnila fait du soutien nocturne un objet de design :
  la tenue d'un fauteuil de designer, dans un oreiller.
- **Promesse** — *Feel it tonight. Keep it for years.*
- **Valeurs** — Précision (chaque courbe, hauteur et densité a une raison
  anatomique) · Retenue (un oreiller qui disparaît dans la chambre, aucun
  gadget) · Durabilité (mousse qui tient, housse lavable incluse, essai
  30 nuits — l'inverse du confort jetable).
- **Archétype** — Créateur, avec le Protecteur en secondaire. Persona
  faceless du fondateur : « l'artisan silencieux » — mains, chambre au petit
  matin, atelier, voix off à la première personne.
- **Ennemi** — l'oreiller « orthopédique » bleu qui crie « j'ai mal au cou »,
  le bloc de mousse à 15 $ qui s'écrase en trois mois, et le faux « −50 % »
  permanent.
- **Taglines** — *Sleep well.* (signature) · *Support, redesigned.* (publicité)
  · *Held all night.* (accroche produit).

## 3. L'histoire du fondateur — ce qui est vrai, et rien d'autre

Trois réponses, données le 10 septembre : des matins avec des réveils
douloureux ; ce qui agaçait dans l'offre — le prix trop élevé, le look
d'hôpital, la mauvaise qualité ; et une conviction : la plupart des gens
dorment mal.

Ce que l'About peut dire, à la première personne, sans promesse médicale (on
raconte un vécu, on ne prescrit rien) :

```
I kept waking up stiff.

Not every morning. Enough of them. I went looking for a pillow I would
actually want to keep, and found three kinds: the blue hospital kind, the
overpriced kind, and the kind that goes flat in three months. Sometimes all
three at once.

Most people sleep badly and accept it. I didn't want to.

So I built the pillow I was looking for. Shaped around the way a body
actually lies, made of foam that holds, with a cover you can wash. Priced
like an object you keep, not a gadget you replace.

Try it for thirty nights. If it isn't right, send it back.
```

Ce qu'il ne dit jamais : que l'oreiller soulage, traite, corrige ou guérit
quoi que ce soit. « I kept waking up stiff » est une biographie ; « this
pillow fixes stiff necks » serait une allégation. La frontière est là.

## 4. Ton de voix

**Faire** — phrases courtes ; verbes physiques : *sink, hold, cradle, lift,
press* ; chiffres concrets : hauteur, dimensions, poids, nuits d'essai ;
sensoriel, calme ; première personne du fondateur dans l'About et les
e-mails, « we » ailleurs ; anglais simple, sans idiome, lisible par un
Allemand ou un Espagnol.

**Ne jamais écrire** — *revolutionary, game-changing, orthopedic, cervical*
(côté client on dit *neck*), *pain, pain relief, relieves, treats, cures,
heals, therapeutic, clinical, clinically proven, doctor recommended,
medical, sciatica, hernia, apnea, snoring cure*, points d'exclamation,
emojis, « −50 % », « limited time ».

**Vocabulaire autorisé pour parler d'ergonomie** — *support, hold, comfort,
posture, pressure distribution, shape, height, density, contour*.

## 5. Système visuel — « nuit et aube »

Version 2, 10 septembre. La DA du brief d'origine (Bone / Clay / travertin,
registre Herman Miller) avait été écrite pour un coussin d'assise ; le
fondateur l'a écartée pour la gamme sommeil. Ce qui suit la remplace.

**Direction** — doux, nuageux, aéré. La marque montre ce qu'elle vend : le
calme d'une chambre à l'aube, un oreiller qui semble flotter, une lumière
basse et diffuse. Premium par la retenue et la lumière, jamais par le
clinquant. Références : Casper première époque pour le duo nuit / accent
chaud, Aesop pour la typographie, la catégorie (Derila, Pilloway) pour le
ciel poudré — en mieux fini, sans faux badge ni faux barré.

**Palette**

| Nom | Hex | Rôle | Part |
|---|---|---|---|
| Cloud | `#F7F9FC` | fond principal, presque blanc, teinté de bleu | 55 % |
| Mist | `#DCE8F2` | bandeaux, tuiles, fonds de cartes, avatar clair | 25 % |
| Night | `#1E2A3A` | texte, wordmark, boutons pleins — jamais de noir pur | 12 % |
| Dawn | `#F0B79B` | accent chaud : le halo de l'aube, un détail par écran, survol | ≤ 6 % |
| Slate | `#6B7D90` | texte secondaire, légendes, lignes | ≤ 2 % |

Un accent Dawn par écran, jamais en aplat de bouton (il ne contraste pas
assez sur Cloud) ; il vit dans les dégradés de ciel, un halo, un liseré. Le
bleu de Somnila est **désaturé et clair** : Mist est un ciel de brume, pas un
bleu d'hôpital. Le bleu saturé (`#0072CE` et parents) reste interdit.

**Dégradé de ciel** — le seul dégradé autorisé, vertical, Cloud en haut vers
Mist en bas, avec un halo Dawn flou en bas à droite. C'est le fond des hero,
des tuiles produit et des visuels de pub.

**Typographie**

- Titres : **Fraunces Soft** — axe SOFT à 100, graisse 300–400, opsz laissé à
  la taille de rendu, casse de phrase, interlettrage −1,5 %. Les empattements
  arrondis portent le moelleux ; la même famille en SOFT 0 était trop sèche.
- Texte, interface, prix, boutons : **Manrope**, 400 et 500. Plus rond
  qu'Inter, encore très lisible.
- Capitales interdites, sauf micro-labels (Manrope 500, tracking +8 %,
  11–12 px) : *free delivery · 30-night trial*.
- Les deux polices sont libres (SIL OFL), auto-hébergées :
  `build/brand/fonts/`.

**Formes** — angles arrondis généreux : 28–32 px sur les cartes et tuiles,
boutons en pastille, champs à 22 px. Ombres diffuses et teintées Night à
faible opacité (jamais grises, jamais dures) : `0 20px 46px −20px
rgba(30,42,58,.30)`.

**Lumière** — aube : basse, diffuse, une seule direction, léger voile ;
draps blancs qui prennent la lumière ; jamais de flash, jamais de midi.

**Matières** — percale et jersey de coton, lin lavé, laine ; chêne clair,
céramique mate. Le tissu de l'oreiller toujours visible en trame.

**Composition** — l'oreiller **en lévitation** sur le ciel dégradé, ombre de
contact douce dessous, décentré sur les tiers, au moins 40 % de vide, un seul
produit par image, hero en légère contre-plongée, packshot à 45 °, macro
texture en B-roll, 50–85 mm.

**Signatures faceless** — la main qui presse la mousse et son rebond lent ;
l'oreiller qui flotte ; le lit fait à l'aube, vu de dos ; la bande de lumière
de la fenêtre sur le drap ; **la ligne d'horizon**, un trait horizontal fin
(`horizon-line.svg`) sous un titre — le fil à plomb de l'ancienne DA est
abandonné.

**Jamais** — bleu saturé, schémas de colonne vertébrale, avant/après
douleur, visages, néons, rendus 3D brillants, chambres stock souriantes,
stickers promo rouges, badges « best pillow », terracotta et bois brut de
l'ancienne DA.

## 6. Le logo

Le logo est un mot : « somnila », en bas de casse, gras et rond, où le « o »
est une lune. La lune est la seule couleur, Dawn, la lueur juste avant le
matin. Tout le reste est dans le bleu du logo. Rien d'autre à côté : ni
étoile, ni nuage, ni visage, ni objet. Il n'y a pas de wordmark séparé : le
logo est le wordmark.

Le dessin retenu est une proposition générée avec ChatGPT (voir PROMPTS.md),
validée par le fondateur, puis reconstruite en vecteur à l'identique. Aucune
image générée n'est utilisée telle quelle.

### 6.1 Fichiers

Dans `build/brand/logo/`, favicons dans `build/brand/` :

| Fichier | Usage |
|---|---|
| `somnila-logo-light.svg` / `.png` | principal : lettres bleu logo, lune Dawn, fond transparent. Sur Cloud, Mist, photo claire |
| `somnila-logo-dark.svg` / `.png` | lettres Cloud, lune Dawn, fond transparent. Sur Night ou photo sombre |
| `somnila-logo-on-black.svg` / `.png` | la proposition validée telle quelle, lune colorée, fond `#141414` intégré |
| `somnila-logo-on-night.svg` / `.png` | lettres Cloud, lune Dawn, fond Night intégré (réseaux, emails) |
| `somnila-logo-night.svg` / `.png` | une couleur bleu logo : broderie, tampon, impression une couleur |
| `somnila-logo-cloud.svg` / `.png` | une couleur Cloud : sur photo sombre |
| `somnila-mark-{night,cloud,dawn,dawn-on-night}.svg` / `.png` | le symbole seul, la lune du « o » |
| `favicon.svg`, `favicon-32.png`, `favicon-180.png`, `favicon-512.png` | lune Dawn sur tuile Night |
| `app-icon-night-1024.png` | icône d'application |
| `avatar-night-1024.png`, `avatar-mist-1024.png` | avatars réseaux sociaux, à recadrer en rond côté plateforme |
| `../horizon-line.svg` | motif secondaire, trait horizontal 1 px |
| `../logo-board.png` | planche de présentation du logo |

### 6.2 Construction

Le s, le m et le n sont repris du tracé de la proposition validée, mesurée
pixel par pixel, puis lissés jusqu'à 28, 68 et 40 segments : les arches du m
et du n sont des bosses rondes qui rejoignent les fûts par un léger creux,
comme sur l'original. Le i, le l et le point du i sont des rectangles arrondis
et un cercle exacts (rayon d'angle 21, point de rayon 36 pour une hauteur d'x
de 212). Le « a » est un cercle plein (rayon 110) plus un fût, avec un
contre-poinçon en cercle (rayon 49). La lune est construite : le cercle du
« o » moins un disque à 68 % de son rayon, décalé de 38 % du rayon vers le
haut à droite (49°) ; les cornes se rejoignent presque en haut à droite. Le
symbole seul reprend exactement cette lune. Aucune ombre, aucun dégradé,
aucun contour.

Couleurs du logo : lettres `#1F2837`, valeur mesurée sur la proposition
validée (le Night du site, `#1E2A3A`, est à un point près la même couleur ;
les deux cohabitent sans écart visible). Lune `#F0B79B` (Dawn). Fond de la
version « telle quelle » : `#141414`.

### 6.3 Règles

- La lune est la seule couleur : Dawn sur fond clair comme sur fond sombre.
  Jamais une autre lettre colorée, jamais le point du i coloré.
- Une couleur quand le support l'impose : bleu logo sur clair, Cloud sur
  sombre. La lune prend alors la couleur des lettres.
- Espace de protection : la hauteur du « o », sur les quatre côtés.
- Tailles minimales : logo 72 px de large à l'écran, 20 mm imprimé. En
  dessous, le symbole seul (la lune), jamais en dessous de 16 px.
- Le symbole seul sert aux favicons, icônes, avatars, petites broderies et
  aux étiquettes de moins de 20 mm.
- Sur photo : Dawn et Cloud sur une zone sombre, bleu logo sur une zone
  claire et calme. Jamais sur une zone chargée sans aplat.
- Jamais d'étoile, de « z », de nuage ni de visage ajoutés. Jamais étiré,
  jamais tourné, jamais en capitales, jamais retapé dans une police (le logo
  n'est pas une police, ce sont des tracés), jamais avec un contour, jamais
  dans un cercle ou un carré ajouté (l'avatar utilise le fichier prévu).
- Typographie du site : Fraunces Soft pour les titres et Manrope pour le
  texte restent la règle.

## 7. Nomenclature produit

Objets de design, nommés par fonction, numérotés. Les noms fournisseur
(Derila, Cloudii, Snuggi) n'apparaissent nulle part.

| Produit | Nom |
|---|---|
| Oreiller cervical — héros | **Neck 01** |
| Oreiller contour | **Contour 01** |
| Oreiller latéral | **Side 01** |
| Oreiller corporel en S | **Body 01** |
| Oreiller de lecture au lit | **Lounge 01** |
| Couverture | **Throw 01** |
| Masque | **Mask 01** |
| Bouchons d'oreilles | **Quiet 01** |
| Housses de rechange | **Cover — Neck / Contour / Side / Body** |
| Packs | **Neck 01 + Cover** · **Sleep Set** · **For Two** · **Side-Sleeper Set** · **Family Set** · **Evening Set** · **Quiet Night** |

**Coloris** : uniquement ceux de l'annexe photos du devis, nommés simplement —
blanc → *Cloud*, gris → *Stone*, bleu clair → *Sky*, bleu marine → *Night*,
rose → *Blush*. Le nom d'un coloris ne promet jamais une teinte que le
fournisseur n'a pas.

## 8. Checklist visuel — un non, on regénère

Palette respectée, un seul accent · lumière d'un seul côté · trame du tissu
visible · forme identique à la photo fournisseur · aucun visage, aucun texte
parasite, aucun badge · au moins 40 % de vide · bon ratio.


---

# ▶ PRIX

_Fichier : `build/PRIX.md`_

# Grille de prix — complète, raisonnée

Base de tout le raisonnement : ce qui reste **par commande après la publicité**.
Sur ce marché la première vente s'achète sur Meta ; un multiple ne dit rien.

Hypothèses, prudentes et écrites : frais de paiement 2,9 % + 0,30 € ; provision
retours 5 % (essai 30 nuits) ; coût d'acquisition client (CAC) **25 €** par
commande, moyenne réaliste d'un produit à 50–70 € en trafic froid pour une
marque sans notoriété. Le fournisseur expédie lui-même, la housse est **incluse
avec chaque oreiller** (devis, réf. 09 à 12). Prix en EUR, devise de base ;
Shopify convertit et arrondit par marché.

## 1. Pourquoi le héros est à 69,90 et pas à × 2

| Prix | Multiple | Reste après CAC | Marge nette |
|---|---|---|---|
| 49,90 | × 2,0 | **−4,34 €** | −9 % |
| 54,90 | × 2,2 | 0,26 € | 0 % |
| 59,90 | × 2,4 | 4,87 € | 8 % |
| **69,90** | **× 2,8** | **14,08 €** | **20 %** |
| 79,90 | × 3,2 | 23,29 € | 29 % |

À × 2, chaque commande payée en pub fait perdre 4 €. Et 69,90 n'est pas cher
pour la catégorie : c'est le prix affiché de Derila (vendu en faux « −50 % »
permanent), sous Pilloway (55–80 €), sous Cloudii (59–79 $).

## 2. Produits seuls

| Réf. | Produit | Coût | Prix | Reste après CAC | Rôle |
|---|---|---|---|---|---|
| 09 | **Oreiller cervical** — héros, housse incluse | 25,00 | **69,90** | 14,08 | l'entrée de toute la pub |
| 12 | Oreiller contour, housse incluse | 19,00 | 59,90 | 10,87 | second oreiller |
| 11 | Oreiller corporel en S, housse incluse | 24,00 | 69,90 | 15,08 | panier élevé, dormeurs latéraux |
| 10 | Oreiller latéral, housse incluse | 20,00 | 54,90 | 5,26 | entrée de gamme, jamais en pub seul |
| 01 | Oreiller de lecture au lit | 19,50 | 54,90 | 5,72 | achat d'impulsion, soirée |
| 02 | Couverture 200 × 230 | 19,00 | 59,90 | 10,87 | cadeau, saison froide |
| 03 | Masque de sommeil 3D | 6,00 | 19,90 | −12,97 | **jamais seul en pub** : ajout au panier |
| 05–08 | Housse de rechange (une par forme) | 3,00 | 16,90 | −12,74 | **jamais seul** : « une sur l'oreiller, une au lavage » |
| 04 | Bouchons d'oreilles, 2 paires + étui | 6,00 | 14,90 | −17,55 | **jamais seul en pub** : ajout et packs. Boîte de marque tierce (iMeBoBo), accepté par le fondateur |

Lecture : masque, housse et bouchons **perdent de l'argent s'ils sont la première
commande**. Ils n'existent que comme ajout — en fiche produit, en panier, et
dans les packs. La publicité ne pousse que le cervical, le corporel et les packs.

## 3. Packs — règle de construction

Un pack n'est retenu que s'il passe trois tests : il a un **sens d'usage**
(pas deux objets collés), la remise est **réelle et visible** (11 à 19 %), et
il rapporte **plus par commande que le meilleur produit seul** qu'il contient,
parce que le CAC se paie une fois par commande, pas par article.

| Pack | Contenu | Total seuls | **Prix pack** | Remise | Coût | Reste après CAC | Gain vs seul |
|---|---|---|---|---|---|---|---|
| **Oreiller + housse de rechange** | cervical + housse | 86,80 | **76,90** | −11 % | 28,0 | 17,52 | +3,45 |
| **Sleep set** | cervical + housse + masque + bouchons | 121,60 | **99,90** | −18 % | 40,0 | 26,70 | +12,62 |
| Nuit calme *(ajout au panier)* | masque + bouchons | 34,80 | **29,90** | −14 % | 12,0 | −9,77 | n/a — jamais première commande |
| **Pour deux** | 2 × cervical | 139,80 | **119,90** | −14 % | 50,0 | 35,13 | +21,05 |
| **Dormeur latéral** | cervical + corporel S | 139,80 | **119,90** | −14 % | 49,0 | 36,13 | +21,05 |
| Contour pour deux | 2 × contour | 119,80 | **99,90** | −17 % | 38,0 | 28,71 | +17,84 |
| Soirée | lecture + couverture | 114,80 | **94,90** | −17 % | 38,5 | 23,60 | +12,74 |
| **Famille** | 3 × cervical | 209,70 | **169,90** | −19 % | 75,0 | 56,18 | +42,10 |

Les quatre en gras sont ceux que la publicité et l'accueil mettent en avant.
« Pour deux » et « Famille » sont les packs qui font vivre Derila : même produit,
CAC payé une fois, marge par commande × 2,5 à × 4.

Pas de prix barré permanent sur les produits seuls (le brief l'interdit, et
c'est ce qui décrédibilise la concurrence). L'économie s'affiche sur le pack :
« 76,90 au lieu de 86,80 », honnête et vérifiable.

## 4. Livraison offerte dès le prix d'un oreiller — décision du fondateur

Seuil à **54,90 €**, le prix de l'oreiller le moins cher : **tout oreiller
part en livraison offerte**, seul ou en pack. Seuls les accessoires achetés
seuls (masque 19,90, housse 16,90) paient le port — et ce cas est rare puisque
la pub ne les pousse jamais seuls. Le message est simple et se tient :
« Free delivery on every pillow. »

Ce que ça coûte : rien sur le produit — le fournisseur expédie, son prix
comprend le transport — mais on renonce aux 4,90 à 9,90 € de port que le
client aurait payés. Les « reste après CAC » des tableaux ci-dessus n'incluaient
pas ce port comme revenu ; ils restent donc valables tels quels.

Réglage par zone dans le profil d'expédition, en équivalent 54,90 € :
≈ 64 $ US · 85 $ CA · 48 £ · 95 $ AU · 54,90 € EU. Reste du monde : 14,90 €
maintenu, ce n'est pas un marché cible et le délai n'y est pas confirmé.

## 5. Mise en œuvre — sans app payante

- Packs en **produits Shopify à part entière** (un produit « Sleep set » avec
  ses variantes de coloris), pas une app de bundle payante. Le stock n'est pas
  géré (le fournisseur expédie), donc aucune contrainte de composants.
- Housse et masque proposés en **ajout dans la fiche produit** de chaque
  oreiller (bloc « Complete the set » de Shrine) et dans le tiroir panier.
- Les prix par marché sont la conversion Shopify arrondie ; rien à saisir à la
  main.

## 6. Ce que ça donne pour l'entreprise

Sur 100 commandes réparties comme le fait la catégorie (55 % oreiller seul,
25 % oreiller + housse ou sleep set, 15 % pour deux ou dormeur latéral, 5 %
famille), le reste après CAC moyen est d'environ **21 € par commande**, contre
14 € si tout le monde achetait le héros seul. Les packs ne sont pas une
option marketing : ils sont la moitié de la marge.

---

## 7. Décisions finales — 10 septembre 2026, validées par le fondateur

Cette section prime sur tout ce qui précède en cas d'écart.

**Prix par marché, fixes, terminaison ,99** (liste de prix Shopify, fonction
native ; taux indicatifs USD 1,159 · GBP 0,86 · CAD 1,57 · AUD 1,74, arrondis
sous la conversion) — le détail par ligne est dans `PRODUCTS.csv`, colonnes
`usd_fixe`, `gbp_fixe`, `cad_fixe`, `aud_fixe`. Héros : 69,90 € · 79,99 $ ·
59,99 £ · 108,99 $ CA · 120,99 $ AU. L'Europe hors euro (CHF, DKK, SEK, PLN…)
reste en conversion automatique.

**Livraison offerte dès le prix d'un oreiller** : 54,90 € · 62,99 $ · 47,99 £ ·
84,99 $ CA · 94,99 $ AU. Reste du monde : 14,90 € sans seuil.

**Visibilité des packs** — quatre en vitrine (accueil, collection, publicité) :
Oreiller + housse 76,90 · Sleep set 99,90 · Pour deux 119,90 · Famille 169,90.
Trois sur leur fiche : Dormeur latéral (fiche corporel), Contour pour deux
(fiche contour), Soirée (fiche lecture). Un dans le panier : Nuit calme 29,90.

**Règle de publicité** : les campagnes ne poussent que le cervical, le
corporel et les quatre packs de vitrine. Jamais un accessoire, un latéral ou un
lecture seul.

**Suivi de gestion** : provision retours 7 % sur les oreillers (remboursement
sans retour), CAC cible 25 €, alerte si le CAC dépasse 35 € — à ce niveau seul
le pack tient.

## 8. Décision du 10 septembre au soir — prix convertis, pas de prix fixes

Le fondateur a tranché en Phase 4 : **un seul catalogue, les mêmes prix
partout, convertis par Shopify Markets dans la devise du pays** (arrondi
automatique par marché). Les colonnes `usd_fixe`, `gbp_fixe`, `cad_fixe`,
`aud_fixe` de `PRODUCTS.csv` deviennent indicatives et aucune liste de prix
n'est créée. Le seuil de livraison offerte reste **54,90 €**, comparé par
Shopify au total de la commande converti en euros. Cette section remplace
le paragraphe « Prix par marché, fixes » de la section 7.


---

# ▶ ANALYSE_PRIX

_Fichier : `build/ANALYSE_PRIX.md`_

# Analyse de validation — produits, packs, prix

Mêmes hypothèses que `PRIX.md` : paiement 2,9 % + 0,30 €, retours 5 % (variante
7 % testée), CAC 25 € (20 et 35 testés), fournisseur expédie, housse incluse
avec l'oreiller, livraison offerte dès 54,90 €. Taux EUR→USD observé 1,159.

## 1. Le test qui compte : que reste-t-il par commande si la pub coûte plus cher que prévu

| | Net après CAC 20 € | **CAC 25 €** | CAC 35 € | CAC 25 €, retours 7 % |
|---|---|---|---|---|
| Cervical seul 69,90 | 19,08 | **14,08** | 4,08 | 12,68 |
| Corporel seul 69,90 | 20,08 | **15,08** | 5,08 | 13,68 |
| Contour seul 59,90 | 15,87 | **10,87** | 0,87 | 9,67 |
| Latéral seul 54,90 | 10,26 | **5,26** | −4,74 | 4,16 |
| Lecture seul 54,90 | 10,76 | **5,76** | −4,24 | 4,66 |
| Couverture seule 59,90 | 15,87 | **10,87** | 0,87 | 9,67 |
| Oreiller + housse 76,90 | 22,52 | **17,52** | 7,52 | 15,99 |
| Sleep set 99,90 | 31,71 | **26,71** | 16,71 | 24,71 |
| Pour deux 119,90 | 40,13 | **35,13** | 25,13 | 32,73 |
| Dormeur latéral 119,90 | 41,13 | **36,13** | 26,13 | 33,73 |
| Contour pour deux 99,90 | 33,71 | **28,71** | 18,71 | 26,71 |
| Soirée 94,90 | 28,60 | **23,60** | 13,60 | 21,70 |
| Famille 169,90 | 61,18 | **56,18** | 46,18 | 52,78 |

Point mort du héros seul : **CAC 39 €**. Au-dessus, chaque commande d'un
oreiller seul perd de l'argent ; les packs, eux, tiennent jusqu'à 45–80 €.
C'est la conclusion structurante : **la publicité vend des packs et le héros,
rien d'autre.**

Sur le mix attendu de la catégorie (40 % héros seul, 10 % contour, 5 %
corporel, 15 % oreiller + housse, 10 % sleep set, 10 % pour deux, 5 % dormeur
latéral, 5 % famille) : **panier moyen 85,45 €, net moyen 20,90 € par commande
(24 %)**. C'est une entreprise qui vit.

## 2. Verdict ligne par ligne

| Ligne | Verdict | Pourquoi |
|---|---|---|
| Cervical 69,90 | **Validé** | prix affiché du leader, point mort CAC 39 €, marge nette 20 % |
| Corporel S 69,90 | **Validé** | meilleure marge unitaire de la gamme (15,08) ; à pousser en pub avec le héros, pas seulement en pack |
| Contour 59,90 | **Validé** | l'oreiller « valeur » ; à CAC 35 il est à zéro → jamais l'entrée d'une campagne seul, il vend en « pour deux » |
| Latéral 54,90 | Validé **sous condition** | −4,74 à CAC 35 ; existe pour la complétude de gamme et la vente croisée, **jamais en pub** |
| Lecture 54,90 | Validé **sous condition** | même logique ; achat d'impulsion, pack Soirée |
| Couverture 59,90 | Validé, **à surveiller** | 3,2 kg : le devis donne un seul prix de 19 € transport compris, à vérifier sur la première commande réelle vers l'Australie |
| Masque 19,90 / housse 16,90 / bouchons 14,90 | **Validé comme ajouts** | perdent 13 à 18 € s'ils sont la première commande ; n'apparaissent qu'en fiche, en panier et en pack |
| Oreiller + housse 76,90 | **Validé** | +3,45 vs seul : petit gain, mais c'est le pack qui convertit le plus (le geste « une au lavage ») |
| Sleep set 99,90 | **Validé** | +12,62 vs seul, −18 % réels ; le pack de la fiche héros |
| Pour deux 119,90 | **Validé** | +21,05 ; le pack qui fait vivre la catégorie |
| Dormeur latéral 119,90 | **Validé** | +21,05 ; seul pack à deux formes différentes, sens d'usage fort |
| Contour pour deux 99,90 | Validé, **secondaire** | bon pack, mais concurrence « Pour deux » sur l'accueil : vit sur la fiche contour |
| Soirée 94,90 | Validé, **secondaire** | assemble les deux ventes les plus faibles ; fiche lecture et saison froide seulement |
| Famille 169,90 | **Validé** | +42,10 ; 56,63 l'unité, encore × 2,3 le coût |
| Nuit calme 29,90 | **Validé comme ajout panier** | jamais première commande |

## 3. Ce qui change à l'issue de l'analyse

1. **Huit packs, c'est trop à montrer.** On les garde tous, on n'en affiche
   que quatre sur l'accueil et les pubs : Oreiller + housse, Sleep set, Pour
   deux, Famille. Dormeur latéral sur la fiche corporel, Contour pour deux sur
   la fiche contour, Soirée sur la fiche lecture, Nuit calme dans le panier.
   Moins de choix, plus de conversion.

2. **Prix fixes en USD sur le marché principal**, au lieu de la conversion
   flottante. Shopify convertit 69,90 € en 81,01 $ aujourd'hui, 78 $ ou 84 $
   demain selon le taux ; une marque ne laisse pas son prix bouger. Prix
   fixés par liste de prix (fonction native, gratuite), terminaison ,99 :

   | | EUR | **USD fixe** | écart vs conversion |
   |---|---|---|---|
   | Cervical | 69,90 | **79,99** | −1,3 % — passe sous la barre des 80 $ |
   | Corporel S | 69,90 | **79,99** | −1,3 % |
   | Contour | 59,90 | **68,99** | −0,6 % |
   | Latéral, Lecture | 54,90 | **62,99** | −1,0 % |
   | Couverture | 59,90 | **68,99** | −0,6 % |
   | Masque | 19,90 | **22,99** | |
   | Housse | 16,90 | **18,99** | |
   | Bouchons | 14,90 | **16,99** | |
   | Oreiller + housse | 76,90 | **88,99** | |
   | Sleep set | 99,90 | **114,99** | |
   | Pour deux, Dormeur latéral | 119,90 | **137,99** | |
   | Contour pour deux | 99,90 | **114,99** | |
   | Soirée | 94,90 | **108,99** | |
   | Famille | 169,90 | **195,99** | |
   | Nuit calme | 29,90 | **33,99** | |

   Même logique pour le Royaume-Uni (héros **59,99 £**) et le Canada / l'Australie
   (arrondi ,99). Le seuil de livraison offerte suit : 62,99 $ US, 47,99 £,
   84,99 $ CA, 94,99 $ AU.

3. **Provision retours à 7 % sur les oreillers** dans le suivi (pas dans les
   prix) : un fournisseur qui expédie ne reprend pas les retours, on
   remboursera sans retour. Le héros reste à 12,68 net.

4. **Règle de publicité gravée** : les campagnes ne poussent que le cervical,
   le corporel et les quatre packs. Aucune campagne sur un accessoire, un
   latéral ou un lecture seul. C'est ce qui protège la marge si le CAC monte.

## 4. Ce qui n'est pas validé, et ne le sera pas sans acte de ta part

- **Bouchons dans une boîte de marque tierce** : accepté par toi. Le risque
  n'est pas le prix, c'est l'unboxing d'un Sleep set à 99,90 avec « iMeBoBo »
  écrit sur un composant. Une boîte neutre chez le fournisseur réglerait ça.
- **Composition des matières inconnue** : les fiches diront ce que le devis
  dit, rien de plus. En Europe, l'étiquetage textile exige la composition sur
  le produit ; c'est le fournisseur qui l'appose, pas la boutique.

Tout le reste est validé : la grille passe en Phase 3 telle quelle.


---

# ▶ PROMPTS

_Fichier : `build/PROMPTS.md`_

# PROMPTS — Somnila

Prompts prêts à coller, en anglais (les modèles d'image répondent mieux en
anglais). Les consignes et notes sont en français. Chaque prompt embarque tout
le système de marque pour que le résultat reste cohérent avec le BRAND_BOOK.

Règle de conservation : une image générée est une **piste**, pas un livrable.
Le logo retenu est reconstruit en vecteur (SVG) à la géométrie près, puis
décliné (Night, Cloud, Dawn sur Night, favicons, lockups). Les images IA ne
vont jamais telles quelles sur le site, un packaging ou un dépôt de marque.

---

## 1. Logo — prompt principal pour ChatGPT (GPT Image)

Mode d'emploi : ouvrir ChatGPT, coller le bloc ci-dessous en entier, demander
4 variations par direction (A, B, C, D), une image par logo. Garder les
propositions où le mot se lit d'un coup et où le motif nuit tient à 16 px.
M'envoyer les 2 ou 3 préférées : je les redessine en vecteur.

```
You are a senior brand designer. Design the logo of SOMNILA, a new international
sleep brand (memory-foam pillows, sleep mask, earplugs, a lounge pillow, a throw
blanket), sold online, US market first, then Canada, UK, Europe, Australia.

BRAND SYSTEM (follow it exactly)
- Name: "somnila", always lowercase in the logo. Pronounced som-NEE-la. Roots:
  "somnus" (sleep) and a soft, feminine ending. Never add a tagline inside the logo.
- Positioning: night support as a design object. The hold of a designer chair, in
  a pillow. Accessible luxury: premium through restraint and light, never through
  gold, gloss or medical imagery.
- Promise: "Feel it tonight. Keep it for years."
- Values: Precision (every curve has an anatomical reason), Restraint (the pillow
  disappears into the bedroom, no gadgets), Durability (foam that holds, washable
  cover, 30-night trial).
- Archetype: the Creator, with the Protector as secondary. Faceless founder
  persona: "the quiet craftsman" — hands, a bedroom at dawn, a workshop.
- Enemy: the blue "orthopedic" pillow that screams "neck pain", the $15 foam block
  that goes flat in three months, the fake permanent "-50%".
- Taglines (not in the logo, for context only): "Sleep well." / "Support,
  redesigned." / "Held all night."
- Tone: simple English, calm, precise, warm. Never medical, never clinical, never
  hype.

VISUAL SYSTEM "night and dawn"
- Palette (use only these): Night #1E2A3A (main ink), Cloud #F7F9FC (background),
  Mist #DCE8F2 (soft surfaces), Dawn #F0B79B (one small warm accent, max 6% of
  the surface), Slate #6B7D90 (secondary text). Never pure black, never saturated
  blue, never hospital teal, never gold.
- Typography of the brand: Fraunces Soft (soft serif) for titles, Manrope for
  body text. For THIS logo, use a geometric extra-bold lowercase sans-serif with
  slightly rounded corners and tight spacing (in the spirit of Outfit, Plus
  Jakarta Sans, Gilroy). Friendly, solid, modern, direct-to-consumer.
- Shapes: soft, rounded (28–32 px radius feel), pill buttons, cloud-like
  softness, floating objects, generous negative space.
- Faceless brand: never a face, never a person, never an eye.

THE LOGO BRIEF
Make a bold lowercase wordmark "somnila" in which ONE letter quietly becomes a
night motif, so the logo says "night" and "sleep" at first glance while staying
a clean, readable word. Flat vector style, single colour Night on a Cloud
background, one optional Dawn accent. It must work at 16 px (favicon), embroidered
on a pillow cover, and printed one-colour on a kraft box.

Produce these four directions, one image per logo, centered, lots of white
space, no mockup, no shadow, no gradient, no 3D, no texture, no extra text, no
tagline, exact spelling "somnila":

A. THE MOON IS THE "o": the letter "o" is drawn as a crescent moon, thick on one
   side and thin on the other, still reading as an "o". Everything else stays a
   normal bold letter. Optional: the dot of the "i" in Dawn.
B. THE MOON ON THE "i": the wordmark stays intact; the dot of the "i" becomes a
   tiny crescent moon lying on its back (horns up), in Dawn. Subtle and elegant.
C. SYMBOL + WORDMARK: a small standalone symbol left of the word: a soft crescent
   moon lying on its back with rounded horns, like a moon that fell asleep. No
   stars. Night symbol, Night word, Cloud background.
D. THE FULL MOON "o": the "o" is a solid Dawn disc (the full moon), all other
   letters in Night. Minimal and warm.

Then show each direction in its dark version: Cloud letters on a Night
background, the Dawn accent unchanged.

Never: stars scattered around, "zzz", clouds, beds, eyes, faces, sleeping
figures, moon with a face, blue medical look, gradients, glow, bevel, drop
shadow, 3D, photo, mockup on a wall or a sign, uppercase, serif letters, any
letter other than the ones in "somnila".
```

### Variations rapides (à envoyer ensuite, une par message)

```
Direction A again, 4 variations: vary the thickness of the moon "o" (from a thin
sliver to a fat crescent) and its orientation (opening to the upper-right, to the
right, or lying on its back). Keep everything else identical.
```

```
Direction B again, 4 variations: the "i" dot as a tiny crescent, then as a tiny
full Dawn disc, then as a crescent slightly larger than the stem width, then
with the crescent in Night and no Dawn at all.
```

```
Direction C again, 4 variations of the symbol only, no text: a soft crescent
moon lying on its back, rounded horns, plump belly, tilted 15 to 25 degrees.
One version tighter, one plumper, one thinner, one wider. Flat Night on Cloud.
```

```
Take the version I mark as favourite and give me: (1) the symbol alone, (2) the
wordmark alone, (3) horizontal lockup, (4) stacked lockup, (5) a 1:1 app icon
with the symbol in Dawn on a Night square, (6) a one-colour Night version for
embroidery with no thin lines under 1.5 px at 40 mm wide.
```

### Ce que je fais ensuite

Tu m'envoies les 2 ou 3 images préférées. Je reconstruis le logo en vecteur
(SVG, arcs exacts), je le décline dans les trois couleurs autorisées, je génère
favicons, avatars et lockups, et je mets à jour le BRAND_BOOK. Aucune image
générée n'est utilisée telle quelle.

---

## 1 bis. Logo final — fusion des images 2 et 4 (prompt avec images)

Mode d'emploi : dans une nouvelle conversation ChatGPT, joindre les deux images
qu'il a produites (image 2 : le mot avec le o en croissant ; image 4 : le mot
avec le point du i en lune Dawn), puis coller le bloc ci-dessous. Il connaît
ainsi la marque même si la conversation est nouvelle.

```
I'm attaching two logo images you generated for my brand SOMNILA.
- Image 1: the wordmark "somnila" where the letter "o" is a crescent moon.
- Image 2: the wordmark "somnila" where the dot of the "i" is a small peach crescent moon.

BRAND CONTEXT (keep it exactly)
Somnila is an international sleep brand (memory-foam pillows, sleep mask,
earplugs, lounge pillow, throw blanket), US market first. Positioning: night
support as a design object, accessible luxury through restraint and light.
Promise: "Feel it tonight. Keep it for years." Values: precision, restraint,
durability. Faceless founder persona, "the quiet craftsman". Never medical,
never hype. Palette: Night #1E2A3A, Cloud #F7F9FC, Mist #DCE8F2, Dawn #F0B79B
(small warm accent), Slate #6B7D90. No pure black, no saturated blue, no gold.

TASK: merge the two images into ONE final logo.
- Keep the letterforms, weight and geometric style of Image 1: bold lowercase,
  single-storey "a", tight spacing. Make every letter slightly ROUNDER and
  softer than Image 1 (softly rounded corners on every stroke), never sharper.
- The "o" stays the crescent moon of Image 1: horns pointing to the upper
  right, plump belly at the lower left, fully readable as an "o" in the word.
  Colour it Dawn #F0B79B.
- The dot of the "i" becomes the small crescent moon of Image 2, lying on its
  back (horns up), also in Dawn #F0B79B, about 1.3 times the width of the "i"
  stem, floating just above the stem with a small gap.
- All other letters in Night #1E2A3A, background Cloud #F7F9FC.
- Exact spelling "somnila", lowercase. Nothing else: no tagline, no stars, no
  extra shapes, no outline, no shadow, no gradient, no glow, no 3D, no texture,
  no mockup, no frame.
- Flat vector look, centered, generous white space, aspect ratio 3:2, highest
  resolution available.

Then give me the same logo, one image each:
1. Dark version: Night #1E2A3A background, letters in Cloud #F7F9FC, both moons
   still Dawn #F0B79B.
2. One-colour version: everything Night on Cloud, moons included.
3. App icon: the crescent "o" alone, Dawn on a Night square, no text, 1:1.
4. The colour version on a transparent background, PNG, at least 3000 px wide.
```

Ce que j'en fais : je reconstruis la version retenue en vecteur (voir
`build/brand/logo/candidates/somnila-V1r-*.svg`, déjà prêts dans le même
esprit), puis lockups, favicons, avatars et BRAND_BOOK.

---

## 2. Visuels produit (Phase 5) — à compléter après validation du logo

Base de chaque prompt : « Place this exact product in: … » avec la photo
fournisseur en référence, aucun visage, lumière d'aube, palette ci-dessus,
40 % d'espace vide, une image mère validée par scène, 4 variantes max.
Les prompts détaillés arrivent en Phase 5.




# ══════ PARTIE 6 — KIT DE LANCEMENT ══════


---

# ▶ launch/EMAILS.md

_Fichier : `build/launch/EMAILS.md`_

# Somnila — launch email kit

Customer-facing copy, in English. Sender name: **Somnila**. Sender and reply-to:
**support@somnila.com**. Founder voice in the first
person, "we" elsewhere. No exclamation marks, no emojis, no medical claims,
no fake urgency. Every number below is a real product fact (prices in EUR,
converted at checkout).

Where each email lives: **Shopify Email** for the welcome series, the
post-purchase note and the review request (Marketing → Automations);
**Settings → Notifications** for the transactional lines. Header image:
`build/images/site/email/somnila_email_header_1200x400.jpg`, footer:
`somnila_email_footer_1200x300.jpg`.

---

## 1. Welcome series (trigger: newsletter sign-up)

### W1 — immediately · "Notes from the workshop, first note"

Preview text: *What we make, and what we refused to make.*

> Hello,
>
> Thank you for signing up. This is the first note, and it is short.
>
> I kept waking up stiff. Not every morning, enough of them. The pillows I
> found were either the blue hospital kind, the overpriced kind, or the kind
> that goes flat in three months. So I built the one I was looking for.
>
> Somnila makes five memory-foam pillows, each shaped for one way of lying.
> Foam that holds its shape through the night. A cover you can unzip and
> wash, included with every pillow. And thirty nights to decide: if it isn't
> right, one email with your order number and we refund the pillow. Nothing
> to send back.
>
> What we refused to make: a permanent "−50 %", a countdown, a badge from an
> award that doesn't exist.
>
> Next note in a few days: how to choose between the five shapes.
>
> Sleep well.
>
> [See the five pillows] → /collections/memory-foam-pillows

### W2 — day 3 · "Which pillow is yours"

Preview text: *Five shapes, one job each. Here is how to pick.*

> Most people choose by the way they fall asleep.
>
> **On your back, sometimes on your side** — Neck 01. Two heights on one
> pillow, 13 cm on one side and 11 cm on the other. Start with the higher
> side; if your head tilts up, turn it over. 62 × 42 cm, cooling cover
> included. €69.90.
>
> **You like a softer, lower pillow** — Contour 01. A gentle wave, 10 cm
> high, that follows the neck and shoulders. 60 × 35 cm, cooling cover
> included. €59.90.
>
> **On your side, all night** — Side 01. A 10 cm profile that keeps the head
> level with the shoulders. Cover included. €54.90.
>
> **You want the whole body held** — Body 01. A 120 cm S-shaped pillow that
> sits between the knees, under the arm and along the back at the same time.
> Breathable cotton cover included. €69.90.
>
> **The hour before sleep** — Lounge 01. A raised back with a ledge for the
> book or the phone. €54.90.
>
> Shipping is free on every pillow, 6 to 10 days, tracked. Thirty nights to
> decide on all of them.
>
> [Choose your shape] → /collections/memory-foam-pillows

### W3 — day 7 · "How the thirty nights work"

Preview text: *Sleep on it at home. Then decide.*

> A pillow can't be judged in a shop. It can be judged in your bed, on your
> real nights, with your real mattress.
>
> So every Somnila pillow, and every set that contains one, comes with
> thirty nights, counted from the day of delivery.
>
> How it works:
> 1. Sleep on it. Give it a few nights; a new shape takes some getting used to.
> 2. If it isn't right, email us within the thirty nights with your order
>    number.
> 3. We refund the price of the pillow to your original payment method.
>    You do not need to send it back.
>
> One more thing worth knowing: the cover unzips and goes in the washing
> machine, cold, gentle cycle, dried flat. The foam itself takes a damp
> cloth, never the machine.
>
> [Start your thirty nights] → /products/neck-01

---

## 2. Abandoned checkout (Shopify automation, one email, 1 hour after)

Subject: *Your pillow is still in the cart*
Preview text: *Thirty nights to decide, shipping included.*

> You left something in your cart. No rush; it will be there.
>
> If it helps with the decision: shipping is free on every pillow and set,
> 6 to 10 days, tracked. And you have thirty nights from delivery to decide,
> refund by email, nothing to send back.
>
> [Back to your cart] → {{ checkout_url }}
>
> A question first? Reply to this email.

No second reminder, no discount in this email.

---

## 3. Transactional notifications (Settings → Notifications)

Keep Shopify's templates; change only these lines.

- **Order confirmation**, first paragraph: *Thank you. Your order is being
  prepared by our manufacturing partner and ships in 6 to 10 days. You will
  get the tracking number by email the day it leaves.*
- **Shipping confirmation**, first paragraph: *Your order is on its way.
  Track it with the link below. Your thirty nights start the day it is
  delivered.*
- **Refund notification** (trial refund): *Your refund is on its way to your
  original payment method. Depending on your bank it appears within 5 to 10
  business days. Thank you for trying it.*

---

## 4. Post-purchase note (Shopify Email automation, 12 days after delivery)

Subject: *How are the nights?*
Preview text: *A few things worth knowing about your pillow.*

> Your pillow has been home for about two weeks. A few things worth knowing.
>
> **If it feels too high or too low** (Neck 01): turn it over. The two sides
> are 13 cm and 11 cm.
>
> **The cover** unzips and goes in the washing machine, cold, gentle cycle.
> Dry it flat. A spare cover is €16.90, so one is on the pillow while the
> other is in the wash.
>
> **If it isn't right**, you still have time: reply to this email with your
> order number before the thirtieth night and we refund the pillow.
>
> Sleep well.

---

## 5. Review request (Shopify Email, 21 days after delivery, one send)

Subject: *Two questions about your pillow*
Preview text: *Honest answers help the next person choose.*

> Three weeks in, you know the pillow better than we can describe it.
>
> Would you write a few lines about it? Two questions are enough: how you
> sleep, and whether the shape fits. Honest answers, including the critical
> ones, help the next person choose the right shape.
>
> [Write a review] → product page link
>
> Nothing is offered in exchange for a review, so that every review stays
> real.

---

## 6. Optional welcome offer — your decision

Not written into any email above. If you want one: a code **WELCOME10**,
10 % on the first order, pillows and sets only, no end date shown, mentioned
once in W1. It costs about €7 per hero order. I create it only on your "ok".


---

# ▶ launch/ADS.md

_Fichier : `build/launch/ADS.md`_

# Somnila — paid ads kit

Rules that apply to every line: real facts only, no prices in creatives
(they are converted per market; prices appear on the page), no medical
words (`pain, relief, orthopedic, cervical, therapeutic, clinical, doctor`),
no exclamation marks, no emojis, no "−50 %", no "limited time", no faces in
visuals. Per `build/PRIX.md`, ads push **Neck 01**, **Body 01** and the
**sets** only; accessories and covers are never advertised alone.

Visuals: `build/images/site/ads/` — three concepts in 1:1, 4:5 and 9:16.
Landing pages: `/products/neck-01`, `/products/body-01`,
`/collections/sets`, `/collections/memory-foam-pillows`.

---

## 1. Meta (Facebook and Instagram)

### Concept A — "Sleep well." (Neck 01, cold traffic)

Primary text, short:
> A memory-foam pillow with two heights, shaped around the way you actually
> lie. Cover included, free shipping, thirty nights to decide.

Primary text, medium:
> Neck 01 has two heights on one pillow: 13 cm on one side, 11 cm on the
> other. Turn it over until your head lies level with your shoulders. The
> foam holds its shape through the night, the cover unzips and goes in the
> washing machine. Free shipping, 6 to 10 days, tracked. Thirty nights to
> decide, refund by email.

Primary text, long:
> I kept waking up stiff. The pillows I found were the blue hospital kind,
> the overpriced kind, or the kind that goes flat in three months. So I
> built the one I was looking for. Neck 01: memory foam that holds its
> shape, two heights on one pillow, a cover you can wash. Priced like an
> object you keep, not a gadget you replace. Sleep on it for thirty nights;
> if it isn't right, one email and we refund it.

Headlines (≤ 40 characters):
- Sleep well.
- Two heights, one pillow
- Held all night
- Support, redesigned
- Thirty nights to decide

Descriptions (≤ 30 characters):
- Free shipping, 30-night trial
- Cover included
- Ships in 6–10 days, tracked

CTA: Shop now → /products/neck-01

### Concept B — "Thirty nights to decide." (trial, retargeting and cold)

Primary text, short:
> A pillow can't be judged in a shop. Sleep on it at home for thirty
> nights. If it isn't right, one email and we refund it. Nothing to send
> back.

Primary text, medium:
> Every Somnila pillow comes with thirty nights, counted from delivery.
> Sleep on it with your own mattress, your own nights. If it isn't right,
> email us your order number and we refund the pillow. No form, nothing to
> send back. Shipping is free, 6 to 10 days, tracked.

Headlines: *Thirty nights to decide* · *Judge it in your bed* · *Refund by
email, no return* · *Sleep well.*

Descriptions: *No form, nothing to send back* · *Free shipping on pillows*

CTA: Shop now → /products/neck-01 (cold) or the product viewed
(retargeting)

### Concept C — "Two heights, one pillow." (product detail, Neck 01)

Primary text:
> 13 cm on one side, 11 cm on the other. Most people know which side is
> theirs after two nights. Memory foam that holds its shape, a cool-touch
> cover included and machine washable. 62 × 42 cm, 1.4 kg.

Headlines: *Two heights, one pillow* · *13 cm or 11 cm, you choose* ·
*Foam that holds*

CTA: Shop now → /products/neck-01

### Concept D — sets (warm traffic, higher basket)

Primary text:
> Two or three pieces together cost less than apart. The saving is on the
> price tag, not in a fake strike-through. For Two: two Neck 01 pillows, one
> for each side of the bed. Side-Sleeper Set: Neck 01 under the head, Body
> 01 between the knees. Sleep Set: Neck 01, Mask 01 and Quiet 01 in one box.

Headlines: *Sets, priced honestly* · *For Two* · *Side-Sleeper Set*

CTA: Shop now → /collections/sets

### Structure and budget (a starting point, not a forecast)

- Campaign 1, cold, US only to begin: three ad sets (broad 25–55; interest
  "sleep, bedding, home"; lookalike once 100 purchases exist). Concepts A, B,
  C, each in 4:5 and 9:16. Advantage+ placements.
- Campaign 2, retargeting: product viewers and cart abandoners, 14 days,
  concept B then D.
- Budget: what you can lose for two weeks without regret; the pricing note
  assumes €25 per order acquired. Break-even acquisition cost on Neck 01 is
  about €39 (price 69.90 − cost 25 − fees − 5 % returns). Rule: after €300
  spent on a creative with no order, pause it; after 10 orders, keep only
  the ad sets under €39 per order.
- Never run accessories, covers or Quiet Night alone: they lose money as a
  first order.

---

## 2. TikTok (faceless, native)

Same rules. Hook in the first second, on-screen text in Manrope, voice-over
in the founder's voice or none. Scripts are in `SOCIAL.md` § 4. Ad text
(≤ 100 characters):

- *Two heights on one pillow. Turn it over until your head lies level.*
- *Thirty nights in your own bed. If it isn't right, one email.*
- *Memory foam that holds its shape. Cover you can wash. Sleep well.*

CTA: Shop now.

---

## 3. Google

### Search — ad group "memory foam pillow" (exact and phrase)

Keywords: memory foam pillow · memory foam neck pillow · contour pillow
memory foam · pillow for side sleepers · body pillow memory foam. Negative
keywords: orthopedic, cervical, medical, hospital, cheap, free, amazon.

Headlines (≤ 30 characters):
1. Somnila Memory-Foam Pillows
2. Two Heights, One Pillow
3. Thirty Nights To Decide
4. Cover Included, Washable
5. Free Shipping On Pillows
6. Shaped For How You Lie
7. Foam That Holds Its Shape
8. Neck 01, Contour 01, Side 01
9. Refund By Email, No Return
10. Ships In 6–10 Days, Tracked
11. Five Shapes, One Job Each
12. Body 01, 120 cm S-Shape
13. Sleep Well.
14. Sets Priced Below The Sum
15. Support, Redesigned

Descriptions (≤ 90 characters):
1. Memory-foam pillows shaped around the way you actually lie. Cover included, 30-night trial.
2. Neck 01 has 13 cm on one side and 11 cm on the other. Turn it over until your head lies level.
3. Free shipping on every pillow and set, 6 to 10 days, tracked. Thirty nights to decide.
4. If it isn't right, one email with your order number and we refund the pillow. Nothing to send back.

Final URL: /collections/memory-foam-pillows (group) · /products/neck-01
(neck keywords) · /products/body-01 (body keywords).

### Shopping

Feed titles follow the product titles already in Shopify ("Neck 01 —
Memory-foam pillow"). Google requires the shipping and return policies to be
published in the store (see the manual checklist) before Shopping ads are
approved. Product images: the sky packshots now in the galleries.

---

## 4. Compliance checklist before any ad goes live

- No word from the banned list, in text or on the image.
- No price in the creative; no "was/now" price.
- No before/after, no spine drawing, no face.
- Shipping and trial statements match the policies: free on pillows and
  sets, 6–10 days, 30 nights, refund by email.
- Landing page loads behind no password (launch day only).


---

# ▶ launch/SOCIAL.md

_Fichier : `build/launch/SOCIAL.md`_

# Somnila — social kit

Faceless by design: hands, the bed at dawn, the pillow floating, the foam
pressed and rebounding, fabric texture. Never a face, never a spine drawing,
never a before/after. Voice: short sentences, physical verbs, real numbers.
No exclamation marks, no emojis, no medical words.

Assets: avatar `build/images/site/social/somnila_avatar_1024.png`, cover
`somnila_cover_1500x500.jpg`, share image `somnila_share_1200x630.jpg`,
packshots `build/images/site/packshots/`, ads `build/images/site/ads/`.

---

## 1. Profiles

Handle to reserve on every platform: **@somnila** (check availability; if
taken, **@somnila.sleep** everywhere, the same on all platforms).

- **Instagram bio** (≤ 150 characters):
  *Memory-foam pillows shaped around the way you actually lie. Cover
  included. Thirty nights to decide.* Link: somnila.com
- **TikTok bio** (≤ 80 characters): *Pillows shaped around the way you lie.
  Thirty nights to decide.*
- **Pinterest** (boards: Pillows · The bedroom at dawn · Notes from the
  workshop): *Sleep well. Memory-foam pillows with a cover you can wash and
  thirty nights to decide.*
- **Facebook page** "About": the founder text from the brand book (§ 3),
  as is.

Pinned posts: post 1 (what Somnila is), post 4 (the thirty nights), post 7
(which pillow is yours).

---

## 2. Cadence

Three posts a week for the first month, then two. One Reel or TikTok a
week from the scripts below. Stories: one a day at most, mostly reposts of
the feed and one question sticker a week ("Back, side, or both?"). Reply to
every comment within a day, in the same voice.

---

## 3. The first twelve posts

| # | Format | Visual | Caption |
|---|---|---|---|
| 1 | Carousel 4:5 | ad *Sleep well.* + Neck 01 sky packshot + Contour + Side | *Somnila. Five memory-foam pillows, each shaped for one way of lying. Foam that holds its shape, a cover you can wash, thirty nights to decide. Sleep well.* |
| 2 | Single 4:5 | Neck 01 Cloud sky packshot | *Neck 01. Two heights on one pillow, 13 cm on one side, 11 cm on the other. Turn it over until your head lies level with your shoulders. Most people know after two nights.* |
| 3 | Reel | script A (the press) | *Memory foam that holds its shape. Press it, and watch it come back.* |
| 4 | Single 1:1 | ad *Thirty nights to decide.* | *A pillow can't be judged in a shop. Sleep on it at home for thirty nights. If it isn't right, one email with your order number and we refund it. Nothing to send back.* |
| 5 | Carousel | Contour 01 in Night, Cloud, Blush, Stone, Blue (sky packshots) | *Contour 01, the softer, lower one. A gentle wave, 10 cm, that follows the neck and shoulders. Five colours. Cooling cover included.* |
| 6 | Single 4:5 | Throw 01 detail (Slate) | *Throw 01. 200 by 230 cm of rabbit-fur effect, big enough for two on the sofa or to lie over the whole bed. Ten colours.* |
| 7 | Carousel "Which pillow is yours" | five sky packshots, one per slide, text overlay: back / softer / side / whole body / reading | *Five shapes, one job each. Back or mixed: Neck 01. Softer and lower: Contour 01. Side, all night: Side 01. The whole body held: Body 01. The hour before sleep: Lounge 01.* |
| 8 | Reel | script B (the cover) | *Unzip it, wash it cold, dry it flat, put it back. The cover comes with every pillow.* |
| 9 | Single 1:1 | Body 01 Night (supplier photo, on the bed) | *Body 01. A 120 cm S-shaped pillow that sits between the knees, under the arm and along the back at the same time.* |
| 10 | Text post on Mist | "What we refused to make: a permanent −50 %, a countdown, a badge from an award that doesn't exist." | *Notes from the workshop, note one.* |
| 11 | Carousel | For Two, Side-Sleeper Set, Sleep Set sky packshots | *Sets, priced honestly. Two or three pieces together cost less than apart. The saving is on the price tag, not in a fake strike-through.* |
| 12 | Reel | script C (the morning) | *Sleep well.* |

Hashtags, five at most, on Instagram only: #memoryfoampillow #sidesleeper
#sleepwell #bedroom #somnila.

---

## 4. Faceless video scripts (Reels, TikTok, ads)

Shot on a phone, natural light from one side, morning. No music with
lyrics; room tone or a low, slow track. On-screen text in Manrope, Night on
Cloud. 15 to 25 seconds each.

### A — The press
1. (0–2 s) Close on the pillow on a white sheet. A hand comes in and presses
   the foam slowly. Text: *Memory foam.*
2. (2–8 s) The hand lifts. The foam comes back over three seconds. Text:
   *It holds its shape.*
3. (8–14 s) Turn the pillow over: the two heights side by side, a finger
   traces the edge. Text: *13 cm on one side, 11 cm on the other.*
4. (14–18 s) Pillow floating packshot. Text: *Neck 01. Thirty nights to
   decide.* End card: wordmark.

### B — The cover
1. (0–3 s) Zip opening, close-up. Text: *Unzip it.*
2. (3–8 s) Cover into the washing machine drum. Text: *Wash it cold, gentle
   cycle.*
3. (8–12 s) Cover laid flat on a rack by a window. Text: *Dry it flat.*
4. (12–18 s) Cover back on the pillow, zip closing. Text: *Put it back. It
   comes with every pillow.* End card.

### C — The morning
1. (0–4 s) A made bed at dawn, seen from the foot of the bed, the light band
   from the window on the sheet. No text.
2. (4–9 s) Slow push-in on the pillow. Text: *Shaped around the way you
   actually lie.*
3. (9–14 s) A hand smooths the pillow once. Text: *Sleep well.*
4. (14–17 s) End card: wordmark, *somnila.com*.

### D — The thirty nights (talking text, no voice)
1. (0–3 s) Pillow on the bed. Text: *A pillow can't be judged in a shop.*
2. (3–8 s) Same shot, light changes (time-lapse, morning to evening). Text:
   *Sleep on it for thirty nights.*
3. (8–13 s) Close on a phone showing an email draft with the subject "Order
   number". Text: *If it isn't right, one email.*
4. (13–17 s) Text: *We refund it. Nothing to send back.* End card.

---

## 5. Replies, in the same voice

- "Is it good for neck pain?" → *We can't make health claims. What we can
  say: Neck 01 has two heights, 13 and 11 cm, and holds its shape through
  the night. Thirty nights to find out at home; refund by email if it isn't
  right.*
- "Where is it made?" → *Made and packed by our manufacturing partner and
  shipped directly to you, 6 to 10 days, tracked.*
- "Discount?" → *We don't run fake sales. Sets cost less than the pieces
  apart, and shipping is free on every pillow.*
- "Can I wash it?" → *The cover, yes: cold, gentle cycle, dried flat. The
  foam takes a damp cloth.*


---

# ▶ launch/PLAN.md

_Fichier : `build/launch/PLAN.md`_

# Somnila — launch plan

Day 0 is the day the store password comes off. Everything before it is
preparation; nothing is announced before the site is complete. Budget rule
from the brief: native Shopify first, no paid app without your approval.

---

## 1. Before day 0 — the checklist (you, unless marked "me")

**Store**
- [ ] Shopify Payments activated (and PayPal); test order with a real card,
      then refunded.
- [ ] Domain `somnila.com` connected; `liyan.shop` redirected.
- [ ] Store name "Somnila" (done), sender email support@somnila.com (Settings →
      Notifications → Sender email, and Settings → General → Store contact
      email), and the legal address.
- [ ] Policies pasted from `build/pages/policies/`, bracketed fields
      filled (refund, shipping, terms, privacy).
- [ ] Checkout branding: logo, Cloud background, Night text and buttons.
- [ ] Default language English (Settings → Languages), then I remove the
      leftover French locale — me, on your "ok".
- [ ] Primary market: United States (Settings → Markets).
- [ ] Theme "Somnila — build v1" published — me, on your "ok".
- [ ] Password removed — you, day 0.

**Tracking (free, native)**
- [ ] Meta pixel and Conversions API through the Facebook & Instagram
      channel app; TikTok pixel through the TikTok app; Google & YouTube
      channel for Shopping and GA4.
- [ ] Google Search Console verified; sitemap `somnila.com/sitemap.xml`
      submitted.
- [ ] UTM scheme for every link you post: `utm_source` (meta, tiktok,
      google, email, pinterest), `utm_medium` (paid, organic, email),
      `utm_campaign` (launch).

**Content**
- [ ] Email automations created from `EMAILS.md` (Shopify Email): welcome
      series, abandoned checkout, post-purchase, review request.
- [ ] Notification templates edited (three lines in `EMAILS.md` § 3).
- [ ] Social profiles created with the avatar and cover; bios from
      `SOCIAL.md`; first three posts scheduled.
- [ ] Ad accounts created; campaigns built from `ADS.md` but paused.
- [ ] Blog "Notes from the workshop": three draft articles to read and
      publish (me: drafted; you: publish).

**Supplier**
- [ ] Confirm with the supplier: neutral packaging for Quiet 01, foam
      composition and density, Side 01 weight and exact dimensions, how
      tracking numbers reach you.
- [ ] Agree the trial refund process: no return, so no reverse logistics.

---

## 2. The timeline

| Day | What happens |
|---|---|
| −14 to −8 | Checklist above. Test orders. Read the three blog drafts. |
| −7 | Password stays on. Send the site link to ten people you trust; ask for one thing they didn't understand. Fix. |
| −3 | Publish theme (me), remove password (you), verify pixels fire on a test purchase. Submit sitemap. |
| 0 | Announce on your own channels: post 1, story, the welcome note to anyone already signed up. Ads on, Meta cold campaign only, small. |
| +1 to +7 | Post 2, 3, 4. Watch cost per order daily; pause creatives at €300 without an order. Answer every message. |
| +7 | First read of the numbers (see § 3). Turn on retargeting. Post 5, 6, 7. |
| +14 | Second read. Kill or scale ad sets. Start TikTok if Meta cost per order is under €39. Post 8, 9, 10. |
| +21 | Review requests start going out automatically. Post 11, 12. |
| +30 | Month-one report: orders, cost per order, trial refunds, best shape, best colour. Decide the second month's budget. |

---

## 3. What to watch, and the decision rules

Shopify Analytics is enough for month one. Numbers to write down every
Monday:

- **Sessions → orders (conversion rate).** Under 1 % after 1,000 sessions:
  the page, not the ad, is the problem. Check speed, the first image, the
  price, the trial line.
- **Average order value.** Neck 01 alone is €69.90; sets pull it up. If it
  stays under €75, push concept D (sets) in retargeting.
- **Cost per order, per ad set.** Break-even on Neck 01 is about €39 (see
  `build/PRIX.md`). Keep what is under, pause what is over after 10 orders.
- **Trial refunds.** The pricing assumes 5 %. Above 10 % over 50 orders,
  read the emails: it is usually one shape or one height. Fix the product
  page copy before spending more.
- **Support volume.** One question asked three times becomes an FAQ entry
  (me, in a day).

Do not read anything before 30 orders; the numbers lie in small samples.

---

## 4. Customer service, five replies

Reply within one business day, from support@somnila.com, in the same voice.

1. **Where is my order?** *It ships in 6 to 10 days from the order, tracked.
   Your tracking link is in the shipping email; if it hasn't arrived after
   10 days, reply here with your order number and we chase it.*
2. **Trial refund.** *Thank you for trying it. I've refunded the pillow to
   your original payment method; it appears within 5 to 10 business days.
   No need to send it back.*
3. **Wrong height.** *Neck 01 has both heights, 13 cm and 11 cm: turn it
   over. If neither feels right, the thirty nights still apply.*
4. **Washing.** *Cover: cold, gentle cycle, dried flat. Foam: a damp cloth,
   never the machine.*
5. **Customs charge.** *Duties are calculated at checkout where possible.
   If a carrier asked you to pay on delivery, send us the receipt and your
   order number and we refund it.*

---

## 5. What is deliberately not in this plan

- No launch discount (your decision, see `EMAILS.md` § 6).
- No influencer seeding before month two: the product should earn its
  first reviews from paying customers.
- No paid apps: reviews through Shopify's free Product Reviews or Judge.me
  free plan once ten real reviews exist; no countdown, no pop-up, no
  upsell app beyond the theme's own blocks.




# ══════ PARTIE 7 — PAGES ET POLITIQUES (HTML, en anglais) ══════


---

# ▶ Page about

_Fichier : `build/pages/about.html`_

```html
<p><em>I kept waking up stiff.</em></p>
<p>Not every morning. Enough of them. I went looking for a pillow I would actually want to keep, and found three kinds: the blue hospital kind, the overpriced kind, and the kind that goes flat in three months. Sometimes all three at once.</p>
<p>Most people sleep badly and accept it. I didn't want to.</p>
<p>So I built the pillow I was looking for. Shaped around the way a body actually lies, made of foam that holds, with a cover you can wash. Priced like an object you keep, not a gadget you replace.</p>
<p>Try it for thirty nights. If it isn't right, send us an email and we refund it.</p>
<h2>What Somnila is</h2>
<p>A small range, named like objects: Neck 01, Contour 01, Side 01, Body 01, Lounge 01. Each one has a job, a height and a shape, and nothing else. No gadgets, no glowing claims, no permanent sale.</p>
<h2>What it isn't</h2>
<p>Somnila is not a medical product and we don't give medical advice. We make pillows that hold a position comfortably. What you do with a better night is yours.</p>
<p><a href="/products/neck-01">Start with Neck 01</a></p>
```

---

# ▶ Page faq

_Fichier : `build/pages/faq.html`_

```html
<h2>Choosing</h2>
<h3>Which pillow is for me?</h3>
<p>Neck 01 is the one most people start with: two heights (13 cm and 11 cm), one on each side, so you pick the one that fits the way you lie. Contour 01 is lower and softer (10 cm), for people who like a pillow that gives more. Side 01 is made for side sleepers who want a firmer 10 cm profile. Body 01 is a 120 cm body pillow that goes between the knees and along the back. Lounge 01 is for reading in bed, not for sleeping on.</p>
<h3>Which height should I choose on Neck 01?</h3>
<p>Both are on the same pillow. Lie on the 13 cm side first: if your head tilts up, turn the pillow to the 11 cm side. Most people know after two nights.</p>
<h3>What is the pillow made of?</h3>
<p>Memory foam, with a removable cover included. The Neck 01 and Contour 01 covers have a cool-touch surface. Dimensions, weight and materials are listed on every product page in centimetres and inches.</p>
<h2>Using it</h2>
<h3>How long does it take to get used to it?</h3>
<p>A contoured pillow holds your head differently from a flat one, so give it a few nights. That is exactly what the 30-night trial is for.</p>
<h3>Can I wash the cover?</h3>
<p>Yes. Unzip it and machine wash it cold on a gentle cycle, then let it dry flat. The foam itself should not go in the machine; a damp cloth is enough.</p>
<h3>Does the foam have a smell when new?</h3>
<p>New foam can have a light smell for the first hours. Leave the pillow uncovered in a ventilated room for half a day before the first night.</p>
<h2>Ordering</h2>
<h3>How long does delivery take?</h3>
<p>6 to 10 days, tracked, to the United States, Canada, the United Kingdom, Europe and Australia. Details on the <a href="/pages/shipping-delivery">shipping page</a>.</p>
<h3>Is shipping free?</h3>
<p>On every pillow and every set, yes. Only accessories bought on their own pay shipping.</p>
<h3>What if it isn't right for me?</h3>
<p>Email us within 30 nights of delivery and we refund the pillow. See <a href="/pages/returns-warranty">returns and the 30-night trial</a>.</p>
<h3>In which currency do I pay?</h3>
<p>In your local currency, converted at checkout: US dollars, Canadian dollars, pounds, euros, Australian dollars and others.</p>
```

---

# ▶ Page contact

_Fichier : `build/pages/contact.html`_

```html
<p>A question about a pillow, an order or the 30-night trial? Write to <a href="mailto:support@somnila.com">support@somnila.com</a> with your order number if you have one, or use the form below. We reply by email, usually within one to two business days.</p>
```

---

# ▶ Page shipping-delivery

_Fichier : `build/pages/shipping-delivery.html`_

```html
<p>Every order ships tracked. You get the tracking number by email as soon as the parcel leaves.</p>
<h2>Delivery times</h2>
<table>
<thead><tr><th>Zone</th><th>Delivery</th><th>Shipping cost</th></tr></thead>
<tbody>
<tr><td>United States</td><td>6–10 days</td><td>Free on every pillow · €5.90 on accessories alone</td></tr>
<tr><td>Canada</td><td>6–10 days</td><td>Free on every pillow · €7.90 on accessories alone</td></tr>
<tr><td>United Kingdom</td><td>6–10 days</td><td>Free on every pillow · €5.90 on accessories alone</td></tr>
<tr><td>Europe (EU, Switzerland, Norway)</td><td>6–10 days</td><td>Free on every pillow · €4.90 on accessories alone</td></tr>
<tr><td>Australia</td><td>6–10 days</td><td>Free on every pillow · €9.90 on accessories alone</td></tr>
<tr><td>Rest of the world</td><td>6–10 days</td><td>€14.90</td></tr>
</tbody></table>
<p>Prices are shown in your local currency at checkout. Free shipping applies to every order from €54.90, which is the price of our least expensive pillow: every pillow and every set ships free. Only accessories bought on their own (mask, earplugs, covers, throw) pay shipping.</p>
<h2>Where the parcel comes from</h2>
<p>Pillows are made and packed by our manufacturing partner and shipped directly to you, which is how we keep the price of a memory-foam pillow where it is. Delivery times are counted from the day the parcel leaves.</p>
<h2>Customs and taxes</h2>
<p>Where duties or import taxes apply to your country, they are calculated at checkout when possible. If your local carrier asks for a payment on delivery, write to us with the receipt and we will sort it out.</p>
<h2>A parcel that arrives damaged</h2>
<p>Take a photo of the box and the product before unpacking further, and <a href="/pages/contact">write to us</a> within 3 days of delivery. We replace or refund.</p>
```

---

# ▶ Page returns-warranty

_Fichier : `build/pages/returns-warranty.html`_

```html
<h2>The 30-night trial</h2>
<p>A pillow can only be judged in bed, on your nights. So every Somnila pillow (Neck 01, Contour 01, Side 01, Body 01, Lounge 01) and every set that contains one comes with a 30-night trial, counted from the day it is delivered.</p>
<p>If it isn't right, <a href="/pages/contact">send us an email</a> within those 30 nights with your order number. We refund the price of the pillow to the payment method you used. No form, no questions beyond what would help us make a better pillow. You don't need to send the pillow back.</p>
<h2>Accessories</h2>
<p>Mask 01, Quiet 01, covers and Throw 01 are hygiene and textile items. They can be returned unused, in their packaging, within 14 days of delivery for a refund. Write to us first and we send the return instructions.</p>
<h2>Defects</h2>
<p>If a product arrives damaged or a defect appears in normal use, write to us with a photo and your order number. We replace it or refund it. This does not limit your statutory rights, for example the two-year legal guarantee of conformity in the European Union.</p>
<h2>Refund timing</h2>
<p>Refunds are issued as soon as we confirm the request by email. Depending on your bank, the amount appears on your statement within 5 to 10 business days.</p>
```

---

# ▶ Politique refund-policy

_Fichier : `build/pages/policies/refund-policy.html`_

```html
<h2>30-night trial on pillows</h2>
<p>Every Somnila pillow (Neck 01, Contour 01, Side 01, Body 01, Lounge 01) and every set that contains one comes with a 30-night trial, counted from the day of delivery. If it isn't right, email us within those 30 nights with your order number. We refund the price of the pillow to the original payment method. You do not need to send the pillow back.</p>
<h2>Accessories</h2>
<p>Mask 01, Quiet 01, covers and Throw 01 are hygiene and textile items. They can be returned unused, in their original packaging, within 14 days of delivery. Write to us first and we send the return instructions. Return shipping for an unwanted accessory is paid by the customer; return shipping for a defective or wrong item is paid by us.</p>
<h2>Damaged or defective items</h2>
<p>If a product arrives damaged or develops a defect in normal use, write to us with a photo and your order number. We replace it or refund it.</p>
<h2>Refunds</h2>
<p>Refunds are issued as soon as we confirm the request by email. Depending on your bank, the amount appears on your statement within 5 to 10 business days.</p>
<h2>Your statutory rights</h2>
<p>Nothing in this policy limits your statutory rights, including the 14-day right of withdrawal and the legal guarantee of conformity where they apply (European Union, United Kingdom).</p>
<p>Contact: support@somnila.com · [RAISON SOCIALE ET ADRESSE POSTALE]</p>
```

---

# ▶ Politique shipping-policy

_Fichier : `build/pages/policies/shipping-policy.html`_

```html
<p>Every order ships tracked; the tracking number is emailed the day the parcel leaves.</p>
<h2>Delivery times and costs</h2>
<ul>
<li>United States: 6–10 days. Free on every pillow and set; €5.90 on accessories alone.</li>
<li>Canada: 6–10 days. Free on every pillow and set; €7.90 on accessories alone.</li>
<li>United Kingdom: 6–10 days. Free on every pillow and set; €5.90 on accessories alone.</li>
<li>Europe (EU, Switzerland, Norway): 6–10 days. Free on every pillow and set; €4.90 on accessories alone.</li>
<li>Australia: 6–10 days. Free on every pillow and set; €9.90 on accessories alone.</li>
<li>Rest of the world: 6–10 days, €14.90.</li>
</ul>
<p>Free shipping applies to every order from €54.90 (or its equivalent in your currency). Prices are shown in your local currency at checkout.</p>
<h2>Origin</h2>
<p>Products are made and packed by our manufacturing partner and shipped directly to you. Delivery times are counted from the day the parcel leaves.</p>
<h2>Duties and taxes</h2>
<p>Where import duties or taxes apply, they are calculated at checkout when possible. If a carrier asks for a payment on delivery, contact us with the receipt.</p>
<h2>Damaged parcel</h2>
<p>Photograph the box and the product and contact us within 3 days of delivery. We replace or refund.</p>
```

---

# ▶ Politique terms-of-service

_Fichier : `build/pages/policies/terms-of-service.html`_

```html
<p>These terms apply to every order placed on this store, operated by [RAISON SOCIALE], [FORME JURIDIQUE], [ADRESSE], [NUMÉRO D'IMMATRICULATION], [NUMÉRO DE TVA] ("Somnila", "we").</p>
<h2>Products and prices</h2>
<p>Product descriptions, dimensions and materials are given in good faith from our manufacturer's specifications. Colours may differ slightly from the photographs. Prices are shown in your local currency; the currency in which you are charged is the one shown at checkout. Somnila products are comfort items, not medical devices, and nothing on this store is medical advice.</p>
<h2>Orders and payment</h2>
<p>An order is accepted when we send the order confirmation email. Payment is taken at the time of the order through the payment providers shown at checkout. We may refuse or cancel an order in case of a pricing error, suspected fraud or unavailability; in that case you are refunded in full.</p>
<h2>Shipping, trial and returns</h2>
<p>Delivery times, shipping costs, the 30-night trial and returns are described in our <a href="/policies/shipping-policy">shipping policy</a> and <a href="/policies/refund-policy">refund policy</a>, which form part of these terms.</p>
<h2>Liability</h2>
<p>Our liability for any order is limited to the amount paid for that order, except where the law does not allow such a limit. Nothing in these terms limits your statutory rights as a consumer.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of [PAYS DU SIÈGE]. Consumers in the European Union may also rely on the mandatory rules of their country of residence and on the EU online dispute resolution platform.</p>
<p>Contact: support@somnila.com.</p>
```

---

# ▶ Politique privacy-policy

_Fichier : `build/pages/policies/privacy-policy.html`_

```html
<p>This policy explains what personal data this store collects, why, and your rights. The data controller is [RAISON SOCIALE], [ADRESSE], support@somnila.com.</p>
<h2>What we collect</h2>
<ul>
<li>Order data: name, shipping and billing address, email, phone, what you bought. Needed to deliver the order and to answer you about it (contract).</li>
<li>Payment data: processed by the payment provider shown at checkout; we never see full card numbers.</li>
<li>Account and newsletter data: email and preferences, only if you sign up (consent, withdrawable at any time by the unsubscribe link).</li>
<li>Technical data: cookies and similar technologies used by Shopify to run the store, keep your cart and measure the site. Marketing pixels are used only with your consent where the law requires it.</li>
</ul>
<h2>Who receives it</h2>
<p>Shopify (hosting and checkout), our payment providers, our manufacturing and shipping partner (name and address to deliver the parcel), and our email provider for the messages you asked for. Data may be transferred outside your country under the safeguards provided by those providers.</p>
<h2>How long</h2>
<p>Order data is kept for as long as the law requires for accounting and warranty purposes. Newsletter data is kept until you unsubscribe.</p>
<h2>Your rights</h2>
<p>You can ask for access, correction, deletion, portability, or object to processing, by writing to support@somnila.com. You can also complain to your data protection authority. Residents of the EU, the UK, California and other jurisdictions have specific rights under their local laws; we honour them on request.</p>
```

---

# ▶ pages/pages.json

_Fichier : `build/pages/pages.json`_

```json
{
 "about": {
  "title": "Our story",
  "template": "",
  "seo_title": "Our story | Somnila",
  "seo_desc": "Why Somnila exists: a founder who kept waking up stiff, and the pillow he went looking for. Memory foam that holds, covers you can wash, 30 nights to decide.",
  "body": "<p><em>I kept waking up stiff.</em></p>\n<p>Not every morning. Enough of them. I went looking for a pillow I would actually want to keep, and found three kinds: the blue hospital kind, the overpriced kind, and the kind that goes flat in three months. Sometimes all three at once.</p>\n<p>Most people sleep badly and accept it. I didn't want to.</p>\n<p>So I built the pillow I was looking for. Shaped around the way a body actually lies, made of foam that holds, with a cover you can wash. Priced like an object you keep, not a gadget you replace.</p>\n<p>Try it for thirty nights. If it isn't right, send us an email and we refund it.</p>\n<h2>What Somnila is</h2>\n<p>A small range, named like objects: Neck 01, Contour 01, Side 01, Body 01, Lounge 01. Each one has a job, a height and a shape, and nothing else. No gadgets, no glowing claims, no permanent sale.</p>\n<h2>What it isn't</h2>\n<p>Somnila is not a medical product and we don't give medical advice. We make pillows that hold a position comfortably. What you do with a better night is yours.</p>\n<p><a href=\"/products/neck-01\">Start with Neck 01</a></p>"
 },
 "shipping-delivery": {
  "title": "Shipping & delivery",
  "template": "",
  "seo_title": "Shipping & delivery | Somnila",
  "seo_desc": "Somnila ships tracked to the US, Canada, the UK, Europe and Australia in 6–10 days. Free shipping on every pillow.",
  "body": "<p>Every order ships tracked. You get the tracking number by email as soon as the parcel leaves.</p>\n<h2>Delivery times</h2>\n<table>\n<thead><tr><th>Zone</th><th>Delivery</th><th>Shipping cost</th></tr></thead>\n<tbody>\n<tr><td>United States</td><td>6–10 days</td><td>Free on every pillow · €5.90 on accessories alone</td></tr>\n<tr><td>Canada</td><td>6–10 days</td><td>Free on every pillow · €7.90 on accessories alone</td></tr>\n<tr><td>United Kingdom</td><td>6–10 days</td><td>Free on every pillow · €5.90 on accessories alone</td></tr>\n<tr><td>Europe (EU, Switzerland, Norway)</td><td>6–10 days</td><td>Free on every pillow · €4.90 on accessories alone</td></tr>\n<tr><td>Australia</td><td>6–10 days</td><td>Free on every pillow · €9.90 on accessories alone</td></tr>\n<tr><td>Rest of the world</td><td>6–10 days</td><td>€14.90</td></tr>\n</tbody></table>\n<p>Prices are shown in your local currency at checkout. Free shipping applies to every order from €54.90, which is the price of our least expensive pillow: every pillow and every set ships free. Only accessories bought on their own (mask, earplugs, covers, throw) pay shipping.</p>\n<h2>Where the parcel comes from</h2>\n<p>Pillows are made and packed by our manufacturing partner and shipped directly to you, which is how we keep the price of a memory-foam pillow where it is. Delivery times are counted from the day the parcel leaves.</p>\n<h2>Customs and taxes</h2>\n<p>Where duties or import taxes apply to your country, they are calculated at checkout when possible. If your local carrier asks for a payment on delivery, write to us with the receipt and we will sort it out.</p>\n<h2>A parcel that arrives damaged</h2>\n<p>Take a photo of the box and the product before unpacking further, and <a href=\"/pages/contact\">write to us</a> within 3 days of delivery. We replace or refund.</p>"
 },
 "returns-warranty": {
  "title": "Returns & 30-night trial",
  "template": "",
  "seo_title": "Returns & 30-night trial | Somnila",
  "seo_desc": "Sleep on any Somnila pillow for 30 nights. If it isn't right, email us and we refund it. How the trial, returns and warranty work.",
  "body": "<h2>The 30-night trial</h2>\n<p>A pillow can only be judged in bed, on your nights. So every Somnila pillow (Neck 01, Contour 01, Side 01, Body 01, Lounge 01) and every set that contains one comes with a 30-night trial, counted from the day it is delivered.</p>\n<p>If it isn't right, <a href=\"/pages/contact\">send us an email</a> within those 30 nights with your order number. We refund the price of the pillow to the payment method you used. No form, no questions beyond what would help us make a better pillow. You don't need to send the pillow back.</p>\n<h2>Accessories</h2>\n<p>Mask 01, Quiet 01, covers and Throw 01 are hygiene and textile items. They can be returned unused, in their packaging, within 14 days of delivery for a refund. Write to us first and we send the return instructions.</p>\n<h2>Defects</h2>\n<p>If a product arrives damaged or a defect appears in normal use, write to us with a photo and your order number. We replace it or refund it. This does not limit your statutory rights, for example the two-year legal guarantee of conformity in the European Union.</p>\n<h2>Refund timing</h2>\n<p>Refunds are issued as soon as we confirm the request by email. Depending on your bank, the amount appears on your statement within 5 to 10 business days.</p>"
 },
 "faq": {
  "title": "FAQ",
  "template": "faq",
  "seo_title": "FAQ | Somnila",
  "seo_desc": "Answers about Somnila pillows: heights, covers, care, delivery in 6–10 days, the 30-night trial and returns.",
  "body": "<h2>Choosing</h2>\n<h3>Which pillow is for me?</h3>\n<p>Neck 01 is the one most people start with: two heights (13 cm and 11 cm), one on each side, so you pick the one that fits the way you lie. Contour 01 is lower and softer (10 cm), for people who like a pillow that gives more. Side 01 is made for side sleepers who want a firmer 10 cm profile. Body 01 is a 120 cm body pillow that goes between the knees and along the back. Lounge 01 is for reading in bed, not for sleeping on.</p>\n<h3>Which height should I choose on Neck 01?</h3>\n<p>Both are on the same pillow. Lie on the 13 cm side first: if your head tilts up, turn the pillow to the 11 cm side. Most people know after two nights.</p>\n<h3>What is the pillow made of?</h3>\n<p>Memory foam, with a removable cover included. The Neck 01 and Contour 01 covers have a cool-touch surface. Dimensions, weight and materials are listed on every product page in centimetres and inches.</p>\n<h2>Using it</h2>\n<h3>How long does it take to get used to it?</h3>\n<p>A contoured pillow holds your head differently from a flat one, so give it a few nights. That is exactly what the 30-night trial is for.</p>\n<h3>Can I wash the cover?</h3>\n<p>Yes. Unzip it and machine wash it cold on a gentle cycle, then let it dry flat. The foam itself should not go in the machine; a damp cloth is enough.</p>\n<h3>Does the foam have a smell when new?</h3>\n<p>New foam can have a light smell for the first hours. Leave the pillow uncovered in a ventilated room for half a day before the first night.</p>\n<h2>Ordering</h2>\n<h3>How long does delivery take?</h3>\n<p>6 to 10 days, tracked, to the United States, Canada, the United Kingdom, Europe and Australia. Details on the <a href=\"/pages/shipping-delivery\">shipping page</a>.</p>\n<h3>Is shipping free?</h3>\n<p>On every pillow and every set, yes. Only accessories bought on their own pay shipping.</p>\n<h3>What if it isn't right for me?</h3>\n<p>Email us within 30 nights of delivery and we refund the pillow. See <a href=\"/pages/returns-warranty\">returns and the 30-night trial</a>.</p>\n<h3>In which currency do I pay?</h3>\n<p>In your local currency, converted at checkout: US dollars, Canadian dollars, pounds, euros, Australian dollars and others.</p>"
 },
 "contact": {
  "title": "Contact",
  "template": "contact",
  "seo_title": "Contact | Somnila",
  "seo_desc": "Write to Somnila about an order, a pillow or the 30-night trial. We reply by email.",
  "body": "<p>A question about a pillow, an order or the 30-night trial? Write to us with your order number if you have one. We reply by email, usually within one to two business days.</p>"
 }
}
```



# ══════ PARTIE 8 — DONNÉES PRODUIT ══════


---

# ▶ PRODUCTS.csv

_Fichier : `build/PRODUCTS.csv`_

```csv
id_devis,nom_fournisseur,type,prix_revient_eur,dimensions_cm,dimensions_in,poids_kg,matieres,coloris_reels,delai_fournisseur,images_source,angles_manquants,donnees_manquantes,prix_eur,compare_at_eur,multiple_du_cout,usd_approx,nom_marque,usd_fixe,gbp_fixe,cad_fixe,aud_fixe,visibilite,handle_shopify,id_shopify,statut_shopify
09,Oreiller ergonomique de soutien cervical (« Derila »),pillow-cervical,"25,00",62 × 42 × 13/11,24.4 × 16.5 × 5.1/4.3,"1,4",mousse à mémoire de forme (devis) ; technologie rafraîchissante ; housse incluse (devis),"bleu marine, blanc, gris, bleu clair",6–10 j,4 (2 propres),"dessus, macro, housse ouverte","on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","69,90",—,×2.80,≈ 81,Neck 01,79.99,59.99,108.99,120.99,accueil + pub,neck-01,9042360369309,DRAFT
12,Oreiller confort ergonomique (« Cloudii »),pillow-contour,"19,00",60 × 35 × 10,23.6 × 13.8 × 3.9,"1,1","housse lavable, surface au toucher frais (devis) ; housse incluse (devis)","gris, blanc, bleu, rose, bleu marine",6–10 j,"11 (5 propres, 6 avec faux badges)","dessus, macro, housse ouverte","on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","59,90",—,×3.15,≈ 69,Contour 01,68.99,50.99,93.99,103.99,catalogue,contour-01,9042360500381,DRAFT
10,Oreiller pour dormeurs latéraux (« Derila »),pillow-side,"20,00",60 (L) — profil 10 cm,23.6 (L) — 3.9 profile,— (absent du devis),mousse à mémoire de forme (devis) ; housse incluse (devis),"bleu, rouge, gris foncé",6–10 j,"6 (0 propre, 2 sont la variante 50 cm écartée)",toutes vues sans cotes,"on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","54,90",—,×2.75,≈ 64,Side 01,62.99,46.99,85.99,94.99,"catalogue, jamais en pub",side-01,9042360598685,DRAFT
11,Oreiller corporel ergonomique en S (« Snuggi »),pillow-body,"24,00",120 (L) × ~30,47.2 (L) × ~11.8,"1,8","housse amovible lavable, tissu respirant toucher frais (devis) ; housse incluse (devis)","bleu clair, rose, bleu ciel, gris, bleu très clair, bleu marine, vert menthe, beige/abricot",6–10 j,8 (8 propres),"3/4, macro, housse ouverte","on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","69,90",—,×2.91,≈ 81,Body 01,79.99,59.99,108.99,120.99,accueil + pub,body-01,9042360696989,DRAFT
01,Oreiller ergonomique pour téléphone au lit,pillow-reading,"19,50",60 × 37 × 23,23.6 × 14.6 × 9.1,"1,1",— (le devis ne précise pas),"bleu clair, gris, beige, rose, vert, jaune, noir",6–10 j,6 (1 propre),"3/4 sans cotes, macro","on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","54,90",—,×2.82,≈ 64,Lounge 01,62.99,46.99,85.99,94.99,"catalogue, jamais en pub",lounge-01,9042360828061,DRAFT
02,"Couverture effet fourrure de lapin, texture bulles",blanket,"19,00",200 × 230,78.7 × 90.6,"3,2","effet fourrure de lapin, surface gaufrée bulles (devis)","blanc crème, rose, beige, vert anis, vert sauge, bleu ardoise, bleu clair, jaune, gris, orange saumon",6–10 j,10 (0 propre : visage sur chaque photo),"packshot plié, macro trame","on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","59,90",—,×3.15,≈ 69,Throw 01,68.99,50.99,93.99,103.99,"catalogue, saison",throw-01,9042360959133,DRAFT
03,Masque de sommeil 3D ajustable,mask,"6,00","57 × 8,5 (L)",22.4 × 3.3,"0,07",— (le devis ne précise pas),"noir, violet, gris chiné, gris clair, bleu marine, rose, blanc",6–10 j,7 (6 propres),"porté de profil (sans visage), macro","on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","19,90",—,×3.32,≈ 23,Mask 01,22.99,16.99,30.99,33.99,ajout fiche + panier,mask-01,9042361090205,DRAFT
04,Bouchons d’oreilles anti-bruit avec étui (2 paires),earplugs,"6,00",—,—,"0,02",— (le devis ne précise pas),"bleu, vert, jaune lait, rose",6–10 j,4 (0 propre : marque tierce iMeBoBo sur la boîte),tout,"emballage de marque tierce (iMeBoBo) : accepté par le fondateur, vendu surtout en pack","14,90",—,×2.48,≈ 17,Quiet 01,16.99,11.99,22.99,24.99,ajout fiche + panier,quiet-01,9042361155741,DRAFT
05,Housse de rechange coton pour oreiller corporel,cover-body,"3,00",120 (L),47.2 (L),"1,8 (?)",coton (devis),"bleu clair, rose, bleu ciel, gris, bleu très clair, bleu marine, vert menthe, beige/abricot",6–10 j,0 dédiée (photos du 11),toutes,"on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","16,90",—,×5.63,≈ 20,Cover for Body 01,18.99,13.99,25.99,28.99,ajout fiche + panier,cover-body,9042361483421,DRAFT
06,Housse de rechange rafraîchissante pour oreiller confort,cover-contour,"3,00","68 × 37 × 11,5",26.8 × 14.6 × 4.5,"1,2 (?)",tissu rafraîchissant (devis),"gris, blanc, bleu, rose, bleu marine",6–10 j,0 dédiée,toutes,"on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","16,90",—,×5.63,≈ 20,Cover for Contour 01,18.99,13.99,25.99,28.99,ajout fiche + panier,cover-contour,9042361319581,DRAFT
07,Housse de rechange rafraîchissante pour oreiller cervical,cover-cervical,"3,00",63 × 39 × 13,24.8 × 15.4 × 5.1,"1,3 (?)","gel rafraîchissant, évacuation de l’humidité (devis)","bleu, blanc, bleu marine, rose",6–10 j,0 dédiée,toutes,"on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","16,90",—,×5.63,≈ 20,Cover for Neck 01,18.99,13.99,25.99,28.99,ajout fiche + panier,cover-neck,9042361188509,DRAFT
08,Housse de rechange pour oreiller latéral,cover-side,"3,00",60 × 35 × 10 (photos : 60 × 33),23.6 × 13.8 × 3.9,"0,8 (?)",— (le devis ne précise pas),"bleu, rouge, gris foncé",6–10 j,0 dédiée,toutes,"on avance avec les données du devis ; les tarifs de port sont forfaitaires, un poids manquant ne change rien","16,90",—,×5.63,≈ 20,Cover for Side 01,18.99,13.99,25.99,28.99,ajout fiche + panier,cover-side,9042361417885,DRAFT
P1,Pack Oreiller + housse de rechange,bundle,"28,00",,,,,,6–10 j,,,,"76,90",,×2.75,≈ 89,Neck 01 + Cover,88.99,65.99,119.99,132.99,ACCUEIL + PUB,neck-01-cover-set,9042361712797,DRAFT
P2,Sleep set — oreiller + housse + masque + bouchons,bundle,"40,00",,,,,,6–10 j,,,,"99,90",,×2.50,≈ 116,Sleep Set,114.99,84.99,155.99,172.99,ACCUEIL + PUB (fiche héros),sleep-set,9042361974941,DRAFT
P3,Pour deux — 2 oreillers cervicaux,bundle,"50,00",,,,,,6–10 j,,,,"119,90",,×2.40,≈ 139,For Two,137.99,102.99,187.99,207.99,ACCUEIL + PUB,for-two,9042362171549,DRAFT
P4,Dormeur latéral — cervical + corporel S,bundle,"49,00",,,,,,6–10 j,,,,"119,90",,×2.45,≈ 139,Side-Sleeper Set,137.99,102.99,187.99,207.99,fiche corporel,side-sleeper-set,9042362237085,DRAFT
P5,Contour pour deux,bundle,"38,00",,,,,,6–10 j,,,,"99,90",,×2.63,≈ 116,Contour for Two,114.99,84.99,155.99,172.99,fiche contour,contour-for-two,9042362335389,DRAFT
P6,Soirée — lecture + couverture,bundle,"38,50",,,,,,6–10 j,,,,"94,90",,×2.46,≈ 110,Evening Set,108.99,80.99,147.99,164.99,"fiche lecture, saison froide",evening-set,9042362761373,DRAFT
P7,Famille — 3 oreillers cervicaux,bundle,"75,00",,,,,,6–10 j,,,,"169,90",,×2.27,≈ 197,Family Set,195.99,145.99,265.99,294.99,ACCUEIL + PUB,family-set,9042362400925,DRAFT
P8,"Nuit calme — masque + bouchons (ajout au panier, jamais en pub)",bundle-addon,"12,00",,,,,,6–10 j,,,,"29,90",,×2.49,≈ 35,Quiet Night,33.99,24.99,45.99,51.99,panier uniquement,quiet-night,9042362564765,DRAFT
```

---

# ▶ shopify/products.json

_Fichier : `build/shopify/products.json`_

```json
[
 {
  "handle": "neck-01",
  "title": "Neck 01 — Memory-foam pillow",
  "vendor": "Somnila",
  "productType": "Pillow",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "pillow",
   "hero",
   "home",
   "ads"
  ],
  "descriptionHtml": "<p>Neck 01 is our contoured memory-foam pillow. Two heights, one on each side, so you choose the one that fits the way you lie. The foam holds its shape through the night instead of flattening under your head.</p><p>The cover is included. It has a cool-touch surface and goes in the washing machine.</p>",
  "seo": {
   "title": "Neck 01 memory-foam pillow | Somnila",
   "description": "A contoured memory-foam pillow with two heights and a washable cooling cover. Made to hold its shape night after night. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Night"
     },
     {
      "name": "Cloud"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Sky"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "69.90",
    "sku": "SMN-NECK01-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "25.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Cloud"
     }
    ],
    "price": "69.90",
    "sku": "SMN-NECK01-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "25.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "69.90",
    "sku": "SMN-NECK01-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "25.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sky"
     }
    ],
    "price": "69.90",
    "sku": "SMN-NECK01-SKY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "25.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "62 × 42 × 13/11 cm"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "24.4 × 16.5 × 5.1/4.3 in"
   },
   {
    "namespace": "somnila",
    "key": "materials",
    "type": "multi_line_text_field",
    "value": "Memory foam. Cooling cover."
   },
   {
    "namespace": "somnila",
    "key": "includes",
    "type": "single_line_text_field",
    "value": "Cooling cover included"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_neck-01_packshot-cloud_1x1_v1.jpg",
    "filename": "somnila_neck-01_packshot-cloud_1x1_v1.jpg",
    "alt": "Somnila Neck 01 in Cloud, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_neck-01_packshot-sky-2_1x1_v1.jpg",
    "filename": "somnila_neck-01_packshot-sky-2_1x1_v1.jpg",
    "alt": "Somnila Neck 01 in Sky, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_neck-01_packshot-night-3_1x1_v1.jpg",
    "filename": "somnila_neck-01_packshot-night-3_1x1_v1.jpg",
    "alt": "Somnila Neck 01 in Night, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_neck-01_packshot-stone-4_1x1_v1.jpg",
    "filename": "somnila_neck-01_packshot-stone-4_1x1_v1.jpg",
    "alt": "Somnila Neck 01 in Stone, three-quarter view",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 79.99,
   "gbp": 59.99,
   "cad": 108.99,
   "aud": 120.99
  }
 },
 {
  "handle": "contour-01",
  "title": "Contour 01 — Contoured comfort pillow",
  "vendor": "Somnila",
  "productType": "Pillow",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "pillow",
   "catalogue"
  ],
  "descriptionHtml": "<p>Contour 01 is the softer, lower profile in the range. A gentle wave shape that follows the neck and shoulders, for people who like a pillow that gives a little more.</p><p>The washable cover is included and stays cool to the touch.</p>",
  "seo": {
   "title": "Contour 01 contoured pillow | Somnila",
   "description": "A low-profile contoured pillow with a washable cool-touch cover included. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Stone"
     },
     {
      "name": "Cloud"
     },
     {
      "name": "Blue"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Night"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "59.90",
    "sku": "SMN-CONT01-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Cloud"
     }
    ],
    "price": "59.90",
    "sku": "SMN-CONT01-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blue"
     }
    ],
    "price": "59.90",
    "sku": "SMN-CONT01-BLUE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "59.90",
    "sku": "SMN-CONT01-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "59.90",
    "sku": "SMN-CONT01-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "60 × 35 × 10 cm"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "23.6 × 13.8 × 3.9 in"
   },
   {
    "namespace": "somnila",
    "key": "materials",
    "type": "multi_line_text_field",
    "value": "Washable cover with a cool-touch surface."
   },
   {
    "namespace": "somnila",
    "key": "includes",
    "type": "single_line_text_field",
    "value": "Cover included"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_packshot-night_1x1_v1.jpg",
    "filename": "somnila_contour-01_packshot-night_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Night, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_packshot-night-2_1x1_v1.jpg",
    "filename": "somnila_contour-01_packshot-night-2_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Night, side view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_lifestyle-cloud-3_1x1_v1.jpg",
    "filename": "somnila_contour-01_lifestyle-cloud-3_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Cloud, on a bed",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_lifestyle-blue-4_1x1_v1.jpg",
    "filename": "somnila_contour-01_lifestyle-blue-4_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Blue, on a bed",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_lifestyle-blush-5_1x1_v1.jpg",
    "filename": "somnila_contour-01_lifestyle-blush-5_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Blush, on a bed",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_packshot-cloud-6_1x1_v1.jpg",
    "filename": "somnila_contour-01_packshot-cloud-6_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Cloud, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_packshot-blush-7_1x1_v1.jpg",
    "filename": "somnila_contour-01_packshot-blush-7_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Blush, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_packshot-stone-8_1x1_v1.jpg",
    "filename": "somnila_contour-01_packshot-stone-8_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Stone, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_packshot-stone-9_1x1_v1.jpg",
    "filename": "somnila_contour-01_packshot-stone-9_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Stone, side view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-01_packshot-blue-10_1x1_v1.jpg",
    "filename": "somnila_contour-01_packshot-blue-10_1x1_v1.jpg",
    "alt": "Somnila Contour 01 in Blue, three-quarter view",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 68.99,
   "gbp": 50.99,
   "cad": 93.99,
   "aud": 103.99
  }
 },
 {
  "handle": "side-01",
  "title": "Side 01 — Side-sleeper pillow",
  "vendor": "Somnila",
  "productType": "Pillow",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "pillow",
   "catalogue"
  ],
  "descriptionHtml": "<p>Side 01 is shaped for people who sleep on their side. A 10 cm profile keeps the head level with the shoulders, and the memory foam holds that position all night.</p><p>The cover is included.</p>",
  "seo": {
   "title": "Side 01 side-sleeper pillow | Somnila",
   "description": "A memory-foam pillow shaped for side sleepers, with a 10 cm profile and a cover included. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Blue"
     },
     {
      "name": "Red"
     },
     {
      "name": "Dark grey"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blue"
     }
    ],
    "price": "54.90",
    "sku": "SMN-SIDE01-BLUE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "20.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Red"
     }
    ],
    "price": "54.90",
    "sku": "SMN-SIDE01-RED",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "20.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Dark grey"
     }
    ],
    "price": "54.90",
    "sku": "SMN-SIDE01-DARK-GREY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "20.00",
     "requiresShipping": true
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "60 cm long, 10 cm profile"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "23.6 in long, 3.9 in profile"
   },
   {
    "namespace": "somnila",
    "key": "materials",
    "type": "multi_line_text_field",
    "value": "Memory foam."
   },
   {
    "namespace": "somnila",
    "key": "includes",
    "type": "single_line_text_field",
    "value": "Cover included"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_side-01_packshot-blue_1x1_v1.jpg",
    "filename": "somnila_side-01_packshot-blue_1x1_v1.jpg",
    "alt": "Somnila Side 01 in Blue, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_side-01_packshot-dark-grey-2_1x1_v1.jpg",
    "filename": "somnila_side-01_packshot-dark-grey-2_1x1_v1.jpg",
    "alt": "Somnila Side 01 in Dark grey, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_side-01_packshot-dark-grey-3_1x1_v1.jpg",
    "filename": "somnila_side-01_packshot-dark-grey-3_1x1_v1.jpg",
    "alt": "Somnila Side 01 in Dark grey, side view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_side-01_packshot-red-4_1x1_v1.jpg",
    "filename": "somnila_side-01_packshot-red-4_1x1_v1.jpg",
    "alt": "Somnila Side 01 in Red, three-quarter view",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 62.99,
   "gbp": 46.99,
   "cad": 85.99,
   "aud": 94.99
  }
 },
 {
  "handle": "body-01",
  "title": "Body 01 — S-shaped body pillow",
  "vendor": "Somnila",
  "productType": "Pillow",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "pillow",
   "hero",
   "home",
   "ads"
  ],
  "descriptionHtml": "<p>Body 01 is a 120 cm body pillow shaped like an S. It sits between the knees, under the arm and along the back at the same time, so the whole body is held in one position.</p><p>The removable cover is breathable, cool to the touch and machine washable. It is included.</p>",
  "seo": {
   "title": "Body 01 S-shaped body pillow | Somnila",
   "description": "A 120 cm S-shaped body pillow with a removable, breathable, washable cover included. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Sky"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Azure"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Ice"
     },
     {
      "name": "Night"
     },
     {
      "name": "Mint"
     },
     {
      "name": "Apricot"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sky"
     }
    ],
    "price": "69.90",
    "sku": "SMN-BODY01-SKY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "24.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "69.90",
    "sku": "SMN-BODY01-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "24.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Azure"
     }
    ],
    "price": "69.90",
    "sku": "SMN-BODY01-AZURE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "24.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "69.90",
    "sku": "SMN-BODY01-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "24.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Ice"
     }
    ],
    "price": "69.90",
    "sku": "SMN-BODY01-ICE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "24.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "69.90",
    "sku": "SMN-BODY01-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "24.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Mint"
     }
    ],
    "price": "69.90",
    "sku": "SMN-BODY01-MINT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "24.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Apricot"
     }
    ],
    "price": "69.90",
    "sku": "SMN-BODY01-APRICOT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "24.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "120 cm long, about 30 cm wide"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "47.2 in long, about 11.8 in wide"
   },
   {
    "namespace": "somnila",
    "key": "materials",
    "type": "multi_line_text_field",
    "value": "Removable washable cover, breathable cool-touch fabric."
   },
   {
    "namespace": "somnila",
    "key": "includes",
    "type": "single_line_text_field",
    "value": "Cover included"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_body-01_packshot-night_1x1_v1.jpg",
    "filename": "somnila_body-01_packshot-night_1x1_v1.jpg",
    "alt": "Somnila Body 01 in Night, top view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_body-01_packshot-stone-2_1x1_v1.jpg",
    "filename": "somnila_body-01_packshot-stone-2_1x1_v1.jpg",
    "alt": "Somnila Body 01 in Stone, top view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_body-01_packshot-sky-3_1x1_v1.jpg",
    "filename": "somnila_body-01_packshot-sky-3_1x1_v1.jpg",
    "alt": "Somnila Body 01 in Sky, top view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_body-01_packshot-blush-4_1x1_v1.jpg",
    "filename": "somnila_body-01_packshot-blush-4_1x1_v1.jpg",
    "alt": "Somnila Body 01 in Blush, top view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_body-01_packshot-ice-5_1x1_v1.jpg",
    "filename": "somnila_body-01_packshot-ice-5_1x1_v1.jpg",
    "alt": "Somnila Body 01 in Ice, top view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_body-01_packshot-blush-and-sky-6_1x1_v1.jpg",
    "filename": "somnila_body-01_packshot-blush-and-sky-6_1x1_v1.jpg",
    "alt": "Somnila Body 01 in Blush and Sky, top view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_body-01_packshot-sky-and-blush-7_1x1_v1.jpg",
    "filename": "somnila_body-01_packshot-sky-and-blush-7_1x1_v1.jpg",
    "alt": "Somnila Body 01 in Sky and Blush, top view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_body-01_packshot-sky-8_1x1_v1.jpg",
    "filename": "somnila_body-01_packshot-sky-8_1x1_v1.jpg",
    "alt": "Somnila Body 01 in Sky, top view, second angle",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 79.99,
   "gbp": 59.99,
   "cad": 108.99,
   "aud": 120.99
  }
 },
 {
  "handle": "lounge-01",
  "title": "Lounge 01 — Reading pillow",
  "vendor": "Somnila",
  "productType": "Pillow",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "pillow",
   "catalogue"
  ],
  "descriptionHtml": "<p>Lounge 01 is the pillow for the hour before sleep. A raised back with a ledge for the phone or the book, so you read or watch in bed without holding anything up.</p>",
  "seo": {
   "title": "Lounge 01 reading pillow | Somnila",
   "description": "A raised reading pillow for the phone or the book in bed. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Sky"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Sand"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Green"
     },
     {
      "name": "Yellow"
     },
     {
      "name": "Black"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sky"
     }
    ],
    "price": "54.90",
    "sku": "SMN-LNG01-SKY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "54.90",
    "sku": "SMN-LNG01-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sand"
     }
    ],
    "price": "54.90",
    "sku": "SMN-LNG01-SAND",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "54.90",
    "sku": "SMN-LNG01-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Green"
     }
    ],
    "price": "54.90",
    "sku": "SMN-LNG01-GREEN",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Yellow"
     }
    ],
    "price": "54.90",
    "sku": "SMN-LNG01-YELLOW",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Black"
     }
    ],
    "price": "54.90",
    "sku": "SMN-LNG01-BLACK",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.1,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "60 × 37 × 23 cm"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "23.6 × 14.6 × 9.1 in"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_lounge-01_packshot-stone-and-sand_4x5_v1.jpg",
    "filename": "somnila_lounge-01_packshot-stone-and-sand_4x5_v1.jpg",
    "alt": "Somnila Lounge 01 in Stone and Sand, two pillows, three-quarter view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_lounge-01_packshot-blue-2_4x5_v1.jpg",
    "filename": "somnila_lounge-01_packshot-blue-2_4x5_v1.jpg",
    "alt": "Somnila Lounge 01 in Blue, three-quarter view",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 62.99,
   "gbp": 46.99,
   "cad": 85.99,
   "aud": 94.99
  }
 },
 {
  "handle": "throw-01",
  "title": "Throw 01 — Bubble-textured throw",
  "vendor": "Somnila",
  "productType": "Blanket",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "blanket",
   "catalogue",
   "season"
  ],
  "descriptionHtml": "<p>Throw 01 is a 200 × 230 cm throw with a rabbit-fur effect and a bubble-embossed surface. Big enough for two on the sofa, or to lie over the whole bed.</p>",
  "seo": {
   "title": "Throw 01 bubble-textured throw | Somnila",
   "description": "A 200 × 230 cm throw with a rabbit-fur effect and a bubble-embossed surface. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Cream"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Sand"
     },
     {
      "name": "Lime"
     },
     {
      "name": "Sage"
     },
     {
      "name": "Slate"
     },
     {
      "name": "Sky"
     },
     {
      "name": "Yellow"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Salmon"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Cream"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-CREAM",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sand"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-SAND",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Lime"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-LIME",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sage"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-SAGE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Slate"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-SLATE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sky"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-SKY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Yellow"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-YELLOW",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Salmon"
     }
    ],
    "price": "59.90",
    "sku": "SMN-THRW01-SALMON",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "19.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "200 × 230 cm"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "78.7 × 90.6 in"
   },
   {
    "namespace": "somnila",
    "key": "materials",
    "type": "multi_line_text_field",
    "value": "Rabbit-fur effect, bubble-embossed surface."
   }
  ],
  "files": [],
  "market_prices": {
   "usd": 68.99,
   "gbp": 50.99,
   "cad": 93.99,
   "aud": 103.99
  }
 },
 {
  "handle": "mask-01",
  "title": "Mask 01 — Contoured sleep mask",
  "vendor": "Somnila",
  "productType": "Sleep mask",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "accessory",
   "add-on"
  ],
  "descriptionHtml": "<p>Mask 01 is a contoured sleep mask. The eye cups are shaped so nothing presses on the eyelids, and the strap adjusts to fit.</p>",
  "seo": {
   "title": "Mask 01 contoured sleep mask | Somnila",
   "description": "A contoured, adjustable sleep mask that keeps pressure off the eyelids. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Black"
     },
     {
      "name": "Violet"
     },
     {
      "name": "Heather grey"
     },
     {
      "name": "Light grey"
     },
     {
      "name": "Night"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Cloud"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Black"
     }
    ],
    "price": "19.90",
    "sku": "SMN-MASK01-BLACK",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.07,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Violet"
     }
    ],
    "price": "19.90",
    "sku": "SMN-MASK01-VIOLET",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.07,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Heather grey"
     }
    ],
    "price": "19.90",
    "sku": "SMN-MASK01-HEATHER-GREY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.07,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Light grey"
     }
    ],
    "price": "19.90",
    "sku": "SMN-MASK01-LIGHT-GREY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.07,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "19.90",
    "sku": "SMN-MASK01-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.07,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "19.90",
    "sku": "SMN-MASK01-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.07,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Cloud"
     }
    ],
    "price": "19.90",
    "sku": "SMN-MASK01-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.07,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "57 × 8.5 cm"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "22.4 × 3.3 in"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_mask-01_packshot-black_1x1_v1.jpg",
    "filename": "somnila_mask-01_packshot-black_1x1_v1.jpg",
    "alt": "Somnila Mask 01 in Black, front view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_mask-01_packshot-cloud-2_1x1_v1.jpg",
    "filename": "somnila_mask-01_packshot-cloud-2_1x1_v1.jpg",
    "alt": "Somnila Mask 01 in Cloud, front view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_mask-01_packshot-blush-3_1x1_v1.jpg",
    "filename": "somnila_mask-01_packshot-blush-3_1x1_v1.jpg",
    "alt": "Somnila Mask 01 in Blush, front view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_mask-01_packshot-violet-4_1x1_v1.jpg",
    "filename": "somnila_mask-01_packshot-violet-4_1x1_v1.jpg",
    "alt": "Somnila Mask 01 in Violet, front view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_mask-01_packshot-heather-grey-5_1x1_v1.jpg",
    "filename": "somnila_mask-01_packshot-heather-grey-5_1x1_v1.jpg",
    "alt": "Somnila Mask 01 in Heather grey, front view",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_mask-01_packshot-black-6_1x1_v1.jpg",
    "filename": "somnila_mask-01_packshot-black-6_1x1_v1.jpg",
    "alt": "Somnila Mask 01 in Black, front view, second angle",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 22.99,
   "gbp": 16.99,
   "cad": 30.99,
   "aud": 33.99
  }
 },
 {
  "handle": "quiet-01",
  "title": "Quiet 01 — Earplugs, 2 pairs with case",
  "vendor": "Somnila",
  "productType": "Earplugs",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "accessory",
   "add-on"
  ],
  "descriptionHtml": "<p>Quiet 01 is two pairs of noise-reducing earplugs in a small case, for the nightstand or the travel bag.</p>",
  "seo": {
   "title": "Quiet 01 earplugs, 2 pairs with case | Somnila",
   "description": "Two pairs of noise-reducing earplugs with a case. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Blue"
     },
     {
      "name": "Green"
     },
     {
      "name": "Butter"
     },
     {
      "name": "Blush"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blue"
     }
    ],
    "price": "14.90",
    "sku": "SMN-QUIET01-BLUE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.02,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Green"
     }
    ],
    "price": "14.90",
    "sku": "SMN-QUIET01-GREEN",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.02,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Butter"
     }
    ],
    "price": "14.90",
    "sku": "SMN-QUIET01-BUTTER",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.02,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "14.90",
    "sku": "SMN-QUIET01-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "6.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.02,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "includes",
    "type": "single_line_text_field",
    "value": "2 pairs, case included"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_quiet-01_packshot-blue_1x1_v1.jpg",
    "filename": "somnila_quiet-01_packshot-blue_1x1_v1.jpg",
    "alt": "Somnila Quiet 01 in Blue, with case",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_quiet-01_packshot-green-2_1x1_v1.jpg",
    "filename": "somnila_quiet-01_packshot-green-2_1x1_v1.jpg",
    "alt": "Somnila Quiet 01 in Green, with case",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_quiet-01_packshot-butter-3_1x1_v1.jpg",
    "filename": "somnila_quiet-01_packshot-butter-3_1x1_v1.jpg",
    "alt": "Somnila Quiet 01 in Butter, with case",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_quiet-01_packshot-blush-4_1x1_v1.jpg",
    "filename": "somnila_quiet-01_packshot-blush-4_1x1_v1.jpg",
    "alt": "Somnila Quiet 01 in Blush, with case",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 16.99,
   "gbp": 11.99,
   "cad": 22.99,
   "aud": 24.99
  }
 },
 {
  "handle": "cover-neck",
  "title": "Cover for Neck 01 — Cooling replacement cover",
  "vendor": "Somnila",
  "productType": "Pillow cover",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "cover",
   "add-on"
  ],
  "descriptionHtml": "<p>A second cover for Neck 01, so one is on the pillow while the other is in the wash. Same fit as the cover that comes with the pillow.</p>",
  "seo": {
   "title": "Cover for Neck 01 | Somnila",
   "description": "A replacement cover for Neck 01, same fit as the original. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Blue"
     },
     {
      "name": "Cloud"
     },
     {
      "name": "Night"
     },
     {
      "name": "Blush"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blue"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVNECK-BLUE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Cloud"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVNECK-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVNECK-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVNECK-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "63 × 39 × 13 cm"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "24.8 × 15.4 × 5.1 in"
   },
   {
    "namespace": "somnila",
    "key": "materials",
    "type": "multi_line_text_field",
    "value": "Cooling gel, moisture-wicking fabric."
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_cover-neck_packshot-cloud_1x1_v1.jpg",
    "filename": "somnila_cover-neck_packshot-cloud_1x1_v1.jpg",
    "alt": "Somnila Cover for Neck 01: replacement cover shown on the pillow in Cloud",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 18.99,
   "gbp": 13.99,
   "cad": 25.99,
   "aud": 28.99
  }
 },
 {
  "handle": "cover-contour",
  "title": "Cover for Contour 01 — Cooling replacement cover",
  "vendor": "Somnila",
  "productType": "Pillow cover",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "cover",
   "add-on"
  ],
  "descriptionHtml": "<p>A second cover for Contour 01, so one is on the pillow while the other is in the wash. Same fit as the cover that comes with the pillow.</p>",
  "seo": {
   "title": "Cover for Contour 01 | Somnila",
   "description": "A replacement cover for Contour 01, same fit as the original. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Stone"
     },
     {
      "name": "Cloud"
     },
     {
      "name": "Blue"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Night"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVCONT-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Cloud"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVCONT-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blue"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVCONT-BLUE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVCONT-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVCONT-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "68 × 37 × 11.5 cm"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "26.8 × 14.6 × 4.5 in"
   },
   {
    "namespace": "somnila",
    "key": "materials",
    "type": "multi_line_text_field",
    "value": "Cooling fabric."
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_cover-contour_packshot-night_1x1_v1.jpg",
    "filename": "somnila_cover-contour_packshot-night_1x1_v1.jpg",
    "alt": "Somnila Cover for Contour 01: replacement cover shown on the pillow in Night",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 18.99,
   "gbp": 13.99,
   "cad": 25.99,
   "aud": 28.99
  }
 },
 {
  "handle": "cover-side",
  "title": "Cover for Side 01 — Replacement cover",
  "vendor": "Somnila",
  "productType": "Pillow cover",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "cover",
   "add-on"
  ],
  "descriptionHtml": "<p>A second cover for Side 01, so one is on the pillow while the other is in the wash. Same fit as the cover that comes with the pillow.</p>",
  "seo": {
   "title": "Cover for Side 01 | Somnila",
   "description": "A replacement cover for Side 01, same fit as the original. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Blue"
     },
     {
      "name": "Red"
     },
     {
      "name": "Dark grey"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blue"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVSIDE-BLUE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Red"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVSIDE-RED",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Dark grey"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVSIDE-DARK-GREY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "60 × 35 × 10 cm"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "23.6 × 13.8 × 3.9 in"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_cover-side_packshot-blue_1x1_v1.jpg",
    "filename": "somnila_cover-side_packshot-blue_1x1_v1.jpg",
    "alt": "Somnila Cover for Side 01: replacement cover shown on the pillow in Blue",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 18.99,
   "gbp": 13.99,
   "cad": 25.99,
   "aud": 28.99
  }
 },
 {
  "handle": "cover-body",
  "title": "Cover for Body 01 — Cotton replacement cover",
  "vendor": "Somnila",
  "productType": "Pillow cover",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "cover",
   "add-on"
  ],
  "descriptionHtml": "<p>A second cover for Body 01, so one is on the pillow while the other is in the wash. Same fit as the cover that comes with the pillow.</p>",
  "seo": {
   "title": "Cover for Body 01 | Somnila",
   "description": "A replacement cover for Body 01, same fit as the original. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Sky"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Azure"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Ice"
     },
     {
      "name": "Night"
     },
     {
      "name": "Mint"
     },
     {
      "name": "Apricot"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sky"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVBODY-SKY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVBODY-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Azure"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVBODY-AZURE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVBODY-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Ice"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVBODY-ICE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVBODY-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Mint"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVBODY-MINT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Apricot"
     }
    ],
    "price": "16.90",
    "sku": "SMN-CVBODY-APRICOT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "3.00",
     "requiresShipping": true
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_cm",
    "type": "single_line_text_field",
    "value": "120 cm long"
   },
   {
    "namespace": "somnila",
    "key": "dimensions_in",
    "type": "single_line_text_field",
    "value": "47.2 in long"
   },
   {
    "namespace": "somnila",
    "key": "materials",
    "type": "multi_line_text_field",
    "value": "Cotton."
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_cover-body_packshot-night_1x1_v1.jpg",
    "filename": "somnila_cover-body_packshot-night_1x1_v1.jpg",
    "alt": "Somnila Cover for Body 01: replacement cover shown on the pillow in Night",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 18.99,
   "gbp": 13.99,
   "cad": 25.99,
   "aud": 28.99
  }
 },
 {
  "handle": "neck-01-cover-set",
  "title": "Neck 01 + Cover",
  "vendor": "Somnila",
  "productType": "Set",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "set",
   "home",
   "ads"
  ],
  "descriptionHtml": "<p>Neck 01 with a second cooling cover. One cover on the pillow, one in the wash, no night without.</p>",
  "seo": {
   "title": "Neck 01 + spare cover set | Somnila",
   "description": "Neck 01 memory-foam pillow with a second cooling cover. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Pillow colour",
    "position": 1,
    "values": [
     {
      "name": "Night"
     },
     {
      "name": "Cloud"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Sky"
     }
    ]
   },
   {
    "name": "Spare cover",
    "position": 2,
    "values": [
     {
      "name": "Cloud"
     },
     {
      "name": "Night"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Night"
     },
     {
      "optionName": "Spare cover",
      "name": "Cloud"
     }
    ],
    "price": "76.90",
    "sku": "SMN-SET-NECKCV-NIG-CLO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "28.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Night"
     },
     {
      "optionName": "Spare cover",
      "name": "Night"
     }
    ],
    "price": "76.90",
    "sku": "SMN-SET-NECKCV-NIG-NIG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "28.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Cloud"
     },
     {
      "optionName": "Spare cover",
      "name": "Cloud"
     }
    ],
    "price": "76.90",
    "sku": "SMN-SET-NECKCV-CLO-CLO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "28.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Cloud"
     },
     {
      "optionName": "Spare cover",
      "name": "Night"
     }
    ],
    "price": "76.90",
    "sku": "SMN-SET-NECKCV-CLO-NIG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "28.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Stone"
     },
     {
      "optionName": "Spare cover",
      "name": "Cloud"
     }
    ],
    "price": "76.90",
    "sku": "SMN-SET-NECKCV-STO-CLO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "28.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Stone"
     },
     {
      "optionName": "Spare cover",
      "name": "Night"
     }
    ],
    "price": "76.90",
    "sku": "SMN-SET-NECKCV-STO-NIG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "28.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Sky"
     },
     {
      "optionName": "Spare cover",
      "name": "Cloud"
     }
    ],
    "price": "76.90",
    "sku": "SMN-SET-NECKCV-SKY-CLO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "28.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Sky"
     },
     {
      "optionName": "Spare cover",
      "name": "Night"
     }
    ],
    "price": "76.90",
    "sku": "SMN-SET-NECKCV-SKY-NIG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "28.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.4,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "contents",
    "type": "multi_line_text_field",
    "value": "1 × Neck 01\n1 × Cover for Neck 01"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_neck-01-cover-set_packshot-cloud_1x1_v1.jpg",
    "filename": "somnila_neck-01-cover-set_packshot-cloud_1x1_v1.jpg",
    "alt": "Somnila Neck 01 + Cover: Neck 01 pillow, cover included plus one spare in Cloud",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 88.99,
   "gbp": 65.99,
   "cad": 119.99,
   "aud": 132.99
  }
 },
 {
  "handle": "sleep-set",
  "title": "Sleep Set — Neck 01, Mask 01, Quiet 01",
  "vendor": "Somnila",
  "productType": "Set",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "set",
   "hero",
   "home",
   "ads"
  ],
  "descriptionHtml": "<p>Everything for one quiet night in one box: the Neck 01 pillow, the contoured Mask 01 and two pairs of Quiet 01 earplugs.</p>",
  "seo": {
   "title": "Sleep Set: pillow, mask and earplugs | Somnila",
   "description": "Neck 01 pillow, Mask 01 sleep mask and Quiet 01 earplugs in one set. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Pillow colour",
    "position": 1,
    "values": [
     {
      "name": "Night"
     },
     {
      "name": "Cloud"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Sky"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Night"
     }
    ],
    "price": "99.90",
    "sku": "SMN-SET-SLEEP-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "40.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.49,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Cloud"
     }
    ],
    "price": "99.90",
    "sku": "SMN-SET-SLEEP-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "40.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.49,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Stone"
     }
    ],
    "price": "99.90",
    "sku": "SMN-SET-SLEEP-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "40.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.49,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Pillow colour",
      "name": "Sky"
     }
    ],
    "price": "99.90",
    "sku": "SMN-SET-SLEEP-SKY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "40.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 1.49,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "contents",
    "type": "multi_line_text_field",
    "value": "1 × Neck 01\n1 × Mask 01 (Black)\n1 × Quiet 01 (Blue)"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_sleep-set_packshot-cloud_1x1_v1.jpg",
    "filename": "somnila_sleep-set_packshot-cloud_1x1_v1.jpg",
    "alt": "Somnila Sleep Set: Neck 01 pillow in Cloud",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_sleep-set_packshot-black-2_1x1_v1.jpg",
    "filename": "somnila_sleep-set_packshot-black-2_1x1_v1.jpg",
    "alt": "Somnila Sleep Set: Mask 01 in Black",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_sleep-set_packshot-blue-3_1x1_v1.jpg",
    "filename": "somnila_sleep-set_packshot-blue-3_1x1_v1.jpg",
    "alt": "Somnila Sleep Set: Quiet 01 earplugs with case in Blue",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 114.99,
   "gbp": 84.99,
   "cad": 155.99,
   "aud": 172.99
  }
 },
 {
  "handle": "for-two",
  "title": "For Two — 2 × Neck 01",
  "vendor": "Somnila",
  "productType": "Set",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "set",
   "home",
   "ads"
  ],
  "descriptionHtml": "<p>Two Neck 01 pillows, one for each side of the bed. Both with the cooling cover included.</p>",
  "seo": {
   "title": "For Two: 2 × Neck 01 pillows | Somnila",
   "description": "Two Neck 01 memory-foam pillows with cooling covers included. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Night"
     },
     {
      "name": "Cloud"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Sky"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "119.90",
    "sku": "SMN-SET-TWO-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "50.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 2.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Cloud"
     }
    ],
    "price": "119.90",
    "sku": "SMN-SET-TWO-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "50.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 2.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "119.90",
    "sku": "SMN-SET-TWO-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "50.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 2.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sky"
     }
    ],
    "price": "119.90",
    "sku": "SMN-SET-TWO-SKY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "50.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 2.8,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "contents",
    "type": "multi_line_text_field",
    "value": "2 × Neck 01"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_for-two_packshot-cloud_1x1_v1.jpg",
    "filename": "somnila_for-two_packshot-cloud_1x1_v1.jpg",
    "alt": "Somnila For Two: Neck 01 pillow in Cloud",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_for-two_packshot-sky-2_1x1_v1.jpg",
    "filename": "somnila_for-two_packshot-sky-2_1x1_v1.jpg",
    "alt": "Somnila For Two: Neck 01 pillow in Sky",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 137.99,
   "gbp": 102.99,
   "cad": 187.99,
   "aud": 207.99
  }
 },
 {
  "handle": "side-sleeper-set",
  "title": "Side-Sleeper Set — Neck 01 + Body 01",
  "vendor": "Somnila",
  "productType": "Set",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "set",
   "pdp-body"
  ],
  "descriptionHtml": "<p>For people who sleep on their side: Neck 01 under the head, Body 01 between the knees and along the back. Two pillows, one position, all night.</p>",
  "seo": {
   "title": "Side-Sleeper Set: Neck 01 + Body 01 | Somnila",
   "description": "Neck 01 and Body 01 together for side sleepers. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Night"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Sky"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "119.90",
    "sku": "SMN-SET-SIDE-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "49.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "119.90",
    "sku": "SMN-SET-SIDE-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "49.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sky"
     }
    ],
    "price": "119.90",
    "sku": "SMN-SET-SIDE-SKY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "49.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 3.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "contents",
    "type": "multi_line_text_field",
    "value": "1 × Neck 01\n1 × Body 01"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_side-sleeper-set_packshot-night_1x1_v1.jpg",
    "filename": "somnila_side-sleeper-set_packshot-night_1x1_v1.jpg",
    "alt": "Somnila Side-Sleeper Set: Neck 01 pillow in Night",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_side-sleeper-set_packshot-night-2_1x1_v1.jpg",
    "filename": "somnila_side-sleeper-set_packshot-night-2_1x1_v1.jpg",
    "alt": "Somnila Side-Sleeper Set: Body 01 pillow in Night",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 137.99,
   "gbp": 102.99,
   "cad": 187.99,
   "aud": 207.99
  }
 },
 {
  "handle": "contour-for-two",
  "title": "Contour for Two — 2 × Contour 01",
  "vendor": "Somnila",
  "productType": "Set",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "set",
   "pdp-contour"
  ],
  "descriptionHtml": "<p>Two Contour 01 pillows for one bed. Both with the washable cool-touch cover included.</p>",
  "seo": {
   "title": "Contour for Two: 2 × Contour 01 | Somnila",
   "description": "Two Contour 01 pillows with washable covers included. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Stone"
     },
     {
      "name": "Cloud"
     },
     {
      "name": "Blue"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Night"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "99.90",
    "sku": "SMN-SET-CONT2-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 2.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Cloud"
     }
    ],
    "price": "99.90",
    "sku": "SMN-SET-CONT2-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 2.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blue"
     }
    ],
    "price": "99.90",
    "sku": "SMN-SET-CONT2-BLUE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 2.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Blush"
     }
    ],
    "price": "99.90",
    "sku": "SMN-SET-CONT2-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 2.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "99.90",
    "sku": "SMN-SET-CONT2-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 2.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "contents",
    "type": "multi_line_text_field",
    "value": "2 × Contour 01"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-for-two_packshot-night_1x1_v1.jpg",
    "filename": "somnila_contour-for-two_packshot-night_1x1_v1.jpg",
    "alt": "Somnila Contour for Two in Night, Contour 01 pillow",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_contour-for-two_packshot-night-2_1x1_v1.jpg",
    "filename": "somnila_contour-for-two_packshot-night-2_1x1_v1.jpg",
    "alt": "Somnila Contour for Two in Night, Contour 01 pillow, side view",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 114.99,
   "gbp": 84.99,
   "cad": 155.99,
   "aud": 172.99
  }
 },
 {
  "handle": "evening-set",
  "title": "Evening Set — Lounge 01 + Throw 01",
  "vendor": "Somnila",
  "productType": "Set",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "set",
   "pdp-lounge",
   "season"
  ],
  "descriptionHtml": "<p>The hour before sleep, sorted: Lounge 01 holds the book or the phone, Throw 01 covers the rest.</p>",
  "seo": {
   "title": "Evening Set: Lounge 01 + Throw 01 | Somnila",
   "description": "Lounge 01 reading pillow and Throw 01 throw together. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Lounge colour",
    "position": 1,
    "values": [
     {
      "name": "Sky"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Sand"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Green"
     },
     {
      "name": "Yellow"
     },
     {
      "name": "Black"
     }
    ]
   },
   {
    "name": "Throw colour",
    "position": 2,
    "values": [
     {
      "name": "Cream"
     },
     {
      "name": "Sand"
     },
     {
      "name": "Sage"
     },
     {
      "name": "Slate"
     },
     {
      "name": "Stone"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sky"
     },
     {
      "optionName": "Throw colour",
      "name": "Cream"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SKY-CRE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sky"
     },
     {
      "optionName": "Throw colour",
      "name": "Sand"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SKY-SAN",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sky"
     },
     {
      "optionName": "Throw colour",
      "name": "Sage"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SKY-SAG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sky"
     },
     {
      "optionName": "Throw colour",
      "name": "Slate"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SKY-SLA",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sky"
     },
     {
      "optionName": "Throw colour",
      "name": "Stone"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SKY-STO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Stone"
     },
     {
      "optionName": "Throw colour",
      "name": "Cream"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-STO-CRE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Stone"
     },
     {
      "optionName": "Throw colour",
      "name": "Sand"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-STO-SAN",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Stone"
     },
     {
      "optionName": "Throw colour",
      "name": "Sage"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-STO-SAG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Stone"
     },
     {
      "optionName": "Throw colour",
      "name": "Slate"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-STO-SLA",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Stone"
     },
     {
      "optionName": "Throw colour",
      "name": "Stone"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-STO-STO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sand"
     },
     {
      "optionName": "Throw colour",
      "name": "Cream"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SAN-CRE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sand"
     },
     {
      "optionName": "Throw colour",
      "name": "Sand"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SAN-SAN",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sand"
     },
     {
      "optionName": "Throw colour",
      "name": "Sage"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SAN-SAG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sand"
     },
     {
      "optionName": "Throw colour",
      "name": "Slate"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SAN-SLA",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Sand"
     },
     {
      "optionName": "Throw colour",
      "name": "Stone"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-SAN-STO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Blush"
     },
     {
      "optionName": "Throw colour",
      "name": "Cream"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLU-CRE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Blush"
     },
     {
      "optionName": "Throw colour",
      "name": "Sand"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLU-SAN",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Blush"
     },
     {
      "optionName": "Throw colour",
      "name": "Sage"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLU-SAG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Blush"
     },
     {
      "optionName": "Throw colour",
      "name": "Slate"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLU-SLA",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Blush"
     },
     {
      "optionName": "Throw colour",
      "name": "Stone"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLU-STO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Green"
     },
     {
      "optionName": "Throw colour",
      "name": "Cream"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-GRE-CRE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Green"
     },
     {
      "optionName": "Throw colour",
      "name": "Sand"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-GRE-SAN",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Green"
     },
     {
      "optionName": "Throw colour",
      "name": "Sage"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-GRE-SAG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Green"
     },
     {
      "optionName": "Throw colour",
      "name": "Slate"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-GRE-SLA",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Green"
     },
     {
      "optionName": "Throw colour",
      "name": "Stone"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-GRE-STO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Yellow"
     },
     {
      "optionName": "Throw colour",
      "name": "Cream"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-YEL-CRE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Yellow"
     },
     {
      "optionName": "Throw colour",
      "name": "Sand"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-YEL-SAN",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Yellow"
     },
     {
      "optionName": "Throw colour",
      "name": "Sage"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-YEL-SAG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Yellow"
     },
     {
      "optionName": "Throw colour",
      "name": "Slate"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-YEL-SLA",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Yellow"
     },
     {
      "optionName": "Throw colour",
      "name": "Stone"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-YEL-STO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Black"
     },
     {
      "optionName": "Throw colour",
      "name": "Cream"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLA-CRE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Black"
     },
     {
      "optionName": "Throw colour",
      "name": "Sand"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLA-SAN",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Black"
     },
     {
      "optionName": "Throw colour",
      "name": "Sage"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLA-SAG",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Black"
     },
     {
      "optionName": "Throw colour",
      "name": "Slate"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLA-SLA",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Lounge colour",
      "name": "Black"
     },
     {
      "optionName": "Throw colour",
      "name": "Stone"
     }
    ],
    "price": "94.90",
    "sku": "SMN-SET-EVE-BLA-STO",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "38.50",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.3,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "contents",
    "type": "multi_line_text_field",
    "value": "1 × Lounge 01\n1 × Throw 01"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_evening-set_packshot-stone-and-sand_4x5_v1.jpg",
    "filename": "somnila_evening-set_packshot-stone-and-sand_4x5_v1.jpg",
    "alt": "Somnila Evening Set: Lounge 01 pillows in Stone and Sand",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 108.99,
   "gbp": 80.99,
   "cad": 147.99,
   "aud": 164.99
  }
 },
 {
  "handle": "family-set",
  "title": "Family Set — 3 × Neck 01",
  "vendor": "Somnila",
  "productType": "Set",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "set",
   "home",
   "ads"
  ],
  "descriptionHtml": "<p>Three Neck 01 pillows for the whole house, each with the cooling cover included.</p>",
  "seo": {
   "title": "Family Set: 3 × Neck 01 pillows | Somnila",
   "description": "Three Neck 01 memory-foam pillows with cooling covers included. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Colour",
    "position": 1,
    "values": [
     {
      "name": "Night"
     },
     {
      "name": "Cloud"
     },
     {
      "name": "Stone"
     },
     {
      "name": "Sky"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Night"
     }
    ],
    "price": "169.90",
    "sku": "SMN-SET-FAM-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "75.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Cloud"
     }
    ],
    "price": "169.90",
    "sku": "SMN-SET-FAM-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "75.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Stone"
     }
    ],
    "price": "169.90",
    "sku": "SMN-SET-FAM-STONE",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "75.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Colour",
      "name": "Sky"
     }
    ],
    "price": "169.90",
    "sku": "SMN-SET-FAM-SKY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "75.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 4.2,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "contents",
    "type": "multi_line_text_field",
    "value": "3 × Neck 01"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_family-set_packshot-cloud_1x1_v1.jpg",
    "filename": "somnila_family-set_packshot-cloud_1x1_v1.jpg",
    "alt": "Somnila Family Set: Neck 01 pillow in Cloud",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_family-set_packshot-sky-2_1x1_v1.jpg",
    "filename": "somnila_family-set_packshot-sky-2_1x1_v1.jpg",
    "alt": "Somnila Family Set: Neck 01 pillow in Sky",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_family-set_packshot-stone-3_1x1_v1.jpg",
    "filename": "somnila_family-set_packshot-stone-3_1x1_v1.jpg",
    "alt": "Somnila Family Set: Neck 01 pillow in Stone",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 195.99,
   "gbp": 145.99,
   "cad": 265.99,
   "aud": 294.99
  }
 },
 {
  "handle": "quiet-night",
  "title": "Quiet Night — Mask 01 + Quiet 01",
  "vendor": "Somnila",
  "productType": "Set",
  "status": "DRAFT",
  "tags": [
   "somnila",
   "set",
   "cart-only"
  ],
  "descriptionHtml": "<p>Mask 01 and Quiet 01 together: dark and quiet, wherever you sleep.</p>",
  "seo": {
   "title": "Quiet Night: Mask 01 + Quiet 01 | Somnila",
   "description": "Mask 01 sleep mask and Quiet 01 earplugs together. Ships in 6–10 days."
  },
  "productOptions": [
   {
    "name": "Mask colour",
    "position": 1,
    "values": [
     {
      "name": "Black"
     },
     {
      "name": "Violet"
     },
     {
      "name": "Heather grey"
     },
     {
      "name": "Light grey"
     },
     {
      "name": "Night"
     },
     {
      "name": "Blush"
     },
     {
      "name": "Cloud"
     }
    ]
   }
  ],
  "variants": [
   {
    "optionValues": [
     {
      "optionName": "Mask colour",
      "name": "Black"
     }
    ],
    "price": "29.90",
    "sku": "SMN-SET-QUIET-BLACK",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "12.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.09,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Mask colour",
      "name": "Violet"
     }
    ],
    "price": "29.90",
    "sku": "SMN-SET-QUIET-VIOLET",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "12.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.09,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Mask colour",
      "name": "Heather grey"
     }
    ],
    "price": "29.90",
    "sku": "SMN-SET-QUIET-HEATHER-GREY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "12.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.09,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Mask colour",
      "name": "Light grey"
     }
    ],
    "price": "29.90",
    "sku": "SMN-SET-QUIET-LIGHT-GREY",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "12.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.09,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Mask colour",
      "name": "Night"
     }
    ],
    "price": "29.90",
    "sku": "SMN-SET-QUIET-NIGHT",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "12.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.09,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Mask colour",
      "name": "Blush"
     }
    ],
    "price": "29.90",
    "sku": "SMN-SET-QUIET-BLUSH",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "12.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.09,
       "unit": "KILOGRAMS"
      }
     }
    }
   },
   {
    "optionValues": [
     {
      "optionName": "Mask colour",
      "name": "Cloud"
     }
    ],
    "price": "29.90",
    "sku": "SMN-SET-QUIET-CLOUD",
    "inventoryPolicy": "CONTINUE",
    "inventoryItem": {
     "tracked": false,
     "cost": "12.00",
     "requiresShipping": true,
     "measurement": {
      "weight": {
       "value": 0.09,
       "unit": "KILOGRAMS"
      }
     }
    }
   }
  ],
  "metafields": [
   {
    "namespace": "somnila",
    "key": "delivery",
    "type": "single_line_text_field",
    "value": "6–10 days"
   },
   {
    "namespace": "somnila",
    "key": "contents",
    "type": "multi_line_text_field",
    "value": "1 × Mask 01\n1 × Quiet 01 (Blue)"
   }
  ],
  "files": [
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_quiet-night_packshot-black_1x1_v1.jpg",
    "filename": "somnila_quiet-night_packshot-black_1x1_v1.jpg",
    "alt": "Somnila Quiet Night: Mask 01 in Black",
    "contentType": "IMAGE"
   },
   {
    "originalSource": "https://raw.githubusercontent.com/IsaacPolignac/shopify/claude/pilloway-shopify-shrine-bwge6y/build/images/shopify/somnila_quiet-night_packshot-blue-2_1x1_v1.jpg",
    "filename": "somnila_quiet-night_packshot-blue-2_1x1_v1.jpg",
    "alt": "Somnila Quiet Night: Quiet 01 earplugs with case in Blue",
    "contentType": "IMAGE"
   }
  ],
  "market_prices": {
   "usd": 33.99,
   "gbp": 24.99,
   "cad": 45.99,
   "aud": 51.99
  }
 }
]
```

---

# ▶ shopify/ids.json

_Fichier : `build/shopify/ids.json`_

```json
{
 "products": {
  "neck-01": "9042360369309",
  "contour-01": "9042360500381",
  "side-01": "9042360598685",
  "body-01": "9042360696989",
  "lounge-01": "9042360828061",
  "throw-01": "9042360959133",
  "mask-01": "9042361090205",
  "quiet-01": "9042361155741",
  "cover-neck": "9042361188509",
  "cover-contour": "9042361319581",
  "cover-side": "9042361417885",
  "cover-body": "9042361483421",
  "neck-01-cover-set": "9042361712797",
  "sleep-set": "9042361974941",
  "for-two": "9042362171549",
  "side-sleeper-set": "9042362237085",
  "contour-for-two": "9042362335389",
  "family-set": "9042362400925",
  "quiet-night": "9042362564765",
  "evening-set": "9042362761373"
 },
 "collections": {
  "somnila-pillows": "348677374109",
  "sets": "348677275805",
  "accessories": "348677308573",
  "covers": "348677341341"
 },
 "metafield_definitions": {
  "dimensions_cm": "237729775773",
  "dimensions_in": "237729808541",
  "materials": "237729841309",
  "delivery": "237729874077",
  "includes": "237729906845",
  "contents": "237729939613"
 }
}
```

---

# ▶ images/shopify.csv (correspondance photos)

_Fichier : `build/images/shopify.csv`_

```csv
handle,position,file,source,alt,colour,usage,ratio,pixels
neck-01,1,somnila_neck-01_packshot-cloud_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg,"Somnila Neck 01 in Cloud, three-quarter view",Cloud,packshot,1x1,800x800
neck-01,2,somnila_neck-01_packshot-sky-2_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_bleu-clair_34_31.jpg,"Somnila Neck 01 in Sky, three-quarter view",Sky,packshot,1x1,800x800
neck-01,3,somnila_neck-01_packshot-night-3_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg,"Somnila Neck 01 in Night, three-quarter view",Night,packshot,1x1,800x800
neck-01,4,somnila_neck-01_packshot-stone-4_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_gris_34_21.jpg,"Somnila Neck 01 in Stone, three-quarter view",Stone,packshot,1x1,800x800
contour-01,1,somnila_contour-01_packshot-night_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg,"Somnila Contour 01 in Night, three-quarter view",Night,packshot,1x1,800x800
contour-01,2,somnila_contour-01_packshot-night-2_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_bleu-marine_34_37.jpg,"Somnila Contour 01 in Night, side view",Night,packshot,1x1,800x800
contour-01,3,somnila_contour-01_lifestyle-cloud-3_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_blanc_lifestyle_30.jpg,"Somnila Contour 01 in Cloud, on a bed",Cloud,lifestyle,1x1,1440x1440
contour-01,4,somnila_contour-01_lifestyle-blue-4_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_bleu_lifestyle_02.jpg,"Somnila Contour 01 in Blue, on a bed",Blue,lifestyle,1x1,790x790
contour-01,5,somnila_contour-01_lifestyle-blush-5_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_rose_lifestyle_15.jpg,"Somnila Contour 01 in Blush, on a bed",Blush,lifestyle,1x1,1440x1440
contour-01,6,somnila_contour-01_packshot-cloud-6_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_blanc_34_08.jpg,"Somnila Contour 01 in Cloud, three-quarter view",Cloud,packshot,1x1,800x800
contour-01,7,somnila_contour-01_packshot-blush-7_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_rose-blanc_34_10.jpg,"Somnila Contour 01 in Blush, three-quarter view",Blush,packshot,1x1,800x800
contour-01,8,somnila_contour-01_packshot-stone-8_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_gris-blanc_34_11.jpg,"Somnila Contour 01 in Stone, three-quarter view",Stone,packshot,1x1,800x800
contour-01,9,somnila_contour-01_packshot-stone-9_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_gris_34_12.jpg,"Somnila Contour 01 in Stone, side view",Stone,packshot,1x1,800x800
contour-01,10,somnila_contour-01_packshot-blue-10_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_bleu_34_22.jpg,"Somnila Contour 01 in Blue, three-quarter view",Blue,packshot,1x1,800x800
side-01,1,somnila_side-01_packshot-blue_1x1_v1.jpg,10-oreiller-lateral/oreiller-lateral_bleu_34_01.jpg,"Somnila Side 01 in Blue, three-quarter view",Blue,packshot,1x1,800x800
side-01,2,somnila_side-01_packshot-dark-grey-2_1x1_v1.jpg,10-oreiller-lateral/oreiller-lateral_gris-fonce_34_26.jpg,"Somnila Side 01 in Dark grey, three-quarter view",Dark grey,packshot,1x1,800x800
side-01,3,somnila_side-01_packshot-dark-grey-3_1x1_v1.jpg,10-oreiller-lateral/oreiller-lateral_gris-fonce_34_54.jpg,"Somnila Side 01 in Dark grey, side view",Dark grey,packshot,1x1,800x800
side-01,4,somnila_side-01_packshot-red-4_1x1_v1.jpg,10-oreiller-lateral/oreiller-lateral_rouge_34_27.jpg,"Somnila Side 01 in Red, three-quarter view",Red,packshot,1x1,800x800
body-01,1,somnila_body-01_packshot-night_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg,"Somnila Body 01 in Night, top view",Night,packshot,1x1,1141x1141
body-01,2,somnila_body-01_packshot-stone-2_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_gris_dessus_18.jpg,"Somnila Body 01 in Stone, top view",Stone,packshot,1x1,800x800
body-01,3,somnila_body-01_packshot-sky-3_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_07.jpg,"Somnila Body 01 in Sky, top view",Sky,packshot,1x1,800x800
body-01,4,somnila_body-01_packshot-blush-4_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_rose_dessus_24.jpg,"Somnila Body 01 in Blush, top view",Blush,packshot,1x1,800x800
body-01,5,somnila_body-01_packshot-ice-5_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_bleu-tres-clair_dessus_53.jpg,"Somnila Body 01 in Ice, top view",Ice,packshot,1x1,800x800
body-01,6,somnila_body-01_packshot-blush-and-sky-6_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_rose-bleu_dessus_00.jpg,"Somnila Body 01 in Blush and Sky, top view",Blush and Sky,packshot,1x1,1440x1440
body-01,7,somnila_body-01_packshot-sky-and-blush-7_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_bleu-rose_dessus_29.jpg,"Somnila Body 01 in Sky and Blush, top view",Sky and Blush,packshot,1x1,1440x1440
body-01,8,somnila_body-01_packshot-sky-8_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_50.jpg,"Somnila Body 01 in Sky, top view, second angle",Sky,packshot,1x1,800x800
lounge-01,1,somnila_lounge-01_packshot-stone-and-sand_4x5_v1.jpg,01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg,"Somnila Lounge 01 in Stone and Sand, two pillows, three-quarter view",Stone and Sand,packshot,4x5,800x1055
lounge-01,2,somnila_lounge-01_packshot-blue-2_4x5_v1.jpg,01-oreiller-telephone/oreiller-telephone_bleu_34_25.jpg,"Somnila Lounge 01 in Blue, three-quarter view",Blue,packshot,4x5,800x979
mask-01,1,somnila_mask-01_packshot-black_1x1_v1.jpg,03-masque/masque_noir_face_05.jpg,"Somnila Mask 01 in Black, front view",Black,packshot,1x1,800x800
mask-01,2,somnila_mask-01_packshot-cloud-2_1x1_v1.jpg,03-masque/masque_blanc_face_04.jpg,"Somnila Mask 01 in Cloud, front view",Cloud,packshot,1x1,800x800
mask-01,3,somnila_mask-01_packshot-blush-3_1x1_v1.jpg,03-masque/masque_rose_face_03.jpg,"Somnila Mask 01 in Blush, front view",Blush,packshot,1x1,800x800
mask-01,4,somnila_mask-01_packshot-violet-4_1x1_v1.jpg,03-masque/masque_violet-blanc_face_20.jpg,"Somnila Mask 01 in Violet, front view",Violet,packshot,1x1,800x800
mask-01,5,somnila_mask-01_packshot-heather-grey-5_1x1_v1.jpg,03-masque/masque_gris-chine_face_38.jpg,"Somnila Mask 01 in Heather grey, front view",Heather grey,packshot,1x1,800x800
mask-01,6,somnila_mask-01_packshot-black-6_1x1_v1.jpg,03-masque/masque_noir_face_16.jpg,"Somnila Mask 01 in Black, front view, second angle",Black,packshot,1x1,800x800
quiet-01,1,somnila_quiet-01_packshot-blue_1x1_v1.jpg,04-bouchons/bouchons_bleu_boite_17.jpg,"Somnila Quiet 01 in Blue, with case",Blue,packshot,1x1,800x800
quiet-01,2,somnila_quiet-01_packshot-green-2_1x1_v1.jpg,04-bouchons/bouchons_vert_boite_14.jpg,"Somnila Quiet 01 in Green, with case",Green,packshot,1x1,800x800
quiet-01,3,somnila_quiet-01_packshot-butter-3_1x1_v1.jpg,04-bouchons/bouchons_jaune-lait_boite_19.jpg,"Somnila Quiet 01 in Butter, with case",Butter,packshot,1x1,800x800
quiet-01,4,somnila_quiet-01_packshot-blush-4_1x1_v1.jpg,04-bouchons/bouchons_rose_boite_28.jpg,"Somnila Quiet 01 in Blush, with case",Blush,packshot,1x1,800x800
cover-neck,1,somnila_cover-neck_packshot-cloud_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg,Somnila Cover for Neck 01: replacement cover shown on the pillow in Cloud,Cloud,packshot,1x1,800x800
cover-contour,1,somnila_cover-contour_packshot-night_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg,Somnila Cover for Contour 01: replacement cover shown on the pillow in Night,Night,packshot,1x1,800x800
cover-side,1,somnila_cover-side_packshot-blue_1x1_v1.jpg,10-oreiller-lateral/oreiller-lateral_bleu_34_01.jpg,Somnila Cover for Side 01: replacement cover shown on the pillow in Blue,Blue,packshot,1x1,800x800
cover-body,1,somnila_cover-body_packshot-night_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg,Somnila Cover for Body 01: replacement cover shown on the pillow in Night,Night,packshot,1x1,1141x1141
neck-01-cover-set,1,somnila_neck-01-cover-set_packshot-cloud_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg,"Somnila Neck 01 + Cover: Neck 01 pillow, cover included plus one spare in Cloud",Cloud,packshot,1x1,800x800
sleep-set,1,somnila_sleep-set_packshot-cloud_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg,Somnila Sleep Set: Neck 01 pillow in Cloud,Cloud,packshot,1x1,800x800
sleep-set,2,somnila_sleep-set_packshot-black-2_1x1_v1.jpg,03-masque/masque_noir_face_05.jpg,Somnila Sleep Set: Mask 01 in Black,Black,packshot,1x1,800x800
sleep-set,3,somnila_sleep-set_packshot-blue-3_1x1_v1.jpg,04-bouchons/bouchons_bleu_boite_17.jpg,Somnila Sleep Set: Quiet 01 earplugs with case in Blue,Blue,packshot,1x1,800x800
for-two,1,somnila_for-two_packshot-cloud_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg,Somnila For Two: Neck 01 pillow in Cloud,Cloud,packshot,1x1,800x800
for-two,2,somnila_for-two_packshot-sky-2_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_bleu-clair_34_31.jpg,Somnila For Two: Neck 01 pillow in Sky,Sky,packshot,1x1,800x800
side-sleeper-set,1,somnila_side-sleeper-set_packshot-night_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg,Somnila Side-Sleeper Set: Neck 01 pillow in Night,Night,packshot,1x1,800x800
side-sleeper-set,2,somnila_side-sleeper-set_packshot-night-2_1x1_v1.jpg,11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg,Somnila Side-Sleeper Set: Body 01 pillow in Night,Night,packshot,1x1,1141x1141
contour-for-two,1,somnila_contour-for-two_packshot-night_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg,"Somnila Contour for Two in Night, Contour 01 pillow",Night,packshot,1x1,800x800
contour-for-two,2,somnila_contour-for-two_packshot-night-2_1x1_v1.jpg,12-oreiller-vague/oreiller-vague_bleu-marine_34_37.jpg,"Somnila Contour for Two in Night, Contour 01 pillow, side view",Night,packshot,1x1,800x800
evening-set,1,somnila_evening-set_packshot-stone-and-sand_4x5_v1.jpg,01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg,Somnila Evening Set: Lounge 01 pillows in Stone and Sand,Stone and Sand,packshot,4x5,800x1055
family-set,1,somnila_family-set_packshot-cloud_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg,Somnila Family Set: Neck 01 pillow in Cloud,Cloud,packshot,1x1,800x800
family-set,2,somnila_family-set_packshot-sky-2_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_bleu-clair_34_31.jpg,Somnila Family Set: Neck 01 pillow in Sky,Sky,packshot,1x1,800x800
family-set,3,somnila_family-set_packshot-stone-3_1x1_v1.jpg,09-oreiller-cervical/oreiller-cervical_gris_34_21.jpg,Somnila Family Set: Neck 01 pillow in Stone,Stone,packshot,1x1,800x800
quiet-night,1,somnila_quiet-night_packshot-black_1x1_v1.jpg,03-masque/masque_noir_face_05.jpg,Somnila Quiet Night: Mask 01 in Black,Black,packshot,1x1,800x800
quiet-night,2,somnila_quiet-night_packshot-blue-2_1x1_v1.jpg,04-bouchons/bouchons_bleu_boite_17.jpg,Somnila Quiet Night: Quiet 01 earplugs with case in Blue,Blue,packshot,1x1,800x800
throw-01,1,somnila_throw-01_detail-sand_4x3_v1.jpg,source/02-couverture/couverture_beige_lit_39.jpeg,"Somnila Throw 01 in Sand, detail on the bed",Sand,packshot,4x3,1200x900
throw-01,2,somnila_throw-01_detail-cream_4x3_v1.jpg,source/02-couverture/couverture_blanc-creme_lit_40.jpeg,"Somnila Throw 01 in Cream, detail on the bed",Cream,packshot,4x3,1200x900
throw-01,3,somnila_throw-01_detail-slate_4x3_v1.jpg,source/02-couverture/couverture_bleu-ardoise_lit_41.jpeg,"Somnila Throw 01 in Slate, detail on the bed",Slate,packshot,4x3,1200x900
throw-01,4,somnila_throw-01_detail-sky_4x3_v1.jpg,source/02-couverture/couverture_bleu-clair_lit_42.jpeg,"Somnila Throw 01 in Sky, detail on the bed",Sky,packshot,4x3,1200x900
throw-01,5,somnila_throw-01_detail-stone_4x3_v1.jpg,source/02-couverture/couverture_gris_lit_43.jpeg,"Somnila Throw 01 in Stone, detail on the bed",Stone,packshot,4x3,1200x900
throw-01,6,somnila_throw-01_detail-yellow_4x3_v1.jpg,source/02-couverture/couverture_jaune_lit_44.jpeg,"Somnila Throw 01 in Yellow, detail on the bed",Yellow,packshot,4x3,1200x900
throw-01,7,somnila_throw-01_detail-salmon_4x3_v1.jpg,source/02-couverture/couverture_orange-saumon_lit_45.jpeg,"Somnila Throw 01 in Salmon, detail on the bed",Salmon,packshot,4x3,1200x900
throw-01,8,somnila_throw-01_detail-blush_4x3_v1.jpg,source/02-couverture/couverture_rose_lit_46.jpeg,"Somnila Throw 01 in Blush, detail on the bed",Blush,packshot,4x3,1200x900
throw-01,9,somnila_throw-01_detail-lime_4x3_v1.jpg,source/02-couverture/couverture_vert-anis_lit_47.jpeg,"Somnila Throw 01 in Lime, detail on the bed",Lime,packshot,4x3,1200x900
throw-01,10,somnila_throw-01_detail-sage_4x3_v1.jpg,source/02-couverture/couverture_vert-sauge_lit_48.jpeg,"Somnila Throw 01 in Sage, detail on the bed",Sage,packshot,4x3,1200x900
```

---

# ▶ images/manifest.csv (photos du zip)

_Fichier : `build/images/manifest.csv`_

```csv
index,produit,coloris,angle,pixels,defaut,fichier_origine,fichier_classe
0,11-oreiller-corporel,rose-bleu,dessus,1440x1440,propre,09534216-2f04-4a87-a2d9-2c260a3f9c0a.JPG,source/11-oreiller-corporel/oreiller-corporel_rose-bleu_dessus_00.jpg
1,10-oreiller-lateral,bleu,3/4,800x800,"schema cotes chinois, 60 cm",16941f7b-f57e-40d1-93df-f7cb8fb09f92.JPG,source/10-oreiller-lateral/oreiller-lateral_bleu_34_01.jpg
2,12-oreiller-vague,bleu,lifestyle,790x790,"propre, decor enfantin",232071a0-c199-4037-bcb9-93a43a101247.JPG,source/12-oreiller-vague/oreiller-vague_bleu_lifestyle_02.jpg
3,03-masque,rose,face,800x800,propre,2841b032-ac3d-4aa5-b13f-c9f72d55755f.JPG,source/03-masque/masque_rose_face_03.jpg
4,03-masque,blanc,face,800x800,propre,292e3443-8750-45f9-b54c-599e68b751ee.JPG,source/03-masque/masque_blanc_face_04.jpg
5,03-masque,noir,face,800x800,propre,3416dafb-f29d-461a-bc9d-6deb4345e663.JPG,source/03-masque/masque_noir_face_05.jpg
6,09-oreiller-cervical,bleu-marine,3/4,800x800,caractere chinois,420d1392-0383-4148-97c6-c811967da496.JPG,source/09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg
7,11-oreiller-corporel,bleu-clair,dessus,800x800,propre,444d7f6a-4048-41eb-ab17-8c18e5d48025.JPG,source/11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_07.jpg
8,12-oreiller-vague,blanc,3/4,800x800,FAUX BADGES Best Pillow 2025,4a130d94-98b1-4081-8a04-0bcf8ef6ade0.JPG,source/12-oreiller-vague/oreiller-vague_blanc_34_08.jpg
9,03-masque,blanc,face,400x388,basse definition 400 px,4c6e203c-3bf3-4dc3-92ce-e9adfbfe6282.JPG,source/03-masque/masque_blanc_face_09.jpg
10,12-oreiller-vague,rose-blanc,3/4,800x800,FAUX BADGES,4c71b046-6101-4756-a059-2ddfdb7c2a07.JPG,source/12-oreiller-vague/oreiller-vague_rose-blanc_34_10.jpg
11,12-oreiller-vague,gris-blanc,3/4,800x800,FAUX BADGES,5b37ae99-6f2e-4683-8fa4-9619a0713068.JPG,source/12-oreiller-vague/oreiller-vague_gris-blanc_34_11.jpg
12,12-oreiller-vague,gris,3/4,800x800,FAUX BADGES,5b7b178a-f288-422b-9bce-aedb58fd2be2.JPG,source/12-oreiller-vague/oreiller-vague_gris_34_12.jpg
13,12-oreiller-vague,bleu-marine,3/4,800x800,propre,5ea8edbe-046a-4812-a7a7-fd56f441b9dd.JPG,source/12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg
14,04-bouchons,vert,boite,800x800,marque tierce iMeBoBo + chinois,639ebae4-df02-404a-ad05-357a0178dde2.JPG,source/04-bouchons/bouchons_vert_boite_14.jpg
15,12-oreiller-vague,rose,lifestyle,1440x1440,"propre, decor enfantin",64514ad5-d42c-4178-8a6b-06fd38f92b47.JPG,source/12-oreiller-vague/oreiller-vague_rose_lifestyle_15.jpg
16,03-masque,noir,face,800x800,propre,64f61d2a-dd07-4021-a599-799bcc279a99.JPG,source/03-masque/masque_noir_face_16.jpg
17,04-bouchons,bleu,boite,800x800,marque tierce iMeBoBo + chinois,6524be4f-2efd-4268-898e-a460c1602fa5.JPG,source/04-bouchons/bouchons_bleu_boite_17.jpg
18,11-oreiller-corporel,gris,dessus,800x800,propre,68bc5d29-5f87-4f38-a3f1-b8f7d6946c05.JPG,source/11-oreiller-corporel/oreiller-corporel_gris_dessus_18.jpg
19,04-bouchons,jaune-lait,boite,800x800,marque tierce iMeBoBo + chinois,711de4c6-5d30-4c68-af2c-c1bef5c7e1b7.JPG,source/04-bouchons/bouchons_jaune-lait_boite_19.jpg
20,03-masque,violet-blanc,face,800x800,propre,729a2bdb-a155-4661-97b6-f29b23234140.JPG,source/03-masque/masque_violet-blanc_face_20.jpg
21,09-oreiller-cervical,gris,3/4,800x800,caractere chinois,760784d5-7c7a-48aa-9daf-954639073e24.JPG,source/09-oreiller-cervical/oreiller-cervical_gris_34_21.jpg
22,12-oreiller-vague,bleu,3/4,800x800,FAUX BADGES,7b18201a-93d2-4f59-8175-792590cc66c0 2.JPG,source/12-oreiller-vague/oreiller-vague_bleu_34_22.jpg
23,12-oreiller-vague,bleu,3/4,800x800,FAUX BADGES (doublon de 22),7b18201a-93d2-4f59-8175-792590cc66c0.JPG,source/12-oreiller-vague/oreiller-vague_bleu_34_23.jpg
24,11-oreiller-corporel,rose,dessus,800x800,propre,7bdf254a-8dab-467e-8b14-0d209bd42895.JPG,source/11-oreiller-corporel/oreiller-corporel_rose_dessus_24.jpg
25,01-oreiller-telephone,bleu,3/4,800x979,texte MULTICOLOURED + chinois,80ed28da-43c3-4a6d-9dd1-7adccb53872d.JPG,source/01-oreiller-telephone/oreiller-telephone_bleu_34_25.jpg
26,10-oreiller-lateral,gris-fonce,3/4,800x800,"schema cotes, 60 cm",8cba63d6-9fe7-4c1c-81ee-bb03d80260f9.JPG,source/10-oreiller-lateral/oreiller-lateral_gris-fonce_34_26.jpg
27,10-oreiller-lateral,rouge,3/4,800x800,"schema cotes, 60 cm",8fe752db-1aa7-4921-b8e6-d3a71d2e01e7.JPG,source/10-oreiller-lateral/oreiller-lateral_rouge_34_27.jpg
28,04-bouchons,rose,boite,800x800,marque tierce iMeBoBo + chinois,IMG_5222.JPG,source/04-bouchons/bouchons_rose_boite_28.jpg
29,11-oreiller-corporel,bleu-rose,dessus,1440x1440,propre,a1f66692-fd88-4862-a1b0-36d34680c474.JPG,source/11-oreiller-corporel/oreiller-corporel_bleu-rose_dessus_29.jpg
30,12-oreiller-vague,blanc,lifestyle,1440x1440,"propre, decor enfantin",a9ff7284-f014-4355-bdbf-540663d98efd.JPG,source/12-oreiller-vague/oreiller-vague_blanc_lifestyle_30.jpg
31,09-oreiller-cervical,bleu-clair,3/4,800x800,propre,ad7155fe-8f39-4ca3-a82b-8b287f4972e6.JPG,source/09-oreiller-cervical/oreiller-cervical_bleu-clair_34_31.jpg
32,01-oreiller-telephone,noir,3/4,800x800,texte chinois + schema cotes + vignettes avec visages,b3a6c5aa-b61c-49a2-b2e0-2f0a858ef989.JPG,source/01-oreiller-telephone/oreiller-telephone_noir_34_32.jpg
33,10-oreiller-lateral,rose,3/4,800x800,"schema cotes, VARIANTE 50 cm ecartee",b4a8a422-5c68-40d2-950d-d4a9ab4d7414.JPG,source/10-oreiller-lateral/oreiller-lateral_rose_34_33.jpg
34,01-oreiller-telephone,gris-blanc,3/4,800x800,texte chinois + schema cotes + vignettes avec visages,b75f0be9-fd40-4af0-bbfa-8af6922537a0.JPG,source/01-oreiller-telephone/oreiller-telephone_gris-blanc_34_34.jpg
35,10-oreiller-lateral,gris-clair,3/4,800x800,"schema cotes, VARIANTE 50 cm ecartee",bd8e52f3-88b6-4fdd-bfe3-b3333356fdf0.JPG,source/10-oreiller-lateral/oreiller-lateral_gris-clair_34_35.jpg
36,01-oreiller-telephone,gris + beige,3/4 duo,800x1055,propre,c6828354-3f21-4f74-b446-bfbcff59c665.JPG,source/01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg
37,12-oreiller-vague,bleu-marine,3/4,800x800,propre,cb19c479-434c-4b2f-bb26-252c54e62f94.JPG,source/12-oreiller-vague/oreiller-vague_bleu-marine_34_37.jpg
38,03-masque,gris-chine,face,800x800,propre,cc9a1ba7-035a-4a59-b82e-a70b5625d389.JPG,source/03-masque/masque_gris-chine_face_38.jpg
39,02-couverture,beige,lit,694x635,visage + interieur stock,couverture-effet-fourrure-beige.jpeg,source/02-couverture/couverture_beige_lit_39.jpeg
40,02-couverture,blanc-creme,lit,800x800,visage + interieur stock,couverture-effet-fourrure-blanc-creme.jpeg,source/02-couverture/couverture_blanc-creme_lit_40.jpeg
41,02-couverture,bleu-ardoise,lit,691x625,visage + interieur stock,couverture-effet-fourrure-bleu-ardoise.jpeg,source/02-couverture/couverture_bleu-ardoise_lit_41.jpeg
42,02-couverture,bleu-clair,lit,696x629,visage + interieur stock,couverture-effet-fourrure-bleu-clair.jpeg,source/02-couverture/couverture_bleu-clair_lit_42.jpeg
43,02-couverture,gris,lit,695x634,visage + interieur stock,couverture-effet-fourrure-gris.jpeg,source/02-couverture/couverture_gris_lit_43.jpeg
44,02-couverture,jaune,lit,739x780,visage + interieur stock,couverture-effet-fourrure-jaune.jpeg,source/02-couverture/couverture_jaune_lit_44.jpeg
45,02-couverture,orange-saumon,lit,736x774,visage + interieur stock,couverture-effet-fourrure-orange-saumon.jpeg,source/02-couverture/couverture_orange-saumon_lit_45.jpeg
46,02-couverture,rose,lit,695x634,visage + interieur stock,couverture-effet-fourrure-rose.jpeg,source/02-couverture/couverture_rose_lit_46.jpeg
47,02-couverture,vert-anis,lit,690x630,visage + interieur stock,couverture-effet-fourrure-vert-anis.jpeg,source/02-couverture/couverture_vert-anis_lit_47.jpeg
48,02-couverture,vert-sauge,lit,694x635,visage + interieur stock,couverture-effet-fourrure-vert-sauge.jpeg,source/02-couverture/couverture_vert-sauge_lit_48.jpeg
49,11-oreiller-corporel,bleu-marine,dessus,1141x1141,propre,d2412814-d89d-43f9-9673-35a7f2ae1e00.JPG,source/11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg
50,11-oreiller-corporel,bleu-clair,dessus,800x800,propre,d41ff7c1-f89a-4ff8-b7e8-a61f9b4dc001.JPG,source/11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_50.jpg
51,09-oreiller-cervical,blanc,3/4,800x800,propre,dda1093c-dc5c-4d50-9c30-014e8f2503d1.JPG,source/09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg
52,01-oreiller-telephone,rose,3/4,800x800,texte chinois + schema cotes + vignettes avec visages,eaf62fe0-2cc4-415c-9af2-e9adb964e3d1.JPG,source/01-oreiller-telephone/oreiller-telephone_rose_34_52.jpg
53,11-oreiller-corporel,bleu-tres-clair,dessus,800x800,propre,eefb333b-4eaa-456b-81e6-22b3ba3448c8.JPG,source/11-oreiller-corporel/oreiller-corporel_bleu-tres-clair_dessus_53.jpg
54,10-oreiller-lateral,gris-fonce,3/4,800x800,"schema cotes, 60 cm",f0a7be61-f7ce-4ff2-af21-969dd8d18a9e.JPG,source/10-oreiller-lateral/oreiller-lateral_gris-fonce_34_54.jpg
55,01-oreiller-telephone,jaune,3/4,800x800,texte chinois + schema cotes + vignettes avec visages,fe49b7f2-8e8e-43dc-8c78-8fd1d2e3b9ec.JPG,source/01-oreiller-telephone/oreiller-telephone_jaune_34_55.jpg
```

---

# ▶ devis_fournisseur.txt

_Fichier : `build/devis_fournisseur.txt`_

```text

===== PAGE 1 (images:21) =====
QUOTATION — MODÈLES SÉLECTIONNÉS
Nom du produit
Photos des variantes
Détails
Variante retenue
Poids (kg)
Prix
Délai de livraison
Oreiller ergonomique pour
téléphone au lit
– Oreiller incliné conçu pour une utilisation confortable au lit.
– Dossier surélevé avec soutien de la tête et de la nuque.
– Forme enveloppante avec zones d'appui pour les bras.
60 × 37 × 23 cm
Coloris : bleu clair,
gris, beige, rose, vert,
jaune, noir
1,1
6–10 jours
Couverture effet fourrure de
lapin - texture bulles
– Couverture épaisse et moelleuse à effet fourrure de lapin.
– Surface gaufrée avec motif en relief de type bulles.
– Conçue pour le lit et les moments de détente.
3,2
6–10 jours
Masque de sommeil 3D
ajustable
– Masque occultant avec cavités 3D autour des yeux.
– Conception sans pression directe sur les paupières.
– Bande de maintien réglable pour le sommeil et le voyage.
L — 57 × 8,5 cm
Coloris illustrés : noir,
violet, gris chiné, gris
clair, bleu marine,
rose, blanc
0,07
6–10 jours
Bouchons d'oreilles anti-bruit
avec étui
– Bouchons d'oreilles réutilisables pour le sommeil et la concentration.
– Forme compacte et ergonomique avec boîte de rangement rigide.
– Présentation illustrée : lot de 4 bouchons, soit 2 paires.
4 pièces (2 paires)
Coloris : bleu, vert,
jaune lait, rose
0,02
6–10 jours
La plus grande taille proposée a été retenue. Les photos détaillées des coloris figurent en annexe.
Page 1 sur 9
19,50 €
19,00 €
6,00 €
6,00 €
200 × 230 cm
10 coloris illustrés
(voir annexe)

===== PAGE 2 (images:20) =====
QUOTATION — MODÈLES SÉLECTIONNÉS
Nom du produit
Photos des variantes
Détails
Variante retenue
Poids (kg)
Prix
Délai de livraison
Housse en coton pour oreiller
corporel Snuggi
– Housse adaptée à la forme courbe de l'oreiller corporel Snuggi.
– Lavable en machine.
– Tissu respirant, frais et doux au contact de la peau.
120 cm
Coloris fournisseur :
bleu, gris, rose,
violet, marron, noir
1,8
6–10 jours
Housse rafraîchissante pour
oreiller Cloudii
– Housse ajustée à la forme ergonomique de l'oreiller Cloudii.
– Surface douce et respirante au toucher frais.
– Conçue pour conserver une sensation de fraîcheur pendant la nuit.
68 × 37 × 11,5 cm
Coloris : blanc, gris,
bleu, bleu marine,
rose
1,2
6–10 jours
Housse d'oreiller Derila Ergo
rafraîchissante
– Housse profilée pour l'oreiller ergonomique Derila Ergo.
– Technologie de gel rafraîchissant et évacuation de l'humidité.
– Toucher doux, confort ajusté et tissu adapté aux peaux sensibles.
63 × 39 × 13 cm
Coloris illustrés : bleu,
blanc, bleu marine,
rose
1,3
6–10 jours
Housse d'oreiller Derila
– Housse conçue pour épouser précisément la forme de l'oreiller Derila.
– Ajustement près du produit sans excès de tissu.
– Entretien facile, sensation fraîche et format pratique à transporter.
60 × 35 × 10 cm
Coloris illustrés : bleu,
rouge, gris foncé
0,8
6–10 jours
Page 2 sur 9
3,00 €
3,00 €
3,00 €
3,00 €
Produits 05 à 08 : housses vendues séparément, à l'unité.

===== PAGE 3 (images:18) =====
QUOTATION — MODÈLES SÉLECTIONNÉS
Nom du produit
Photos des variantes
Détails
Variante retenue
Poids (kg)
Prix
Délai de livraison
Oreiller ergonomique de
soutien cervical Derila
– Forme ergonomique profilée pour soutenir la nuque et les cervicales.
– Conçu pour limiter les tensions musculaires et améliorer le confort.
– Technologie rafraîchissante et soutien adapté aux positions de sommeil.
62 × 42 × 13/11 cm
Coloris fournisseur :
bleu, gris, rose,
violet, marron, noir
1,4
25,00 €
6–10 jours
Oreiller Derila pour dormeurs
latéraux
– Oreiller allongé conçu pour le sommeil sur le côté.
– Mousse à mémoire de forme pour accompagner la posture du corps.
– Soutien de la nuque, des épaules et du dos avec adaptation progressive.
60 cm
Coloris fournisseur :
rose, jaune, rouge,
bleu, gris
20,00 €
6–10 jours
Oreiller corporel
ergonomique Snuggi
– Oreiller corporel courbé en S avec soutien en 3 zones : épaules, hanches
et genoux.
– Forme ergonomique douce et stable, conçue pour conserver son volume.
– Housse amovible lavable et tissu respirant au toucher frais.
– Dimensions de référence visibles : 105 cm de long x 30 cm de large.
120 cm
Coloris fournisseur :
bleu, gris, rose,
violet, marron, noir
1,8
24,00 €
6–10 jours
Oreiller confort ergonomique
Cloudii
– Oreiller profilé soutenant simultanément la tête, la nuque et les épaules.
– Double hauteur réversible pour s'adapter à différentes positions de
sommeil.
– Surface au toucher frais, housse lavable et structure conçue pour garder
sa forme.
– Conception favorisant l'alignement de la nuque et de la colonne
vertébrale.
60 × 35 × 10 cm
Coloris : blanc, gris,
bleu, bleu marine,
rose
1,1
19,00 €
6–10 jours
Page 3 sur 9
Produits 09 à 12 : kits coussin avec une housse incluse ; le coloris choisi correspond à cette housse.
Derila et Cloudii : modèles visuellement très proches, mais dimensions, poids et prix différents - à confirmer avec le fournisseur.

===== PAGE 4 (images:16) =====
ANNEXE — PHOTOS DES VARIANTES RETENUES
TAILLES LES PLUS GRANDES UNIQUEMENT
01. Oreiller ergonomique pour téléphone au lit
Variante retenue : 60 × 37 × 23 cm
Coloris : bleu clair, gris, beige, rose, vert, jaune, noir    Poids : 1,1 kg    Prix :
   Livraison : 6–10 jours
Bleu clair — vue générale
Gris et beige
Rose
Vert
Jaune
Noir
Page 4 sur 9
19,50 €
02. Couverture effet fourrure de lapin - texture bulles
Variante retenue : 200 × 230 cm
Coloris illustrés : 10 coloris    Poids : 3,2 kg    Prix : 19,00 €    Livraison : 6-10 jours
Blanc crème
Rose
Beige
Vert anis
Vert sauge
Bleu ardoise
Bleu clair
Jaune
Gris
Orange saumon

===== PAGE 5 (images:11) =====
ANNEXE — PHOTOS DES VARIANTES RETENUES
TAILLES LES PLUS GRANDES UNIQUEMENT
03. Masque de sommeil 3D ajustable
Variante retenue : L — 57 × 8,5 cm
Coloris illustrés : noir, violet, gris chiné, gris clair, bleu marine, rose, blanc    Poids : 0,07 kg    Prix :
   Livraison : 6–10 jours
Noir
Violet
Gris chiné
Gris clair
Bleu marine
Rose
Blanc
04. Bouchons d'oreilles anti-bruit avec étui
Variante retenue : 4 pièces (2 paires)
Coloris : bleu, vert, jaune lait, rose    Poids : 0,02 kg    Prix :
   Livraison : 6–10 jours
Bleu — 4 pièces
Vert — 4 pièces
Jaune lait — 4 pièces
Rose — 4 pièces
Les quatre coloris envoyés par le fournisseur sont inclus : bleu, vert, jaune lait et rose. Chaque boîte contient 4 bouchons, soit 2 paires.
Page 5 sur 9
6,00 €
6,00 €

===== PAGE 6 (images:13) =====
ANNEXE — PHOTOS DES VARIANTES RETENUES
TAILLES LES PLUS GRANDES UNIQUEMENT
05. Housse en coton pour oreiller corporel Snuggi
Variante retenue : 120 cm
Coloris fournisseur : bleu, gris, rose, violet, marron, noir    Poids : 1,8 kg    Prix :
   Livraison : 6–10 jours
Bleu clair
Rose
Bleu ciel
Gris
Bleu très clair
Bleu marine
Vert menthe
Beige / abricot
06. Housse rafraîchissante pour oreiller Cloudii
Variante retenue : 68 × 37 × 11,5 cm
Coloris : blanc, gris, bleu, bleu marine, rose    Poids : 1,2 kg    Prix :
   Livraison : 6–10 jours
Gris
Blanc
Bleu
Rose
Bleu marine
Page 6 sur 9
3,00 €
3,00 €

===== PAGE 7 (images:9) =====
ANNEXE — PHOTOS DES VARIANTES RETENUES
TAILLES LES PLUS GRANDES UNIQUEMENT
07. Housse d'oreiller Derila Ergo rafraîchissante
Variante retenue : 63 × 39 × 13 cm
Coloris illustrés : bleu, blanc, bleu marine, rose    Poids : 1,3 kg    Prix :
   Livraison : 6–10 jours
Bleu — vue produit
Blanc — vue produit
Bleu marine
Rose — mise en scène
Blanc — mise en scène
Bleu — mise en scène
08. Housse d'oreiller Derila
Variante retenue : 60 × 35 × 10 cm
Coloris illustrés : bleu, rouge, gris foncé    Poids : 0,8 kg    Prix :
   Livraison : 6–10 jours
Bleu — 60 cm
Rouge — 60 cm
Gris foncé — 60 cm
Seules les photos marquées 60 cm ont été conservées ; les variantes 50 cm ont été écartées. Le PDF indique 60 × 35 × 10 cm, tandis que les photos affichent 60 × 33 × 10 cm : dimension à confirmer.
Page 7 sur 9
3,00 €
3,00 €

===== PAGE 8 (images:7) =====
ANNEXE — PHOTOS DES VARIANTES RETENUES
TAILLES LES PLUS GRANDES UNIQUEMENT
09. Oreiller ergonomique de soutien cervical Derila
Variante retenue : 62 × 42 × 13/11 cm
Coloris fournisseur : bleu, gris, rose, violet, marron, noir    Poids : 1,4 kg    Prix : 25,00 €    Livraison : 6–10 jours
Bleu marine
Blanc
Gris
Bleu clair
10. Oreiller Derila pour dormeurs latéraux
Variante retenue : 60 cm
Coloris fournisseur : rose, jaune, rouge, bleu, gris    Poids : non renseigné    Prix : 20,00 €    Livraison : 6–10 jours
Bleu — 60 cm
Rouge — 60 cm
Gris foncé — 60 cm
Le poids du modèle 60 cm n’était pas renseigné dans le PDF du fournisseur ; la case reste vide.
Page 8 sur 9

===== PAGE 9 (images:13) =====
ANNEXE — PHOTOS DES VARIANTES RETENUES
TAILLES LES PLUS GRANDES UNIQUEMENT
11. Oreiller corporel ergonomique Snuggi
Variante retenue : 120 cm
Coloris fournisseur : bleu, gris, rose, violet, marron, noir    Poids : 1,8 kg    Prix : 24,00 €    Livraison : 6–10 jours
Bleu clair
Rose
Bleu ciel
Gris
Bleu très clair
Bleu marine
Vert menthe
Beige / abricot
12. Oreiller confort ergonomique Cloudii
Variante retenue : 60 × 35 × 10 cm
Coloris : blanc, gris, bleu, bleu marine, rose    Poids : 1,1 kg    Prix : 19,00 €    Livraison : 6–10 jours
Gris
Blanc
Bleu
Rose
Bleu marine
Page 9 sur 9
```



# ══════ PARTIE 9 — THÈME (fichiers envoyés au thème Somnila — build v1) ══════


---

# ▶ theme/config/settings_data.json

_Fichier : `build/theme/config/settings_data.json`_

```json
{
  "current": {
    "animations_type": "GGkLhoTOiV67l21Pb1r8JxbwGAkXLmer7YrABSJ9+A9EXpMu2rSrjF9lHa0vqrWGeeDHu7qtpr+mgxIPPKrM0ejIby9ZNuJF4dFk6amcBZ0jotWApqjdOhQIhMWQVZ0794EEN3Gp6q+hiFhBjWHj1+pTBR3xtiz1jODSHRCNTCGlXN7Iu8CDFs/VLut3g5H43vDSZMIwAJMurqV3IK5GOHTrH1NdIVG0H3QcA9//zSQlxswDRMsm5bamaw9MygihDMlZQ6QlPFSP2VFmaUrRhvwHgDWkOcFtLkvV1HQqnzdRA3AbzmzffCiXn1Gkd7DwMBp/kXuCvSCHt9TT0ZQbA5CyZBX5SXu5n3utfkf4ZEYF+ckSufFydtJWhrRuDGuKYruLRto9jNPdruIZvchs7Q==",
    "disable_inspect": false,
    "country_list_function": "block",
    "country_list": "",
    "logo": "shopify://shop_images/somnila-logo-light.png",
    "logo_width": 160,
    "mobile_logo_width": 120,
    "favicon": "shopify://shop_images/somnila-favicon-512.png",
    "colors_solid_button_labels": "#F7F9FC",
    "colors_accent_1": "#1E2A3A",
    "gradient_accent_1": "",
    "colors_accent_2": "#6B7D90",
    "gradient_accent_2": "",
    "colors_text": "#1E2A3A",
    "colors_outline_button_labels": "#1E2A3A",
    "colors_background_1": "#F7F9FC",
    "gradient_background_1": "",
    "colors_background_2": "#DCE8F2",
    "gradient_background_2": "",
    "type_header_font": "sans_serif_n4",
    "heading_scale": 110,
    "heading_letter_spacing": 0.0,
    "type_body_font": "sans_serif_n4",
    "body_scale": 100,
    "enable_load_animations": false,
    "repeat_section_animations": false,
    "badge_position": "top left",
    "badge_corner_radius": 20,
    "sale_badge_color_scheme": "accent-1",
    "sale_badge_text": "Save [percentage]",
    "sold_out_badge_color_scheme": "background-1",
    "accent_icons": "accent-1",
    "product_cards_badge_push_sides": true,
    "product_cards_custom_badges_list": "",
    "page_width": 1400,
    "spacing_sections": 0,
    "spacing_grid_horizontal": 24,
    "spacing_grid_vertical": 32,
    "link_btn_hover": "arrow",
    "action_btn_hover": "center",
    "buttons_border_thickness": 1,
    "buttons_border_opacity": 100,
    "buttons_radius": 40,
    "buttons_shadow_opacity": 0,
    "buttons_shadow_horizontal_offset": 0,
    "buttons_shadow_vertical_offset": 0,
    "buttons_shadow_blur": 0,
    "variant_pills_accent_color": "accent-1",
    "variant_pills_bold_text": false,
    "variant_pills_border_thickness": 1,
    "variant_pills_border_opacity": 30,
    "variant_pills_radius": 40,
    "variant_pills_shadow_opacity": 0,
    "variant_pills_shadow_horizontal_offset": 0,
    "variant_pills_shadow_vertical_offset": 4,
    "variant_pills_shadow_blur": 5,
    "pickers_border_color": "text",
    "pickers_text_color": "text",
    "pickers_overlay_color": "accent-1",
    "pickers_overlay_opacity": 0,
    "pickers_border_thickness": 1,
    "pickers_border_opacity": 20,
    "pickers_radius": 22,
    "pickers_hover_overlay_opacity": 4,
    "pickers_hover_border_opacity": 55,
    "quantity_color_scheme": "background-1",
    "quantity_border_color": "text",
    "quantity_text_color": "text",
    "quantity_overlay_color": "accent-1",
    "quantity_overlay_opacity": 0,
    "quantity_border_thickness": 1,
    "quantity_border_opacity": 20,
    "quantity_radius": 22,
    "quantity_hover_overlay_opacity": 4,
    "inputs_border_thickness": 1,
    "inputs_border_opacity": 30,
    "inputs_radius": 22,
    "inputs_shadow_opacity": 0,
    "inputs_shadow_horizontal_offset": 0,
    "inputs_shadow_vertical_offset": 4,
    "inputs_shadow_blur": 5,
    "card_style": "card",
    "card_image_padding": 0,
    "card_text_alignment": "left",
    "card_color_scheme": "background-1",
    "card_border_thickness": 0,
    "card_border_opacity": 0,
    "card_corner_radius": 28,
    "card_shadow_opacity": 10,
    "card_shadow_horizontal_offset": 0,
    "card_shadow_vertical_offset": 20,
    "card_shadow_blur": 40,
    "collection_card_style": "card",
    "collection_card_image_padding": 0,
    "collection_card_text_alignment": "left",
    "collection_card_color_scheme": "background-2",
    "collection_card_border_thickness": 0,
    "collection_card_border_opacity": 0,
    "collection_card_corner_radius": 28,
    "collection_card_shadow_opacity": 0,
    "collection_card_shadow_horizontal_offset": 2,
    "collection_card_shadow_vertical_offset": 6,
    "collection_card_shadow_blur": 15,
    "blog_card_style": "standard",
    "blog_card_image_padding": 0,
    "blog_card_text_alignment": "left",
    "blog_card_color_scheme": "background-1",
    "blog_card_border_thickness": 0,
    "blog_card_border_opacity": 10,
    "blog_card_corner_radius": 28,
    "blog_card_shadow_opacity": 0,
    "blog_card_shadow_horizontal_offset": 0,
    "blog_card_shadow_vertical_offset": 6,
    "blog_card_shadow_blur": 20,
    "text_boxes_border_thickness": 0,
    "text_boxes_border_opacity": 0,
    "text_boxes_radius": 28,
    "text_boxes_shadow_opacity": 0,
    "text_boxes_shadow_horizontal_offset": 0,
    "text_boxes_shadow_vertical_offset": 12,
    "text_boxes_shadow_blur": 20,
    "media_border_thickness": 0,
    "media_border_opacity": 0,
    "media_radius": 28,
    "media_shadow_opacity": 10,
    "media_shadow_horizontal_offset": 0,
    "media_shadow_vertical_offset": 20,
    "media_shadow_blur": 40,
    "popup_border_thickness": 0,
    "popup_border_opacity": 0,
    "popup_corner_radius": 28,
    "popup_shadow_opacity": 15,
    "popup_shadow_horizontal_offset": 0,
    "popup_shadow_vertical_offset": 20,
    "popup_shadow_blur": 40,
    "drawer_border_thickness": 0,
    "drawer_border_opacity": 0,
    "drawer_shadow_opacity": 15,
    "drawer_shadow_horizontal_offset": 0,
    "drawer_shadow_vertical_offset": 0,
    "drawer_shadow_blur": 40,
    "brand_headline": "Sleep well.",
    "brand_description": "<p>Pillows and sleep accessories shaped around the way you actually lie. Foam that holds its shape, covers you can wash, 30 nights to decide.</p>",
    "brand_image_width": 55,
    "social_facebook_link": "",
    "social_instagram_link": "",
    "social_youtube_link": "",
    "social_tiktok_link": "",
    "social_twitter_link": "",
    "social_snapchat_link": "",
    "social_pinterest_link": "",
    "social_tumblr_link": "",
    "social_vimeo_link": "",
    "predictive_search_enabled": true,
    "predictive_search_show_vendor": false,
    "predictive_search_show_price": true,
    "currency_code_enabled": false,
    "scrollbar_style": "default",
    "scrollbar_thumb_color": "#7FA6BE",
    "scrollbar_width": 9,
    "cart_type": "drawer",
    "cart_icon": "bag_1",
    "show_vendor": false,
    "show_cart_note": false,
    "cart_drawer_collection": "accessories",
    "fav_collection": "GGkLhoTOiV67l21Pb1r8JxbwGAkXLmer7YrABSJ9+A9EXpMu2rSrjF9lHa0vqrWGeeDHu7qtpr+mgxIPPKrM0ejIby9ZNuJF4dFk6amcBZ0jotWApqjdOhQIhMWQVZ0794EEN3Gp6q+hiFhBjWHj1+pTBR3xtiz1jODSHRCNTCGlXN7Iu8CDFs/VLut3g5H43vDSZMIwAJMurqV3IK5GOHTrH1NdIVG0H3QcA9//zSQlxswDRMsm5bamaw9MygihDMlZQ6QlPFSP2VFmaUrRhvwHgDWkOcFtLkvV1HQqnzdRA3AbzmzffCiXn1Gkd7DwMBp/kXuCvSCHt9TT0ZQbA5CyZBX5SXu5n3utfkf4ZEYF+ckSufFydtJWhrRuDGuKYruLRto9jNPdruIZvchs7Q==",
    "sections": {
      "main-password-header": {
        "type": "main-password-header",
        "settings": {
          "color_scheme": "background-1"
        }
      },
      "main-password-footer": {
        "type": "main-password-footer",
        "settings": {
          "color_scheme": "background-1"
        }
      },
      "promo-popup": {
        "type": "promo-popup",
        "settings": {
          "mode": "disabled",
          "popup_seconds": 8,
          "popup_days": 30,
          "display_timer": false,
          "timer_duration": 3,
          "layout": "image_second",
          "color_scheme": "background-2",
          "heading_prefix": "",
          "heading": "Notes from the workshop",
          "heading_size": "h1",
          "heading_suffix": "",
          "text": "<p>One email a month at most.</p>",
          "button_label": "Sign up",
          "dismiss_btn_label": "Non merci",
          "discount_code": "",
          "success_heading_prefix": "",
          "success_heading": "MERCI",
          "success_heading_size": "h1",
          "success_heading_suffix": "",
          "success_text": "<p>Vous recevrez le prochain envoi.</p>",
          "discount_code_label": "",
          "copy_button_label": "Copier",
          "copy_message": "",
          "success_dismiss_btn_label": "Fermer",
          "success_display_image": true
        }
      },
      "scroll-to-top-btn": {
        "type": "scroll-to-top-btn",
        "settings": {
          "enable_scroll_btn": true,
          "display_after": 500,
          "color_scheme": "accent-1",
          "position": "bottom-right",
          "offset_x": 20,
          "offset_y": 20
        }
      },
      "global-music-player": {
        "type": "global-music-player",
        "settings": {
          "enabled": false,
          "audio_src": "",
          "volume": 10,
          "position": "bottom-left",
          "offset_x": 20,
          "offset_y": 20,
          "btn_animation": true,
          "color_scheme": "accent-1"
        }
      },
      "cart-drawer": {
        "type": "cart-drawer",
        "blocks": {
          "items": {
            "type": "cart_items",
            "settings": {
              "image_size": "20",
              "image_link": true,
              "title_size": "1.5",
              "title_link": true,
              "displayed_variants": "compact",
              "prices_position": "right",
              "displayed_compare_prices": "product",
              "price_color": "accent-1",
              "compare_price_color": "text",
              "display_single_item_prices": true,
              "enable_savings": true,
              "savings_text": "<strong>(you save [amount])</strong>",
              "savings_color": "text",
              "quantity_font_size": 14,
              "quantity_container_padding": 0,
              "quantity_corner_radius": 22,
              "quantity_border_width": 1,
              "quantity_border_color": "#C5D2DE",
              "quantity_container_color_scheme": "background-2",
              "quantity_input_padding": 0.7,
              "quantity_separators_opacity": 20,
              "quantity_padding": 0.4,
              "quantity_btns_color_scheme": "background-2",
              "quantity_round_btns": true,
              "quantity_outline_btns": false,
              "quantity_btns_icon_size": 70,
              "margin_top": 18,
              "margin_bottom": 18
            }
          },
          "discount": {
            "type": "discount_field",
            "settings": {
              "bottom_separator": true,
              "placeholder": "Discount code",
              "btn_label": "Apply",
              "error_msg": "Enter a discount code.",
              "margin_top": 12,
              "margin_bottom": 12
            }
          },
          "subtotals": {
            "type": "subtotals",
            "settings": {
              "display_total_savings": true,
              "savings_left_text": "<strong>You save</strong>",
              "savings_right_text": "<strong>-[savings]</strong>",
              "savings_alignment": "spaced",
              "savings_text_color": "accent-1",
              "savings_text_size": 15,
              "savings_position": "above",
              "savings_spacing": 10,
              "display_subtotal": true,
              "subtotal_left_text": "<strong>Subtotal</strong>",
              "subtotal_right_text": "<strong>[subtotal]</strong>",
              "subtotal_alignment": "spaced",
              "subtotal_text_color": "text",
              "subtotal_text_size": 20,
              "display_discounts": true,
              "discounts_label": "<strong>Discounts</strong>",
              "discounts_alignment": "flex-start",
              "margin_top": 12,
              "margin_bottom": 12
            }
          },
          "checkout": {
            "type": "checkout_btn",
            "settings": {
              "show_additional_checkout_buttons": true,
              "display_price": true,
              "enable_custom_color": false,
              "icon_scale": 120,
              "icon_spacing": 10,
              "margin_top": 12,
              "margin_bottom": 12
            }
          },
          "badges": {
            "type": "payment_badges",
            "settings": {
              "enabled_payment_types": "visa, master, american_express, paypal, apple_pay, google_pay, shopify_pay",
              "margin_top": 9,
              "margin_bottom": 9
            }
          }
        },
        "block_order": [
          "items",
          "discount",
          "subtotals",
          "checkout",
          "badges"
        ],
        "settings": {
          "test_mode": false,
          "heading_text": "Your bag · [count]",
          "heading_alignment": "flex-start",
          "desktop_width": "normal",
          "mobile_width": "full",
          "enable_header_bg": false,
          "header_bg_color": "#DCE8F2",
          "enable_body_bg": false,
          "body_bg_color": "#DCE8F2",
          "enable_footer_bg": true,
          "footer_bg_color": "#DCE8F2"
        }
      }
    },
    "content_for_index": [],
    "secondary_logo": "shopify://shop_images/somnila-logo-dark.png",
    "custom_header_font_link": "",
    "custom_header_font_name": "Custom headings font",
    "custom_header_font_weight": 400,
    "heading_line_height": 1.2,
    "custom_body_font_link": "",
    "custom_body_font_name": "Custom body font",
    "custom_body_font_weight": 400,
    "custom_body_bold_font_link": "",
    "body_line_height": 1.7,
    "body_letter_spacing": 0.0,
    "sale_basge_discount_icon": false,
    "product_card_badge_position": "top left",
    "product_card_title_limited_lines": "2",
    "card_button_style": "primary",
    "swatches_border_radius": 100,
    "swatches_border_opacity": 10,
    "swatches_selected_border_opacity": 100,
    "variant_pills_inactive_overlay_opacity": 0,
    "variant_pills_text_size": 14,
    "variant_pills_padding_y": 10,
    "variant_pills_padding_x": 20,
    "pickers_color_scheme": "background-1",
    "pickers_shadow_opacity": 0,
    "quantity_shadow_opacity": 0,
    "quantity_hover_border_opacity": 55,
    "brand_image": "shopify://shop_images/somnila-mark-dawn.png",
    "display_continue_shopping": true,
    "continue_shopping_url": "/collections/shop-all",
    "swatches_predefined_colors_list": "<p>Night = #1E2A3A</p><p>Cloud = #F7F9FC</p><p>Stone = #C4C2BD</p><p>Sky = #A9C8E8</p><p>Blush = #E9C6C6</p><p>Blue = #4A78B8</p><p>Red = #B4463C</p><p>Dark grey = #5A5F66</p><p>Azure = #8FB8E8</p><p>Ice = #DCE8F2</p><p>Mint = #BFE0CF</p><p>Apricot = #F3C7A2</p><p>Sand = #D9C6A8</p><p>Green = #7FA07F</p><p>Yellow = #E9D77A</p><p>Black = #141414</p><p>Cream = #F3EEE2</p><p>Lime = #C9D97A</p><p>Sage = #A8BCA9</p><p>Slate = #6B7D90</p><p>Salmon = #EF9E8F</p><p>Violet = #8E7CC3</p><p>Heather grey = #9A9CA3</p><p>Light grey = #D2D4D8</p><p>Butter = #F2E3A2</p>"
  },
  "presets": {
    "Default": {
      "logo_width": 70,
      "colors_accent_1": "#43789A",
      "colors_text": "#121212",
      "colors_background_1": "#FFFFFF",
      "colors_background_2": "#DCE8F0",
      "type_header_font": "poppins_n7",
      "type_body_font": "poppins_n4",
      "page_width": 1400,
      "cart_type": "drawer",
      "sections": {
        "main-password-header": {
          "type": "main-password-header",
          "settings": {
            "color_scheme": "background-1"
          }
        },
        "main-password-footer": {
          "type": "main-password-footer",
          "settings": {
            "color_scheme": "background-1"
          }
        }
      }
    }
  },
  "platform_customizations": {
    "custom_css": []
  }
}
```

---

# ▶ theme/sections/footer-group.json

_Fichier : `build/theme/sections/footer-group.json`_

```json
{
  "name": "t:sections.footer.name",
  "type": "footer",
  "sections": {
    "footer": {
      "type": "footer",
      "blocks": {
        "brand": {
          "type": "brand_information",
          "settings": {
            "show_social": true,
            "width_desktop": 4,
            "width_mobile": "2"
          }
        },
        "shop": {
          "type": "link_list",
          "settings": {
            "heading": "Shop",
            "menu": "somnila-shop",
            "width_desktop": 2,
            "width_mobile": "1"
          }
        },
        "help": {
          "type": "link_list",
          "settings": {
            "heading": "Help",
            "menu": "somnila-help",
            "width_desktop": 2,
            "width_mobile": "1"
          }
        },
        "legal": {
          "type": "link_list",
          "settings": {
            "heading": "Legal",
            "menu": "somnila-legal",
            "width_desktop": 2,
            "width_mobile": "1"
          }
        },
        "news": {
          "type": "email_signup",
          "settings": {
            "heading": "Notes from the workshop",
            "subtext": "<p>One email a month at most. What we make, what we refuse to make.</p>",
            "button_type": "arrow",
            "button_label": "Sign up",
            "button_style_secondary": false,
            "width_desktop": 2,
            "width_mobile": "2"
          }
        }
      },
      "block_order": [
        "brand",
        "shop",
        "help",
        "legal",
        "news"
      ],
      "settings": {
        "color_scheme": "inverse",
        "enable_follow_on_shop": false,
        "show_social": true,
        "enable_country_selector": true,
        "enable_language_selector": false,
        "payment_enable": true,
        "enabled_payment_types": "visa, master, american_express, paypal, apple_pay, google_pay, shopify_pay",
        "show_policy": false,
        "branding_text": "",
        "margin_top": 0,
        "padding_top": 56,
        "padding_bottom": 32
      }
    }
  },
  "order": [
    "footer"
  ]
}
```

---

# ▶ theme/sections/header-group.json

_Fichier : `build/theme/sections/header-group.json`_

```json
{
  "name": "t:sections.header.name",
  "type": "header",
  "sections": {
    "somnila-styles": {
      "type": "custom-liquid",
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "custom_liquid": "<style>\n#shopify-section-{{ section.id }}{height:0;overflow:hidden;padding:0!important;margin:0!important}\n@font-face{font-family:'Somnila Serif';src:url('https://cdn.shopify.com/s/files/1/0778/2629/3917/files/somnila-serif-fraunces-soft-var.woff2?v=1789072486') format('woff2');font-weight:300 700;font-style:normal;font-display:swap}\n@font-face{font-family:'Somnila Sans';src:url('https://cdn.shopify.com/s/files/1/0778/2629/3917/files/somnila-sans-manrope-var.woff2?v=1789072486') format('woff2');font-weight:200 800;font-style:normal;font-display:swap}\n:root{--font-heading-family:'Somnila Serif',Georgia,'Times New Roman',serif;--font-heading-style:normal;--font-heading-weight:400;--font-body-family:'Somnila Sans',system-ui,-apple-system,'Segoe UI',sans-serif;--font-body-style:normal;--font-body-weight:400;--font-body-weight-bold:600;--color-shadow:30,42,58;--somnila-dawn:#F0B79B;--somnila-mist:#DCE8F2;--somnila-slate:#6B7D90}\nh1,h2,h3,h4,.h0,.h1,.h2,.h3,.h4,.hxl{letter-spacing:-.015em;font-variation-settings:'opsz' 72;font-weight:400}\n.h0,.hxl,h1.h0{font-variation-settings:'opsz' 120}\nbody{-webkit-font-smoothing:antialiased}\nstrong,b{font-weight:600}\n.button,.shopify-challenge__button,.customer button,button.button{letter-spacing:0;text-transform:none;font-weight:500}\n.button--secondary{background:transparent}\n.caption-with-letter-spacing,.announcement-bar__message,.announcement-bar__message strong{letter-spacing:.08em;text-transform:uppercase;font-size:1.1rem;font-weight:500}\n.announcement-bar__message strong{font-weight:600}\n.somnila-sky{background:linear-gradient(180deg,#F7F9FC 0%,#DCE8F2 100%)}\n.card,.card__inner,.card__media,.media{box-shadow:none}\n.card--card:hover .card__media{transform:none}\na{text-underline-offset:.2em}\n.price{font-variant-numeric:tabular-nums}\n.product__title h1,.product__title .h1{font-variation-settings:'opsz' 96}\n.somnila-specs h3{font-family:var(--font-body-family);font-size:1.2rem;letter-spacing:.08em;text-transform:uppercase;color:var(--somnila-slate);margin:1.6rem 0 .4rem;font-weight:500}\n.somnila-specs table{border-collapse:collapse;font-variant-numeric:tabular-nums}\n.somnila-specs th{text-align:left;font-weight:500;padding:.2rem 1.6rem .2rem 0;color:var(--somnila-slate)}\n.somnila-specs td{padding:.2rem 0}\n.somnila-horizon{display:block;width:5.6rem;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--somnila-dawn),rgba(240,183,155,0));margin:1.2rem 0 0}\n@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}\n\n/* --- passe design 2 --- */\n.hero__heading.hxl{font-size:clamp(5.2rem,7.2vw,9.6rem);line-height:.98;margin-bottom:1.2rem}\n.hero__text{max-width:52rem}.hero__text p{font-size:1.9rem;line-height:1.55}\n.hero__buttons{margin-top:2.4rem}\n.icon-bar h3,.multicolumn-card__info h3,.card__heading,.card__heading a,.footer-block__heading,.collapsible-content__heading.small,.product__accordion .accordion__title,.cart-drawer__heading{font-family:var(--font-body-family)!important;font-weight:600!important;letter-spacing:0!important;font-variation-settings:normal}\n.icon-bar h3{font-size:1.5rem;margin:0 0 .2rem}\n.multicolumn-card__info h3{font-size:2.1rem;font-family:var(--font-heading-family)!important;font-weight:400!important;letter-spacing:-.01em!important}\n.card__heading{font-size:1.5rem}\n.card-information .price{font-size:1.5rem}\n.collapsible-content-wrapper-narrow{max-width:96rem;margin:0 auto}\n.collapsible-content__header{margin-bottom:2.4rem}\n.accordion__title,.collapsible-content .accordion__title{font-family:var(--font-body-family)!important;font-weight:600;font-size:1.6rem;letter-spacing:0}\n.title-with-highlight b,.title-with-highlight strong{font-weight:600;color:inherit}\n.rich-text__heading,.collapsible-content__heading,.title.h1,.featured-collection .title,.multicolumn .title{font-size:calc(var(--font-heading-scale)*3.8rem)}\n.product__title h1{font-size:3.6rem}\n.product-form__submit,.button.button--full-width{height:5.4rem}\n.product__info-wrapper .product__text.inline-richtext{font-size:1.5rem}\n.footer-block__heading:has(+ ul),.footer-block__heading:has(+ .footer-block__details-content),.footer-block--menu .footer-block__heading,.footer-block__newsletter .footer-block__heading{font-size:1.3rem;letter-spacing:.08em!important;text-transform:uppercase;color:rgba(247,249,252,.72)}\n.footer-block__brand-info .footer-block__heading,.footer-block__brand-info h2{font-family:var(--font-heading-family)!important;font-weight:400!important;font-size:2.2rem;text-transform:none;letter-spacing:-.01em!important}\n.footer__content-bottom{border-top:1px solid rgba(247,249,252,.14)}\n@media screen and (min-width:990px){.section-padding-tight{padding-top:2rem}}\n\n/* passe design 3 : tuiles de confiance et icônes de réassurance en Manrope */\n.icon-bar .multicolumn-card__info h3{font-family:var(--font-body-family)!important;font-weight:600!important;font-size:1.5rem!important;letter-spacing:0!important;font-variation-settings:normal}\n.icon-with-text .h4{font-family:var(--font-body-family)!important;font-weight:500!important;font-size:1.3rem!important;letter-spacing:0!important;color:rgb(var(--color-foreground))}\n.icon-with-text--horizontal .icon-with-text__item{gap:.6rem}\n</style>\n{%- if template.name == 'index' -%}<h1 class=\"visually-hidden\">Somnila memory-foam pillows shaped around the way you actually lie</h1>{%- endif -%}"
      }
    },
    "annonce": {
      "type": "announcement-bar",
      "blocks": {
        "a1": {
          "type": "announcement",
          "settings": {
            "text": "<strong>Free shipping</strong> on every pillow",
            "text_alignment": "center",
            "mobile_text_size": 11,
            "desktop_text_size": 12,
            "icon": "local_shipping",
            "filled_icon": false,
            "mobile_icon_size": 14,
            "desktop_icon_size": 16,
            "desktop_layout": "horizontal",
            "mobile_layout": "horizontal"
          }
        },
        "a2": {
          "type": "announcement",
          "settings": {
            "text": "Ships in <strong>6–10 days</strong>, tracked",
            "text_alignment": "center",
            "mobile_text_size": 11,
            "desktop_text_size": 12,
            "icon": "schedule",
            "filled_icon": false,
            "mobile_icon_size": 14,
            "desktop_icon_size": 16,
            "desktop_layout": "horizontal",
            "mobile_layout": "horizontal"
          }
        },
        "a3": {
          "type": "announcement",
          "settings": {
            "text": "<strong>30-night trial</strong> on every pillow",
            "text_alignment": "center",
            "mobile_text_size": 11,
            "desktop_text_size": 12,
            "icon": "bedtime",
            "filled_icon": false,
            "mobile_icon_size": 14,
            "desktop_icon_size": 16,
            "desktop_layout": "horizontal",
            "mobile_layout": "horizontal"
          }
        }
      },
      "block_order": [
        "a1",
        "a2",
        "a3"
      ],
      "settings": {
        "columns_desktop": 3,
        "columns_mobile": 1,
        "desktop_spacing": 40,
        "mobile_spacing": 16,
        "show_separator": false,
        "color_scheme": "background-2",
        "slider_mobile": true,
        "slider_desktop": false,
        "type": "fade",
        "autoplay": true,
        "autoplay_speed": 5,
        "padding_top": 8,
        "padding_bottom": 8
      }
    },
    "header": {
      "type": "header",
      "settings": {
        "sticky_header_type": "on-scroll-up",
        "show_line_separator": false,
        "color_scheme": "background-1",
        "logo_link": "/",
        "logo_position": "middle-left",
        "menu": "somnila-main",
        "menu_type_desktop": "dropdown",
        "highlight_active_link": false,
        "highlighted_link_color_scheme": "background-2",
        "products_mega_menu_links": "",
        "products_mega_menu_display_collection_products": false,
        "products_mega_menu_display_collection_images": false,
        "products_mega_menu_display_collection_images_on_mobile": false,
        "mobile_menu_title": "Menu",
        "secondary_menu": "",
        "menu_color_scheme": "background-1",
        "mobile_logo_position": "center",
        "display_search": true,
        "margin_bottom": 0,
        "padding_top": 16,
        "padding_bottom": 16
      }
    }
  },
  "order": [
    "somnila-styles",
    "annonce",
    "header"
  ]
}
```

---

# ▶ theme/sections/somnila-styles.liquid.txt

_Fichier : `build/theme/sections/somnila-styles.liquid.txt`_

```liquid
<style>
#shopify-section-{{ section.id }}{height:0;overflow:hidden;padding:0!important;margin:0!important}
@font-face{font-family:'Somnila Serif';src:url('https://cdn.shopify.com/s/files/1/0778/2629/3917/files/somnila-serif-fraunces-soft-var.woff2?v=1789072486') format('woff2');font-weight:300 700;font-style:normal;font-display:swap}
@font-face{font-family:'Somnila Sans';src:url('https://cdn.shopify.com/s/files/1/0778/2629/3917/files/somnila-sans-manrope-var.woff2?v=1789072486') format('woff2');font-weight:200 800;font-style:normal;font-display:swap}
:root{--font-heading-family:'Somnila Serif',Georgia,'Times New Roman',serif;--font-heading-style:normal;--font-heading-weight:400;--font-body-family:'Somnila Sans',system-ui,-apple-system,'Segoe UI',sans-serif;--font-body-style:normal;--font-body-weight:400;--font-body-weight-bold:600;--color-shadow:30,42,58;--somnila-dawn:#F0B79B;--somnila-mist:#DCE8F2;--somnila-slate:#6B7D90}
h1,h2,h3,h4,.h0,.h1,.h2,.h3,.h4,.hxl{letter-spacing:-.015em;font-variation-settings:'opsz' 72;font-weight:400}
.h0,.hxl,h1.h0{font-variation-settings:'opsz' 120}
body{-webkit-font-smoothing:antialiased}
strong,b{font-weight:600}
.button,.shopify-challenge__button,.customer button,button.button{letter-spacing:0;text-transform:none;font-weight:500}
.button--secondary{background:transparent}
.caption-with-letter-spacing,.announcement-bar__message,.announcement-bar__message strong{letter-spacing:.08em;text-transform:uppercase;font-size:1.1rem;font-weight:500}
.announcement-bar__message strong{font-weight:600}
.somnila-sky{background:linear-gradient(180deg,#F7F9FC 0%,#DCE8F2 100%)}
.card,.card__inner,.card__media,.media{box-shadow:none}
.card--card:hover .card__media{transform:none}
a{text-underline-offset:.2em}
.price{font-variant-numeric:tabular-nums}
.product__title h1,.product__title .h1{font-variation-settings:'opsz' 96}
.somnila-specs h3{font-family:var(--font-body-family);font-size:1.2rem;letter-spacing:.08em;text-transform:uppercase;color:var(--somnila-slate);margin:1.6rem 0 .4rem;font-weight:500}
.somnila-specs table{border-collapse:collapse;font-variant-numeric:tabular-nums}
.somnila-specs th{text-align:left;font-weight:500;padding:.2rem 1.6rem .2rem 0;color:var(--somnila-slate)}
.somnila-specs td{padding:.2rem 0}
.somnila-horizon{display:block;width:5.6rem;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--somnila-dawn),rgba(240,183,155,0));margin:1.2rem 0 0}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}

/* --- passe design 2 --- */
.hero__heading.hxl{font-size:clamp(5.2rem,7.2vw,9.6rem);line-height:.98;margin-bottom:1.2rem}
.hero__text{max-width:52rem}.hero__text p{font-size:1.9rem;line-height:1.55}
.hero__buttons{margin-top:2.4rem}
.icon-bar h3,.multicolumn-card__info h3,.card__heading,.card__heading a,.footer-block__heading,.collapsible-content__heading.small,.product__accordion .accordion__title,.cart-drawer__heading{font-family:var(--font-body-family)!important;font-weight:600!important;letter-spacing:0!important;font-variation-settings:normal}
.icon-bar h3{font-size:1.5rem;margin:0 0 .2rem}
.multicolumn-card__info h3{font-size:2.1rem;font-family:var(--font-heading-family)!important;font-weight:400!important;letter-spacing:-.01em!important}
.card__heading{font-size:1.5rem}
.card-information .price{font-size:1.5rem}
.collapsible-content-wrapper-narrow{max-width:96rem;margin:0 auto}
.collapsible-content__header{margin-bottom:2.4rem}
.accordion__title,.collapsible-content .accordion__title{font-family:var(--font-body-family)!important;font-weight:600;font-size:1.6rem;letter-spacing:0}
.title-with-highlight b,.title-with-highlight strong{font-weight:600;color:inherit}
.rich-text__heading,.collapsible-content__heading,.title.h1,.featured-collection .title,.multicolumn .title{font-size:calc(var(--font-heading-scale)*3.8rem)}
.product__title h1{font-size:3.6rem}
.product-form__submit,.button.button--full-width{height:5.4rem}
.product__info-wrapper .product__text.inline-richtext{font-size:1.5rem}
.footer-block__heading:has(+ ul),.footer-block__heading:has(+ .footer-block__details-content),.footer-block--menu .footer-block__heading,.footer-block__newsletter .footer-block__heading{font-size:1.3rem;letter-spacing:.08em!important;text-transform:uppercase;color:rgba(247,249,252,.72)}
.footer-block__brand-info .footer-block__heading,.footer-block__brand-info h2{font-family:var(--font-heading-family)!important;font-weight:400!important;font-size:2.2rem;text-transform:none;letter-spacing:-.01em!important}
.footer__content-bottom{border-top:1px solid rgba(247,249,252,.14)}
@media screen and (min-width:990px){.section-padding-tight{padding-top:2rem}}

/* passe design 3 : tuiles de confiance et icônes de réassurance en Manrope */
.icon-bar .multicolumn-card__info h3{font-family:var(--font-body-family)!important;font-weight:600!important;font-size:1.5rem!important;letter-spacing:0!important;font-variation-settings:normal}
.icon-with-text .h4{font-family:var(--font-body-family)!important;font-weight:500!important;font-size:1.3rem!important;letter-spacing:0!important;color:rgb(var(--color-foreground))}
.icon-with-text--horizontal .icon-with-text__item{gap:.6rem}
</style>
{%- if template.name == 'index' -%}<h1 class="visually-hidden">Somnila memory-foam pillows shaped around the way you actually lie</h1>{%- endif -%}
```

---

# ▶ theme/templates/404.json

_Fichier : `build/theme/templates/404.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-404",
      "settings": {}
    },
    "cta": {
      "type": "rich-text",
      "blocks": {
        "t": {
          "type": "text",
          "settings": {
            "text": "<p>Nothing here. The pillows are this way.</p>"
          }
        },
        "b": {
          "type": "button",
          "settings": {
            "button_label": "All pillows",
            "button_link": "shopify://collections/memory-foam-pillows",
            "button_style_secondary": false,
            "button_label_2": "",
            "button_link_2": "",
            "button_style_secondary_2": false
          }
        }
      },
      "block_order": [
        "t",
        "b"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "desktop_content_position": "center",
        "content_alignment": "center",
        "full_width": true,
        "color_scheme": "background-1",
        "padding_top": 0,
        "padding_bottom": 64
      }
    }
  },
  "order": [
    "main",
    "cta"
  ]
}
```

---

# ▶ theme/templates/article.json

_Fichier : `build/theme/templates/article.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-article",
      "blocks": {
        "featured_image": {
          "type": "featured_image",
          "settings": {
            "image_height": "large"
          }
        },
        "title": {
          "type": "title",
          "settings": {
            "blog_show_date": true,
            "blog_show_author": false
          }
        },
        "content": {
          "type": "content",
          "settings": {}
        },
        "share": {
          "type": "share",
          "settings": {
            "share_label": "Share"
          }
        }
      },
      "block_order": [
        "featured_image",
        "title",
        "content",
        "share"
      ],
      "settings": {}
    },
    "newsletter": {
      "type": "newsletter",
      "blocks": {
        "h": {
          "type": "heading",
          "settings": {
            "title": "Notes from the workshop",
            "title_highlight_color": "#1E2A3A",
            "heading_size": "h1"
          }
        },
        "p": {
          "type": "paragraph",
          "settings": {
            "text": "<p>One email a month at most: what we are making, what we refused to make. No countdowns, no fake sales.</p>"
          }
        },
        "f": {
          "type": "email_form",
          "settings": {}
        }
      },
      "block_order": [
        "h",
        "p",
        "f"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "button_type": "arrow",
        "button_label": "Sign up",
        "button_style_secondary": false,
        "color_scheme": "background-1",
        "full_width": true,
        "padding_top": 64,
        "padding_bottom": 64
      }
    }
  },
  "order": [
    "main",
    "newsletter"
  ]
}
```

---

# ▶ theme/templates/blog.json

_Fichier : `build/theme/templates/blog.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-blog",
      "settings": {
        "layout": "grid",
        "show_image": true,
        "image_height": "medium",
        "show_date": true,
        "show_author": false,
        "padding_top": 0,
        "padding_bottom": 64
      }
    },
    "newsletter": {
      "type": "newsletter",
      "blocks": {
        "h": {
          "type": "heading",
          "settings": {
            "title": "Notes from the workshop",
            "title_highlight_color": "#1E2A3A",
            "heading_size": "h1"
          }
        },
        "p": {
          "type": "paragraph",
          "settings": {
            "text": "<p>One email a month at most: what we are making, what we refused to make. No countdowns, no fake sales.</p>"
          }
        },
        "f": {
          "type": "email_form",
          "settings": {}
        }
      },
      "block_order": [
        "h",
        "p",
        "f"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "button_type": "arrow",
        "button_label": "Sign up",
        "button_style_secondary": false,
        "color_scheme": "background-1",
        "full_width": true,
        "padding_top": 64,
        "padding_bottom": 64
      }
    }
  },
  "order": [
    "main",
    "newsletter"
  ]
}
```

---

# ▶ theme/templates/cart.json

_Fichier : `build/theme/templates/cart.json`_

```json
{
  "sections": {
    "items": {
      "type": "main-cart-items",
      "settings": {}
    },
    "footer": {
      "type": "main-cart-footer",
      "blocks": {
        "subtotal": {
          "type": "subtotal",
          "settings": {}
        },
        "buttons": {
          "type": "buttons",
          "settings": {}
        }
      },
      "block_order": [
        "subtotal",
        "buttons"
      ],
      "settings": {}
    },
    "trust": {
      "type": "icon-bar",
      "blocks": {
        "t1": {
          "type": "column",
          "settings": {
            "icon": "local_shipping",
            "filled_icon": false,
            "title": "Free shipping",
            "text": "<p>On every pillow and every set, to the US, Canada, the UK, Europe and Australia.</p>"
          }
        },
        "t2": {
          "type": "column",
          "settings": {
            "icon": "schedule",
            "filled_icon": false,
            "title": "6–10 days, tracked",
            "text": "<p>Tracking number by email the day it ships.</p>"
          }
        },
        "t3": {
          "type": "column",
          "settings": {
            "icon": "bedtime",
            "filled_icon": false,
            "title": "30-night trial",
            "text": "<p>Sleep on it. If it isn't right, one email and we refund it.</p>"
          }
        }
      },
      "block_order": [
        "t1",
        "t2",
        "t3"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h2",
        "text": "",
        "color_scheme": "background-1",
        "icon_layout": "horizontal",
        "icon_size": "small",
        "icon_color": "accent-1",
        "cards_color_scheme": "background-2",
        "type": "slide",
        "autoplay": false,
        "desktop_full_page": false,
        "columns_desktop": 3,
        "slider_desktop": false,
        "desktop_spacing": 16,
        "desktop_side_padding": 0,
        "desktop_padding_calc": true,
        "desktop_adaptive_height": false,
        "desktop_dots_position": "hidden",
        "desktop_arrows_position": "hidden",
        "columns_mobile": "1",
        "slider_mobile": true,
        "mobile_dots_position": "under",
        "mobile_arrows_position": "hidden",
        "padding_top": 24,
        "padding_bottom": 56
      }
    }
  },
  "order": [
    "items",
    "footer",
    "trust"
  ]
}
```

---

# ▶ theme/templates/collection.json

_Fichier : `build/theme/templates/collection.json`_

```json
{
  "sections": {
    "banner": {
      "type": "main-collection-banner",
      "settings": {
        "show_collection_description": true,
        "show_collection_image": false,
        "color_scheme": "background-1"
      }
    },
    "grid": {
      "type": "main-collection-product-grid",
      "settings": {
        "products_per_page": 24,
        "columns_desktop": 3,
        "stretch_cards": false,
        "image_ratio": "square",
        "show_secondary_image": true,
        "badges": "disabled",
        "show_vendor": false,
        "show_rating": false,
        "enable_quick_add": false,
        "swatches_option_name": "",
        "swatches_position": "bottom",
        "enable_filtering": false,
        "filter_type": "horizontal",
        "enable_sorting": true,
        "columns_mobile": "2",
        "padding_top": 24,
        "padding_bottom": 56
      }
    },
    "trust": {
      "type": "icon-bar",
      "blocks": {
        "t1": {
          "type": "column",
          "settings": {
            "icon": "local_shipping",
            "filled_icon": false,
            "title": "Free shipping",
            "text": "<p>On every pillow and every set, to the US, Canada, the UK, Europe and Australia.</p>"
          }
        },
        "t2": {
          "type": "column",
          "settings": {
            "icon": "schedule",
            "filled_icon": false,
            "title": "6–10 days, tracked",
            "text": "<p>Tracking number by email the day it ships.</p>"
          }
        },
        "t3": {
          "type": "column",
          "settings": {
            "icon": "bedtime",
            "filled_icon": false,
            "title": "30-night trial",
            "text": "<p>Sleep on it. If it isn't right, one email and we refund it.</p>"
          }
        },
        "t4": {
          "type": "column",
          "settings": {
            "icon": "local_laundry_service",
            "filled_icon": false,
            "title": "Cover included",
            "text": "<p>Removable and machine washable, on every pillow.</p>"
          }
        }
      },
      "block_order": [
        "t1",
        "t2",
        "t3",
        "t4"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h2",
        "text": "",
        "color_scheme": "background-2",
        "icon_layout": "horizontal",
        "icon_size": "small",
        "icon_color": "accent-1",
        "cards_color_scheme": "background-1",
        "type": "slide",
        "autoplay": false,
        "desktop_full_page": false,
        "columns_desktop": 4,
        "slider_desktop": false,
        "desktop_spacing": 16,
        "desktop_side_padding": 0,
        "desktop_padding_calc": true,
        "desktop_adaptive_height": false,
        "desktop_dots_position": "hidden",
        "desktop_arrows_position": "hidden",
        "columns_mobile": "1",
        "slider_mobile": true,
        "mobile_dots_position": "under",
        "mobile_arrows_position": "hidden",
        "padding_top": 40,
        "padding_bottom": 40
      }
    },
    "newsletter": {
      "type": "newsletter",
      "blocks": {
        "h": {
          "type": "heading",
          "settings": {
            "title": "Notes from the workshop",
            "title_highlight_color": "#1E2A3A",
            "heading_size": "h1"
          }
        },
        "p": {
          "type": "paragraph",
          "settings": {
            "text": "<p>One email a month at most: what we are making, what we refused to make. No countdowns, no fake sales.</p>"
          }
        },
        "f": {
          "type": "email_form",
          "settings": {}
        }
      },
      "block_order": [
        "h",
        "p",
        "f"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "button_type": "arrow",
        "button_label": "Sign up",
        "button_style_secondary": false,
        "color_scheme": "background-1",
        "full_width": true,
        "padding_top": 64,
        "padding_bottom": 64
      }
    }
  },
  "order": [
    "banner",
    "grid",
    "trust",
    "newsletter"
  ]
}
```

---

# ▶ theme/templates/index.json

_Fichier : `build/theme/templates/index.json`_

```json
{
  "sections": {
    "hero": {
      "type": "slideshow-hero",
      "blocks": {
        "s1": {
          "type": "slide",
          "settings": {
            "desktop_bg_image": "shopify://shop_images/somnila_neck-01_hero_16x9_v2.jpg",
            "desktop_overlay_color": "#000000",
            "desktop_overlay_opacity": 0,
            "mobile_bg_image": "shopify://shop_images/somnila_neck-01_hero_4x5_v2.jpg",
            "mobile_overlay_color": "#000000",
            "mobile_overlay_opacity": 0,
            "display_sound_btn": false,
            "heading_prefix": "",
            "heading": "Sleep well.",
            "title_highlight_color": "#1E2A3A",
            "heading_size": "hxl",
            "heading_suffix": "",
            "heading_prefix_size": "h4",
            "text": "<p>Neck 01 is a memory-foam pillow with two heights, shaped around the way you actually lie. Ships in 6–10 days. Thirty nights to decide.</p>",
            "button_label_1": "Shop Neck 01",
            "button_link_1": "shopify://products/neck-01",
            "button_style_secondary_1": false,
            "button_label_2": "All pillows",
            "button_link_2": "shopify://collections/memory-foam-pillows",
            "button_style_secondary_2": true,
            "color_scheme": "custom",
            "full_page_width": false,
            "content_max_width": "pixels",
            "content_pixels_max_width": 560,
            "content_percentage_max_width": 50,
            "content_vertical_position": "center",
            "content_horizontal_position": "flex-start",
            "content_text_alignment": "left",
            "mobile_content_vertical_position": "flex-end",
            "mobile_content_text_alignment": "left",
            "custom_colors_text": "#1E2A3A",
            "custom_colors_solid_button_background": "#1E2A3A",
            "custom_colors_solid_button_text": "#F7F9FC",
            "custom_colors_outline_button": "#1E2A3A"
          }
        }
      },
      "block_order": [
        "s1"
      ],
      "settings": {
        "visibility": "always-display",
        "min_desktop_height_type": "pixels",
        "desktop_pixels_height": 680,
        "min_mobile_height_type": "pixels",
        "mobile_pixels_height": 640,
        "transparent_header": false,
        "hide_announcement_bars": false,
        "slider_type": "fade",
        "drag": false,
        "autoplay": false,
        "autoplay_speed": 10,
        "enable_dots": false,
        "dots_color_scheme": "background-1",
        "padding_top": 0,
        "padding_bottom": 0
      }
    },
    "trust": {
      "type": "icon-bar",
      "blocks": {
        "t1": {
          "type": "column",
          "settings": {
            "icon": "local_shipping",
            "filled_icon": false,
            "title": "Free shipping",
            "text": "<p>On every pillow and every set, to the US, Canada, the UK, Europe and Australia.</p>"
          }
        },
        "t2": {
          "type": "column",
          "settings": {
            "icon": "schedule",
            "filled_icon": false,
            "title": "6–10 days, tracked",
            "text": "<p>Tracking number by email the day it ships.</p>"
          }
        },
        "t3": {
          "type": "column",
          "settings": {
            "icon": "bedtime",
            "filled_icon": false,
            "title": "30-night trial",
            "text": "<p>Sleep on it. If it isn't right, one email and we refund it.</p>"
          }
        },
        "t4": {
          "type": "column",
          "settings": {
            "icon": "local_laundry_service",
            "filled_icon": false,
            "title": "Cover included",
            "text": "<p>Removable and machine washable, on every pillow.</p>"
          }
        }
      },
      "block_order": [
        "t1",
        "t2",
        "t3",
        "t4"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h2",
        "text": "",
        "color_scheme": "background-1",
        "icon_layout": "horizontal",
        "icon_size": "small",
        "icon_color": "accent-1",
        "cards_color_scheme": "background-2",
        "type": "slide",
        "autoplay": false,
        "desktop_full_page": false,
        "columns_desktop": 4,
        "slider_desktop": false,
        "desktop_spacing": 16,
        "desktop_side_padding": 0,
        "desktop_padding_calc": true,
        "desktop_adaptive_height": false,
        "desktop_dots_position": "hidden",
        "desktop_arrows_position": "hidden",
        "columns_mobile": "1",
        "slider_mobile": true,
        "mobile_dots_position": "under",
        "mobile_arrows_position": "hidden",
        "padding_top": 24,
        "padding_bottom": 24
      }
    },
    "neck": {
      "type": "featured-product",
      "blocks": {
        "title": {
          "type": "title",
          "settings": {
            "text_size": "h1",
            "title_alignment": "left",
            "uppercase_title": false,
            "margin_top": 0,
            "margin_bottom": 9
          }
        },
        "bullets": {
          "type": "text",
          "settings": {
            "text_1": "Two heights on one pillow: 13 cm and 11 cm (5.1 / 4.3 in)",
            "text_2": "Memory foam that holds its shape through the night",
            "text_3": "Cool-touch cover included, machine washable",
            "icon_1": "check_circle",
            "icon_2": "check_circle",
            "icon_3": "check_circle",
            "filled_icon_1": false,
            "filled_icon_2": false,
            "filled_icon_3": false,
            "icon_color": "#1E2A3A",
            "text_color": "#1E2A3A",
            "icon_scale": 110,
            "alignment": "left",
            "direction": "vertical",
            "width": "100%",
            "column_gap": 2.5,
            "desktop_text_size": 15,
            "mobile_text_size": 14,
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "price": {
          "type": "price",
          "settings": {
            "layout": "price_first",
            "price_color": "text",
            "compare_price_color": "text",
            "displayed_badge": "none",
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "picker": {
          "type": "variant_picker",
          "settings": {
            "picker_types": "swatches",
            "custom_labels": "[name] · [selected]",
            "swatches_size": "large",
            "swatches_custom_colors": "predefined",
            "margin_top": 15,
            "margin_bottom": 15
          }
        },
        "buy": {
          "type": "buy_buttons",
          "settings": {
            "show_dynamic_checkout": true,
            "skip_cart": false,
            "uppercase_text": false,
            "icon_scale": 120,
            "icon_spacing": 10,
            "display_price": false,
            "enable_custom_color": false,
            "margin_top": 18,
            "margin_bottom": 12
          }
        },
        "reassure": {
          "type": "icon_with_text",
          "settings": {
            "layout": "horizontal",
            "icon_color": "accent-1",
            "desktop_icon_size": 28,
            "desktop_spacing": 10,
            "desktop_text_size": 14,
            "mobile_icon_size": 24,
            "mobile_spacing": 8,
            "mobile_text_size": 12,
            "icon_1": "bedtime",
            "icon_1_fill": false,
            "heading_1": "30-night trial",
            "icon_2": "local_shipping",
            "icon_2_fill": false,
            "heading_2": "Free shipping",
            "icon_3": "local_laundry_service",
            "icon_3_fill": false,
            "heading_3": "Washable cover",
            "margin_top": 12,
            "margin_bottom": 12
          }
        }
      },
      "block_order": [
        "title",
        "bullets",
        "price",
        "picker",
        "buy",
        "reassure"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "product": "neck-01",
        "color_scheme": "background-1",
        "secondary_background": false,
        "media_size": "medium",
        "constrain_to_viewport": true,
        "media_fit": "contain",
        "media_position": "left",
        "image_zoom": "none",
        "hide_variants": false,
        "enable_video_looping": false,
        "mobile_media_corner_radius": 28,
        "full_media_width": false,
        "padding_top": 48,
        "padding_bottom": 48
      }
    },
    "why": {
      "type": "multicolumn",
      "blocks": {
        "c1": {
          "type": "column",
          "settings": {
            "title": "Two heights, one pillow",
            "text": "<p>13 cm on one side, 11 cm on the other. Turn it over until your head lies level with your shoulders. Most people know after two nights.</p>",
            "link_label": "",
            "link": ""
          }
        },
        "c2": {
          "type": "column",
          "settings": {
            "title": "Foam that holds",
            "text": "<p>Memory foam takes the shape of your neck and keeps it, instead of flattening under your head by three in the morning.</p>",
            "link_label": "",
            "link": ""
          }
        },
        "c3": {
          "type": "column",
          "settings": {
            "title": "A cover you can wash",
            "text": "<p>The cool-touch cover comes with the pillow. Unzip it, machine wash it, put it back. A spare is €16.90.</p>",
            "link_label": "",
            "link": ""
          }
        }
      },
      "block_order": [
        "c1",
        "c2",
        "c3"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "Why it <b>holds</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "button_label": "",
        "button_link": "",
        "color_scheme": "background-1",
        "cards_color_scheme": "background-2",
        "cards_corner_radius": 28,
        "stretch_cards": true,
        "stretched_cards_content_alignment": "flex-start",
        "image_width": "full",
        "image_ratio": "square",
        "media_position": "top",
        "column_alignment": "left",
        "desktop_heading_size": 22,
        "mobile_heading_size": 20,
        "desktop_text_size": 15,
        "mobile_text_size": 14,
        "desktop_text_top_margin": 10,
        "mobile_text_top_margin": 10,
        "desktop_container_padding_y": 32,
        "desktop_container_padding_x": 32,
        "mobile_container_padding_y": 24,
        "mobile_container_padding_x": 24,
        "type": "slide",
        "autoplay": false,
        "desktop_full_page": false,
        "columns_desktop": 3,
        "slider_desktop": false,
        "desktop_spacing": 24,
        "desktop_side_padding": 0,
        "desktop_padding_calc": true,
        "desktop_dots_position": "hidden",
        "desktop_arrows_position": "hidden",
        "columns_mobile": "1",
        "slider_mobile": true,
        "mobile_dots_position": "under",
        "mobile_arrows_position": "hidden",
        "padding_top": 48,
        "padding_bottom": 48
      }
    },
    "materials": {
      "type": "image-with-text",
      "blocks": {
        "c": {
          "type": "caption",
          "settings": {
            "caption": "Materials",
            "text_style": "caption-with-letter-spacing",
            "text_size": "small"
          }
        },
        "h": {
          "type": "heading",
          "settings": {
            "title": "Memory foam. <b>Cool-touch cover.</b> Nothing else.",
            "title_highlight_color": "#1E2A3A",
            "heading_size": "h1"
          }
        },
        "t": {
          "type": "text",
          "settings": {
            "text": "<p>Every Somnila pillow is a memory-foam core with a removable cover. Neck 01 and Contour 01 come with a cooling cover; Body 01 with a breathable cotton one. Dimensions and weight are on every product page, in centimetres and inches.</p>",
            "text_style": "body"
          }
        },
        "b": {
          "type": "button",
          "settings": {
            "button_label": "See all pillows",
            "button_link": "shopify://collections/memory-foam-pillows"
          }
        }
      },
      "block_order": [
        "c",
        "h",
        "t",
        "b"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "image": "shopify://shop_images/somnila_contour-01_materials_1x1_v1.jpg",
        "video_autoplay": true,
        "video_loop": true,
        "height": "adapt",
        "color_scheme": "background-1",
        "section_color_scheme": "background-2",
        "full_desktop_width": false,
        "content_layout": "no-overlap",
        "desktop_media_width": 50,
        "layout": "image_first",
        "desktop_content_position": "middle",
        "desktop_content_alignment": "left",
        "mobile_full_media_width": false,
        "mobile_direction": "normal",
        "mobile_image_quanlity": "2",
        "mobile_content_alignment": "left",
        "mobile_padding_top": 24,
        "mobile_padding_bottom": 24,
        "desktop_padding_top": 64,
        "desktop_padding_bottom": 64
      }
    },
    "range": {
      "type": "featured-collection",
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "Five pillows, <b>one job each</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "description": "<p>Named like objects, numbered like versions. Each one has a height and a shape for one way of lying.</p>",
        "show_description": true,
        "description_style": "body",
        "color_scheme": "background-1",
        "collection": "memory-foam-pillows",
        "products_to_show": 5,
        "stretch_cards": false,
        "show_view_all": true,
        "view_all_style": "link",
        "cards_color_scheme": "background-1",
        "image_ratio": "square",
        "show_secondary_image": true,
        "badges": "disabled",
        "show_vendor": false,
        "show_rating": false,
        "enable_quick_add": false,
        "swatches_option_name": "",
        "swatches_position": "bottom",
        "type": "slide",
        "autoplay": false,
        "desktop_full_page": false,
        "columns_desktop": 5,
        "slider_desktop": false,
        "per_move_desktop": 1,
        "desktop_spacing": 16,
        "desktop_side_padding": 0,
        "desktop_padding_calc": true,
        "desktop_adaptive_height": false,
        "desktop_dots_position": "hidden",
        "desktop_arrows_position": "hidden",
        "columns_mobile": "2",
        "slider_mobile": true,
        "mobile_dots_position": "under",
        "mobile_arrows_position": "hidden",
        "padding_top": 48,
        "padding_bottom": 48
      }
    },
    "reviews": {
      "type": "testimonials",
      "disabled": true,
      "blocks": {
        "a1": {
          "type": "column",
          "settings": {
            "title": "[REPLACE WITH A REAL REVIEW]",
            "author": "—",
            "text": "<p>Section disabled on purpose. Publish it only with real, verifiable reviews collected after purchase. An invented testimonial is a deceptive commercial practice.</p>"
          }
        },
        "a2": {
          "type": "column",
          "settings": {
            "title": "[REPLACE WITH A REAL REVIEW]",
            "author": "—",
            "text": "<p>Connect a verified-reviews app (Judge.me free plan is enough to start), then replace these three blocks.</p>"
          }
        },
        "a3": {
          "type": "column",
          "settings": {
            "title": "[REPLACE WITH A REAL REVIEW]",
            "author": "—",
            "text": "<p>Enable the section once about ten authentic reviews exist.</p>"
          }
        }
      },
      "block_order": [
        "a1",
        "a2",
        "a3"
      ],
      "settings": {
        "title": "What people say after <b>thirty nights</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "color_scheme": "background-2",
        "column_alignment": "left",
        "show_stars": false,
        "show_quotes": true,
        "padding_top": 64,
        "padding_bottom": 64
      }
    },
    "faq": {
      "type": "collapsible-content",
      "blocks": {
        "f1": {
          "type": "collapsible_row",
          "settings": {
            "heading": "How long does delivery take?",
            "icon": "schedule",
            "filled_icon": false,
            "row_content": "<p>6 to 10 days, tracked, to the United States, Canada, the United Kingdom, Europe and Australia. You get the tracking number by email the day it ships.</p>",
            "page": ""
          }
        },
        "f2": {
          "type": "collapsible_row",
          "settings": {
            "heading": "Is shipping free?",
            "icon": "local_shipping",
            "filled_icon": false,
            "row_content": "<p>On every pillow and every set, yes. Only accessories bought on their own (mask, earplugs, covers, throw) pay shipping.</p>",
            "page": ""
          }
        },
        "f3": {
          "type": "collapsible_row",
          "settings": {
            "heading": "How does the 30-night trial work?",
            "icon": "bedtime",
            "filled_icon": false,
            "row_content": "<p>Sleep on the pillow for up to 30 nights from delivery. If it isn't right, send us an email with your order number and we refund the price of the pillow. You don't need to send it back.</p>",
            "page": ""
          }
        },
        "f4": {
          "type": "collapsible_row",
          "settings": {
            "heading": "Which height should I choose?",
            "icon": "straighten",
            "filled_icon": false,
            "row_content": "<p>Neck 01 has both: 13 cm on one side, 11 cm on the other. Start with the higher side; if your head tilts up, turn the pillow over.</p>",
            "page": ""
          }
        },
        "f5": {
          "type": "collapsible_row",
          "settings": {
            "heading": "Can I wash the cover?",
            "icon": "local_laundry_service",
            "filled_icon": false,
            "row_content": "<p>Yes. Unzip it and machine wash it cold on a gentle cycle, then dry it flat. The foam itself takes a damp cloth, never the machine.</p>",
            "page": ""
          }
        }
      },
      "block_order": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "caption": "FAQ",
        "title": "Before you <b>order</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "heading_alignment": "center",
        "layout": "none",
        "color_scheme": "background-1",
        "container_color_scheme": "background-2",
        "open_first_collapsible_row": false,
        "image_ratio": "adapt",
        "desktop_layout": "image_second",
        "row_heading_size": "medium",
        "collapse_icon": "plus",
        "display_top_border": true,
        "padding_top": 56,
        "padding_bottom": 56
      }
    },
    "sets": {
      "type": "featured-collection",
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "Sets, <b>priced honestly</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "description": "<p>Two or three pieces together cost less than apart. The saving is on the price tag, not in a fake strike-through.</p>",
        "show_description": true,
        "description_style": "body",
        "color_scheme": "background-2",
        "collection": "sets",
        "products_to_show": 4,
        "stretch_cards": false,
        "show_view_all": true,
        "view_all_style": "link",
        "cards_color_scheme": "background-1",
        "image_ratio": "square",
        "show_secondary_image": false,
        "badges": "disabled",
        "show_vendor": false,
        "show_rating": false,
        "enable_quick_add": false,
        "swatches_option_name": "",
        "swatches_position": "bottom",
        "type": "slide",
        "autoplay": false,
        "desktop_full_page": false,
        "columns_desktop": 4,
        "slider_desktop": false,
        "desktop_spacing": 24,
        "desktop_side_padding": 0,
        "desktop_padding_calc": true,
        "desktop_adaptive_height": false,
        "desktop_dots_position": "hidden",
        "desktop_arrows_position": "hidden",
        "columns_mobile": "2",
        "slider_mobile": true,
        "mobile_dots_position": "under",
        "mobile_arrows_position": "hidden",
        "padding_top": 56,
        "padding_bottom": 56
      }
    },
    "newsletter": {
      "type": "newsletter",
      "blocks": {
        "h": {
          "type": "heading",
          "settings": {
            "title": "Notes from the workshop",
            "title_highlight_color": "#1E2A3A",
            "heading_size": "h1"
          }
        },
        "p": {
          "type": "paragraph",
          "settings": {
            "text": "<p>One email a month at most: what we are making, what we refused to make. No countdowns, no fake sales.</p>"
          }
        },
        "f": {
          "type": "email_form",
          "settings": {}
        }
      },
      "block_order": [
        "h",
        "p",
        "f"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "button_type": "arrow",
        "button_label": "Sign up",
        "button_style_secondary": false,
        "color_scheme": "background-1",
        "full_width": true,
        "padding_top": 64,
        "padding_bottom": 64
      }
    }
  },
  "order": [
    "hero",
    "trust",
    "neck",
    "why",
    "materials",
    "range",
    "reviews",
    "faq",
    "sets",
    "newsletter"
  ]
}
```

---

# ▶ theme/templates/list-collections.json

_Fichier : `build/theme/templates/list-collections.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-list-collections",
      "settings": {
        "title": "Collections",
        "sort": "alphabetical",
        "image_ratio": "square",
        "columns_desktop": 3,
        "columns_mobile": "2"
      }
    }
  },
  "order": [
    "main"
  ]
}
```

---

# ▶ theme/templates/page.contact.json

_Fichier : `build/theme/templates/page.contact.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-page",
      "settings": {
        "padding_top": 40,
        "padding_bottom": 0
      }
    },
    "form": {
      "type": "contact-form",
      "blocks": {
        "r1": {
          "type": "field_row",
          "settings": {
            "input_1_enabled": true,
            "input_1_type": "name",
            "input_1_required": true,
            "input_1_error_message": "Please enter your name",
            "input_1_custom_name": "Name",
            "input_2_enabled": true,
            "input_2_type": "email",
            "input_2_required": true,
            "input_2_error_message": "Please enter a valid email",
            "input_2_custom_name": "Email"
          }
        },
        "r2": {
          "type": "field_row",
          "settings": {
            "input_1_enabled": true,
            "input_1_type": "custom",
            "input_1_required": false,
            "input_1_error_message": "",
            "input_1_custom_name": "Order number (if you have one)",
            "input_2_enabled": false,
            "input_2_type": "custom",
            "input_2_required": false,
            "input_2_error_message": "",
            "input_2_custom_name": ""
          }
        },
        "m": {
          "type": "textarea",
          "settings": {
            "input_type": "comment",
            "input_required": true,
            "input_error_message": "Please write your message",
            "input_custom_name": "Message"
          }
        }
      },
      "block_order": [
        "r1",
        "r2",
        "m"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h2",
        "button_full_width": false,
        "color_scheme": "background-1",
        "padding_top": 0,
        "padding_bottom": 64
      }
    }
  },
  "order": [
    "main",
    "form"
  ]
}
```

---

# ▶ theme/templates/page.faq.json

_Fichier : `build/theme/templates/page.faq.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-page",
      "settings": {
        "padding_top": 40,
        "padding_bottom": 40
      }
    },
    "cta": {
      "type": "rich-text",
      "blocks": {
        "h": {
          "type": "heading",
          "settings": {
            "title": "Still a question?",
            "title_highlight_color": "#1E2A3A",
            "heading_size": "h2"
          }
        },
        "b": {
          "type": "button",
          "settings": {
            "button_label": "Write to us",
            "button_link": "shopify://pages/contact",
            "button_style_secondary": false,
            "button_label_2": "",
            "button_link_2": "",
            "button_style_secondary_2": false
          }
        }
      },
      "block_order": [
        "h",
        "b"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "desktop_content_position": "center",
        "content_alignment": "center",
        "full_width": true,
        "color_scheme": "background-2",
        "padding_top": 48,
        "padding_bottom": 48
      }
    }
  },
  "order": [
    "main",
    "cta"
  ]
}
```

---

# ▶ theme/templates/page.json

_Fichier : `build/theme/templates/page.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-page",
      "settings": {
        "padding_top": 40,
        "padding_bottom": 64
      }
    }
  },
  "order": [
    "main"
  ]
}
```

---

# ▶ theme/templates/product.accessory.json

_Fichier : `build/theme/templates/product.accessory.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-product",
      "blocks": {
        "title": {
          "type": "title",
          "settings": {
            "text_size": "h1",
            "title_alignment": "left",
            "uppercase_title": false,
            "margin_top": 0,
            "margin_bottom": 9
          }
        },
        "bullets": {
          "type": "text",
          "settings": {
            "text_1": "Ships in 6–10 days, tracked",
            "text_2": "Free shipping from €54.90",
            "text_3": "Returns accepted unused within 14 days",
            "icon_1": "check_circle",
            "icon_2": "check_circle",
            "icon_3": "check_circle",
            "filled_icon_1": false,
            "filled_icon_2": false,
            "filled_icon_3": false,
            "icon_color": "#1E2A3A",
            "text_color": "#1E2A3A",
            "icon_scale": 110,
            "alignment": "left",
            "direction": "vertical",
            "width": "100%",
            "column_gap": 2.5,
            "desktop_text_size": 15,
            "mobile_text_size": 14,
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "price": {
          "type": "price",
          "settings": {
            "layout": "price_first",
            "price_color": "text",
            "compare_price_color": "text",
            "displayed_badge": "none",
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "picker": {
          "type": "variant_picker",
          "settings": {
            "picker_types": "swatches",
            "custom_labels": "[name] · [selected]",
            "skip_unavailable": false,
            "swatches_size": "large",
            "swatches_custom_colors": "predefined",
            "full_width_dropdowns": false,
            "margin_top": 15,
            "margin_bottom": 15
          }
        },
        "buy": {
          "type": "buy_buttons",
          "settings": {
            "show_dynamic_checkout": true,
            "skip_cart": false,
            "uppercase_text": false,
            "icon_scale": 120,
            "icon_spacing": 10,
            "display_price": false,
            "enable_custom_color": false,
            "margin_top": 18,
            "margin_bottom": 12
          }
        },
        "pay": {
          "type": "payment_badges",
          "settings": {
            "enabled_payment_types": "visa, master, american_express, paypal, apple_pay, google_pay, shopify_pay",
            "margin_top": 6,
            "margin_bottom": 15
          }
        },
        "ship": {
          "type": "estimated_shipping",
          "settings": {
            "icon": "local_shipping",
            "filled_icon": false,
            "icon_size": "small",
            "icon_alignment": "middle",
            "message": "<p>Ships in 6–10 days, tracked. Estimated delivery <strong>[start_date]</strong> to <strong>[end_date]</strong>.</p>",
            "min_shipping_days": 6,
            "max_shipping_days": 10,
            "date_format": "day_mm_dd",
            "days_labels": "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday",
            "months_labels": "January, February, March, April, May, June, July, August, September, October, November, December",
            "margin_top": 6,
            "margin_bottom": 12
          }
        },
        "reassure": {
          "type": "icon_with_text",
          "settings": {
            "layout": "horizontal",
            "icon_color": "accent-1",
            "desktop_icon_size": 28,
            "desktop_spacing": 10,
            "desktop_text_size": 14,
            "mobile_icon_size": 24,
            "mobile_spacing": 8,
            "mobile_text_size": 12,
            "icon_1": "schedule",
            "icon_1_fill": false,
            "heading_1": "6–10 days",
            "icon_2": "local_shipping",
            "icon_2_fill": false,
            "heading_2": "Tracked",
            "icon_3": "undo",
            "icon_3_fill": false,
            "heading_3": "14-day returns",
            "margin_top": 12,
            "margin_bottom": 18
          }
        },
        "div": {
          "type": "divider",
          "settings": {
            "color": "#C5D2DE",
            "height": 1,
            "width": 100,
            "Full_mobile_width": false,
            "alignment": "center",
            "border_radius": 0,
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "desc": {
          "type": "description",
          "settings": {
            "margin_top": 12,
            "margin_bottom": 18
          }
        },
        "specs": {
          "type": "custom_liquid",
          "settings": {
            "custom_liquid": "{%- assign mf = product.metafields.somnila -%}\n{%- assign v = product.selected_or_first_available_variant -%}\n<div class=\"somnila-specs\">\n{%- if mf.contents != blank -%}<h3>In the box</h3><p>{{ mf.contents.value | newline_to_br }}</p>{%- endif -%}\n{%- if mf.dimensions_cm != blank -%}<h3>Dimensions</h3><table><tr><th>Metric</th><td>{{ mf.dimensions_cm.value }}</td></tr><tr><th>Imperial</th><td>{{ mf.dimensions_in.value }}</td></tr>{%- if v.weight > 0 -%}<tr><th>Weight</th><td>{{ v.weight | divided_by: 1000.0 | round: 2 }} kg ({{ v.weight | times: 0.00220462 | round: 1 }} lb)</td></tr>{%- endif -%}</table>{%- endif -%}\n{%- if mf.materials != blank -%}<h3>Materials</h3><p>{{ mf.materials.value | newline_to_br }}</p>{%- endif -%}\n{%- if mf.includes != blank -%}<h3>Included</h3><p>{{ mf.includes.value }}</p>{%- endif -%}\n{%- if mf.delivery != blank -%}<h3>Delivery</h3><p>Ships in {{ mf.delivery.value }}, tracked.</p>{%- endif -%}\n</div>"
          }
        },
        "t1": {
          "type": "collapsible_tab",
          "settings": {
            "heading": "30-night trial & returns",
            "heading_size": "medium",
            "icon": "bedtime",
            "filled_icon": false,
            "collapse_icon": "plus",
            "display_top_border": true,
            "open": false,
            "content": "<p>Accessories are hygiene and textile items: they can be returned unused, in their packaging, within 14 days of delivery. Write to us first and we send the instructions.</p>",
            "margin_top": 0,
            "margin_bottom": 0
          }
        },
        "t2": {
          "type": "collapsible_tab",
          "settings": {
            "heading": "Shipping",
            "heading_size": "medium",
            "icon": "local_shipping",
            "filled_icon": false,
            "collapse_icon": "plus",
            "display_top_border": true,
            "open": false,
            "content": "<p>Every order ships tracked and arrives in 6 to 10 days in the United States, Canada, the United Kingdom, Europe and Australia. Free shipping on every pillow and every set; accessories on their own pay €4.90 to €9.90 depending on the zone. Details on the <a href=\"/pages/shipping-delivery\">shipping page</a>.</p>",
            "margin_top": 0,
            "margin_bottom": 0
          }
        },
        "t3": {
          "type": "collapsible_tab",
          "settings": {
            "heading": "Care",
            "heading_size": "medium",
            "icon": "local_laundry_service",
            "filled_icon": false,
            "collapse_icon": "plus",
            "display_top_border": true,
            "open": false,
            "content": "<p>Mask 01 and covers: hand wash or machine wash cold on a gentle cycle, dry flat. Quiet 01 earplugs: rinse with water, dry before putting them back in the case. Throw 01: machine wash cold, tumble dry low.</p>",
            "margin_top": 0,
            "margin_bottom": 0
          }
        },
        "sticky": {
          "type": "sticky_atc",
          "settings": {
            "function": "add_to_cart",
            "display_when": "after_scroll",
            "button_label": "Add to cart",
            "enable_custom_btn_color": false,
            "color_scheme": "background-1",
            "picker_type": "combined",
            "desktop_show_image": true,
            "desktop_show_title": true,
            "desktop_rating_stars": false,
            "desktop_show_price": true,
            "desktop_show_sale_badge": false,
            "desktop_variant_picker": true,
            "desktop_full_button_width": false,
            "desktop_show_price_in_button": false,
            "desktop_transparent_bg": false,
            "mobile_show_image": false,
            "mobile_show_title": true,
            "mobile_rating_stars": false,
            "mobile_show_price": true,
            "mobile_show_sale_badge": false,
            "mobile_variant_picker": false,
            "mobile_full_button_width": true
          }
        }
      },
      "block_order": [
        "title",
        "bullets",
        "price",
        "picker",
        "buy",
        "pay",
        "ship",
        "reassure",
        "div",
        "desc",
        "specs",
        "t1",
        "t2",
        "t3",
        "sticky"
      ],
      "settings": {
        "display_id": false,
        "enable_sticky_info": true,
        "display_variant_image_first": true,
        "disable_prepend": true,
        "hide_variants": false,
        "variant_image_filtering": "none",
        "image_zoom": "lightbox",
        "arrows_color_scheme": "inverse",
        "transparent_arrows": true,
        "dots_color_scheme": "inverse",
        "media_size": "medium",
        "media_position": "left",
        "gallery_layout": "thumbnail_slider",
        "desktop_thumbnails_count": 5,
        "constrain_to_viewport": true,
        "media_fit": "contain",
        "desktop_arrows_position": "hidden",
        "mobile_media_corner_radius": 28,
        "mobile_spacing_pixels": 0,
        "mobile_arrows_position": "hidden",
        "mobile_pagination": "dots_under",
        "mobile_thumbnails": "hide",
        "mobile_thumbnails_count": 5,
        "mobile_scroll_padding_percentage": 0,
        "mobile_scroll_padding_pixels": 16,
        "enable_mobile_outher_spacing": false,
        "mobile_slides_container_width": 100,
        "mobile_slides_inner_width": 100,
        "trust_badge_position": "top-right",
        "trust_badge_size": "medium",
        "mobile_padding_top": 0,
        "mobile_padding_bottom": 16,
        "desktop_padding_top": 36,
        "desktop_padding_bottom": 36
      }
    },
    "why": {
      "type": "multicolumn",
      "blocks": {
        "c1": {
          "type": "column",
          "settings": {
            "title": "Made to go with the pillows",
            "text": "<p>Covers fit the exact pillow they are named for. Mask 01 and Quiet 01 fit the nightstand.</p>",
            "link_label": "",
            "link": ""
          }
        },
        "c2": {
          "type": "column",
          "settings": {
            "title": "Ships with your pillow",
            "text": "<p>Add it to a pillow order and it travels free in the same box.</p>",
            "link_label": "",
            "link": ""
          }
        },
        "c3": {
          "type": "column",
          "settings": {
            "title": "14-day returns",
            "text": "<p>Unused and in its packaging, within 14 days of delivery.</p>",
            "link_label": "",
            "link": ""
          }
        }
      },
      "block_order": [
        "c1",
        "c2",
        "c3"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "What you are <b>buying</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "button_label": "",
        "button_link": "",
        "color_scheme": "background-2",
        "cards_color_scheme": "background-1",
        "cards_corner_radius": 28,
        "stretch_cards": true,
        "stretched_cards_content_alignment": "flex-start",
        "image_width": "full",
        "image_ratio": "square",
        "media_position": "top",
        "column_alignment": "left",
        "desktop_heading_size": 22,
        "mobile_heading_size": 20,
        "desktop_text_size": 15,
        "mobile_text_size": 14,
        "desktop_text_top_margin": 10,
        "mobile_text_top_margin": 10,
        "desktop_container_padding_y": 32,
        "desktop_container_padding_x": 32,
        "mobile_container_padding_y": 24,
        "mobile_container_padding_x": 24,
        "type": "slide",
        "autoplay": false,
        "desktop_full_page": false,
        "columns_desktop": 3,
        "slider_desktop": false,
        "desktop_spacing": 24,
        "desktop_side_padding": 0,
        "desktop_padding_calc": true,
        "desktop_dots_position": "hidden",
        "desktop_arrows_position": "hidden",
        "columns_mobile": "1",
        "slider_mobile": true,
        "mobile_dots_position": "under",
        "mobile_arrows_position": "hidden",
        "padding_top": 56,
        "padding_bottom": 56
      }
    },
    "faq": {
      "type": "collapsible-content",
      "blocks": {
        "f1": {
          "type": "collapsible_row",
          "settings": {
            "heading": "How long does delivery take?",
            "icon": "schedule",
            "filled_icon": false,
            "row_content": "<p>6 to 10 days, tracked. You get the tracking number by email the day it ships.</p>",
            "page": ""
          }
        },
        "f2": {
          "type": "collapsible_row",
          "settings": {
            "heading": "What if it isn't right for me?",
            "icon": "bedtime",
            "filled_icon": false,
            "row_content": "<p>Email us within 30 nights of delivery with your order number. We refund the pillow; you don't need to send it back.</p>",
            "page": ""
          }
        },
        "f3": {
          "type": "collapsible_row",
          "settings": {
            "heading": "Does the foam smell when new?",
            "icon": "air",
            "filled_icon": false,
            "row_content": "<p>New foam can have a light smell for the first hours. Air the pillow uncovered for half a day before the first night.</p>",
            "page": ""
          }
        },
        "f4": {
          "type": "collapsible_row",
          "settings": {
            "heading": "How do I wash it?",
            "icon": "local_laundry_service",
            "filled_icon": false,
            "row_content": "<p>The cover goes in the machine, cold, gentle cycle, dried flat. The foam takes a damp cloth only.</p>",
            "page": ""
          }
        }
      },
      "block_order": [
        "f1",
        "f2",
        "f3",
        "f4"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "caption": "FAQ",
        "title": "Before you <b>order</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "heading_alignment": "center",
        "layout": "none",
        "color_scheme": "background-1",
        "container_color_scheme": "background-2",
        "open_first_collapsible_row": false,
        "image_ratio": "adapt",
        "desktop_layout": "image_second",
        "row_heading_size": "medium",
        "collapse_icon": "plus",
        "display_top_border": true,
        "padding_top": 56,
        "padding_bottom": 56
      }
    },
    "related": {
      "type": "related-products",
      "settings": {
        "display_id": false,
        "title": "Goes with it",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h2",
        "products_to_show": 4,
        "columns_desktop": 4,
        "color_scheme": "background-1",
        "image_ratio": "square",
        "show_secondary_image": false,
        "show_vendor": false,
        "show_rating": false,
        "enable_quick_add": false,
        "columns_mobile": "2",
        "padding_top": 48,
        "padding_bottom": 56
      }
    }
  },
  "order": [
    "main",
    "why",
    "faq",
    "related"
  ]
}
```

---

# ▶ theme/templates/product.json

_Fichier : `build/theme/templates/product.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-product",
      "blocks": {
        "title": {
          "type": "title",
          "settings": {
            "text_size": "h1",
            "title_alignment": "left",
            "uppercase_title": false,
            "margin_top": 0,
            "margin_bottom": 9
          }
        },
        "bullets": {
          "type": "text",
          "settings": {
            "text_1": "Ships in 6–10 days, tracked",
            "text_2": "30-night trial, refund by email",
            "text_3": "Removable cover included, machine washable",
            "icon_1": "check_circle",
            "icon_2": "check_circle",
            "icon_3": "check_circle",
            "filled_icon_1": false,
            "filled_icon_2": false,
            "filled_icon_3": false,
            "icon_color": "#1E2A3A",
            "text_color": "#1E2A3A",
            "icon_scale": 110,
            "alignment": "left",
            "direction": "vertical",
            "width": "100%",
            "column_gap": 2.5,
            "desktop_text_size": 15,
            "mobile_text_size": 14,
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "price": {
          "type": "price",
          "settings": {
            "layout": "price_first",
            "price_color": "text",
            "compare_price_color": "text",
            "displayed_badge": "none",
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "picker": {
          "type": "variant_picker",
          "settings": {
            "picker_types": "swatches",
            "custom_labels": "[name] · [selected]",
            "skip_unavailable": false,
            "swatches_size": "large",
            "swatches_custom_colors": "predefined",
            "full_width_dropdowns": false,
            "margin_top": 15,
            "margin_bottom": 15
          }
        },
        "buy": {
          "type": "buy_buttons",
          "settings": {
            "show_dynamic_checkout": true,
            "skip_cart": false,
            "uppercase_text": false,
            "icon_scale": 120,
            "icon_spacing": 10,
            "display_price": false,
            "enable_custom_color": false,
            "margin_top": 18,
            "margin_bottom": 12
          }
        },
        "pay": {
          "type": "payment_badges",
          "settings": {
            "enabled_payment_types": "visa, master, american_express, paypal, apple_pay, google_pay, shopify_pay",
            "margin_top": 6,
            "margin_bottom": 15
          }
        },
        "ship": {
          "type": "estimated_shipping",
          "settings": {
            "icon": "local_shipping",
            "filled_icon": false,
            "icon_size": "small",
            "icon_alignment": "middle",
            "message": "<p>Ships in 6–10 days, tracked. Estimated delivery <strong>[start_date]</strong> to <strong>[end_date]</strong>.</p>",
            "min_shipping_days": 6,
            "max_shipping_days": 10,
            "date_format": "day_mm_dd",
            "days_labels": "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday",
            "months_labels": "January, February, March, April, May, June, July, August, September, October, November, December",
            "margin_top": 6,
            "margin_bottom": 12
          }
        },
        "reassure": {
          "type": "icon_with_text",
          "settings": {
            "layout": "horizontal",
            "icon_color": "accent-1",
            "desktop_icon_size": 28,
            "desktop_spacing": 10,
            "desktop_text_size": 14,
            "mobile_icon_size": 24,
            "mobile_spacing": 8,
            "mobile_text_size": 12,
            "icon_1": "bedtime",
            "icon_1_fill": false,
            "heading_1": "30-night trial",
            "icon_2": "local_shipping",
            "icon_2_fill": false,
            "heading_2": "Free shipping",
            "icon_3": "local_laundry_service",
            "icon_3_fill": false,
            "heading_3": "Washable cover",
            "margin_top": 12,
            "margin_bottom": 18
          }
        },
        "div": {
          "type": "divider",
          "settings": {
            "color": "#C5D2DE",
            "height": 1,
            "width": 100,
            "Full_mobile_width": false,
            "alignment": "center",
            "border_radius": 0,
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "desc": {
          "type": "description",
          "settings": {
            "margin_top": 12,
            "margin_bottom": 18
          }
        },
        "specs": {
          "type": "custom_liquid",
          "settings": {
            "custom_liquid": "{%- assign mf = product.metafields.somnila -%}\n{%- assign v = product.selected_or_first_available_variant -%}\n<div class=\"somnila-specs\">\n{%- if mf.contents != blank -%}<h3>In the box</h3><p>{{ mf.contents.value | newline_to_br }}</p>{%- endif -%}\n{%- if mf.dimensions_cm != blank -%}<h3>Dimensions</h3><table><tr><th>Metric</th><td>{{ mf.dimensions_cm.value }}</td></tr><tr><th>Imperial</th><td>{{ mf.dimensions_in.value }}</td></tr>{%- if v.weight > 0 -%}<tr><th>Weight</th><td>{{ v.weight | divided_by: 1000.0 | round: 2 }} kg ({{ v.weight | times: 0.00220462 | round: 1 }} lb)</td></tr>{%- endif -%}</table>{%- endif -%}\n{%- if mf.materials != blank -%}<h3>Materials</h3><p>{{ mf.materials.value | newline_to_br }}</p>{%- endif -%}\n{%- if mf.includes != blank -%}<h3>Included</h3><p>{{ mf.includes.value }}</p>{%- endif -%}\n{%- if mf.delivery != blank -%}<h3>Delivery</h3><p>Ships in {{ mf.delivery.value }}, tracked.</p>{%- endif -%}\n</div>"
          }
        },
        "t1": {
          "type": "collapsible_tab",
          "settings": {
            "heading": "30-night trial & returns",
            "heading_size": "medium",
            "icon": "bedtime",
            "filled_icon": false,
            "collapse_icon": "plus",
            "display_top_border": true,
            "open": false,
            "content": "<p>Sleep on it for up to 30 nights from delivery. If it isn't right, email us with your order number and we refund the price of the pillow. You don't need to send it back. This commercial guarantee comes on top of your statutory rights.</p>",
            "margin_top": 0,
            "margin_bottom": 0
          }
        },
        "t2": {
          "type": "collapsible_tab",
          "settings": {
            "heading": "Shipping",
            "heading_size": "medium",
            "icon": "local_shipping",
            "filled_icon": false,
            "collapse_icon": "plus",
            "display_top_border": true,
            "open": false,
            "content": "<p>Every order ships tracked and arrives in 6 to 10 days in the United States, Canada, the United Kingdom, Europe and Australia. Free shipping on every pillow and every set; accessories on their own pay €4.90 to €9.90 depending on the zone. Details on the <a href=\"/pages/shipping-delivery\">shipping page</a>.</p>",
            "margin_top": 0,
            "margin_bottom": 0
          }
        },
        "t3": {
          "type": "collapsible_tab",
          "settings": {
            "heading": "Care",
            "heading_size": "medium",
            "icon": "local_laundry_service",
            "filled_icon": false,
            "collapse_icon": "plus",
            "display_top_border": true,
            "open": false,
            "content": "<p>Covers: unzip, machine wash cold on a gentle cycle, dry flat. Foam: a damp cloth, never the machine, never the dryer. New foam can have a light smell for a few hours; air the pillow uncovered before the first night.</p>",
            "margin_top": 0,
            "margin_bottom": 0
          }
        },
        "sticky": {
          "type": "sticky_atc",
          "settings": {
            "function": "add_to_cart",
            "display_when": "after_scroll",
            "button_label": "Add to cart",
            "enable_custom_btn_color": false,
            "color_scheme": "background-1",
            "picker_type": "combined",
            "desktop_show_image": true,
            "desktop_show_title": true,
            "desktop_rating_stars": false,
            "desktop_show_price": true,
            "desktop_show_sale_badge": false,
            "desktop_variant_picker": true,
            "desktop_full_button_width": false,
            "desktop_show_price_in_button": false,
            "desktop_transparent_bg": false,
            "mobile_show_image": false,
            "mobile_show_title": true,
            "mobile_rating_stars": false,
            "mobile_show_price": true,
            "mobile_show_sale_badge": false,
            "mobile_variant_picker": false,
            "mobile_full_button_width": true
          }
        },
        "upsell": {
          "type": "product_upsell",
          "settings": {
            "style": "checkbox_1",
            "btn_position": "right",
            "toggle_element": "container",
            "add_btn_label": "<strong>Add</strong>",
            "stacking": "column",
            "accent_color": "accent-1",
            "color_scheme": "background-2",
            "product_list": [
              "mask-01",
              "quiet-01"
            ],
            "enable_dynamic_recommendations": false
          }
        }
      },
      "block_order": [
        "title",
        "bullets",
        "price",
        "picker",
        "upsell",
        "buy",
        "pay",
        "ship",
        "reassure",
        "div",
        "desc",
        "specs",
        "t1",
        "t2",
        "t3",
        "sticky"
      ],
      "settings": {
        "display_id": false,
        "enable_sticky_info": true,
        "display_variant_image_first": true,
        "disable_prepend": true,
        "hide_variants": false,
        "variant_image_filtering": "none",
        "image_zoom": "lightbox",
        "arrows_color_scheme": "inverse",
        "transparent_arrows": true,
        "dots_color_scheme": "inverse",
        "media_size": "medium",
        "media_position": "left",
        "gallery_layout": "thumbnail_slider",
        "desktop_thumbnails_count": 5,
        "constrain_to_viewport": true,
        "media_fit": "contain",
        "desktop_arrows_position": "hidden",
        "mobile_media_corner_radius": 28,
        "mobile_spacing_pixels": 0,
        "mobile_arrows_position": "hidden",
        "mobile_pagination": "dots_under",
        "mobile_thumbnails": "hide",
        "mobile_thumbnails_count": 5,
        "mobile_scroll_padding_percentage": 0,
        "mobile_scroll_padding_pixels": 16,
        "enable_mobile_outher_spacing": false,
        "mobile_slides_container_width": 100,
        "mobile_slides_inner_width": 100,
        "trust_badge_position": "top-right",
        "trust_badge_size": "medium",
        "mobile_padding_top": 0,
        "mobile_padding_bottom": 16,
        "desktop_padding_top": 36,
        "desktop_padding_bottom": 36
      }
    },
    "why": {
      "type": "multicolumn",
      "blocks": {
        "c1": {
          "type": "column",
          "settings": {
            "title": "Shaped for one position",
            "text": "<p>Each Somnila pillow is cut for one way of lying, with a height and a contour to match. Not a block, not a bag of fibre.</p>",
            "link_label": "",
            "link": ""
          }
        },
        "c2": {
          "type": "column",
          "settings": {
            "title": "Foam that holds",
            "text": "<p>Memory foam takes the shape of your neck and keeps it through the night instead of flattening.</p>",
            "link_label": "",
            "link": ""
          }
        },
        "c3": {
          "type": "column",
          "settings": {
            "title": "A cover you can wash",
            "text": "<p>Removable and machine washable. It comes with the pillow, and a spare is €16.90.</p>",
            "link_label": "",
            "link": ""
          }
        }
      },
      "block_order": [
        "c1",
        "c2",
        "c3"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "What you are <b>buying</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "button_label": "",
        "button_link": "",
        "color_scheme": "background-2",
        "cards_color_scheme": "background-1",
        "cards_corner_radius": 28,
        "stretch_cards": true,
        "stretched_cards_content_alignment": "flex-start",
        "image_width": "full",
        "image_ratio": "square",
        "media_position": "top",
        "column_alignment": "left",
        "desktop_heading_size": 22,
        "mobile_heading_size": 20,
        "desktop_text_size": 15,
        "mobile_text_size": 14,
        "desktop_text_top_margin": 10,
        "mobile_text_top_margin": 10,
        "desktop_container_padding_y": 32,
        "desktop_container_padding_x": 32,
        "mobile_container_padding_y": 24,
        "mobile_container_padding_x": 24,
        "type": "slide",
        "autoplay": false,
        "desktop_full_page": false,
        "columns_desktop": 3,
        "slider_desktop": false,
        "desktop_spacing": 24,
        "desktop_side_padding": 0,
        "desktop_padding_calc": true,
        "desktop_dots_position": "hidden",
        "desktop_arrows_position": "hidden",
        "columns_mobile": "1",
        "slider_mobile": true,
        "mobile_dots_position": "under",
        "mobile_arrows_position": "hidden",
        "padding_top": 56,
        "padding_bottom": 56
      }
    },
    "band": {
      "type": "rich-text",
      "blocks": {
        "h": {
          "type": "heading",
          "settings": {
            "title": "Thirty nights to <b>decide</b>.",
            "title_highlight_color": "#F0B79B",
            "heading_size": "h1"
          }
        },
        "t": {
          "type": "text",
          "settings": {
            "text": "<p>You sleep on it at home, on your real nights. If it isn't right, one email with your order number and we refund the pillow. No form, nothing to send back.</p>"
          }
        },
        "b": {
          "type": "button",
          "settings": {
            "button_label": "How the trial works",
            "button_link": "shopify://pages/returns-warranty",
            "button_style_secondary": true,
            "button_label_2": "",
            "button_link_2": "",
            "button_style_secondary_2": false
          }
        }
      },
      "block_order": [
        "h",
        "t",
        "b"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "desktop_content_position": "center",
        "content_alignment": "center",
        "full_width": true,
        "color_scheme": "inverse",
        "padding_top": 64,
        "padding_bottom": 64
      }
    },
    "faq": {
      "type": "collapsible-content",
      "blocks": {
        "f1": {
          "type": "collapsible_row",
          "settings": {
            "heading": "How long does delivery take?",
            "icon": "schedule",
            "filled_icon": false,
            "row_content": "<p>6 to 10 days, tracked. You get the tracking number by email the day it ships.</p>",
            "page": ""
          }
        },
        "f2": {
          "type": "collapsible_row",
          "settings": {
            "heading": "What if it isn't right for me?",
            "icon": "bedtime",
            "filled_icon": false,
            "row_content": "<p>Email us within 30 nights of delivery with your order number. We refund the pillow; you don't need to send it back.</p>",
            "page": ""
          }
        },
        "f3": {
          "type": "collapsible_row",
          "settings": {
            "heading": "Does the foam smell when new?",
            "icon": "air",
            "filled_icon": false,
            "row_content": "<p>New foam can have a light smell for the first hours. Air the pillow uncovered for half a day before the first night.</p>",
            "page": ""
          }
        },
        "f4": {
          "type": "collapsible_row",
          "settings": {
            "heading": "How do I wash it?",
            "icon": "local_laundry_service",
            "filled_icon": false,
            "row_content": "<p>The cover goes in the machine, cold, gentle cycle, dried flat. The foam takes a damp cloth only.</p>",
            "page": ""
          }
        }
      },
      "block_order": [
        "f1",
        "f2",
        "f3",
        "f4"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "caption": "FAQ",
        "title": "Before you <b>order</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "heading_alignment": "center",
        "layout": "none",
        "color_scheme": "background-1",
        "container_color_scheme": "background-2",
        "open_first_collapsible_row": false,
        "image_ratio": "adapt",
        "desktop_layout": "image_second",
        "row_heading_size": "medium",
        "collapse_icon": "plus",
        "display_top_border": true,
        "padding_top": 56,
        "padding_bottom": 56
      }
    },
    "related": {
      "type": "related-products",
      "settings": {
        "display_id": false,
        "title": "Goes with it",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h2",
        "products_to_show": 4,
        "columns_desktop": 4,
        "color_scheme": "background-1",
        "image_ratio": "square",
        "show_secondary_image": false,
        "show_vendor": false,
        "show_rating": false,
        "enable_quick_add": false,
        "columns_mobile": "2",
        "padding_top": 48,
        "padding_bottom": 56
      }
    }
  },
  "order": [
    "main",
    "why",
    "band",
    "faq",
    "related"
  ]
}
```

---

# ▶ theme/templates/product.set.json

_Fichier : `build/theme/templates/product.set.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-product",
      "blocks": {
        "title": {
          "type": "title",
          "settings": {
            "text_size": "h1",
            "title_alignment": "left",
            "uppercase_title": false,
            "margin_top": 0,
            "margin_bottom": 9
          }
        },
        "bullets": {
          "type": "text",
          "settings": {
            "text_1": "Ships in 6–10 days, tracked",
            "text_2": "30-night trial on the pillows in the set",
            "text_3": "Cheaper together than apart, no fake strike-through",
            "icon_1": "check_circle",
            "icon_2": "check_circle",
            "icon_3": "check_circle",
            "filled_icon_1": false,
            "filled_icon_2": false,
            "filled_icon_3": false,
            "icon_color": "#1E2A3A",
            "text_color": "#1E2A3A",
            "icon_scale": 110,
            "alignment": "left",
            "direction": "vertical",
            "width": "100%",
            "column_gap": 2.5,
            "desktop_text_size": 15,
            "mobile_text_size": 14,
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "price": {
          "type": "price",
          "settings": {
            "layout": "price_first",
            "price_color": "text",
            "compare_price_color": "text",
            "displayed_badge": "none",
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "picker": {
          "type": "variant_picker",
          "settings": {
            "picker_types": "swatches, swatches",
            "custom_labels": "[name] · [selected]",
            "skip_unavailable": false,
            "swatches_size": "large",
            "swatches_custom_colors": "predefined",
            "full_width_dropdowns": false,
            "margin_top": 15,
            "margin_bottom": 15
          }
        },
        "buy": {
          "type": "buy_buttons",
          "settings": {
            "show_dynamic_checkout": true,
            "skip_cart": false,
            "uppercase_text": false,
            "icon_scale": 120,
            "icon_spacing": 10,
            "display_price": false,
            "enable_custom_color": false,
            "margin_top": 18,
            "margin_bottom": 12
          }
        },
        "pay": {
          "type": "payment_badges",
          "settings": {
            "enabled_payment_types": "visa, master, american_express, paypal, apple_pay, google_pay, shopify_pay",
            "margin_top": 6,
            "margin_bottom": 15
          }
        },
        "ship": {
          "type": "estimated_shipping",
          "settings": {
            "icon": "local_shipping",
            "filled_icon": false,
            "icon_size": "small",
            "icon_alignment": "middle",
            "message": "<p>Ships in 6–10 days, tracked. Estimated delivery <strong>[start_date]</strong> to <strong>[end_date]</strong>.</p>",
            "min_shipping_days": 6,
            "max_shipping_days": 10,
            "date_format": "day_mm_dd",
            "days_labels": "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday",
            "months_labels": "January, February, March, April, May, June, July, August, September, October, November, December",
            "margin_top": 6,
            "margin_bottom": 12
          }
        },
        "reassure": {
          "type": "icon_with_text",
          "settings": {
            "layout": "horizontal",
            "icon_color": "accent-1",
            "desktop_icon_size": 28,
            "desktop_spacing": 10,
            "desktop_text_size": 14,
            "mobile_icon_size": 24,
            "mobile_spacing": 8,
            "mobile_text_size": 12,
            "icon_1": "bedtime",
            "icon_1_fill": false,
            "heading_1": "30-night trial",
            "icon_2": "local_shipping",
            "icon_2_fill": false,
            "heading_2": "Free shipping",
            "icon_3": "inventory_2",
            "icon_3_fill": false,
            "heading_3": "One box",
            "margin_top": 12,
            "margin_bottom": 18
          }
        },
        "div": {
          "type": "divider",
          "settings": {
            "color": "#C5D2DE",
            "height": 1,
            "width": 100,
            "Full_mobile_width": false,
            "alignment": "center",
            "border_radius": 0,
            "margin_top": 9,
            "margin_bottom": 15
          }
        },
        "desc": {
          "type": "description",
          "settings": {
            "margin_top": 12,
            "margin_bottom": 18
          }
        },
        "specs": {
          "type": "custom_liquid",
          "settings": {
            "custom_liquid": "{%- assign mf = product.metafields.somnila -%}\n{%- assign v = product.selected_or_first_available_variant -%}\n<div class=\"somnila-specs\">\n{%- if mf.contents != blank -%}<h3>In the box</h3><p>{{ mf.contents.value | newline_to_br }}</p>{%- endif -%}\n{%- if mf.dimensions_cm != blank -%}<h3>Dimensions</h3><table><tr><th>Metric</th><td>{{ mf.dimensions_cm.value }}</td></tr><tr><th>Imperial</th><td>{{ mf.dimensions_in.value }}</td></tr>{%- if v.weight > 0 -%}<tr><th>Weight</th><td>{{ v.weight | divided_by: 1000.0 | round: 2 }} kg ({{ v.weight | times: 0.00220462 | round: 1 }} lb)</td></tr>{%- endif -%}</table>{%- endif -%}\n{%- if mf.materials != blank -%}<h3>Materials</h3><p>{{ mf.materials.value | newline_to_br }}</p>{%- endif -%}\n{%- if mf.includes != blank -%}<h3>Included</h3><p>{{ mf.includes.value }}</p>{%- endif -%}\n{%- if mf.delivery != blank -%}<h3>Delivery</h3><p>Ships in {{ mf.delivery.value }}, tracked.</p>{%- endif -%}\n</div>"
          }
        },
        "t1": {
          "type": "collapsible_tab",
          "settings": {
            "heading": "30-night trial & returns",
            "heading_size": "medium",
            "icon": "bedtime",
            "filled_icon": false,
            "collapse_icon": "plus",
            "display_top_border": true,
            "open": false,
            "content": "<p>The pillows in this set come with the 30-night trial: if one isn't right, email us within 30 nights of delivery and we refund it. Accessories in the set can be returned unused within 14 days.</p>",
            "margin_top": 0,
            "margin_bottom": 0
          }
        },
        "t2": {
          "type": "collapsible_tab",
          "settings": {
            "heading": "Shipping",
            "heading_size": "medium",
            "icon": "local_shipping",
            "filled_icon": false,
            "collapse_icon": "plus",
            "display_top_border": true,
            "open": false,
            "content": "<p>Every order ships tracked and arrives in 6 to 10 days in the United States, Canada, the United Kingdom, Europe and Australia. Free shipping on every pillow and every set; accessories on their own pay €4.90 to €9.90 depending on the zone. Details on the <a href=\"/pages/shipping-delivery\">shipping page</a>.</p>",
            "margin_top": 0,
            "margin_bottom": 0
          }
        },
        "t3": {
          "type": "collapsible_tab",
          "settings": {
            "heading": "Care",
            "heading_size": "medium",
            "icon": "local_laundry_service",
            "filled_icon": false,
            "collapse_icon": "plus",
            "display_top_border": true,
            "open": false,
            "content": "<p>Covers: unzip, machine wash cold on a gentle cycle, dry flat. Foam: a damp cloth, never the machine, never the dryer. New foam can have a light smell for a few hours; air the pillow uncovered before the first night.</p>",
            "margin_top": 0,
            "margin_bottom": 0
          }
        },
        "sticky": {
          "type": "sticky_atc",
          "settings": {
            "function": "add_to_cart",
            "display_when": "after_scroll",
            "button_label": "Add to cart",
            "enable_custom_btn_color": false,
            "color_scheme": "background-1",
            "picker_type": "combined",
            "desktop_show_image": true,
            "desktop_show_title": true,
            "desktop_rating_stars": false,
            "desktop_show_price": true,
            "desktop_show_sale_badge": false,
            "desktop_variant_picker": true,
            "desktop_full_button_width": false,
            "desktop_show_price_in_button": false,
            "desktop_transparent_bg": false,
            "mobile_show_image": false,
            "mobile_show_title": true,
            "mobile_rating_stars": false,
            "mobile_show_price": true,
            "mobile_show_sale_badge": false,
            "mobile_variant_picker": false,
            "mobile_full_button_width": true
          }
        }
      },
      "block_order": [
        "title",
        "bullets",
        "price",
        "picker",
        "buy",
        "pay",
        "ship",
        "reassure",
        "div",
        "desc",
        "specs",
        "t1",
        "t2",
        "t3",
        "sticky"
      ],
      "settings": {
        "display_id": false,
        "enable_sticky_info": true,
        "display_variant_image_first": true,
        "disable_prepend": true,
        "hide_variants": false,
        "variant_image_filtering": "none",
        "image_zoom": "lightbox",
        "arrows_color_scheme": "inverse",
        "transparent_arrows": true,
        "dots_color_scheme": "inverse",
        "media_size": "medium",
        "media_position": "left",
        "gallery_layout": "thumbnail_slider",
        "desktop_thumbnails_count": 5,
        "constrain_to_viewport": true,
        "media_fit": "contain",
        "desktop_arrows_position": "hidden",
        "mobile_media_corner_radius": 28,
        "mobile_spacing_pixels": 0,
        "mobile_arrows_position": "hidden",
        "mobile_pagination": "dots_under",
        "mobile_thumbnails": "hide",
        "mobile_thumbnails_count": 5,
        "mobile_scroll_padding_percentage": 0,
        "mobile_scroll_padding_pixels": 16,
        "enable_mobile_outher_spacing": false,
        "mobile_slides_container_width": 100,
        "mobile_slides_inner_width": 100,
        "trust_badge_position": "top-right",
        "trust_badge_size": "medium",
        "mobile_padding_top": 0,
        "mobile_padding_bottom": 16,
        "desktop_padding_top": 36,
        "desktop_padding_bottom": 36
      }
    },
    "why": {
      "type": "multicolumn",
      "blocks": {
        "c1": {
          "type": "column",
          "settings": {
            "title": "One box, fewer decisions",
            "text": "<p>Everything in the set arrives together, each piece in its own colour where you chose one.</p>",
            "link_label": "",
            "link": ""
          }
        },
        "c2": {
          "type": "column",
          "settings": {
            "title": "Priced honestly",
            "text": "<p>The set costs less than the pieces bought apart. The saving is on the tag, not in a strike-through.</p>",
            "link_label": "",
            "link": ""
          }
        },
        "c3": {
          "type": "column",
          "settings": {
            "title": "Same trial, same shipping",
            "text": "<p>Free shipping, 6–10 days tracked, and the 30-night trial on every pillow in the set.</p>",
            "link_label": "",
            "link": ""
          }
        }
      },
      "block_order": [
        "c1",
        "c2",
        "c3"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "title": "What you are <b>buying</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "button_label": "",
        "button_link": "",
        "color_scheme": "background-2",
        "cards_color_scheme": "background-1",
        "cards_corner_radius": 28,
        "stretch_cards": true,
        "stretched_cards_content_alignment": "flex-start",
        "image_width": "full",
        "image_ratio": "square",
        "media_position": "top",
        "column_alignment": "left",
        "desktop_heading_size": 22,
        "mobile_heading_size": 20,
        "desktop_text_size": 15,
        "mobile_text_size": 14,
        "desktop_text_top_margin": 10,
        "mobile_text_top_margin": 10,
        "desktop_container_padding_y": 32,
        "desktop_container_padding_x": 32,
        "mobile_container_padding_y": 24,
        "mobile_container_padding_x": 24,
        "type": "slide",
        "autoplay": false,
        "desktop_full_page": false,
        "columns_desktop": 3,
        "slider_desktop": false,
        "desktop_spacing": 24,
        "desktop_side_padding": 0,
        "desktop_padding_calc": true,
        "desktop_dots_position": "hidden",
        "desktop_arrows_position": "hidden",
        "columns_mobile": "1",
        "slider_mobile": true,
        "mobile_dots_position": "under",
        "mobile_arrows_position": "hidden",
        "padding_top": 56,
        "padding_bottom": 56
      }
    },
    "band": {
      "type": "rich-text",
      "blocks": {
        "h": {
          "type": "heading",
          "settings": {
            "title": "Thirty nights to <b>decide</b>.",
            "title_highlight_color": "#F0B79B",
            "heading_size": "h1"
          }
        },
        "t": {
          "type": "text",
          "settings": {
            "text": "<p>You sleep on it at home, on your real nights. If it isn't right, one email with your order number and we refund the pillow. No form, nothing to send back.</p>"
          }
        },
        "b": {
          "type": "button",
          "settings": {
            "button_label": "How the trial works",
            "button_link": "shopify://pages/returns-warranty",
            "button_style_secondary": true,
            "button_label_2": "",
            "button_link_2": "",
            "button_style_secondary_2": false
          }
        }
      },
      "block_order": [
        "h",
        "t",
        "b"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "desktop_content_position": "center",
        "content_alignment": "center",
        "full_width": true,
        "color_scheme": "inverse",
        "padding_top": 64,
        "padding_bottom": 64
      }
    },
    "faq": {
      "type": "collapsible-content",
      "blocks": {
        "f1": {
          "type": "collapsible_row",
          "settings": {
            "heading": "How long does delivery take?",
            "icon": "schedule",
            "filled_icon": false,
            "row_content": "<p>6 to 10 days, tracked. You get the tracking number by email the day it ships.</p>",
            "page": ""
          }
        },
        "f2": {
          "type": "collapsible_row",
          "settings": {
            "heading": "What if it isn't right for me?",
            "icon": "bedtime",
            "filled_icon": false,
            "row_content": "<p>Email us within 30 nights of delivery with your order number. We refund the pillow; you don't need to send it back.</p>",
            "page": ""
          }
        },
        "f3": {
          "type": "collapsible_row",
          "settings": {
            "heading": "Does the foam smell when new?",
            "icon": "air",
            "filled_icon": false,
            "row_content": "<p>New foam can have a light smell for the first hours. Air the pillow uncovered for half a day before the first night.</p>",
            "page": ""
          }
        },
        "f4": {
          "type": "collapsible_row",
          "settings": {
            "heading": "How do I wash it?",
            "icon": "local_laundry_service",
            "filled_icon": false,
            "row_content": "<p>The cover goes in the machine, cold, gentle cycle, dried flat. The foam takes a damp cloth only.</p>",
            "page": ""
          }
        }
      },
      "block_order": [
        "f1",
        "f2",
        "f3",
        "f4"
      ],
      "settings": {
        "display_id": false,
        "visibility": "always-display",
        "caption": "FAQ",
        "title": "Before you <b>order</b>.",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h1",
        "heading_alignment": "center",
        "layout": "none",
        "color_scheme": "background-1",
        "container_color_scheme": "background-2",
        "open_first_collapsible_row": false,
        "image_ratio": "adapt",
        "desktop_layout": "image_second",
        "row_heading_size": "medium",
        "collapse_icon": "plus",
        "display_top_border": true,
        "padding_top": 56,
        "padding_bottom": 56
      }
    },
    "related": {
      "type": "related-products",
      "settings": {
        "display_id": false,
        "title": "Goes with it",
        "title_highlight_color": "#1E2A3A",
        "heading_size": "h2",
        "products_to_show": 4,
        "columns_desktop": 4,
        "color_scheme": "background-1",
        "image_ratio": "square",
        "show_secondary_image": false,
        "show_vendor": false,
        "show_rating": false,
        "enable_quick_add": false,
        "columns_mobile": "2",
        "padding_top": 48,
        "padding_bottom": 56
      }
    }
  },
  "order": [
    "main",
    "why",
    "band",
    "faq",
    "related"
  ]
}
```

---

# ▶ theme/templates/search.json

_Fichier : `build/theme/templates/search.json`_

```json
{
  "sections": {
    "main": {
      "type": "main-search",
      "settings": {
        "columns_desktop": 4,
        "image_ratio": "square",
        "show_secondary_image": false,
        "show_vendor": false,
        "show_rating": false,
        "enable_filtering": false,
        "filter_type": "horizontal",
        "enable_sorting": true,
        "article_show_date": false,
        "article_show_author": false,
        "columns_mobile": "2",
        "padding_top": 36,
        "padding_bottom": 56
      }
    }
  },
  "order": [
    "main"
  ]
}
```



# ══════ PARTIE 10 — SCRIPTS ══════


---

# ▶ images/site/sky-packshots.py

_Fichier : `build/images/site/sky-packshots.py`_

```python
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
```

---

# ▶ images/site/gen-visuals.py

_Fichier : `build/images/site/gen-visuals.py`_

```python
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
```

---

# ▶ images/clean-supplier-photos.py

_Fichier : `build/images/clean-supplier-photos.py`_

```python
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
```

---

# ▶ tools/render.cjs

_Fichier : `build/tools/render.cjs`_

```javascript
// Rend le preview du thème Somnila via un relais fetch (le proxy coupe les tunnels navigateur).
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs');
const UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36';
const THEME=process.env.THEME||'157447585949';
const BASE='https://liyan.shop';
function mkRelay(ctx, cacheGet){
  return async (route,req)=>{
    const u=req.url();
    if(/^(data|blob):/.test(u))return route.continue().catch(()=>{});
    const isGet=req.method()==='GET';
    const cacheable=isGet && !/\/cart|cart\.js|checkout|preview_theme_id/i.test(u);
    try{
      if(cacheable && cacheGet.has(u)) return route.fulfill(cacheGet.get(u));
      const jar=await ctx.cookies(u); const cookieHeader=jar.map(c=>`${c.name}=${c.value}`).join('; ');
      const headers={...req.headers(),'user-agent':UA}; if(cookieHeader) headers['cookie']=cookieHeader;
      const r=await fetch(u,{method:req.method(),headers,body:isGet||req.method()==='HEAD'?undefined:req.postDataBuffer(),redirect:'follow'});
      try{ const sc=r.headers.getSetCookie?r.headers.getSetCookie():[]; const origin=new URL(u); const toAdd=[];
        for(const line of sc){const [pair,...attrs]=line.split(';'); const i=pair.indexOf('='); if(i<0)continue;
          const c={name:pair.slice(0,i).trim(),value:pair.slice(i+1).trim(),domain:origin.hostname,path:'/'};
          for(const a of attrs){const [k,v]=a.split('=').map(x=>(x||'').trim()); if(/^path$/i.test(k)&&v)c.path=v; if(/^domain$/i.test(k)&&v)c.domain=v.replace(/^\./,''); if(/^secure$/i.test(k))c.secure=true; if(/^httponly$/i.test(k))c.httpOnly=true;}
          toAdd.push(c);}
        if(toAdd.length) await ctx.addCookies(toAdd).catch(()=>{});
      }catch(e){}
      const bb=Buffer.from(await r.arrayBuffer()); const h={};
      r.headers.forEach((v,k)=>{if(!/^(content-encoding|content-length|transfer-encoding|content-security-policy|set-cookie)/i.test(k))h[k]=v;});
      const o={status:r.status,headers:h,body:bb}; if(cacheable && bb.length<2e6) cacheGet.set(u,o);
      return route.fulfill(o);
    }catch(e){return route.abort().catch(()=>{});}
  };
}
const JOBS=JSON.parse(process.env.JOBS||'[]'); // [{slug,url,mobile?}]
(async()=>{
  const b=await chromium.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
  const out={};
  for(const j of JOBS){
    const ctx=await b.newContext({viewport:j.mobile?{width:390,height:844}:{width:1440,height:900},userAgent:UA,locale:'en-US',extraHTTPHeaders:{'accept-language':'en-US,en;q=0.9'}, deviceScaleFactor:1});
    const cacheGet=new Map(); await ctx.route('**/*',mkRelay(ctx,cacheGet));
    const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,160))); p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,160));});
    try{
      const sep=j.url.includes('?')?'&':'?';
      const url=j.url+sep+`preview_theme_id=${THEME}&_ab=0&_fd=0&_sc=1`;
      // mot de passe boutique (env PW) : POST sur /password via le relais, le cookie storefront_digest est posé sur le contexte
      if(process.env.PW){
        await p.goto(BASE+'/password',{waitUntil:'load',timeout:90000});
        const st=await p.evaluate(async(pw)=>{const r=await fetch('/password',{method:'POST',body:new URLSearchParams({form_type:'storefront_password',utf8:'✓',password:pw}),redirect:'follow',credentials:'include'});return r.status+' '+r.url;},process.env.PW);
        console.log('password:',st); await p.waitForTimeout(800);
      }
      if(process.env.ADD_VARIANT && j.addToCart){ await p.goto(BASE+'/?preview_theme_id='+THEME,{waitUntil:'load',timeout:90000}); const st=await p.evaluate(async(id)=>{const r=await fetch('/cart/add.js',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({items:[{id:Number(id),quantity:1}]})});return r.status;},process.env.ADD_VARIANT); console.log('cart/add:',st); }
      // première requête pour poser le cookie de preview, puis navigation
      await p.goto(url,{waitUntil:'load',timeout:90000}); await p.waitForTimeout(2500);
      await p.goto(url,{waitUntil:'load',timeout:90000}); await p.waitForTimeout(3500);
      await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=700){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}window.scrollTo(0,0);});
      await p.waitForTimeout(1500);
      await p.screenshot({path:`preview/${j.slug}.png`,fullPage:true});
      out[j.slug]=await p.evaluate(()=>{
        const cs=n=>getComputedStyle(n);
        const themeId=(document.documentElement.outerHTML.match(/Shopify\.theme\s*=\s*(\{[^}]*\})/)||[])[1]||null;
        const h1=document.querySelector('h1'); const btn=document.querySelector('.button, button[name="add"]');
        const sections=[...document.querySelectorAll('.shopify-section')].map(s=>s.id.replace('shopify-section-','')+':'+Math.round(s.getBoundingClientRect().height));
        const fonts=[...new Set([...document.querySelectorAll('h1,h2,p,a,.button')].slice(0,60).map(n=>cs(n).fontFamily.split(',')[0].replace(/["']/g,'')))];
        const imgs=[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.currentSrc.slice(0,100));
        return {title:document.title, themeId, h1:h1?h1.innerText.trim().slice(0,80):null, h1font:h1?cs(h1).fontFamily.split(',')[0]:null, bodyFont:cs(document.body).fontFamily.split(',')[0], bodyBg:cs(document.body).backgroundColor, btn:btn?{bg:cs(btn).backgroundColor,r:cs(btn).borderRadius,txt:btn.innerText.trim().slice(0,30)}:null, sections, fonts, brokenImgs:imgs.slice(0,8), height:document.body.scrollHeight, text:document.body.innerText.replace(/\s+/g,' ').slice(0,1500)};
      });
      out[j.slug].errors=errs.slice(0,6);
      console.log(`OK ${j.slug} ${out[j.slug].height}px theme=${out[j.slug].themeId} h1="${out[j.slug].h1}" fonts=${out[j.slug].fonts.join('|')}`);
    }catch(e){out[j.slug]={err:String(e).split('\n')[0].slice(0,200),errors:errs}; console.log('ECHEC',j.slug,out[j.slug].err);}
    await ctx.close();
  }
  fs.writeFileSync('preview/report.json',JSON.stringify(out,null,1)); await b.close();
})();
```

---

# ▶ tools/qa-crawl.cjs

_Fichier : `build/tools/qa-crawl.cjs`_

```javascript
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
```

---

# ▶ tools/qa-links.cjs

_Fichier : `build/tools/qa-links.cjs`_

```javascript
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
```



# ══════ PARTIE 11 — INVENTAIRE DES IMAGES ══════


277 fichiers image et marque dans le dépôt (les images elles-mêmes ne tiennent pas dans un texte) :

- `build/brand/favicon-180.png`
- `build/brand/favicon-32.png`
- `build/brand/favicon-512.png`
- `build/brand/fonts/Fraunces-Wordmark-Soft350.ttf`
- `build/brand/fonts/Fraunces-var.ttf`
- `build/brand/fonts/Fredoka-var.ttf`
- `build/brand/fonts/Inter-var.ttf`
- `build/brand/fonts/Manrope-var.ttf`
- `build/brand/fonts/Nunito-var.ttf`
- `build/brand/fonts/Outfit-var.ttf`
- `build/brand/fonts/PlusJakartaSans-var.ttf`
- `build/brand/fonts/Urbanist-var.ttf`
- `build/brand/fonts/somnila-sans-manrope-var.woff2`
- `build/brand/fonts/somnila-serif-fraunces-soft-var.woff2`
- `build/brand/horizon-line.svg`
- `build/brand/logo-board.png`
- `build/brand/logo/app-icon-night-1024.png`
- `build/brand/logo/app-icon-night.svg`
- `build/brand/logo/avatar-mist-1024.png`
- `build/brand/logo/avatar-mist.svg`
- `build/brand/logo/avatar-night-1024.png`
- `build/brand/logo/avatar-night.svg`
- `build/brand/logo/favicon.svg`
- `build/brand/logo/somnila-logo-cloud.png`
- `build/brand/logo/somnila-logo-cloud.svg`
- `build/brand/logo/somnila-logo-dark.png`
- `build/brand/logo/somnila-logo-dark.svg`
- `build/brand/logo/somnila-logo-light.png`
- `build/brand/logo/somnila-logo-light.svg`
- `build/brand/logo/somnila-logo-night.png`
- `build/brand/logo/somnila-logo-night.svg`
- `build/brand/logo/somnila-logo-on-black.png`
- `build/brand/logo/somnila-logo-on-black.svg`
- `build/brand/logo/somnila-logo-on-night.png`
- `build/brand/logo/somnila-logo-on-night.svg`
- `build/brand/logo/somnila-mark-cloud.png`
- `build/brand/logo/somnila-mark-cloud.svg`
- `build/brand/logo/somnila-mark-dawn-on-night.png`
- `build/brand/logo/somnila-mark-dawn-on-night.svg`
- `build/brand/logo/somnila-mark-dawn.png`
- `build/brand/logo/somnila-mark-dawn.svg`
- `build/brand/logo/somnila-mark-night.png`
- `build/brand/logo/somnila-mark-night.svg`
- `build/images/shopify/somnila_body-01_packshot-blush-4_1x1_v1.jpg`
- `build/images/shopify/somnila_body-01_packshot-blush-and-sky-6_1x1_v1.jpg`
- `build/images/shopify/somnila_body-01_packshot-ice-5_1x1_v1.jpg`
- `build/images/shopify/somnila_body-01_packshot-night_1x1_v1.jpg`
- `build/images/shopify/somnila_body-01_packshot-sky-3_1x1_v1.jpg`
- `build/images/shopify/somnila_body-01_packshot-sky-8_1x1_v1.jpg`
- `build/images/shopify/somnila_body-01_packshot-sky-and-blush-7_1x1_v1.jpg`
- `build/images/shopify/somnila_body-01_packshot-stone-2_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_lifestyle-blue-4_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_lifestyle-blush-5_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_lifestyle-cloud-3_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_packshot-blue-10_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_packshot-blue-10_1x1_v2.jpg`
- `build/images/shopify/somnila_contour-01_packshot-blush-7_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_packshot-blush-7_1x1_v2.jpg`
- `build/images/shopify/somnila_contour-01_packshot-cloud-6_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_packshot-cloud-6_1x1_v2.jpg`
- `build/images/shopify/somnila_contour-01_packshot-night-2_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_packshot-night_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_packshot-night_1x1_v2.jpg`
- `build/images/shopify/somnila_contour-01_packshot-stone-8_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-01_packshot-stone-8_1x1_v2.jpg`
- `build/images/shopify/somnila_contour-01_packshot-stone-9_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-for-two_packshot-night-2_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-for-two_packshot-night_1x1_v1.jpg`
- `build/images/shopify/somnila_contour-for-two_packshot-night_1x1_v2.jpg`
- `build/images/shopify/somnila_cover-body_packshot-night_1x1_v1.jpg`
- `build/images/shopify/somnila_cover-contour_packshot-night_1x1_v1.jpg`
- `build/images/shopify/somnila_cover-contour_packshot-night_1x1_v2.jpg`
- `build/images/shopify/somnila_cover-neck_packshot-cloud_1x1_v1.jpg`
- `build/images/shopify/somnila_cover-side_packshot-blue_1x1_v1.jpg`
- `build/images/shopify/somnila_cover-side_packshot-blue_1x1_v2.jpg`
- `build/images/shopify/somnila_evening-set_packshot-stone-and-sand_4x5_v1.jpg`
- `build/images/shopify/somnila_family-set_packshot-cloud_1x1_v1.jpg`
- `build/images/shopify/somnila_family-set_packshot-sky-2_1x1_v1.jpg`
- `build/images/shopify/somnila_family-set_packshot-stone-3_1x1_v1.jpg`
- `build/images/shopify/somnila_family-set_packshot-stone-3_1x1_v2.jpg`
- `build/images/shopify/somnila_for-two_packshot-cloud_1x1_v1.jpg`
- `build/images/shopify/somnila_for-two_packshot-sky-2_1x1_v1.jpg`
- `build/images/shopify/somnila_lounge-01_packshot-blue-2_4x5_v1.jpg`
- `build/images/shopify/somnila_lounge-01_packshot-blue-2_4x5_v2.jpg`
- `build/images/shopify/somnila_lounge-01_packshot-stone-and-sand_4x5_v1.jpg`
- `build/images/shopify/somnila_mask-01_packshot-black-6_1x1_v1.jpg`
- `build/images/shopify/somnila_mask-01_packshot-black_1x1_v1.jpg`
- `build/images/shopify/somnila_mask-01_packshot-blush-3_1x1_v1.jpg`
- `build/images/shopify/somnila_mask-01_packshot-cloud-2_1x1_v1.jpg`
- `build/images/shopify/somnila_mask-01_packshot-heather-grey-5_1x1_v1.jpg`
- `build/images/shopify/somnila_mask-01_packshot-violet-4_1x1_v1.jpg`
- `build/images/shopify/somnila_neck-01-cover-set_packshot-cloud_1x1_v1.jpg`
- `build/images/shopify/somnila_neck-01_packshot-cloud_1x1_v1.jpg`
- `build/images/shopify/somnila_neck-01_packshot-night-3_1x1_v1.jpg`
- `build/images/shopify/somnila_neck-01_packshot-night-3_1x1_v2.jpg`
- `build/images/shopify/somnila_neck-01_packshot-sky-2_1x1_v1.jpg`
- `build/images/shopify/somnila_neck-01_packshot-stone-4_1x1_v1.jpg`
- `build/images/shopify/somnila_neck-01_packshot-stone-4_1x1_v2.jpg`
- `build/images/shopify/somnila_quiet-01_packshot-blue_1x1_v1.jpg`
- `build/images/shopify/somnila_quiet-01_packshot-blue_1x1_v2.jpg`
- `build/images/shopify/somnila_quiet-01_packshot-blush-4_1x1_v1.jpg`
- `build/images/shopify/somnila_quiet-01_packshot-blush-4_1x1_v2.jpg`
- `build/images/shopify/somnila_quiet-01_packshot-butter-3_1x1_v1.jpg`
- `build/images/shopify/somnila_quiet-01_packshot-butter-3_1x1_v2.jpg`
- `build/images/shopify/somnila_quiet-01_packshot-green-2_1x1_v1.jpg`
- `build/images/shopify/somnila_quiet-01_packshot-green-2_1x1_v2.jpg`
- `build/images/shopify/somnila_quiet-night_packshot-black_1x1_v1.jpg`
- `build/images/shopify/somnila_quiet-night_packshot-blue-2_1x1_v1.jpg`
- `build/images/shopify/somnila_quiet-night_packshot-blue-2_1x1_v2.jpg`
- `build/images/shopify/somnila_side-01_packshot-blue_1x1_v1.jpg`
- `build/images/shopify/somnila_side-01_packshot-blue_1x1_v2.jpg`
- `build/images/shopify/somnila_side-01_packshot-dark-grey-2_1x1_v1.jpg`
- `build/images/shopify/somnila_side-01_packshot-dark-grey-2_1x1_v2.jpg`
- `build/images/shopify/somnila_side-01_packshot-dark-grey-3_1x1_v1.jpg`
- `build/images/shopify/somnila_side-01_packshot-red-4_1x1_v1.jpg`
- `build/images/shopify/somnila_side-01_packshot-red-4_1x1_v2.jpg`
- `build/images/shopify/somnila_side-sleeper-set_packshot-night-2_1x1_v1.jpg`
- `build/images/shopify/somnila_side-sleeper-set_packshot-night_1x1_v1.jpg`
- `build/images/shopify/somnila_side-sleeper-set_packshot-night_1x1_v2.jpg`
- `build/images/shopify/somnila_sleep-set_packshot-black-2_1x1_v1.jpg`
- `build/images/shopify/somnila_sleep-set_packshot-blue-3_1x1_v1.jpg`
- `build/images/shopify/somnila_sleep-set_packshot-blue-3_1x1_v2.jpg`
- `build/images/shopify/somnila_sleep-set_packshot-cloud_1x1_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-blush_4x3_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-cream_4x3_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-lime_4x3_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-sage_4x3_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-salmon_4x3_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-sand_4x3_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-sky_4x3_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-slate_4x3_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-stone_4x3_v1.jpg`
- `build/images/shopify/somnila_throw-01_detail-yellow_4x3_v1.jpg`
- `build/images/site/ads/somnila_ad_sleep-well_1x1.jpg`
- `build/images/site/ads/somnila_ad_sleep-well_4x5.jpg`
- `build/images/site/ads/somnila_ad_sleep-well_9x16.jpg`
- `build/images/site/ads/somnila_ad_thirty-nights_1x1.jpg`
- `build/images/site/ads/somnila_ad_thirty-nights_4x5.jpg`
- `build/images/site/ads/somnila_ad_thirty-nights_9x16.jpg`
- `build/images/site/ads/somnila_ad_two-heights_1x1.jpg`
- `build/images/site/ads/somnila_ad_two-heights_4x5.jpg`
- `build/images/site/ads/somnila_ad_two-heights_9x16.jpg`
- `build/images/site/banners/somnila_collection_accessories_3x1.jpg`
- `build/images/site/banners/somnila_collection_covers_3x1.jpg`
- `build/images/site/banners/somnila_collection_memory-foam-pillows_3x1.jpg`
- `build/images/site/banners/somnila_collection_sets_3x1.jpg`
- `build/images/site/banners/somnila_collection_shop-all_3x1.jpg`
- `build/images/site/contour-01-night-cutout.png`
- `build/images/site/email/somnila_email_footer_1200x300.jpg`
- `build/images/site/email/somnila_email_header_1200x400.jpg`
- `build/images/site/lounge-01-cutout.png`
- `build/images/site/neck-01-cloud-cutout-v2.png`
- `build/images/site/neck-01-cloud-cutout.png`
- `build/images/site/packshots/somnila_contour-01_packshot-blue-10_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-blue-10_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-blush-7_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-blush-7_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-cloud-6_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-cloud-6_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-night-2_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-night-2_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-night_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-night_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-stone-8_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_contour-01_packshot-stone-8_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_contour-for-two_packshot-night-2_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_contour-for-two_packshot-night-2_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_contour-for-two_packshot-night_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_contour-for-two_packshot-night_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_cover-contour_packshot-night_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_cover-contour_packshot-night_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_cover-neck_packshot-cloud_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_cover-neck_packshot-cloud_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_cover-side_packshot-blue_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_cover-side_packshot-blue_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_evening-set_packshot-stone-and-sand_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_evening-set_packshot-stone-and-sand_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_family-set_packshot-cloud_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_family-set_packshot-cloud_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_family-set_packshot-sky-2_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_family-set_packshot-sky-2_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_family-set_packshot-stone-3_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_family-set_packshot-stone-3_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_for-two_packshot-cloud_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_for-two_packshot-cloud_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_for-two_packshot-sky-2_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_for-two_packshot-sky-2_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_lounge-01_packshot-blue-2_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_lounge-01_packshot-blue-2_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_lounge-01_packshot-stone-and-sand_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_lounge-01_packshot-stone-and-sand_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_neck-01-cover-set_packshot-cloud_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_neck-01-cover-set_packshot-cloud_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_neck-01_packshot-cloud_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_neck-01_packshot-cloud_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_neck-01_packshot-night-3_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_neck-01_packshot-night-3_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_neck-01_packshot-sky-2_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_neck-01_packshot-sky-2_v1_sky_4x5.jpg`
- `build/images/site/packshots/somnila_neck-01_packshot-stone-4_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_neck-01_packshot-stone-4_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_side-01_packshot-blue_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_side-01_packshot-blue_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_side-01_packshot-dark-grey-2_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_side-01_packshot-dark-grey-2_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_side-01_packshot-red-4_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_side-01_packshot-red-4_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_side-sleeper-set_packshot-night_v2_sky_1x1.jpg`
- `build/images/site/packshots/somnila_side-sleeper-set_packshot-night_v2_sky_4x5.jpg`
- `build/images/site/packshots/somnila_sleep-set_packshot-cloud_v1_sky_1x1.jpg`
- `build/images/site/packshots/somnila_sleep-set_packshot-cloud_v1_sky_4x5.jpg`
- `build/images/site/side-01-blue-cutout.png`
- `build/images/site/social/somnila_avatar_1024.png`
- `build/images/site/social/somnila_cover_1500x500.jpg`
- `build/images/site/social/somnila_share_1200x630.jpg`
- `build/images/site/somnila_contour-01_materials_1x1_v1.jpg`
- `build/images/site/somnila_neck-01_hero_16x9_v1.jpg`
- `build/images/site/somnila_neck-01_hero_16x9_v2.jpg`
- `build/images/site/somnila_neck-01_hero_4x5_v1.jpg`
- `build/images/site/somnila_neck-01_hero_4x5_v2.jpg`
- `build/images/site/somnila_neck-01_sky_1x1_v1.jpg`
- `build/images/source/01-oreiller-telephone/oreiller-telephone_bleu_34_25.jpg`
- `build/images/source/01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg`
- `build/images/source/01-oreiller-telephone/oreiller-telephone_gris-blanc_34_34.jpg`
- `build/images/source/01-oreiller-telephone/oreiller-telephone_jaune_34_55.jpg`
- `build/images/source/01-oreiller-telephone/oreiller-telephone_noir_34_32.jpg`
- `build/images/source/01-oreiller-telephone/oreiller-telephone_rose_34_52.jpg`
- `build/images/source/02-couverture/couverture_beige_lit_39.jpeg`
- `build/images/source/02-couverture/couverture_blanc-creme_lit_40.jpeg`
- `build/images/source/02-couverture/couverture_bleu-ardoise_lit_41.jpeg`
- `build/images/source/02-couverture/couverture_bleu-clair_lit_42.jpeg`
- `build/images/source/02-couverture/couverture_gris_lit_43.jpeg`
- `build/images/source/02-couverture/couverture_jaune_lit_44.jpeg`
- `build/images/source/02-couverture/couverture_orange-saumon_lit_45.jpeg`
- `build/images/source/02-couverture/couverture_rose_lit_46.jpeg`
- `build/images/source/02-couverture/couverture_vert-anis_lit_47.jpeg`
- `build/images/source/02-couverture/couverture_vert-sauge_lit_48.jpeg`
- `build/images/source/03-masque/masque_blanc_face_04.jpg`
- `build/images/source/03-masque/masque_blanc_face_09.jpg`
- `build/images/source/03-masque/masque_gris-chine_face_38.jpg`
- `build/images/source/03-masque/masque_noir_face_05.jpg`
- `build/images/source/03-masque/masque_noir_face_16.jpg`
- `build/images/source/03-masque/masque_rose_face_03.jpg`
- `build/images/source/03-masque/masque_violet-blanc_face_20.jpg`
- `build/images/source/04-bouchons/bouchons_bleu_boite_17.jpg`
- `build/images/source/04-bouchons/bouchons_jaune-lait_boite_19.jpg`
- `build/images/source/04-bouchons/bouchons_rose_boite_28.jpg`
- `build/images/source/04-bouchons/bouchons_vert_boite_14.jpg`
- `build/images/source/09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg`
- `build/images/source/09-oreiller-cervical/oreiller-cervical_bleu-clair_34_31.jpg`
- `build/images/source/09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg`
- `build/images/source/09-oreiller-cervical/oreiller-cervical_gris_34_21.jpg`
- `build/images/source/10-oreiller-lateral/oreiller-lateral_bleu_34_01.jpg`
- `build/images/source/10-oreiller-lateral/oreiller-lateral_gris-clair_34_35.jpg`
- `build/images/source/10-oreiller-lateral/oreiller-lateral_gris-fonce_34_26.jpg`
- `build/images/source/10-oreiller-lateral/oreiller-lateral_gris-fonce_34_54.jpg`
- `build/images/source/10-oreiller-lateral/oreiller-lateral_rose_34_33.jpg`
- `build/images/source/10-oreiller-lateral/oreiller-lateral_rouge_34_27.jpg`
- `build/images/source/11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_07.jpg`
- `build/images/source/11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_50.jpg`
- `build/images/source/11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg`
- `build/images/source/11-oreiller-corporel/oreiller-corporel_bleu-rose_dessus_29.jpg`
- `build/images/source/11-oreiller-corporel/oreiller-corporel_bleu-tres-clair_dessus_53.jpg`
- `build/images/source/11-oreiller-corporel/oreiller-corporel_gris_dessus_18.jpg`
- `build/images/source/11-oreiller-corporel/oreiller-corporel_rose-bleu_dessus_00.jpg`
- `build/images/source/11-oreiller-corporel/oreiller-corporel_rose_dessus_24.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_blanc_34_08.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_blanc_lifestyle_30.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_bleu-marine_34_37.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_bleu_34_22.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_bleu_34_23.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_bleu_lifestyle_02.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_gris-blanc_34_11.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_gris_34_12.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_rose-blanc_34_10.jpg`
- `build/images/source/12-oreiller-vague/oreiller-vague_rose_lifestyle_15.jpg`