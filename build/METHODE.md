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

## 11. Passe conversion

1. Lire la structure des deux sites de référence (Derila, Pilloway) section par section, noter l'ordre et ce que chaque section prouve.
2. Lire les schémas des sections Shrine disponibles (`multicolumn`, `comparison-table`, `image-with-text`, `rich-text`, `featured-product`) : les clés inconnues sont ignorées en silence, une image d'`icons-with-content` est un bloc et pas un réglage.
3. Réécrire `templates/index.json` et `templates/product.json` en local, puis les envoyer avec `themeFilesUpsert` sur le thème non publié.
4. Uploader les images dans Files par URL brute GitHub (`fileCreate`), puis relire les noms réels avec `files(query:"filename:…")` : Shopify ajoute un suffixe UUID et refuse `fileUpdate(filename:)`.
5. Rendre l'aperçu avec `build/tools/render.cjs` (mot de passe, desktop et mobile), découper les captures en tranches, corriger, renvoyer, re-rendre. Trois passes ont suffi.
6. Documenter dans `build/CONVERSION.md`, committer, pousser.
7. Animations : activer `enable_load_animations` dans `settings_data.json` (lire le fichier du thème, modifier, renvoyer entier sans toucher aux blobs `animations_type`/`fav_collection`), ajouter la section `horizontal-ticker`, écrire la couche CSS dans `somnila-styles`, puis sonder le DOM (Playwright) pour vérifier que les classes de révélation sont bien ajoutées et que les animations calculées sont actives.
