# Somnila — launch plan

Day 0 is the day the store password comes off. Everything before it is
preparation; nothing is announced before the site is complete. Budget rule
from the brief: native Shopify first, no paid app without your approval.

---

## 1. Before day 0 — the checklist (you, unless marked "me")

**Store**
- [ ] Shopify Payments activated (and PayPal); test order with a real card,
      then refunded.
- [ ] Domain `somnila.com` connected; `liyan.shop` redirected.
- [ ] Store name "Somnila" (done), sender email, and the legal address in
      Settings → General.
- [ ] Policies pasted from `build/pages/policies/`, bracketed fields
      filled (refund, shipping, terms, privacy).
- [ ] Checkout branding: logo, Cloud background, Night text and buttons.
- [ ] Default language English (Settings → Languages), then I remove the
      leftover French locale — me, on your "ok".
- [ ] Primary market: United States (Settings → Markets).
- [ ] Theme "Somnila — build v1" published — me, on your "ok".
- [ ] Password removed — you, day 0.

**Tracking (free, native)**
- [ ] Meta pixel and Conversions API through the Facebook & Instagram
      channel app; TikTok pixel through the TikTok app; Google & YouTube
      channel for Shopping and GA4.
- [ ] Google Search Console verified; sitemap `somnila.com/sitemap.xml`
      submitted.
- [ ] UTM scheme for every link you post: `utm_source` (meta, tiktok,
      google, email, pinterest), `utm_medium` (paid, organic, email),
      `utm_campaign` (launch).

**Content**
- [ ] Email automations created from `EMAILS.md` (Shopify Email): welcome
      series, abandoned checkout, post-purchase, review request.
- [ ] Notification templates edited (three lines in `EMAILS.md` § 3).
- [ ] Social profiles created with the avatar and cover; bios from
      `SOCIAL.md`; first three posts scheduled.
- [ ] Ad accounts created; campaigns built from `ADS.md` but paused.
- [ ] Blog "Notes from the workshop": three draft articles to read and
      publish (me: drafted; you: publish).

**Supplier**
- [ ] Confirm with the supplier: neutral packaging for Quiet 01, foam
      composition and density, Side 01 weight and exact dimensions, how
      tracking numbers reach you.
- [ ] Agree the trial refund process: no return, so no reverse logistics.

---

## 2. The timeline

| Day | What happens |
|---|---|
| −14 to −8 | Checklist above. Test orders. Read the three blog drafts. |
| −7 | Password stays on. Send the site link to ten people you trust; ask for one thing they didn't understand. Fix. |
| −3 | Publish theme (me), remove password (you), verify pixels fire on a test purchase. Submit sitemap. |
| 0 | Announce on your own channels: post 1, story, the welcome note to anyone already signed up. Ads on, Meta cold campaign only, small. |
| +1 to +7 | Post 2, 3, 4. Watch cost per order daily; pause creatives at €300 without an order. Answer every message. |
| +7 | First read of the numbers (see § 3). Turn on retargeting. Post 5, 6, 7. |
| +14 | Second read. Kill or scale ad sets. Start TikTok if Meta cost per order is under €39. Post 8, 9, 10. |
| +21 | Review requests start going out automatically. Post 11, 12. |
| +30 | Month-one report: orders, cost per order, trial refunds, best shape, best colour. Decide the second month's budget. |

---

## 3. What to watch, and the decision rules

Shopify Analytics is enough for month one. Numbers to write down every
Monday:

- **Sessions → orders (conversion rate).** Under 1 % after 1,000 sessions:
  the page, not the ad, is the problem. Check speed, the first image, the
  price, the trial line.
- **Average order value.** Neck 01 alone is €69.90; sets pull it up. If it
  stays under €75, push concept D (sets) in retargeting.
- **Cost per order, per ad set.** Break-even on Neck 01 is about €39 (see
  `build/PRIX.md`). Keep what is under, pause what is over after 10 orders.
- **Trial refunds.** The pricing assumes 5 %. Above 10 % over 50 orders,
  read the emails: it is usually one shape or one height. Fix the product
  page copy before spending more.
- **Support volume.** One question asked three times becomes an FAQ entry
  (me, in a day).

Do not read anything before 30 orders; the numbers lie in small samples.

---

## 4. Customer service, five replies

Reply within one business day, from the brand address, in the same voice.

1. **Where is my order?** *It ships in 6 to 10 days from the order, tracked.
   Your tracking link is in the shipping email; if it hasn't arrived after
   10 days, reply here with your order number and we chase it.*
2. **Trial refund.** *Thank you for trying it. I've refunded the pillow to
   your original payment method; it appears within 5 to 10 business days.
   No need to send it back.*
3. **Wrong height.** *Neck 01 has both heights, 13 cm and 11 cm: turn it
   over. If neither feels right, the thirty nights still apply.*
4. **Washing.** *Cover: cold, gentle cycle, dried flat. Foam: a damp cloth,
   never the machine.*
5. **Customs charge.** *Duties are calculated at checkout where possible.
   If a carrier asked you to pay on delivery, send us the receipt and your
   order number and we refund it.*

---

## 5. What is deliberately not in this plan

- No launch discount (your decision, see `EMAILS.md` § 6).
- No influencer seeding before month two: the product should earn its
  first reviews from paying customers.
- No paid apps: reviews through Shopify's free Product Reviews or Judge.me
  free plan once ten real reviews exist; no countdown, no pop-up, no
  upsell app beyond the theme's own blocks.
