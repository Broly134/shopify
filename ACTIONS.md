# Ce que tu dois faire toi-même

Classé par urgence. Les trois premières lignes ne sont pas faisables par API — Shopify
les réserve à l'admin.

---

## Aujourd'hui

### 1. Repasser Shopify en Basic — **économie ~$360/mois**

`Réglages → Forfait → Changer de forfait`

Tu es sur **Advanced à $399/mois**. Ce forfait n'est rentable qu'au-delà de ~$72 000 de
CA mensuel : l'écart de commission (2,4 % contre 2,9 %) ne compense pas la différence
d'abonnement avant ce seuil.

**C'est de loin l'action la plus rentable de cette liste.** Sur trois mois elle libère
~$1 080 — davantage que le budget de lancement dont tu disposes. Fais-la avant tout le reste.

### 2. Renommer la boutique

`Réglages → Détails de la boutique → Nom`

`PawDeck` → `FREEHOLD`. Non modifiable par API.

Change aussi l'e-mail de contact : une adresse Gmail personnelle sur une boutique à $249
est un signal négatif pour les processeurs de paiement.

### 3. Passer l'anglais en langue principale

`Réglages → Langues`

L'anglais est **activé et publié**, mais le français reste principal. Or tes fiches
produits, tes pages légales et ton marché sont en anglais. Bascule la langue par défaut,
puis republie le thème.

### 4. Vérifier la marque FREEHOLD — **avant d'imprimer quoi que ce soit**

Recherche USPTO/TESS en **classe 14** (horlogerie) : https://tmsearch.uspto.gov — gratuit,
30 minutes.

⚠️ La recherche a vérifié le DNS des domaines mais **n'a pas pu exécuter de recherche
USPTO ni de RDAP**. Un domaine sans site actif n'est pas une preuve de disponibilité.
Ne commande aucun cadran gravé avant cette vérification.

Si c'est propre, réserve : `freeholdwatches.com`, `freeholdwatch.com`, `wearfreehold.com`
(~$36 au total) et les handles Instagram / TikTok / X.
`freehold.com` est parqué chez Afternic — en vente, probablement à 5 chiffres. Lance sur
`freeholdwatches.com`.

---

## Cette semaine

### 5. Remplir tous les `[TO COMPLETE]`

Les 7 pages contiennent des placeholders entre crochets. Cherche `[TO COMPLETE` dans
`Contenu → Pages`. Il te faut au minimum :

- entité légale, adresse physique réelle, numéro d'immatriculation
- `support@tondomaine.com` (pas de Gmail)
- délais de livraison réels par destination — **le délai réel + 3 jours**
- statut IOSS pour l'UE
- descripteur bancaire = **le nom de la marque** (sinon tu génères des litiges)

Une page publiée avec des crochets visibles est pire qu'une page absente.

### 6. Commander les échantillons

Contacte 10 fournisseurs Alibaba (Verified Supplier, >3 ans, Trade Assurance) avec le
cahier des charges de `docs/produits/architecture-gamme.md`.

**Commande 2 exemplaires identiques chez le même fournisseur**, pas un seul. Comparer deux
unités du même lot mesure la variance intra-lot — c'est ce qui prédit le désastre à 100
unités, et presque personne ne le fait.

Protocole de réception complet (aimant, goutte d'eau, alignement lunette, mesure de marche
sur 5 positions) : `docs/strategie/synthese-strategique.md`, semaine 3.

### 7. Ouvrir les comptes de contenu et publier immédiatement

Avant d'avoir le produit. Le compte doit avoir un historique avant la première vente.
Objectif : 1 publication par jour, dès maintenant.

Avec ton budget, **c'est ça le projet.** La boutique est prête ; le contenu est le seul
goulot d'étranglement qui reste.

---

## Avant la première vente

- [ ] Photos réelles sur les 5 fiches produits (issues des échantillons)
- [ ] Retirer la mention **200 m** si le fournisseur ne fournit pas de rapport de test de pression
- [ ] Passer les produits de `Brouillon` à `Actif`
- [ ] Créer le marché Europe avec l'EUR si tu vends en UE (`Réglages → Marchés`)
- [ ] Tester une commande de bout en bout, y compris un remboursement
- [ ] Vérifier le descripteur bancaire sur un vrai relevé
- [ ] Checklist compliance complète : `docs/compliance/risques-juridiques-et-paiement.md`

---

## À ne jamais faire

| Interdit | Pourquoi |
|---|---|
| Écrire « Seiko » dans un titre produit, une balise SEO ou une annonce | Le mouvement NH35A est un composant Seiko Instruments qu'on peut **nommer factuellement**. Le suggérer comme marque de la montre est de la contrefaçon. |
| Copier une Submariner | Aiguilles Mercedes, cyclope de date, lunette Pepsi/Batman : ce sont des signes distinctifs protégés. Le boîtier coussin et la lunette 120 clics sont fonctionnels, donc sûrs. |
| Promettre un résultat financier | La FTC sanctionne les allégations de revenus. Et ça détruit la crédibilité auprès de l'audience visée. |
| Descendre sous $229 | Le CAC plancher de la catégorie est de $35-45 et ne baisse pas avec ton prix. Sous ce seuil tu perds de l'argent à chaque vente. |
| Faire de la pub sous $3 000 de budget média | Tu paies pour du bruit statistique, pas pour de l'apprentissage. |
| Employer un juron dans une annonce payante | Motif de refus Meta/TikTok. L'angle vit dans l'organique et le packaging — le sens sans le mot. |
