# Prompt ChatGPT — images des fiches produit Somnila, en boucle sur le zip

11 septembre 2026. À utiliser dans une conversation ChatGPT où le brand book et le
zip des photos fournisseur ont déjà été envoyés. ChatGPT génère en général une
image par réponse : la boucle avance à chaque « suivant ». Le budget est de 40
images, dans l'ordre de `build/images/kontext-batch.csv` (colonne `priorite`).

## Mode d'emploi

1. Dans la conversation : le brand book (`build/BRAND_BOOK.md`) puis le zip.
2. Coller le prompt ci-dessous en entier.
3. Répondre « suivant » après chaque image. Ne rien ajouter d'autre : chaque mot
   en plus dérive le style.
4. Si ChatGPT dit qu'il ne peut pas utiliser une photo extraite du zip comme
   référence, lui envoyer cette photo seule, puis « suivant ».
5. Télécharger chaque image sous le nom donné et la déposer dans
   `build/images/generated/<produit>/`. Je fais ensuite le recadrage, les formats
   4:5 et 16:9, la compression et l'envoi dans les galeries Shopify.

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
Produire, une par une, les images des fiches produit Somnila à partir de ces photos. Chaque image reprend le produit À L'IDENTIQUE et pose uniquement notre STYLE autour de lui.

RÈGLES ABSOLUES (elles priment sur tout le reste)
1. Le produit est recopié à l'identique : même forme, mêmes proportions, même couleur, même tissu et sa trame, mêmes coutures, même zip au même endroit, même angle de vue que la photo. Tu ne le redessines pas, tu ne l'embellis pas, tu n'ajoutes pas de passepoil, de matelassage, de piqûre, d'étiquette. Tu ne montres pas un angle que la photo ne montre pas.
2. Tu ne brandes PAS le produit : aucun logo, aucun mot « somnila », aucune lune, aucune broderie, aucune étiquette, aucun tag, aucun texte, chiffre ou badge nulle part dans l'image. Le branding, c'est le style de l'image (couleurs, lumière, composition), jamais une marque sur l'objet.
3. Aucune personne, aucun visage, aucune main, aucun animal.
4. Rien d'inventé : pas de dimension, pas de coupe de la mousse, pas de « deux hauteurs », pas de coloris qui n'est pas dans le zip, pas de second produit qui n'est pas demandé.
5. Un seul produit par image, sauf les lignes « two copies » et « three copies ».
6. Tu supprimes ce que la ligne « cleanup » indique (textes chinois, schémas de cotes, faux badges, marque tierce sur l'étui, personne sur les photos de la couverture, forme blanche derrière le masque) et tu reconstruis le fond naturellement.

LE STYLE SOMNILA, à appliquer à chaque image
- « sky packshot » : fond = dégradé vertical lisse, Cloud #F7F9FC en haut vers Mist #DCE8F2 en bas, un halo chaud Dawn #F0B79B flou en bas à droite ; le produit flotte légèrement au-dessus du sol avec une ombre de contact douce, large et faible juste dessous ; produit centré, environ 75 % de la largeur, au moins 40 % de vide ; format carré.
- « dawn bedroom » : le produit posé sur un lit fait, draps en percale de coton blanc, couette lin clair, vu depuis le pied du lit légèrement en plongée ; lumière du matin par une fenêtre à gauche qui pose une bande de lumière douce sur le drap ; mur blanc cassé chaud, tête de lit en chêne clair, rien d'autre (pas de plante, cadre, lampe, livre, affiche, jouet) ; le produit est le seul objet coloré.
- « fabric detail » : gros plan macro 85 mm sur le tissu du produit, faible profondeur de champ, trame visible, bord du zip dans le cadre si la photo le montre, fond bleu-blanc flou.
- « two copies » / « three copies » : le même produit, même coloris, dupliqué côte à côte en léger décalé, sur le ciel dégradé, une seule ombre commune.
- Lumière toujours d'aube : basse, diffuse, un seul côté, léger voile, ombres douces ; jamais de flash, jamais de midi, jamais de reflet brillant, jamais de rendu 3D plastique. Jamais de bleu saturé, jamais de pièce grise de banque d'images. Réalisme photographique mat.

LA BOUCLE, exactement comme ça
A. Ouvre le zip, liste les fichiers, et affiche-moi la photo n° 1 de la liste ci-dessous.
B. Analyse-la en trois lignes : produit et coloris, ce qui doit être supprimé, ce qui doit rester identique.
C. Génère l'image n° 1 en utilisant cette photo comme référence stricte, au format indiqué (carré = 1024×1024, portrait 4:5 = 1024×1536 à recadrer), avec le plan indiqué.
D. Contrôle ton image contre la photo : silhouette identique ? couleur identique ? aucun texte, logo, badge, visage ? fond conforme ? au moins 40 % de vide ? Si un point échoue, regénère une fois, sinon passe.
E. Écris une ligne de journal : « n° / fichier source / produit, coloris / plan / nom de sortie / contrôle OK ».
F. Passe IMMÉDIATEMENT à la ligne suivante sans me poser de question. Si tu ne peux générer qu'une image par réponse, termine ta réponse après l'étape E et, dès que je réponds « suivant », reprends à la ligne suivante sans rien redemander. Ne t'arrête que quand la liste est finie ou quand le budget de 40 images est atteint.
G. Si tu ne peux pas utiliser une image extraite du zip comme référence, dis-le en une phrase et demande-moi de te l'envoyer directement ; ne génère jamais sans référence.

BUDGET : 40 images. Les 37 lignes ci-dessous d'abord, dans l'ordre. Les 3 dernières générations servent à refaire ce qui a échoué au contrôle. Tu ne fais pas de variantes gratuites.

NOMMAGE : le nom de sortie est donné à chaque ligne ; garde-le tel quel.

LISTE (fichier du zip → produit, coloris → plan, format → nettoyage → nom de sortie)
1. `09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg` → Neck 01, Cloud → sky packshot, 1:1 → `somnila_neck-01_sky-cloud_1x1_v3.jpg`
2. `09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg` → Neck 01, Night → sky packshot, 1:1 → cleanup: remove the small Chinese characters printed on the image. → `somnila_neck-01_sky-night_1x1_v3.jpg`
3. `09-oreiller-cervical/oreiller-cervical_bleu-clair_34_31.jpg` → Neck 01, Sky → sky packshot, 1:1 → `somnila_neck-01_sky-sky_1x1_v3.jpg`
4. `09-oreiller-cervical/oreiller-cervical_gris_34_21.jpg` → Neck 01, Stone → sky packshot, 1:1 → cleanup: remove the small Chinese characters printed on the image. → `somnila_neck-01_sky-stone_1x1_v3.jpg`
5. `09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg` → Neck 01, Cloud → dawn bedroom, 1:1 → `somnila_neck-01_dawn-bedroom-cloud_1x1_v3.jpg`
6. `09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg` → Neck 01, Night → dawn bedroom, 1:1 → cleanup: remove the small Chinese characters printed on the image. → `somnila_neck-01_dawn-bedroom-night_1x1_v3.jpg`
7. `09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg` → Neck 01, Cloud → fabric detail, 1:1 → `somnila_neck-01_detail-cloud_1x1_v3.jpg`
8. `12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg` → Contour 01, Night → sky packshot, 1:1 → `somnila_contour-01_sky-night_1x1_v3.jpg`
9. `12-oreiller-vague/oreiller-vague_blanc_34_08.jpg` → Contour 01, Cloud → sky packshot, 1:1 → cleanup: remove every award badge, medal, ribbon and text overlay ("Best Pillow", years, stars); keep only the pillow. → `somnila_contour-01_sky-cloud_1x1_v3.jpg`
10. `12-oreiller-vague/oreiller-vague_gris-blanc_34_11.jpg` → Contour 01, Stone → sky packshot, 1:1 → cleanup: remove every award badge, medal, ribbon and text overlay; keep only the pillow. → `somnila_contour-01_sky-stone_1x1_v3.jpg`
11. `12-oreiller-vague/oreiller-vague_bleu_34_22.jpg` → Contour 01, Blue → sky packshot, 1:1 → cleanup: remove every award badge, medal, ribbon and text overlay; keep only the pillow. → `somnila_contour-01_sky-blue_1x1_v3.jpg`
12. `12-oreiller-vague/oreiller-vague_rose-blanc_34_10.jpg` → Contour 01, Blush → sky packshot, 1:1 → cleanup: remove every award badge, medal, ribbon and text overlay; keep only the pillow. → `somnila_contour-01_sky-blush_1x1_v3.jpg`
13. `12-oreiller-vague/oreiller-vague_blanc_lifestyle_30.jpg` → Contour 01, Cloud → dawn bedroom, 1:1 → cleanup: remove the posters, the plush toy and every decorative object; plain calm bedroom. → `somnila_contour-01_dawn-bedroom-cloud_1x1_v3.jpg`
14. `10-oreiller-lateral/oreiller-lateral_bleu_34_01.jpg` → Side 01, Blue → sky packshot, 1:1 → cleanup: remove the dimension diagram, the measurement lines and every number and Chinese character; keep only the pillow. → `somnila_side-01_sky-blue_1x1_v3.jpg`
15. `10-oreiller-lateral/oreiller-lateral_gris-fonce_34_26.jpg` → Side 01, Dark Grey → sky packshot, 1:1 → cleanup: remove the dimension diagram, the measurement lines and every number and Chinese character; keep only the pillow. → `somnila_side-01_sky-dark-grey_1x1_v3.jpg`
16. `10-oreiller-lateral/oreiller-lateral_rouge_34_27.jpg` → Side 01, Red → sky packshot, 1:1 → cleanup: remove the dimension diagram, the measurement lines and every number and Chinese character; keep only the pillow. → `somnila_side-01_sky-red_1x1_v3.jpg`
17. `11-oreiller-corporel/oreiller-corporel_bleu-marine_dessus_49.jpg` → Body 01, Night → sky packshot, 1:1 → cleanup: remove the striped bedsheet; the S-shaped pillow is the only object. → `somnila_body-01_sky-night_1x1_v3.jpg`
18. `11-oreiller-corporel/oreiller-corporel_bleu-clair_dessus_07.jpg` → Body 01, Sky → sky packshot, 1:1 → cleanup: remove the striped bedsheet; the S-shaped pillow is the only object. → `somnila_body-01_sky-sky_1x1_v3.jpg`
19. `11-oreiller-corporel/oreiller-corporel_rose_dessus_24.jpg` → Body 01, Blush → sky packshot, 1:1 → cleanup: remove the striped bedsheet; the S-shaped pillow is the only object. → `somnila_body-01_sky-blush_1x1_v3.jpg`
20. `11-oreiller-corporel/oreiller-corporel_gris_dessus_18.jpg` → Body 01, Stone → sky packshot, 1:1 → cleanup: remove the striped bedsheet; the S-shaped pillow is the only object. → `somnila_body-01_sky-stone_1x1_v3.jpg`
21. `01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg` → Lounge 01, Stone and Sand → sky packshot, 1:1 → `somnila_lounge-01_sky-stone-and-sand_1x1_v3.jpg`
22. `01-oreiller-telephone/oreiller-telephone_bleu_34_25.jpg` → Lounge 01, Sky → sky packshot, 1:1 → cleanup: remove the words "MULTICOLOURED" and the Chinese characters. → `somnila_lounge-01_sky-sky_1x1_v3.jpg`
23. `01-oreiller-telephone/oreiller-telephone_gris + beige_34-duo_36.jpg` → Lounge 01, Stone and Sand → dawn bedroom, 1:1 → `somnila_lounge-01_dawn-bedroom-stone-and-sand_1x1_v3.jpg`
24. `02-couverture/couverture_blanc-creme_lit_40.jpeg` → Throw 01, Cream → dawn bedroom, 4:5 → cleanup: remove the person entirely, including hair, hands and clothing; keep the throw blanket draped on the bed and rebuild the bed and wall naturally where the person was. → `somnila_throw-01_dawn-bedroom-cream_4x5_v3.jpg`
25. `02-couverture/couverture_beige_lit_39.jpeg` → Throw 01, Sand → dawn bedroom, 4:5 → cleanup: remove the person entirely, including hair, hands and clothing; keep the throw blanket draped on the bed and rebuild the bed and wall naturally where the person was. → `somnila_throw-01_dawn-bedroom-sand_4x5_v3.jpg`
26. `02-couverture/couverture_vert-sauge_lit_48.jpeg` → Throw 01, Sage → dawn bedroom, 4:5 → cleanup: remove the person entirely, including hair, hands and clothing; keep the throw blanket draped on the bed and rebuild the bed and wall naturally where the person was. → `somnila_throw-01_dawn-bedroom-sage_4x5_v3.jpg`
27. `02-couverture/couverture_bleu-ardoise_lit_41.jpeg` → Throw 01, Slate → dawn bedroom, 4:5 → cleanup: remove the person entirely, including hair, hands and clothing; keep the throw blanket draped on the bed and rebuild the bed and wall naturally where the person was. → `somnila_throw-01_dawn-bedroom-slate_4x5_v3.jpg`
28. `02-couverture/couverture_bleu-clair_lit_42.jpeg` → Throw 01, Sky → dawn bedroom, 4:5 → cleanup: remove the person entirely, including hair, hands and clothing; keep the throw blanket draped on the bed and rebuild the bed and wall naturally where the person was. → `somnila_throw-01_dawn-bedroom-sky_4x5_v3.jpg`
29. `02-couverture/couverture_gris_lit_43.jpeg` → Throw 01, Stone → dawn bedroom, 4:5 → cleanup: remove the person entirely, including hair, hands and clothing; keep the throw blanket draped on the bed and rebuild the bed and wall naturally where the person was. → `somnila_throw-01_dawn-bedroom-stone_4x5_v3.jpg`
30. `03-masque/masque_noir_face_05.jpg` → Mask 01, Black → sky packshot, 1:1 → cleanup: remove the white display head or form behind the mask so the mask floats on its own; keep the mask shape, strap and colour. → `somnila_mask-01_sky-black_1x1_v3.jpg`
31. `03-masque/masque_blanc_face_04.jpg` → Mask 01, Cloud → sky packshot, 1:1 → cleanup: remove the white display head or form behind the mask so the mask floats on its own; keep the mask shape, strap and colour. → `somnila_mask-01_sky-cloud_1x1_v3.jpg`
32. `03-masque/masque_rose_face_03.jpg` → Mask 01, Blush → sky packshot, 1:1 → cleanup: remove the white display head or form behind the mask so the mask floats on its own; keep the mask shape, strap and colour. → `somnila_mask-01_sky-blush_1x1_v3.jpg`
33. `04-bouchons/bouchons_bleu_boite_17.jpg` → Quiet 01, Blue → sky packshot, 1:1 → cleanup: remove the third-party brand name, all Chinese text and all printed graphics on the case, leaving a plain matte case in the same colour; keep the two pairs of earplugs exactly as they are. → `somnila_quiet-01_sky-blue_1x1_v3.jpg`
34. `04-bouchons/bouchons_vert_boite_14.jpg` → Quiet 01, Green → sky packshot, 1:1 → cleanup: remove the third-party brand name, all Chinese text and all printed graphics on the case, leaving a plain matte case in the same colour; keep the two pairs of earplugs exactly as they are. → `somnila_quiet-01_sky-green_1x1_v3.jpg`
35. `09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg` → For Two (2 × Neck 01), Cloud → two copies side by side, 1:1 → `somnila_for-two_sky-cloud_1x1_v3.jpg`
36. `09-oreiller-cervical/oreiller-cervical_blanc_34_51.jpg` → Family Set (3 × Neck 01), Cloud → three copies in a shallow diagonal line, 1:1 → `somnila_family-set_sky-cloud_1x1_v3.jpg`
37. `12-oreiller-vague/oreiller-vague_bleu-marine_34_13.jpg` → Contour for Two (2 × Contour 01), Night → two copies side by side, 1:1 → `somnila_contour-for-two_sky-night_1x1_v3.jpg`

Commence maintenant par la ligne 1.
```

## Ce que j'ai volontairement laissé dehors

- Les formats 4:5 et 16:9 des packshots : dérivés du 1:1 par extension du dégradé.
- Les coloris secondaires (Body 01 bicolores, Lounge 01 Stone/Yellow/Black/Blush,
  Throw 01 Yellow/Salmon/Blush/Lime, Mask 01 Violet/Heather grey, Quiet 01
  Butter/Blush) : hors budget, ils gardent la photo fournisseur nettoyée.
- Toute image avec du texte : le texte est posé par le site, jamais par le modèle.
