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
- What's the actual service area? We listed Twisp, Winthrop, Mazama, Carlton, Pateros, Methow — confirm.
- Pricing: stay by-quote, or post starting prices for transparency?
- Photos: any of the 9 we picked she'd rather not use? Any clients who *don't* want their home shown publicly?
- Are TikTok and Pinterest links worth keeping, or can we drop dormant ones?
- Does she want a "Meet Alondra" personal section — her story, why she started, immigrant business owner in the valley?
- Bilingual version eventually? Probably no for customers (her base is English) but worth confirming.
- Logo — happy with current, or want a refresh someday?
- Anything from the old site she misses that we didn't carry over?

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
