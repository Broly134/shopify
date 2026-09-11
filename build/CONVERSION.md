# Passe conversion — accueil et fiche produit (11 septembre)

Demande : « améliore le design avec ma DA et mon personal branding, le site ne va pas convertir, inspire-toi de Derila et Pilloway, sans agents ».
Thème modifié : **Somnila — build v1** (157447585949), toujours non publié. Rien n'a été publié, supprimé ni envoyé.

## 1. Ce qui a changé

### Accueil (15 sections, dans l'ordre)

1. **Hero** — « Sleep well. », une phrase de promesse, puis une ligne de preuves en capitales (Free shipping · Ships in 6–10 days · 30-night trial). Deux boutons : *Shop Neck 01* (plein) et *Which pillow is mine?* (contour, renvoie à l'ancre `#which`).
2. **Barre de confiance** — quatre tuiles (livraison offerte, 6–10 jours suivis, essai 30 nuits, housse incluse).
3. **Which pillow is yours?** — cinq cartes, une par façon de dormir, avec le packshot ciel de chaque oreiller et un lien *Shop …*. C'est le bloc « positions » de Derila, sans dessin de silhouette.
4. **Neck 01 en produit vedette** — image, titre, trois puces, prix, couleurs, *Add to cart*, Shop Pay, trois icônes de réassurance. On peut acheter sans quitter l'accueil.
5. **Why it holds.** — trois cartes (deux hauteurs, mousse qui tient, housse lavable).
6. **When did a flat pillow start feeling normal?** — le bloc « THE PROBLEM 01 / 02 / 03 » de Pilloway : il s'affaisse, il n'a qu'une hauteur, il ne se lave pas. Chaque problème se termine par la réponse Somnila.
7. **Somnila or a standard fibre pillow?** — tableau comparatif à six lignes, toutes vérifiables sur la fiche produit (pas de « 97 % satisfaits »). Logo Somnila en tête de colonne, bouton *Shop Neck 01*.
8. **Thirty nights to decide.** — image Neck 01 (4:5) à gauche, trois étapes à droite (Order · Sleep on it · Keep it, or one email), bouton *Start your thirty nights*.
9. **Bande fondateur** — fond Night, caption Dawn « From the workshop », titre « I kept waking up stiff. », le texte du brand book et « what we refused to make ». Bouton *Our story*. Aucun visage.
10. **Avis** — section toujours **désactivée** (aucun avis réel).
11. **Sets, priced honestly.** — quatre sets de la collection.
12. **FAQ** — cinq questions.
13. **Still deciding? Thirty nights.** — dernier appel, deux boutons (*Shop Neck 01*, *All pillows*).
14. **Newsletter** — « Notes from the workshop ».
15. Pied de page inchangé.

Sections retirées : « range » et « materials » (elles répétaient les cartes et la fiche produit).

### Fiche produit (gabarit `product`, les 5 oreillers)

Colonne d'achat, de haut en bas : titre → **tagline** (métachamp `somnila.tagline`, ex. « Two heights on one pillow. Turn it over until your head lies level. ») → trois puces de preuve → prix → couleurs → *Add to cart* + Shop Pay → badges de paiement → date de livraison estimée → trois icônes de réassurance → **upsell Mask 01 / Quiet 01** (déplacé **sous** le bouton d'achat : avant, sur mobile, il repoussait le bouton de 250 px) → description → dimensions, matières, contenu → trois onglets (essai, livraison, entretien). Barre d'achat collante à l'écran.

Sous la colonne : *What you are buying* (trois cartes) → tableau comparatif avec bouton *Add to cart* → *Thirty nights to decide* avec *Add to cart* → FAQ → *Goes with it*.

### Images

Six visuels d'accueil dans `build/images/site/home/`, tous composés à partir des photos fournisseur détourées sur le ciel Cloud → Mist : Neck (cloud), Contour (night), Side (blue), **Body 01 (night, nouveau détourage par saturation + GrabCut)**, Lounge (stone-and-sand), Neck 4:5 pour la section essai. Le packshot ciel de Body 01 est aussi devenu la **première image de sa galerie** (les sept photos sur lit restent derrière).

### CSS (section `somnila-styles`, blocs « passe conversion » et « passe conversion 2 »)

Tagline en serif Slate sous le titre ; ligne de preuves du hero en capitales espacées ; liens des cartes en 600 ; titres des sections comparatif, essai et rich-text à la même échelle que les autres ; caption Dawn sur fond Night ; texte de la bande fondateur limité à 80 rem ; ancre `#which` avec marge de défilement sous l'en-tête collant.

## 2. Décisions

- **Aucun levier trompeur** : pas de compte à rebours, pas de −50 % permanent, pas d'avis inventé, pas de « recommandé par des médecins », pas de compteur de visiteurs. Ce que Derila et Pilloway font avec ces leviers, on le fait avec quatre faits répétés partout : livraison offerte, 6–10 jours suivis, essai 30 nuits, housse lavable.
- **Numérotation 01 / 02 / 03** des problèmes : reprise de Pilloway. Ce n'est pas une séquence, c'est un repère de lecture. Facile à retirer si tu préfères.
- **Comparatif contre « Standard fibre pillow »** : un générique, jamais une marque nommée.
- **« Which pillow is mine? » renvoie à une ancre**, pas à un quiz. Un vrai quiz demande une app payante ou du développement ; à décider plus tard.
- **Noms de fichiers Shopify** : Shopify a ajouté un suffixe UUID aux six images (`somnila_home_pos-neck_1x1_91331e7f-….jpg`, etc.) et refuse de les renommer. Les gabarits pointent vers les noms réels ; rien à faire de ton côté.
- **Section essai** : Shrine n'a pas de colonne image dans « Icons with content » (l'image y est un bloc dans la colonne de texte). J'ai utilisé « Image with text » avec un bloc « texte avec icônes » ; même rendu que Derila, mais natif.

## 3. Ce qu'il te faut faire ou décider

1. **Bandeau cookies** — dans l'aperçu, Shopify affiche « Cookie consent » à tous les visiteurs et il masque le hero. Aux États-Unis il n'est pas obligatoire. Réglages → Confidentialité des clients → Bannière de cookies : limiter aux régions qui l'exigent (UE, Royaume-Uni, Canada). Manuel, je n'y ai pas accès.
2. **Avis** — la section est prête et désactivée. Dès dix avis réels (app d'avis gratuite type Judge.me), on l'active. Pas avant.
3. **Vidéo** — Derila et Pilloway ouvrent sur une vidéo. Si tu as (ou fais tourner) 10 à 20 secondes de la main qui presse la mousse et la voit remonter, le hero et la section essai peuvent l'accueillir. Envoie le fichier ; sans vidéo, l'image reste.
4. **Le reste de la liste HANDOFF.md** est inchangé (renommer la boutique « Somnila », coller les politiques, retirer PORTANCE, publier le thème, retirer le mot de passe).

## 4. Comment vérifier

Avec le mot de passe de la boutique, puis `?preview_theme_id=157447585949` sur : `/`, `/products/neck-01`, `/products/body-01`. Captures dans `build/preview/` (`accueil-desktop.jpg`, `accueil-mobile.jpg`, `neck-01-desktop.jpg`, `neck-01-mobile.jpg`, `contour-01-desktop.jpg`, `body-01-desktop.jpg`).

Fichiers du dépôt : `build/theme/templates/index.json`, `build/theme/templates/product.json`, `build/theme/sections/header-group.json` (et sa copie lisible `somnila-styles.liquid.txt`), `build/images/site/home/`, `build/images/site/packshots/somnila_body-01_packshot-night_v1_sky_*.jpg`.

## 5. Animations (ajout du 11 septembre, sur ta demande « mets plein d'animations »)

Tout est natif Shrine ou CSS/JS dans la section `somnila-styles` ; aucune app, aucun crédit. Lentes, calmes, sur les couleurs de la marque, et coupées d'un coup pour les visiteurs qui ont réglé « réduire les animations ».

**Réglages du thème** (`config/settings_data.json`) : animations de chargement activées (`enable_load_animations`), 700 ms, départ 5 % plus bas, décalage de 120 ms entre les enfants d'une section. Chaque section apparaît en fondu remonté quand elle entre dans l'écran ; les blocs enfants (tableau, cartes) suivent en cascade.

**Bandeau défilant** (« Horizontal Ticker », natif) sous le hero de l'accueil et sous la colonne d'achat de la fiche produit : fond Night, capitales espacées, un point Dawn entre les cinq preuves, 75 s par tour, pause au survol.

**Couche CSS de marque** (bloc « passe animations ») :
- hero : titre, texte puis boutons montent en trois temps (0,15 / 0,35 / 0,55 s) ; l'image dérive très lentement (zoom 5 % sur 24 s, aller-retour) ;
- oreillers sur ciel (produit vedette, section essai) : flottement de 7 px sur 8 s ;
- icônes de la barre de confiance : même flottement, décalé d'une tuile à l'autre ;
- cartes (positions, sets) : élévation de 6 px, ombre Night douce et zoom 5 % de l'image au survol ;
- boutons : légère élévation et ombre au survol ; liens du menu : soulignement qui se déploie ;
- tableau comparatif : les coches apparaissent en « pop » l'une après l'autre quand le tableau entre dans l'écran ;
- titres de section : une ligne d'horizon Dawn se déploie sous le titre à l'entrée dans l'écran ;
- bande fondateur : halo Dawn qui respire lentement derrière le titre ;
- FAQ : le contenu d'une question s'ouvre en fondu remonté ; champ e-mail : anneau Dawn au focus.

**Mécanique** : Shrine ajoute `animate--shown` à une section quand elle entre dans l'écran ; un observateur de 10 lignes ajoute en parallèle `somnila-in`, dont dépendent les coches et les lignes d'horizon, pour qu'elles fonctionnent même si tu désactives un jour les animations du thème. Sans JavaScript, tout est visible d'emblée.

**Ce que je n'ai pas fait** : compte à rebours, compteur de visiteurs, notifications « X vient d'acheter » (règle 1 : rien d'inventé), confettis ou curseurs personnalisés (ça sent l'app). Si tu veux plus de mouvement, la prochaine marche est une vidéo produit dans le hero.
