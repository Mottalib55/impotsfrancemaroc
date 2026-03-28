#!/usr/bin/env python3
"""
Fix comparison links on native language pages.

On each native page, the "Compare with similar countries" section links to /en/ pages.
This script replaces those links with native versions when available.

Example: On /es/espana/, a link to /en/mexico/income-tax/ becomes /es/mexico/simulador-impuestos/
"""

import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# EN slug -> (lang_code, native_url)
# Copied from refonte_navbar.py EN_NATIVE_LANG_MAP
EN_NATIVE_LANG_MAP = {
    'germany': ('de', '/de/deutschland/einkommensteuer/'),
    'austria': ('de', '/de/oesterreich/einkommensteuer/'),
    'switzerland': ('de', '/de/schweiz/einkommensteuer/'),
    'spain': ('es', '/es/espana/simulador-impuestos/'),
    'mexico': ('es', '/es/mexico/simulador-impuestos/'),
    'argentina': ('es', '/es/argentina/simulador-impuestos/'),
    'chile': ('es', '/es/chile/simulador-impuestos/'),
    'colombia': ('es', '/es/colombia/simulador-impuestos/'),
    'peru': ('es', '/es/peru/simulador-impuestos/'),
    'portugal': ('pt', '/pt/portugal/simulador-impostos/'),
    'brazil': ('pt', '/pt/brasil/simulador-impostos/'),
    'netherlands': ('nl', '/nl/nederland/belasting-berekenen/'),
    'belgium': ('nl', '/nl/belgie/belasting-berekenen/'),
    'saudi-arabia': ('ar', '/ar/arabie-saoudite/tax-calculator/'),
    'dubai': ('ar', '/ar/dubai/tax-calculator/'),
    'qatar': ('ar', '/ar/qatar/tax-calculator/'),
    'kuwait': ('ar', '/ar/koweit/tax-calculator/'),
    'egypt': ('ar', '/ar/egypte/tax-calculator/'),
    'italy': ('it', '/it/italia/calcolatore-imposte/'),
    'sweden': ('sv', '/sv/sverige/skatteberaknare/'),
    'norway': ('no', '/no/norge/skattekalkulator/'),
    'denmark': ('da', '/da/danmark/skatteberegner/'),
    'finland': ('fi', '/fi/suomi/verolaskuri/'),
    'greece': ('el', '/el/ellada/ypologismos-forou/'),
    'poland': ('pl', '/pl/polska/kalkulator-podatkowy/'),
    'czech-republic': ('cs', '/cs/cesko/danovy-kalkulator/'),
    'hungary': ('hu', '/hu/magyarorszag/ado-kalkulator/'),
    'romania': ('ro', '/ro/romania/calculator-impozit/'),
    'croatia': ('hr', '/hr/hrvatska/porezni-kalkulator/'),
    'turkey': ('tr', '/tr/turkiye/vergi-hesaplama/'),
    'japan': ('ja', '/ja/nihon/zeikin-keisan/'),
    'south-korea': ('ko', '/ko/hanguk/segeum-gyesan/'),
    'china': ('zh', '/zh/zhongguo/shuishou-jisuan/'),
    'thailand': ('th', '/th/prathet-thai/khamnuan-phasi/'),
    'malaysia': ('ms', '/ms/malaysia/kalkulator-cukai/'),
    'indonesia': ('id', '/id/indonesia/kalkulator-pajak/'),
    'vietnam': ('vi', '/vi/viet-nam/tinh-thue/'),
}

# All native language codes (to find native page files)
NATIVE_LANGS = ['ar', 'cs', 'da', 'de', 'el', 'es', 'fi', 'hr', 'hu',
                'id', 'it', 'ja', 'ko', 'ms', 'nl', 'no', 'pl', 'pt',
                'ro', 'sv', 'th', 'tr', 'vi', 'zh']


def detect_lang(filepath):
    """Detect language code from file path like .../es/espana/simulador-impuestos/index.html"""
    rel = os.path.relpath(filepath, BASE_DIR)
    parts = rel.replace('\\', '/').split('/')
    if parts[0] in NATIVE_LANGS:
        return parts[0]
    return None


def fix_comparison_links(filepath, lang):
    """Fix /en/ links in the comparison section of a native page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the comparison section: from git-compare icon to </main>
    marker_match = re.search(r'icon="lucide:git-compare"', content)
    if not marker_match:
        print(f"  SKIP (no comparison section): {filepath}")
        return 0

    marker_pos = marker_match.start()
    main_end = content.find('</main>', marker_pos)
    if main_end == -1:
        print(f"  SKIP (no </main> after comparison): {filepath}")
        return 0

    # Extract the comparison section
    section = content[marker_pos:main_end]

    # Find all /en/COUNTRY/income-tax/ links
    replacements = 0
    pattern = re.compile(r'href="/en/([a-z-]+)/income-tax/"')

    def replace_link(match):
        nonlocal replacements
        en_slug = match.group(1)
        if en_slug in EN_NATIVE_LANG_MAP:
            target_lang, native_url = EN_NATIVE_LANG_MAP[en_slug]
            if target_lang == lang:
                replacements += 1
                return f'href="{native_url}"'
        # No native version in same language → keep /en/
        return match.group(0)

    new_section = pattern.sub(replace_link, section)

    if replacements > 0:
        new_content = content[:marker_pos] + new_section + content[main_end:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return replacements


def main():
    total_files = 0
    total_replacements = 0
    files_modified = []

    # Find all native page index.html files
    for lang in NATIVE_LANGS:
        lang_dir = os.path.join(BASE_DIR, lang)
        if not os.path.isdir(lang_dir):
            continue
        for html_file in glob.glob(os.path.join(lang_dir, '*', '*', 'index.html')):
            total_files += 1
            rel_path = os.path.relpath(html_file, BASE_DIR)
            page_lang = detect_lang(html_file)
            if not page_lang:
                print(f"  SKIP (can't detect lang): {rel_path}")
                continue

            count = fix_comparison_links(html_file, page_lang)
            if count > 0:
                files_modified.append((rel_path, count))
                total_replacements += count
                print(f"  FIXED {count} link(s): {rel_path}")
            else:
                print(f"  no change: {rel_path}")

    print(f"\n{'='*60}")
    print(f"Total files scanned: {total_files}")
    print(f"Files modified: {len(files_modified)}")
    print(f"Links replaced: {total_replacements}")
    if files_modified:
        print(f"\nModified files:")
        for path, count in sorted(files_modified):
            print(f"  {path} ({count} links)")


if __name__ == '__main__':
    main()
