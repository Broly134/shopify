# Reprise du projet dans une autre session

À lire en premier si tu arrives sur ce projet sans contexte.

## En une phrase

Boutique Shopify recyclée depuis l'ancien projet PawDeck en **FREEHOLD**, marque de
montres mécaniques automatiques visant l'audience indépendante / anti-salariat.
Positionnement : *« Own your hours outright. »*

## Ordre de lecture

1. `README.md` — état de la boutique et gamme produits
2. `ACTIONS.md` — **ce qui reste à faire**, classé par urgence
3. `docs/strategie/synthese-strategique.md` — le raisonnement complet derrière chaque décision

## Boutique connectée

| | |
|---|---|
| Domaine admin | `07beme-9h.myshopify.com` |
| Vitrine | `pawdeck-store.myshopify.com` |
| Forfait | Advanced — **à redescendre en Basic**, voir `ACTIONS.md` |
| Commandes | 0 |

Nom encore affiché : **PawDeck**. Le renommage en FREEHOLD est la première action en attente.

## Déjà fait (par API)

- 5 anciens produits VELYRA / PawDeck archivés
- Collections `Watches` et `Straps & Accessories`
- 5 produits actifs, 8 SKU, stock suivi à 0 donc affichés en « épuisé »
- 7 pages : Shipping, Returns & Refunds, Warranty, Terms of Service, About, FAQ, Contact
- Menus principal et pied de page recâblés
- Langue anglaise activée et publiée

## Ce qui reste — et pourquoi l'API n'a pas suffi

Ces trois points **nécessitent l'interface d'administration Shopify**, pas l'API. Une
session capable de piloter un navigateur est mieux placée pour les traiter.

| Tâche | Blocage rencontré |
|---|---|
| Renommer la boutique en FREEHOLD | L'API Admin expose la ressource Shop en lecture seule |
| Refaire la bannière d'accueil du thème Horizon | Les écritures de fichiers de thème sont interdites sur un thème publié |
| Redescendre le forfait Advanced → Basic | Action de facturation, réservée à l'admin |
| Passer l'anglais en langue principale | `ShopLocaleInput` n'expose pas le champ `primary` |
| Visuels produits | Génération d'images bloquée par le classificateur de permissions de la session |

## Points à ne pas casser

- Les fiches produits publient volontairement la tolérance de marche **−20/+40 s/jour**.
  C'est un choix de positionnement, pas un oubli à corriger.
- Les pages légales contiennent des `[TO COMPLETE]` : ce sont des champs que seul le
  propriétaire peut renseigner (entité, adresse, e-mail, délais réels).
- Le stock à 0 est délibéré : aucun fournisseur n'est encore validé.
- Ne jamais écrire « Seiko » dans un titre produit, une balise SEO ou une annonce.
  Le mouvement NH35A peut être nommé factuellement ; suggérer la marque est de la contrefaçon.
