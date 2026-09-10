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
