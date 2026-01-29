#!/usr/bin/env python3
"""
Update currency conversions to show under EACH amount, not just at the bottom.
Adds conversion display under: gross income input, income tax, social tax, net income, total tax
"""

import os
import re

# Exchange rates
RATES = {
    'USD': {'eur': 0.92, 'usd': 1},
    'EUR': {'eur': 1, 'usd': 1.09},
    'GBP': {'eur': 1.17, 'usd': 1.27},
    'CHF': {'eur': 1.05, 'usd': 1.14},
    'AED': {'eur': 0.25, 'usd': 0.27},
    'SGD': {'eur': 0.69, 'usd': 0.75},
    'SAR': {'eur': 0.24, 'usd': 0.27},
    'JPY': {'eur': 0.0061, 'usd': 0.0066},
    'CNY': {'eur': 0.13, 'usd': 0.14},
    'INR': {'eur': 0.011, 'usd': 0.012},
    'PKR': {'eur': 0.0033, 'usd': 0.0036},
}

COUNTRIES_FR = {
    'usa': {'currency': 'USD', 'show': ['EUR']},
    'royaume-uni': {'currency': 'GBP', 'show': ['EUR', 'USD']},
    'suisse': {'currency': 'CHF', 'show': ['EUR', 'USD']},
    'dubai': {'currency': 'AED', 'show': ['EUR', 'USD']},
    'singapour': {'currency': 'SGD', 'show': ['EUR', 'USD']},
    'luxembourg': {'currency': 'EUR', 'show': ['USD']},
    'arabie-saoudite': {'currency': 'SAR', 'show': ['EUR', 'USD']},
    'espagne': {'currency': 'EUR', 'show': ['USD']},
    'japon': {'currency': 'JPY', 'show': ['EUR', 'USD']},
    'chine': {'currency': 'CNY', 'show': ['EUR', 'USD']},
    'inde': {'currency': 'INR', 'show': ['EUR', 'USD']},
    'pakistan': {'currency': 'PKR', 'show': ['EUR', 'USD']},
}

COUNTRIES_EN = {
    'usa': {'currency': 'USD', 'show': ['EUR']},
    'uk': {'currency': 'GBP', 'show': ['EUR', 'USD']},
    'switzerland': {'currency': 'CHF', 'show': ['EUR', 'USD']},
    'dubai': {'currency': 'AED', 'show': ['EUR', 'USD']},
    'singapore': {'currency': 'SGD', 'show': ['EUR', 'USD']},
    'luxembourg': {'currency': 'EUR', 'show': ['USD']},
    'saudi-arabia': {'currency': 'SAR', 'show': ['EUR', 'USD']},
    'spain': {'currency': 'EUR', 'show': ['USD']},
    'japan': {'currency': 'JPY', 'show': ['EUR', 'USD']},
    'china': {'currency': 'CNY', 'show': ['EUR', 'USD']},
    'india': {'currency': 'INR', 'show': ['EUR', 'USD']},
    'pakistan': {'currency': 'PKR', 'show': ['EUR', 'USD']},
}

def get_conv_span(show, id_suffix):
    """Generate the conversion span HTML"""
    if show == ['EUR']:
        return f'<span id="conv-{id_suffix}-eur" class="text-slate-400">~0 EUR</span>'
    elif show == ['USD']:
        return f'<span id="conv-{id_suffix}-usd" class="text-slate-400">~$0</span>'
    else:
        return f'<span id="conv-{id_suffix}-eur" class="text-slate-400">~0 EUR</span> | <span id="conv-{id_suffix}-usd" class="text-slate-400">~$0</span>'

def get_js_conversion(currency, show):
    """Generate JavaScript for all conversions"""
    rates = RATES[currency]

    js = f'''
            // Currency conversions
            const toEur = {rates['eur']};
            const toUsd = {rates['usd']};

            function formatConv(val, isUsd) {{
                const formatted = Math.round(val).toLocaleString();
                return isUsd ? '~$' + formatted : '~' + formatted + ' EUR';
            }}
'''

    # Fields to convert: gross, tax, social, net, monthly, total
    fields = [
        ('gross', 'income'),
        ('tax', 'incomeTax'),
        ('social', 'socialTax'),
        ('net', 'netIncome'),
        ('monthly', 'netIncome / 12'),
        ('total', 'totalTax'),
    ]

    for field_id, var_name in fields:
        if 'EUR' in show:
            js += f"            document.getElementById('conv-{field_id}-eur').textContent = formatConv({var_name} * toEur, false);\n"
        if 'USD' in show:
            js += f"            document.getElementById('conv-{field_id}-usd').textContent = formatConv({var_name} * toUsd, true);\n"

    return js

def update_file(filepath, config, lang):
    """Update a single file with conversions under each amount"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    show = config['show']
    currency = config['currency']

    # Remove old conversion section if exists
    content = re.sub(r'\s*<!-- Currency Conversion Reference -->.*?</div>\s*(?=</div>\s*<div class="bg-white)', '', content, flags=re.DOTALL)

    # Also remove old JS conversion code
    content = re.sub(r'\s*// Currency conversion\s*const toEur.*?toLocaleString\(\);', '', content, flags=re.DOTALL)

    # 1. Add conversion under gross income input
    # Find the closing </div> after the input field
    pattern = r'(<input type="number" id="income-input"[^>]+>)\s*(<span class="absolute[^>]+>[^<]+</span>\s*</div>\s*</div>\s*</div>)'
    replacement = r'\1\n                            \2\n                    <p class="text-xs text-slate-400 mt-2 text-right">' + get_conv_span(show, 'gross') + '</p>'
    content = re.sub(pattern, replacement, content)

    # 2. Add conversion under income tax
    # Pattern: <p class="text-2xl font-bold text-indigo-600" id="income-tax">
    pattern = r'(<p class="text-2xl font-bold text-indigo-600" id="income-tax">[^<]+</p>)'
    replacement = r'\1\n                        <p class="text-xs mt-1">' + get_conv_span(show, 'tax') + '</p>'
    content = re.sub(pattern, replacement, content)

    # 3. Add conversion under social tax
    pattern = r'(<p class="text-2xl font-bold text-amber-600" id="social-tax">[^<]+</p>)'
    replacement = r'\1\n                        <p class="text-xs mt-1">' + get_conv_span(show, 'social') + '</p>'
    content = re.sub(pattern, replacement, content)

    # For USA which has different structure (fica-tax instead of social-tax)
    pattern = r'(<p class="text-2xl font-bold text-amber-600" id="fica-tax">[^<]+</p>)'
    replacement = r'\1\n                        <p class="text-xs mt-1">' + get_conv_span(show, 'social') + '</p>'
    content = re.sub(pattern, replacement, content)

    # 4. Add conversion under net income (both annual and monthly)
    pattern = r'(<p class="text-3xl font-bold text-emerald-600" id="net-income">[^<]+</p>)'
    replacement = r'\1\n                        <p class="text-xs mt-1">' + get_conv_span(show, 'net') + '</p>'
    content = re.sub(pattern, replacement, content)

    # Also for 2xl variant
    pattern = r'(<p class="text-2xl font-bold text-emerald-600" id="net-income">[^<]+</p>)'
    replacement = r'\1\n                        <p class="text-xs mt-1">' + get_conv_span(show, 'net') + '</p>'
    content = re.sub(pattern, replacement, content)

    # 5. Add conversion under monthly
    pattern = r'(Mensuel\s*:\s*<span id="net-monthly"[^>]*>[^<]+</span>)'
    replacement = r'\1 (' + get_conv_span(show, 'monthly') + ')'
    content = re.sub(pattern, replacement, content)

    # English version
    pattern = r'(Monthly:\s*<span id="net-monthly"[^>]*>[^<]+</span>)'
    replacement = r'\1 (' + get_conv_span(show, 'monthly') + ')'
    content = re.sub(pattern, replacement, content)

    # 6. Add conversion under total tax
    pattern = r'(<span class="text-lg font-bold text-slate-900" id="total-tax">[^<]+</span>)'
    replacement = r'\1 <span class="text-xs font-normal">(' + get_conv_span(show, 'total') + ')</span>'
    content = re.sub(pattern, replacement, content)

    # 7. Add/Update JavaScript conversion code
    js_code = get_js_conversion(currency, show)

    # Insert JS after netIncome calculation, before tax-bar update
    # Find the pattern and insert conversion code
    pattern = r"(const taxPercent = income > 0 \? Math\.min\(\(totalTax / income\) \* 100, 100\) : 0;)"
    if re.search(pattern, content):
        content = re.sub(pattern, js_code + '\n            \\1', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Updated: {filepath}")
    return True

def main():
    base_path = '/Users/motta/Documents/GitHub/impotsfrancemaroc'

    # Update FR pages
    print("\nUpdating FR pages...")
    for country, config in COUNTRIES_FR.items():
        filepath = os.path.join(base_path, 'fr', country, 'simulateur-impot', 'index.html')
        if os.path.exists(filepath):
            update_file(filepath, config, 'fr')

    # Update EN pages
    print("\nUpdating EN pages...")
    for country, config in COUNTRIES_EN.items():
        filepath = os.path.join(base_path, 'en', country, 'income-tax', 'index.html')
        if os.path.exists(filepath):
            update_file(filepath, config, 'en')

    print("\nDone!")

if __name__ == '__main__':
    main()
