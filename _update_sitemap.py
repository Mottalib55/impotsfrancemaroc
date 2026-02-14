#!/usr/bin/env python3
"""Regenerate sitemap.xml with all pages including native language pages.
Adds hreflang alternates for native pages and updates lastmod dates."""
import os, re
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
TODAY = date.today().isoformat()  # 2026-02-14

# Native pages mapping: lang_code -> [(native_url, fr_url, en_url), ...]
NATIVE_PAGES = [
    ("de", "/de/deutschland/einkommensteuer/", "/fr/allemagne/simulateur-impot/", "/en/germany/income-tax/"),
    ("de", "/de/oesterreich/einkommensteuer/", "/fr/autriche/simulateur-impot/", "/en/austria/income-tax/"),
    ("de", "/de/schweiz/einkommensteuer/", "/fr/suisse/simulateur-impot/", "/en/switzerland/income-tax/"),
    ("es", "/es/espana/simulador-impuestos/", "/fr/espagne/simulateur-impot/", "/en/spain/income-tax/"),
    ("es", "/es/mexico/simulador-impuestos/", "/fr/mexique/simulateur-impot/", "/en/mexico/income-tax/"),
    ("es", "/es/argentina/simulador-impuestos/", "/fr/argentine/simulateur-impot/", "/en/argentina/income-tax/"),
    ("es", "/es/chile/simulador-impuestos/", "/fr/chili/simulateur-impot/", "/en/chile/income-tax/"),
    ("es", "/es/colombia/simulador-impuestos/", "/fr/colombie/simulateur-impot/", "/en/colombia/income-tax/"),
    ("es", "/es/peru/simulador-impuestos/", "/fr/perou/simulateur-impot/", "/en/peru/income-tax/"),
    ("pt", "/pt/portugal/simulador-impostos/", "/fr/portugal/simulateur-impot/", "/en/portugal/income-tax/"),
    ("pt", "/pt/brasil/simulador-impostos/", "/fr/bresil/simulateur-impot/", "/en/brazil/income-tax/"),
    ("nl", "/nl/nederland/belasting-berekenen/", "/fr/pays-bas/simulateur-impot/", "/en/netherlands/income-tax/"),
    ("nl", "/nl/belgie/belasting-berekenen/", "/fr/belgique/simulateur-impot/", "/en/belgium/income-tax/"),
    ("ar", "/ar/arabie-saoudite/tax-calculator/", "/fr/arabie-saoudite/simulateur-impot/", "/en/saudi-arabia/income-tax/"),
    ("ar", "/ar/dubai/tax-calculator/", "/fr/dubai/simulateur-impot/", "/en/dubai/income-tax/"),
    ("ar", "/ar/qatar/tax-calculator/", "/fr/qatar/simulateur-impot/", "/en/qatar/income-tax/"),
    ("ar", "/ar/koweit/tax-calculator/", "/fr/koweit/simulateur-impot/", "/en/kuwait/income-tax/"),
    ("ar", "/ar/egypte/tax-calculator/", "/fr/egypte/simulateur-impot/", "/en/egypt/income-tax/"),
    ("it", "/it/italia/calcolatore-imposte/", "/fr/italie/simulateur-impot/", "/en/italy/income-tax/"),
    ("sv", "/sv/sverige/skatteberaknare/", "/fr/suede/simulateur-impot/", "/en/sweden/income-tax/"),
    ("no", "/no/norge/skattekalkulator/", "/fr/norvege/simulateur-impot/", "/en/norway/income-tax/"),
    ("da", "/da/danmark/skatteberegner/", "/fr/danemark/simulateur-impot/", "/en/denmark/income-tax/"),
    ("fi", "/fi/suomi/verolaskuri/", "/fr/finlande/simulateur-impot/", "/en/finland/income-tax/"),
    ("el", "/el/ellada/ypologismos-forou/", "/fr/grece/simulateur-impot/", "/en/greece/income-tax/"),
    ("pl", "/pl/polska/kalkulator-podatkowy/", "/fr/pologne/simulateur-impot/", "/en/poland/income-tax/"),
    ("cs", "/cs/cesko/danovy-kalkulator/", "/fr/tchequie/simulateur-impot/", "/en/czech-republic/income-tax/"),
    ("hu", "/hu/magyarorszag/ado-kalkulator/", "/fr/hongrie/simulateur-impot/", "/en/hungary/income-tax/"),
    ("ro", "/ro/romania/calculator-impozit/", "/fr/roumanie/simulateur-impot/", "/en/romania/income-tax/"),
    ("hr", "/hr/hrvatska/porezni-kalkulator/", "/fr/croatie/simulateur-impot/", "/en/croatia/income-tax/"),
    ("tr", "/tr/turkiye/vergi-hesaplama/", "/fr/turquie/simulateur-impot/", "/en/turkey/income-tax/"),
    ("ja", "/ja/nihon/zeikin-keisan/", "/fr/japon/simulateur-impot/", "/en/japan/income-tax/"),
    ("ko", "/ko/hanguk/segeum-gyesan/", "/fr/coree-du-sud/simulateur-impot/", "/en/south-korea/income-tax/"),
    ("zh", "/zh/zhongguo/shuishou-jisuan/", "/fr/chine/simulateur-impot/", "/en/china/income-tax/"),
    ("th", "/th/prathet-thai/khamnuan-phasi/", "/fr/thailande/simulateur-impot/", "/en/thailand/income-tax/"),
    ("ms", "/ms/malaysia/kalkulator-cukai/", "/fr/malaisie/simulateur-impot/", "/en/malaysia/income-tax/"),
    ("id", "/id/indonesia/kalkulator-pajak/", "/fr/indonesie/simulateur-impot/", "/en/indonesia/income-tax/"),
    ("vi", "/vi/viet-nam/tinh-thue/", "/fr/vietnam/simulateur-impot/", "/en/vietnam/income-tax/"),
]

# Build lookup: fr_url -> (lang, native_url) and en_url -> (lang, native_url)
native_by_fr = {}
native_by_en = {}
for lang, native_url, fr_url, en_url in NATIVE_PAGES:
    native_by_fr[fr_url] = (lang, native_url)
    native_by_en[en_url] = (lang, native_url)

DOMAIN = "https://netsalaire.com"

def url(path):
    return DOMAIN + path

def hreflang_link(lang, href):
    return f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}"/>'

# Read existing sitemap
sitemap_path = os.path.join(BASE, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Parse all existing <url> blocks
url_blocks = re.findall(r'<url>(.*?)</url>', content, re.DOTALL)
print(f"Existing sitemap: {len(url_blocks)} URLs")

# Track which native pages are already referenced (by their FR/EN counterpart)
native_pages_added = set()

# Build new sitemap
lines = []
lines.append('<?xml version="1.0" encoding="UTF-8"?>')
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
lines.append('        xmlns:xhtml="http://www.w3.org/1999/xhtml">')

# Process existing URL blocks
comments_seen = set()
for block in url_blocks:
    loc_m = re.search(r'<loc>(.*?)</loc>', block)
    if not loc_m:
        continue
    loc = loc_m.group(1)
    path = loc.replace(DOMAIN, '')

    # Extract existing data
    priority_m = re.search(r'<priority>(.*?)</priority>', block)
    changefreq_m = re.search(r'<changefreq>(.*?)</changefreq>', block)
    priority = priority_m.group(1) if priority_m else '0.7'
    changefreq = changefreq_m.group(1) if changefreq_m else 'monthly'

    # Find comment for this block in original content
    # We'll regenerate comments based on the URL

    # Check if this page has a native alternate
    native_lang = None
    native_url = None
    if path in native_by_fr:
        native_lang, native_url = native_by_fr[path]
    elif path in native_by_en:
        native_lang, native_url = native_by_en[path]

    # Extract existing hreflang links
    existing_hreflangs = re.findall(r'hreflang="([^"]*)".*?href="([^"]*)"', block)
    hreflang_map = {lang: href for lang, href in existing_hreflangs}

    # Add native hreflang if applicable
    if native_lang and native_lang not in hreflang_map:
        hreflang_map[native_lang] = url(native_url)
        native_pages_added.add(native_url)

    # Build URL block
    lines.append('')
    lines.append('  <url>')
    lines.append(f'    <loc>{loc}</loc>')
    lines.append(f'    <lastmod>{TODAY}</lastmod>')
    lines.append(f'    <changefreq>{changefreq}</changefreq>')
    lines.append(f'    <priority>{priority}</priority>')

    # Write hreflang links in order: fr, en, native, x-default
    for lang_code in ['fr', 'en']:
        if lang_code in hreflang_map:
            lines.append(hreflang_link(lang_code, hreflang_map[lang_code]))
    # Native language
    for lang_code, href in sorted(hreflang_map.items()):
        if lang_code not in ('fr', 'en', 'x-default'):
            lines.append(hreflang_link(lang_code, href))
    # x-default
    if 'x-default' in hreflang_map:
        lines.append(hreflang_link('x-default', hreflang_map['x-default']))

    lines.append('  </url>')

# Now add native pages that don't yet have their own <url> entry
lines.append('')
lines.append('  <!-- ========== NATIVE LANGUAGE PAGES ========== -->')

for lang, native_path, fr_path, en_path in NATIVE_PAGES:
    lines.append('')
    lines.append('  <url>')
    lines.append(f'    <loc>{url(native_path)}</loc>')
    lines.append(f'    <lastmod>{TODAY}</lastmod>')
    lines.append(f'    <changefreq>monthly</changefreq>')
    lines.append(f'    <priority>0.7</priority>')
    lines.append(hreflang_link('fr', url(fr_path)))
    lines.append(hreflang_link('en', url(en_path)))
    lines.append(hreflang_link(lang, url(native_path)))
    lines.append(hreflang_link('x-default', url(fr_path)))
    lines.append('  </url>')

lines.append('')
lines.append('</urlset>')

# Write new sitemap
new_content = '\n'.join(lines) + '\n'
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Count URLs in new sitemap
new_count = new_content.count('<loc>')
print(f"New sitemap: {new_count} URLs (added {new_count - len(url_blocks)} native pages)")
print(f"All lastmod updated to {TODAY}")
print(f"Native hreflang added to {len(native_pages_added)} existing FR/EN pairs")
