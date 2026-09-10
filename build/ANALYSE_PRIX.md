# Analyse de validation — produits, packs, prix

Mêmes hypothèses que `PRIX.md` : paiement 2,9 % + 0,30 €, retours 5 % (variante
7 % testée), CAC 25 € (20 et 35 testés), fournisseur expédie, housse incluse
avec l'oreiller, livraison offerte dès 54,90 €. Taux EUR→USD observé 1,159.

## 1. Le test qui compte : que reste-t-il par commande si la pub coûte plus cher que prévu

| | Net après CAC 20 € | **CAC 25 €** | CAC 35 € | CAC 25 €, retours 7 % |
|---|---|---|---|---|
| Cervical seul 69,90 | 19,08 | **14,08** | 4,08 | 12,68 |
| Corporel seul 69,90 | 20,08 | **15,08** | 5,08 | 13,68 |
| Contour seul 59,90 | 15,87 | **10,87** | 0,87 | 9,67 |
| Latéral seul 54,90 | 10,26 | **5,26** | −4,74 | 4,16 |
| Lecture seul 54,90 | 10,76 | **5,76** | −4,24 | 4,66 |
| Couverture seule 59,90 | 15,87 | **10,87** | 0,87 | 9,67 |
| Oreiller + housse 76,90 | 22,52 | **17,52** | 7,52 | 15,99 |
| Sleep set 99,90 | 31,71 | **26,71** | 16,71 | 24,71 |
| Pour deux 119,90 | 40,13 | **35,13** | 25,13 | 32,73 |
| Dormeur latéral 119,90 | 41,13 | **36,13** | 26,13 | 33,73 |
| Contour pour deux 99,90 | 33,71 | **28,71** | 18,71 | 26,71 |
| Soirée 94,90 | 28,60 | **23,60** | 13,60 | 21,70 |
| Famille 169,90 | 61,18 | **56,18** | 46,18 | 52,78 |

Point mort du héros seul : **CAC 39 €**. Au-dessus, chaque commande d'un
oreiller seul perd de l'argent ; les packs, eux, tiennent jusqu'à 45–80 €.
C'est la conclusion structurante : **la publicité vend des packs et le héros,
rien d'autre.**

Sur le mix attendu de la catégorie (40 % héros seul, 10 % contour, 5 %
corporel, 15 % oreiller + housse, 10 % sleep set, 10 % pour deux, 5 % dormeur
latéral, 5 % famille) : **panier moyen 85,45 €, net moyen 20,90 € par commande
(24 %)**. C'est une entreprise qui vit.

## 2. Verdict ligne par ligne

| Ligne | Verdict | Pourquoi |
|---|---|---|
| Cervical 69,90 | **Validé** | prix affiché du leader, point mort CAC 39 €, marge nette 20 % |
| Corporel S 69,90 | **Validé** | meilleure marge unitaire de la gamme (15,08) ; à pousser en pub avec le héros, pas seulement en pack |
| Contour 59,90 | **Validé** | l'oreiller « valeur » ; à CAC 35 il est à zéro → jamais l'entrée d'une campagne seul, il vend en « pour deux » |
| Latéral 54,90 | Validé **sous condition** | −4,74 à CAC 35 ; existe pour la complétude de gamme et la vente croisée, **jamais en pub** |
| Lecture 54,90 | Validé **sous condition** | même logique ; achat d'impulsion, pack Soirée |
| Couverture 59,90 | Validé, **à surveiller** | 3,2 kg : le devis donne un seul prix de 19 € transport compris, à vérifier sur la première commande réelle vers l'Australie |
| Masque 19,90 / housse 16,90 / bouchons 14,90 | **Validé comme ajouts** | perdent 13 à 18 € s'ils sont la première commande ; n'apparaissent qu'en fiche, en panier et en pack |
| Oreiller + housse 76,90 | **Validé** | +3,45 vs seul : petit gain, mais c'est le pack qui convertit le plus (le geste « une au lavage ») |
| Sleep set 99,90 | **Validé** | +12,62 vs seul, −18 % réels ; le pack de la fiche héros |
| Pour deux 119,90 | **Validé** | +21,05 ; le pack qui fait vivre la catégorie |
| Dormeur latéral 119,90 | **Validé** | +21,05 ; seul pack à deux formes différentes, sens d'usage fort |
| Contour pour deux 99,90 | Validé, **secondaire** | bon pack, mais concurrence « Pour deux » sur l'accueil : vit sur la fiche contour |
| Soirée 94,90 | Validé, **secondaire** | assemble les deux ventes les plus faibles ; fiche lecture et saison froide seulement |
| Famille 169,90 | **Validé** | +42,10 ; 56,63 l'unité, encore × 2,3 le coût |
| Nuit calme 29,90 | **Validé comme ajout panier** | jamais première commande |

## 3. Ce qui change à l'issue de l'analyse

1. **Huit packs, c'est trop à montrer.** On les garde tous, on n'en affiche
   que quatre sur l'accueil et les pubs : Oreiller + housse, Sleep set, Pour
   deux, Famille. Dormeur latéral sur la fiche corporel, Contour pour deux sur
   la fiche contour, Soirée sur la fiche lecture, Nuit calme dans le panier.
   Moins de choix, plus de conversion.

2. **Prix fixes en USD sur le marché principal**, au lieu de la conversion
   flottante. Shopify convertit 69,90 € en 81,01 $ aujourd'hui, 78 $ ou 84 $
   demain selon le taux ; une marque ne laisse pas son prix bouger. Prix
   fixés par liste de prix (fonction native, gratuite), terminaison ,99 :

   | | EUR | **USD fixe** | écart vs conversion |
   |---|---|---|---|
   | Cervical | 69,90 | **79,99** | −1,3 % — passe sous la barre des 80 $ |
   | Corporel S | 69,90 | **79,99** | −1,3 % |
   | Contour | 59,90 | **68,99** | −0,6 % |
   | Latéral, Lecture | 54,90 | **62,99** | −1,0 % |
   | Couverture | 59,90 | **68,99** | −0,6 % |
   | Masque | 19,90 | **22,99** | |
   | Housse | 16,90 | **18,99** | |
   | Bouchons | 14,90 | **16,99** | |
   | Oreiller + housse | 76,90 | **88,99** | |
   | Sleep set | 99,90 | **114,99** | |
   | Pour deux, Dormeur latéral | 119,90 | **137,99** | |
   | Contour pour deux | 99,90 | **114,99** | |
   | Soirée | 94,90 | **108,99** | |
   | Famille | 169,90 | **195,99** | |
   | Nuit calme | 29,90 | **33,99** | |

   Même logique pour le Royaume-Uni (héros **59,99 £**) et le Canada / l'Australie
   (arrondi ,99). Le seuil de livraison offerte suit : 62,99 $ US, 47,99 £,
   84,99 $ CA, 94,99 $ AU.

3. **Provision retours à 7 % sur les oreillers** dans le suivi (pas dans les
   prix) : un fournisseur qui expédie ne reprend pas les retours, on
   remboursera sans retour. Le héros reste à 12,68 net.

4. **Règle de publicité gravée** : les campagnes ne poussent que le cervical,
   le corporel et les quatre packs. Aucune campagne sur un accessoire, un
   latéral ou un lecture seul. C'est ce qui protège la marge si le CAC monte.

## 4. Ce qui n'est pas validé, et ne le sera pas sans acte de ta part

- **Bouchons dans une boîte de marque tierce** : accepté par toi. Le risque
  n'est pas le prix, c'est l'unboxing d'un Sleep set à 99,90 avec « iMeBoBo »
  écrit sur un composant. Une boîte neutre chez le fournisseur réglerait ça.
- **Composition des matières inconnue** : les fiches diront ce que le devis
  dit, rien de plus. En Europe, l'étiquetage textile exige la composition sur
  le produit ; c'est le fournisseur qui l'appose, pas la boutique.

Tout le reste est validé : la grille passe en Phase 3 telle quelle.
