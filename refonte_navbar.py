#!/usr/bin/env python3
"""
Refonte du menu de navigation (navbar) - Script de remplacement automatique.

Ce script remplace le <nav>...</nav> de chaque fichier HTML par un menu unifié :
1. Mega-menu "Tous les pays" par régions (multi-colonnes)
2. "France vs Maroc" déplacé dans les dropdowns France/Maroc
3. Menu mobile complet avec accordéons
4. Consistant sur les 136+ pages
"""

import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def extract_lang_switcher_links(nav_html):
    """Extract the language switcher <a> links from the existing nav.

    Returns a list of <a>...</a> strings from inside the lang-dropdown div.
    """
    # Match the lang dropdown div content (both home and page variants)
    pattern = r'<div\s+id="lang-dropdown-(?:home|page)"[^>]*>(.*?)</div>'
    match = re.search(pattern, nav_html, re.DOTALL)
    if not match:
        return []
    inner = match.group(1)
    # Extract all <a> tags
    links = re.findall(r'<a\s[^>]*>.*?</a>', inner, re.DOTALL)
    return links


def detect_lang_dropdown_id(nav_html):
    """Detect whether this page uses lang-dropdown-home or lang-dropdown-page."""
    if 'lang-dropdown-home' in nav_html:
        return 'lang-dropdown-home'
    return 'lang-dropdown-page'


def detect_language(filepath):
    """Detect FR or EN from file path."""
    rel = os.path.relpath(filepath, BASE_DIR)
    if rel.startswith('en/') or rel.startswith('en\\'):
        return 'en'
    return 'fr'


def is_homepage(filepath):
    """Check if this is the homepage (fr/index.html or en/index.html)."""
    rel = os.path.relpath(filepath, BASE_DIR).replace('\\', '/')
    return rel in ('fr/index.html', 'en/index.html')


def build_navbar(lang, lang_dropdown_id, lang_links, is_home):
    """Build the new unified navbar HTML."""

    if lang == 'fr':
        return build_navbar_fr(lang_dropdown_id, lang_links, is_home)
    else:
        return build_navbar_en(lang_dropdown_id, lang_links, is_home)


def build_navbar_fr(lang_dropdown_id, lang_links, is_home):
    """Build the French version of the navbar."""
    # France/Maroc anchor links differ on homepage vs inner pages
    france_anchor = "#france" if is_home else "/fr/#france"
    maroc_anchor = "#maroc" if is_home else "/fr/#maroc"
    contact_anchor = "#contact" if is_home else "/fr/#contact"
    logo_href = "/fr/"

    lang_links_html = "\n                        ".join(lang_links)

    # Contact button only on homepage
    contact_btn = ""
    if is_home:
        contact_btn = f'''
                <a href="{contact_anchor}" class="hidden md:flex items-center gap-2 text-xs font-medium bg-slate-100 hover:bg-slate-200 border border-slate-200 text-slate-900 px-4 py-2 rounded-full transition-all">
                    Contact
                    <iconify-icon icon="lucide:arrow-right" width="14" stroke-width="1.5"></iconify-icon>
                </a>'''

    nav = f'''<nav class="fixed top-0 w-full z-50 border-b border-slate-200 bg-white/80 backdrop-blur-md">
        <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
            <a href="{logo_href}" class="flex items-center gap-2 group">
                <div class="w-8 h-8 bg-slate-900 rounded flex items-center justify-center text-white font-semibold tracking-tighter shadow-md group-hover:bg-indigo-600 transition-colors duration-300">
                    N.
                </div>
                <span class="font-semibold tracking-tight text-slate-900">NetSalaire</span>
            </a>
            <!-- Desktop Menu -->
            <div class="hidden md:flex items-center gap-8 text-sm font-medium text-slate-600">
                <!-- France Dropdown -->
                <div class="relative group">
                    <a href="{france_anchor}" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
                        <iconify-icon icon="circle-flags:fr" width="16"></iconify-icon> France
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </a>
                    <div class="absolute top-full left-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-lg shadow-lg py-2 min-w-[220px]">
                            <a href="/fr/france/simulateur-impot-revenu/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:landmark" width="18" class="text-indigo-500"></iconify-icon>
                                Simulateur Impôt
                            </a>
                            <a href="/fr/france/simulateur-salaire-brut-net/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:calculator" width="18" class="text-indigo-500"></iconify-icon>
                                Brut vers Net
                            </a>
                            <a href="/fr/france/guide/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:book-open" width="18" class="text-indigo-500"></iconify-icon>
                                Guide Fiscal
                            </a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <a href="/fr/france/simulateur-chomage-are/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">📉</span>
                                Chômage ARE
                            </a>
                            <a href="/fr/france/simulateur-indemnite-licenciement/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">📋</span>
                                Licenciement
                            </a>
                            <a href="/fr/france/simulateur-rupture-conventionnelle/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">🤝</span>
                                Rupture Conv.
                            </a>
                            <a href="/fr/france/simulateur-apl/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">🏠</span>
                                APL
                            </a>
                            <a href="/fr/france/creche-tarifs/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">👶</span>
                                Crèche
                            </a>
                            <a href="/fr/france/simulateur-indemnite-kilometrique/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">🚗</span>
                                Frais Km
                            </a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <a href="/fr/comparateur-salaire-france-maroc/" class="flex items-center gap-3 px-4 py-2 text-indigo-600 hover:bg-indigo-50 hover:text-indigo-700 transition-colors text-sm font-medium">
                                <span class="w-[18px] text-center">🔀</span>
                                Comparer France vs Maroc
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Maroc Dropdown -->
                <div class="relative group">
                    <a href="{maroc_anchor}" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
                        <iconify-icon icon="circle-flags:ma" width="16"></iconify-icon> Maroc
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </a>
                    <div class="absolute top-full left-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-lg shadow-lg py-2 min-w-[220px]">
                            <a href="/fr/maroc/simulateur-impot-revenu/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:landmark" width="18" class="text-emerald-500"></iconify-icon>
                                Simulateur Impôt
                            </a>
                            <a href="/fr/maroc/simulateur-salaire-brut-net/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:calculator" width="18" class="text-emerald-500"></iconify-icon>
                                Brut vers Net
                            </a>
                            <a href="/fr/maroc/guide/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:book-open" width="18" class="text-emerald-500"></iconify-icon>
                                Guide Fiscal
                            </a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <a href="/fr/comparateur-salaire-france-maroc/" class="flex items-center gap-3 px-4 py-2 text-emerald-600 hover:bg-emerald-50 hover:text-emerald-700 transition-colors text-sm font-medium">
                                <span class="w-[18px] text-center">🔀</span>
                                Comparer France vs Maroc
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Mega-menu Tous les pays -->
                <div class="relative group">
                    <button class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2 text-sm font-medium text-slate-600">
                        <iconify-icon icon="lucide:globe" width="16"></iconify-icon> Tous les pays
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </button>
                    <div class="absolute top-full right-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-xl shadow-xl mega-country-container" style="width: 600px; max-height: 75vh; overflow-y: auto;">
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mega-country-title">Europe</div>
                            <div class="grid grid-cols-2 mega-country-grid" style="column-gap: 2rem; row-gap: 0.25rem;">
                                <a href="/fr/france/simulateur-impot-revenu/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇫🇷</span> France</a>
                                <a href="/fr/espagne/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇪🇸</span> Espagne</a>
                                <a href="/fr/royaume-uni/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇬🇧</span> Royaume-Uni</a>
                                <a href="/fr/allemagne/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇩🇪</span> Allemagne</a>
                                <a href="/fr/italie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇮🇹</span> Italie</a>
                                <a href="/fr/pays-bas/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇳🇱</span> Pays-Bas</a>
                                <a href="/fr/suisse/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇭</span> Suisse</a>
                                <a href="/fr/portugal/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇹</span> Portugal</a>
                                <a href="/fr/belgique/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇧🇪</span> Belgique</a>
                                <a href="/fr/luxembourg/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇱🇺</span> Luxembourg</a>
                                <a href="/fr/autriche/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇦🇹</span> Autriche</a>
                                <a href="/fr/irlande/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇮🇪</span> Irlande</a>
                                <a href="/fr/suede/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇸🇪</span> Suède</a>
                                <a href="/fr/norvege/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇳🇴</span> Norvège</a>
                                <a href="/fr/danemark/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇩🇰</span> Danemark</a>
                                <a href="/fr/finlande/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇫🇮</span> Finlande</a>
                                <a href="/fr/grece/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇬🇷</span> Grèce</a>
                                <a href="/fr/pologne/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇱</span> Pologne</a>
                                <a href="/fr/tchequie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇿</span> Tchéquie</a>
                                <a href="/fr/hongrie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇭🇺</span> Hongrie</a>
                                <a href="/fr/roumanie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇷🇴</span> Roumanie</a>
                                <a href="/fr/croatie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇭🇷</span> Croatie</a>
                                <a href="/fr/turquie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇹🇷</span> Turquie</a>
                            </div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mega-country-title">Amériques</div>
                            <div class="grid grid-cols-2 mega-country-grid" style="column-gap: 2rem; row-gap: 0.25rem;">
                                <a href="/fr/usa/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇺🇸</span> USA</a>
                                <a href="/fr/canada/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇦</span> Canada</a>
                                <a href="/fr/bresil/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇧🇷</span> Brésil</a>
                                <a href="/fr/mexique/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇲🇽</span> Mexique</a>
                                <a href="/fr/argentine/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇦🇷</span> Argentine</a>
                                <a href="/fr/chili/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇱</span> Chili</a>
                                <a href="/fr/colombie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇴</span> Colombie</a>
                                <a href="/fr/perou/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇪</span> Pérou</a>
                            </div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mega-country-title">Asie-Pacifique</div>
                            <div class="grid grid-cols-2 mega-country-grid" style="column-gap: 2rem; row-gap: 0.25rem;">
                                <a href="/fr/japon/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇯🇵</span> Japon</a>
                                <a href="/fr/coree-du-sud/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇰🇷</span> Corée du Sud</a>
                                <a href="/fr/chine/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇳</span> Chine</a>
                                <a href="/fr/singapour/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇸🇬</span> Singapour</a>
                                <a href="/fr/australie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇦🇺</span> Australie</a>
                                <a href="/fr/hong-kong/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇭🇰</span> Hong Kong</a>
                                <a href="/fr/inde/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇮🇳</span> Inde</a>
                                <a href="/fr/nouvelle-zelande/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇳🇿</span> Nouvelle-Zélande</a>
                                <a href="/fr/indonesie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇮🇩</span> Indonésie</a>
                                <a href="/fr/malaisie/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇲🇾</span> Malaisie</a>
                                <a href="/fr/thailande/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇹🇭</span> Thaïlande</a>
                                <a href="/fr/pakistan/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇰</span> Pakistan</a>
                                <a href="/fr/philippines/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇭</span> Philippines</a>
                                <a href="/fr/vietnam/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇻🇳</span> Vietnam</a>
                            </div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mega-country-title">Moyen-Orient & Afrique</div>
                            <div class="grid grid-cols-2 mega-country-grid" style="column-gap: 2rem; row-gap: 0.25rem;">
                                <a href="/fr/maroc/simulateur-impot-revenu/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇲🇦</span> Maroc</a>
                                <a href="/fr/dubai/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇦🇪</span> Émirats arabes</a>
                                <a href="/fr/arabie-saoudite/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇸🇦</span> Arabie Saoudite</a>
                                <a href="/fr/qatar/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇶🇦</span> Qatar</a>
                                <a href="/fr/koweit/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇰🇼</span> Koweït</a>
                                <a href="/fr/egypte/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇪🇬</span> Égypte</a>
                                <a href="/fr/afrique-du-sud/simulateur-impot/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇿🇦</span> Afrique du Sud</a>
                            </div>
                            <div class="border-t border-slate-100 pt-3">
                                <a href="/fr/comparateur-global/" class="flex items-center gap-2 text-sm font-medium text-indigo-600 hover:text-indigo-700 transition-colors">
                                    <iconify-icon icon="lucide:bar-chart-3" width="16"></iconify-icon> 📊 Comparer tous les pays →
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <a href="/fr/faq/" class="hover:text-slate-900 transition-colors">FAQ</a>
            </div>
            <div class="flex items-center gap-3">
                <!-- Language Switcher -->
                <div class="relative">
                    <button onclick="document.getElementById('{lang_dropdown_id}').classList.toggle('hidden')" class="flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-medium text-slate-600 hover:text-slate-900 bg-slate-100 hover:bg-slate-200 border border-slate-200 rounded-full transition-all" title="Changer de langue">
                        <span class="lang-flag">🇫🇷</span>
                        <iconify-icon icon="lucide:chevron-down" width="14"></iconify-icon>
                    </button>
                    <div id="{lang_dropdown_id}" class="hidden absolute top-full right-0 mt-2 bg-white border border-slate-200 rounded-lg shadow-lg min-w-[140px] py-1 z-50">
                        {lang_links_html}
                    </div>
                </div>{contact_btn}
                <!-- Mobile Menu Button -->
                <button onclick="document.getElementById('mobile-menu').classList.toggle('hidden')" class="md:hidden p-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-colors">
                    <iconify-icon icon="lucide:menu" width="24"></iconify-icon>
                </button>
            </div>
        </div>
        <!-- Mobile Menu (Accordéons) -->
        <div id="mobile-menu" class="hidden md:hidden bg-white border-t border-slate-200">
            <div class="px-6 py-4 space-y-1">
                <!-- France Accordion -->
                <div>
                    <button onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('.chevron-icon').classList.toggle('rotate-180')" class="w-full flex items-center justify-between py-3 text-sm font-semibold text-slate-900">
                        <span class="flex items-center gap-2">
                            <iconify-icon icon="circle-flags:fr" width="18"></iconify-icon> France
                        </span>
                        <iconify-icon icon="lucide:chevron-down" width="16" class="chevron-icon text-slate-400 transition-transform duration-200"></iconify-icon>
                    </button>
                    <div class="hidden pl-6 pb-3 space-y-2">
                        <a href="/fr/france/simulateur-impot-revenu/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <iconify-icon icon="lucide:landmark" width="16" class="text-indigo-500"></iconify-icon> Simulateur Impôt
                        </a>
                        <a href="/fr/france/simulateur-salaire-brut-net/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <iconify-icon icon="lucide:calculator" width="16" class="text-indigo-500"></iconify-icon> Brut vers Net
                        </a>
                        <a href="/fr/france/guide/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <iconify-icon icon="lucide:book-open" width="16" class="text-indigo-500"></iconify-icon> Guide Fiscal
                        </a>
                        <a href="/fr/france/simulateur-chomage-are/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>📉</span> Chômage ARE
                        </a>
                        <a href="/fr/france/simulateur-indemnite-licenciement/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>📋</span> Licenciement
                        </a>
                        <a href="/fr/france/simulateur-rupture-conventionnelle/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>🤝</span> Rupture Conv.
                        </a>
                        <a href="/fr/france/simulateur-apl/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>🏠</span> APL
                        </a>
                        <a href="/fr/france/creche-tarifs/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>👶</span> Crèche
                        </a>
                        <a href="/fr/france/simulateur-indemnite-kilometrique/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>🚗</span> Frais Km
                        </a>
                        <div class="border-t border-slate-100 my-1"></div>
                        <a href="/fr/comparateur-salaire-france-maroc/" class="flex items-center gap-2 text-sm text-indigo-600 font-medium py-1">
                            <span>🔀</span> Comparer France vs Maroc
                        </a>
                    </div>
                </div>
                <!-- Maroc Accordion -->
                <div>
                    <button onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('.chevron-icon').classList.toggle('rotate-180')" class="w-full flex items-center justify-between py-3 text-sm font-semibold text-slate-900 border-t border-slate-100">
                        <span class="flex items-center gap-2">
                            <iconify-icon icon="circle-flags:ma" width="18"></iconify-icon> Maroc
                        </span>
                        <iconify-icon icon="lucide:chevron-down" width="16" class="chevron-icon text-slate-400 transition-transform duration-200"></iconify-icon>
                    </button>
                    <div class="hidden pl-6 pb-3 space-y-2">
                        <a href="/fr/maroc/simulateur-impot-revenu/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600 py-1">
                            <iconify-icon icon="lucide:landmark" width="16" class="text-emerald-500"></iconify-icon> Simulateur Impôt
                        </a>
                        <a href="/fr/maroc/simulateur-salaire-brut-net/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600 py-1">
                            <iconify-icon icon="lucide:calculator" width="16" class="text-emerald-500"></iconify-icon> Brut vers Net
                        </a>
                        <a href="/fr/maroc/guide/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600 py-1">
                            <iconify-icon icon="lucide:book-open" width="16" class="text-emerald-500"></iconify-icon> Guide Fiscal
                        </a>
                        <div class="border-t border-slate-100 my-1"></div>
                        <a href="/fr/comparateur-salaire-france-maroc/" class="flex items-center gap-2 text-sm text-emerald-600 font-medium py-1">
                            <span>🔀</span> Comparer France vs Maroc
                        </a>
                    </div>
                </div>
                <!-- Tous les pays Accordion -->
                <div>
                    <button onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('.chevron-icon').classList.toggle('rotate-180')" class="w-full flex items-center justify-between py-3 text-sm font-semibold text-slate-900 border-t border-slate-100">
                        <span class="flex items-center gap-2">
                            <iconify-icon icon="lucide:globe" width="18"></iconify-icon> Tous les pays
                        </span>
                        <iconify-icon icon="lucide:chevron-down" width="16" class="chevron-icon text-slate-400 transition-transform duration-200"></iconify-icon>
                    </button>
                    <div class="hidden pl-4 pb-3 space-y-3">
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">⭐ Populaires</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/fr/france/simulateur-impot-revenu/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇫🇷 France</a>
                                <a href="/fr/maroc/simulateur-impot-revenu/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇲🇦 Maroc</a>
                                <a href="/fr/usa/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇺🇸 USA</a>
                                <a href="/fr/royaume-uni/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇬🇧 Royaume-Uni</a>
                                <a href="/fr/suisse/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇭 Suisse</a>
                                <a href="/fr/dubai/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇪 Dubai</a>
                            </div>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Europe</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/fr/allemagne/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇩🇪 Allemagne</a>
                                <a href="/fr/belgique/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇧🇪 Belgique</a>
                                <a href="/fr/espagne/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇪🇸 Espagne</a>
                                <a href="/fr/italie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇮🇹 Italie</a>
                                <a href="/fr/pays-bas/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇳🇱 Pays-Bas</a>
                                <a href="/fr/portugal/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇹 Portugal</a>
                                <a href="/fr/suede/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇸🇪 Suède</a>
                                <a href="/fr/norvege/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇳🇴 Norvège</a>
                                <a href="/fr/danemark/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇩🇰 Danemark</a>
                                <a href="/fr/irlande/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇮🇪 Irlande</a>
                                <a href="/fr/luxembourg/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇱🇺 Luxembourg</a>
                                <a href="/fr/autriche/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇹 Autriche</a>
                                <a href="/fr/finlande/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇫🇮 Finlande</a>
                                <a href="/fr/pologne/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇱 Pologne</a>
                                <a href="/fr/grece/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇬🇷 Grèce</a>
                                <a href="/fr/tchequie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇿 Tchéquie</a>
                                <a href="/fr/hongrie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇭🇺 Hongrie</a>
                                <a href="/fr/roumanie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇷🇴 Roumanie</a>
                                <a href="/fr/croatie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇭🇷 Croatie</a>
                            </div>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Amériques</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/fr/usa/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇺🇸 USA</a>
                                <a href="/fr/canada/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇦 Canada</a>
                                <a href="/fr/mexique/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇲🇽 Mexique</a>
                                <a href="/fr/bresil/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇧🇷 Brésil</a>
                                <a href="/fr/argentine/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇷 Argentine</a>
                                <a href="/fr/chili/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇱 Chili</a>
                                <a href="/fr/colombie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇴 Colombie</a>
                                <a href="/fr/perou/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇪 Pérou</a>
                            </div>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Asie & Moyen-Orient</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/fr/japon/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇯🇵 Japon</a>
                                <a href="/fr/chine/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇳 Chine</a>
                                <a href="/fr/coree-du-sud/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇰🇷 Corée du Sud</a>
                                <a href="/fr/inde/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇮🇳 Inde</a>
                                <a href="/fr/singapour/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇸🇬 Singapour</a>
                                <a href="/fr/hong-kong/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇭🇰 Hong Kong</a>
                                <a href="/fr/dubai/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇪 Dubai</a>
                                <a href="/fr/qatar/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇶🇦 Qatar</a>
                                <a href="/fr/koweit/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇰🇼 Koweït</a>
                                <a href="/fr/arabie-saoudite/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇸🇦 Arabie Saoudite</a>
                                <a href="/fr/turquie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇹🇷 Turquie</a>
                                <a href="/fr/indonesie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇮🇩 Indonésie</a>
                                <a href="/fr/malaisie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇲🇾 Malaisie</a>
                                <a href="/fr/pakistan/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇰 Pakistan</a>
                                <a href="/fr/thailande/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇹🇭 Thaïlande</a>
                                <a href="/fr/philippines/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇭 Philippines</a>
                                <a href="/fr/vietnam/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇻🇳 Vietnam</a>
                                <a href="/fr/egypte/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇪🇬 Égypte</a>
                            </div>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Afrique & Océanie</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/fr/afrique-du-sud/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇿🇦 Afrique du Sud</a>
                                <a href="/fr/australie/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇺 Australie</a>
                                <a href="/fr/nouvelle-zelande/simulateur-impot/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇳🇿 Nouvelle-Zélande</a>
                            </div>
                        </div>
                        <div class="border-t border-slate-100 pt-2">
                            <a href="/fr/comparateur-global/" class="flex items-center gap-2 text-sm font-medium text-indigo-600">
                                📊 Comparer tous les pays →
                            </a>
                        </div>
                    </div>
                </div>
                <!-- FAQ & other links -->
                <div class="border-t border-slate-100">
                    <a href="/fr/faq/" class="flex items-center gap-2 py-3 text-sm font-semibold text-slate-900">
                        <iconify-icon icon="lucide:help-circle" width="18"></iconify-icon> FAQ
                    </a>
                </div>
            </div>
        </div>
    </nav>'''

    return nav


def build_navbar_en(lang_dropdown_id, lang_links, is_home):
    """Build the English version of the navbar."""
    france_anchor = "#france" if is_home else "/en/#france"
    morocco_anchor = "#morocco" if is_home else "/en/#morocco"
    contact_anchor = "#contact" if is_home else "/en/#contact"
    logo_href = "/en/"

    lang_links_html = "\n                        ".join(lang_links)

    contact_btn = ""
    if is_home:
        contact_btn = f'''
                <a href="{contact_anchor}" class="hidden md:flex items-center gap-2 text-xs font-medium bg-slate-100 hover:bg-slate-200 border border-slate-200 text-slate-900 px-4 py-2 rounded-full transition-all">
                    Contact
                    <iconify-icon icon="lucide:arrow-right" width="14" stroke-width="1.5"></iconify-icon>
                </a>'''

    nav = f'''<nav class="fixed top-0 w-full z-50 border-b border-slate-200 bg-white/80 backdrop-blur-md">
        <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
            <a href="{logo_href}" class="flex items-center gap-2 group">
                <div class="w-8 h-8 bg-slate-900 rounded flex items-center justify-center text-white font-semibold tracking-tighter shadow-md group-hover:bg-indigo-600 transition-colors duration-300">
                    N.
                </div>
                <span class="font-semibold tracking-tight text-slate-900">NetSalaire</span>
            </a>
            <!-- Desktop Menu -->
            <div class="hidden md:flex items-center gap-8 text-sm font-medium text-slate-600">
                <!-- France Dropdown -->
                <div class="relative group">
                    <a href="{france_anchor}" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
                        <iconify-icon icon="circle-flags:fr" width="16"></iconify-icon> France
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </a>
                    <div class="absolute top-full left-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-lg shadow-lg py-2 min-w-[220px]">
                            <a href="/en/france/income-tax/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:landmark" width="18" class="text-indigo-500"></iconify-icon>
                                Tax Simulator
                            </a>
                            <a href="/en/france/gross-to-net/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:calculator" width="18" class="text-indigo-500"></iconify-icon>
                                Gross to Net
                            </a>
                            <a href="/en/france/tax-guide/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:book-open" width="18" class="text-indigo-500"></iconify-icon>
                                Tax Guide
                            </a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <a href="/en/france/unemployment-calculator/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">📉</span>
                                Unemployment
                            </a>
                            <a href="/en/france/severance-calculator/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">📋</span>
                                Severance
                            </a>
                            <a href="/en/france/mutual-termination-calculator/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">🤝</span>
                                Mutual Termination
                            </a>
                            <a href="/en/france/housing-benefit-calculator/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">🏠</span>
                                Housing Aid
                            </a>
                            <a href="/en/france/daycare-calculator/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">👶</span>
                                Daycare
                            </a>
                            <a href="/en/france/mileage-calculator/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">🚗</span>
                                Mileage
                            </a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <a href="/en/france-morocco-comparison/" class="flex items-center gap-3 px-4 py-2 text-indigo-600 hover:bg-indigo-50 hover:text-indigo-700 transition-colors text-sm font-medium">
                                <span class="w-[18px] text-center">🔀</span>
                                Compare France vs Morocco
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Morocco Dropdown -->
                <div class="relative group">
                    <a href="{morocco_anchor}" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
                        <iconify-icon icon="circle-flags:ma" width="16"></iconify-icon> Morocco
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </a>
                    <div class="absolute top-full left-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-lg shadow-lg py-2 min-w-[220px]">
                            <a href="/en/morocco/income-tax/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:landmark" width="18" class="text-emerald-500"></iconify-icon>
                                Tax Simulator
                            </a>
                            <a href="/en/morocco/gross-to-net/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:calculator" width="18" class="text-emerald-500"></iconify-icon>
                                Gross to Net
                            </a>
                            <a href="/en/morocco/tax-guide/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:book-open" width="18" class="text-emerald-500"></iconify-icon>
                                Tax Guide
                            </a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <a href="/en/france-morocco-comparison/" class="flex items-center gap-3 px-4 py-2 text-emerald-600 hover:bg-emerald-50 hover:text-emerald-700 transition-colors text-sm font-medium">
                                <span class="w-[18px] text-center">🔀</span>
                                Compare France vs Morocco
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Mega-menu All Countries -->
                <div class="relative group">
                    <button class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2 text-sm font-medium text-slate-600">
                        <iconify-icon icon="lucide:globe" width="16"></iconify-icon> All Countries
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </button>
                    <div class="absolute top-full right-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-xl shadow-xl mega-country-container" style="width: 600px; max-height: 75vh; overflow-y: auto;">
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mega-country-title">Europe</div>
                            <div class="grid grid-cols-2 mega-country-grid" style="column-gap: 2rem; row-gap: 0.25rem;">
                                <a href="/en/france/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇫🇷</span> France</a>
                                <a href="/en/spain/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇪🇸</span> Spain</a>
                                <a href="/en/uk/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇬🇧</span> United Kingdom</a>
                                <a href="/en/germany/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇩🇪</span> Germany</a>
                                <a href="/en/italy/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇮🇹</span> Italy</a>
                                <a href="/en/netherlands/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇳🇱</span> Netherlands</a>
                                <a href="/en/switzerland/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇭</span> Switzerland</a>
                                <a href="/en/portugal/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇹</span> Portugal</a>
                                <a href="/en/belgium/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇧🇪</span> Belgium</a>
                                <a href="/en/luxembourg/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇱🇺</span> Luxembourg</a>
                                <a href="/en/austria/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇦🇹</span> Austria</a>
                                <a href="/en/ireland/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇮🇪</span> Ireland</a>
                                <a href="/en/sweden/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇸🇪</span> Sweden</a>
                                <a href="/en/norway/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇳🇴</span> Norway</a>
                                <a href="/en/denmark/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇩🇰</span> Denmark</a>
                                <a href="/en/finland/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇫🇮</span> Finland</a>
                                <a href="/en/greece/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇬🇷</span> Greece</a>
                                <a href="/en/poland/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇱</span> Poland</a>
                                <a href="/en/czech-republic/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇿</span> Czech Republic</a>
                                <a href="/en/hungary/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇭🇺</span> Hungary</a>
                                <a href="/en/romania/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇷🇴</span> Romania</a>
                                <a href="/en/croatia/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇭🇷</span> Croatia</a>
                                <a href="/en/turkey/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇹🇷</span> Turkey</a>
                            </div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mega-country-title">Americas</div>
                            <div class="grid grid-cols-2 mega-country-grid" style="column-gap: 2rem; row-gap: 0.25rem;">
                                <a href="/en/usa/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇺🇸</span> USA</a>
                                <a href="/en/canada/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇦</span> Canada</a>
                                <a href="/en/brazil/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇧🇷</span> Brazil</a>
                                <a href="/en/mexico/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇲🇽</span> Mexico</a>
                                <a href="/en/argentina/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇦🇷</span> Argentina</a>
                                <a href="/en/chile/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇱</span> Chile</a>
                                <a href="/en/colombia/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇴</span> Colombia</a>
                                <a href="/en/peru/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇪</span> Peru</a>
                            </div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mega-country-title">Asia-Pacific</div>
                            <div class="grid grid-cols-2 mega-country-grid" style="column-gap: 2rem; row-gap: 0.25rem;">
                                <a href="/en/japan/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇯🇵</span> Japan</a>
                                <a href="/en/south-korea/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇰🇷</span> South Korea</a>
                                <a href="/en/china/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇨🇳</span> China</a>
                                <a href="/en/singapore/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇸🇬</span> Singapore</a>
                                <a href="/en/australia/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇦🇺</span> Australia</a>
                                <a href="/en/hong-kong/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇭🇰</span> Hong Kong</a>
                                <a href="/en/india/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇮🇳</span> India</a>
                                <a href="/en/new-zealand/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇳🇿</span> New Zealand</a>
                                <a href="/en/indonesia/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇮🇩</span> Indonesia</a>
                                <a href="/en/malaysia/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇲🇾</span> Malaysia</a>
                                <a href="/en/thailand/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇹🇭</span> Thailand</a>
                                <a href="/en/pakistan/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇰</span> Pakistan</a>
                                <a href="/en/philippines/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇵🇭</span> Philippines</a>
                                <a href="/en/vietnam/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇻🇳</span> Vietnam</a>
                            </div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mega-country-title">Middle East & Africa</div>
                            <div class="grid grid-cols-2 mega-country-grid" style="column-gap: 2rem; row-gap: 0.25rem;">
                                <a href="/en/morocco/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇲🇦</span> Morocco</a>
                                <a href="/en/dubai/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇦🇪</span> UAE</a>
                                <a href="/en/saudi-arabia/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇸🇦</span> Saudi Arabia</a>
                                <a href="/en/qatar/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇶🇦</span> Qatar</a>
                                <a href="/en/kuwait/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇰🇼</span> Kuwait</a>
                                <a href="/en/egypt/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇪🇬</span> Egypt</a>
                                <a href="/en/south-africa/income-tax/" class="flex items-center gap-2 px-2 py-1.5 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900 rounded-md transition-colors"><span>🇿🇦</span> South Africa</a>
                            </div>
                            <div class="border-t border-slate-100 pt-3">
                                <a href="/en/global-comparison/" class="flex items-center gap-2 text-sm font-medium text-indigo-600 hover:text-indigo-700 transition-colors">
                                    <iconify-icon icon="lucide:bar-chart-3" width="16"></iconify-icon> 📊 Compare all countries →
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <a href="/en/faq/" class="hover:text-slate-900 transition-colors">FAQ</a>
            </div>
            <div class="flex items-center gap-3">
                <!-- Language Switcher -->
                <div class="relative">
                    <button onclick="document.getElementById('{lang_dropdown_id}').classList.toggle('hidden')" class="flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-medium text-slate-600 hover:text-slate-900 bg-slate-100 hover:bg-slate-200 border border-slate-200 rounded-full transition-all" title="Switch language">
                        <span class="lang-flag">🇬🇧</span>
                        <iconify-icon icon="lucide:chevron-down" width="14"></iconify-icon>
                    </button>
                    <div id="{lang_dropdown_id}" class="hidden absolute top-full right-0 mt-2 bg-white border border-slate-200 rounded-lg shadow-lg min-w-[140px] py-1 z-50">
                        {lang_links_html}
                    </div>
                </div>{contact_btn}
                <!-- Mobile Menu Button -->
                <button onclick="document.getElementById('mobile-menu').classList.toggle('hidden')" class="md:hidden p-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-colors">
                    <iconify-icon icon="lucide:menu" width="24"></iconify-icon>
                </button>
            </div>
        </div>
        <!-- Mobile Menu (Accordions) -->
        <div id="mobile-menu" class="hidden md:hidden bg-white border-t border-slate-200">
            <div class="px-6 py-4 space-y-1">
                <!-- France Accordion -->
                <div>
                    <button onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('.chevron-icon').classList.toggle('rotate-180')" class="w-full flex items-center justify-between py-3 text-sm font-semibold text-slate-900">
                        <span class="flex items-center gap-2">
                            <iconify-icon icon="circle-flags:fr" width="18"></iconify-icon> France
                        </span>
                        <iconify-icon icon="lucide:chevron-down" width="16" class="chevron-icon text-slate-400 transition-transform duration-200"></iconify-icon>
                    </button>
                    <div class="hidden pl-6 pb-3 space-y-2">
                        <a href="/en/france/income-tax/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <iconify-icon icon="lucide:landmark" width="16" class="text-indigo-500"></iconify-icon> Tax Simulator
                        </a>
                        <a href="/en/france/gross-to-net/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <iconify-icon icon="lucide:calculator" width="16" class="text-indigo-500"></iconify-icon> Gross to Net
                        </a>
                        <a href="/en/france/tax-guide/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <iconify-icon icon="lucide:book-open" width="16" class="text-indigo-500"></iconify-icon> Tax Guide
                        </a>
                        <a href="/en/france/unemployment-calculator/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>📉</span> Unemployment
                        </a>
                        <a href="/en/france/severance-calculator/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>📋</span> Severance
                        </a>
                        <a href="/en/france/mutual-termination-calculator/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>🤝</span> Mutual Termination
                        </a>
                        <a href="/en/france/housing-benefit-calculator/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>🏠</span> Housing Aid
                        </a>
                        <a href="/en/france/daycare-calculator/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>👶</span> Daycare
                        </a>
                        <a href="/en/france/mileage-calculator/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600 py-1">
                            <span>🚗</span> Mileage
                        </a>
                        <div class="border-t border-slate-100 my-1"></div>
                        <a href="/en/france-morocco-comparison/" class="flex items-center gap-2 text-sm text-indigo-600 font-medium py-1">
                            <span>🔀</span> Compare France vs Morocco
                        </a>
                    </div>
                </div>
                <!-- Morocco Accordion -->
                <div>
                    <button onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('.chevron-icon').classList.toggle('rotate-180')" class="w-full flex items-center justify-between py-3 text-sm font-semibold text-slate-900 border-t border-slate-100">
                        <span class="flex items-center gap-2">
                            <iconify-icon icon="circle-flags:ma" width="18"></iconify-icon> Morocco
                        </span>
                        <iconify-icon icon="lucide:chevron-down" width="16" class="chevron-icon text-slate-400 transition-transform duration-200"></iconify-icon>
                    </button>
                    <div class="hidden pl-6 pb-3 space-y-2">
                        <a href="/en/morocco/income-tax/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600 py-1">
                            <iconify-icon icon="lucide:landmark" width="16" class="text-emerald-500"></iconify-icon> Tax Simulator
                        </a>
                        <a href="/en/morocco/gross-to-net/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600 py-1">
                            <iconify-icon icon="lucide:calculator" width="16" class="text-emerald-500"></iconify-icon> Gross to Net
                        </a>
                        <a href="/en/morocco/tax-guide/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600 py-1">
                            <iconify-icon icon="lucide:book-open" width="16" class="text-emerald-500"></iconify-icon> Tax Guide
                        </a>
                        <div class="border-t border-slate-100 my-1"></div>
                        <a href="/en/france-morocco-comparison/" class="flex items-center gap-2 text-sm text-emerald-600 font-medium py-1">
                            <span>🔀</span> Compare France vs Morocco
                        </a>
                    </div>
                </div>
                <!-- All Countries Accordion -->
                <div>
                    <button onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('.chevron-icon').classList.toggle('rotate-180')" class="w-full flex items-center justify-between py-3 text-sm font-semibold text-slate-900 border-t border-slate-100">
                        <span class="flex items-center gap-2">
                            <iconify-icon icon="lucide:globe" width="18"></iconify-icon> All Countries
                        </span>
                        <iconify-icon icon="lucide:chevron-down" width="16" class="chevron-icon text-slate-400 transition-transform duration-200"></iconify-icon>
                    </button>
                    <div class="hidden pl-4 pb-3 space-y-3">
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">⭐ Popular</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/en/france/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇫🇷 France</a>
                                <a href="/en/morocco/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇲🇦 Morocco</a>
                                <a href="/en/usa/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇺🇸 USA</a>
                                <a href="/en/uk/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇬🇧 United Kingdom</a>
                                <a href="/en/switzerland/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇭 Switzerland</a>
                                <a href="/en/dubai/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇪 Dubai</a>
                            </div>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Europe</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/en/germany/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇩🇪 Germany</a>
                                <a href="/en/belgium/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇧🇪 Belgium</a>
                                <a href="/en/spain/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇪🇸 Spain</a>
                                <a href="/en/italy/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇮🇹 Italy</a>
                                <a href="/en/netherlands/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇳🇱 Netherlands</a>
                                <a href="/en/portugal/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇹 Portugal</a>
                                <a href="/en/sweden/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇸🇪 Sweden</a>
                                <a href="/en/norway/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇳🇴 Norway</a>
                                <a href="/en/denmark/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇩🇰 Denmark</a>
                                <a href="/en/ireland/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇮🇪 Ireland</a>
                                <a href="/en/luxembourg/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇱🇺 Luxembourg</a>
                                <a href="/en/austria/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇹 Austria</a>
                                <a href="/en/finland/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇫🇮 Finland</a>
                                <a href="/en/poland/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇱 Poland</a>
                                <a href="/en/greece/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇬🇷 Greece</a>
                                <a href="/en/czech-republic/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇿 Czech Republic</a>
                                <a href="/en/hungary/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇭🇺 Hungary</a>
                                <a href="/en/romania/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇷🇴 Romania</a>
                                <a href="/en/croatia/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇭🇷 Croatia</a>
                            </div>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Americas</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/en/usa/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇺🇸 USA</a>
                                <a href="/en/canada/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇦 Canada</a>
                                <a href="/en/mexico/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇲🇽 Mexico</a>
                                <a href="/en/brazil/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇧🇷 Brazil</a>
                                <a href="/en/argentina/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇷 Argentina</a>
                                <a href="/en/chile/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇱 Chile</a>
                                <a href="/en/colombia/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇴 Colombia</a>
                                <a href="/en/peru/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇪 Peru</a>
                            </div>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Asia & Middle East</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/en/japan/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇯🇵 Japan</a>
                                <a href="/en/china/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇨🇳 China</a>
                                <a href="/en/south-korea/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇰🇷 South Korea</a>
                                <a href="/en/india/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇮🇳 India</a>
                                <a href="/en/singapore/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇸🇬 Singapore</a>
                                <a href="/en/hong-kong/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇭🇰 Hong Kong</a>
                                <a href="/en/dubai/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇪 Dubai</a>
                                <a href="/en/qatar/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇶🇦 Qatar</a>
                                <a href="/en/kuwait/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇰🇼 Kuwait</a>
                                <a href="/en/saudi-arabia/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇸🇦 Saudi Arabia</a>
                                <a href="/en/turkey/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇹🇷 Turkey</a>
                                <a href="/en/indonesia/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇮🇩 Indonesia</a>
                                <a href="/en/malaysia/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇲🇾 Malaysia</a>
                                <a href="/en/pakistan/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇰 Pakistan</a>
                                <a href="/en/thailand/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇹🇭 Thailand</a>
                                <a href="/en/philippines/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇵🇭 Philippines</a>
                                <a href="/en/vietnam/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇻🇳 Vietnam</a>
                                <a href="/en/egypt/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇪🇬 Egypt</a>
                            </div>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Africa & Oceania</div>
                            <div class="grid grid-cols-2 gap-1 mega-country-grid">
                                <a href="/en/south-africa/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇿🇦 South Africa</a>
                                <a href="/en/australia/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇦🇺 Australia</a>
                                <a href="/en/new-zealand/income-tax/" class="text-sm text-slate-600 hover:text-slate-900 py-1">🇳🇿 New Zealand</a>
                            </div>
                        </div>
                        <div class="border-t border-slate-100 pt-2">
                            <a href="/en/global-comparison/" class="flex items-center gap-2 text-sm font-medium text-indigo-600">
                                📊 Compare all countries →
                            </a>
                        </div>
                    </div>
                </div>
                <!-- FAQ & other links -->
                <div class="border-t border-slate-100">
                    <a href="/en/faq/" class="flex items-center gap-2 py-3 text-sm font-semibold text-slate-900">
                        <iconify-icon icon="lucide:help-circle" width="18"></iconify-icon> FAQ
                    </a>
                </div>
            </div>
        </div>
    </nav>'''

    return nav


def find_html_files():
    """Find all HTML files under fr/ and en/ directories."""
    files = []
    for lang_dir in ['fr', 'en']:
        pattern = os.path.join(BASE_DIR, lang_dir, '**', 'index.html')
        files.extend(glob.glob(pattern, recursive=True))
    # Also add the root-level index.html for fr/ and en/
    for lang_dir in ['fr', 'en']:
        root_file = os.path.join(BASE_DIR, lang_dir, 'index.html')
        if root_file not in files and os.path.exists(root_file):
            files.append(root_file)
    return sorted(set(files))


def process_file(filepath):
    """Process a single HTML file: replace its <nav> with the new navbar."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the nav block using regex
    # Match from <nav class="fixed to the closing </nav>
    nav_pattern = r'<nav\s+class="fixed[^"]*"[^>]*>.*?</nav>'
    nav_match = re.search(nav_pattern, content, re.DOTALL)

    if not nav_match:
        print(f"  SKIP (no nav found): {filepath}")
        return False

    old_nav = nav_match.group(0)

    # Extract language switcher links
    lang_links = extract_lang_switcher_links(old_nav)
    if not lang_links:
        print(f"  WARN (no lang links found): {filepath}")
        # Provide fallback lang links
        lang = detect_language(filepath)
        if lang == 'fr':
            lang_links = [
                '<a href="/fr/" class="w-full flex items-center gap-2 px-3 py-2 text-sm text-slate-700 bg-slate-50 transition-colors">\n                            <span>🇫🇷</span> Français\n                        </a>',
                '<a href="/en/" class="w-full flex items-center gap-2 px-3 py-2 text-sm text-slate-700 hover:bg-slate-50 transition-colors">\n                            <span>🇬🇧</span> English\n                        </a>'
            ]
        else:
            lang_links = [
                '<a href="/fr/" class="w-full flex items-center gap-2 px-3 py-2 text-sm text-slate-700 hover:bg-slate-50 transition-colors">\n                            <span>🇫🇷</span> Francais\n                        </a>',
                '<a href="/en/" class="w-full flex items-center gap-2 px-3 py-2 text-sm text-slate-700 bg-slate-50 transition-colors">\n                            <span>🇬🇧</span> English\n                        </a>'
            ]

    # Detect lang dropdown ID and language
    lang_dropdown_id = detect_lang_dropdown_id(old_nav)
    lang = detect_language(filepath)
    is_home = is_homepage(filepath)

    # Build new navbar
    new_nav = build_navbar(lang, lang_dropdown_id, lang_links, is_home)

    # Replace old nav with new nav
    new_content = content[:nav_match.start()] + new_nav + content[nav_match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    files = find_html_files()
    print(f"Found {len(files)} HTML files to process.\n")

    success = 0
    skipped = 0

    for filepath in files:
        rel = os.path.relpath(filepath, BASE_DIR)
        if process_file(filepath):
            print(f"  OK: {rel}")
            success += 1
        else:
            skipped += 1

    print(f"\nDone! Processed: {success}, Skipped: {skipped}")


if __name__ == '__main__':
    main()
