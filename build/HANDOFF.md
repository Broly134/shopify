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

## 7. Passe conversion

L'accueil et la fiche produit ont été restructurés après la QA (cartes par position, problème 01/02/03, comparatif, essai 30 nuits, bande fondateur, upsell sous le bouton d'achat). Une action manuelle de plus : limiter le bandeau cookies aux régions qui l'exigent (Réglages → Confidentialité des clients). Tout est dans `build/CONVERSION.md`.