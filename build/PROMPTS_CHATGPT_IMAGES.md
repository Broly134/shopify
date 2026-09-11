# Prompt ChatGPT — images des fiches produit Somnila, en boucle sur le zip

11 septembre 2026. À utiliser dans une conversation ChatGPT où le brand book et le
zip des photos fournisseur ont déjà été envoyés. Pas de limite de génération :
la liste couvre les 51 photos utilisables du zip et 86 images (packshots ciel de
tous les coloris, scènes de chambre, chevet pour les accessoires, détails matière,
heros 16:9, packs à deux et trois exemplaires, packs multi-produits composés avec
plusieurs photos de référence). Les 37 premières lignes sont l'ordre de
conversion ; le reste suit par produit.

ChatGPT génère en général une image par réponse : la boucle avance à chaque
« suivant ». La table `build/images/kontext-batch.csv` reprend chaque ligne
(colonne `priorite`, `references` pour les packs multi-produits).

## Mode d'emploi

1. Dans la conversation : le brand book (`build/BRAND_BOOK.md`) puis le zip.
2. Coller le prompt ci-dessous en entier.
3. Répondre « suivant » après chaque image. Ne rien ajouter d'autre : chaque mot
   en plus dérive le style.
4. Si ChatGPT dit qu'il ne peut pas utiliser une photo extraite du zip comme
   référence, lui envoyer cette photo seule, puis « suivant ».
5. Télécharger chaque image sous le nom donné et la déposer dans
   `build/images/generated/<produit>/`. Je fais ensuite le contrôle contre les
   photos fournisseur, les formats 4:5 et 16:9 manquants, la compression et
   l'envoi dans les galeries Shopify.

## Relance si la boucle décroche

```
Reprends la boucle à la ligne N de la liste, mêmes règles, même style, sans rien
redemander. Affiche la photo, analyse en trois lignes, génère, contrôle, journal,
puis attends mon « suivant ».
```

## Le prompt (à coller tel quel)

```
Tu es le photographe produit et le directeur artistique de Somnila. Tu as déjà reçu notre brand book (système « nuit et aube » : Cloud #F7F9FC, Mist #DCE8F2, Night #1E2A3A, Dawn #F0B79B, Slate #6B7D90 ; lumière d'aube basse et diffuse ; oreiller en lévitation sur un ciel dégradé ; aucun visage, aucun texte). Je viens de t'envoyer le zip des photos fournisseur.

TA MISSION
Produire, une par une, toutes les images des fiches produit Somnila à partir de ces photos. Chaque image reprend le produit À L'IDENTIQUE et pose uniquement notre STYLE autour de lui.

RÈGLES ABSOLUES (elles priment sur tout le reste)
1. Le produit est recopié à l'identique : même forme, mêmes proportions, même couleur, même tissu et sa trame, mêmes coutures, même zip au même endroit, même angle de vue que la photo. Tu ne le redessines pas, tu ne l'embellis pas, tu n'ajoutes pas de passepoil, de matelassage, de piqûre, d'étiquette. Tu ne montres pas un angle que la photo ne montre pas.
2. Tu ne brandes PAS le produit : aucun logo, aucun mot « somnila », aucune lune, aucune broderie, aucune étiquette, aucun tag, aucun texte, chiffre ou badge nulle part dans l'image. Le branding, c'est le style de l'image (couleurs, lumière, composition), jamais une marque sur l'objet.
3. Aucune personne, aucun visage, aucune main, aucun animal.
4. Rien d'inventé : pas de dimension, pas de coupe de la mousse, pas de « deux hauteurs », pas de coloris qui n'est pas dans le zip, pas de second produit qui n'est pas demandé.
5. Un seul produit par image, sauf les plans « two copies », « three copies » et « set composition ».
6. Tu appliques le code de nettoyage de la ligne (légende ci-dessous) et tu reconstruis le fond naturellement.

CODES DE NETTOYAGE
C1 = retirer les petits caractères chinois imprimés sur l'image.
C2 = retirer le schéma de cotes, les lignes de mesure, tous les chiffres et caractères chinois ; ne garder que l'oreiller.
C3 = retirer le mot « MULTICOLOURED » et les caractères chinois.
C4 = retirer tout le texte chinois, le schéma de cotes et les petites vignettes qui montrent des personnes ; ne garder que l'oreiller.
C5 = retirer tous les badges, médailles, rubans et textes (« Best Pillow », années, étoiles) ; ne garder que l'oreiller.
C6 = retirer les affiches, la peluche et tout objet décoratif ; chambre calme et nue.
C7 = retirer la marque tierce, tout le texte chinois et tous les graphismes imprimés sur l'étui, qui devient un étui mat uni de la même couleur ; garder les deux paires de bouchons exactement telles quelles.
C8 = retirer la forme blanche derrière le masque pour qu'il flotte seul ; garder la forme du masque, la sangle et la couleur.
C9 = retirer entièrement la personne (cheveux, mains, vêtements) ; garder la couverture drapée sur le lit et reconstruire le lit et le mur là où elle était.
C10 = retirer le drap rayé ; l'oreiller en S est le seul objet.

LES PLANS
- « sky packshot » : fond = dégradé vertical lisse, Cloud #F7F9FC en haut vers Mist #DCE8F2 en bas, un halo chaud Dawn #F0B79B flou en bas à droite ; le produit flotte légèrement au-dessus du sol avec une ombre de contact douce, large et faible juste dessous ; produit centré, environ 75 % de la largeur, au moins 40 % de vide ; carré 1024×1024.
- « dawn bedroom » : le produit posé sur un lit fait, draps en percale de coton blanc, couette lin clair, vu depuis le pied du lit légèrement en plongée ; lumière du matin par une fenêtre à gauche qui pose une bande de lumière douce sur le drap ; mur blanc cassé chaud, tête de lit en chêne clair, rien d'autre (pas de plante, cadre, lampe, livre, affiche, jouet) ; le produit est le seul objet coloré. Carré 1024×1024, ou portrait 1024×1536 quand la ligne dit 4:5.
- « nightstand » : le produit posé sur une table de chevet en chêne clair, drap blanc flou derrière, même lumière d'aube, rien d'autre sur la table. Carré.
- « fabric detail » : gros plan macro 85 mm sur le tissu du produit, faible profondeur de champ, trame visible, bord du zip dans le cadre si la photo le montre, fond bleu-blanc flou. Carré.
- « hero 16:9 » : paysage 1536×1024 ; le produit flotte sur le tiers droit, ciel dégradé Cloud vers Mist, halo Dawn derrière et sous le produit à droite ; les deux tiers gauches restent complètement vides et calmes (un titre y sera posé par le site) ; ombre de contact douce ; aucun texte.
- « two copies » / « three copies » : le même produit, même coloris, dupliqué côte à côte en léger décalé (trois exemplaires : en légère diagonale), sur le ciel dégradé, une seule ombre commune. Carré.
- « set composition » : utilise TOUTES les photos listées sur la ligne comme références ; chaque produit reste identique à sa photo ; le plus grand au centre, les petits devant à droite en léger décalé, tous flottant sur le ciel dégradé avec une ombre commune ; rien n'est ajouté. Carré.
- Lumière toujours d'aube : basse, diffuse, un seul côté, léger voile, ombres douces ; jamais de flash, jamais de midi, jamais de reflet brillant, jamais de rendu 3D plastique. Jamais de bleu saturé, jamais de pièce grise de banque d'images. Réalisme photographique mat.

LA BOUCLE, exactement comme ça
A. Ouvre le zip, liste les fichiers, et affiche-moi la photo de la ligne 1 (pour un « set composition », toutes les photos de la ligne).
B. Analyse-la en trois lignes : produit et coloris, ce qui doit être retiré, ce qui doit rester identique.
C. Génère l'image en utilisant cette photo comme référence stricte, au format et au plan indiqués.
D. Contrôle ton image contre la photo : silhouette identique ? couleur identique ? aucun texte, logo, badge, visage ? fond conforme ? au moins 40 % de vide ? Si un point échoue, regénère une fois, sinon passe.
E. Écris une ligne de journal : « n° / fichier source / produit, coloris / plan / nom de sortie / contrôle OK ».
F. Passe IMMÉDIATEMENT à la ligne suivante sans me poser de question. Si tu ne peux générer qu'une image par réponse, termine ta réponse après l'étape E et, dès que je réponds « suivant », reprends à la ligne suivante sans rien redemander. Continue jusqu'à la dernière ligne.
G. Si tu ne peux pas utiliser une image extraite du zip comme référence, dis-le en une phrase et demande-moi de te l'envoyer directement ; ne génère jamais sans référence.
H. À la fin de la liste, dresse le tableau de ce qui a échoué au contrôle et propose une seconde passe ligne par ligne.

PAS DE LIMITE DE NOMBRE. Tu fais toutes les lignes, dans l'ordre. Pas de variantes non demandées.

NOMMAGE : le nom de sortie est donné à chaque ligne ; garde-le tel quel.

LISTE (fichier(s) du zip → produit, coloris → plan, format → nettoyage → nom de sortie)
1. 09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg → Neck 01, Cloud → sky packshot, 1:1 → somnila_neck-01_sky-cloud_1x1_v3.jpg
2. 09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg → Neck 01, Night → sky packshot, 1:1 → C1 → somnila_neck-01_sky-night_1x1_v3.jpg
3. 09-oreiller-cervical/oreiller-cervical_bleu-clair_34_31.jpg → Neck 01, Sky → sky packshot, 1:1 → somnila_neck-01_sky-sky_1x1_v3.jpg
4. 09-oreiller-cervical/oreiller-cervical_gris_34_21.jpg → Neck 01, Stone → sky packshot, 1:1 → C1 → somnila_neck-01_sky-stone_1x1_v3.jpg
5. 09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg → Neck 01, Cloud → dawn bedroom, 1:1 → somnila_neck-01_dawn-bedroom-cloud_1x1_v3.jpg
6. 09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg → Neck 01, Night → dawn bedroom, 1:1 → C1 → somnila_neck-01_dawn-bedroom-night_1x1_v3.jpg
7. 09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg → Neck 01, Cloud → fabric detail, 1:1 → somnila_neck-01_detail-cloud_1x1_v3.jpg
8. 12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg → Contour 01, Night → sky packshot, 1:1 → somnila_contour-01_sky-night_1x1_v3.jpg
9. 12-oreiller-vague/oreiller-vague_blanc_34_08.jpg → Contour 01, Cloud → sky packshot, 1:1 → C5 → somnila_contour-01_sky-cloud_1x1_v3.jpg
10. 12-oreiller-vague/oreiller-vague_gris-blanc_34_11.jpg → Contour 01, Stone → sky packshot, 1:1 → C5 → somnila_contour-01_sky-stone_1x1_v3.jpg
11. 12-oreiller-vague/oreiller-vague_bleu_34_22.jpg → Contour 01, Blue → sky packshot, 1:1 → C5 → somnila_contour-01_sky-blue_1x1_v3.jpg
12. 12-oreiller-vague/oreiller-vague_rose-blanc_34_10.jpg → Contour 01, Blush → sky packshot, 1:1 → C5 → somnila_contour-01_sky-blush_1x1_v3.jpg
13. 12-oreiller-vague/oreiller-vague_blanc_lifestyle_30.jpg → Contour 01, Cloud → dawn bedroom, 1:1 → C6 → somnila_contour-01_dawn-bedroom-cloud_1x1_v3.jpg
14. 10-oreiller-lateral/oreiller-lateral_bleu_34_01.jpg → Side 01, Blue → sky packshot, 1:1 → C2 → somnila_side-01_sky-blue_1x1_v3.jpg
15. 10-oreiller-lateral/oreiller-lateral_gris-fonce_34_26.jpg → Side 01, Dark grey → sky packshot, 1:1 → C2 → somnila_side-01_sky-dark-grey_1x1_v3.jpg
16. 10-oreiller-lateral/oreiller-lateral_rouge_34_27.jpg → Side 01, Red → sky packshot, 1:1 → C2 → somnila_side-01_sky-red_1x1_v3.jpg
17. 11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg → Body 01, Night → sky packshot, 1:1 → C10 → somnila_body-01_sky-night_1x1_v3.jpg
18. 11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_07.jpg → Body 01, Sky → sky packshot, 1:1 → C10 → somnila_body-01_sky-sky_1x1_v3.jpg
19. 11-oreiller-corporel/oreiller-corporel_rose_dessus_24.jpg → Body 01, Blush → sky packshot, 1:1 → C10 → somnila_body-01_sky-blush_1x1_v3.jpg
20. 11-oreiller-corporel/oreiller-corporel_gris_dessus_18.jpg → Body 01, Stone → sky packshot, 1:1 → C10 → somnila_body-01_sky-stone_1x1_v3.jpg
21. 01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg → Lounge 01, Stone and Sand → sky packshot, 1:1 → somnila_lounge-01_sky-stone-and-sand_1x1_v3.jpg
22. 01-oreiller-telephone/oreiller-telephone_bleu_34_25.jpg → Lounge 01, Sky → sky packshot, 1:1 → C3 → somnila_lounge-01_sky-sky_1x1_v3.jpg
23. 01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg → Lounge 01, Stone and Sand → dawn bedroom, 1:1 → somnila_lounge-01_dawn-bedroom-stone-and-sand_1x1_v3.jpg
24. 02-couverture/couverture_blanc-creme_lit_40.jpeg → Throw 01, Cream → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-cream_4x5_v3.jpg
25. 02-couverture/couverture_beige_lit_39.jpeg → Throw 01, Sand → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-sand_4x5_v3.jpg
26. 02-couverture/couverture_vert-sauge_lit_48.jpeg → Throw 01, Sage → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-sage_4x5_v3.jpg
27. 02-couverture/couverture_bleu-ardoise_lit_41.jpeg → Throw 01, Slate → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-slate_4x5_v3.jpg
28. 02-couverture/couverture_bleu-clair_lit_42.jpeg → Throw 01, Sky → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-sky_4x5_v3.jpg
29. 02-couverture/couverture_gris_lit_43.jpeg → Throw 01, Stone → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-stone_4x5_v3.jpg
30. 03-masque/masque_noir_face_05.jpg → Mask 01, Black → sky packshot, 1:1 → C8 → somnila_mask-01_sky-black_1x1_v3.jpg
31. 03-masque/masque_blanc_face_04.jpg → Mask 01, Cloud → sky packshot, 1:1 → C8 → somnila_mask-01_sky-cloud_1x1_v3.jpg
32. 03-masque/masque_rose_face_03.jpg → Mask 01, Blush → sky packshot, 1:1 → C8 → somnila_mask-01_sky-blush_1x1_v3.jpg
33. 04-bouchons/bouchons_bleu_boite_17.jpg → Quiet 01, Blue → sky packshot, 1:1 → C7 → somnila_quiet-01_sky-blue_1x1_v3.jpg
34. 04-bouchons/bouchons_vert_boite_14.jpg → Quiet 01, Green → sky packshot, 1:1 → C7 → somnila_quiet-01_sky-green_1x1_v3.jpg
35. 09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg → For Two (2 × Neck 01), Cloud → two copies side by side, 1:1 → somnila_for-two_sky-cloud_1x1_v3.jpg
36. 09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg → Family Set (3 × Neck 01), Cloud → three copies in a shallow diagonal line, 1:1 → somnila_family-set_sky-cloud_1x1_v3.jpg
37. 12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg → Contour for Two (2 × Contour 01), Night → two copies side by side, 1:1 → somnila_contour-for-two_sky-night_1x1_v3.jpg
38. 11-oreiller-corporel/oreiller-corporel_rose-bleu_dessus_00.jpg → Body 01, Blush and Sky → sky packshot, 1:1 → C10 → somnila_body-01_sky-blush-and-sky_1x1_v3.jpg
39. 11-oreiller-corporel/oreiller-corporel_bleu-rose_dessus_29.jpg → Body 01, Sky and Blush → sky packshot, 1:1 → C10 → somnila_body-01_sky-sky-and-blush_1x1_v3.jpg
40. 11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_50.jpg → Body 01, Sky → sky packshot, 1:1 → C10 → somnila_body-01_sky-sky-2_1x1_v3.jpg
41. 01-oreiller-telephone/oreiller-telephone_gris-blanc_34_34.jpg → Lounge 01, Stone → sky packshot, 1:1 → C4 → somnila_lounge-01_sky-stone_1x1_v3.jpg
42. 01-oreiller-telephone/oreiller-telephone_jaune_34_55.jpg → Lounge 01, Yellow → sky packshot, 1:1 → C4 → somnila_lounge-01_sky-yellow_1x1_v3.jpg
43. 01-oreiller-telephone/oreiller-telephone_noir_34_32.jpg → Lounge 01, Black → sky packshot, 1:1 → C4 → somnila_lounge-01_sky-black_1x1_v3.jpg
44. 01-oreiller-telephone/oreiller-telephone_rose_34_52.jpg → Lounge 01, Blush → sky packshot, 1:1 → C4 → somnila_lounge-01_sky-blush_1x1_v3.jpg
45. 02-couverture/couverture_jaune_lit_44.jpeg → Throw 01, Yellow → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-yellow_4x5_v3.jpg
46. 02-couverture/couverture_orange-saumon_lit_45.jpeg → Throw 01, Salmon → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-salmon_4x5_v3.jpg
47. 02-couverture/couverture_rose_lit_46.jpeg → Throw 01, Blush → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-blush_4x5_v3.jpg
48. 02-couverture/couverture_vert-anis_lit_47.jpeg → Throw 01, Lime → dawn bedroom, 4:5 → C9 → somnila_throw-01_dawn-bedroom-lime_4x5_v3.jpg
49. 03-masque/masque_violet-blanc_face_20.jpg → Mask 01, Violet → sky packshot, 1:1 → C8 → somnila_mask-01_sky-violet_1x1_v3.jpg
50. 03-masque/masque_gris-chine_face_38.jpg → Mask 01, Heather grey → sky packshot, 1:1 → C8 → somnila_mask-01_sky-heather-grey_1x1_v3.jpg
51. 03-masque/masque_noir_face_16.jpg → Mask 01, Black → sky packshot, 1:1 → C8 → somnila_mask-01_sky-black-2_1x1_v3.jpg
52. 04-bouchons/bouchons_jaune-lait_boite_19.jpg → Quiet 01, Butter → sky packshot, 1:1 → C7 → somnila_quiet-01_sky-butter_1x1_v3.jpg
53. 04-bouchons/bouchons_rose_boite_28.jpg → Quiet 01, Blush → sky packshot, 1:1 → C7 → somnila_quiet-01_sky-blush_1x1_v3.jpg
54. 10-oreiller-lateral/oreiller-lateral_gris-fonce_34_54.jpg → Side 01, Dark grey → sky packshot, 1:1 → C2 → somnila_side-01_sky-dark-grey-2_1x1_v3.jpg
55. 12-oreiller-vague/oreiller-vague_bleu-marine_34_37.jpg → Contour 01, Night → sky packshot, 1:1 → somnila_contour-01_sky-night-2_1x1_v3.jpg
56. 12-oreiller-vague/oreiller-vague_gris_34_12.jpg → Contour 01, Stone → sky packshot, 1:1 → C5 → somnila_contour-01_sky-stone-2_1x1_v3.jpg
57. 09-oreiller-cervical/oreiller-cervical_bleu-clair_34_31.jpg → Neck 01, Sky → dawn bedroom, 1:1 → somnila_neck-01_dawn-bedroom-sky_1x1_v3.jpg
58. 09-oreiller-cervical/oreiller-cervical_gris_34_21.jpg → Neck 01, Stone → dawn bedroom, 1:1 → C1 → somnila_neck-01_dawn-bedroom-stone_1x1_v3.jpg
59. 12-oreiller-vague/oreiller-vague_bleu_lifestyle_02.jpg → Contour 01, Blue → dawn bedroom, 1:1 → C6 → somnila_contour-01_dawn-bedroom-blue_1x1_v3.jpg
60. 12-oreiller-vague/oreiller-vague_rose_lifestyle_15.jpg → Contour 01, Blush → dawn bedroom, 1:1 → C6 → somnila_contour-01_dawn-bedroom-blush_1x1_v3.jpg
61. 12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg → Contour 01, Night → dawn bedroom, 1:1 → somnila_contour-01_dawn-bedroom-night_1x1_v3.jpg
62. 10-oreiller-lateral/oreiller-lateral_bleu_34_01.jpg → Side 01, Blue → dawn bedroom, 1:1 → C2 → somnila_side-01_dawn-bedroom-blue_1x1_v3.jpg
63. 11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg → Body 01, Night → dawn bedroom, 1:1 → C10 → somnila_body-01_dawn-bedroom-night_1x1_v3.jpg
64. 11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_07.jpg → Body 01, Sky → dawn bedroom, 1:1 → C10 → somnila_body-01_dawn-bedroom-sky_1x1_v3.jpg
65. 01-oreiller-telephone/oreiller-telephone_bleu_34_25.jpg → Lounge 01, Sky → dawn bedroom, 1:1 → C3 → somnila_lounge-01_dawn-bedroom-sky_1x1_v3.jpg
66. 03-masque/masque_noir_face_05.jpg → Mask 01, Black → nightstand, 1:1 → C8 → somnila_mask-01_nightstand-black_1x1_v3.jpg
67. 04-bouchons/bouchons_bleu_boite_17.jpg → Quiet 01, Blue → nightstand, 1:1 → C7 → somnila_quiet-01_nightstand-blue_1x1_v3.jpg
68. 12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg → Contour 01, Night → fabric detail, 1:1 → somnila_contour-01_detail-night_1x1_v3.jpg
69. 10-oreiller-lateral/oreiller-lateral_bleu_34_01.jpg → Side 01, Blue → fabric detail, 1:1 → C2 → somnila_side-01_detail-blue_1x1_v3.jpg
70. 11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg → Body 01, Night → fabric detail, 1:1 → C10 → somnila_body-01_detail-night_1x1_v3.jpg
71. 01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg → Lounge 01, Stone and Sand → fabric detail, 1:1 → somnila_lounge-01_detail-stone-and-sand_1x1_v3.jpg
72. 02-couverture/couverture_blanc-creme_lit_40.jpeg → Throw 01, Cream → fabric detail, 1:1 → C9 → somnila_throw-01_detail-cream_1x1_v3.jpg
73. 02-couverture/couverture_vert-sauge_lit_48.jpeg → Throw 01, Sage → fabric detail, 1:1 → C9 → somnila_throw-01_detail-sage_1x1_v3.jpg
74. 03-masque/masque_noir_face_05.jpg → Mask 01, Black → fabric detail, 1:1 → C8 → somnila_mask-01_detail-black_1x1_v3.jpg
75. 04-bouchons/bouchons_bleu_boite_17.jpg → Quiet 01, Blue → fabric detail, 1:1 → C7 → somnila_quiet-01_detail-blue_1x1_v3.jpg
76. 09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg → Neck 01, Cloud → hero 16:9, 16:9 → somnila_neck-01_hero-cloud_16x9_v3.jpg
77. 09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg → Neck 01, Night → hero 16:9, 16:9 → C1 → somnila_neck-01_hero-night_16x9_v3.jpg
78. 12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg → Contour 01, Night → hero 16:9, 16:9 → somnila_contour-01_hero-night_16x9_v3.jpg
79. 11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg → Body 01, Night → hero 16:9, 16:9 → C10 → somnila_body-01_hero-night_16x9_v3.jpg
80. 09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg → For Two (2 × Neck 01), Night → two copies side by side, 1:1 → C1 → somnila_for-two_sky-night_1x1_v3.jpg
81. 12-oreiller-vague/oreiller-vague_blanc_34_08.jpg → Contour for Two (2 × Contour 01), Cloud → two copies side by side, 1:1 → C5 → somnila_contour-for-two_sky-cloud_1x1_v3.jpg
82. 09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg → Family Set (3 × Neck 01), Night → three copies in a shallow diagonal line, 1:1 → C1 → somnila_family-set_sky-night_1x1_v3.jpg
83. 09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg + 03-masque/masque_noir_face_05.jpg + 04-bouchons/bouchons_bleu_boite_17.jpg → Sleep Set (Neck 01 + Mask 01 + Quiet 01), Cloud / Black / Blue → set composition, 1:1 → somnila_sleep-set_sky-cloud_1x1_v3.jpg
84. 03-masque/masque_noir_face_05.jpg + 04-bouchons/bouchons_bleu_boite_17.jpg → Quiet Night (Mask 01 + Quiet 01), Black / Blue → set composition, 1:1 → C8 → somnila_quiet-night_sky-black_1x1_v3.jpg
85. 01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg + 02-couverture/couverture_blanc-creme_lit_40.jpeg → Evening Set (Lounge 01 + Throw 01), Stone and Sand / Cream → set composition, 1:1 → somnila_evening-set_sky-stone-and-sand_1x1_v3.jpg
86. 09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg + 11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg → Side-Sleeper Set (Neck 01 + Body 01), Night → set composition, 1:1 → C1 → somnila_side-sleeper-set_sky-night_1x1_v3.jpg

Commence maintenant par la ligne 1.
```

## Ce que j'ai volontairement laissé dehors

- Cinq photos du zip : deux Side 01 en variante 50 cm (écartée du catalogue), un
  masque blanc en 400 px, un doublon de Contour 01 bleu, une photo « Ice » de
  Body 01 qui montre un autre produit avec des cotes en chinois.
- Body 01 Azure / Mint / Apricot, Mask 01 Light grey / Night, Lounge 01 Green :
  coloris du devis sans photo ; on ne génère jamais un coloris sans photo.
- Le pack Neck 01 + Cover : la housse seule n'a pas de photo ; le pack garde le
  packshot de l'oreiller.
- Toute image avec du texte : le texte est posé par le site, jamais par le modèle.
