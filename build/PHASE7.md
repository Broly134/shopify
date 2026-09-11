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
