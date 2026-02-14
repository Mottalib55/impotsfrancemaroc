/**
 * NetSalaire - Language Router
 * Handles language switching between /fr/, /en/ and native-language versions
 */

(function() {
    'use strict';

    const STORAGE_KEY = 'netsalaire_lang';
    const SUPPORTED_LANGS = ['fr', 'en', 'de', 'es', 'pt', 'nl', 'ar', 'it', 'sv', 'no', 'da', 'fi', 'el', 'pl', 'cs', 'hu', 'ro', 'hr', 'tr', 'ja', 'ko', 'zh', 'th', 'ms', 'id', 'vi'];

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
        '/fr/maroc/simulateur-impot-revenu/': '/en/morocco/income-tax/',
        '/fr/maroc/guide/': '/en/morocco/tax-guide/',

        // Comparators
        '/fr/comparateur-salaire-france-maroc/': '/en/france-morocco-comparison/',
        '/fr/comparateur-global/': '/en/global-comparison/',

        // Info pages
        '/fr/faq/': '/en/faq/',
        '/fr/mentions-legales/': '/en/legal-notice/',
        '/fr/politique-confidentialite/': '/en/privacy-policy/'
    };

    // Native language mappings: FR URL -> { lang: native URL }
    const NATIVE_MAPPINGS = {
        '/fr/allemagne/simulateur-impot/': { lang: 'de', native: '/de/deutschland/einkommensteuer/', en: '/en/germany/income-tax/' },
        '/fr/autriche/simulateur-impot/': { lang: 'de', native: '/de/oesterreich/einkommensteuer/', en: '/en/austria/income-tax/' },
        '/fr/suisse/simulateur-impot/': { lang: 'de', native: '/de/schweiz/einkommensteuer/', en: '/en/switzerland/income-tax/' },
        '/fr/espagne/simulateur-impot/': { lang: 'es', native: '/es/espana/simulador-impuestos/', en: '/en/spain/income-tax/' },
        '/fr/mexique/simulateur-impot/': { lang: 'es', native: '/es/mexico/simulador-impuestos/', en: '/en/mexico/income-tax/' },
        '/fr/argentine/simulateur-impot/': { lang: 'es', native: '/es/argentina/simulador-impuestos/', en: '/en/argentina/income-tax/' },
        '/fr/chili/simulateur-impot/': { lang: 'es', native: '/es/chile/simulador-impuestos/', en: '/en/chile/income-tax/' },
        '/fr/colombie/simulateur-impot/': { lang: 'es', native: '/es/colombia/simulador-impuestos/', en: '/en/colombia/income-tax/' },
        '/fr/perou/simulateur-impot/': { lang: 'es', native: '/es/peru/simulador-impuestos/', en: '/en/peru/income-tax/' },
        '/fr/portugal/simulateur-impot/': { lang: 'pt', native: '/pt/portugal/simulador-impostos/', en: '/en/portugal/income-tax/' },
        '/fr/bresil/simulateur-impot/': { lang: 'pt', native: '/pt/brasil/simulador-impostos/', en: '/en/brazil/income-tax/' },
        '/fr/pays-bas/simulateur-impot/': { lang: 'nl', native: '/nl/nederland/belasting-berekenen/', en: '/en/netherlands/income-tax/' },
        '/fr/belgique/simulateur-impot/': { lang: 'nl', native: '/nl/belgie/belasting-berekenen/', en: '/en/belgium/income-tax/' },
        '/fr/arabie-saoudite/simulateur-impot/': { lang: 'ar', native: '/ar/arabie-saoudite/tax-calculator/', en: '/en/saudi-arabia/income-tax/' },
        '/fr/dubai/simulateur-impot/': { lang: 'ar', native: '/ar/dubai/tax-calculator/', en: '/en/dubai/income-tax/' },
        '/fr/qatar/simulateur-impot/': { lang: 'ar', native: '/ar/qatar/tax-calculator/', en: '/en/qatar/income-tax/' },
        '/fr/koweit/simulateur-impot/': { lang: 'ar', native: '/ar/koweit/tax-calculator/', en: '/en/kuwait/income-tax/' },
        '/fr/egypte/simulateur-impot/': { lang: 'ar', native: '/ar/egypte/tax-calculator/', en: '/en/egypt/income-tax/' },
        '/fr/italie/simulateur-impot/': { lang: 'it', native: '/it/italia/calcolatore-imposte/', en: '/en/italy/income-tax/' },
        '/fr/suede/simulateur-impot/': { lang: 'sv', native: '/sv/sverige/skatteberaknare/', en: '/en/sweden/income-tax/' },
        '/fr/norvege/simulateur-impot/': { lang: 'no', native: '/no/norge/skattekalkulator/', en: '/en/norway/income-tax/' },
        '/fr/danemark/simulateur-impot/': { lang: 'da', native: '/da/danmark/skatteberegner/', en: '/en/denmark/income-tax/' },
        '/fr/finlande/simulateur-impot/': { lang: 'fi', native: '/fi/suomi/verolaskuri/', en: '/en/finland/income-tax/' },
        '/fr/grece/simulateur-impot/': { lang: 'el', native: '/el/ellada/ypologismos-forou/', en: '/en/greece/income-tax/' },
        '/fr/pologne/simulateur-impot/': { lang: 'pl', native: '/pl/polska/kalkulator-podatkowy/', en: '/en/poland/income-tax/' },
        '/fr/tchequie/simulateur-impot/': { lang: 'cs', native: '/cs/cesko/danovy-kalkulator/', en: '/en/czech-republic/income-tax/' },
        '/fr/hongrie/simulateur-impot/': { lang: 'hu', native: '/hu/magyarorszag/ado-kalkulator/', en: '/en/hungary/income-tax/' },
        '/fr/roumanie/simulateur-impot/': { lang: 'ro', native: '/ro/romania/calculator-impozit/', en: '/en/romania/income-tax/' },
        '/fr/croatie/simulateur-impot/': { lang: 'hr', native: '/hr/hrvatska/porezni-kalkulator/', en: '/en/croatia/income-tax/' },
        '/fr/turquie/simulateur-impot/': { lang: 'tr', native: '/tr/turkiye/vergi-hesaplama/', en: '/en/turkey/income-tax/' },
        '/fr/japon/simulateur-impot/': { lang: 'ja', native: '/ja/nihon/zeikin-keisan/', en: '/en/japan/income-tax/' },
        '/fr/coree-du-sud/simulateur-impot/': { lang: 'ko', native: '/ko/hanguk/segeum-gyesan/', en: '/en/south-korea/income-tax/' },
        '/fr/chine/simulateur-impot/': { lang: 'zh', native: '/zh/zhongguo/shuishou-jisuan/', en: '/en/china/income-tax/' },
        '/fr/thailande/simulateur-impot/': { lang: 'th', native: '/th/prathet-thai/khamnuan-phasi/', en: '/en/thailand/income-tax/' },
        '/fr/malaisie/simulateur-impot/': { lang: 'ms', native: '/ms/malaysia/kalkulator-cukai/', en: '/en/malaysia/income-tax/' },
        '/fr/indonesie/simulateur-impot/': { lang: 'id', native: '/id/indonesia/kalkulator-pajak/', en: '/en/indonesia/income-tax/' },
        '/fr/vietnam/simulateur-impot/': { lang: 'vi', native: '/vi/viet-nam/tinh-thue/', en: '/en/vietnam/income-tax/' }
    };

    // Build reverse lookup: native URL -> { fr, en, lang }
    const NATIVE_REVERSE = {};
    // Build EN -> { fr, native, lang }
    const EN_NATIVE = {};
    for (const [frUrl, info] of Object.entries(NATIVE_MAPPINGS)) {
        NATIVE_REVERSE[info.native] = { fr: frUrl, en: info.en, lang: info.lang };
        EN_NATIVE[info.en] = { fr: frUrl, native: info.native, lang: info.lang };
    }

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
        // Check native language prefixes
        const match = path.match(/^\/([a-z]{2})\//);
        if (match && SUPPORTED_LANGS.includes(match[1])) {
            return match[1];
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

        // Current page is FR
        if (currentLang === 'fr') {
            if (targetLang === 'en') {
                // Check native mappings first (they have EN URLs)
                const nativeInfo = NATIVE_MAPPINGS[currentPath];
                if (nativeInfo) return nativeInfo.en;
                return URL_MAPPINGS[currentPath] || null;
            }
            // FR -> native language
            const nativeInfo = NATIVE_MAPPINGS[currentPath];
            if (nativeInfo && nativeInfo.lang === targetLang) {
                return nativeInfo.native;
            }
            return null;
        }

        // Current page is EN
        if (currentLang === 'en') {
            if (targetLang === 'fr') {
                // Check native reverse mappings
                const nativeInfo = EN_NATIVE[currentPath];
                if (nativeInfo) return nativeInfo.fr;
                return REVERSE_MAPPINGS[currentPath] || null;
            }
            // EN -> native language
            const nativeInfo = EN_NATIVE[currentPath];
            if (nativeInfo && nativeInfo.lang === targetLang) {
                return nativeInfo.native;
            }
            return null;
        }

        // Current page is native language
        const nativeInfo = NATIVE_REVERSE[currentPath];
        if (nativeInfo) {
            if (targetLang === 'fr') return nativeInfo.fr;
            if (targetLang === 'en') return nativeInfo.en;
        }
        return null;
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
