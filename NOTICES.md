# NOTICES

Outside-eye observations of the current site (the five generated pages in `public/`), parked here in case Alondra wants the input later. Not assigned work.

**Filter:** keep things only an outside vantage would catch — gaps Alondra is too close to see, or that need context she's working in but hasn't externalized. Drop things she'd obviously notice on her next walkthrough.

**Source of truth:** `public/*.html` as of commit `787e04b` (post-asset self-host).

---

## 2026-05-05 — first walkthrough of the new site

### Trust signals

- **Testimonial is fictional.** Home page pull-quote attributes a quote to "a Twisp homeowner" — there's no such customer. Three real options: (1) replace with a real quote (with permission), (2) remove the section entirely until we have one, (3) leave as placeholder but flag visibly. Leaving fictional copy in production reads worse than no testimonial at all if a real customer notices.
- **"Methow Valley · Est. 2013" is inferred.** Old site said "12+ years of experience" — we worked backward from 2025 to 2013. If she actually started 2012 or 2014, the brand mark is wrong. Worth a confirm before launch.
- **No photo of Alondra herself.** A small-business site without a face of the owner is asking the visitor to take more of a leap. Even a casual photo + first-name caption on About would shift the trust read meaningfully — particularly given the immigrant-business-owner story hasn't been told here yet.

### Photos

- **All gallery photos are interior shots of customers' homes.** We curated for "no toilets, no befores," but didn't ask whether any of the homeowners object to having their kitchen / fireplace / bedroom on a public website. For a small valley where neighbors recognize each other's interiors, this is worth confirming before launch — not after.
- **One photo is the visual anchor for the whole site.** The hero "window cleaning + autumn mountains" shot is doing 80% of the brand work. If that house's owner ever asks us to take it down, we lose the strongest piece. Worth having a plan B (commission a similar shot, or bank permission explicitly).
- **No photo on About or Contact.** Both pages use existing gallery shots, but neither shows *people*. A team photo or even a single candid of Alondra working would make those pages stop feeling like template stand-ins.

### Voice

- **Service descriptions are mine, not hers.** Sentences like "thoughtful, top-to-bottom cleans tailored to your home" are editorial-Sam, not how Alondra would describe her own work. They read polished, but they're not authentic to her voice. Worth her revising in her own words once she's seen the site — even if the changes are small, they'll feel more like her.
- **The bilingual reality is invisible on the site.** Alondra is Spanish-first; her customers are English-speaking. That's an authentic story (immigrant business owner serving an English-speaking valley) and the site says nothing about it. A short About paragraph naming this would deepen the brand without changing the language of the site.

### Functional

- **Contact form is mailto fallback only.** `<form action="REPLACE_WITH_FORMSPREE_ID">` — submissions only work if the visitor has a configured mail client, which on mobile increasingly they don't. The text-first CTAs cover most cases, but the form looks broken if anyone tries it before Formspree is wired.
- **No Google Business Profile alignment visible.** The site has hours, a phone, an address — they should match (and link from) her Google Business listing. If they drift, the visitor experience degrades silently.
- **WhatsApp link uses US number.** `wa.me/+15094495690` — most US cleaning customers won't have WhatsApp. Spanish-speaking referrals via family overseas might, which could matter for her network specifically. Worth confirming whether to keep or quietly drop.
- **No `og:image`.** When she shares the URL in a text or on Instagram, the preview will be a generic favicon and a clipped meta-description. For a "the world has changed, here's the new site" launch text, the preview is the thing.
- **No analytics.** Cloudflare Web Analytics is free, privacy-friendly, and one snippet — without it we won't know whether anyone's reading the About page, whether the Text Us button is what people click, etc.

### Repo / process

- **Image filenames are inscrutable.** Files like `acee2a-asset.webp` are fine for code but if Alondra ever clicks into the GitHub repo (or someone helping her does), they can't tell which file is which. A renaming pass to descriptive names (`window-mountains.webp`, `log-cabin-pendant.webp`) would make the repo self-documenting without changing anything user-visible.
- **No README.** Public repo with no README looks abandoned at a glance. Even a 5-line "What this is, how to edit, who to call" would help future helpers.
- **Process files are English.** CLAUDE.md, BACKLOG.md, NOTICES.md, VISION.md are all in English. If Alondra ever does want to read them, they're a wall of jargon. Not urgent — she shouldn't need to — but the moment she wants to, we'll wish a Spanish translation existed.

### Specific to the launch text

- The "the world has changed. alondrascleaning.com" framing implies *change*. The site says nothing about being new — no "we just refreshed our site" line, no thank-you-for-visiting-the-new-place note. Probably fine. Just noting it.

---

## How to use this file

- Append in the moment.
- Filter: would only an outside vantage catch this? If Alondra would obviously hit it on her next click-through, leave it out.
- This file lives in the repo. If/when Alondra wants the input, share by paste — don't push her to read a file in a folder.
