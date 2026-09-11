# Somnila — launch email kit

Customer-facing copy, in English. Sender name: **Somnila**. Reply-to: the
brand address once it exists (see HANDOFF). Founder voice in the first
person, "we" elsewhere. No exclamation marks, no emojis, no medical claims,
no fake urgency. Every number below is a real product fact (prices in EUR,
converted at checkout).

Where each email lives: **Shopify Email** for the welcome series, the
post-purchase note and the review request (Marketing → Automations);
**Settings → Notifications** for the transactional lines. Header image:
`build/images/site/email/somnila_email_header_1200x400.jpg`, footer:
`somnila_email_footer_1200x300.jpg`.

---

## 1. Welcome series (trigger: newsletter sign-up)

### W1 — immediately · "Notes from the workshop, first note"

Preview text: *What we make, and what we refused to make.*

> Hello,
>
> Thank you for signing up. This is the first note, and it is short.
>
> I kept waking up stiff. Not every morning, enough of them. The pillows I
> found were either the blue hospital kind, the overpriced kind, or the kind
> that goes flat in three months. So I built the one I was looking for.
>
> Somnila makes five memory-foam pillows, each shaped for one way of lying.
> Foam that holds its shape through the night. A cover you can unzip and
> wash, included with every pillow. And thirty nights to decide: if it isn't
> right, one email with your order number and we refund the pillow. Nothing
> to send back.
>
> What we refused to make: a permanent "−50 %", a countdown, a badge from an
> award that doesn't exist.
>
> Next note in a few days: how to choose between the five shapes.
>
> Sleep well.
>
> [See the five pillows] → /collections/memory-foam-pillows

### W2 — day 3 · "Which pillow is yours"

Preview text: *Five shapes, one job each. Here is how to pick.*

> Most people choose by the way they fall asleep.
>
> **On your back, sometimes on your side** — Neck 01. Two heights on one
> pillow, 13 cm on one side and 11 cm on the other. Start with the higher
> side; if your head tilts up, turn it over. 62 × 42 cm, cooling cover
> included. €69.90.
>
> **You like a softer, lower pillow** — Contour 01. A gentle wave, 10 cm
> high, that follows the neck and shoulders. 60 × 35 cm, cooling cover
> included. €59.90.
>
> **On your side, all night** — Side 01. A 10 cm profile that keeps the head
> level with the shoulders. Cover included. €54.90.
>
> **You want the whole body held** — Body 01. A 120 cm S-shaped pillow that
> sits between the knees, under the arm and along the back at the same time.
> Breathable cotton cover included. €69.90.
>
> **The hour before sleep** — Lounge 01. A raised back with a ledge for the
> book or the phone. €54.90.
>
> Shipping is free on every pillow, 6 to 10 days, tracked. Thirty nights to
> decide on all of them.
>
> [Choose your shape] → /collections/memory-foam-pillows

### W3 — day 7 · "How the thirty nights work"

Preview text: *Sleep on it at home. Then decide.*

> A pillow can't be judged in a shop. It can be judged in your bed, on your
> real nights, with your real mattress.
>
> So every Somnila pillow, and every set that contains one, comes with
> thirty nights, counted from the day of delivery.
>
> How it works:
> 1. Sleep on it. Give it a few nights; a new shape takes some getting used to.
> 2. If it isn't right, email us within the thirty nights with your order
>    number.
> 3. We refund the price of the pillow to your original payment method.
>    You do not need to send it back.
>
> One more thing worth knowing: the cover unzips and goes in the washing
> machine, cold, gentle cycle, dried flat. The foam itself takes a damp
> cloth, never the machine.
>
> [Start your thirty nights] → /products/neck-01

---

## 2. Abandoned checkout (Shopify automation, one email, 1 hour after)

Subject: *Your pillow is still in the cart*
Preview text: *Thirty nights to decide, shipping included.*

> You left something in your cart. No rush; it will be there.
>
> If it helps with the decision: shipping is free on every pillow and set,
> 6 to 10 days, tracked. And you have thirty nights from delivery to decide,
> refund by email, nothing to send back.
>
> [Back to your cart] → {{ checkout_url }}
>
> A question first? Reply to this email.

No second reminder, no discount in this email.

---

## 3. Transactional notifications (Settings → Notifications)

Keep Shopify's templates; change only these lines.

- **Order confirmation**, first paragraph: *Thank you. Your order is being
  prepared by our manufacturing partner and ships in 6 to 10 days. You will
  get the tracking number by email the day it leaves.*
- **Shipping confirmation**, first paragraph: *Your order is on its way.
  Track it with the link below. Your thirty nights start the day it is
  delivered.*
- **Refund notification** (trial refund): *Your refund is on its way to your
  original payment method. Depending on your bank it appears within 5 to 10
  business days. Thank you for trying it.*

---

## 4. Post-purchase note (Shopify Email automation, 12 days after delivery)

Subject: *How are the nights?*
Preview text: *A few things worth knowing about your pillow.*

> Your pillow has been home for about two weeks. A few things worth knowing.
>
> **If it feels too high or too low** (Neck 01): turn it over. The two sides
> are 13 cm and 11 cm.
>
> **The cover** unzips and goes in the washing machine, cold, gentle cycle.
> Dry it flat. A spare cover is €16.90, so one is on the pillow while the
> other is in the wash.
>
> **If it isn't right**, you still have time: reply to this email with your
> order number before the thirtieth night and we refund the pillow.
>
> Sleep well.

---

## 5. Review request (Shopify Email, 21 days after delivery, one send)

Subject: *Two questions about your pillow*
Preview text: *Honest answers help the next person choose.*

> Three weeks in, you know the pillow better than we can describe it.
>
> Would you write a few lines about it? Two questions are enough: how you
> sleep, and whether the shape fits. Honest answers, including the critical
> ones, help the next person choose the right shape.
>
> [Write a review] → product page link
>
> Nothing is offered in exchange for a review, so that every review stays
> real.

---

## 6. Optional welcome offer — your decision

Not written into any email above. If you want one: a code **WELCOME10**,
10 % on the first order, pillows and sets only, no end date shown, mentioned
once in W1. It costs about €7 per hero order. I create it only on your "ok".
