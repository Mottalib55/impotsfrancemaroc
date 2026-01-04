/**
 * NetSalaire - Language Router
 * Handles language switching between /fr/ and /en/ versions
 */

(function() {
    'use strict';

    const STORAGE_KEY = 'netsalaire_lang';
    const SUPPORTED_LANGS = ['fr', 'en'];

    // URL mappings: French URL -> English URL
    const URL_MAPPINGS = {
        // Homepage
        '/fr/': '/en/',

        // France section
        '/fr/france/simulateur-salaire-brut-net/': '/en/france/gross-to-net/',
        '/fr/france/simulateur-impot-revenu/': '/en/france/income-tax/',
        '/fr/france/guide/': '/en/france/tax-guide/',

        // Morocco section
        '/fr/maroc/simulateur-salaire-brut-net/': '/en/morocco/gross-to-net/',
        '/fr/maroc/simulateur-ir/': '/en/morocco/tax-simulator/',
        '/fr/maroc/guide/': '/en/morocco/tax-guide/',

        // Comparators
        '/fr/comparateur-salaire-france-maroc/': '/en/france-morocco-comparison/',
        '/fr/comparateur-global/': '/en/global-comparison/',

        // Tax simulators (alternative paths)
        '/fr/simulateur-impot-revenu/': '/en/income-tax-simulator/',

        // Info pages
        '/fr/faq/': '/en/faq/',
        '/fr/mentions-legales/': '/en/legal-notice/',
        '/fr/politique-confidentialite/': '/en/privacy-policy/'
    };

    // Create reverse mappings (English -> French)
    const REVERSE_MAPPINGS = {};
    for (const [fr, en] of Object.entries(URL_MAPPINGS)) {
        REVERSE_MAPPINGS[en] = fr;
    }

    /**
     * Get stored language preference
     */
    function getStoredLang() {
        try {
            return localStorage.getItem(STORAGE_KEY);
        } catch (e) {
            return null;
        }
    }

    /**
     * Store language preference
     */
    function storeLang(lang) {
        try {
            localStorage.setItem(STORAGE_KEY, lang);
        } catch (e) {
            // localStorage not available
        }
    }

    /**
     * Detect browser language
     */
    function detectBrowserLang() {
        const browserLang = (navigator.language || navigator.userLanguage || 'fr').toLowerCase();
        if (browserLang.startsWith('en')) {
            return 'en';
        }
        return 'fr'; // Default to French
    }

    /**
     * Get current page language from URL
     */
    function getCurrentPageLang() {
        const path = window.location.pathname;
        if (path.startsWith('/en/')) {
            return 'en';
        }
        if (path.startsWith('/fr/')) {
            return 'fr';
        }
        return null; // Root pages (redirects)
    }

    /**
     * Normalize path (ensure trailing slash, remove index.html)
     */
    function normalizePath(path) {
        path = path.replace(/index\.html$/, '');
        if (!path.endsWith('/')) {
            path += '/';
        }
        return path;
    }

    /**
     * Get equivalent URL in target language
     */
    function getEquivalentUrl(targetLang) {
        const currentPath = normalizePath(window.location.pathname);
        const currentLang = getCurrentPageLang();

        if (currentLang === targetLang) {
            return null; // Already on correct language
        }

        if (targetLang === 'en') {
            // French -> English
            return URL_MAPPINGS[currentPath] || null;
        } else {
            // English -> French
            return REVERSE_MAPPINGS[currentPath] || null;
        }
    }

    /**
     * Switch language manually (called by language switcher)
     */
    function switchLanguage(targetLang) {
        if (!SUPPORTED_LANGS.includes(targetLang)) {
            console.warn('Unsupported language:', targetLang);
            return;
        }

        storeLang(targetLang);

        const equivalentUrl = getEquivalentUrl(targetLang);
        if (equivalentUrl) {
            window.location.href = equivalentUrl;
        } else {
            // Fallback to homepage of target language
            window.location.href = targetLang === 'en' ? '/en/' : '/fr/';
        }
    }

    /**
     * Get current preferred language
     */
    function getPreferredLang() {
        return getStoredLang() || detectBrowserLang();
    }

    /**
     * Update stored language based on current page
     */
    function updateStoredLangFromPage() {
        const pageLang = getCurrentPageLang();
        if (pageLang) {
            storeLang(pageLang);
        }
    }

    // Update stored language when on a /fr/ or /en/ page
    updateStoredLangFromPage();

    // Export to global scope
    window.langRouter = {
        switchLanguage: switchLanguage,
        getPreferredLang: getPreferredLang,
        getCurrentPageLang: getCurrentPageLang,
        getEquivalentUrl: getEquivalentUrl,
        storeLang: storeLang
    };
})();
