#!/usr/bin/env python3
"""
Add currency conversion references (EUR/USD) to all tax simulator pages.
- If currency is EUR: show USD only
- If currency is USD: show EUR only
- Other currencies: show both EUR and USD
"""

import os
import re

# Exchange rates (approximate, for reference purposes)
EXCHANGE_RATES = {
    'USD': {'to_eur': 0.92, 'to_usd': 1},
    'EUR': {'to_eur': 1, 'to_usd': 1.09},
    'GBP': {'to_eur': 1.17, 'to_usd': 1.27},
    'CHF': {'to_eur': 1.05, 'to_usd': 1.14},
    'AED': {'to_eur': 0.25, 'to_usd': 0.27},
    'SGD': {'to_eur': 0.69, 'to_usd': 0.75},
    'SAR': {'to_eur': 0.24, 'to_usd': 0.27},
    'JPY': {'to_eur': 0.0061, 'to_usd': 0.0066},
    'CNY': {'to_eur': 0.13, 'to_usd': 0.14},
    'INR': {'to_eur': 0.011, 'to_usd': 0.012},
    'PKR': {'to_eur': 0.0033, 'to_usd': 0.0036},
}

# Country configurations
COUNTRIES_FR = {
    'usa': {'currency': 'USD', 'symbol': '$', 'show': ['EUR']},
    'royaume-uni': {'currency': 'GBP', 'symbol': '£', 'show': ['EUR', 'USD']},
    'suisse': {'currency': 'CHF', 'symbol': 'CHF', 'show': ['EUR', 'USD']},
    'dubai': {'currency': 'AED', 'symbol': 'AED', 'show': ['EUR', 'USD']},
    'singapour': {'currency': 'SGD', 'symbol': 'SGD', 'show': ['EUR', 'USD']},
    'luxembourg': {'currency': 'EUR', 'symbol': '€', 'show': ['USD']},
    'arabie-saoudite': {'currency': 'SAR', 'symbol': 'SAR', 'show': ['EUR', 'USD']},
    'espagne': {'currency': 'EUR', 'symbol': '€', 'show': ['USD']},
    'japon': {'currency': 'JPY', 'symbol': '¥', 'show': ['EUR', 'USD']},
    'chine': {'currency': 'CNY', 'symbol': '¥', 'show': ['EUR', 'USD']},
    'inde': {'currency': 'INR', 'symbol': '₹', 'show': ['EUR', 'USD']},
    'pakistan': {'currency': 'PKR', 'symbol': 'PKR', 'show': ['EUR', 'USD']},
}

COUNTRIES_EN = {
    'usa': {'currency': 'USD', 'symbol': '$', 'show': ['EUR']},
    'uk': {'currency': 'GBP', 'symbol': '£', 'show': ['EUR', 'USD']},
    'switzerland': {'currency': 'CHF', 'symbol': 'CHF', 'show': ['EUR', 'USD']},
    'dubai': {'currency': 'AED', 'symbol': 'AED', 'show': ['EUR', 'USD']},
    'singapore': {'currency': 'SGD', 'symbol': 'SGD', 'show': ['EUR', 'USD']},
    'luxembourg': {'currency': 'EUR', 'symbol': '€', 'show': ['USD']},
    'saudi-arabia': {'currency': 'SAR', 'symbol': 'SAR', 'show': ['EUR', 'USD']},
    'spain': {'currency': 'EUR', 'symbol': '€', 'show': ['USD']},
    'japan': {'currency': 'JPY', 'symbol': '¥', 'show': ['EUR', 'USD']},
    'china': {'currency': 'CNY', 'symbol': '¥', 'show': ['EUR', 'USD']},
    'india': {'currency': 'INR', 'symbol': '₹', 'show': ['EUR', 'USD']},
    'pakistan': {'currency': 'PKR', 'symbol': 'PKR', 'show': ['EUR', 'USD']},
}

def get_conversion_html_fr(show_currencies):
    """Generate HTML for conversion display (French)"""
    if show_currencies == ['EUR']:
        return '''
                <!-- Currency Conversion Reference -->
                <div class="bg-slate-100 rounded-xl p-4 mt-4">
                    <p class="text-xs text-slate-500 flex items-center gap-2">
                        <iconify-icon icon="lucide:repeat" width="14"></iconify-icon>
                        <span>Equivalent : <span id="conv-eur" class="font-medium text-slate-700">~0 EUR</span></span>
                    </p>
                </div>'''
    elif show_currencies == ['USD']:
        return '''
                <!-- Currency Conversion Reference -->
                <div class="bg-slate-100 rounded-xl p-4 mt-4">
                    <p class="text-xs text-slate-500 flex items-center gap-2">
                        <iconify-icon icon="lucide:repeat" width="14"></iconify-icon>
                        <span>Equivalent : <span id="conv-usd" class="font-medium text-slate-700">~$0</span></span>
                    </p>
                </div>'''
    else:  # Both EUR and USD
        return '''
                <!-- Currency Conversion Reference -->
                <div class="bg-slate-100 rounded-xl p-4 mt-4">
                    <p class="text-xs text-slate-500 flex items-center gap-2">
                        <iconify-icon icon="lucide:repeat" width="14"></iconify-icon>
                        <span>Equivalents : <span id="conv-eur" class="font-medium text-slate-700">~0 EUR</span> | <span id="conv-usd" class="font-medium text-slate-700">~$0</span></span>
                    </p>
                </div>'''

def get_conversion_html_en(show_currencies):
    """Generate HTML for conversion display (English)"""
    if show_currencies == ['EUR']:
        return '''
                <!-- Currency Conversion Reference -->
                <div class="bg-slate-100 rounded-xl p-4 mt-4">
                    <p class="text-xs text-slate-500 flex items-center gap-2">
                        <iconify-icon icon="lucide:repeat" width="14"></iconify-icon>
                        <span>Equivalent: <span id="conv-eur" class="font-medium text-slate-700">~0 EUR</span></span>
                    </p>
                </div>'''
    elif show_currencies == ['USD']:
        return '''
                <!-- Currency Conversion Reference -->
                <div class="bg-slate-100 rounded-xl p-4 mt-4">
                    <p class="text-xs text-slate-500 flex items-center gap-2">
                        <iconify-icon icon="lucide:repeat" width="14"></iconify-icon>
                        <span>Equivalent: <span id="conv-usd" class="font-medium text-slate-700">~$0</span></span>
                    </p>
                </div>'''
    else:  # Both EUR and USD
        return '''
                <!-- Currency Conversion Reference -->
                <div class="bg-slate-100 rounded-xl p-4 mt-4">
                    <p class="text-xs text-slate-500 flex items-center gap-2">
                        <iconify-icon icon="lucide:repeat" width="14"></iconify-icon>
                        <span>Equivalents: <span id="conv-eur" class="font-medium text-slate-700">~0 EUR</span> | <span id="conv-usd" class="font-medium text-slate-700">~$0</span></span>
                    </p>
                </div>'''

def get_conversion_js(currency, show_currencies):
    """Generate JavaScript for currency conversion"""
    rates = EXCHANGE_RATES[currency]

    js_lines = ["\n            // Currency conversion"]

    if 'EUR' in show_currencies:
        js_lines.append(f"            const toEur = {rates['to_eur']};")
        js_lines.append("            document.getElementById('conv-eur').textContent = '~' + Math.round(netIncome * toEur).toLocaleString() + ' EUR';")

    if 'USD' in show_currencies:
        js_lines.append(f"            const toUsd = {rates['to_usd']};")
        js_lines.append("            document.getElementById('conv-usd').textContent = '~$' + Math.round(netIncome * toUsd).toLocaleString();")

    return '\n'.join(js_lines)

def update_file(filepath, country_config, lang):
    """Update a single file with currency conversion"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has conversion
    if 'conv-eur' in content or 'conv-usd' in content:
        print(f"  Skipping (already has conversion): {filepath}")
        return False

    currency = country_config['currency']
    show = country_config['show']

    # Get HTML and JS for this currency
    if lang == 'fr':
        conv_html = get_conversion_html_fr(show)
    else:
        conv_html = get_conversion_html_en(show)

    conv_js = get_conversion_js(currency, show)

    # Insert HTML after the summary bar (before </div> that closes the calculator card)
    # Find the pattern: total-rate followed by closing divs
    pattern = r'(Taux effectif total.*?</span></p>\s*</div>)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + conv_html + content[insert_pos:]
    else:
        # Try English pattern
        pattern = r'(Effective total rate.*?</span></p>\s*</div>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            insert_pos = match.end()
            content = content[:insert_pos] + conv_html + content[insert_pos:]
        else:
            print(f"  Warning: Could not find insertion point in {filepath}")
            return False

    # Insert JS in the calculate() function, after netIncome calculation
    # Look for the tax-bar update line and insert before it
    js_pattern = r"(document\.getElementById\('tax-bar'\)\.style\.width = taxPercent \+ '%';)"
    if re.search(js_pattern, content):
        content = re.sub(js_pattern, conv_js + '\n\n            \\1', content)
    else:
        print(f"  Warning: Could not find JS insertion point in {filepath}")
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Updated: {filepath}")
    return True

def main():
    base_path = '/Users/motta/Documents/GitHub/impotsfrancemaroc'

    updated_count = 0

    # Update FR pages
    print("\nUpdating FR pages...")
    for country, config in COUNTRIES_FR.items():
        filepath = os.path.join(base_path, 'fr', country, 'simulateur-impot', 'index.html')
        if os.path.exists(filepath):
            if update_file(filepath, config, 'fr'):
                updated_count += 1
        else:
            print(f"  Not found: {filepath}")

    # Update EN pages
    print("\nUpdating EN pages...")
    for country, config in COUNTRIES_EN.items():
        filepath = os.path.join(base_path, 'en', country, 'income-tax', 'index.html')
        if os.path.exists(filepath):
            if update_file(filepath, config, 'en'):
                updated_count += 1
        else:
            print(f"  Not found: {filepath}")

    print(f"\nTotal updated: {updated_count}")

if __name__ == '__main__':
    main()
