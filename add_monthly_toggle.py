#!/usr/bin/env python3
"""
Add Monthly/Annual toggle to all tax simulators
"""

import os
import re

base = '/Users/motta/Documents/GitHub/impotsfrancemaroc'

# HTML for the toggle buttons (French)
TOGGLE_HTML_FR = '''                <div class="mb-8">
                    <div class="flex items-center justify-between mb-3">
                        <label class="block text-sm font-medium text-slate-700">Revenu Brut</label>
                        <div class="flex rounded-lg overflow-hidden border border-slate-200">
                            <button type="button" id="btn-monthly" onclick="setMode('monthly')" class="px-3 py-1 text-xs font-medium bg-white text-slate-600 hover:bg-slate-50 transition-colors">Mensuel</button>
                            <button type="button" id="btn-annual" onclick="setMode('annual')" class="px-3 py-1 text-xs font-medium bg-indigo-600 text-white">Annuel</button>
                        </div>
                    </div>
                    <div class="flex items-center gap-4">'''

# HTML for the toggle buttons (English)
TOGGLE_HTML_EN = '''                <div class="mb-8">
                    <div class="flex items-center justify-between mb-3">
                        <label class="block text-sm font-medium text-slate-700">Gross Income</label>
                        <div class="flex rounded-lg overflow-hidden border border-slate-200">
                            <button type="button" id="btn-monthly" onclick="setMode('monthly')" class="px-3 py-1 text-xs font-medium bg-white text-slate-600 hover:bg-slate-50 transition-colors">Monthly</button>
                            <button type="button" id="btn-annual" onclick="setMode('annual')" class="px-3 py-1 text-xs font-medium bg-indigo-600 text-white">Annual</button>
                        </div>
                    </div>
                    <div class="flex items-center gap-4">'''

# JavaScript for the toggle functionality
JS_TOGGLE = '''
        let isMonthly = false;

        function setMode(mode) {
            const input = document.getElementById('income-input');
            const slider = document.getElementById('income-slider');
            const btnMonthly = document.getElementById('btn-monthly');
            const btnAnnual = document.getElementById('btn-annual');
            const currentValue = parseFloat(input.value) || 0;

            if (mode === 'monthly' && !isMonthly) {
                // Switch to monthly: divide by 12
                isMonthly = true;
                input.value = Math.round(currentValue / 12);
                slider.max = Math.round(parseInt(slider.max) / 12);
                slider.value = Math.min(input.value, slider.max);
                btnMonthly.classList.remove('bg-white', 'text-slate-600');
                btnMonthly.classList.add('bg-indigo-600', 'text-white');
                btnAnnual.classList.remove('bg-indigo-600', 'text-white');
                btnAnnual.classList.add('bg-white', 'text-slate-600');
            } else if (mode === 'annual' && isMonthly) {
                // Switch to annual: multiply by 12
                isMonthly = false;
                input.value = Math.round(currentValue * 12);
                slider.max = Math.round(parseInt(slider.max) * 12);
                slider.value = Math.min(input.value, slider.max);
                btnAnnual.classList.remove('bg-white', 'text-slate-600');
                btnAnnual.classList.add('bg-indigo-600', 'text-white');
                btnMonthly.classList.remove('bg-indigo-600', 'text-white');
                btnMonthly.classList.add('bg-white', 'text-slate-600');
            }
            calculate();
        }

        function getAnnualIncome() {
            const input = parseFloat(document.getElementById('income-input').value) || 0;
            return isMonthly ? input * 12 : input;
        }

'''

def update_file(filepath, is_french):
    with open(filepath, 'r') as f:
        content = f.read()

    # Skip if already has toggle
    if 'btn-monthly' in content:
        print(f"  Skipping (already has toggle): {filepath}")
        return False

    # 1. Replace the input section header
    if is_french:
        # Pattern for French pages
        pattern = r'<div class="mb-8">\s*<label class="block text-sm font-medium text-slate-700 mb-3">Revenu [^<]+</label>\s*<div class="flex items-center gap-4">'
        content = re.sub(pattern, TOGGLE_HTML_FR, content)
    else:
        # Pattern for English pages
        pattern = r'<div class="mb-8">\s*<label class="block text-sm font-medium text-slate-700 mb-3">[^<]*(?:Income|Gross)[^<]*</label>\s*<div class="flex items-center gap-4">'
        content = re.sub(pattern, TOGGLE_HTML_EN, content)

    # 2. Update calculate() to use getAnnualIncome()
    # Replace: const income = parseFloat(document.getElementById('income-input').value) || 0;
    # With: const income = getAnnualIncome();
    content = re.sub(
        r"const income = parseFloat\(document\.getElementById\('income-input'\)\.value\) \|\| 0;",
        "const income = getAnnualIncome();",
        content
    )

    # 3. Add toggle JavaScript before the calculate function or at start of script
    # Find the main script and add toggle functions
    if 'function getAnnualIncome' not in content:
        # Add after BRACKETS/FEDERAL declaration or at start of calculate
        pattern = r'(const (?:BRACKETS|FEDERAL_BRACKETS) = \[[\s\S]*?\];[\s\S]*?(?:const \w+ = [^;]+;\s*)+)'
        match = re.search(pattern, content)
        if match:
            insert_pos = match.end()
            content = content[:insert_pos] + JS_TOGGLE + content[insert_pos:]

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"  Updated: {filepath}")
    return True

def main():
    updated = 0

    # FR pages
    print("\nUpdating FR pages...")
    for country in ['usa', 'royaume-uni', 'suisse', 'dubai', 'singapour', 'luxembourg',
                    'arabie-saoudite', 'espagne', 'japon', 'chine', 'inde', 'pakistan']:
        path = os.path.join(base, 'fr', country, 'simulateur-impot', 'index.html')
        if os.path.exists(path):
            if update_file(path, is_french=True):
                updated += 1

    # EN pages
    print("\nUpdating EN pages...")
    for country in ['usa', 'uk', 'switzerland', 'dubai', 'singapore', 'luxembourg',
                    'saudi-arabia', 'spain', 'japan', 'china', 'india', 'pakistan']:
        path = os.path.join(base, 'en', country, 'income-tax', 'index.html')
        if os.path.exists(path):
            if update_file(path, is_french=False):
                updated += 1

    print(f"\nTotal updated: {updated}")

if __name__ == '__main__':
    main()
