#!/usr/bin/env python3
"""Fix all SEO snippets to be within Google's ideal ranges (title: 50-60, desc: 150-160).
Run with --check to validate only, no argument to apply fixes."""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))

# Each entry: relative_path -> (new_title, new_description)
# Title MUST be 50-60 chars, Description MUST be 150-160 chars
FIXES = {
    # =====================================================================
    # ROOT REDIRECT PAGE
    # =====================================================================
    'index.html': (
        "NetSalaire - Simulateur d'Impôt et Salaire Net 2026",
        "Calculez gratuitement votre salaire net, impôt sur le revenu et cotisations sociales. Simulateurs pour la France, le Maroc et plus de 50 pays. Barèmes 2026.",
    ),

    # =====================================================================
    # ARABIC (5 pages)
    # =====================================================================
    'ar/arabie-saoudite/tax-calculator/index.html': (
        "حاسبة ضرائب السعودية 2026 - محاكاة ضريبية مجانية ودقيقة",
        "احسب ضرائبك في المملكة العربية السعودية مجاناً. محاكاة مفصلة مع ضريبة القيمة المضافة والزكاة والاشتراكات الاجتماعية. نتائج فورية حسب جداول 2026 الرسمية.",
    ),
    'ar/dubai/tax-calculator/index.html': (
        "حاسبة ضرائب دبي والإمارات 2026 - محاكاة مجانية ودقيقة",
        "احسب ضرائبك في دبي والإمارات العربية المتحدة مجاناً. محاكاة مفصلة مع ضريبة القيمة المضافة والرسوم. احسب راتبك الصافي فوراً حسب جداول 2026 الرسمية المعتمدة.",
    ),
    'ar/egypte/tax-calculator/index.html': (
        "حاسبة ضرائب مصر 2026 - محاكاة ضريبية مجانية ودقيقة",
        "احسب ضرائبك في جمهورية مصر العربية مجاناً. محاكاة مفصلة مع ضريبة الدخل التصاعدية والتأمينات الاجتماعية والتأمين الصحي. نتائج فورية حسب جداول 2026 الرسمية.",
    ),
    'ar/koweit/tax-calculator/index.html': (
        "حاسبة ضرائب الكويت 2026 - محاكاة مجانية ودقيقة للراتب",
        "احسب ضرائبك في دولة الكويت مجاناً. الكويت بدون ضريبة دخل شخصية على الأفراد. محاكاة مفصلة مع الاشتراكات الاجتماعية والتأمينات. نتائج حسب جداول 2026 الرسمية.",
    ),
    'ar/qatar/tax-calculator/index.html': (
        "حاسبة ضرائب قطر 2026 - محاكاة ضريبية مجانية ودقيقة",
        "احسب ضرائبك في دولة قطر مجاناً. قطر بدون ضريبة دخل شخصية على الأفراد. احسب راتبك الصافي فوراً. محاكاة مع الاشتراكات والرسوم الاجتماعية. جداول 2026 الرسمية.",
    ),

    # =====================================================================
    # CZECH (1 page)
    # =====================================================================
    'cs/cesko/danovy-kalkulator/index.html': (
        "Daňový Kalkulátor Česko 2026 - Bezplatný Výpočet Čisté Mzdy",
        "Vypočítejte si daně v České republice zcela zdarma. Podrobná simulace s daní z příjmu, sociálním a zdravotním pojištěním. Okamžité výsledky dle sazeb roku 2026.",
    ),

    # =====================================================================
    # DANISH (1 page)
    # =====================================================================
    'da/danmark/skatteberegner/index.html': (
        "Skatteberegner Danmark 2026 - Gratis og Præcis Beregning",
        "Beregn dine skatter i Danmark helt gratis. Detaljeret simulering med indkomstskat, kommuneskat, AM-bidrag og sociale bidrag. Resultater med 2026-satser.",
    ),

    # =====================================================================
    # GERMAN (3 pages)
    # =====================================================================
    'de/deutschland/einkommensteuer/index.html': (
        "Einkommensteuerrechner Deutschland 2026 - Kostenlos",
        "Berechnen Sie Ihre Steuern in Deutschland kostenlos. Simulation mit Einkommensteuer, Solidaritätszuschlag und Sozialabgaben. Ergebnisse mit Steuertarifen 2026.",
    ),
    'de/oesterreich/einkommensteuer/index.html': (
        "Einkommensteuerrechner Österreich 2026 - Kostenlos",
        "Berechnen Sie Ihre Steuern in Österreich kostenlos. Simulation mit Einkommensteuer, Sozialversicherung und Lohnnebenkosten. Ergebnisse mit Steuertarifen 2026.",
    ),
    'de/schweiz/einkommensteuer/index.html': (
        "Einkommensteuerrechner Schweiz 2026 - Kostenlose Berechnung",
        "Berechnen Sie Ihre Steuern in der Schweiz kostenlos. Simulation mit Einkommensteuer, AHV/IV/EO und Sozialabgaben. Sofortige Ergebnisse mit Steuertarifen 2026.",
    ),

    # =====================================================================
    # GREEK (1 page)
    # =====================================================================
    'el/ellada/ypologismos-forou/index.html': (
        "Υπολογισμός Φόρου Ελλάδα 2026 - Δωρεάν Υπολογισμός",
        "Υπολογίστε τους φόρους σας στην Ελλάδα εντελώς δωρεάν. Προσομοίωση με φόρο εισοδήματος, κοινωνικές εισφορές ΕΦΚΑ και εισφορά αλληλεγγύης. Κλίμακες 2026.",
    ),

    # =====================================================================
    # ENGLISH (35+ pages)
    # =====================================================================
    'en/argentina/income-tax/index.html': (
        "Argentina Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Argentine income tax for free. Detailed simulation with Impuesto a las Ganancias, ANSES contributions and social charges. 2026 rates included.",
    ),
    'en/australia/income-tax/index.html': (
        "Australia Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Australian income tax for free. Detailed simulation with progressive tax brackets, Medicare Levy and superannuation. 2026 rates included.",
    ),
    'en/austria/income-tax/index.html': (
        "Austria Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Austrian income tax for free. Detailed simulation with Einkommensteuer and social insurance contributions. Net salary with 2026 rates included.",
    ),
    'en/belgium/income-tax/index.html': (
        "Belgium Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Belgian income tax for free. Detailed simulation with IPP, RSZ/ONSS social contributions and net salary breakdown. Official 2026 rates included.",
    ),
    'en/brazil/income-tax/index.html': (
        "Brazil Income Tax Calculator IRPF 2026 - Free Online",
        "Calculate your Brazilian income tax (IRPF) for free. Simulation with official progressive brackets and INSS social contributions. Net salary. 2026 rates.",
    ),
    'en/chile/income-tax/index.html': (
        "Chile Income Tax Calculator 2026 - Free Tax Simulator",
        "Calculate your Chilean income tax for free. Detailed simulation with Impuesto a la Renta, AFP pension and social contributions. Official 2026 rates included.",
    ),
    'en/colombia/income-tax/index.html': (
        "Colombia Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Colombian income tax for free. Detailed simulation with Impuesto de Renta, pension, health contributions and FSP. 2026 UVT rates included.",
    ),
    'en/croatia/income-tax/index.html': (
        "Croatia Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Croatian income tax for free. Detailed simulation with Porez na dohodak, HZMO and HZZO social contributions. Eurozone 2026 rates included.",
    ),
    'en/czech-republic/income-tax/index.html': (
        "Czech Republic Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Czech income tax for free. Detailed simulation with 15%/23% flat rate system, OSSZ and VZP contributions. 2026 rates and brackets included.",
    ),
    'en/denmark/income-tax/index.html': (
        "Denmark Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Danish income tax for free. Detailed simulation with municipal tax, topskat, bundskat and AM-bidrag contributions. Official 2026 rates included.",
    ),
    'en/egypt/income-tax/index.html': (
        "Egypt Income Tax Calculator 2026 - Free Tax Simulator",
        "Calculate your Egyptian income tax for free. Detailed simulation with progressive tax rates, social insurance and health contributions. 2026 rates in EGP.",
    ),
    'en/france-morocco-comparison/index.html': (
        "France vs Morocco Tax Comparison 2026 | Free Simulator",
        "Compare your net salary and taxes between France and Morocco side by side. Personalized results based on your income and family situation. Free simulation.",
    ),
    'en/france/daycare-calculator/index.html': (
        "Daycare Cost Calculator France 2026 - Free Comparison",
        "Calculate and compare childcare costs after CAF benefits and tax credits. Public daycare, micro-daycare or registered childminder options in France 2026.",
    ),
    'en/france/unemployment-calculator/index.html': (
        "Unemployment Benefits Calculator ARE 2026 - Free & Instant",
        "Calculate your unemployment allowance and entitlements from France Travail (ARE). Simulator with 2026 rates and scales. Daily amount and duration included.",
    ),
    'en/greece/income-tax/index.html': (
        "Greece Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Greek income tax for free. Detailed simulation with progressive brackets, EFKA social contributions and solidarity tax. 2026 rates included.",
    ),
    'en/hungary/income-tax/index.html': (
        "Hungary Income Tax Calculator 2026 - Free SZJA Simulator",
        "Calculate your Hungarian income tax for free. Detailed simulation with SZJA 15% flat tax and TB social contributions. France-Hungary comparison. 2026.",
    ),
    'en/index.html': (
        "Tax & Gross ⇒ Net Salary Calculator 2026 | Free & Fast",
        "Calculate your taxes and gross to net salary for free in 2 clicks. Detailed simulation with hourly, monthly or annual breakdown. 2026 tax rates included.",
    ),
    'en/indonesia/income-tax/index.html': (
        "Indonesia Income Tax Calculator 2026 - Free PPh 21 Simulator",
        "Calculate your Indonesian income tax for free. Simulation with PPh 21 progressive brackets and BPJS social contributions. Official 2026 rates included.",
    ),
    'en/ireland/income-tax/index.html': (
        "Ireland Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Irish income tax for free. Detailed simulation with Income Tax, USC (Universal Social Charge) and PRSI contributions. 2026 rates included.",
    ),
    'en/italy/income-tax/index.html': (
        "Italy Income Tax Calculator 2026 - Free IRPEF Simulator",
        "Calculate your Italian income tax for free. Detailed simulation with IRPEF progressive brackets, INPS contributions and regional taxes. 2026 rates included.",
    ),
    'en/kuwait/income-tax/index.html': (
        "Kuwait Income Tax Calculator 2026 - Free Tax Simulator",
        "Calculate your Kuwait income tax for free. Kuwait has 0% personal income tax - one of the most tax-friendly countries in the world. 2026 rates included.",
    ),
    'en/legal-notice/index.html': (
        "Legal Notice & Privacy Policy - NetSalaire.com Simulators",
        "Legal information, publisher, hosting and privacy policy for NetSalaire.com. Free and reliable tax simulators for France, Morocco and 50+ countries included.",
    ),
    'en/malaysia/income-tax/index.html': (
        "Malaysia Income Tax Calculator 2026 - Free PCB Simulator",
        "Calculate your Malaysian income tax for free. Simulation with PCB monthly tax deduction, EPF and SOCSO social contributions. Official 2026 rates included.",
    ),
    'en/mexico/income-tax/index.html': (
        "Mexico Income Tax Calculator ISR 2026 - Free Online",
        "Calculate your Mexican income tax (ISR) for free. Simulation with progressive brackets and IMSS social contributions. Net salary. Official 2026 rates included.",
    ),
    'en/morocco/tax-guide/index.html': (
        "Morocco Tax Guide 2026 – CNSS, IR & Net Salary Explained",
        "CNSS, AMO, income tax brackets and deductions explained simply. The complete guide to Moroccan taxation you wish you had before working in Morocco. Year 2026.",
    ),
    'en/netherlands/income-tax/index.html': (
        "Netherlands Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Dutch income tax for free. Detailed simulation with loonbelasting brackets and social contributions. Net salary. Official 2026 rates included.",
    ),
    'en/new-zealand/income-tax/index.html': (
        "New Zealand Income Tax Calculator 2026 - Free PAYE Simulator",
        "Calculate your New Zealand income tax for free. Simulation with PAYE brackets, ACC levy and KiwiSaver contributions. Net salary. Official 2026 rates included.",
    ),
    'en/peru/income-tax/index.html': (
        "Peru Income Tax Calculator 2026 - Free Tax Simulator",
        "Calculate your Peruvian income tax for free. Detailed simulation with Impuesto a la Renta, UIT brackets, and ONP/AFP pension contributions. 2026 rates.",
    ),
    'en/philippines/income-tax/index.html': (
        "Philippines Income Tax Calculator 2026 - Free Online",
        "Calculate your Philippine income tax for free. Detailed simulation with TRAIN Law rates, SSS, PhilHealth, and Pag-IBIG contributions. 2026 rates included.",
    ),
    'en/poland/income-tax/index.html': (
        "Poland Income Tax Calculator 2026 - Free PIT Simulator",
        "Calculate your Polish income tax for free. Detailed simulation with PIT progressive brackets, ZUS social contributions and net salary. 2026 rates included.",
    ),
    'en/qatar/income-tax/index.html': (
        "Qatar Income Tax Calculator 2026 - Free Calculator (0% Tax)",
        "Calculate your net income in Qatar for free. 0% personal income tax with no social security for expats. QAR currency converter. Official 2026 rates included.",
    ),
    'en/romania/income-tax/index.html': (
        "Romania Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Romanian income tax for free. Simulation with 10% flat tax rate, CAS pension and CASS health social contributions. Official 2026 rates included.",
    ),
    'en/south-africa/income-tax/index.html': (
        "South Africa Income Tax Calculator 2026 - Free SARS",
        "Calculate your South African income tax for free. Simulation with SARS tax brackets, primary rebate and UIF contributions. Official 2026 rates included.",
    ),
    'en/south-korea/income-tax/index.html': (
        "South Korea Income Tax Calculator 2026 - Free Simulator",
        "Calculate your South Korean income tax for free. Simulation with progressive income tax brackets and social contributions. Official 2026 rates included.",
    ),
    'en/sweden/income-tax/index.html': (
        "Sweden Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Swedish income tax for free. Simulation with municipal tax, state tax and pension social contributions. Official 2026 rates and brackets.",
    ),
    'en/thailand/income-tax/index.html': (
        "Thailand Income Tax Calculator 2026 - Free PIT Simulator",
        "Calculate your Thai income tax for free. Simulation with PIT progressive brackets and Social Security Fund contributions. Official 2026 rates included.",
    ),
    'en/turkey/income-tax/index.html': (
        "Turkey Income Tax Calculator 2026 - Free Simulator",
        "Calculate your Turkish income tax for free. Simulation with Gelir Vergisi progressive brackets and SGK social contributions. Official 2026 rates included.",
    ),
    'en/vietnam/income-tax/index.html': (
        "Vietnam Income Tax Calculator 2026 - Free PIT Simulator",
        "Calculate your Vietnamese income tax for free. Simulation with PIT brackets, Social Insurance and Health Insurance contributions. Official 2026 rates included.",
    ),

    # =====================================================================
    # SPANISH (6 pages)
    # =====================================================================
    'es/argentina/simulador-impuestos/index.html': (
        "Simulador de Impuestos Argentina 2026 - Cálculo Gratuito",
        "Calcule sus impuestos en Argentina gratis. Simulación con Impuesto a las Ganancias, aportes jubilatorios y contribuciones ANSES. Escalas oficiales 2026.",
    ),
    'es/chile/simulador-impuestos/index.html': (
        "Simulador de Impuestos Chile 2026 - Cálculo Gratuito",
        "Calcule sus impuestos en Chile gratis. Simulación detallada con Impuesto a la Renta, AFP, FONASA o Isapre y cotizaciones sociales. Tablas del SII 2026.",
    ),
    'es/colombia/simulador-impuestos/index.html': (
        "Simulador de Impuestos Colombia 2026 - Cálculo Gratuito",
        "Calcule sus impuestos en Colombia gratis. Simulación con Impuesto de Renta, aportes a pensión, salud y Fondo de Solidaridad. Tarifas UVT oficiales 2026.",
    ),
    'es/espana/simulador-impuestos/index.html': (
        "Simulador de Impuestos España 2026 - Cálculo Gratuito",
        "Calcule sus impuestos en España gratis. Simulación detallada con IRPF, tramos estatales y autonómicos, cotizaciones Seguridad Social. Tablas oficiales 2026.",
    ),
    'es/mexico/simulador-impuestos/index.html': (
        "Simulador de Impuestos México 2026 - Cálculo Gratuito",
        "Calcule sus impuestos en México gratis. Simulación con ISR (Impuesto Sobre la Renta), cuotas IMSS y contribuciones sociales. Tablas oficiales del SAT 2026.",
    ),
    'es/peru/simulador-impuestos/index.html': (
        "Simulador de Impuestos Perú 2026 - Cálculo Gratuito",
        "Calcule sus impuestos en Perú gratis. Simulación con Impuesto a la Renta, aportes ONP o AFP, EsSalud y contribuciones sociales. Tablas oficiales SUNAT 2026.",
    ),

    # =====================================================================
    # FINNISH (1 page)
    # =====================================================================
    'fi/suomi/verolaskuri/index.html': (
        "Verolaskuri Suomi 2026 - Ilmainen ja Tarkka Verolaskenta",
        "Laske verot Suomessa ilmaiseksi. Yksityiskohtainen simulaatio tuloverolla, kunnallisverolla ja sosiaaliturvamaksuilla. Tulokset virallisilla veroprosenteilla.",
    ),

    # =====================================================================
    # FRENCH (40+ pages)
    # =====================================================================
    'fr/afrique-du-sud/simulateur-impot/index.html': (
        "Simulateur Impot Afrique du Sud 2026 - Calcul SARS Gratuit",
        "Calculez vos impots en Afrique du Sud gratuitement. Simulation avec baremes SARS, UIF et cotisations sociales. Resultat net instantane. Baremes 2026 officiels.",
    ),
    'fr/allemagne/simulateur-impot/index.html': (
        "Simulateur Impot Allemagne 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Allemagne gratuitement. Simulation detaillee avec Einkommensteuer, Solidaritatszuschlag et cotisations sociales. Baremes 2026 inclus.",
    ),
    'fr/arabie-saoudite/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Arabie Saoudite 2026 - Gratuit",
        "Calculez vos impôts en Arabie Saoudite gratuitement. Simulation avec TVA, Zakat et cotisations sociales GOSI. Résultat net instantané. Barèmes 2026 officiels.",
    ),
    'fr/argentine/simulateur-impot/index.html': (
        "Simulateur Impot Argentine 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Argentine gratuitement. Simulation avec Impuesto a las Ganancias, cotisations ANSES et charges sociales. Baremes 2026 officiels inclus.",
    ),
    'fr/australie/simulateur-impot/index.html': (
        "Simulateur Impot Australie 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Australie gratuitement. Simulation avec Income Tax, Medicare Levy et cotisations superannuation. Baremes 2026 en AUD inclus officiels.",
    ),
    'fr/autriche/simulateur-impot/index.html': (
        "Simulateur Impot Autriche 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Autriche gratuitement. Simulation avec Einkommensteuer, assurance sociale et cotisations patronales. Baremes 2026. Resultat net inclus.",
    ),
    'fr/belgique/simulateur-impot/index.html': (
        "Simulateur Impot Belgique 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Belgique gratuitement. Simulation avec IPP (Impot des Personnes Physiques), cotisations sociales RSZ/ONSS. Baremes 2026 officiels.",
    ),
    'fr/bresil/simulateur-impot/index.html': (
        "Simulateur Impot Bresil IRPF 2026 - Calcul Gratuit",
        "Calculez votre impot sur le revenu au Bresil (IRPF) gratuitement. Simulation avec baremes progressifs et cotisations INSS. Net en BRL. Baremes 2026 officiels.",
    ),
    'fr/canada/simulateur-impot/index.html': (
        "Simulateur Impot Canada 2026 - Calcul du Net Gratuit",
        "Calculez vos impots au Canada gratuitement. Simulation avec impot federal, provincial et cotisations sociales RPC et AE. Baremes 2026 en CAD inclus. Net.",
    ),
    'fr/chili/simulateur-impot/index.html': (
        "Simulateur Impot Chili 2026 - Calcul Salaire Net Gratuit",
        "Calculez vos impots au Chili gratuitement. Simulation avec Impuesto a la Renta, AFP retraite, FONASA ou Isapre sante. Baremes 2026 en CLP. Resultat net gratuit.",
    ),
    'fr/chine/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Chine 2026 - Calcul Gratuit",
        "Calculez vos impôts en Chine gratuitement. Simulation avec IIT (impôt sur le revenu individuel), assurance sociale et fonds de logement. Barèmes 2026.",
    ),
    'fr/coree-du-sud/simulateur-impot/index.html': (
        "Simulateur Impot Coree du Sud 2026 - Calcul Gratuit",
        "Calculez vos impots en Coree du Sud gratuitement. Simulation avec impot progressif sur le revenu, retraite nationale et assurance sante. Baremes 2026.",
    ),
    'fr/croatie/simulateur-impot/index.html': (
        "Simulateur Impot Croatie 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Croatie gratuitement. Simulation avec Porez na dohodak, cotisations HZMO retraite et HZZO sante. Baremes officiels 2026 en euros.",
    ),
    'fr/danemark/simulateur-impot/index.html': (
        "Simulateur Impot Danemark 2026 - Calcul Net Gratuit",
        "Calculez vos impots au Danemark gratuitement. Simulation avec impot municipal, topskat, bundskat et AM-bidrag. Baremes 2026 en DKK. Resultat net instantane.",
    ),
    'fr/dubai/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Dubai EAU 2026 - Calcul Gratuit",
        "Calculez vos impôts à Dubai et aux Émirats Arabes Unis gratuitement. Simulation avec TVA 5% et absence d'impôt sur le revenu. Barèmes 2026 officiels inclus.",
    ),
    'fr/egypte/simulateur-impot/index.html': (
        "Simulateur Impot Egypte 2026 - Calcul Gratuit en EGP",
        "Calculez vos impots en Egypte gratuitement. Simulation avec baremes progressifs, cotisations sociales NOSI et assurance maladie. Baremes 2026 en EGP inclus.",
    ),
    'fr/espagne/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Espagne 2026 - Calcul Gratuit",
        "Calculez vos impôts en Espagne gratuitement. Simulation avec IRPF, tranches étatiques et autonomiques, cotisations Seguridad Social. Barèmes 2026 officiels.",
    ),
    'fr/faq/index.html': (
        "FAQ Salaire Brut en Net & Impôts – Toutes les Réponses",
        "Brut vs net ? Cadre vs non-cadre ? Différence France/Maroc ? Défiscalisation et réductions d'impôt ? Toutes les réponses simples aux questions courantes.",
    ),
    'fr/finlande/simulateur-impot/index.html': (
        "Simulateur Impot Finlande 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Finlande gratuitement. Simulation avec impot municipal, impot national progressif et cotisations sociales. Baremes 2026 en EUR.",
    ),
    'fr/france/creche-tarifs/index.html': (
        "Simulateur Tarif Crèche et Garde 2026 - Comparateur",
        "Calculez et comparez le coût réel de garde après aides CAF et crédit d'impôt. Crèche municipale, micro-crèche ou assistante maternelle agréée. Tarifs 2026.",
    ),
    'fr/france/guide/index.html': (
        "Guide Fiscal France 2026 – Tout Comprendre en 5 Minutes",
        "Cotisations sociales, tranches d'impôt sur le revenu, prélèvement à la source, CSG et CRDS expliqués simplement. Guide fiscal France complet et gratuit 2026.",
    ),
    'fr/france/simulateur-chomage-are/index.html': (
        "Simulateur Chomage ARE 2026 - Calcul Gratuit et Instantane",
        "Calculez votre indemnité chômage et droits ARE de France Travail. Simulateur gratuit avec barèmes 2026. Montant journalier, durée et délai de carence.",
    ),
    'fr/france/simulateur-impot-revenu/index.html': (
        "Simulateur Impôt sur le Revenu 2026 | Rapide et Précis",
        "Calculez votre impôt sur le revenu et réductions : PER, frais de garde, dons, emploi à domicile et frais de scolarité. Simulation gratuite. Barèmes 2026.",
    ),
    'fr/france/simulateur-indemnite-licenciement/index.html': (
        "Calcul Indemnite Licenciement 2026 - Simulateur Gratuit",
        "Calculez votre indemnité de licenciement légale ou conventionnelle gratuitement. Simulation selon ancienneté, salaire et convention collective. Baremes 2026.",
    ),
    'fr/france/simulateur-salaire-brut-net/index.html': (
        "Simulateur Salaire Brut Net 2026 → Calcul Gratuit Instantané",
        "Convertissez votre salaire brut en net selon votre statut cadre ou non-cadre. Simulation horaire, mensuelle ou annuelle. Barèmes URSSAF 2026 officiels.",
    ),
    'fr/grece/simulateur-impot/index.html': (
        "Simulateur Impot Grece 2026 - Calcul du Net Gratuit",
        "Calculez vos impots en Grece gratuitement. Simulation detaillee avec bareme progressif, cotisations EFKA et contribution de solidarite. Baremes 2026 inclus.",
    ),
    'fr/hong-kong/simulateur-impot/index.html': (
        "Simulateur Impot Hong Kong 2026 - Calcul Net Gratuit",
        "Calculez vos impots a Hong Kong gratuitement. Simulation avec impot progressif ou taux standard 15%, cotisations MPF retraite. Baremes 2026 en HKD officiels.",
    ),
    'fr/hongrie/simulateur-impot/index.html': (
        "Simulateur Impot Hongrie 2026 - Calcul SZJA Gratuit",
        "Calculez vos impots en Hongrie gratuitement. Simulation avec SZJA 15% taux unique et cotisations sociales TB. Comparaison France-Hongrie. Baremes 2026.",
    ),
    'fr/inde/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Inde 2026 - Calcul gratuit",
        "Calculez vos impôts en Inde gratuitement. Simulation avec barèmes progressifs, PF (Provident Fund), ESI et cotisations sociales. Résultat net en INR 2026.",
    ),
    'fr/indonesie/simulateur-impot/index.html': (
        "Simulateur Impot Indonesie 2026 - Calcul PPh 21 Gratuit",
        "Calculez vos impots en Indonesie gratuitement. Simulation avec PPh 21 progressif, cotisations BPJS sante et emploi. Salaire net en IDR. Baremes 2026 officiels.",
    ),
    'fr/irlande/simulateur-impot/index.html': (
        "Simulateur Impot Irlande 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Irlande gratuitement. Simulation avec Income Tax, USC (Universal Social Charge) et PRSI cotisations. Baremes 2026 en EUR officiels.",
    ),
    'fr/italie/simulateur-impot/index.html': (
        "Simulateur Impot Italie 2026 - Calcul Gratuit IRPEF",
        "Calculez vos impots en Italie gratuitement. Simulation avec IRPEF progressif, cotisations INPS et impots regionaux et communaux. Baremes 2026 inclus officiels.",
    ),
    'fr/japon/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Japon 2026 - Calcul Gratuit",
        "Calculez vos impôts au Japon gratuitement. Simulation avec impôt sur le revenu progressif, cotisations retraite et assurance santé. Net en JPY. Baremes 2026.",
    ),
    'fr/koweit/simulateur-impot/index.html': (
        "Simulateur Impot Koweit 2026 - 0% Tax Free Gratuit",
        "Calculez votre salaire net au Koweit gratuitement. Pays sans impot sur le revenu (0% tax free), seules les cotisations PIFSS s'appliquent. Baremes 2026.",
    ),
    'fr/luxembourg/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Luxembourg 2026 - Gratuit",
        "Calculez vos impôts au Luxembourg gratuitement. Simulation avec barèmes progressifs, cotisations sociales CNS et assurance dépendance. Barèmes 2026 officiels.",
    ),
    'fr/malaisie/simulateur-impot/index.html': (
        "Simulateur Impot Malaisie 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Malaisie gratuitement. Simulation detaillee avec tranches progressives 0-30%, EPF, SOCSO et cotisations sociales. Baremes 2026 inclus.",
    ),
    'fr/maroc/guide/index.html': (
        "Guide Fiscal Maroc 2026 – CNSS, IR et Salaire Net Expliqués",
        "CNSS, AMO, tranches IR impôt sur le revenu au Maroc expliqués simplement. Le guide fiscal complet et gratuit pour comprendre la fiscalité marocaine 2026.",
    ),
    'fr/mexique/simulateur-impot/index.html': (
        "Simulateur Impot Mexique ISR 2026 - Calcul Gratuit",
        "Calculez votre impot au Mexique (ISR) gratuitement. Simulation avec baremes progressifs officiels et cotisations IMSS. Net en MXN. Baremes 2026 officiels.",
    ),
    'fr/norvege/simulateur-impot/index.html': (
        "Simulateur Impot Norvege 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Norvege gratuitement. Simulation avec trinnskatt impot progressif et trygdeavgift cotisations sociales. Baremes 2026 en NOK officiels.",
    ),
    'fr/nouvelle-zelande/simulateur-impot/index.html': (
        "Simulateur Impot Nouvelle-Zelande 2026 - Calcul PAYE Gratuit",
        "Calculez vos impots en Nouvelle-Zelande gratuitement. Simulation avec PAYE, ACC levy et KiwiSaver cotisations retraite. Net en NZD. Baremes 2026 officiels.",
    ),
    'fr/pakistan/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Pakistan 2026 - Calcul Gratuit",
        "Calculez vos impôts au Pakistan gratuitement. Simulation avec barèmes progressifs FBR, cotisations EOBI et sécurité sociale. Net en PKR. Barèmes 2026.",
    ),
    'fr/pays-bas/simulateur-impot/index.html': (
        "Simulateur Impot Pays-Bas 2026 - Calcul Net Gratuit",
        "Calculez vos impots aux Pays-Bas gratuitement. Simulation avec loonbelasting progressif et cotisations volksverzekeringen. Baremes 2026 en EUR inclus.",
    ),
    'fr/perou/simulateur-impot/index.html': (
        "Simulateur Impot Perou 2026 - Calcul du Net Gratuit",
        "Calculez vos impots au Perou gratuitement. Simulation avec Impuesto a la Renta progressif, cotisations ONP ou AFP et EsSalud. Baremes 2026 en PEN officiels.",
    ),
    'fr/pologne/simulateur-impot/index.html': (
        "Simulateur Impot Pologne 2026 - Calcul PIT Gratuit",
        "Calculez vos impots en Pologne gratuitement. Simulation avec PIT progressif 12%/32%, ZUS et cotisations sociales sante. Net en PLN. Baremes 2026 officiels.",
    ),
    'fr/politique-confidentialite/index.html': (
        "Politique de Confidentialité – NetSalaire.com - simulateur",
        "Découvrez comment NetSalaire.com protège vos données. Aucune donnée stockée, calculs effectués localement dans votre navigateur. Conforme RGPD et sécurisé.",
    ),
    'fr/portugal/simulateur-impot/index.html': (
        "Simulateur Impot Portugal 2026 - Calcul Net Gratuit",
        "Calculez vos impots au Portugal gratuitement. Simulation avec IRS (Imposto sobre o Rendimento) et cotisations sociales. Baremes 2026 en EUR. Resultat net.",
    ),
    'fr/qatar/simulateur-impot/index.html': (
        "Simulateur Impot Qatar 2026 - Calcul Gratuit (0% Impot)",
        "Calculez votre salaire net au Qatar gratuitement. 0% d'impôt sur le revenu, aucune cotisation sociale pour les expatriés. Barèmes officiels 2026 en QAR.",
    ),
    'fr/roumanie/simulateur-impot/index.html': (
        "Simulateur Impot Roumanie 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Roumanie gratuitement. Simulation avec taux unique de 10%, cotisations CAS retraite et CASS sante. Net en RON. Baremes 2026 officiels.",
    ),
    'fr/royaume-uni/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Royaume-Uni UK 2026 - Gratuit",
        "Calculez vos impôts au Royaume-Uni gratuitement. Simulation avec Income Tax, National Insurance et cotisations pension. Net en GBP. Barèmes 2026 officiels.",
    ),
    'fr/singapour/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Singapour 2026 - Calcul Gratuit",
        "Calculez vos impôts à Singapour gratuitement. Simulation avec barèmes progressifs IRAS, CPF et cotisations sociales. Net en SGD. Barèmes 2026 officiels inclus.",
    ),
    'fr/suede/simulateur-impot/index.html': (
        "Simulateur Impot Suede 2026 - Calcul du Net Gratuit",
        "Calculez vos impots en Suede gratuitement. Simulation avec impot municipal, impot national progressif et cotisations retraite. Baremes 2026 en SEK officiels.",
    ),
    'fr/suisse/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe Suisse 2026 - Calcul Gratuit",
        "Calculez vos impôts en Suisse gratuitement. Simulation avec impôt fédéral, cantonal, communal et cotisations AVS/AI/APG. Net en CHF. Barèmes 2026 officiels.",
    ),
    'fr/tchequie/simulateur-impot/index.html': (
        "Simulateur Impot Tchequie 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Republique tcheque gratuitement. Simulation detaillee avec taux forfaitaire 15%/23%, cotisations OSSZ et VZP. Baremes 2026 inclus.",
    ),
    'fr/thailande/simulateur-impot/index.html': (
        "Simulateur Impot Thailande 2026 - Calcul Net Gratuit",
        "Calculez vos impots en Thailande gratuitement. Simulation avec baremes progressifs 0-35% et cotisations sociales SSO. Net en THB. Baremes 2026 officiels inclus.",
    ),
    'fr/usa/simulateur-impot/index.html': (
        "Simulateur Impôt et taxe USA États-Unis 2026 - Gratuit",
        "Calculez vos impôts aux USA gratuitement. Simulation avec Federal Income Tax, State Tax, Social Security et Medicare. Net en USD. Barèmes 2026 officiels inclus.",
    ),
    'fr/vietnam/simulateur-impot/index.html': (
        "Simulateur Impot Vietnam 2026 - Calcul Net Gratuit",
        "Calculez vos impots au Vietnam gratuitement. Simulation avec TNCN impot sur le revenu, BHXH assurance sociale et cotisations. Baremes 2026 en VND officiels.",
    ),

    # =====================================================================
    # CROATIAN (1 page)
    # =====================================================================
    'hr/hrvatska/porezni-kalkulator/index.html': (
        "Porezni Kalkulator Hrvatska 2026 - Besplatno Izračunavanje",
        "Izračunajte svoje poreze u Hrvatskoj besplatno. Detaljna simulacija s porezom na dohodak, prirezom, HZMO i HZZO doprinosima. Rezultati prema stopama 2026.",
    ),

    # =====================================================================
    # HUNGARIAN (1 page)
    # =====================================================================
    'hu/magyarorszag/ado-kalkulator/index.html': (
        "Adókalkulátor Magyarország 2026 - Ingyenes Számítás Nettó",
        "Számítsa ki adóit Magyarországon ingyenesen. Részletes szimuláció személyi jövedelemadóval és társadalombiztosítási járulékokkal. Nettó fizetés. 2026.",
    ),

    # =====================================================================
    # INDONESIAN (1 page)
    # =====================================================================
    'id/indonesia/kalkulator-pajak/index.html': (
        "Kalkulator Pajak Indonesia 2026 - Perhitungan Gratis Online",
        "Hitung pajak Anda di Indonesia gratis. Simulasi terperinci dengan PPh 21 pajak penghasilan, iuran BPJS Kesehatan dan Ketenagakerjaan. Tarif resmi 2026.",
    ),

    # =====================================================================
    # ITALIAN (1 page)
    # =====================================================================
    'it/italia/calcolatore-imposte/index.html': (
        "Calcolatore Imposte Italia 2026 - Calcolo Gratuito Online",
        "Calcola le tue tasse in Italia gratis. Simulazione con IRPEF progressiva, contributi INPS, addizionali regionali e comunali. Aliquote ufficiali del 2026.",
    ),

    # =====================================================================
    # JAPANESE (1 page)
    # =====================================================================
    'ja/nihon/zeikin-keisan/index.html': (
        "税金計算シミュレーター 日本 2026年度版 - 完全無料で所得税・住民税・社会保険料をオンラインで即時に計算",
        "日本の税金を完全無料で正確に計算できるオンラインシミュレーターです。所得税、住民税、厚生年金保険料、健康保険料、介護保険料、雇用保険料を含む詳細な計算結果をすぐに確認できます。2026年度の最新税率・控除額に完全対応。毎月の手取り額から年間の納税額まで、給与明細の全項目を網羅した包括的なシミュレーションツールです。",
    ),

    # =====================================================================
    # KOREAN (1 page)
    # =====================================================================
    'ko/hanguk/segeum-gyesan/index.html': (
        "세금 계산기 한국 2026년 - 소득세 주민세 국민연금 건강보험 고용보험 무료 계산 시뮬레이터 도구",
        "한국의 세금을 완전 무료로 정확하게 계산하세요. 소득세, 주민세, 국민연금, 건강보험, 고용보험, 장기요양보험의 상세 시뮬레이션을 제공합니다. 2026년 최신 세율과 공제 항목을 반영하여 실수령액을 즉시 확인할 수 있는 편리한 온라인 계산 도구입니다. 급여 내역 상세 분석도 제공합니다.",
    ),

    # =====================================================================
    # MALAY (1 page)
    # =====================================================================
    'ms/malaysia/kalkulator-cukai/index.html': (
        "Kalkulator Cukai Malaysia 2026 - Pengiraan Percuma Online",
        "Kira cukai anda di Malaysia secara percuma. Simulasi terperinci dengan cukai pendapatan PCB, caruman KWSP, PERKESO dan EIS. Kadar rasmi 2026. Gaji bersih.",
    ),

    # =====================================================================
    # DUTCH (2 pages)
    # =====================================================================
    'nl/belgie/belasting-berekenen/index.html': (
        "Belastingcalculator België 2026 - Gratis Netto Berekening",
        "Bereken uw belastingen in België gratis. Simulatie met personenbelasting, RSZ sociale bijdragen en bedrijfsvoorheffing. Nettoloon direct. Tarieven 2026.",
    ),
    'nl/nederland/belasting-berekenen/index.html': (
        "Belastingcalculator Nederland 2026 - Gratis Netto Berekening",
        "Bereken uw belastingen in Nederland gratis. Simulatie met inkomstenbelasting, premies volksverzekeringen en nettoloon berekening. Officiële tarieven 2026.",
    ),

    # =====================================================================
    # NORWEGIAN (1 page)
    # =====================================================================
    'no/norge/skattekalkulator/index.html': (
        "Skattekalkulator Norge 2026 - Gratis og Nøyaktig Beregning",
        "Beregn skattene dine i Norge helt gratis. Detaljert simulering med trinnskatt, trygdeavgift, kommuneskatt og sosiale avgifter. Resultater med 2026-satser.",
    ),

    # =====================================================================
    # POLISH (1 page)
    # =====================================================================
    'pl/polska/kalkulator-podatkowy/index.html': (
        "Kalkulator Podatkowy Polska 2026 - Bezpłatne Obliczenie",
        "Oblicz swoje podatki w Polsce za darmo. Symulacja z podatkiem dochodowym PIT, składkami ZUS i ubezpieczeniem zdrowotnym. Oficjalne stawki podatkowe 2026.",
    ),

    # =====================================================================
    # PORTUGUESE (2 pages)
    # =====================================================================
    'pt/brasil/simulador-impostos/index.html': (
        "Simulador de Impostos Brasil 2026 - Cálculo Gratuito IRPF",
        "Calcule seus impostos no Brasil gratis. Simulação com IRPF, faixas progressivas oficiais e contribuições INSS. Salário líquido. Tabelas da Receita 2026.",
    ),
    'pt/portugal/simulador-impostos/index.html': (
        "Simulador de Impostos Portugal 2026 - Cálculo Gratuito IRS",
        "Calcule seus impostos em Portugal gratis. Simulação com IRS, escalões progressivos e contribuições Segurança Social. Salário líquido. Tabelas 2026 incluídas.",
    ),

    # =====================================================================
    # ROMANIAN (1 page)
    # =====================================================================
    'ro/romania/calculator-impozit/index.html': (
        "Calculator Impozit România 2026 - Calcul Gratuit Salariu Net",
        "Calculați impozitele în România gratuit. Simulare cu impozit pe venit 10%, contribuții CAS pensie și CASS sănătate. Salariu net instant. Cote oficiale 2026.",
    ),

    # =====================================================================
    # SWEDISH (1 page)
    # =====================================================================
    'sv/sverige/skatteberaknare/index.html': (
        "Skatteberäknare Sverige 2026 - Gratis och Exakt Beräkning",
        "Beräkna dina skatter i Sverige gratis. Detaljerad simulering med kommunalskatt, statlig inkomstskatt och sociala avgifter. Resultat med 2026 skattesatser.",
    ),

    # =====================================================================
    # THAI (1 page)
    # =====================================================================
    'th/prathet-thai/khamnuan-phasi/index.html': (
        "คำนวณภาษี ประเทศไทย 2026 - เครื่องคำนวณภาษีเงินได้ฟรี ทันที",
        "คำนวณภาษีของคุณในประเทศไทยฟรี การจำลองพร้อมภาษีเงินได้บุคคลธรรมดา เงินสมทบประกันสังคม และกองทุนสำรองเลี้ยงชีพ ผลลัพธ์ทันทีตามอัตราภาษี 2026 คำนวณเงินเดือนสุทธิ",
    ),

    # =====================================================================
    # TURKISH (1 page)
    # =====================================================================
    'tr/turkiye/vergi-hesaplama/index.html': (
        "Vergi Hesaplama Türkiye 2026 - Ücretsiz ve Hızlı Hesaplama",
        "Türkiye vergilerinizi tamamen ücretsiz hesaplayın. Gelir vergisi, SGK primleri ve damga vergisi ile detaylı simülasyon. 2026 yılı güncel oran ve dilimleri.",
    ),

    # =====================================================================
    # VIETNAMESE (1 page)
    # =====================================================================
    'vi/viet-nam/tinh-thue/index.html': (
        "Tính Thuế Việt Nam 2026 - Công Cụ Tính Thuế TNCN Miễn Phí",
        "Tính thuế của bạn tại Việt Nam hoàn toàn miễn phí. Mô phỏng chi tiết với thuế thu nhập cá nhân TNCN, bảo hiểm xã hội BHXH và bảo hiểm y tế. Biểu thuế 2026.",
    ),

    # =====================================================================
    # CHINESE (1 page)
    # =====================================================================
    'zh/zhongguo/shuishou-jisuan/index.html': (
        "税收计算器 中国 2026年度版 - 完全免费在线精准计算个人所得税五险一金社保公积金和实际到手工资",
        "完全免费在线计算中国的个人所得税和五险一金详细金额。包含养老保险、医疗保险、失业保险、工伤保险、生育保险和住房公积金的精准模拟计算工具。完全支持2026年最新个人所得税税率表和各类专项附加扣除政策。即时在线查看每月税后实际到手工资金额、各项社保公积金扣除明细和全年度累计纳税总额。适用于工薪阶层和自由职业者。",
    ),
}


def validate_fixes():
    """Validate all title/desc lengths are in range."""
    errors = []
    for path, (title, desc) in FIXES.items():
        tLen = len(title)
        dLen = len(desc)
        issues = []
        if not (50 <= tLen <= 60):
            issues.append(f"title={tLen}")
        if not (150 <= dLen <= 160):
            issues.append(f"desc={dLen}")
        if issues:
            errors.append((path, tLen, dLen, ', '.join(issues), title, desc))
    return errors


def apply_fixes():
    """Apply all fixes to HTML files."""
    applied = 0
    skipped = 0
    for rel_path, (new_title, new_desc) in FIXES.items():
        filepath = os.path.join(BASE, rel_path)
        if not os.path.exists(filepath):
            print(f"  SKIP (not found): {rel_path}")
            skipped += 1
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace title
        new_content = re.sub(
            r'<title>.*?</title>',
            f'<title>{new_title}</title>',
            content,
            count=1,
            flags=re.DOTALL
        )

        # Replace meta description (use [^"]* to avoid matching apostrophes inside content)
        new_content = re.sub(
            r'(<meta\s+name=["\']description["\']\s+content=")([^"]*)"',
            rf'\g<1>{new_desc}"',
            new_content,
            count=1,
            flags=re.DOTALL
        )

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            applied += 1
        else:
            print(f"  NO CHANGE: {rel_path}")
            skipped += 1

    return applied, skipped


if __name__ == '__main__':
    check_only = '--check' in sys.argv

    print(f"Total fixes defined: {len(FIXES)}")
    print()

    # Validate
    errors = validate_fixes()
    if errors:
        print(f"VALIDATION ERRORS ({len(errors)}):")
        for path, tLen, dLen, issues, title, desc in errors:
            print(f"  {path}: {issues}")
            if 'title' in issues:
                print(f"    TITLE ({tLen}): {title}")
            if 'desc' in issues:
                print(f"    DESC ({dLen}): {desc}")
        print()
        if not check_only:
            print("Fix validation errors before applying!")
            sys.exit(1)
    else:
        print("All lengths validated OK (title: 50-60, desc: 150-160)")

    if check_only:
        print("\n--check mode, not applying changes.")
        sys.exit(0)

    # Apply
    print("\nApplying fixes...")
    applied, skipped = apply_fixes()
    print(f"\nDone! Applied: {applied}, Skipped: {skipped}")
