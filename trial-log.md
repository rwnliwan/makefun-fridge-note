# Trial log — makefun-fridge-note

- Slug: `u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7`
- Bounty: Notes From a Passive-Aggressive Fridge — $2, free entry
- Deadline: 26 Nov 2026 05:25 WITA (2026-11-25T21:25:00Z); R1 cutoff 25 Nov 21:45 WITA
- Gate: `/output/entry.txt`, UTF-8, 1–200 characters, one line
- Kit: fresh tarball from the coordinator, extracted to `fridge/kit/`;
  `kit.json` bundle_sha256 `a84779ec16866edeb055942399a40a296ce9d7f2bedd11125e2e65800a917a7f`
  matches the live API payload (field `bundleSha256`).
  CLI verified present at
  `fridge/kit/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7-kit/cli/makefun.mjs`.

## Field research (live API, 25 Nov ~18:55 WITA)

- Live field: 973 submissions, 248 titles are the competition name itself
  (placeholder), leaving **725 real titles** as the denominator.
- Saturated clusters (real titles): yogurt 97, door openings 55,
  leftovers 59, ice maker 37, expired 46, milk 36, receipts/evidence 35,
  "filed a complaint" 25, rent/charging 20, 2 a.m. 18, "not a museum" 11,
  "I counted" 10, "I told X" (mother / smart scale / oven) 6.
- Fresh ground found at 0 hits: the fridge reviewing its owner
  (one-star review), annual/performance review, referee yellow card,
  free-trial expiry, lost-and-found, weather forecast, warranty.
  The winning shift is WHO judges WHOM, not a new food item.

## Candidates discarded (with reason)

1. Yogurt expired Tuesday + "I kept it cold anyway" — yogurt 97 hits,
   expired 46; the single most saturated object in the field.
2. Leftovers formed a union / filed a complaint — leftovers 59 hits,
   complaint family 25 hits; the joke's mechanism is already the field's
   house style.
3. Door log / receipts ("14 openings at 2 a.m., I counted") — door 55,
   receipts 35, "I counted" 10; counting openings is the default voice.
4. "I told your mother / I told the smart scale" — "told X" family 6 hits;
   the gossip-to-a-third-party turn is taken twice over.
5. Ice maker quit / filed a complaint — ice maker 37 hits, complaint 25;
   the appliance-complains angle is exhausted.
6. Butter on the top shelf since March, "I have named it" — near-verbatim
   an existing entry; unusable even though the object is small.
7. Kale in the crisper, "getting healthy" for 18 days — near-duplicate of
   an existing kale entry (same object, same number, same quote).
8. "Your leftovers now pay rent" / charging rent for the light — rent
   family 20 hits; the landlord voice is taken.
9. 2 a.m. ice cream / cake raid — 2 a.m. 18 hits, ice cream 10; the
   midnight slot is the most crowded time in the field.
10. "I am not a museum, eat the leftovers" — museum family 11 hits.
11. Free trial of opening me just to stare ends tonight — mechanism fresh
    (0 hits) but "stare" family 4 hits and the sting ("eat something") is
    weaker than the review's sting; kept as runner-up, not the entry.
12. Lost and found: one diet, answering to the kale in my crisper — fresh
    format (0 hits) but leans on the kale object that entry 7 already uses.
13. Annual review with 47 door openings — fresh format, but it drags the
    saturated door-count back in as its evidence; weaker than the review
    built on untouched inventory.

## Chosen entry (v1)

> One-star review: the ketchup expired in March, the jam has never been opened, and you keep buying more of both.

- Length: 111 characters (Python `len()`), one line, inside the 1–200 gate.
- Dup-check on the phrases: "one-star review" 0 hits, "ketchup" 1 hit
  (a slug-like title only, no shared mechanism), "jam" 0 hits,
  "never been opened" 0 hits, "keep buying more" 0 hits.
  "Expired in March" appears in 3 titles, all with different objects and
  mechanisms (water filter, pickle paying rent, butter named) — a date
  marker, not the joke.
- Why it should win: the fridge reverses the rating relationship (the
  appliance reviews the human), the inventory is the evidence, and the
  sting lands last — the owner is the one restocking the food nobody eats.
  No explanation of the joke anywhere in the line.

## Trials

### v1 — 25 Nov 2026 ~19:00 WITA

- `main.py` written with the file tool in this authoring session; entry
  string identical to the chosen line above.
- Preflight (token-free): `python3 main.py` run locally; check the output
  file next, then bundle + kit check.
- Result: pending — recorded here after the run.
