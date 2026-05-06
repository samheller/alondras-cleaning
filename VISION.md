# VISION

A more sophisticated alondrascleaning.com — a place that earns trust before the first text.

This isn't a spec. It's a sketch of what the site could become, organized so items can earn their way into BACKLOG when signal warrants. Read it; argue with it; move things into warm.

---

## Frame

The current build treats the site as a **brochure** — five pages, one phone number, done. The vision treats it as a **trust object** for a small valley business: a thing that does the convincing so Alondra doesn't have to.

The site's job is one moment: a Mazama homeowner gets recommended Alondra by a neighbor, types the URL into their phone, scrolls for thirty seconds, and texts. The whole experience should make that thirty seconds feel like meeting a careful, local person.

It is not:
- A booking platform (humans book by text)
- A SaaS app (no logged-in surface)
- A CMS (Alondra doesn't edit; someone she trusts does)

It is:
- A 30-second trust read for a recommended-by-a-friend visitor
- A Spanish-speaking owner's English storefront
- A repo Alondra never opens — kept maintainable by whoever does

---

## Possible surfaces (signal-pending)

### Customer-facing
- **Meet Alondra** — short personal section, her story (immigrant business owner, twelve years in the valley, what she cares about). The single biggest trust-build a small-business site can do.
- **Real testimonials** — 3–5 rotating, with first names and town. Bigger than any tagline.
- **Service-area illustration** — stylized valley map showing Twisp, Winthrop, Mazama, Carlton, Pateros. Localness made visible.
- **Before-on-request** — most customers don't want to see toilet befores. Offer "see the gross stuff" as an opt-in section for the curious / move-out crowd.
- **Seasonal callouts** — Spring deep cleans, holiday prep, vacation-rental turnover. Small modular section that swaps with the calendar.
- **Vacation rental / Airbnb specialty** — the Methow has a serious short-term-rental economy. A page or block speaking directly to STR hosts could be a real lead source.
- **Bilingual mode** — `EN | ES` toggle. Today: probably unused. If she gets Spanish-speaking customers in the valley, an instant differentiator.
- **A "what's included" checklist** — sets expectations, kills "but does she also do…" anxiety.
- **Soft inquiry capture** — "not ready to book? get a Methow cleaning tip in your inbox" type opt-in. Only if there's content to send.

### Owner-facing
- **A simple edit doc** (Notion or Google Doc, in Spanish) — "to change the hours, change this; to swap a photo, send it to Sam" — so Alondra can drive content without touching code.
- **Decap CMS or similar** — git-backed, browser-editable. Maybe later. Almost certainly overkill for a 5-page site.
- **Quarterly review checklist** — "are these photos still right? is this still your service area?" — keeps the site from going stale silently.

### Distribution
- **Google Business Profile claim/refresh** — single biggest local-SEO move.
- **`LocalBusiness` schema.org** — invisible but meaningful for "cleaner near me" search.
- **Cloudflare Web Analytics** — privacy-friendly, free, just enough to see what works.
- **Instagram embed or feed link** — only if she posts there.
- **Referral mechanism** — "tell a friend, get a discount on your next clean." Informal in real life; probably stays informal.

### System
- **Build on Cloudflare** — switch from "commit HTML" to `python3 build.py` so github.com web edits produce correct deploys.
- **Pre-commit image size cap** — keep gallery loads fast as photos accrue.
- **Sanitize commit history** if asset URLs ever contained anything sensitive.

---

## What unlocks growth

Most of the surfaces above depend on three foundations being real:

1. **Real photos.** Curated 9 today. 15–20 great ones (interiors + exteriors + valley context) would carry the site for years.
2. **Real testimonials.** Two or three quotes from Twisp / Winthrop / Mazama homeowners are worth more than any visual polish.
3. **Local SEO basics.** Google Business profile + structured data + review surfacing. Most of her customers come from word of mouth; the site catches the ones who Google after the recommendation.

Once those exist, almost everything else above is a small addition.

---

## How to use this document

- Read it before each working session.
- When Alondra mentions something, find it here — it's probably already sketched, and now has signal.
- When something here turns out to be wrong, edit it. This is a living sketch.
- Items move into BACKLOG (warm) when signal warrants. They don't come back into VISION — vision is upstream.

The vision will outgrow itself. That's fine. When it does, the parts that matter will already be in BACKLOG.
