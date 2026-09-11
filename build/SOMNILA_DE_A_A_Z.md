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

## 7. Passe conversion (11 septembre)

Après la QA, l'accueil et la fiche produit ont été refaits pour convertir, en s'inspirant de la structure de Derila et Pilloway mais sans leurs leviers trompeurs : hero avec ligne de preuves, cinq cartes « quelle façon de dormir », Neck 01 achetable depuis l'accueil, problème 01/02/03, comparatif six lignes, essai 30 nuits en trois étapes, bande fondateur, dernier appel. Fiche produit : tagline sous le titre, upsell déplacé sous le bouton d'achat. Rapport : `build/CONVERSION.md`.