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
