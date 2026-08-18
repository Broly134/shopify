# Ce que tu dois faire toi-même

---

## Tout de suite

### 1. Repasser le dépôt GitHub en privé

`Settings → General → Danger Zone → Change visibility`

Tu l'as passé public pour que Shopify accède aux images. **C'est fait** : les visuels sont
désormais hébergés sur le CDN Shopify, l'accès public n'a plus d'utilité.

Le dépôt contient ta charte de marque complète et, dans `archive/freehold/`, une analyse
de marché avec des marges et des coûts d'achat cibles. Rien de tout ça n'a vocation à
rester lisible par n'importe qui.

### 2. Renommer la boutique

`Réglages → Détails de la boutique`

Elle s'appelle encore **PawDeck**, sur le domaine `pawdeck-store.myshopify.com`.
Non modifiable par API. Change aussi l'e-mail de contact : une adresse Gmail personnelle
est un signal négatif pour les processeurs de paiement.

### 3. Redescendre en forfait Basic — économie ~360 $/mois

`Réglages → Forfait`

Tu es sur **Advanced**, rentable seulement au-delà d'environ 72 000 € de chiffre d'affaires
mensuel. Sur trois mois, ce changement libère plus que ton budget de lancement.

### 4. Refaire la page d'accueil du thème

`Boutique en ligne → Thèmes → Personnaliser`

Le thème Horizon affiche encore la bannière PawDeck. L'API interdit l'écriture sur un thème
publié. Mets en avant la collection **Coffrets Cadeaux** — c'est le produit d'appel de la
catégorie.

---

## Avant la première vente — non négociable

### 5. Constituer le dossier de conformité

Checklist complète dans [`docs/compliance/normes-puericulture.md`](docs/compliance/normes-puericulture.md).

Il te faut, **du fournisseur et portant sur tes références précises** :

- [ ] Rapports d'essai EN 1400 (tétines), EN 14350 (biberons), EN 71-1/2/3 (anneaux, hochets)
- [ ] Déclaration UE de conformité signée + marquage CE
- [ ] Déclaration contact alimentaire (1935/2004 et 10/2011)
- [ ] Attestation sans BPA ni PVC
- [ ] Traçabilité des lots

**Tant que ces documents n'existent pas, retire de la boutique toute mention de norme.**
Une allégation de conformité invérifiable est plus dangereuse que pas d'allégation du tout.

### 6. Vérifier deux points opérationnels

- [ ] **Scellés individuels** sur tétines, téterelles et anneaux. Sans scellé, tu ne peux
      pas invoquer l'exception d'hygiène et tout retour devient recevable.
- [ ] **Assurance responsabilité civile produits couvrant les nourrissons.** Beaucoup
      d'assureurs excluent cette catégorie — vérifie l'exclusion, pas seulement le contrat.

### 7. Remplir les `[À COMPLÉTER]`

Cherche `[À COMPLÉTER` dans `Contenu → Pages`. Il te faut au minimum : entité légale,
adresse physique réelle, numéro d'immatriculation, TVA, e-mail de contact, délais de
livraison réels, statut IOSS, libellé bancaire (= le nom de la marque).

### 8. Vérifier la marque LIYAN

Recherche d'antériorité en **classe 12 (puériculture)** et **classe 10** auprès de l'INPI
ou de l'EUIPO. `liyan.tn` apparaît sur la charte : si ce domaine et cette marque ne sont
pas déjà à toi, règle ce point avant d'investir dans le packaging.

---

## Ensuite

- [ ] Valider les prix du kit 6 et du coffret naissance contre le coût d'achat réel
- [ ] Trier les trois `visuel-a-classer-*.png` et les affecter aux fiches
- [ ] Ajouter des visuels secondaires sur chaque fiche (une seule image par produit actuellement)
- [ ] Mettre le stock à jour à réception de la première série
- [ ] Créer le marché et la langue arabe si tu vises aussi le public arabophone

---

## À ne jamais faire

| Interdit | Pourquoi |
|---|---|
| Affirmer une norme sans le rapport d'essai correspondant | Tu es juridiquement le fabricant. Une allégation fausse t'expose personnellement. |
| Promettre un bénéfice santé | Une tétine ne soigne rien. La valve anti-colique réduit l'air avalé, c'est un fait mécanique, pas une promesse médicale. |
| Vendre un article buccal non scellé | Impossible d'invoquer l'exception d'hygiène, et risque sanitaire réel. |
| Refuser un remboursement sur un produit défectueux | L'exception d'hygiène ne joue jamais pour un défaut. La garantie légale de 2 ans s'applique. |
| Culpabiliser les parents dans le marketing | Registre le plus répandu du secteur et le plus méprisable. La charte de marque s'y oppose explicitement. |
