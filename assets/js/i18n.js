/**
 * NetSalaire - Internationalization (i18n) System
 * Supports: French (fr), English (en)
 */

const translations = {
    // ==========================================
    // COMMON / NAVIGATION
    // ==========================================
    'nav.france_vs_maroc': {
        fr: 'France vs Maroc',
        en: 'France vs Morocco'
    },
    'nav.global_comparator': {
        fr: 'Comparateur Global',
        en: 'Global Comparator'
    },
    'nav.france': {
        fr: 'France',
        en: 'France'
    },
    'nav.maroc': {
        fr: 'Maroc',
        en: 'Morocco'
    },
    'nav.faq': {
        fr: 'FAQ',
        en: 'FAQ'
    },
    'nav.contact': {
        fr: 'Contact',
        en: 'Contact'
    },
    'nav.brut_to_net': {
        fr: 'Brut vers Net',
        en: 'Gross to Net'
    },
    'nav.tax_simulator': {
        fr: 'Simulateur Impot',
        en: 'Tax Simulator'
    },
    'nav.fiscal_guide': {
        fr: 'Guide Fiscal',
        en: 'Tax Guide'
    },
    'nav.comparator': {
        fr: 'Comparateur',
        en: 'Comparator'
    },

    // ==========================================
    // HOMEPAGE
    // ==========================================
    'home.badge': {
        fr: 'Baremes fiscaux 2025',
        en: 'Tax rates 2025'
    },
    'home.title1': {
        fr: 'Calculez votre',
        en: 'Calculate your'
    },
    'home.title2': {
        fr: 'salaire net en 2 clics.',
        en: 'net salary in 2 clicks.'
    },
    'home.subtitle': {
        fr: 'Simulateurs fiscaux gratuits pour la France et le Maroc. Calculez salaires, impots et comparez la pression fiscale entre les deux pays.',
        en: 'Free tax simulators for France and Morocco. Calculate salaries, taxes and compare the tax burden between the two countries.'
    },
    'home.compare_btn': {
        fr: 'Comparer France vs Maroc',
        en: 'Compare France vs Morocco'
    },
    'home.france_tools': {
        fr: 'Outils dedies a la legislation francaise',
        en: 'Tools dedicated to French legislation'
    },
    'home.maroc_tools': {
        fr: 'Fiscalite et prelevement a la source',
        en: 'Taxation and withholding tax'
    },
    'home.brut_net_title': {
        fr: 'Salaire Brut a Net',
        en: 'Gross to Net Salary'
    },
    'home.brut_net_desc': {
        fr: 'Calcul precis du salaire net avant et apres impot. Prise en charge des statuts cadre et non-cadre.',
        en: 'Precise calculation of net salary before and after tax. Support for executive and non-executive status.'
    },
    'home.ir_simulator_title': {
        fr: 'Simulateur Impot sur le Revenu',
        en: 'Income Tax Simulator'
    },
    'home.ir_simulator_desc_fr': {
        fr: 'Estimation avec bareme progressif, quotient familial et decotes en vigueur.',
        en: 'Estimate with progressive scale, family quotient and applicable rebates.'
    },
    'home.ir_simulator_desc_ma': {
        fr: 'Calcul complet avec CNSS, AMO, frais professionnels et abattement familial. Baremes 2025.',
        en: 'Complete calculation with CNSS, AMO, professional expenses and family allowance. 2025 rates.'
    },
    'home.guide_title_fr': {
        fr: 'Guide Fiscal France 2025',
        en: 'France Tax Guide 2025'
    },
    'home.guide_desc_fr': {
        fr: 'Tout comprendre sur la fiscalite francaise : cotisations sociales, quotient familial, tranches IR, optimisation fiscale.',
        en: 'Understand everything about French taxation: social contributions, family quotient, tax brackets, tax optimization.'
    },
    'home.guide_title_ma': {
        fr: 'Guide Fiscal Maroc 2025',
        en: 'Morocco Tax Guide 2025'
    },
    'home.guide_desc_ma': {
        fr: 'Tout comprendre sur la fiscalite marocaine : CNSS, AMO, tranches IR, abattements.',
        en: 'Understand everything about Moroccan taxation: CNSS, AMO, tax brackets, allowances.'
    },
    'home.comparators_title': {
        fr: 'Comparateurs Internationaux',
        en: 'International Comparators'
    },
    'home.comparators_subtitle': {
        fr: 'Analyse croisee des regimes fiscaux',
        en: 'Cross-analysis of tax systems'
    },
    'home.compare_fr_ma_desc': {
        fr: 'Comparaison detaillee entre la France et le Maroc. Cotisations, IR, quotient familial.',
        en: 'Detailed comparison between France and Morocco. Contributions, income tax, family quotient.'
    },
    'home.compare_btn_short': {
        fr: 'Comparer',
        en: 'Compare'
    },
    'home.global_comp_desc': {
        fr: 'Comparez 5 pays : France, Maroc, Dubai, Geneve et Luxembourg. Trouvez le meilleur net !',
        en: 'Compare 5 countries: France, Morocco, Dubai, Geneva and Luxembourg. Find the best net!'
    },
    'home.launch_comparator': {
        fr: 'Lancer le comparateur',
        en: 'Launch comparator'
    },

    // FAQ Section
    'faq.title': {
        fr: 'Questions Frequentes',
        en: 'Frequently Asked Questions'
    },
    'faq.q1': {
        fr: 'Comment fonctionne le comparateur pays ?',
        en: 'How does the country comparator work?'
    },
    'faq.a1': {
        fr: 'Le comparateur calcule simultanement votre salaire net et votre pression fiscale totale dans les deux pays, pour un meme salaire brut. Il utilise le taux de change en temps reel pour convertir les montants.',
        en: 'The comparator simultaneously calculates your net salary and total tax burden in both countries, for the same gross salary. It uses real-time exchange rates to convert amounts.'
    },
    'faq.q2': {
        fr: 'Les calculs sont-ils fiables ?',
        en: 'Are the calculations reliable?'
    },
    'faq.a2': {
        fr: 'Nos simulateurs utilisent les baremes officiels 2025 publies par les administrations fiscales francaise et marocaine. Cependant, ils fournissent une estimation et ne remplacent pas un conseil fiscal personnalise.',
        en: 'Our simulators use the official 2025 rates published by the French and Moroccan tax authorities. However, they provide an estimate and do not replace personalized tax advice.'
    },
    'faq.q3': {
        fr: 'Puis-je simuler un statut cadre en France ?',
        en: 'Can I simulate executive status in France?'
    },
    'faq.a3': {
        fr: 'Tout a fait. Le calculateur "Salaire Brut a Net" pour la France dispose d\'une option pour basculer entre statut Cadre et Non-Cadre, ajustant ainsi les cotisations de retraite complementaire.',
        en: 'Absolutely. The "Gross to Net Salary" calculator for France has an option to switch between Executive and Non-Executive status, thus adjusting supplementary pension contributions.'
    },
    'faq.q4': {
        fr: 'Mes donnees sont-elles stockees ?',
        en: 'Is my data stored?'
    },
    'faq.a4': {
        fr: 'Non. Tous les calculs sont effectues localement dans votre navigateur. Aucune donnee personnelle n\'est envoyee a nos serveurs ni stockee. Vous pouvez utiliser nos outils en toute confidentialite.',
        en: 'No. All calculations are performed locally in your browser. No personal data is sent to our servers or stored. You can use our tools with complete privacy.'
    },
    'faq.see_all': {
        fr: 'Voir toutes les questions',
        en: 'See all questions'
    },

    // Reassurance
    'reassurance.secure': {
        fr: '100% Securise',
        en: '100% Secure'
    },
    'reassurance.secure_desc': {
        fr: 'Aucune donnee stockee',
        en: 'No data stored'
    },
    'reassurance.official': {
        fr: 'Baremes Officiels',
        en: 'Official Rates'
    },
    'reassurance.official_desc': {
        fr: 'Mis a jour 2025',
        en: 'Updated 2025'
    },
    'reassurance.instant': {
        fr: 'Instantane',
        en: 'Instant'
    },
    'reassurance.instant_desc': {
        fr: 'Calculs en temps reel',
        en: 'Real-time calculations'
    },
    'reassurance.free': {
        fr: 'Gratuit',
        en: 'Free'
    },
    'reassurance.free_desc': {
        fr: 'Sans pub ni inscription',
        en: 'No ads or registration'
    },

    // Contact
    'contact.title': {
        fr: 'Une question ?',
        en: 'Have a question?'
    },
    'contact.subtitle': {
        fr: 'Contactez-nous, nous vous repondrons rapidement.',
        en: 'Contact us, we will respond quickly.'
    },
    'contact.name': {
        fr: 'Nom',
        en: 'Name'
    },
    'contact.name_placeholder': {
        fr: 'Votre nom',
        en: 'Your name'
    },
    'contact.email': {
        fr: 'Email',
        en: 'Email'
    },
    'contact.subject': {
        fr: 'Sujet',
        en: 'Subject'
    },
    'contact.subject_question': {
        fr: 'Question generale',
        en: 'General question'
    },
    'contact.subject_bug': {
        fr: 'Signaler un probleme',
        en: 'Report a problem'
    },
    'contact.subject_suggestion': {
        fr: 'Suggestion d\'amelioration',
        en: 'Improvement suggestion'
    },
    'contact.subject_other': {
        fr: 'Autre',
        en: 'Other'
    },
    'contact.message': {
        fr: 'Message',
        en: 'Message'
    },
    'contact.message_placeholder': {
        fr: 'Comment pouvons-nous vous aider ?',
        en: 'How can we help you?'
    },
    'contact.send': {
        fr: 'Envoyer le message',
        en: 'Send message'
    },
    'contact.sending': {
        fr: 'Envoi en cours...',
        en: 'Sending...'
    },
    'contact.success_title': {
        fr: 'Message envoye !',
        en: 'Message sent!'
    },
    'contact.success_text': {
        fr: 'Merci de nous avoir contacte. Nous vous repondrons rapidement.',
        en: 'Thank you for contacting us. We will respond shortly.'
    },
    'contact.send_another': {
        fr: 'Envoyer un autre message',
        en: 'Send another message'
    },

    // Footer
    'footer.description': {
        fr: 'Simulateurs fiscaux gratuits pour la France et le Maroc.',
        en: 'Free tax simulators for France and Morocco.'
    },
    'footer.info': {
        fr: 'Informations',
        en: 'Information'
    },
    'footer.legal': {
        fr: 'Mentions Legales',
        en: 'Legal Notice'
    },
    'footer.privacy': {
        fr: 'Confidentialite',
        en: 'Privacy'
    },
    'footer.rights': {
        fr: 'Tous droits reserves',
        en: 'All rights reserved'
    },

    // ==========================================
    // SIMULATORS COMMON
    // ==========================================
    'sim.gross_salary': {
        fr: 'Salaire Brut',
        en: 'Gross Salary'
    },
    'sim.monthly': {
        fr: 'Mensuel',
        en: 'Monthly'
    },
    'sim.annual': {
        fr: 'Annuel',
        en: 'Annual'
    },
    'sim.family_status': {
        fr: 'Situation Familiale',
        en: 'Family Status'
    },
    'sim.single': {
        fr: 'Celibataire',
        en: 'Single'
    },
    'sim.married': {
        fr: 'Marie(e)',
        en: 'Married'
    },
    'sim.divorced': {
        fr: 'Divorce(e)',
        en: 'Divorced'
    },
    'sim.children': {
        fr: 'Enfants a charge',
        en: 'Dependent children'
    },
    'sim.children_note': {
        fr: 'Enfants a charge (-21 ans ou handicap)',
        en: 'Dependent children (under 21 or disabled)'
    },
    'sim.net_estimated': {
        fr: 'Estimation Net',
        en: 'Net Estimate'
    },
    'sim.net_monthly': {
        fr: 'Net Mensuel Estime',
        en: 'Estimated Monthly Net'
    },
    'sim.net_annual': {
        fr: 'Net Annuel',
        en: 'Annual Net'
    },
    'sim.effective_rate': {
        fr: 'Taux Effectif',
        en: 'Effective Rate'
    },
    'sim.deducted': {
        fr: 'preleves',
        en: 'deducted'
    },
    'sim.in_pocket': {
        fr: 'Dans ma poche',
        en: 'In my pocket'
    },
    'sim.deductions': {
        fr: 'Prelevements',
        en: 'Deductions'
    },
    'sim.total_deducted': {
        fr: 'Total Deduit',
        en: 'Total Deducted'
    },
    'sim.see_details': {
        fr: 'Voir le detail du calcul',
        en: 'See calculation details'
    },
    'sim.breakdown': {
        fr: 'Decomposition (Annuel)',
        en: 'Breakdown (Annual)'
    },
    'sim.social_contrib': {
        fr: 'Cotisations Sociales',
        en: 'Social Contributions'
    },
    'sim.taxable_income': {
        fr: 'Net Imposable',
        en: 'Taxable Income'
    },
    'sim.income_tax': {
        fr: 'Impot sur le Revenu',
        en: 'Income Tax'
    },
    'sim.family_reduction': {
        fr: 'Reduction Charges Famille',
        en: 'Family Allowance Reduction'
    },
    'sim.final_tax': {
        fr: 'Impot sur le Revenu (IR) Final',
        en: 'Final Income Tax'
    },
    'sim.bracket_calc': {
        fr: 'Calcul par tranches (Progressif)',
        en: 'Progressive Tax Brackets'
    },
    'sim.bracket': {
        fr: 'Tranche',
        en: 'Bracket'
    },
    'sim.rate': {
        fr: 'Taux',
        en: 'Rate'
    },
    'sim.amount': {
        fr: 'Montant',
        en: 'Amount'
    },
    'sim.tax': {
        fr: 'Impot',
        en: 'Tax'
    },
    'sim.total': {
        fr: 'Total',
        en: 'Total'
    },
    'sim.net_salary': {
        fr: 'Salaire Net',
        en: 'Net Salary'
    },

    // ==========================================
    // COMPARATOR
    // ==========================================
    'comp.title': {
        fr: 'Comparateur Fiscal',
        en: 'Tax Comparator'
    },
    'comp.subtitle': {
        fr: 'Comparez votre salaire net et votre pression fiscale entre les deux pays. Simulateur mis a jour avec les baremes 2025.',
        en: 'Compare your net salary and tax burden between the two countries. Simulator updated with 2025 rates.'
    },
    'comp.select_countries': {
        fr: 'Selectionnez les pays a comparer (2 minimum)',
        en: 'Select countries to compare (minimum 2)'
    },
    'comp.gross_annual': {
        fr: 'Salaire Brut Annuel',
        en: 'Annual Gross Salary'
    },
    'comp.converted_note': {
        fr: 'Le salaire est converti dans chaque devise locale pour les calculs.',
        en: 'The salary is converted to each local currency for calculations.'
    },
    'comp.net_in_pocket': {
        fr: 'Net "En Poche"',
        en: 'Net "In Pocket"'
    },
    'comp.tax_rate': {
        fr: 'Taux d\'Imposition',
        en: 'Tax Rate'
    },
    'comp.total_pressure': {
        fr: 'Pression Totale',
        en: 'Total Burden'
    },
    'comp.distribution': {
        fr: 'Distribution',
        en: 'Distribution'
    },
    'comp.of_gross': {
        fr: '100% du Brut',
        en: '100% of Gross'
    },
    'comp.net': {
        fr: 'Net',
        en: 'Net'
    },
    'comp.social': {
        fr: 'Social',
        en: 'Social'
    },
    'comp.ranking': {
        fr: 'Classement',
        en: 'Ranking'
    },
    'comp.winner': {
        fr: 'en tete !',
        en: 'wins!'
    },
    'comp.vs_last': {
        fr: 'vs dernier',
        en: 'vs last'
    },
    'comp.select_min_2': {
        fr: 'Selectionnez au moins 2 pays pour comparer.',
        en: 'Select at least 2 countries to compare.'
    },
    'comp.annual_diff': {
        fr: 'Difference Annuelle',
        en: 'Annual Difference'
    },
    'comp.wins': {
        fr: 'l\'emporte !',
        en: 'wins!'
    },
    'comp.you_save': {
        fr: 'Vous economisez',
        en: 'You save'
    },
    'comp.points': {
        fr: 'points de pression fiscale',
        en: 'points of tax burden'
    },

    // Countries
    'country.france': {
        fr: 'France',
        en: 'France'
    },
    'country.maroc': {
        fr: 'Maroc',
        en: 'Morocco'
    },
    'country.dubai': {
        fr: 'Dubai',
        en: 'Dubai'
    },
    'country.geneve': {
        fr: 'Geneve',
        en: 'Geneva'
    },
    'country.luxembourg': {
        fr: 'Luxembourg',
        en: 'Luxembourg'
    },

    // ==========================================
    // DISCLAIMERS
    // ==========================================
    'disclaimer.general': {
        fr: 'Cet outil est fourni a titre indicatif uniquement. Les cotisations sociales sont estimees a un taux moyen standard. Bareme IR 2025.',
        en: 'This tool is provided for informational purposes only. Social contributions are estimated at a standard average rate. 2025 income tax rates.'
    },
    'disclaimer.comparator': {
        fr: 'Avertissement Legal : Cet outil est fourni a titre indicatif uniquement. Les lois fiscales varient selon les pays et sont sujettes a modifications.',
        en: 'Legal Disclaimer: This tool is provided for informational purposes only. Tax laws vary by country and are subject to change.'
    }
};

// ==========================================
// i18n ENGINE
// ==========================================

const i18n = {
    currentLang: 'fr',
    supportedLangs: ['fr', 'en'],
    storageKey: 'netsalaire_lang',

    /**
     * Initialize the i18n system
     */
    init() {
        // Check localStorage first
        const storedLang = localStorage.getItem(this.storageKey);

        if (storedLang && this.supportedLangs.includes(storedLang)) {
            this.currentLang = storedLang;
        } else {
            // Auto-detect from browser
            const browserLang = navigator.language.split('-')[0];
            this.currentLang = this.supportedLangs.includes(browserLang) ? browserLang : 'fr';
        }

        // Apply translations
        this.applyTranslations();

        // Update language switcher UI
        this.updateSwitcherUI();

        // Set html lang attribute
        document.documentElement.lang = this.currentLang;
    },

    /**
     * Get translation for a key
     */
    t(key) {
        const translation = translations[key];
        if (!translation) {
            console.warn(`Missing translation for key: ${key}`);
            return key;
        }
        return translation[this.currentLang] || translation['fr'] || key;
    },

    /**
     * Switch language
     */
    setLang(lang) {
        if (!this.supportedLangs.includes(lang)) {
            console.warn(`Unsupported language: ${lang}`);
            return;
        }

        this.currentLang = lang;
        localStorage.setItem(this.storageKey, lang);

        this.applyTranslations();
        this.updateSwitcherUI();

        document.documentElement.lang = lang;
    },

    /**
     * Toggle between languages
     */
    toggle() {
        const newLang = this.currentLang === 'fr' ? 'en' : 'fr';
        this.setLang(newLang);
    },

    /**
     * Apply translations to all elements with data-i18n attribute
     */
    applyTranslations() {
        // Translate text content
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            el.textContent = this.t(key);
        });

        // Translate placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            el.placeholder = this.t(key);
        });

        // Translate titles/tooltips
        document.querySelectorAll('[data-i18n-title]').forEach(el => {
            const key = el.getAttribute('data-i18n-title');
            el.title = this.t(key);
        });

        // Translate aria-labels
        document.querySelectorAll('[data-i18n-aria]').forEach(el => {
            const key = el.getAttribute('data-i18n-aria');
            el.setAttribute('aria-label', this.t(key));
        });
    },

    /**
     * Update language switcher UI
     */
    updateSwitcherUI() {
        const switcher = document.getElementById('lang-switcher');
        if (switcher) {
            const frBtn = switcher.querySelector('[data-lang="fr"]');
            const enBtn = switcher.querySelector('[data-lang="en"]');

            if (frBtn && enBtn) {
                frBtn.classList.toggle('active', this.currentLang === 'fr');
                enBtn.classList.toggle('active', this.currentLang === 'en');
            }
        }

        // Update flag display if exists
        const currentFlag = document.getElementById('current-lang-flag');
        if (currentFlag) {
            currentFlag.textContent = this.currentLang === 'fr' ? '🇫🇷' : '🇬🇧';
        }
    }
};

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => i18n.init());
} else {
    i18n.init();
}

// Make i18n globally available
window.i18n = i18n;
window.t = (key) => i18n.t(key);
