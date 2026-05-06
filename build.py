#!/usr/bin/env python3
"""Generate the static HTML pages.

Run: python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent

# --- her assets on her firebase ---
LOGO = "https://firebasestorage.googleapis.com/v0/b/interscopemediacrm.appspot.com/o/Clientes%2Fb03e5cfa-d159-422f-95df-f5fbe73e26fc%2Fb03e5cfa-d159-422f-95df-f5fbe73e26fc_normalLogo.webp?alt=media&token=9a50c1b2-0d53-4738-98d7-91836d65528a"
FAVICON = "https://firebasestorage.googleapis.com/v0/b/interscopemediacrm.appspot.com/o/Clientes%2Fb03e5cfa-d159-422f-95df-f5fbe73e26fc%2Fb03e5cfa-d159-422f-95df-f5fbe73e26fc_redesLogo.webp?alt=media&token=17749670-7d78-49a3-b620-79cc10e342fc"

# curated keepers from her gallery — clean, finished, Methow-feeling
def gphoto(name, token):
    return f"https://firebasestorage.googleapis.com/v0/b/interscopemediacrm.appspot.com/o/galleryClientes%2Fb03e5cfa-d159-422f-95df-f5fbe73e26fc%2FfotosCliente%2F{name}?alt=media&token={token}"

PHOTO_WINDOW_VIEW   = gphoto("0%20(20)-5369.webp", "8c18613b-d802-4f74-b95f-22282242a6af")  # exterior window cleaning + Methow mountains
PHOTO_SILL_VALLEY   = gphoto("0%20(21)-548.webp",  "7651bc23-f31b-40d9-9cc6-1415b4954cdc")  # window sill + valley view
PHOTO_FIREPLACE     = gphoto("0%20(22)-392.webp",  "61de97a1-c4f6-40b1-be92-b7991663feb2")  # river-rock fireplace
PHOTO_EXTERIOR      = gphoto("0%20(23)-607.webp",  "b4648395-d12f-4cb3-917d-2c72bea892df")  # exterior cabin
PHOTO_RAFTERS       = gphoto("0%20(24)-2443.webp", "19233d18-f1ed-474b-b065-57d63f7d0bdb")  # high ceiling rafters
PHOTO_MODERN_HOME   = gphoto("0%20(17)-9754.webp", "aaf931bf-929a-40b3-9866-1ad9110e5b53")  # modern open room
PHOTO_LOG_CABIN     = gphoto("0%20(18)-638.webp",  "b5a68c47-2650-40fa-bb8a-2a50a8826562")  # log cabin pendant
PHOTO_BEDROOM_VIEW  = gphoto("0%20(19)-5115.webp", "5f76010a-37ec-4799-85b5-b64b240b657a")  # bedroom + valley window
PHOTO_CEILING_FAN   = gphoto("0%20(16)-6023.webp", "4711f986-93fa-4833-a463-1a0c820a80f3")  # ceiling fan detail

GALLERY_PHOTOS = [
    PHOTO_WINDOW_VIEW, PHOTO_LOG_CABIN, PHOTO_MODERN_HOME, PHOTO_FIREPLACE,
    PHOTO_BEDROOM_VIEW, PHOTO_SILL_VALLEY, PHOTO_RAFTERS, PHOTO_EXTERIOR, PHOTO_CEILING_FAN,
]

SERVICES = [
    ("01", "House Cleaning",
     "Thoughtful, top-to-bottom cleans tailored to your home and your schedule.",
     PHOTO_LOG_CABIN),
    ("02", "Residential Care",
     "Recurring visits that keep your home consistently fresh — weekly, bi-weekly, or monthly.",
     PHOTO_MODERN_HOME),
    ("03", "Office & Commercial",
     "Sanitized, productive workspaces — scheduled around your business hours.",
     PHOTO_RAFTERS),
    ("04", "Deep Cleaning",
     "A full reset that reaches the corners regular cleans miss.",
     PHOTO_FIREPLACE),
    ("05", "Move-In · Move-Out",
     "Hand the keys back spotless or move into a place that already feels yours.",
     PHOTO_BEDROOM_VIEW),
    ("06", "Post-Construction",
     "Construction dust, debris, and residue cleared so a finished build feels truly finished.",
     PHOTO_EXTERIOR),
]

TOWNS = ["Twisp", "Winthrop", "Mazama", "Carlton", "Pateros", "Methow"]


# ---- partials ----
def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="icon" type="image/webp" href="{FAVICON}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>"""


def utility_bar():
    return f"""
<div class="utility">
  <div class="container">
    <div class="utility-info">
      <span><i class="fa-solid fa-location-dot"></i> Twisp, WA — serving the Methow Valley</span>
      <span><i class="fa-regular fa-clock"></i> Mon – Sun · 8 AM – 5 PM</span>
    </div>
    <div class="utility-social">
      <a href="https://wa.me/+15094495690" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
      <a href="https://www.tiktok.com/@alondras.cleaning1" target="_blank" rel="noopener" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a>
      <a href="https://www.pinterest.com/alondrascleaningllc/" target="_blank" rel="noopener" aria-label="Pinterest"><i class="fa-brands fa-pinterest"></i></a>
      <a href="https://g.page/r/CdIszSM9pV25EBM/review" target="_blank" rel="noopener" aria-label="Google reviews"><i class="fa-brands fa-google"></i></a>
    </div>
  </div>
</div>"""


def site_header(active):
    def cls(p): return ' class="active"' if p == active else ''
    return f"""
<header class="site-header">
  <div class="container">
    <div class="utility-fixed-left">
      <button class="nav-toggle" id="navToggle" aria-controls="primaryNav" aria-expanded="false">Menu</button>
    </div>
    <a class="brand" href="index.html" aria-label="Alondra's Cleaning Services LLC">
      <img src="{LOGO}" alt="Alondra's Cleaning Services LLC" />
      <span class="brand-mark">Methow Valley · Est. 2013</span>
    </a>
    <div class="utility-fixed-right">
      <a class="header-cta" href="tel:+15094495690"><span>Call</span> <span class="phone">509-449-5690</span></a>
    </div>
  </div>
</header>
<nav class="primary-nav" id="primaryNav">
  <div class="container">
    <a href="index.html"{cls('home')}>Home</a>
    <a href="about.html"{cls('about')}>About</a>
    <a href="services.html"{cls('services')}>Services</a>
    <a href="gallery.html"{cls('gallery')}>Gallery</a>
    <a href="contact.html"{cls('contact')}>Contact</a>
  </div>
</nav>"""


def page_hero(title, crumb, img):
    return f"""
<section class="page-hero" style="background-image: url('{img}');">
  <div class="container">
    <p class="crumb"><a href="index.html">Home</a> <span class="sep">/</span> {crumb}</p>
    <h1>{title}</h1>
  </div>
</section>"""


def cta_band():
    return """
<section class="cta-band">
  <div class="container">
    <p class="eyebrow" style="color:var(--tan);">Ready when you are</p>
    <h2>Let's get your space sparkling.</h2>
    <a class="phone-large" href="tel:+15094495690">509 · 449 · 5690</a>
    <p>Texting is the fastest way to reach us — most messages get a same-day reply.</p>
    <div style="display:flex; gap:0.85rem; justify-content:center; flex-wrap:wrap;">
      <a class="btn btn-light" href="sms:+15094495690"><i class="fa-solid fa-comment"></i> Text Us</a>
      <a class="btn" style="background:transparent; color:var(--cream); border-color:rgba(250,245,236,0.4);" href="tel:+15094495690"><i class="fa-solid fa-phone"></i> Call</a>
      <a class="btn" style="background:transparent; color:var(--cream); border-color:rgba(250,245,236,0.4);" href="contact.html"><i class="fa-regular fa-envelope"></i> Email</a>
    </div>
  </div>
</section>"""


def site_footer():
    return f"""
<footer class="site-footer">
  <div class="container footer-top">
    <div class="footer-brand">
      <img src="{LOGO}" alt="" />
      <p>Quiet, careful cleaning for the homes and businesses of the Methow Valley.</p>
      <div class="socials">
        <a href="https://wa.me/+15094495690" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
        <a href="https://www.tiktok.com/@alondras.cleaning1" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a>
        <a href="https://www.pinterest.com/alondrascleaningllc/" aria-label="Pinterest"><i class="fa-brands fa-pinterest"></i></a>
        <a href="https://g.page/r/CdIszSM9pV25EBM/review" aria-label="Google"><i class="fa-brands fa-google"></i></a>
      </div>
    </div>
    <div>
      <h4>Visit</h4>
      <ul>
        <li>1212 Riverside Ave</li>
        <li>Twisp, WA 98856</li>
        <li>&nbsp;</li>
        <li>Mon–Sun · 8 AM–5 PM</li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li><a href="tel:+15094495690">509-449-5690</a></li>
        <li><a href="mailto:alondrascleaningservicesllc@gmail.com">Email us</a></li>
      </ul>
    </div>
    <div>
      <h4>Site</h4>
      <ul>
        <li><a href="about.html">About</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="gallery.html">Gallery</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© <span id="yr"></span> Alondra's Cleaning Services LLC</span>
    <span>Methow Valley, Washington</span>
  </div>
</footer>
<a class="fab" href="https://wa.me/+15094495690" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
<script src="script.js"></script>
</body>
</html>"""


# ---- pages ----
def home():
    services_tiles = "\n".join(
        f'''      <a href="services.html" class="service-tile">
        <span class="num">{num}</span>
        <h3>{name}</h3>
        <p>{blurb}</p>
        <span class="more">Learn more</span>
      </a>'''
        for num, name, blurb, _ in SERVICES[:6]
    )
    towns = "".join(f'<div class="area-cell">{t}</div>' for t in TOWNS)

    return f"""{head("Alondra's Cleaning Services LLC — Methow Valley", "Quiet, careful residential and commercial cleaning across the Methow Valley. Twisp, Winthrop, Mazama, Carlton.")}
{utility_bar()}
{site_header('home')}

<section class="hero" style="background-image: url('{PHOTO_WINDOW_VIEW}');">
  <div class="container">
    <p class="eyebrow">Methow Valley, est. 2013</p>
    <h1>Honest, careful cleaning for the homes of the <em>valley</em>.</h1>
    <p>We've been quietly caring for homes and businesses across Twisp, Winthrop, and Mazama for more than a decade — one careful clean at a time.</p>
    <div class="hero-actions">
      <a class="btn btn-light" href="sms:+15094495690"><i class="fa-solid fa-comment"></i> Text 509-449-5690</a>
      <a class="btn" style="background:transparent; color:var(--cream); border-color:rgba(250,245,236,0.5);" href="tel:+15094495690"><i class="fa-solid fa-phone"></i> Call</a>
    </div>
  </div>
  <div class="hero-meta">— Alondra's Cleaning Services</div>
</section>

<!-- Signals -->
<section style="padding: 2rem 0;">
  <div class="container">
    <div class="signals">
      <div class="signal"><strong>12+</strong><span>Years in the Valley</span></div>
      <div class="signal"><strong>40 mi</strong><span>Service Radius</span></div>
      <div class="signal"><strong>Mon–Sun</strong><span>8 AM – 5 PM</span></div>
    </div>
  </div>
</section>

<!-- Story / about preview -->
<section>
  <div class="container split">
    <div>
      <p class="eyebrow sage">Our Story</p>
      <h2>A quiet team that's been here a while.</h2>
      <p>Alondra's started small in Twisp — one client, one careful clean. Twelve years on, we're still small on purpose. Our team is consistent, vetted, and treats every home the way we'd treat our own.</p>
      <p>We bring our own supplies and offer eco-friendly products on request. We work around your schedule. And we sweat the details — baseboards, ceiling fans, behind the appliances — because that's where careful work shows.</p>
      <a href="about.html" class="btn btn-outline">More about us</a>
    </div>
    <div class="split-img-frame"><img src="{PHOTO_LOG_CABIN}" alt="Cleaning the pendant light in a log cabin home" /></div>
  </div>
</section>

<!-- Services -->
<section class="paper">
  <div class="container">
    <div class="section-intro">
      <p class="eyebrow">What We Do</p>
      <h2>Six services, one careful approach.</h2>
      <p>From a single deep clean to ongoing care for a vacation rental, we work in homes and businesses of every shape across the valley.</p>
    </div>
    <div class="services-list">
{services_tiles}
    </div>
  </div>
</section>

<!-- Quote -->
<section>
  <div class="container quote">
    <p class="eyebrow sage">From a recent visit</p>
    <blockquote>They are thorough, kind, and treat the place like their own. Worth every penny — we have them back every other week.</blockquote>
    <cite>— a Twisp homeowner</cite>
  </div>
</section>

<!-- Service area -->
<section class="paper-dark">
  <div class="container">
    <div class="section-intro">
      <p class="eyebrow sage">Where We Work</p>
      <h2>The Methow, end to end.</h2>
      <p>We cover the valley within roughly 40 miles of Twisp.</p>
    </div>
    <div class="area-grid">{towns}</div>
  </div>
</section>

<!-- Featured photo / second story -->
<section>
  <div class="container split reverse">
    <div>
      <p class="eyebrow">The Way We Work</p>
      <h2>Detail-led, schedule-friendly, no fuss.</h2>
      <p>You shouldn't have to think about your cleaner. We arrive on time, work quietly, and leave the place in the kind of condition you'd photograph.</p>
      <ul class="checks">
        <li>Vetted, consistent team members</li>
        <li>Eco-friendly products available on request</li>
        <li>Flexible weekly, bi-weekly, monthly, or one-time</li>
        <li>Free, no-pressure estimates</li>
      </ul>
    </div>
    <div class="split-img-frame"><img src="{PHOTO_MODERN_HOME}" alt="A modern Methow Valley home being cleaned" /></div>
  </div>
</section>

{cta_band()}
{site_footer()}
"""


def about():
    return f"""{head("About — Alondra's Cleaning Services LLC", "Locally owned cleaning service rooted in the Methow Valley. Meet Alondra and the team.")}
{utility_bar()}
{site_header('about')}
{page_hero("About Us", "About", PHOTO_BEDROOM_VIEW)}

<section>
  <div class="container split">
    <div class="split-img-frame"><img src="{PHOTO_FIREPLACE}" alt="Cleaning a river-rock fireplace in a Methow home" /></div>
    <div>
      <p class="eyebrow">Who we are</p>
      <h2>A small Methow team that takes pride in careful work.</h2>
      <p>Alondra's Cleaning Services started with one simple idea: the Methow Valley deserves a cleaning crew that shows up on time, treats every home with respect, and pays attention to the parts most people miss.</p>
      <p>Twelve years and a few thousand cleans later, we're still small on purpose. Our team is local, consistent, and trained in the kind of careful work that earns trust.</p>
      <a href="contact.html" class="btn btn-outline">Get a Quote</a>
    </div>
  </div>
</section>

<section class="paper">
  <div class="container">
    <div class="section-intro">
      <p class="eyebrow sage">What We Believe</p>
      <h2>Three things we hold to.</h2>
    </div>
    <div class="split" style="grid-template-columns: repeat(3, 1fr); align-items: flex-start; gap: 3rem;">
      <div>
        <p class="eyebrow">Care</p>
        <h3>Treat every home like our own.</h3>
        <p>We're guests in your space. We work quietly, lock up properly, and leave things the way we'd want to find them.</p>
      </div>
      <div>
        <p class="eyebrow">Consistency</p>
        <h3>The same team, the same standards.</h3>
        <p>Vetted team members, regular routes, and a punch-list approach so nothing gets skipped between visits.</p>
      </div>
      <div>
        <p class="eyebrow">Local</p>
        <h3>The Methow is home.</h3>
        <p>Twisp, Winthrop, Mazama, Carlton — we know the valley because we live here. Same-day quotes, real phone calls.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container split reverse">
    <div>
      <p class="eyebrow sage">A few things included</p>
      <h2>What's on every clean.</h2>
      <p>The basics show up every visit. The deeper work happens on request — quoted up front, never a surprise.</p>
      <ul class="checks">
        <li>Dust, vacuum, and mop floors throughout</li>
        <li>Clean and sanitize kitchens and bathrooms</li>
        <li>Wipe high-touch surfaces, handles, and switches</li>
        <li>Tidy and refresh living spaces and bedrooms</li>
        <li>Empty trash and reset recycling</li>
      </ul>
    </div>
    <div class="split-img-frame"><img src="{PHOTO_RAFTERS}" alt="Cleaning a high-ceilinged interior" /></div>
  </div>
</section>

{cta_band()}
{site_footer()}
"""


def services_page():
    rows = "\n".join(
        f'''  <article class="service-row">
    <div class="service-row-img"><img src="{img}" alt="{name}" /></div>
    <div>
      <span class="num">— {num}</span>
      <h2 style="margin-top:0.4rem;">{name}</h2>
      <p>{blurb}</p>
      <a href="contact.html" class="btn btn-outline">Request a Quote</a>
    </div>
  </article>'''
        for num, name, blurb, img in SERVICES
    )
    return f"""{head("Services — Alondra's Cleaning Services LLC", "Residential, commercial, deep, move-in/out, and post-construction cleaning across the Methow Valley.")}
{utility_bar()}
{site_header('services')}
{page_hero("Services", "Services", PHOTO_MODERN_HOME)}

<section>
  <div class="container">
    <div class="section-intro">
      <p class="eyebrow">What we do</p>
      <h2>Six ways we help.</h2>
      <p>Pick one or pair a deep clean with ongoing care — we'll quote a plan that fits your home and your schedule.</p>
    </div>
{rows}
  </div>
</section>

{cta_band()}
{site_footer()}
"""


def gallery_page():
    items = ""
    for i, u in enumerate(GALLERY_PHOTOS, 1):
        items += f'      <figure class="g-{i}"><img src="{u}" alt="Recent project" loading="lazy" /></figure>\n'
    return f"""{head("Gallery — Alondra's Cleaning Services LLC", "A look at recent cleaning projects in the Methow Valley.")}
{utility_bar()}
{site_header('gallery')}
{page_hero("Gallery", "Gallery", PHOTO_LOG_CABIN)}

<section>
  <div class="container">
    <div class="section-intro">
      <p class="eyebrow">Recent work</p>
      <h2>A few homes from this season.</h2>
      <p>A small selection of recent visits across the valley. We add to this whenever a homeowner gives us the okay.</p>
    </div>
    <div class="gallery-grid">
{items}    </div>
  </div>
</section>

{cta_band()}
{site_footer()}
"""


def contact_page():
    return f"""{head("Contact — Alondra's Cleaning Services LLC", "Request a free cleaning estimate. Serving Twisp, WA and the Methow Valley.")}
{utility_bar()}
{site_header('contact')}
{page_hero("Get in touch", "Contact", PHOTO_SILL_VALLEY)}

<section>
  <div class="container">
    <div class="contact-grid">
      <aside class="contact-side">
        <p class="eyebrow">Say hi</p>
        <h2 style="font-size: clamp(1.8rem, 3vw, 2.4rem);">Texting is the fastest.</h2>
        <p>Most quote requests come in by text — it's the quickest way to reach Alondra. Calls and emails work too, and we reply the same day.</p>
        <div style="display:flex; gap:0.6rem; flex-wrap:wrap; margin: 1.5rem 0 0;">
          <a class="btn btn-ink" href="sms:+15094495690"><i class="fa-solid fa-comment"></i> Text Us</a>
          <a class="btn btn-outline" href="tel:+15094495690"><i class="fa-solid fa-phone"></i> Call</a>
        </div>
        <dl>
          <dt>Phone</dt>
          <dd><a href="tel:+15094495690">509-449-5690</a></dd>
          <dt>Email</dt>
          <dd><a href="mailto:alondrascleaningservicesllc@gmail.com">alondrascleaningservicesllc@gmail.com</a></dd>
          <dt>Visit</dt>
          <dd>1212 Riverside Ave<br>Twisp, WA 98856</dd>
          <dt>Hours</dt>
          <dd>Mon – Sun · 8 AM – 5 PM</dd>
          <dt>Service area</dt>
          <dd>The Methow Valley, within ~40 miles of Twisp.</dd>
        </dl>
      </aside>

      <form class="contact-form"
            action="https://formspree.io/f/REPLACE_WITH_FORMSPREE_ID"
            method="POST"
            onsubmit="return handleContactSubmit(event)">
        <input type="hidden" name="_subject" value="New cleaning quote request" />
        <div class="row">
          <div><label for="name">Name</label><input id="name" name="name" type="text" required /></div>
          <div><label for="phone">Phone</label><input id="phone" name="phone" type="tel" /></div>
        </div>
        <label for="email">Email</label>
        <input id="email" name="email" type="email" required />
        <div class="row">
          <div>
            <label for="service">Service</label>
            <select id="service" name="service">
              <option>House Cleaning</option>
              <option>Residential Care (recurring)</option>
              <option>Office &amp; Commercial</option>
              <option>Deep Cleaning</option>
              <option>Move-In or Move-Out</option>
              <option>Post-Construction</option>
              <option>Not sure yet</option>
            </select>
          </div>
          <div>
            <label for="frequency">Frequency</label>
            <select id="frequency" name="frequency">
              <option>One-time</option>
              <option>Weekly</option>
              <option>Bi-weekly</option>
              <option>Monthly</option>
            </select>
          </div>
        </div>
        <label for="message">A few details</label>
        <textarea id="message" name="message" placeholder="Square footage, bedrooms/baths, anything else worth knowing"></textarea>
        <button type="submit" class="btn btn-ink"><i class="fa-solid fa-arrow-right"></i> Send Note</button>
      </form>
    </div>
  </div>
</section>

<section style="padding:0;">
  <iframe
    title="Map of Twisp, WA"
    src="https://www.google.com/maps?q=Twisp,+WA+98856&output=embed"
    width="100%" height="380" style="border:0; display:block; filter: grayscale(0.3) contrast(0.95);" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>

{site_footer()}
"""


def main():
    pages = {
        'index.html': home(),
        'about.html': about(),
        'services.html': services_page(),
        'gallery.html': gallery_page(),
        'contact.html': contact_page(),
    }
    for name, content in pages.items():
        (ROOT / name).write_text(content)
        print(f"wrote {name}")


if __name__ == '__main__':
    main()
