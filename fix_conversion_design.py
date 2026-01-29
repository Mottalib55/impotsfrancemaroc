#!/usr/bin/env python3
"""
Improve the design of currency conversions - make them more visually appealing
with badges/pills style instead of plain text in parentheses.
"""

import os
import re

COUNTRIES_FR = ['usa', 'royaume-uni', 'suisse', 'dubai', 'singapour', 'luxembourg',
                'arabie-saoudite', 'espagne', 'japon', 'chine', 'inde', 'pakistan']
COUNTRIES_EN = ['usa', 'uk', 'switzerland', 'dubai', 'singapore', 'luxembourg',
                'saudi-arabia', 'spain', 'japan', 'china', 'india', 'pakistan']

# Which countries show which currencies
SHOW_BOTH = ['royaume-uni', 'suisse', 'dubai', 'singapour', 'arabie-saoudite', 'japon', 'chine', 'inde', 'pakistan',
             'uk', 'switzerland', 'singapore', 'saudi-arabia', 'japan', 'china', 'india']
SHOW_EUR_ONLY = ['usa']
SHOW_USD_ONLY = ['luxembourg', 'espagne', 'spain']

def get_badge_html(country):
    """Get the styled badge HTML for conversions"""
    if country in SHOW_EUR_ONLY:
        return '''<div class="flex items-center justify-end gap-2 mt-3">
                        <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-blue-50 border border-blue-200 text-xs font-medium text-blue-700">
                            <span class="text-blue-400">≈</span> <span id="conv-total-eur">0 EUR</span>
                        </span>
                    </div>'''
    elif country in SHOW_USD_ONLY:
        return '''<div class="flex items-center justify-end gap-2 mt-3">
                        <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-green-50 border border-green-200 text-xs font-medium text-green-700">
                            <span class="text-green-400">≈</span> <span id="conv-total-usd">$0</span>
                        </span>
                    </div>'''
    else:
        return '''<div class="flex items-center justify-end gap-2 mt-3">
                        <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-blue-50 border border-blue-200 text-xs font-medium text-blue-700">
                            <span class="text-blue-400">≈</span> <span id="conv-total-eur">0 EUR</span>
                        </span>
                        <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-green-50 border border-green-200 text-xs font-medium text-green-700">
                            <span class="text-green-400">≈</span> <span id="conv-total-usd">$0</span>
                        </span>
                    </div>'''

def update_file(filepath, country):
    """Update a single file with better conversion design"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old inline conversion after total-tax
    # Pattern: </span> <span class="text-xs font-normal">(<span id="conv-total-eur"...)</span>
    content = re.sub(
        r'</span>\s*<span class="text-xs font-normal">\(<span id="conv-total-eur"[^)]+\)</span>',
        '</span>',
        content
    )

    # Also handle USD-only case
    content = re.sub(
        r'</span>\s*<span class="text-xs font-normal">\(<span id="conv-total-usd"[^)]+\)</span>',
        '</span>',
        content
    )

    # Now add the new styled badges after the progress bar section
    # Find: Taux effectif total...%</span></p>\n                </div>
    # And add badges after the </p> but before the </div>

    badge_html = get_badge_html(country)

    # Pattern to find the end of the taux effectif line
    pattern = r'(Taux effectif total.*?<span id="total-rate"[^>]*>[^<]*</span></p>)(\s*</div>)'

    # Check if badges already exist
    if 'conv-total-eur' not in content and 'conv-total-usd' not in content:
        # Badges were completely removed, need to add them back
        replacement = r'\1\n                    ' + badge_html + r'\2'
        content = re.sub(pattern, replacement, content)
    elif 'rounded-full bg-blue-50' not in content and 'rounded-full bg-green-50' not in content:
        # Old style exists, need to add new style
        # First remove any remaining old conv-total references
        content = re.sub(r'<span id="conv-total-eur"[^<]*</span>', '', content)
        content = re.sub(r'<span id="conv-total-usd"[^<]*</span>', '', content)
        content = re.sub(r'\s*\|\s*', '', content)  # Remove orphan pipes

        replacement = r'\1\n                    ' + badge_html + r'\2'
        content = re.sub(pattern, replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Updated: {filepath}")
    return True

def main():
    base_path = '/Users/motta/Documents/GitHub/impotsfrancemaroc'

    # Update FR pages
    print("\nUpdating FR pages...")
    for country in COUNTRIES_FR:
        filepath = os.path.join(base_path, 'fr', country, 'simulateur-impot', 'index.html')
        if os.path.exists(filepath):
            update_file(filepath, country)

    # Update EN pages
    print("\nUpdating EN pages...")
    for country in COUNTRIES_EN:
        filepath = os.path.join(base_path, 'en', country, 'income-tax', 'index.html')
        if os.path.exists(filepath):
            update_file(filepath, country)

    print("\nDone!")

if __name__ == '__main__':
    main()
