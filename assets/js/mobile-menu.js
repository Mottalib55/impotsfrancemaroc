/* Mobile Menu - Country search & toggle */
(function() {
    var lang = document.documentElement.lang || 'fr';
    var isFr = lang === 'fr' || window.location.pathname.startsWith('/fr/');

    var countriesFR = [
        { name: 'France', flag: '\u{1F1EB}\u{1F1F7}', url: '/fr/france/simulateur-impot-revenu/', region: 'popular' },
        { name: 'Maroc', flag: '\u{1F1F2}\u{1F1E6}', url: '/fr/maroc/simulateur-impot-revenu/', region: 'popular' },
        { name: 'USA', flag: '\u{1F1FA}\u{1F1F8}', url: '/fr/usa/simulateur-impot/', region: 'popular' },
        { name: 'Royaume-Uni', flag: '\u{1F1EC}\u{1F1E7}', url: '/fr/royaume-uni/simulateur-impot/', region: 'popular' },
        { name: 'Suisse', flag: '\u{1F1E8}\u{1F1ED}', url: '/fr/suisse/simulateur-impot/', region: 'popular' },
        { name: 'Dubai', flag: '\u{1F1E6}\u{1F1EA}', url: '/fr/dubai/simulateur-impot/', region: 'popular' },
        { name: 'Allemagne', flag: '\u{1F1E9}\u{1F1EA}', url: '/fr/allemagne/simulateur-impot/', region: 'europe' },
        { name: 'Belgique', flag: '\u{1F1E7}\u{1F1EA}', url: '/fr/belgique/simulateur-impot/', region: 'europe' },
        { name: 'Espagne', flag: '\u{1F1EA}\u{1F1F8}', url: '/fr/espagne/simulateur-impot/', region: 'europe' },
        { name: 'Italie', flag: '\u{1F1EE}\u{1F1F9}', url: '/fr/italie/simulateur-impot/', region: 'europe' },
        { name: 'Pays-Bas', flag: '\u{1F1F3}\u{1F1F1}', url: '/fr/pays-bas/simulateur-impot/', region: 'europe' },
        { name: 'Portugal', flag: '\u{1F1F5}\u{1F1F9}', url: '/fr/portugal/simulateur-impot/', region: 'europe' },
        { name: 'Luxembourg', flag: '\u{1F1F1}\u{1F1FA}', url: '/fr/luxembourg/simulateur-impot/', region: 'europe' },
        { name: 'Autriche', flag: '\u{1F1E6}\u{1F1F9}', url: '/fr/autriche/simulateur-impot/', region: 'europe' },
        { name: 'Irlande', flag: '\u{1F1EE}\u{1F1EA}', url: '/fr/irlande/simulateur-impot/', region: 'europe' },
        { name: 'Suede', flag: '\u{1F1F8}\u{1F1EA}', url: '/fr/suede/simulateur-impot/', region: 'europe' },
        { name: 'Norvege', flag: '\u{1F1F3}\u{1F1F4}', url: '/fr/norvege/simulateur-impot/', region: 'europe' },
        { name: 'Danemark', flag: '\u{1F1E9}\u{1F1F0}', url: '/fr/danemark/simulateur-impot/', region: 'europe' },
        { name: 'Finlande', flag: '\u{1F1EB}\u{1F1EE}', url: '/fr/finlande/simulateur-impot/', region: 'europe' },
        { name: 'Grece', flag: '\u{1F1EC}\u{1F1F7}', url: '/fr/grece/simulateur-impot/', region: 'europe' },
        { name: 'Pologne', flag: '\u{1F1F5}\u{1F1F1}', url: '/fr/pologne/simulateur-impot/', region: 'europe' },
        { name: 'Tchequie', flag: '\u{1F1E8}\u{1F1FF}', url: '/fr/tchequie/simulateur-impot/', region: 'europe' },
        { name: 'Hongrie', flag: '\u{1F1ED}\u{1F1FA}', url: '/fr/hongrie/simulateur-impot/', region: 'europe' },
        { name: 'Roumanie', flag: '\u{1F1F7}\u{1F1F4}', url: '/fr/roumanie/simulateur-impot/', region: 'europe' },
        { name: 'Croatie', flag: '\u{1F1ED}\u{1F1F7}', url: '/fr/croatie/simulateur-impot/', region: 'europe' },
        { name: 'Turquie', flag: '\u{1F1F9}\u{1F1F7}', url: '/fr/turquie/simulateur-impot/', region: 'europe' },
        { name: 'Canada', flag: '\u{1F1E8}\u{1F1E6}', url: '/fr/canada/simulateur-impot/', region: 'americas' },
        { name: 'Mexique', flag: '\u{1F1F2}\u{1F1FD}', url: '/fr/mexique/simulateur-impot/', region: 'americas' },
        { name: 'Bresil', flag: '\u{1F1E7}\u{1F1F7}', url: '/fr/bresil/simulateur-impot/', region: 'americas' },
        { name: 'Argentine', flag: '\u{1F1E6}\u{1F1F7}', url: '/fr/argentine/simulateur-impot/', region: 'americas' },
        { name: 'Chili', flag: '\u{1F1E8}\u{1F1F1}', url: '/fr/chili/simulateur-impot/', region: 'americas' },
        { name: 'Colombie', flag: '\u{1F1E8}\u{1F1F4}', url: '/fr/colombie/simulateur-impot/', region: 'americas' },
        { name: 'Perou', flag: '\u{1F1F5}\u{1F1EA}', url: '/fr/perou/simulateur-impot/', region: 'americas' },
        { name: 'Japon', flag: '\u{1F1EF}\u{1F1F5}', url: '/fr/japon/simulateur-impot/', region: 'asia' },
        { name: 'Chine', flag: '\u{1F1E8}\u{1F1F3}', url: '/fr/chine/simulateur-impot/', region: 'asia' },
        { name: 'Coree du Sud', flag: '\u{1F1F0}\u{1F1F7}', url: '/fr/coree-du-sud/simulateur-impot/', region: 'asia' },
        { name: 'Inde', flag: '\u{1F1EE}\u{1F1F3}', url: '/fr/inde/simulateur-impot/', region: 'asia' },
        { name: 'Singapour', flag: '\u{1F1F8}\u{1F1EC}', url: '/fr/singapour/simulateur-impot/', region: 'asia' },
        { name: 'Hong Kong', flag: '\u{1F1ED}\u{1F1F0}', url: '/fr/hong-kong/simulateur-impot/', region: 'asia' },
        { name: 'Indonesie', flag: '\u{1F1EE}\u{1F1E9}', url: '/fr/indonesie/simulateur-impot/', region: 'asia' },
        { name: 'Malaisie', flag: '\u{1F1F2}\u{1F1FE}', url: '/fr/malaisie/simulateur-impot/', region: 'asia' },
        { name: 'Pakistan', flag: '\u{1F1F5}\u{1F1F0}', url: '/fr/pakistan/simulateur-impot/', region: 'asia' },
        { name: 'Thailande', flag: '\u{1F1F9}\u{1F1ED}', url: '/fr/thailande/simulateur-impot/', region: 'asia' },
        { name: 'Philippines', flag: '\u{1F1F5}\u{1F1ED}', url: '/fr/philippines/simulateur-impot/', region: 'asia' },
        { name: 'Vietnam', flag: '\u{1F1FB}\u{1F1F3}', url: '/fr/vietnam/simulateur-impot/', region: 'asia' },
        { name: 'Dubai', flag: '\u{1F1E6}\u{1F1EA}', url: '/fr/dubai/simulateur-impot/', region: 'mena' },
        { name: 'Arabie Saoudite', flag: '\u{1F1F8}\u{1F1E6}', url: '/fr/arabie-saoudite/simulateur-impot/', region: 'mena' },
        { name: 'Qatar', flag: '\u{1F1F6}\u{1F1E6}', url: '/fr/qatar/simulateur-impot/', region: 'mena' },
        { name: 'Koweit', flag: '\u{1F1F0}\u{1F1FC}', url: '/fr/koweit/simulateur-impot/', region: 'mena' },
        { name: 'Egypte', flag: '\u{1F1EA}\u{1F1EC}', url: '/fr/egypte/simulateur-impot/', region: 'mena' },
        { name: 'Maroc', flag: '\u{1F1F2}\u{1F1E6}', url: '/fr/maroc/simulateur-impot-revenu/', region: 'mena' },
        { name: 'Afrique du Sud', flag: '\u{1F1FF}\u{1F1E6}', url: '/fr/afrique-du-sud/simulateur-impot/', region: 'other' },
        { name: 'Australie', flag: '\u{1F1E6}\u{1F1FA}', url: '/fr/australie/simulateur-impot/', region: 'other' },
        { name: 'Nouvelle-Zelande', flag: '\u{1F1F3}\u{1F1FF}', url: '/fr/nouvelle-zelande/simulateur-impot/', region: 'other' }
    ];

    var countriesEN = [
        { name: 'France', flag: '\u{1F1EB}\u{1F1F7}', url: '/en/france/income-tax/', region: 'popular' },
        { name: 'Morocco', flag: '\u{1F1F2}\u{1F1E6}', url: '/en/morocco/income-tax/', region: 'popular' },
        { name: 'USA', flag: '\u{1F1FA}\u{1F1F8}', url: '/en/usa/income-tax/', region: 'popular' },
        { name: 'United Kingdom', flag: '\u{1F1EC}\u{1F1E7}', url: '/en/uk/income-tax/', region: 'popular' },
        { name: 'Switzerland', flag: '\u{1F1E8}\u{1F1ED}', url: '/en/switzerland/income-tax/', region: 'popular' },
        { name: 'Dubai', flag: '\u{1F1E6}\u{1F1EA}', url: '/en/dubai/income-tax/', region: 'popular' },
        { name: 'Germany', flag: '\u{1F1E9}\u{1F1EA}', url: '/en/germany/income-tax/', region: 'europe' },
        { name: 'Belgium', flag: '\u{1F1E7}\u{1F1EA}', url: '/en/belgium/income-tax/', region: 'europe' },
        { name: 'Spain', flag: '\u{1F1EA}\u{1F1F8}', url: '/en/spain/income-tax/', region: 'europe' },
        { name: 'Italy', flag: '\u{1F1EE}\u{1F1F9}', url: '/en/italy/income-tax/', region: 'europe' },
        { name: 'Netherlands', flag: '\u{1F1F3}\u{1F1F1}', url: '/en/netherlands/income-tax/', region: 'europe' },
        { name: 'Portugal', flag: '\u{1F1F5}\u{1F1F9}', url: '/en/portugal/income-tax/', region: 'europe' },
        { name: 'Luxembourg', flag: '\u{1F1F1}\u{1F1FA}', url: '/en/luxembourg/income-tax/', region: 'europe' },
        { name: 'Austria', flag: '\u{1F1E6}\u{1F1F9}', url: '/en/austria/income-tax/', region: 'europe' },
        { name: 'Ireland', flag: '\u{1F1EE}\u{1F1EA}', url: '/en/ireland/income-tax/', region: 'europe' },
        { name: 'Sweden', flag: '\u{1F1F8}\u{1F1EA}', url: '/en/sweden/income-tax/', region: 'europe' },
        { name: 'Norway', flag: '\u{1F1F3}\u{1F1F4}', url: '/en/norway/income-tax/', region: 'europe' },
        { name: 'Denmark', flag: '\u{1F1E9}\u{1F1F0}', url: '/en/denmark/income-tax/', region: 'europe' },
        { name: 'Finland', flag: '\u{1F1EB}\u{1F1EE}', url: '/en/finland/income-tax/', region: 'europe' },
        { name: 'Greece', flag: '\u{1F1EC}\u{1F1F7}', url: '/en/greece/income-tax/', region: 'europe' },
        { name: 'Poland', flag: '\u{1F1F5}\u{1F1F1}', url: '/en/poland/income-tax/', region: 'europe' },
        { name: 'Czech Republic', flag: '\u{1F1E8}\u{1F1FF}', url: '/en/czech-republic/income-tax/', region: 'europe' },
        { name: 'Hungary', flag: '\u{1F1ED}\u{1F1FA}', url: '/en/hungary/income-tax/', region: 'europe' },
        { name: 'Romania', flag: '\u{1F1F7}\u{1F1F4}', url: '/en/romania/income-tax/', region: 'europe' },
        { name: 'Croatia', flag: '\u{1F1ED}\u{1F1F7}', url: '/en/croatia/income-tax/', region: 'europe' },
        { name: 'Turkey', flag: '\u{1F1F9}\u{1F1F7}', url: '/en/turkey/income-tax/', region: 'europe' },
        { name: 'Canada', flag: '\u{1F1E8}\u{1F1E6}', url: '/en/canada/income-tax/', region: 'americas' },
        { name: 'Mexico', flag: '\u{1F1F2}\u{1F1FD}', url: '/en/mexico/income-tax/', region: 'americas' },
        { name: 'Brazil', flag: '\u{1F1E7}\u{1F1F7}', url: '/en/brazil/income-tax/', region: 'americas' },
        { name: 'Argentina', flag: '\u{1F1E6}\u{1F1F7}', url: '/en/argentina/income-tax/', region: 'americas' },
        { name: 'Chile', flag: '\u{1F1E8}\u{1F1F1}', url: '/en/chile/income-tax/', region: 'americas' },
        { name: 'Colombia', flag: '\u{1F1E8}\u{1F1F4}', url: '/en/colombia/income-tax/', region: 'americas' },
        { name: 'Peru', flag: '\u{1F1F5}\u{1F1EA}', url: '/en/peru/income-tax/', region: 'americas' },
        { name: 'Japan', flag: '\u{1F1EF}\u{1F1F5}', url: '/en/japan/income-tax/', region: 'asia' },
        { name: 'China', flag: '\u{1F1E8}\u{1F1F3}', url: '/en/china/income-tax/', region: 'asia' },
        { name: 'South Korea', flag: '\u{1F1F0}\u{1F1F7}', url: '/en/south-korea/income-tax/', region: 'asia' },
        { name: 'India', flag: '\u{1F1EE}\u{1F1F3}', url: '/en/india/income-tax/', region: 'asia' },
        { name: 'Singapore', flag: '\u{1F1F8}\u{1F1EC}', url: '/en/singapore/income-tax/', region: 'asia' },
        { name: 'Hong Kong', flag: '\u{1F1ED}\u{1F1F0}', url: '/en/hong-kong/income-tax/', region: 'asia' },
        { name: 'Indonesia', flag: '\u{1F1EE}\u{1F1E9}', url: '/en/indonesia/income-tax/', region: 'asia' },
        { name: 'Malaysia', flag: '\u{1F1F2}\u{1F1FE}', url: '/en/malaysia/income-tax/', region: 'asia' },
        { name: 'Pakistan', flag: '\u{1F1F5}\u{1F1F0}', url: '/en/pakistan/income-tax/', region: 'asia' },
        { name: 'Thailand', flag: '\u{1F1F9}\u{1F1ED}', url: '/en/thailand/income-tax/', region: 'asia' },
        { name: 'Philippines', flag: '\u{1F1F5}\u{1F1ED}', url: '/en/philippines/income-tax/', region: 'asia' },
        { name: 'Vietnam', flag: '\u{1F1FB}\u{1F1F3}', url: '/en/vietnam/income-tax/', region: 'asia' },
        { name: 'Dubai', flag: '\u{1F1E6}\u{1F1EA}', url: '/en/dubai/income-tax/', region: 'mena' },
        { name: 'Saudi Arabia', flag: '\u{1F1F8}\u{1F1E6}', url: '/en/saudi-arabia/income-tax/', region: 'mena' },
        { name: 'Qatar', flag: '\u{1F1F6}\u{1F1E6}', url: '/en/qatar/income-tax/', region: 'mena' },
        { name: 'Kuwait', flag: '\u{1F1F0}\u{1F1FC}', url: '/en/kuwait/income-tax/', region: 'mena' },
        { name: 'Egypt', flag: '\u{1F1EA}\u{1F1EC}', url: '/en/egypt/income-tax/', region: 'mena' },
        { name: 'Morocco', flag: '\u{1F1F2}\u{1F1E6}', url: '/en/morocco/income-tax/', region: 'mena' },
        { name: 'South Africa', flag: '\u{1F1FF}\u{1F1E6}', url: '/en/south-africa/income-tax/', region: 'other' },
        { name: 'Australia', flag: '\u{1F1E6}\u{1F1FA}', url: '/en/australia/income-tax/', region: 'other' },
        { name: 'New Zealand', flag: '\u{1F1F3}\u{1F1FF}', url: '/en/new-zealand/income-tax/', region: 'other' }
    ];

    var countries = isFr ? countriesFR : countriesEN;
    var regionLabels = isFr
        ? { popular: '\u2B50 Populaires', europe: '\u{1F30D} Europe', americas: '\u{1F30E} Ameriques', asia: '\u{1F30F} Asie-Pacifique', mena: '\u{1F3DC}\uFE0F Moyen-Orient & Afrique du Nord', other: '\u{1F310} Afrique & Oceanie' }
        : { popular: '\u2B50 Popular', europe: '\u{1F30D} Europe', americas: '\u{1F30E} Americas', asia: '\u{1F30F} Asia-Pacific', mena: '\u{1F3DC}\uFE0F Middle East & North Africa', other: '\u{1F310} Africa & Oceania' };

    var mobileList = document.getElementById('mobile-country-list');
    var mobileSearch = document.getElementById('mobile-country-search');
    var mobileNoResults = document.getElementById('mobile-no-results');

    function normalize(str) {
        return str.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    }

    function renderMobileCountries(filter) {
        filter = filter || '';
        var norm = normalize(filter);
        var filtered = countries.filter(function(c) { return normalize(c.name).indexOf(norm) !== -1; });

        if (filtered.length === 0) {
            if (mobileList) mobileList.innerHTML = '';
            if (mobileNoResults) mobileNoResults.classList.remove('hidden');
            return;
        }
        if (mobileNoResults) mobileNoResults.classList.add('hidden');

        var groups = {};
        filtered.forEach(function(c) {
            if (!groups[c.region]) groups[c.region] = [];
            groups[c.region].push(c);
        });

        var regionOrder = ['popular', 'europe', 'americas', 'asia', 'mena', 'other'];
        var html = '';
        regionOrder.forEach(function(region) {
            if (!groups[region]) return;
            html += '<div><div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 px-1">' + regionLabels[region] + '</div><div class="grid grid-cols-2 gap-0.5">';
            groups[region].forEach(function(c) {
                html += '<a href="' + c.url + '" class="flex items-center gap-1.5 text-sm text-slate-600 hover:text-slate-900 hover:bg-slate-50 py-1.5 px-2 rounded-lg transition-colors"><span>' + c.flag + '</span> ' + c.name + '</a>';
            });
            html += '</div></div>';
        });
        if (mobileList) mobileList.innerHTML = html;
    }

    if (mobileSearch) {
        mobileSearch.addEventListener('input', function() { renderMobileCountries(mobileSearch.value); });
    }
    renderMobileCountries();

    // Mobile menu toggle - lock body scroll (iOS Safari compatible)
    var mobileMenu = document.getElementById('mobile-menu');
    var mobileMenuBtn = document.getElementById('mobile-menu-btn');
    var savedScrollY = 0;

    function openMenu() {
        savedScrollY = window.scrollY;
        mobileMenu.classList.remove('hidden');
        document.body.style.position = 'fixed';
        document.body.style.top = '-' + savedScrollY + 'px';
        document.body.style.left = '0';
        document.body.style.right = '0';
        document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
        mobileMenu.classList.add('hidden');
        document.body.style.position = '';
        document.body.style.top = '';
        document.body.style.left = '';
        document.body.style.right = '';
        document.body.style.overflow = '';
        window.scrollTo(0, savedScrollY);
    }

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            if (mobileMenu.classList.contains('hidden')) {
                openMenu();
            } else {
                closeMenu();
            }
        });
    }
})();
