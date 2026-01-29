#!/usr/bin/env python3
"""Update navigation on all country pages to match homepage"""

import os
import re
from pathlib import Path

BASE_PATH = '/Users/motta/Documents/GitHub/impotsfrancemaroc'

# FR Navigation (from homepage)
NAV_FR = '''    <!-- Navbar -->
    <nav class="fixed top-0 w-full z-50 border-b border-slate-200 bg-white/80 backdrop-blur-md">
        <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
            <a href="/fr/" class="flex items-center gap-2 group">
                <div class="w-8 h-8 bg-slate-900 rounded flex items-center justify-center text-white font-semibold tracking-tighter shadow-md group-hover:bg-indigo-600 transition-colors duration-300">
                    N.
                </div>
                <span class="font-semibold tracking-tight text-slate-900">NetSalaire</span>
            </a>
            <!-- Desktop Menu -->
            <div class="hidden md:flex items-center gap-8 text-sm font-medium text-slate-600">
                <!-- France Dropdown -->
                <div class="relative group">
                    <a href="/fr/#france" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
                        <iconify-icon icon="circle-flags:fr" width="16"></iconify-icon> France
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </a>
                    <div class="absolute top-full left-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-lg shadow-lg py-2 min-w-[220px]">
                            <a href="/fr/france/simulateur-impot-revenu/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:landmark" width="18" class="text-indigo-500"></iconify-icon>
                                Simulateur Impot
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
                                <span class="w-[18px] text-center">📉</span> Chomage ARE
                            </a>
                            <a href="/fr/france/simulateur-indemnite-licenciement/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">📋</span> Licenciement
                            </a>
                            <a href="/fr/france/simulateur-apl/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">🏠</span> APL
                            </a>
                            <a href="/fr/france/creche-tarifs/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">👶</span> Creche
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Maroc Dropdown -->
                <div class="relative group">
                    <a href="/fr/#maroc" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
                        <iconify-icon icon="circle-flags:ma" width="16"></iconify-icon> Maroc
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </a>
                    <div class="absolute top-full left-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-lg shadow-lg py-2 min-w-[220px]">
                            <a href="/fr/maroc/simulateur-impot-revenu/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:landmark" width="18" class="text-emerald-500"></iconify-icon>
                                Simulateur Impot
                            </a>
                            <a href="/fr/maroc/simulateur-salaire-brut-net/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:calculator" width="18" class="text-emerald-500"></iconify-icon>
                                Brut vers Net
                            </a>
                            <a href="/fr/maroc/guide/" class="flex items-center gap-3 px-4 py-2.5 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors">
                                <iconify-icon icon="lucide:book-open" width="18" class="text-emerald-500"></iconify-icon>
                                Guide Fiscal
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Autres Pays Dropdown -->
                <div class="relative group">
                    <a href="/fr/comparateur-global/" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
                        <iconify-icon icon="lucide:globe" width="16"></iconify-icon> Autres Pays
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </a>
                    <div class="absolute top-full left-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-lg shadow-lg py-2 min-w-[200px] max-h-[400px] overflow-y-auto">
                            <a href="/fr/usa/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇺🇸</span> USA (New York)
                            </a>
                            <a href="/fr/royaume-uni/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇬🇧</span> Royaume-Uni
                            </a>
                            <a href="/fr/suisse/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇨🇭</span> Suisse (Geneve)
                            </a>
                            <a href="/fr/dubai/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇦🇪</span> Dubai (0% impot)
                            </a>
                            <a href="/fr/singapour/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇸🇬</span> Singapour
                            </a>
                            <a href="/fr/luxembourg/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇱🇺</span> Luxembourg
                            </a>
                            <a href="/fr/arabie-saoudite/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇸🇦</span> Arabie Saoudite
                            </a>
                            <a href="/fr/espagne/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇪🇸</span> Espagne
                            </a>
                            <a href="/fr/japon/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇯🇵</span> Japon
                            </a>
                            <a href="/fr/chine/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇨🇳</span> Chine (Shanghai)
                            </a>
                            <a href="/fr/inde/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇮🇳</span> Inde
                            </a>
                            <a href="/fr/pakistan/simulateur-impot/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇵🇰</span> Pakistan
                            </a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <a href="/fr/comparateur-global/" class="flex items-center gap-3 px-4 py-2 text-indigo-600 hover:bg-indigo-50 hover:text-indigo-700 transition-colors text-sm font-medium">
                                <iconify-icon icon="lucide:bar-chart-3" width="16"></iconify-icon> Comparer tous
                            </a>
                        </div>
                    </div>
                </div>
                <a href="/fr/comparateur-salaire-france-maroc/" class="hover:text-slate-900 transition-colors">France vs Maroc</a>
                <a href="/fr/faq/" class="hover:text-slate-900 transition-colors">FAQ</a>
            </div>
            <div class="flex items-center gap-3">
                <!-- Language Switcher -->
                <div class="relative">
                    <button onclick="document.getElementById('lang-dropdown-page').classList.toggle('hidden')" class="flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-medium text-slate-600 hover:text-slate-900 bg-slate-100 hover:bg-slate-200 border border-slate-200 rounded-full transition-all">
                        <span>🇫🇷</span>
                        <iconify-icon icon="lucide:chevron-down" width="14"></iconify-icon>
                    </button>
                    <div id="lang-dropdown-page" class="hidden absolute top-full right-0 mt-2 bg-white border border-slate-200 rounded-lg shadow-lg min-w-[140px] py-1 z-50">
                        <a href="LANG_LINK_FR" class="w-full flex items-center gap-2 px-3 py-2 text-sm text-slate-700 bg-slate-50 transition-colors">
                            <span>🇫🇷</span> Francais
                        </a>
                        <a href="LANG_LINK_EN" class="w-full flex items-center gap-2 px-3 py-2 text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                            <span>🇬🇧</span> English
                        </a>
                    </div>
                </div>
                <!-- Mobile Menu Button -->
                <button onclick="document.getElementById('mobile-menu').classList.toggle('hidden')" class="md:hidden p-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-colors">
                    <iconify-icon icon="lucide:menu" width="24"></iconify-icon>
                </button>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden bg-white border-t border-slate-200">
            <div class="px-6 py-4 space-y-4">
                <div class="space-y-2">
                    <div class="flex items-center gap-2 text-sm font-semibold text-slate-900">
                        <iconify-icon icon="circle-flags:fr" width="18"></iconify-icon> France
                    </div>
                    <div class="pl-6 space-y-2">
                        <a href="/fr/france/simulateur-impot-revenu/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600">
                            <iconify-icon icon="lucide:landmark" width="16" class="text-indigo-500"></iconify-icon> Simulateur Impot
                        </a>
                        <a href="/fr/france/simulateur-salaire-brut-net/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600">
                            <iconify-icon icon="lucide:calculator" width="16" class="text-indigo-500"></iconify-icon> Brut vers Net
                        </a>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex items-center gap-2 text-sm font-semibold text-slate-900">
                        <iconify-icon icon="circle-flags:ma" width="18"></iconify-icon> Maroc
                    </div>
                    <div class="pl-6 space-y-2">
                        <a href="/fr/maroc/simulateur-impot-revenu/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600">
                            <iconify-icon icon="lucide:landmark" width="16" class="text-emerald-500"></iconify-icon> Simulateur Impot
                        </a>
                        <a href="/fr/maroc/simulateur-salaire-brut-net/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600">
                            <iconify-icon icon="lucide:calculator" width="16" class="text-emerald-500"></iconify-icon> Brut vers Net
                        </a>
                    </div>
                </div>
                <div class="pt-2 border-t border-slate-100 space-y-2">
                    <a href="/fr/comparateur-global/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-slate-900">
                        <iconify-icon icon="lucide:globe" width="16"></iconify-icon> Autres Pays
                    </a>
                    <a href="/fr/comparateur-salaire-france-maroc/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-slate-900">
                        <iconify-icon icon="lucide:scale" width="16"></iconify-icon> France vs Maroc
                    </a>
                    <a href="/fr/faq/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-slate-900">
                        <iconify-icon icon="lucide:help-circle" width="16"></iconify-icon> FAQ
                    </a>
                </div>
            </div>
        </div>
    </nav>'''

# EN Navigation
NAV_EN = '''    <!-- Navbar -->
    <nav class="fixed top-0 w-full z-50 border-b border-slate-200 bg-white/80 backdrop-blur-md">
        <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
            <a href="/en/" class="flex items-center gap-2 group">
                <div class="w-8 h-8 bg-slate-900 rounded flex items-center justify-center text-white font-semibold tracking-tighter shadow-md group-hover:bg-indigo-600 transition-colors duration-300">
                    N.
                </div>
                <span class="font-semibold tracking-tight text-slate-900">NetSalaire</span>
            </a>
            <!-- Desktop Menu -->
            <div class="hidden md:flex items-center gap-8 text-sm font-medium text-slate-600">
                <!-- France Dropdown -->
                <div class="relative group">
                    <a href="/en/#france" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
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
                                <span class="w-[18px] text-center">📉</span> Unemployment
                            </a>
                            <a href="/en/france/severance-calculator/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">📋</span> Severance
                            </a>
                            <a href="/en/france/housing-benefit-calculator/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">🏠</span> Housing Aid
                            </a>
                            <a href="/en/france/daycare-calculator/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span class="w-[18px] text-center">👶</span> Daycare
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Morocco Dropdown -->
                <div class="relative group">
                    <a href="/en/#morocco" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
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
                        </div>
                    </div>
                </div>
                <!-- Other Countries Dropdown -->
                <div class="relative group">
                    <a href="/en/global-comparison/" class="hover:text-slate-900 transition-colors flex items-center gap-1.5 py-2">
                        <iconify-icon icon="lucide:globe" width="16"></iconify-icon> Other Countries
                        <iconify-icon icon="lucide:chevron-down" width="14" class="text-slate-400 group-hover:text-slate-600 transition-transform group-hover:rotate-180"></iconify-icon>
                    </a>
                    <div class="absolute top-full left-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                        <div class="bg-white border border-slate-200 rounded-lg shadow-lg py-2 min-w-[200px] max-h-[400px] overflow-y-auto">
                            <a href="/en/usa/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇺🇸</span> USA (New York)
                            </a>
                            <a href="/en/uk/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇬🇧</span> United Kingdom
                            </a>
                            <a href="/en/switzerland/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇨🇭</span> Switzerland (Geneva)
                            </a>
                            <a href="/en/dubai/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇦🇪</span> Dubai (0% tax)
                            </a>
                            <a href="/en/singapore/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇸🇬</span> Singapore
                            </a>
                            <a href="/en/luxembourg/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇱🇺</span> Luxembourg
                            </a>
                            <a href="/en/saudi-arabia/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇸🇦</span> Saudi Arabia
                            </a>
                            <a href="/en/spain/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇪🇸</span> Spain
                            </a>
                            <a href="/en/japan/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇯🇵</span> Japan
                            </a>
                            <a href="/en/china/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇨🇳</span> China (Shanghai)
                            </a>
                            <a href="/en/india/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇮🇳</span> India
                            </a>
                            <a href="/en/pakistan/income-tax/" class="flex items-center gap-3 px-4 py-2 text-slate-600 hover:bg-slate-50 hover:text-slate-900 transition-colors text-sm">
                                <span>🇵🇰</span> Pakistan
                            </a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <a href="/en/global-comparison/" class="flex items-center gap-3 px-4 py-2 text-indigo-600 hover:bg-indigo-50 hover:text-indigo-700 transition-colors text-sm font-medium">
                                <iconify-icon icon="lucide:bar-chart-3" width="16"></iconify-icon> Compare all
                            </a>
                        </div>
                    </div>
                </div>
                <a href="/en/france-morocco-comparison/" class="hover:text-slate-900 transition-colors">France vs Morocco</a>
                <a href="/en/faq/" class="hover:text-slate-900 transition-colors">FAQ</a>
            </div>
            <div class="flex items-center gap-3">
                <!-- Language Switcher -->
                <div class="relative">
                    <button onclick="document.getElementById('lang-dropdown-page').classList.toggle('hidden')" class="flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-medium text-slate-600 hover:text-slate-900 bg-slate-100 hover:bg-slate-200 border border-slate-200 rounded-full transition-all">
                        <span>🇬🇧</span>
                        <iconify-icon icon="lucide:chevron-down" width="14"></iconify-icon>
                    </button>
                    <div id="lang-dropdown-page" class="hidden absolute top-full right-0 mt-2 bg-white border border-slate-200 rounded-lg shadow-lg min-w-[140px] py-1 z-50">
                        <a href="LANG_LINK_FR" class="w-full flex items-center gap-2 px-3 py-2 text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                            <span>🇫🇷</span> Francais
                        </a>
                        <a href="LANG_LINK_EN" class="w-full flex items-center gap-2 px-3 py-2 text-sm text-slate-700 bg-slate-50 transition-colors">
                            <span>🇬🇧</span> English
                        </a>
                    </div>
                </div>
                <!-- Mobile Menu Button -->
                <button onclick="document.getElementById('mobile-menu').classList.toggle('hidden')" class="md:hidden p-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-colors">
                    <iconify-icon icon="lucide:menu" width="24"></iconify-icon>
                </button>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden bg-white border-t border-slate-200">
            <div class="px-6 py-4 space-y-4">
                <div class="space-y-2">
                    <div class="flex items-center gap-2 text-sm font-semibold text-slate-900">
                        <iconify-icon icon="circle-flags:fr" width="18"></iconify-icon> France
                    </div>
                    <div class="pl-6 space-y-2">
                        <a href="/en/france/income-tax/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600">
                            <iconify-icon icon="lucide:landmark" width="16" class="text-indigo-500"></iconify-icon> Tax Simulator
                        </a>
                        <a href="/en/france/gross-to-net/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-indigo-600">
                            <iconify-icon icon="lucide:calculator" width="16" class="text-indigo-500"></iconify-icon> Gross to Net
                        </a>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex items-center gap-2 text-sm font-semibold text-slate-900">
                        <iconify-icon icon="circle-flags:ma" width="18"></iconify-icon> Morocco
                    </div>
                    <div class="pl-6 space-y-2">
                        <a href="/en/morocco/income-tax/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600">
                            <iconify-icon icon="lucide:landmark" width="16" class="text-emerald-500"></iconify-icon> Tax Simulator
                        </a>
                        <a href="/en/morocco/gross-to-net/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-emerald-600">
                            <iconify-icon icon="lucide:calculator" width="16" class="text-emerald-500"></iconify-icon> Gross to Net
                        </a>
                    </div>
                </div>
                <div class="pt-2 border-t border-slate-100 space-y-2">
                    <a href="/en/global-comparison/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-slate-900">
                        <iconify-icon icon="lucide:globe" width="16"></iconify-icon> Other Countries
                    </a>
                    <a href="/en/france-morocco-comparison/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-slate-900">
                        <iconify-icon icon="lucide:scale" width="16"></iconify-icon> France vs Morocco
                    </a>
                    <a href="/en/faq/" class="flex items-center gap-2 text-sm text-slate-600 hover:text-slate-900">
                        <iconify-icon icon="lucide:help-circle" width="16"></iconify-icon> FAQ
                    </a>
                </div>
            </div>
        </div>
    </nav>'''

# Language mapping for each country page
COUNTRY_LANG_LINKS = {
    'usa': {'fr': '/fr/usa/simulateur-impot/', 'en': '/en/usa/income-tax/'},
    'royaume-uni': {'fr': '/fr/royaume-uni/simulateur-impot/', 'en': '/en/uk/income-tax/'},
    'uk': {'fr': '/fr/royaume-uni/simulateur-impot/', 'en': '/en/uk/income-tax/'},
    'suisse': {'fr': '/fr/suisse/simulateur-impot/', 'en': '/en/switzerland/income-tax/'},
    'switzerland': {'fr': '/fr/suisse/simulateur-impot/', 'en': '/en/switzerland/income-tax/'},
    'dubai': {'fr': '/fr/dubai/simulateur-impot/', 'en': '/en/dubai/income-tax/'},
    'singapour': {'fr': '/fr/singapour/simulateur-impot/', 'en': '/en/singapore/income-tax/'},
    'singapore': {'fr': '/fr/singapour/simulateur-impot/', 'en': '/en/singapore/income-tax/'},
    'luxembourg': {'fr': '/fr/luxembourg/simulateur-impot/', 'en': '/en/luxembourg/income-tax/'},
    'arabie-saoudite': {'fr': '/fr/arabie-saoudite/simulateur-impot/', 'en': '/en/saudi-arabia/income-tax/'},
    'saudi-arabia': {'fr': '/fr/arabie-saoudite/simulateur-impot/', 'en': '/en/saudi-arabia/income-tax/'},
    'espagne': {'fr': '/fr/espagne/simulateur-impot/', 'en': '/en/spain/income-tax/'},
    'spain': {'fr': '/fr/espagne/simulateur-impot/', 'en': '/en/spain/income-tax/'},
    'japon': {'fr': '/fr/japon/simulateur-impot/', 'en': '/en/japan/income-tax/'},
    'japan': {'fr': '/fr/japon/simulateur-impot/', 'en': '/en/japan/income-tax/'},
    'chine': {'fr': '/fr/chine/simulateur-impot/', 'en': '/en/china/income-tax/'},
    'china': {'fr': '/fr/chine/simulateur-impot/', 'en': '/en/china/income-tax/'},
    'inde': {'fr': '/fr/inde/simulateur-impot/', 'en': '/en/india/income-tax/'},
    'india': {'fr': '/fr/inde/simulateur-impot/', 'en': '/en/india/income-tax/'},
    'pakistan': {'fr': '/fr/pakistan/simulateur-impot/', 'en': '/en/pakistan/income-tax/'},
}

def get_country_from_path(filepath):
    """Extract country code from file path"""
    parts = filepath.split('/')
    for i, part in enumerate(parts):
        if part in ['fr', 'en'] and i + 1 < len(parts):
            return parts[i + 1]
    return None

def update_file(filepath, is_fr):
    """Update a single file with the new navigation"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Get the country code
        country = get_country_from_path(filepath)
        if not country or country not in COUNTRY_LANG_LINKS:
            print(f"  Skipped (unknown country): {filepath}")
            return False

        lang_links = COUNTRY_LANG_LINKS[country]

        # Choose the right navigation template
        nav = NAV_FR if is_fr else NAV_EN
        nav = nav.replace('LANG_LINK_FR', lang_links['fr'])
        nav = nav.replace('LANG_LINK_EN', lang_links['en'])

        # Replace the navigation section
        # Match from <nav to </nav>
        pattern = r'<nav\s+class="fixed[^>]*>.*?</nav>'

        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, nav.strip(), content, flags=re.DOTALL)

            # Also remove any <!-- Navigation --> comment before nav
            new_content = re.sub(r'\s*<!-- Navigation -->\s*', '\n\n', new_content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        else:
            print(f"  No nav found: {filepath}")
            return False

    except Exception as e:
        print(f"  Error: {filepath} - {e}")
        return False

def main():
    updated = 0

    # Update FR country pages
    print("Updating FR pages...")
    fr_dirs = ['usa', 'royaume-uni', 'suisse', 'dubai', 'singapour', 'luxembourg',
               'arabie-saoudite', 'espagne', 'japon', 'chine', 'inde', 'pakistan']
    for country in fr_dirs:
        filepath = f"{BASE_PATH}/fr/{country}/simulateur-impot/index.html"
        if os.path.exists(filepath):
            if update_file(filepath, is_fr=True):
                print(f"  Updated: {filepath}")
                updated += 1

    # Update EN country pages
    print("\nUpdating EN pages...")
    en_dirs = ['usa', 'uk', 'switzerland', 'dubai', 'singapore', 'luxembourg',
               'saudi-arabia', 'spain', 'japan', 'china', 'india', 'pakistan']
    for country in en_dirs:
        filepath = f"{BASE_PATH}/en/{country}/income-tax/index.html"
        if os.path.exists(filepath):
            if update_file(filepath, is_fr=False):
                print(f"  Updated: {filepath}")
                updated += 1

    print(f"\nTotal updated: {updated}")

if __name__ == '__main__':
    main()
