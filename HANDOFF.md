# Reprise du projet dans une autre session

À lire en premier si tu arrives sur ce projet sans contexte.

## En une phrase

Boutique Shopify **LIYAN** — puériculture haut de gamme : tétines en silicone médical,
biberons en verre borosilicate, anneaux de dentition. Contenu en français, devise EUR.
Signature : لحظات صغيرة، معنى كبير — *Little moments, big meaning*.

## Historique — important pour ne pas se tromper

La boutique a servi successivement à trois projets. Les deux premiers sont abandonnés :

1. **PawDeck / VELYRA** — accessoire auto pour chien et compléments alimentaires. Archivés.
2. **FREEHOLD** — marque de montres mécaniques. Abandonné en cours de route ; toute la
   recherche est conservée dans `archive/freehold/`, elle n'est plus d'actualité.
3. **LIYAN** — le projet en cours. C'est le seul qui compte.

La boutique s'appelle encore **PawDeck** dans les réglages Shopify : c'est un renommage
en attente, pas une erreur de compréhension.

## Ordre de lecture

1. `README.md` — état de la boutique et gamme
2. `ACTIONS.md` — **ce qui reste à faire**
3. `docs/compliance/normes-puericulture.md` — **à lire avant toute vente**
4. `docs/produits/charte-de-marque.md` — couleurs, typographies, index des visuels

## Boutique connectée

| | |
|---|---|
| Domaine admin | `07beme-9h.myshopify.com` |
| Vitrine | `pawdeck-store.myshopify.com` |
| Devise | EUR |
| Forfait | Advanced — **à redescendre en Basic** |
| Commandes | 0 |

## Déjà fait

- 5 produits LIYAN actifs, visuels importés sur le CDN Shopify, stock à 0
- 4 collections intelligentes par type de produit
- 7 pages en français : Notre histoire, Sécurité & Conformité, Livraison,
  Retours & Remboursements, Questions fréquentes, CGV, Nous contacter
- Menus principal et pied de page refaits
- Anciens produits des deux projets précédents archivés

## Ce qui reste — et pourquoi l'API n'a pas suffi

| Tâche | Blocage |
|---|---|
| Renommer la boutique en LIYAN | La ressource Shop est en lecture seule dans l'API Admin |
| Refaire la bannière du thème Horizon | Écriture interdite sur un thème publié |
| Redescendre le forfait | Action de facturation, réservée à l'admin |
| Passer le français en langue principale | Déjà le cas — le français est la langue principale |

## Points à ne pas casser

- **Le stock à 0 est délibéré.** Il empêche toute vente tant que le dossier de conformité
  (EN 1400, EN 14350, EN 71, marquage CE) n'est pas constitué. Ne le remplis pas « pour
  que ça marche ».
- **Les mentions de normes sur les pages sont des engagements non encore prouvés.** Elles
  portent un `[À COMPLÉTER]` explicite. Soit on obtient les rapports d'essai, soit on
  retire les mentions.
- **L'exception d'hygiène** sur le droit de rétractation suppose des articles buccaux
  livrés scellés individuellement. C'est écrit dans les CGV et les retours.
- Les consignes de sécurité sur chaque fiche produit ne sont pas du remplissage : elles
  couvrent des risques réels (strangulation, brûlure, étouffement).
- Le dépôt a été passé en public pour importer les images. **Il doit repasser en privé.**
