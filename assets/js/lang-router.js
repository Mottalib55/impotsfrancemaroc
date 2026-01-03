/**
 * NetSalaire - Language Router
 * Handles automatic language detection, preference storage, and URL routing
 */

(function() {
    'use strict';

    const STORAGE_KEY = 'netsalaire_lang';
    const SUPPORTED_LANGS = ['fr', 'en'];

    // URL mappings: French URL -> English URL
    const URL_MAPPINGS = {
        // Homepage
        '/': '/en/',
        '/index.html': '/en/',

        // France section
        '/france/simulateur-salaire-brut-net/': '/en/france/gross-to-net/',
        '/france/simulateur-impot-revenu/': '/en/france/income-tax/',
        '/france/guide/': '/en/france/guide/',

        // Morocco section
        '/maroc/simulateur-salaire-brut-net/': '/en/morocco/gross-to-net/',
        '/maroc/simulateur-ir/': '/en/morocco/income-tax/',
        '/maroc/guide/': '/en/morocco/guide/',

        // Comparators
        '/comparateur-salaire-france-maroc/': '/en/france-morocco-comparator/',
        '/fr/comparateur-global/': '/en/global-comparison/',
        '/comparateur-global/': '/en/global-comparison/',

        // Info pages
        '/faq/': '/en/faq/',
        '/mentions-legales/': '/en/legal-notice/',
        '/politique-confidentialite/': '/en/privacy-policy/'
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
        return 'fr';
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
     * Initialize language router
     */
    function init() {
        const storedLang = getStoredLang();
        const currentPageLang = getCurrentPageLang();

        // If user has a stored preference
        if (storedLang && SUPPORTED_LANGS.includes(storedLang)) {
            // Check if we need to redirect
            if (storedLang !== currentPageLang) {
                const equivalentUrl = getEquivalentUrl(storedLang);
                if (equivalentUrl) {
                    window.location.replace(equivalentUrl);
                    return;
                }
            }
        } else {
            // No stored preference - detect from browser
            const browserLang = detectBrowserLang();
            storeLang(browserLang);

            // Redirect if needed
            if (browserLang !== currentPageLang) {
                const equivalentUrl = getEquivalentUrl(browserLang);
                if (equivalentUrl) {
                    window.location.replace(equivalentUrl);
                    return;
                }
            }
        }

        // Update stored language to match current page
        // (in case user manually navigated to a different language version)
        storeLang(currentPageLang);
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
        }
    }

    /**
     * Get current preferred language
     */
    function getPreferredLang() {
        return getStoredLang() || detectBrowserLang();
    }

    // Export to global scope
    window.langRouter = {
        init: init,
        switchLanguage: switchLanguage,
        getPreferredLang: getPreferredLang,
        getCurrentPageLang: getCurrentPageLang,
        storeLang: storeLang
    };

    // Auto-initialize
    init();
})();
