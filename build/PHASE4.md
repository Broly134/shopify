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
- **Collections** : `pillows` (5), `sets` (8), `accessories` (3), `covers`
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
- **Collection `pillows`** : la première tentative de Phase 3 avait bien
  créé une collection `pillows` vide malgré l'erreur affichée. Les 5
  oreillers y sont maintenant, et la collection provisoire `somnila-pillows`
  (créée par moi, vide après transfert) a été supprimée. L'URL finale
  `/collections/pillows` est donc déjà la bonne.
- **Traductions héritées retirées.** Le duplicata avait copié les
  traductions PORTANCE du thème (en, de, es, it, nl : 270 clés × 5 langues)
  qui **écrasaient mes textes** dans l'aperçu (barre d'annonce, puces,
  FAQ, pied de page). Je les ai supprimées sur le thème Somnila uniquement ;
  le thème PORTANCE garde les siennes.
- **Collision d'URL `/collections/pillows`.** En langue anglaise, cette
  adresse renvoie encore vers la collection PORTANCE « Oreillers » (son
  handle traduit en anglais est `pillows`) : la section « Five pillows » de
  l'accueil et le lien du menu affichent Appui / Aplomb au lieu de la gamme
  Somnila. Ça se règle en une opération que la règle 4 me fait te demander
  (voir § 3).
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
   langues PORTANCE (de, es, fr, it, nl) pour une boutique 100 % anglais, et
   suppression du handle anglais `pillows` de la collection PORTANCE
   « Oreillers » (une traduction, réversible) pour libérer
   `/collections/pillows`.
3. **Aperçu complet** : si tu veux voir l'accueil avec les produits,
   active le mot de passe de la boutique (Boutique en ligne → Préférences)
   et dis-le-moi : je passe les 20 produits en actif, ils restent invisibles
   du public.
4. **Checklist manuelle** (elle ne bouge pas) : Shopify Payments / PayPal,
   domaine `somnila.com`, marché principal = États-Unis et langue principale
   = anglais (Paramètres → Marchés / Langues), pixels Meta / GA4 / TikTok,
   adresse d'expéditeur `hello@somnila.com` (ou autre) dans Paramètres →
   Notifications, réseaux sociaux (liens à me donner), publication du thème,
   retrait du mot de passe. Détail dans `HANDOFF.md` en Phase 7.
