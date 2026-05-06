# VISION

Not a feature list. An attempt at understanding what Alondra is actually building, so the site can grow with it instead of against it.

**Don't be greedy.** Vision is where "wouldn't it be cool if…" creeps in. Sketch widely here if it helps you think, but moving anything from this document into BACKLOG warm requires real signal — Alondra says it, a customer surfaces it, a visitor visibly stumbles. Author-enthusiasm doesn't count. The site stays small on purpose.

Read it; argue with it; edit when reality moves.

---

## Who she is

Alondra is a Spanish-first immigrant business owner who has run a cleaning service in the Methow Valley for over a decade. She works in English with valley homeowners, second-home owners, and businesses. Her customer base today is almost entirely English-speaking. Her base of operations is **Winthrop**.

The business is small on purpose. It runs on word-of-mouth, a phone, and showing up. The site is not the product — the site is the thing that catches a recommended-by-a-neighbor visitor before they put their phone away.

## Who her customers are today

- **Methow homeowners** — primary residences in Twisp / Winthrop / Mazama / Carlton.
- **Second-home and vacation-rental owners** — a serious slice of the Methow economy. STR turnovers and seasonal deep-cleans are a real category.
- **Small businesses** — offices, the occasional commercial space.

Almost all English. Almost all word-of-mouth. The site catches the ones who Google after the recommendation.

---

## The arc

### Today: a Winthrop brochure

One owner, a small team, a tight valley, a phone-and-text business. The site is a 30-second trust read. Five pages, no backend, photos and a number. This is what we just shipped.

What the *today* version actually needs:
- Real photos (we have 9; 15–20 would carry it)
- Real testimonials (the placeholder one is fictional — see NOTICES)
- A face for the business — Alondra herself, her story
- Local SEO basics so "cleaner near me" Google results put her on the map
- A working contact form (Formspree) for the people who don't text

That's it. Everything else is downstream.

### Maybe: south to Wenatchee

Wenatchee is ~80 miles south, ~35k population, a real city by Methow standards. If Alondra expands there, three things shift at once:

1. **The market is bigger and more competitive.** Word-of-mouth alone gets thinner; the site has to do more lifting. Local SEO, reviews, structured data, possibly paid search — all become real instead of nice-to-have.
2. **Bilingual stops being theoretical.** Wenatchee is meaningfully Hispanic / Spanish-speaking (~30%+ of the population). A native-Spanish-speaking cleaning business owner in Wenatchee is *positioned* in a way she isn't in the Methow. An `EN | ES` site isn't a feature — it's table stakes for that market.
3. **Two service areas, one business** — or two? Probably one site with two service areas, separate phone numbers, separate Google Business profiles. Possibly distinct landing experiences (`/methow` and `/wenatchee`) sharing a brand. Worth not over-architecting until she signals real expansion.

This is the moment the site has to evolve from brochure to real local marketing surface.

### Eventually: a real small operation

If both regions land, the team is bigger, the schedule is harder, the customer list is real. At some point the site stops being the only digital surface — there's a scheduling tool, a CRM-of-sorts, an estimating workflow. Most of that is *not* the public site's job. The public site stays a trust object and a catcher for new leads.

The risk in growth: that the site becomes another generic-cleaning-business website. The protection against that is whatever makes today's site feel like *her* — the photos of her actual jobs in the actual valley, her voice, her face, her bilingual story.

---

## The bilingual question

Today: park it. Her customer base is English. Adding `EN | ES` on day one is over-engineering and dilutes voice.

If Wenatchee happens: revisit hard. The argument changes from "no signal" to "this is the differentiator." Likely shape:

- Header toggle, persisted in localStorage
- Translatable strings file (not prose welded into HTML)
- Spanish-language Google Business profile + structured data
- The About page in particular benefits — her bilingual immigrant-business story is the trust anchor for Spanish-speaking customers

Tracked in BACKLOG as quiet, with a note that Wenatchee expansion promotes it to warm.

## The "Meet Alondra" question

The single biggest trust-build a small-business site can do is show the owner. Today, the site has zero photo of Alondra and zero of her story.

There's a Spanish-first immigrant business owner serving an English-speaking valley for twelve years, possibly expanding to a city with a large Spanish-speaking population. That story is rare and good. The site should tell it. (Tracked in BACKLOG.)

The instinct to leave it off — "I'd rather just talk about the work" — is a real and respectable preference. But for someone deciding whether to text a stranger about cleaning their home, a face and a sentence does more than any service description.

---

## What's at risk in the move

The old CRM was likely claiming "SEO" as part of what she paid for — possibly real (managing her Google Business Profile, baseline schema), possibly theater. Either way, leaving exposes the business in two specific ways:

- **Twelve years of search equity tied to `alondrascleaningllc.com` is decaying right now.** That domain already returns DNS failure. Anyone Googling her old name lands on nothing.
- **Her Google Business Profile may be CRM-managed.** If so, ownership may need to be reclaimed.

Two moves matter most:

1. **Set up a 301 redirect from the old domain to the new one** — if she still controls the old domain's DNS. Single most leveraged action; the window may be closing.
2. **Claim Google Business Profile and point it at the new URL.** For a local trade business, this drives more search traffic than the website itself.

Everything else (schema markup, Search Console submission, citation audits, review surfacing) is real work that comes when signal warrants. Don't pile it on.

## What unlocks the next stage

Three foundations, in this order:

1. **Real photos** — owner's own jobs, with permission. 15–20 great ones future-proof the site for years.
2. **Real testimonials** — two or three quotes with names + town. Worth more than any visual polish.
3. **Local SEO defense** (above). The bridge from word-of-mouth to discoverability — the thing that has to be real before Wenatchee.

After those: the bilingual layer (when Wenatchee is real), and the second service area landing experience.

---

## How to use this document

- Read it before each working session.
- When Alondra mentions something — Wenatchee timing, a price change, a new town — find it here. It's probably already sketched, and the mention is signal.
- When something here turns out to be wrong, edit it. Vision is a living sketch.
- Items move into BACKLOG (warm) when signal warrants. They don't come back into VISION.
