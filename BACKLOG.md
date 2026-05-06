# BACKLOG

What we've discussed but haven't shipped. Sparse on purpose. Items move between states without ceremony.

- **Warm** — actively shaping current build, recently real, pulls on you
- **Quiet** — known and parked, will return
- **Composting** — was here, isn't pulling weight, may fade or break down into something else

Read it before each session. Update it after.

---

## Open questions for Alondra (these can re-sort everything below)

- Does the new site feel like *her*? What rings true, what feels off?
- Is "Methow Valley · Est. 2013" right, or did she start a different year?
- How do customers actually reach her — text, call, email? Which does she prefer?
- Are there 2–3 real customer testimonials we can quote (with their permission)?
- ~~What's the actual service area?~~ **Confirmed: Lost River to Carlton.** Address is 1212 Riverside Ave, Twisp (correct as displayed).
- Pricing: stay by-quote, or post starting prices for transparency?
- Photos: any of the 9 we picked she'd rather not use? Any clients who *don't* want their home shown publicly?
- Are TikTok and Pinterest links worth keeping, or can we drop dormant ones?
- Does she want a "Meet Alondra" personal section — her story, why she started, immigrant business owner in the valley?
- Bilingual version eventually? Probably no for customers (her base is English) but worth confirming.
- Logo — happy with current, or want a refresh someday?
- Anything from the old site she misses that we didn't carry over?

---

## Service-detail interview (for Alondra)

The services page reads vapid because the descriptions are mine, not hers. The fix is asking targeted questions — her answers become the new copy. Best done in one sitting, in Spanish if easier (Sam translates).

**Lead-in:** "I'm trying to make the services page sound like you, not like a template. Can I ask you a handful of questions? Some answers I'll use word-for-word — your words always sound better than mine."

### Cross-cutting (ask first — these inform everything)
- What's something you always do on every job that most cleaners skip?
- Walk me through what you bring with you — products, tools, anything specific.
- What's a recent job you were proud of? What made it good?
- Is there a customer you've cleaned for for years — what does that relationship look like?

### Per service (one or two each)
- **House Cleaning** — What's always on your list, no matter what? What does "tailored to the home" actually look like in practice?
- **Residential / recurring** — Why do people pick recurring vs one-time? What changes between visits when you've been somewhere a year?
- **Office & Commercial** — What kinds of businesses do you clean? After-hours or during the day? Any commercial work that's particularly satisfying?
- **Deep Cleaning** — What's in a deep clean that isn't in a regular one? How long does one usually take? When do people book it?
- **Move-In** — When you walk into an empty new home, what do you do first? What do people worry about, and how do you settle them?
- **Move-Out** — What's on your checklist that landlords or buyers actually look for? Has someone gotten their full deposit back because of you?
- **Post-Construction** — What's the hardest part? Drywall dust, paint, debris — which gets the most attention? A recent job worth telling a story about?

### Wrap-up (negative space — defines what she does well)
- What's something you DON'T do that customers sometimes ask for?
- If a customer is comparing you to another cleaner, what do you want them to know?
- What's a service you wish customers asked for more often?

After the interview: rewrite each service-row paragraph in her words. Keep them short (2–3 sentences each), specific, with a concrete detail per service that no template would write.

---

## Warm

- **Wire Formspree on the contact form.** Currently `action=REPLACE_WITH_FORMSPREE_ID`; falls back to mailto. Sign her up, paste the ID, deploy.
- **Real testimonial.** Replace the home-page pull-quote ("a Twisp homeowner") with a real one or remove the section.
- **Custom domain on Cloudflare Pages.** Repo is live; need to verify `alondrascleaning.com` and `www.` are pointing correctly and serving over HTTPS.
- **README at repo root.** Short handoff doc: what's here, how to edit, how to deploy. (Spanish version too if Alondra wants to ever look.)
- **`og:image` + `LocalBusiness` structured data.** When she shares the link in a text or on Instagram, the preview should look like the brand.

## Quiet

### Content
- More photos — current set is 9; ideal is 15–20 across services + about
- "Meet Alondra" section on About — her story (signal: confirm she wants this)
- Service-area visual map (sketched / stylized, not a Google embed)
- Replace placeholder quote with 2–3 rotating testimonials
- Pricing transparency block (only if she signals)
- Seasonal callouts ("Spring deep cleans" / "Holiday prep") — small modular section

### Visual / UX
- Image filenames are hash-prefixed (`acee2a-asset.webp`); rename to descriptive (`window-mountains.webp`) so the repo is browsable
- Mobile menu polish — current nav-toggle is functional but could feel more deliberate
- Custom 404 page that matches the brand
- Slight motion on hero photo (subtle parallax or fade-in)
- Print stylesheet for the contact page (people occasionally print to stick on a fridge)

### Integrations / infra
- Formspree (warm) → if Formspree caps annoy, consider Cloudflare Pages Functions + Resend
- Cloudflare Web Analytics (free, privacy-friendly) — measure what's working
- Google Business Profile claim/refresh + reviews surfacing on the site
- Pre-commit hook: image size cap (no >500KB webp accidents)
- Build command in Cloudflare set to `python3 build.py` (so editing on github.com directly still produces a correct deploy)

### Bilingual
- Translation system (i18n strings vs hardcoded prose) — only if signal
- `EN | ES` toggle in header
- Spanish version of the handoff/README for Alondra

### Distant
- Online booking / availability (only if her volume grows enough to want it)
- Customer self-serve cancel/reschedule (out-of-scope for a brochure site)
- Email newsletter (seasonal cleaning tips) — interesting, no signal yet
- Blog (cleaning tips, Methow seasonal) for SEO — post-launch consideration
- Branded printables (business cards, flyers, magnet) — out of repo scope

## Composting

- Bilingual toggle on day one — replaced by "wait for signal; her customers are English"
- Stock photos from CRM — replaced by self-hosted curated set (decision 2026-05-05)
- Brown + cyan CRM palette — replaced by cream/sage/clay editorial direction
- Verbatim CRM marketing copy — replaced by fresh editorial prose; voice may shift again when Alondra revises
- Online quote calculator — over-engineered for a phone-call business

---

## Recently moved

- *Self-host all firebase assets* — completed (warm → done, 2026-05-05)
- *Repo restructure: site to `public/`* — completed (warm → done)
- *Push to GitHub as `samheller/alondras-cleaning`* — completed
- *Editorial redesign (Fraunces, cream/sage/clay)* — completed (replaced v2 brown+cyan)
- *Curate 9 photos from gallery, skip toilets/dirty/befores* — completed
- *Text-first CTAs (sms: links throughout)* — completed (replaced quote-heavy form-first)

---

## Process notes

This is a brochure site, not a product. The backlog should stay short — items earn warmth by Alondra-signal or visitor-friction, not by interestingness.

When in doubt: simpler. Fewer pages, fewer fields, fewer choices. The site's job is to make texting her feel obvious.
