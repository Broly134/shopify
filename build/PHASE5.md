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
- **Throw 01 n'a aucune photo** (ni chez le fournisseur ni dans tes
  fichiers) : la fiche est en ligne sans image, et l'Evening Set ne montre
  que Lounge 01.
- **Mask 01** : les photos fournisseur montrent le masque sur une forme
  blanche ; gardées telles quelles, sans détourage.
- Les fichiers `_v1` d'origine restent dans `build/images/shopify/` ; rien
  n'est perdu.

## 3. Ce qu'il me faut de toi

1. **Photos de Throw 01** (10 coloris annoncés), ou la décision de retirer
   Throw 01 et l'Evening Set du lancement.
2. **Crédits de génération** (Higgsfield ou autre) si tu veux des scènes
   lifestyle et des UGC sans visage ; sinon on reste sur ces visuels.
3. Toujours en attente de la Phase 4 : politiques à coller (champs entre
   crochets à remplir), branding du checkout, langue principale → anglais.
4. **Shopify Email** : importer `email/somnila_email_header_1200x400.jpg` et
   le pied dans le modèle (Marketing → Shopify Email → modèle de marque).
5. **« ok » pour la Phase 6** (kit de lancement : emails, textes pubs, plan
   de lancement, réseaux).
