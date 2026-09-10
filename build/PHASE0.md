# Phase 0 — Découverte

Date : 10 septembre 2026. Aucune écriture dans Shopify pendant cette phase.

## 1. Fichiers tagués « Shopify » — INTROUVABLES d'ici

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
