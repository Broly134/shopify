# Prompts Flux.1 Kontext Pro — images produit Somnila

11 septembre 2026. Prompts en anglais (Kontext répond mieux en anglais), notes en
français. Tout est construit sur le `BRAND_BOOK.md` (système « nuit et aube ») et
sur les règles du brief : données réelles uniquement, zéro promesse médicale,
aucun visage, aucun texte parasite, un produit par image (sauf packs).

## 0. Ce qu'il faut savoir avant de coller quoi que ce soit

- **Kontext travaille image par image.** Il prend UNE photo de référence et UNE
  instruction, et rend UNE image. Il n'ouvre pas un zip. Le zip sert de réserve :
  tu glisses une photo, tu colles le prompt qui correspond, tu récupères le résultat,
  photo suivante. En API (BFL, fal, Replicate) on boucle sur le même principe ;
  la table de lot du § 6 est faite pour ça.
- **512 tokens maximum par prompt** (≈ 350 mots). Au-delà, Kontext tronque en silence.
  Chaque prompt ci-dessous = `BLOC DE STYLE` (≈ 110 mots) + `PLAN` (≈ 60 mots)
  + `NETTOYAGE` du fichier (≈ 20 mots). Ça tient. N'ajoute rien d'autre.
- **Prompt upsampling : OFF.** Cette option réécrit le prompt et invente des
  détails (coutures, passepoils, logos). On la laisse désactivée.
- **Kontext ne connaît pas les vraies dimensions.** On ne lui demande jamais de
  montrer « les deux hauteurs », « 13 cm », une coupe de la mousse ou un nouvel
  angle de vue : il inventerait. Il change le fond, la lumière, la scène, il
  nettoie ; il ne redessine pas le produit.
- **Réglages** : modèle *FLUX.1 Kontext [pro]* ; format de sortie selon le plan
  (1:1, 4:5, 16:9) ; **seed fixe par produit** (ex. Neck 01 = 101, Contour 01 = 102,
  Side 01 = 103, Body 01 = 104, Lounge 01 = 105, Throw 01 = 106, Mask 01 = 107,
  Quiet 01 = 108) pour que les coloris d'un même produit aient la même lumière ;
  2 à 4 tirages par photo, on en garde un ; PNG ou JPEG qualité 90–95, sRGB.
- **Une image générée est un livrable seulement si elle passe la checklist du § 7.**
  Sinon on regénère ou on garde la photo fournisseur nettoyée.

## 1. BLOC DE STYLE — à coller en tête de chaque prompt

```
Product photo edit for SOMNILA, a calm premium sleep brand. Keep the product in
the reference image exactly as it is: same shape, proportions, colour, fabric
texture, seams, zip and stitching, same angle. Do not add, remove or redraw any
part of the product. Do not add text, letters, numbers, logos, badges, labels,
stickers, tags or watermarks. No people, no faces, no hands, no animals.
Style: dawn light, low and diffuse, coming from one side only, slight haze,
soft shadows, no flash, no midday sun, no hard highlights. Palette: pale
blue-white #F7F9FC to misty blue #DCE8F2, a faint warm peach glow #F0B79B in one
corner, deep navy #1E2A3A only as the darkest tone. Never saturated blue, never
hospital teal, never grey stock-photo rooms. Airy, quiet, at least 40% empty
space, matte photographic realism, 85 mm lens look, no 3D-render gloss.
```

## 2. PLANS — un bloc par type d'image (à coller après le bloc de style)

### P1 · Packshot ciel 1:1 (image 1 de chaque fiche, cartes produit)

```
SHOT: Replace the entire background with a smooth vertical gradient, pale
blue-white #F7F9FC at the top fading to misty blue #DCE8F2 at the bottom, with a
soft out-of-focus warm peach glow #F0B79B in the lower right. Make the product
appear to float slightly above the ground with a soft, wide, faint contact shadow
directly below it. Product centred, filling about 75% of the width, seen from the
same three-quarter angle as the reference. Square format.
```

### P2 · Packshot ciel 4:5 (mobile, Meta, cartes hautes)

```
SHOT: Same treatment as a sky packshot: smooth vertical gradient background from
pale blue-white #F7F9FC at the top to misty blue #DCE8F2 at the bottom, soft warm
peach glow #F0B79B lower right, product floating with a soft contact shadow.
Portrait 4:5 format, product in the lower two-thirds, more empty sky above it,
product filling about 78% of the width.
```

### P3 · Chambre à l'aube, sans personne (images 2–3, accueil, pubs)

```
SHOT: Place this exact product on a neatly made bed with crisp white cotton
percale sheets and a pale linen duvet, seen from the foot of the bed, slightly
above. Early morning light from a window on the left lays a soft band of light
across the sheet. Wall in warm off-white, a light oak headboard, nothing else:
no décor, no plants, no frames, no books, no lamps, no posters, no toys. No
people. The product is the only object with colour. Calm, empty, quiet.
```

### P4 · Détail matière (image 4, B-roll)

```
SHOT: Close-up of the fabric of this exact product, 85 mm macro look, shallow
depth of field, the weave and texture of the cover clearly visible, the zip
edge in frame if the reference shows one, soft dawn light from one side, misty
blue-white background falling out of focus. Do not change the fabric pattern or
colour. Square format.
```

### P5 · Hero accueil 16:9 (2400 × 1000, le texte est posé par le site)

```
SHOT: Wide 16:9 frame. Place this exact product on the right third of the image,
floating over a smooth vertical gradient from pale blue-white #F7F9FC at the top
to misty blue #DCE8F2 at the bottom, with a soft warm peach glow #F0B79B behind
and below the product on the right. Leave the left two-thirds completely empty
and calm for a headline that will be added later. Soft contact shadow under the
product. No text of any kind in the image.
```

### P6 · Packs « deux » et « trois » (For Two, Contour for Two, Family Set)

```
SHOT: Show two identical copies of this exact product side by side, slightly
overlapping, the second one a little behind the first, both floating over a
smooth vertical gradient from pale blue-white #F7F9FC to misty blue #DCE8F2 with
a soft warm peach glow #F0B79B lower right, one shared soft contact shadow.
Same colour, same shape, same fabric on both. Square format.
```
(Pour Family Set : « three identical copies … in a shallow diagonal line ».)

### P7 · Nettoyage seul (quand la photo fournisseur reste, mais propre)

```
SHOT: Keep the background and composition of the reference. Only remove every
piece of text, every diagram, every dimension line, every badge, sticker or
inset thumbnail, and fill those areas naturally with the surrounding background.
Nothing else changes.
```

## 3. NETTOYAGE — une ligne par famille de photos (à coller en fin de prompt)

Le manifeste du zip (`build/images/manifest.csv`) liste les défauts. Voici la
ligne à ajouter selon le fichier :

| Fichiers du zip | Ligne NETTOYAGE à ajouter |
|---|---|
| `09-oreiller-cervical/*bleu-marine*`, `*gris*` | `CLEANUP: remove the small Chinese characters printed on the image.` |
| `10-oreiller-lateral/*` (bleu, gris-foncé ×2, rouge) | `CLEANUP: remove the dimension diagram, the measurement lines and every number and Chinese character; keep only the pillow.` |
| `01-oreiller-telephone/*bleu*` | `CLEANUP: remove the words "MULTICOLOURED" and the Chinese characters.` |
| `01-oreiller-telephone/*gris-blanc*`, `*jaune*`, `*noir*`, `*rose*` | `CLEANUP: remove all Chinese text, the dimension diagram and the small inset thumbnails showing people; keep only the pillow.` |
| `12-oreiller-vague/*_34_08`, `_34_22`, `_34_11`, `_34_12`, `_34_10` | `CLEANUP: remove every award badge, medal, ribbon and text overlay ("Best Pillow", years, stars); keep only the pillow.` |
| `12-oreiller-vague/*lifestyle*` | `CLEANUP: remove the posters, the plush toy and every decorative object; plain calm bedroom.` |
| `04-bouchons/*` | `CLEANUP: remove the third-party brand name, all Chinese text and all printed graphics on the case, leaving a plain matte case in the same colour; keep the two pairs of earplugs exactly as they are.` |
| `03-masque/*` | `CLEANUP: remove the white display head or form behind the mask so the mask floats on its own; keep the mask shape, strap and colour.` |
| `02-couverture/*` | `CLEANUP: remove the person entirely, including hair, hands and clothing; keep the throw blanket draped on the bed and rebuild the bed and wall naturally where the person was.` |
| `11-oreiller-corporel/*` | `CLEANUP: remove the striped bedsheet; the S-shaped pillow is the only object.` |
| photos déjà propres | rien |

## 4. LE PROMPT COMPLET, exemple prêt à coller (Neck 01 Night, image 1)

Photo : `09-oreiller-cervical/oreiller-cervical_bleu-marine_34_06.jpg`, format 1:1,
seed 101, upsampling off.

```
Product photo edit for SOMNILA, a calm premium sleep brand. Keep the product in
the reference image exactly as it is: same shape, proportions, colour, fabric
texture, seams, zip and stitching, same angle. Do not add, remove or redraw any
part of the product. Do not add text, letters, numbers, logos, badges, labels,
stickers, tags or watermarks. No people, no faces, no hands, no animals.
Style: dawn light, low and diffuse, coming from one side only, slight haze,
soft shadows, no flash, no midday sun, no hard highlights. Palette: pale
blue-white #F7F9FC to misty blue #DCE8F2, a faint warm peach glow #F0B79B in one
corner, deep navy #1E2A3A only as the darkest tone. Never saturated blue, never
hospital teal, never grey stock-photo rooms. Airy, quiet, at least 40% empty
space, matte photographic realism, 85 mm lens look, no 3D-render gloss.
SHOT: Replace the entire background with a smooth vertical gradient, pale
blue-white #F7F9FC at the top fading to misty blue #DCE8F2 at the bottom, with a
soft out-of-focus warm peach glow #F0B79B in the lower right. Make the product
appear to float slightly above the ground with a soft, wide, faint contact shadow
directly below it. Product centred, filling about 75% of the width, seen from the
same three-quarter angle as the reference. Square format.
CLEANUP: remove the small Chinese characters printed on the image.
```

## 5. Notes par produit (ce que Kontext doit savoir, et ce qu'il ne doit pas inventer)

| Produit (dossier du zip) | Coloris à produire (nom fournisseur → nom Somnila) | Plans | À ne jamais faire |
|---|---|---|---|
| **Neck 01** (`09-oreiller-cervical`) — 62 × 42 × 13/11 cm | blanc → Cloud, bleu-clair → Sky, bleu-marine → Night, gris → Stone | P1, P2 pour les 4 ; P3, P4, P5 sur Cloud et Night | montrer « deux hauteurs », une coupe, une règle |
| **Contour 01** (`12-oreiller-vague`) — 60 × 35 × 10 cm | blanc → Cloud, bleu → Blue, gris → Stone, rose → Blush, bleu-marine → Night | P1, P2 pour les 5 ; P3 sur Cloud (repartir du lifestyle blanc nettoyé) et Night | ajouter un liseré, changer la vague |
| **Side 01** (`10-oreiller-lateral`) — 60 cm, profil 10 cm | bleu → Blue, gris-foncé → Dark grey, rouge → Red ; **gris-clair et rose = variante 50 cm écartée, ne pas traiter** | P1, P2 pour les 3 ; P4 sur Blue | reproduire le schéma de cotes |
| **Body 01** (`11-oreiller-corporel`) — 120 cm, S | bleu-clair → Sky, rose → Blush, gris → Stone, bleu-marine → Night, rose-bleu → Blush and Sky, bleu-rose → Sky and Blush ; **bleu-très-clair `_53` = autre produit, ne pas traiter** ; Azure, Mint, Apricot n'ont pas de photo : ne pas générer un coloris sans photo | P1, P2 pour les 6 ; P3 sur Night | changer le S, raccourcir, ajouter un coloris |
| **Lounge 01** (`01-oreiller-telephone`) — 60 × 37 × 23 cm | bleu → Sky, gris + beige duo → Stone and Sand, gris-blanc → Stone, jaune → Yellow, noir → Black, rose → Blush | P1, P2 pour les 6 ; P3 sur Stone and Sand (le lit, un livre fermé sans titre lisible est autorisé) | poser un téléphone allumé, un écran |
| **Throw 01** (`02-couverture`) — 200 × 230 cm | beige → Sand, blanc-crème → Cream, bleu-ardoise → Slate, bleu-clair → Sky, gris → Stone, jaune → Yellow, orange-saumon → Salmon, rose → Blush, vert-anis → Lime, vert-sauge → Sage | P3 (nettoyage « personne » puis chambre à l'aube) pour les 10 ; P4 sur Cream et Sage | garder la personne, inventer une frange |
| **Mask 01** (`03-masque`) — 57 × 8,5 cm | noir → Black, blanc → Cloud, rose → Blush, violet-blanc → Violet, gris-chiné → Heather grey ; **`_09` basse définition, ne pas traiter** ; Light grey et Night sans photo : ne pas générer | P1, P2 pour les 5 ; P4 sur Black | remplacer la forme par un visage |
| **Quiet 01** (`04-bouchons`) — 2 paires + étui | bleu → Blue, vert → Green, jaune-lait → Butter, rose → Blush | P1 pour les 4 (nettoyage marque tierce obligatoire) | écrire « somnila » sur l'étui |
| **Housses** (Cover — Neck / Contour / Side / Body) | reprendre l'image P1 de l'oreiller correspondant | — | une housse « vide » inventée |
| **Packs** For Two, Contour for Two, Family Set | à partir du P1 du coloris | P6 | mélanger deux coloris qui n'existent pas ensemble |
| **Packs** Sleep Set, Quiet Night, Evening Set, Side-Sleeper Set, Neck 01 + Cover | composition faite par moi à partir des P1 (deux références, Kontext n'en prend qu'une) | — | — |

## 6. Table de lot (fichier du zip → prompt → nom de sortie)

Le fichier `build/images/kontext-batch.csv` liste chaque photo utilisable avec le
plan, la ligne de nettoyage, le format, la seed et le nom de sortie attendu.
Convention de nommage : `somnila_<handle>_<plan>-<coloris>_<ratio>_v3.jpg` ; `v3`
= édité par Kontext (v1 = fournisseur brut, v2 = nettoyé à la main).
Résultats à déposer dans `build/images/generated/<handle>/` ; je m'occupe ensuite
du recadrage, de la compression et de l'envoi dans les galeries Shopify.

## 7. Checklist d'acceptation — un non, on regénère

1. Le produit est **identique** à la photo fournisseur : silhouette, proportions,
   coutures, zip, couleur (poser les deux côte à côte ; en cas de doute, superposer).
2. Aucun texte, chiffre, logo, badge, étiquette ; aucun visage, main, animal.
3. Un seul produit (sauf P6), rien d'autre dans le cadre que le lit et le mur en P3.
4. Lumière d'un seul côté, douce ; pas d'ombre dure, pas de reflet brillant.
5. Fond : dégradé Cloud → Mist, halo Dawn discret ; jamais de bleu saturé, jamais
   de pièce grise.
6. Trame du tissu visible ; pas d'aspect rendu 3D ou plastique.
7. Au moins 40 % de vide ; produit ni coupé ni collé aux bords.
8. Bon format (1:1 / 4:5 / 16:9) et taille ≥ 1200 px de côté.
9. Le coloris existe dans le devis fournisseur (jamais de coloris inventé).

## 8. Si tu utilises l'API plutôt que le playground

Même prompt, même seed, `prompt_upsampling: false`, `aspect_ratio` selon le plan,
`output_format: "png"`, `safety_tolerance` par défaut. Une requête par ligne du
CSV ; garder le `seed` de la ligne. Kontext [pro] accepte une image de
référence ; pour les packs à deux références, m'envoyer les P1 et je compose.
