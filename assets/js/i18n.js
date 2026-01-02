/**
 * NetSalaire - Internationalization (i18n) System
 * Supports: French (fr), English (en)
 * Complete translations for all pages
 */

const translations = {
    // ==========================================
    // COMMON / NAVIGATION
    // ==========================================
    'nav.france_vs_maroc': { fr: 'France vs Maroc', en: 'France vs Morocco' },
    'nav.global_comparator': { fr: 'Comparateur Global', en: 'Global Comparator' },
    'nav.france': { fr: 'France', en: 'France' },
    'nav.maroc': { fr: 'Maroc', en: 'Morocco' },
    'nav.faq': { fr: 'FAQ', en: 'FAQ' },
    'nav.contact': { fr: 'Contact', en: 'Contact' },
    'nav.brut_to_net': { fr: 'Brut vers Net', en: 'Gross to Net' },
    'nav.tax_simulator': { fr: 'Simulateur Impôt', en: 'Tax Simulator' },
    'nav.fiscal_guide': { fr: 'Guide Fiscal', en: 'Tax Guide' },
    'nav.comparator': { fr: 'Comparateur', en: 'Comparator' },

    // ==========================================
    // HOMEPAGE - Hero
    // ==========================================
    'home.badge': { fr: 'Barèmes fiscaux 2025', en: '2025 Tax Rates' },
    'home.title1': { fr: 'Calculez votre', en: 'Calculate your' },
    'home.title2': { fr: 'salaire net en 2 clics.', en: 'net salary in 2 clicks.' },
    'home.subtitle': {
        fr: 'Simulateurs fiscaux gratuits pour la France et le Maroc. Calculez salaires, impôts et comparez la pression fiscale entre les deux pays.',
        en: 'Free tax simulators for France and Morocco. Calculate salaries, taxes and compare the tax burden between both countries.'
    },
    'home.compare_btn': { fr: 'Comparer France vs Maroc', en: 'Compare France vs Morocco' },

    // HOMEPAGE - France Section
    'home.france_tools': { fr: 'Outils dédiés à la législation française', en: 'Tools dedicated to French legislation' },
    'home.brut_net_title': { fr: 'Salaire Brut à Net', en: 'Gross to Net Salary' },
    'home.brut_net_desc': {
        fr: 'Calcul précis du salaire net avant et après impôt. Prise en charge des statuts cadre et non-cadre.',
        en: 'Precise calculation of net salary before and after tax. Supports executive and non-executive status.'
    },
    'home.ir_title_fr': { fr: 'Simulateur Impôt sur le Revenu', en: 'Income Tax Simulator' },
    'home.ir_desc_fr': {
        fr: 'Estimation avec barème progressif, quotient familial et décotes en vigueur.',
        en: 'Estimate with progressive scale, family quotient and applicable rebates.'
    },
    'home.guide_title_fr': { fr: 'Guide Fiscal France 2025', en: 'France Tax Guide 2025' },
    'home.guide_desc_fr': {
        fr: 'Tout comprendre sur la fiscalité française : cotisations sociales, quotient familial, tranches IR, optimisation fiscale.',
        en: 'Understand everything about French taxation: social contributions, family quotient, tax brackets, tax optimization.'
    },

    // HOMEPAGE - Maroc Section
    'home.maroc_tools': { fr: 'Fiscalité et prélèvement à la source', en: 'Taxation and withholding tax' },
    'home.ir_title_ma': { fr: 'Simulateur Impôt sur le Revenu', en: 'Income Tax Simulator' },
    'home.ir_desc_ma': {
        fr: 'Calcul complet avec CNSS, AMO, frais professionnels et abattement familial. Barèmes 2025.',
        en: 'Complete calculation with CNSS, AMO, professional expenses and family allowance. 2025 rates.'
    },
    'home.guide_title_ma': { fr: 'Guide Fiscal Maroc 2025', en: 'Morocco Tax Guide 2025' },
    'home.guide_desc_ma': {
        fr: 'Tout comprendre sur la fiscalité marocaine : CNSS, AMO, tranches IR, abattements.',
        en: 'Understand everything about Moroccan taxation: CNSS, AMO, tax brackets, allowances.'
    },

    // HOMEPAGE - Comparators Section
    'home.comparators_title': { fr: 'Comparateurs Internationaux', en: 'International Comparators' },
    'home.comparators_subtitle': { fr: 'Analyse croisée des régimes fiscaux', en: 'Cross-analysis of tax systems' },
    'home.compare_fr_ma': { fr: 'France vs Maroc', en: 'France vs Morocco' },
    'home.compare_fr_ma_desc': {
        fr: 'Comparaison détaillée entre la France et le Maroc. Cotisations, IR, quotient familial.',
        en: 'Detailed comparison between France and Morocco. Contributions, income tax, family quotient.'
    },
    'home.compare_btn_short': { fr: 'Comparer', en: 'Compare' },
    'home.global_title': { fr: 'Comparateur Global', en: 'Global Comparator' },
    'home.global_desc': {
        fr: 'Comparez 5 pays : France, Maroc, Dubaï, Genève et Luxembourg. Trouvez le meilleur net !',
        en: 'Compare 5 countries: France, Morocco, Dubai, Geneva and Luxembourg. Find the best net!'
    },
    'home.launch_comparator': { fr: 'Lancer le comparateur', en: 'Launch comparator' },
    'home.new': { fr: 'NOUVEAU', en: 'NEW' },

    // HOMEPAGE - FAQ Section
    'faq.title': { fr: 'Questions Fréquentes', en: 'Frequently Asked Questions' },
    'faq.q1': { fr: 'Comment fonctionne le comparateur pays ?', en: 'How does the country comparator work?' },
    'faq.a1': {
        fr: 'Le comparateur calcule simultanément votre salaire net et votre pression fiscale totale dans les deux pays, pour un même salaire brut. Il utilise le taux de change en temps réel pour convertir les montants.',
        en: 'The comparator simultaneously calculates your net salary and total tax burden in both countries, for the same gross salary. It uses real-time exchange rates to convert amounts.'
    },
    'faq.q2': { fr: 'Les calculs sont-ils fiables ?', en: 'Are the calculations reliable?' },
    'faq.a2': {
        fr: 'Nos simulateurs utilisent les barèmes officiels 2025 publiés par les administrations fiscales française et marocaine. Cependant, ils fournissent une estimation et ne remplacent pas un conseil fiscal personnalisé.',
        en: 'Our simulators use the official 2025 rates published by the French and Moroccan tax authorities. However, they provide an estimate and do not replace personalized tax advice.'
    },
    'faq.q3': { fr: 'Puis-je simuler un statut cadre en France ?', en: 'Can I simulate executive status in France?' },
    'faq.a3': {
        fr: 'Tout à fait. Le calculateur "Salaire Brut à Net" pour la France dispose d\'une option pour basculer entre statut Cadre et Non-Cadre, ajustant ainsi les cotisations de retraite complémentaire.',
        en: 'Absolutely. The "Gross to Net Salary" calculator for France has an option to switch between Executive and Non-Executive status, adjusting supplementary pension contributions.'
    },
    'faq.q4': { fr: 'Mes données sont-elles stockées ?', en: 'Is my data stored?' },
    'faq.a4': {
        fr: 'Non. Tous les calculs sont effectués localement dans votre navigateur. Aucune donnée personnelle n\'est envoyée à nos serveurs ni stockée. Vous pouvez utiliser nos outils en toute confidentialité.',
        en: 'No. All calculations are performed locally in your browser. No personal data is sent to our servers or stored. You can use our tools with complete privacy.'
    },
    'faq.see_all': { fr: 'Voir toutes les questions', en: 'See all questions' },

    // HOMEPAGE - Reassurance
    'reassurance.secure': { fr: '100% Sécurisé', en: '100% Secure' },
    'reassurance.secure_desc': { fr: 'Aucune donnée stockée', en: 'No data stored' },
    'reassurance.official': { fr: 'Barèmes Officiels', en: 'Official Rates' },
    'reassurance.official_desc': { fr: 'Mis à jour 2025', en: 'Updated 2025' },
    'reassurance.instant': { fr: 'Instantané', en: 'Instant' },
    'reassurance.instant_desc': { fr: 'Calculs en temps réel', en: 'Real-time calculations' },
    'reassurance.free': { fr: 'Gratuit', en: 'Free' },
    'reassurance.free_desc': { fr: 'Sans pub ni inscription', en: 'No ads or registration' },

    // HOMEPAGE - Contact
    'contact.title': { fr: 'Une question ?', en: 'Have a question?' },
    'contact.subtitle': { fr: 'Contactez-nous, nous vous répondrons rapidement.', en: 'Contact us, we will respond quickly.' },
    'contact.name': { fr: 'Nom', en: 'Name' },
    'contact.name_placeholder': { fr: 'Votre nom', en: 'Your name' },
    'contact.email': { fr: 'Email', en: 'Email' },
    'contact.subject': { fr: 'Sujet', en: 'Subject' },
    'contact.subject_question': { fr: 'Question générale', en: 'General question' },
    'contact.subject_bug': { fr: 'Signaler un problème', en: 'Report a problem' },
    'contact.subject_suggestion': { fr: 'Suggestion d\'amélioration', en: 'Improvement suggestion' },
    'contact.subject_other': { fr: 'Autre', en: 'Other' },
    'contact.message': { fr: 'Message', en: 'Message' },
    'contact.message_placeholder': { fr: 'Comment pouvons-nous vous aider ?', en: 'How can we help you?' },
    'contact.send': { fr: 'Envoyer le message', en: 'Send message' },
    'contact.sending': { fr: 'Envoi en cours...', en: 'Sending...' },
    'contact.success_title': { fr: 'Message envoyé !', en: 'Message sent!' },
    'contact.success_text': { fr: 'Merci de nous avoir contacté. Nous vous répondrons rapidement.', en: 'Thank you for contacting us. We will respond shortly.' },
    'contact.send_another': { fr: 'Envoyer un autre message', en: 'Send another message' },

    // Footer
    'footer.description': { fr: 'Simulateurs fiscaux gratuits pour la France et le Maroc.', en: 'Free tax simulators for France and Morocco.' },
    'footer.info': { fr: 'Informations', en: 'Information' },
    'footer.legal': { fr: 'Mentions Légales', en: 'Legal Notice' },
    'footer.privacy': { fr: 'Confidentialité', en: 'Privacy' },
    'footer.rights': { fr: 'Tous droits réservés', en: 'All rights reserved' },

    // ==========================================
    // FAQ PAGE
    // ==========================================
    'faq.page_title': { fr: 'Questions Fréquentes', en: 'Frequently Asked Questions' },
    'faq.page_subtitle': { fr: 'Tout savoir sur nos simulateurs fiscaux', en: 'Everything about our tax simulators' },

    // General Questions
    'faq.general_title': { fr: 'Questions Générales', en: 'General Questions' },
    'faq.reliable_title': { fr: 'Les calculs sont-ils fiables ?', en: 'Are the calculations reliable?' },
    'faq.reliable_text': {
        fr: 'Nos simulateurs utilisent les barèmes officiels 2025 publiés par les administrations fiscales française et marocaine. Cependant, ils fournissent une estimation et ne remplacent pas un conseil fiscal personnalisé. Les cotisations sociales sont calculées avec des taux moyens qui peuvent varier selon votre situation spécifique.',
        en: 'Our simulators use the official 2025 rates published by the French and Moroccan tax authorities. However, they provide an estimate and do not replace personalized tax advice. Social contributions are calculated with average rates that may vary depending on your specific situation.'
    },
    'faq.data_title': { fr: 'Mes données sont-elles stockées ?', en: 'Is my data stored?' },
    'faq.data_text': {
        fr: 'Non. Tous les calculs sont effectués localement dans votre navigateur. Aucune donnée personnelle n\'est envoyée à nos serveurs ni stockée. Vous pouvez utiliser nos outils en toute confidentialité.',
        en: 'No. All calculations are performed locally in your browser. No personal data is sent to our servers or stored. You can use our tools with complete privacy.'
    },
    'faq.free_title': { fr: 'Les simulateurs sont-ils gratuits ?', en: 'Are the simulators free?' },
    'faq.free_text': {
        fr: 'Oui, tous nos simulateurs sont 100% gratuits, sans publicité et sans inscription requise. Vous pouvez les utiliser autant de fois que vous le souhaitez.',
        en: 'Yes, all our simulators are 100% free, without ads and without required registration. You can use them as many times as you want.'
    },
    'faq.update_title': { fr: 'À quelle fréquence les barèmes sont-ils mis à jour ?', en: 'How often are the rates updated?' },
    'faq.update_text': {
        fr: 'Nous mettons à jour les barèmes chaque année après la publication des lois de finances. Les barèmes actuels correspondent à l\'année fiscale 2025.',
        en: 'We update the rates each year after the publication of finance laws. Current rates correspond to the 2025 tax year.'
    },

    // France FAQ
    'faq.france_title': { fr: '🇫🇷 France', en: '🇫🇷 France' },
    'faq.france_net_title': { fr: 'Comment est calculé le salaire net en France ?', en: 'How is net salary calculated in France?' },
    'faq.france_net_text': {
        fr: 'Le salaire net est obtenu en déduisant du brut les cotisations sociales salariales (environ 22% pour les non-cadres, 25% pour les cadres). Ces cotisations financent la sécurité sociale, la retraite, le chômage et la retraite complémentaire.',
        en: 'Net salary is obtained by deducting employee social contributions from gross (about 22% for non-executives, 25% for executives). These contributions fund social security, retirement, unemployment and supplementary pension.'
    },
    'faq.france_quotient_title': { fr: 'Qu\'est-ce que le quotient familial ?', en: 'What is the family quotient?' },
    'faq.france_quotient_text': {
        fr: 'Le quotient familial est un mécanisme qui divise le revenu imposable par le nombre de parts du foyer fiscal. Un célibataire a 1 part, un couple marié 2 parts, et les enfants ajoutent des demi-parts supplémentaires. Cela réduit la progressivité de l\'impôt pour les familles.',
        en: 'The family quotient is a mechanism that divides taxable income by the number of shares in the household. A single person has 1 share, a married couple has 2 shares, and children add additional half-shares. This reduces the progressivity of tax for families.'
    },
    'faq.france_cadre_title': { fr: 'Quelle est la différence entre cadre et non-cadre ?', en: 'What is the difference between executive and non-executive?' },
    'faq.france_cadre_text': {
        fr: 'Les cadres ont des cotisations sociales plus élevées (environ 25% vs 22%) principalement dues à des cotisations de retraite complémentaire supérieures. En contrepartie, ils bénéficient d\'une meilleure couverture retraite.',
        en: 'Executives have higher social contributions (about 25% vs 22%) mainly due to higher supplementary pension contributions. In return, they benefit from better retirement coverage.'
    },
    'faq.france_abatement_title': { fr: 'Qu\'est-ce que l\'abattement de 10% ?', en: 'What is the 10% allowance?' },
    'faq.france_abatement_text': {
        fr: 'L\'abattement de 10% pour frais professionnels est automatiquement appliqué au revenu imposable. Il représente les frais engagés pour exercer votre activité (transport, repas, etc.). Vous pouvez opter pour les frais réels si ceux-ci sont supérieurs.',
        en: 'The 10% allowance for professional expenses is automatically applied to taxable income. It represents expenses incurred for your work (transport, meals, etc.). You can opt for actual expenses if they are higher.'
    },

    // Maroc FAQ
    'faq.maroc_title': { fr: '🇲🇦 Maroc', en: '🇲🇦 Morocco' },
    'faq.maroc_tranches_title': { fr: 'Quelles sont les tranches d\'IR au Maroc ?', en: 'What are the income tax brackets in Morocco?' },
    'faq.maroc_tranches_text': {
        fr: 'L\'IR marocain comporte 6 tranches progressives : 0% jusqu\'à 40 000 DH, 10% de 40 001 à 60 000 DH, 20% de 60 001 à 80 000 DH, 30% de 80 001 à 100 000 DH, 34% de 100 001 à 180 000 DH, et 37% au-delà.',
        en: 'Moroccan income tax has 6 progressive brackets: 0% up to 40,000 DH, 10% from 40,001 to 60,000 DH, 20% from 60,001 to 80,000 DH, 30% from 80,001 to 100,000 DH, 34% from 100,001 to 180,000 DH, and 37% beyond.'
    },
    'faq.maroc_cnss_title': { fr: 'Qu\'est-ce que la CNSS et l\'AMO ?', en: 'What are CNSS and AMO?' },
    'faq.maroc_cnss_text': {
        fr: 'La CNSS (Caisse Nationale de Sécurité Sociale) couvre les prestations familiales, maladie et retraite. Le taux salarial est de 4.48%, plafonné à 6 000 DH/mois. L\'AMO (Assurance Maladie Obligatoire) couvre les frais de santé au taux de 2.26% sans plafond.',
        en: 'CNSS (National Social Security Fund) covers family benefits, health and retirement. The employee rate is 4.48%, capped at 6,000 DH/month. AMO (Mandatory Health Insurance) covers healthcare costs at 2.26% with no cap.'
    },
    'faq.maroc_family_title': { fr: 'Comment fonctionne l\'abattement familial au Maroc ?', en: 'How does the family allowance work in Morocco?' },
    'faq.maroc_family_text': {
        fr: 'L\'abattement familial réduit l\'IR de 500 DH par an et par personne à charge (conjoint et enfants), dans la limite de 3 000 DH par an (soit 6 personnes maximum).',
        en: 'The family allowance reduces income tax by 500 DH per year per dependent (spouse and children), up to a limit of 3,000 DH per year (maximum 6 people).'
    },
    'faq.maroc_pro_title': { fr: 'Que sont les frais professionnels de 20% ?', en: 'What is the 20% professional expenses deduction?' },
    'faq.maroc_pro_text': {
        fr: 'Une déduction forfaitaire de 20% du revenu brut (après cotisations sociales) est appliquée pour frais professionnels. Cette déduction est plafonnée à 30 000 DH par an.',
        en: 'A flat 20% deduction from gross income (after social contributions) is applied for professional expenses. This deduction is capped at 30,000 DH per year.'
    },

    // Comparator FAQ
    'faq.comp_title': { fr: 'Comparateur France vs Maroc', en: 'France vs Morocco Comparator' },
    'faq.comp_how_title': { fr: 'Comment fonctionne le comparateur ?', en: 'How does the comparator work?' },
    'faq.comp_how_text': {
        fr: 'Le comparateur calcule simultanément votre salaire net et votre pression fiscale totale (cotisations + impôt) dans les deux pays, pour un même salaire brut. Il utilise le taux de change en temps réel pour convertir les montants.',
        en: 'The comparator simultaneously calculates your net salary and total tax burden (contributions + tax) in both countries, for the same gross salary. It uses real-time exchange rates to convert amounts.'
    },
    'faq.comp_rate_title': { fr: 'D\'où vient le taux de change ?', en: 'Where does the exchange rate come from?' },
    'faq.comp_rate_text': {
        fr: 'Le taux de change EUR/MAD est récupéré automatiquement depuis l\'API Frankfurter, qui utilise les données de la Banque Centrale Européenne. Vous pouvez aussi saisir un taux personnalisé.',
        en: 'The EUR/MAD exchange rate is automatically fetched from the Frankfurter API, which uses European Central Bank data. You can also enter a custom rate.'
    },
    'faq.comp_cost_title': { fr: 'Le comparateur prend-il en compte le coût de la vie ?', en: 'Does the comparator consider cost of living?' },
    'faq.comp_cost_text': {
        fr: 'Non, le comparateur se concentre uniquement sur la fiscalité. Le coût de la vie, le pouvoir d\'achat et autres facteurs économiques ne sont pas pris en compte. Ces éléments doivent être considérés séparément dans votre réflexion.',
        en: 'No, the comparator focuses only on taxation. Cost of living, purchasing power and other economic factors are not taken into account. These elements should be considered separately in your thinking.'
    },

    // FAQ CTA
    'faq.cta_title': { fr: 'Une question ?', en: 'Have a question?' },
    'faq.cta_text': { fr: 'Vous n\'avez pas trouvé la réponse à votre question ? Contactez-nous.', en: 'Didn\'t find the answer to your question? Contact us.' },
    'faq.cta_button': { fr: 'Nous contacter', en: 'Contact us' },

    // ==========================================
    // SIMULATORS COMMON
    // ==========================================
    'sim.gross_salary': { fr: 'Salaire Brut', en: 'Gross Salary' },
    'sim.gross_monthly': { fr: 'Salaire Brut Mensuel', en: 'Monthly Gross Salary' },
    'sim.gross_annual': { fr: 'Salaire Brut Annuel', en: 'Annual Gross Salary' },
    'sim.monthly': { fr: 'Mensuel', en: 'Monthly' },
    'sim.annual': { fr: 'Annuel', en: 'Annual' },
    'sim.period': { fr: 'Période', en: 'Period' },
    'sim.status': { fr: 'Statut', en: 'Status' },
    'sim.non_cadre': { fr: 'Non-Cadre', en: 'Non-Executive' },
    'sim.cadre': { fr: 'Cadre', en: 'Executive' },
    'sim.family_status': { fr: 'Situation Familiale', en: 'Family Status' },
    'sim.single': { fr: 'Célibataire', en: 'Single' },
    'sim.married': { fr: 'Marié(e)', en: 'Married' },
    'sim.divorced': { fr: 'Divorcé(e)', en: 'Divorced' },
    'sim.widowed': { fr: 'Veuf(ve)', en: 'Widowed' },
    'sim.children': { fr: 'Enfants à charge', en: 'Dependent children' },
    'sim.children_note': { fr: 'Enfants à charge (-21 ans ou handicap)', en: 'Dependent children (under 21 or disabled)' },
    'sim.net_salary': { fr: 'Salaire Net', en: 'Net Salary' },
    'sim.net_before_tax': { fr: 'Salaire Net avant IR', en: 'Net Salary before Tax' },
    'sim.net_after_tax': { fr: 'Salaire Net après IR', en: 'Net Salary after Tax' },
    'sim.net_estimated': { fr: 'Estimation Net', en: 'Net Estimate' },
    'sim.net_monthly': { fr: 'Net Mensuel Estimé', en: 'Estimated Monthly Net' },
    'sim.net_annual': { fr: 'Net Annuel', en: 'Annual Net' },
    'sim.or': { fr: 'soit', en: 'i.e.' },
    'sim.per_year': { fr: '/ an', en: '/ year' },
    'sim.per_month': { fr: '/ mois', en: '/ month' },
    'sim.effective_rate': { fr: 'Taux Effectif', en: 'Effective Rate' },
    'sim.marginal_rate': { fr: 'Taux Marginal', en: 'Marginal Rate' },
    'sim.deducted': { fr: 'prélevés', en: 'deducted' },
    'sim.in_pocket': { fr: 'Dans ma poche', en: 'In my pocket' },
    'sim.deductions': { fr: 'Prélèvements', en: 'Deductions' },
    'sim.total_deducted': { fr: 'Total Déduit', en: 'Total Deducted' },
    'sim.see_details': { fr: 'Voir le détail du calcul', en: 'See calculation details' },
    'sim.breakdown': { fr: 'Décomposition', en: 'Breakdown' },
    'sim.breakdown_annual': { fr: 'Décomposition (Annuel)', en: 'Breakdown (Annual)' },
    'sim.social_contrib': { fr: 'Cotisations Sociales', en: 'Social Contributions' },
    'sim.social_security': { fr: 'Sécurité sociale', en: 'Social Security' },
    'sim.retirement': { fr: 'Retraite complémentaire', en: 'Supplementary Pension' },
    'sim.unemployment': { fr: 'Chômage', en: 'Unemployment' },
    'sim.taxable_income': { fr: 'Net Imposable', en: 'Taxable Income' },
    'sim.income_tax': { fr: 'Impôt sur le Revenu', en: 'Income Tax' },
    'sim.income_tax_ir': { fr: 'Impôt sur le Revenu (IR)', en: 'Income Tax' },
    'sim.family_reduction': { fr: 'Réduction Charges Famille', en: 'Family Allowance Reduction' },
    'sim.final_tax': { fr: 'Impôt sur le Revenu (IR) Final', en: 'Final Income Tax' },
    'sim.bracket_calc': { fr: 'Calcul par tranches (Progressif)', en: 'Progressive Tax Brackets' },
    'sim.bracket': { fr: 'Tranche', en: 'Bracket' },
    'sim.rate': { fr: 'Taux', en: 'Rate' },
    'sim.amount': { fr: 'Montant', en: 'Amount' },
    'sim.tax': { fr: 'Impôt', en: 'Tax' },
    'sim.total': { fr: 'Total', en: 'Total' },
    'sim.how_it_works': { fr: 'Comment ça marche ?', en: 'How does it work?' },
    'sim.disclaimer': {
        fr: 'Les cotisations sont estimées à environ 22% pour non-cadre et 25% pour cadre. Ces chiffres sont des approximations.',
        en: 'Contributions are estimated at about 22% for non-executive and 25% for executive. These figures are approximations.'
    },

    // France Brut Net Specific
    'sim.fr.title': { fr: 'Simulateur Brut → Net', en: 'Gross → Net Simulator' },
    'sim.fr.subtitle': { fr: 'Calculez votre salaire net à partir du brut. Barèmes 2025.', en: 'Calculate your net salary from gross. 2025 rates.' },
    'sim.fr.how_text': {
        fr: 'Le salaire net est calculé en déduisant les cotisations sociales du salaire brut :',
        en: 'Net salary is calculated by deducting social contributions from gross salary:'
    },
    'sim.fr.how_secu': { fr: 'Sécurité sociale : maladie, vieillesse, famille', en: 'Social Security: health, old age, family' },
    'sim.fr.how_retirement': { fr: 'Retraite complémentaire : AGIRC-ARRCO', en: 'Supplementary pension: AGIRC-ARRCO' },
    'sim.fr.how_unemployment': { fr: 'Assurance chômage : contribution salariale', en: 'Unemployment insurance: employee contribution' },
    'sim.fr.how_csg': { fr: 'CSG/CRDS : contributions sociales', en: 'CSG/CRDS: social contributions' },
    'sim.fr.how_rate': {
        fr: 'Le taux global varie entre 22% (non-cadre) et 25% (cadre) du salaire brut.',
        en: 'The overall rate varies between 22% (non-executive) and 25% (executive) of gross salary.'
    },

    // France IR Specific
    'sim.fr_ir.title': { fr: 'Simulateur Impôt sur le Revenu', en: 'Income Tax Simulator' },
    'sim.fr_ir.subtitle': { fr: 'Calculez votre impôt 2025 en quelques clics', en: 'Calculate your 2025 tax in a few clicks' },
    'sim.fr_ir.badge': { fr: 'Barème 2025 - 100% Gratuit - Résultat instantané', en: '2025 Rates - 100% Free - Instant Result' },
    'sim.fr_ir.net_annual': { fr: 'Revenu Net Annuel', en: 'Annual Net Income' },
    'sim.fr_ir.net_annual_help': { fr: 'Salaire net imposable annuel (avant abattement)', en: 'Annual taxable net salary (before allowance)' },
    'sim.fr_ir.parts': { fr: 'Parts Fiscales', en: 'Tax Shares' },
    'sim.fr_ir.half_parts': { fr: 'Demi-parts', en: 'Half-shares' },
    'sim.fr_ir.single_parent': { fr: 'Parent isolé', en: 'Single parent' },
    'sim.fr_ir.per_savings': { fr: 'Épargne PER', en: 'PER Savings' },
    'sim.fr_ir.per_help': { fr: 'Versements sur votre Plan Épargne Retraite', en: 'Contributions to your Retirement Savings Plan' },
    'sim.fr_ir.simulate_per': { fr: 'Simuler économie PER', en: 'Simulate PER savings' },
    'sim.fr_ir.per_amount': { fr: 'Montant versé sur PER', en: 'Amount contributed to PER' },
    'sim.fr_ir.your_tax': { fr: 'Votre Impôt', en: 'Your Tax' },
    'sim.fr_ir.monthly_withholding': { fr: 'Prélèvement mensuel', en: 'Monthly withholding' },
    'sim.fr_ir.tax_breakdown': { fr: 'Détail du Calcul', en: 'Calculation Details' },
    'sim.fr_ir.abatement_10': { fr: 'Abattement 10%', en: '10% Allowance' },
    'sim.fr_ir.taxable_after_abatement': { fr: 'Revenu imposable après abattement', en: 'Taxable income after allowance' },
    'sim.fr_ir.quotient': { fr: 'Quotient familial', en: 'Family quotient' },
    'sim.fr_ir.tax_per_part': { fr: 'Impôt par part', en: 'Tax per share' },
    'sim.fr_ir.gross_tax': { fr: 'Impôt brut', en: 'Gross tax' },
    'sim.fr_ir.ceiling': { fr: 'Plafonnement QF', en: 'QF ceiling' },
    'sim.fr_ir.decote': { fr: 'Décote', en: 'Rebate' },
    'sim.fr_ir.final_tax': { fr: 'Impôt final', en: 'Final tax' },
    'sim.fr_ir.with_per': { fr: 'Avec PER', en: 'With PER' },
    'sim.fr_ir.savings': { fr: 'Économie', en: 'Savings' },
    'sim.fr_ir.brackets_title': { fr: 'Tranches d\'Imposition 2025', en: '2025 Tax Brackets' },
    'sim.fr_ir.rate_info': {
        fr: 'L\'impôt est calculé par tranches successives. Seule la partie du revenu dans chaque tranche est imposée au taux correspondant.',
        en: 'Tax is calculated in successive brackets. Only the portion of income in each bracket is taxed at the corresponding rate.'
    },
    'sim.fr_ir.understand_title': { fr: 'Comprendre le Calcul', en: 'Understanding the Calculation' },

    // Maroc IR Specific
    'sim.ma_ir.title': { fr: 'Simulateur IR Maroc', en: 'Morocco Income Tax Simulator' },
    'sim.ma_ir.subtitle': { fr: 'Calculez votre impôt sur le revenu et votre salaire net. Barèmes 2025.', en: 'Calculate your income tax and net salary. 2025 rates.' },
    'sim.ma_ir.dependents': { fr: 'Personnes à charge', en: 'Dependents' },
    'sim.ma_ir.dependents_note': { fr: 'Conjoint + enfants (max 6)', en: 'Spouse + children (max 6)' },
    'sim.ma_ir.cnss': { fr: 'CNSS', en: 'CNSS' },
    'sim.ma_ir.amo': { fr: 'AMO', en: 'AMO' },
    'sim.ma_ir.pro_expenses': { fr: 'Frais Pro (20%)', en: 'Pro Expenses (20%)' },
    'sim.ma_ir.family_deduction': { fr: 'Déduction Familiale', en: 'Family Deduction' },
    'sim.ma_ir.total_deductions': { fr: 'Total Déductions', en: 'Total Deductions' },
    'sim.ma_ir.net_in_pocket': { fr: 'Net "En Poche"', en: 'Net "In Pocket"' },
    'sim.ma_ir.fiscal_pressure': { fr: 'Pression Fiscale Totale', en: 'Total Tax Burden' },
    'sim.ma_ir.brackets_title': { fr: 'Barème IR Maroc 2025', en: 'Morocco 2025 Tax Brackets' },
    'sim.ma_ir.exempt': { fr: 'Exonéré', en: 'Exempt' },

    // ==========================================
    // COMPARATOR
    // ==========================================
    'comp.title': { fr: 'Comparateur Fiscal', en: 'Tax Comparator' },
    'comp.fr_ma_title': { fr: 'Comparateur Fiscal France vs Maroc', en: 'France vs Morocco Tax Comparator' },
    'comp.subtitle': {
        fr: 'Comparez votre salaire net et votre pression fiscale entre les deux pays. Simulateur mis à jour avec les barèmes 2025.',
        en: 'Compare your net salary and tax burden between both countries. Simulator updated with 2025 rates.'
    },
    'comp.global_title': { fr: 'Comparateur Fiscal International', en: 'International Tax Comparator' },
    'comp.global_subtitle': {
        fr: 'Comparez votre salaire net dans 5 pays : France, Maroc, Dubaï, Genève et Luxembourg.',
        en: 'Compare your net salary in 5 countries: France, Morocco, Dubai, Geneva and Luxembourg.'
    },
    'comp.select_countries': { fr: 'Sélectionnez les pays à comparer (2 minimum)', en: 'Select countries to compare (minimum 2)' },
    'comp.gross_annual': { fr: 'Salaire Brut Annuel', en: 'Annual Gross Salary' },
    'comp.converted_note': { fr: 'Le salaire est converti dans chaque devise locale pour les calculs.', en: 'The salary is converted to each local currency for calculations.' },
    'comp.net_in_pocket': { fr: 'Net "En Poche"', en: 'Net "In Pocket"' },
    'comp.tax_rate': { fr: 'Taux d\'Imposition', en: 'Tax Rate' },
    'comp.total_pressure': { fr: 'Pression Totale', en: 'Total Burden' },
    'comp.distribution': { fr: 'Distribution', en: 'Distribution' },
    'comp.of_gross': { fr: '100% du Brut', en: '100% of Gross' },
    'comp.net': { fr: 'Net', en: 'Net' },
    'comp.social': { fr: 'Social', en: 'Social' },
    'comp.ranking': { fr: 'Classement', en: 'Ranking' },
    'comp.winner': { fr: 'en tête !', en: 'wins!' },
    'comp.vs_last': { fr: 'vs dernier', en: 'vs last' },
    'comp.select_min_2': { fr: 'Sélectionnez au moins 2 pays pour comparer.', en: 'Select at least 2 countries to compare.' },
    'comp.annual_diff': { fr: 'Différence Annuelle', en: 'Annual Difference' },
    'comp.wins': { fr: 'l\'emporte !', en: 'wins!' },
    'comp.you_save': { fr: 'Vous économisez', en: 'You save' },
    'comp.points': { fr: 'points de pression fiscale', en: 'points of tax burden' },
    'comp.per_year': { fr: 'par an', en: 'per year' },
    'comp.more_net': { fr: 'de net en plus', en: 'more net' },
    'comp.exchange_rate': { fr: 'Taux de change', en: 'Exchange rate' },
    'comp.custom_rate': { fr: 'Taux personnalisé', en: 'Custom rate' },
    'comp.live_rate': { fr: 'Taux en direct', en: 'Live rate' },

    // Countries
    'country.france': { fr: 'France', en: 'France' },
    'country.maroc': { fr: 'Maroc', en: 'Morocco' },
    'country.dubai': { fr: 'Dubaï', en: 'Dubai' },
    'country.geneve': { fr: 'Genève', en: 'Geneva' },
    'country.luxembourg': { fr: 'Luxembourg', en: 'Luxembourg' },

    // Global Comparator Page
    'comp_global.badge': { fr: '5 pays - Barèmes 2025', en: '5 countries - 2025 Rates' },
    'comp_global.title': { fr: 'Comparateur Fiscal International', en: 'International Tax Comparator' },
    'comp_global.subtitle': { fr: 'Sélectionnez les pays à comparer et découvrez où votre salaire net sera le plus avantageux.', en: 'Select countries to compare and discover where your net salary will be most advantageous.' },
    'comp_global.select_countries': { fr: 'Sélectionnez les pays à comparer (2 minimum)', en: 'Select countries to compare (minimum 2)' },
    'comp_global.ir_rate': { fr: 'IR', en: 'IT' },
    'comp_global.no_tax': { fr: '0% IMPÔT', en: '0% TAX' },
    'comp_global.gross_annual': { fr: 'Salaire Brut Annuel', en: 'Annual Gross Salary' },
    'comp_global.annual': { fr: 'Annuel', en: 'Annual' },
    'comp_global.monthly': { fr: 'Mensuel', en: 'Monthly' },
    'comp_global.salary_note': { fr: 'Le salaire est converti dans chaque devise locale pour les calculs.', en: 'Salary is converted to each local currency for calculations.' },
    'comp_global.family_status': { fr: 'Situation Familiale', en: 'Family Status' },
    'comp_global.marital_status': { fr: 'Statut Marital', en: 'Marital Status' },
    'comp_global.single': { fr: 'Célibataire', en: 'Single' },
    'comp_global.married': { fr: 'Marié(e)', en: 'Married' },
    'comp_global.children': { fr: 'Enfants à charge', en: 'Dependent children' },
    'comp_global.net_in_pocket': { fr: 'Net "En Poche"', en: 'Net "In Pocket"' },
    'comp_global.tax_burden': { fr: 'Pression Fiscale', en: 'Tax Burden' },
    'comp_global.gross': { fr: 'Brut', en: 'Gross' },
    'comp_global.social_contrib': { fr: 'Cotisations sociales', en: 'Social contributions' },
    'comp_global.income_tax': { fr: 'Impôt (IR)', en: 'Income Tax' },
    'comp_global.net': { fr: 'Net', en: 'Net' },
    'comp_global.ranking': { fr: 'Classement', en: 'Ranking' },
    'comp_global.wins': { fr: 'en tête !', en: 'wins!' },
    'comp_global.vs_last': { fr: 'vs dernier', en: 'vs last' },
    'comp_global.effective_rate': { fr: 'Taux effectif', en: 'Effective rate' },
    'comp_global.select_min_2': { fr: 'Sélectionnez au moins 2 pays pour comparer.', en: 'Select at least 2 countries to compare.' },
    'comp_global.select_min_2_title': { fr: 'Sélectionnez au moins 2 pays', en: 'Select at least 2 countries' },
    'comp_global.countries_5': { fr: '5 Pays', en: '5 Countries' },
    'comp_global.intl_comparison': { fr: 'Comparaison internationale', en: 'International comparison' },
    'comp_global.rates_2025': { fr: 'Barèmes 2025', en: '2025 Rates' },
    'comp_global.updated_data': { fr: 'Données à jour', en: 'Up-to-date data' },
    'comp_global.real_time': { fr: 'Temps Réel', en: 'Real Time' },
    'comp_global.instant_calc': { fr: 'Calcul instantané', en: 'Instant calculation' },
    'comp_global.private': { fr: '100% Privé', en: '100% Private' },
    'comp_global.no_data_stored': { fr: 'Aucune donnée stockée', en: 'No data stored' },
    'comp_global.disclaimer': {
        fr: 'Avertissement Légal : Cet outil est fourni à titre indicatif uniquement. Les lois fiscales varient selon les pays et sont sujettes à modifications. Les cotisations sociales sont des estimations moyennes. Dubai: 0% IR pour résidents fiscaux. Genève: taux cantonal + communal estimés. Luxembourg: barème 2025 classe 1. France et Maroc: barèmes 2025 officiels.',
        en: 'Legal Disclaimer: This tool is provided for informational purposes only. Tax laws vary by country and are subject to change. Social contributions are average estimates. Dubai: 0% income tax for tax residents. Geneva: estimated cantonal + municipal rates. Luxembourg: 2025 class 1 rates. France and Morocco: official 2025 rates.'
    },

    // ==========================================
    // GUIDES
    // ==========================================
    'guide.fr.title': { fr: 'Guide Fiscal France 2025', en: 'France Tax Guide 2025' },
    'guide.fr.subtitle': { fr: 'Tout comprendre sur la fiscalité française', en: 'Understanding French taxation' },
    'guide.ma.title': { fr: 'Guide Fiscal Maroc 2025', en: 'Morocco Tax Guide 2025' },
    'guide.ma.subtitle': {
        fr: 'Tout comprendre sur la fiscalité marocaine : cotisations sociales, impôt sur le revenu, abattements et déductions.',
        en: 'Understanding Moroccan taxation: social contributions, income tax, allowances and deductions.'
    },
    'guide.simulate': { fr: 'Simulez votre situation', en: 'Simulate your situation' },
    'guide.simulate_text': { fr: 'Utilisez notre simulateur gratuit pour calculer votre impôt sur le revenu.', en: 'Use our free simulator to calculate your income tax.' },
    'guide.ir_simulator': { fr: 'Simulateur Impôt sur le Revenu', en: 'Income Tax Simulator' },

    // ==========================================
    // LEGAL PAGES
    // ==========================================
    'legal.title': { fr: 'Mentions Légales', en: 'Legal Notice' },
    'legal.editor': { fr: 'Éditeur du site', en: 'Website Publisher' },
    'legal.editor_text': {
        fr: 'Le site NetSalaire.com est édité par un particulier.',
        en: 'The website NetSalaire.com is published by a private individual.'
    },
    'legal.hosting': { fr: 'Hébergement', en: 'Hosting' },
    'legal.hosting_text': { fr: 'Le site est hébergé par GitHub Pages.', en: 'The site is hosted by GitHub Pages.' },
    'legal.ip': { fr: 'Propriété intellectuelle', en: 'Intellectual Property' },
    'legal.ip_text': {
        fr: 'L\'ensemble du contenu de ce site (textes, graphismes, code source, etc.) est protégé par le droit d\'auteur. Toute reproduction ou représentation, totale ou partielle, de ce site ou de son contenu est interdite sans autorisation préalable.',
        en: 'All content on this site (texts, graphics, source code, etc.) is protected by copyright. Any reproduction or representation, in whole or in part, of this site or its content is prohibited without prior authorization.'
    },
    'legal.responsibility': { fr: 'Responsabilité', en: 'Liability' },
    'legal.responsibility_text': {
        fr: 'Les informations et calculs fournis sur ce site le sont à titre indicatif uniquement. Ils ne constituent en aucun cas un conseil fiscal, juridique ou financier. L\'éditeur ne saurait être tenu responsable de toute erreur, omission ou interprétation des informations publiées.',
        en: 'The information and calculations provided on this site are for informational purposes only. They do not constitute tax, legal or financial advice. The publisher cannot be held responsible for any error, omission or interpretation of the published information.'
    },
    'legal.responsibility_text2': {
        fr: 'Les simulateurs utilisent des barèmes officiels mais les cotisations sociales et impôts réels peuvent varier selon votre situation personnelle. Pour toute question fiscale, consultez un professionnel qualifié.',
        en: 'The simulators use official rates but actual social contributions and taxes may vary depending on your personal situation. For any tax questions, consult a qualified professional.'
    },
    'legal.data': { fr: 'Données personnelles', en: 'Personal Data' },
    'legal.data_text': {
        fr: 'Ce site ne collecte aucune donnée personnelle. Tous les calculs sont effectués localement dans votre navigateur. Aucune information n\'est transmise à nos serveurs.',
        en: 'This site does not collect any personal data. All calculations are performed locally in your browser. No information is transmitted to our servers.'
    },
    'legal.data_text2': {
        fr: 'Pour plus d\'informations, consultez notre politique de confidentialité.',
        en: 'For more information, see our privacy policy.'
    },
    'legal.cookies': { fr: 'Cookies', en: 'Cookies' },
    'legal.cookies_text': {
        fr: 'Ce site n\'utilise pas de cookies de suivi ni de cookies publicitaires. Seuls des cookies techniques strictement nécessaires au fonctionnement du site peuvent être utilisés.',
        en: 'This site does not use tracking cookies or advertising cookies. Only strictly necessary technical cookies for the site operation may be used.'
    },
    'legal.law': { fr: 'Droit applicable', en: 'Applicable Law' },
    'legal.law_text': {
        fr: 'Les présentes mentions légales sont soumises au droit français. Tout litige relatif à l\'utilisation du site sera soumis à la compétence exclusive des tribunaux français.',
        en: 'These legal notices are subject to French law. Any dispute relating to the use of the site will be subject to the exclusive jurisdiction of the French courts.'
    },

    // Privacy Policy
    'privacy.title': { fr: 'Politique de Confidentialité', en: 'Privacy Policy' },
    'privacy.updated': { fr: 'Dernière mise à jour : Décembre 2025', en: 'Last updated: December 2025' },
    'privacy.intro': { fr: 'Introduction', en: 'Introduction' },
    'privacy.intro_text': {
        fr: 'Chez NetSalaire, nous accordons une importance primordiale à la protection de votre vie privée. Cette politique de confidentialité explique comment nous traitons les informations lorsque vous utilisez notre site.',
        en: 'At NetSalaire, we attach primary importance to protecting your privacy. This privacy policy explains how we handle information when you use our site.'
    },
    'privacy.data_collected': { fr: 'Données collectées', en: 'Data Collected' },
    'privacy.good_news': { fr: 'Bonne nouvelle : nous ne collectons aucune donnée personnelle.', en: 'Good news: we do not collect any personal data.' },
    'privacy.data_text': {
        fr: 'Tous les calculs effectués sur nos simulateurs sont réalisés localement dans votre navigateur. Aucune information (salaire, situation familiale, etc.) n\'est envoyée à nos serveurs ni stockée de quelque manière que ce soit.',
        en: 'All calculations performed on our simulators are done locally in your browser. No information (salary, family status, etc.) is sent to our servers or stored in any way.'
    },
    'privacy.cookies_text': {
        fr: 'Notre site n\'utilise pas de cookies de suivi, de cookies publicitaires ou de cookies tiers. Nous n\'utilisons aucun outil d\'analyse de trafic (Google Analytics, etc.).',
        en: 'Our site does not use tracking cookies, advertising cookies or third-party cookies. We do not use any traffic analysis tools (Google Analytics, etc.).'
    },
    'privacy.cookies_text2': {
        fr: 'Seuls des cookies techniques strictement nécessaires au fonctionnement du site peuvent être utilisés par votre navigateur.',
        en: 'Only strictly necessary technical cookies for site operation may be used by your browser.'
    },
    'privacy.third_party': { fr: 'Services tiers', en: 'Third-Party Services' },
    'privacy.third_party_text': { fr: 'Notre site utilise les services tiers suivants :', en: 'Our site uses the following third-party services:' },
    'privacy.third_party_hosting': { fr: 'hébergement du site', en: 'site hosting' },
    'privacy.third_party_rate': { fr: 'récupération du taux de change EUR/MAD (aucune donnée personnelle transmise)', en: 'EUR/MAD exchange rate retrieval (no personal data transmitted)' },
    'privacy.third_party_cdn': { fr: 'chargement de polices et icônes (Tailwind, Iconify, Google Fonts)', en: 'loading fonts and icons (Tailwind, Iconify, Google Fonts)' },
    'privacy.security': { fr: 'Sécurité', en: 'Security' },
    'privacy.security_text': {
        fr: 'Notre site est servi via HTTPS, garantissant que toutes les communications entre votre navigateur et notre site sont chiffrées.',
        en: 'Our site is served via HTTPS, ensuring that all communications between your browser and our site are encrypted.'
    },
    'privacy.rights': { fr: 'Vos droits', en: 'Your Rights' },
    'privacy.rights_text': {
        fr: 'Conformément au RGPD, vous disposez de droits sur vos données personnelles. Cependant, comme nous ne collectons aucune donnée, ces droits ne s\'appliquent pas dans le cadre de l\'utilisation de nos simulateurs.',
        en: 'In accordance with GDPR, you have rights over your personal data. However, as we do not collect any data, these rights do not apply when using our simulators.'
    },
    'privacy.changes': { fr: 'Modifications', en: 'Changes' },
    'privacy.changes_text': {
        fr: 'Nous nous réservons le droit de modifier cette politique de confidentialité à tout moment. Les modifications prendront effet dès leur publication sur cette page.',
        en: 'We reserve the right to modify this privacy policy at any time. Changes will take effect upon publication on this page.'
    },

    // ==========================================
    // MAROC BRUT NET SIMULATOR
    // ==========================================
    'sim_ma.badge': { fr: 'Maroc', en: 'Morocco' },
    'sim_ma.title': { fr: 'Simulateur Brut \u2192 Net', en: 'Gross \u2192 Net Simulator' },
    'sim_ma.subtitle': { fr: 'Calculez votre salaire net au Maroc. Bar\u00e8mes 2025.', en: 'Calculate your net salary in Morocco. 2025 rates.' },
    'sim_ma.gross_monthly': { fr: 'Salaire Brut Mensuel', en: 'Monthly Gross Salary' },
    'sim_ma.situation': { fr: 'Situation', en: 'Status' },
    'sim_ma.celibataire': { fr: 'C\u00e9libataire', en: 'Single' },
    'sim_ma.marie': { fr: 'Mari\u00e9(e)', en: 'Married' },
    'sim_ma.children': { fr: 'Enfants', en: 'Children' },
    'sim_ma.net_salary': { fr: 'Salaire Net', en: 'Net Salary' },
    'sim_ma.gross_salary': { fr: 'Salaire Brut', en: 'Gross Salary' },
    'sim_ma.cnss_rate': { fr: 'CNSS (4.48%)', en: 'CNSS (4.48%)' },
    'sim_ma.amo_rate': { fr: 'AMO (2.26%)', en: 'AMO (2.26%)' },
    'sim_ma.pro_expenses': { fr: 'Frais professionnels (20%)', en: 'Professional expenses (20%)' },
    'sim_ma.ir': { fr: 'IR (Imp\u00f4t sur le Revenu)', en: 'IR (Income Tax)' },
    'sim_ma.family_allowance': { fr: 'Abattement familial', en: 'Family allowance' },
    'sim_ma.info_title': { fr: 'Cotisations au Maroc', en: 'Contributions in Morocco' },
    'sim_ma.cnss_desc': { fr: '(Caisse Nationale de S\u00e9curit\u00e9 Sociale) : 4.48% du brut, plafonn\u00e9 \u00e0 6 000 MAD/mois.', en: '(National Social Security Fund): 4.48% of gross, capped at 6,000 MAD/month.' },
    'sim_ma.amo_desc': { fr: '(Assurance Maladie Obligatoire) : 2.26% du brut, sans plafond.', en: '(Mandatory Health Insurance): 2.26% of gross, no cap.' },
    'sim_ma.pro_expenses_desc': { fr: 'D\u00e9duction forfaitaire de 20% du brut apr\u00e8s cotisations (plafonn\u00e9e \u00e0 30 000 MAD/an).', en: 'Flat 20% deduction from gross after contributions (capped at 30,000 MAD/year).' },
    'sim_ma.family_allowance_desc': { fr: '500 MAD/an par personne \u00e0 charge (conjoint + enfants), plafonn\u00e9 \u00e0 3 000 MAD/an.', en: '500 MAD/year per dependent (spouse + children), capped at 3,000 MAD/year.' },
    'sim_ma.netsalaire_desc': { fr: 'Simulateurs fiscaux gratuits pour la France et le Maroc. Comparez, simulez, optimisez.', en: 'Free tax simulators for France and Morocco. Compare, simulate, optimize.' },

    // ==========================================
    // DISCLAIMERS
    // ==========================================
    'disclaimer.general': {
        fr: 'Cet outil est fourni à titre indicatif uniquement. Les cotisations sociales sont estimées à un taux moyen standard. Barème IR 2025.',
        en: 'This tool is provided for informational purposes only. Social contributions are estimated at a standard average rate. 2025 income tax rates.'
    },
    'disclaimer.comparator': {
        fr: 'Avertissement Légal : Cet outil est fourni à titre indicatif uniquement. Les lois fiscales varient selon les pays et sont sujettes à modifications.',
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
            const translation = this.t(key);
            if (translation !== key) {
                el.textContent = translation;
            }
        });

        // Translate HTML content (for elements with HTML inside)
        document.querySelectorAll('[data-i18n-html]').forEach(el => {
            const key = el.getAttribute('data-i18n-html');
            const translation = this.t(key);
            if (translation !== key) {
                el.innerHTML = translation;
            }
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

        // Translate value attributes (for inputs, options)
        document.querySelectorAll('[data-i18n-value]').forEach(el => {
            const key = el.getAttribute('data-i18n-value');
            el.value = this.t(key);
        });
    },

    /**
     * Update language switcher UI
     */
    updateSwitcherUI() {
        // Update all flag displays
        document.querySelectorAll('.lang-flag').forEach(el => {
            el.textContent = this.currentLang === 'fr' ? '🇫🇷' : '🇬🇧';
        });

        // Legacy support for id-based flag
        const currentFlag = document.getElementById('current-lang-flag');
        if (currentFlag) {
            currentFlag.textContent = this.currentLang === 'fr' ? '🇫🇷' : '🇬🇧';
        }

        // Update switcher button states
        const switcher = document.getElementById('lang-switcher');
        if (switcher) {
            const frBtn = switcher.querySelector('[data-lang="fr"]');
            const enBtn = switcher.querySelector('[data-lang="en"]');

            if (frBtn && enBtn) {
                frBtn.classList.toggle('active', this.currentLang === 'fr');
                enBtn.classList.toggle('active', this.currentLang === 'en');
            }
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
