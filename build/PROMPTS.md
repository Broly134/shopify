# PROMPTS — Somnila

Prompts prêts à coller, en anglais (les modèles d'image répondent mieux en
anglais). Les consignes et notes sont en français. Chaque prompt embarque tout
le système de marque pour que le résultat reste cohérent avec le BRAND_BOOK.

Règle de conservation : une image générée est une **piste**, pas un livrable.
Le logo retenu est reconstruit en vecteur (SVG) à la géométrie près, puis
décliné (Night, Cloud, Dawn sur Night, favicons, lockups). Les images IA ne
vont jamais telles quelles sur le site, un packaging ou un dépôt de marque.

---

## 1. Logo — prompt principal pour ChatGPT (GPT Image)

Mode d'emploi : ouvrir ChatGPT, coller le bloc ci-dessous en entier, demander
4 variations par direction (A, B, C, D), une image par logo. Garder les
propositions où le mot se lit d'un coup et où le motif nuit tient à 16 px.
M'envoyer les 2 ou 3 préférées : je les redessine en vecteur.

```
You are a senior brand designer. Design the logo of SOMNILA, a new international
sleep brand (memory-foam pillows, sleep mask, earplugs, a lounge pillow, a throw
blanket), sold online, US market first, then Canada, UK, Europe, Australia.

BRAND SYSTEM (follow it exactly)
- Name: "somnila", always lowercase in the logo. Pronounced som-NEE-la. Roots:
  "somnus" (sleep) and a soft, feminine ending. Never add a tagline inside the logo.
- Positioning: night support as a design object. The hold of a designer chair, in
  a pillow. Accessible luxury: premium through restraint and light, never through
  gold, gloss or medical imagery.
- Promise: "Feel it tonight. Keep it for years."
- Values: Precision (every curve has an anatomical reason), Restraint (the pillow
  disappears into the bedroom, no gadgets), Durability (foam that holds, washable
  cover, 30-night trial).
- Archetype: the Creator, with the Protector as secondary. Faceless founder
  persona: "the quiet craftsman" — hands, a bedroom at dawn, a workshop.
- Enemy: the blue "orthopedic" pillow that screams "neck pain", the $15 foam block
  that goes flat in three months, the fake permanent "-50%".
- Taglines (not in the logo, for context only): "Sleep well." / "Support,
  redesigned." / "Held all night."
- Tone: simple English, calm, precise, warm. Never medical, never clinical, never
  hype.

VISUAL SYSTEM "night and dawn"
- Palette (use only these): Night #1E2A3A (main ink), Cloud #F7F9FC (background),
  Mist #DCE8F2 (soft surfaces), Dawn #F0B79B (one small warm accent, max 6% of
  the surface), Slate #6B7D90 (secondary text). Never pure black, never saturated
  blue, never hospital teal, never gold.
- Typography of the brand: Fraunces Soft (soft serif) for titles, Manrope for
  body text. For THIS logo, use a geometric extra-bold lowercase sans-serif with
  slightly rounded corners and tight spacing (in the spirit of Outfit, Plus
  Jakarta Sans, Gilroy). Friendly, solid, modern, direct-to-consumer.
- Shapes: soft, rounded (28–32 px radius feel), pill buttons, cloud-like
  softness, floating objects, generous negative space.
- Faceless brand: never a face, never a person, never an eye.

THE LOGO BRIEF
Make a bold lowercase wordmark "somnila" in which ONE letter quietly becomes a
night motif, so the logo says "night" and "sleep" at first glance while staying
a clean, readable word. Flat vector style, single colour Night on a Cloud
background, one optional Dawn accent. It must work at 16 px (favicon), embroidered
on a pillow cover, and printed one-colour on a kraft box.

Produce these four directions, one image per logo, centered, lots of white
space, no mockup, no shadow, no gradient, no 3D, no texture, no extra text, no
tagline, exact spelling "somnila":

A. THE MOON IS THE "o": the letter "o" is drawn as a crescent moon, thick on one
   side and thin on the other, still reading as an "o". Everything else stays a
   normal bold letter. Optional: the dot of the "i" in Dawn.
B. THE MOON ON THE "i": the wordmark stays intact; the dot of the "i" becomes a
   tiny crescent moon lying on its back (horns up), in Dawn. Subtle and elegant.
C. SYMBOL + WORDMARK: a small standalone symbol left of the word: a soft crescent
   moon lying on its back with rounded horns, like a moon that fell asleep. No
   stars. Night symbol, Night word, Cloud background.
D. THE FULL MOON "o": the "o" is a solid Dawn disc (the full moon), all other
   letters in Night. Minimal and warm.

Then show each direction in its dark version: Cloud letters on a Night
background, the Dawn accent unchanged.

Never: stars scattered around, "zzz", clouds, beds, eyes, faces, sleeping
figures, moon with a face, blue medical look, gradients, glow, bevel, drop
shadow, 3D, photo, mockup on a wall or a sign, uppercase, serif letters, any
letter other than the ones in "somnila".
```

### Variations rapides (à envoyer ensuite, une par message)

```
Direction A again, 4 variations: vary the thickness of the moon "o" (from a thin
sliver to a fat crescent) and its orientation (opening to the upper-right, to the
right, or lying on its back). Keep everything else identical.
```

```
Direction B again, 4 variations: the "i" dot as a tiny crescent, then as a tiny
full Dawn disc, then as a crescent slightly larger than the stem width, then
with the crescent in Night and no Dawn at all.
```

```
Direction C again, 4 variations of the symbol only, no text: a soft crescent
moon lying on its back, rounded horns, plump belly, tilted 15 to 25 degrees.
One version tighter, one plumper, one thinner, one wider. Flat Night on Cloud.
```

```
Take the version I mark as favourite and give me: (1) the symbol alone, (2) the
wordmark alone, (3) horizontal lockup, (4) stacked lockup, (5) a 1:1 app icon
with the symbol in Dawn on a Night square, (6) a one-colour Night version for
embroidery with no thin lines under 1.5 px at 40 mm wide.
```

### Ce que je fais ensuite

Tu m'envoies les 2 ou 3 images préférées. Je reconstruis le logo en vecteur
(SVG, arcs exacts), je le décline dans les trois couleurs autorisées, je génère
favicons, avatars et lockups, et je mets à jour le BRAND_BOOK. Aucune image
générée n'est utilisée telle quelle.

---

## 1 bis. Logo final — fusion des images 2 et 4 (prompt avec images)

Mode d'emploi : dans une nouvelle conversation ChatGPT, joindre les deux images
qu'il a produites (image 2 : le mot avec le o en croissant ; image 4 : le mot
avec le point du i en lune Dawn), puis coller le bloc ci-dessous. Il connaît
ainsi la marque même si la conversation est nouvelle.

```
I'm attaching two logo images you generated for my brand SOMNILA.
- Image 1: the wordmark "somnila" where the letter "o" is a crescent moon.
- Image 2: the wordmark "somnila" where the dot of the "i" is a small peach crescent moon.

BRAND CONTEXT (keep it exactly)
Somnila is an international sleep brand (memory-foam pillows, sleep mask,
earplugs, lounge pillow, throw blanket), US market first. Positioning: night
support as a design object, accessible luxury through restraint and light.
Promise: "Feel it tonight. Keep it for years." Values: precision, restraint,
durability. Faceless founder persona, "the quiet craftsman". Never medical,
never hype. Palette: Night #1E2A3A, Cloud #F7F9FC, Mist #DCE8F2, Dawn #F0B79B
(small warm accent), Slate #6B7D90. No pure black, no saturated blue, no gold.

TASK: merge the two images into ONE final logo.
- Keep the letterforms, weight and geometric style of Image 1: bold lowercase,
  single-storey "a", tight spacing. Make every letter slightly ROUNDER and
  softer than Image 1 (softly rounded corners on every stroke), never sharper.
- The "o" stays the crescent moon of Image 1: horns pointing to the upper
  right, plump belly at the lower left, fully readable as an "o" in the word.
  Colour it Dawn #F0B79B.
- The dot of the "i" becomes the small crescent moon of Image 2, lying on its
  back (horns up), also in Dawn #F0B79B, about 1.3 times the width of the "i"
  stem, floating just above the stem with a small gap.
- All other letters in Night #1E2A3A, background Cloud #F7F9FC.
- Exact spelling "somnila", lowercase. Nothing else: no tagline, no stars, no
  extra shapes, no outline, no shadow, no gradient, no glow, no 3D, no texture,
  no mockup, no frame.
- Flat vector look, centered, generous white space, aspect ratio 3:2, highest
  resolution available.

Then give me the same logo, one image each:
1. Dark version: Night #1E2A3A background, letters in Cloud #F7F9FC, both moons
   still Dawn #F0B79B.
2. One-colour version: everything Night on Cloud, moons included.
3. App icon: the crescent "o" alone, Dawn on a Night square, no text, 1:1.
4. The colour version on a transparent background, PNG, at least 3000 px wide.
```

Ce que j'en fais : je reconstruis la version retenue en vecteur (voir
`build/brand/logo/candidates/somnila-V1r-*.svg`, déjà prêts dans le même
esprit), puis lockups, favicons, avatars et BRAND_BOOK.

---

## 2. Visuels produit (Phase 5) — à compléter après validation du logo

Base de chaque prompt : « Place this exact product in: … » avec la photo
fournisseur en référence, aucun visage, lumière d'aube, palette ci-dessus,
40 % d'espace vide, une image mère validée par scène, 4 variantes max.
Les prompts détaillés arrivent en Phase 5.
