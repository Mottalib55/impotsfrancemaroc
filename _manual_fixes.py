#!/usr/bin/env python3
"""Manually fix remaining SEO entries that the auto-adjuster couldn't handle,
and clean up bad auto-generated text (doubled words, wrong language appended)."""
import re

with open('_fix_seo.py', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# REPLACEMENTS: (old_string, new_string)
# ============================================================
replacements = [
    # --- FIX REMAINING 14 BROKEN ENTRIES ---

    # ar/dubai desc=146 -> need 150-160
    (
        'احسب ضرائبك في دبي والإمارات العربية المتحدة مجاناً. محاكاة مفصلة مع ضريبة القيمة المضافة والرسوم. احسب راتبك الصافي فوراً حسب جداول 2026 الرسمية.',
        'احسب ضرائبك في دبي والإمارات العربية المتحدة مجاناً. محاكاة مفصلة مع ضريبة القيمة المضافة والرسوم. احسب راتبك الصافي فوراً حسب جداول 2026 الرسمية المعتمدة.',
    ),
    # ar/egypte desc=145 -> need 150+
    (
        'احسب ضرائبك في مصر مجاناً. محاكاة مفصلة مع ضريبة الدخل التصاعدية والتأمينات الاجتماعية والتأمين الصحي. نتائج فورية ودقيقة حسب جداول 2026 الرسمية.',
        'احسب ضرائبك في جمهورية مصر العربية مجاناً. محاكاة مفصلة مع ضريبة الدخل التصاعدية والتأمينات الاجتماعية والتأمين الصحي. نتائج فورية ودقيقة حسب جداول 2026 الرسمية.',
    ),
    # ar/koweit desc=144 -> need 150+
    (
        'احسب ضرائبك في الكويت مجاناً. الكويت بدون ضريبة دخل شخصية. محاكاة مفصلة مع الاشتراكات الاجتماعية والتأمينات. نتائج فورية حسب جداول 2026 الرسمية.',
        'احسب ضرائبك في دولة الكويت مجاناً. الكويت بدون ضريبة دخل شخصية على الأفراد. محاكاة مفصلة مع الاشتراكات الاجتماعية والتأمينات. نتائج فورية حسب جداول 2026 الرسمية.',
    ),
    # ar/qatar desc=144 -> need 150+
    (
        'احسب ضرائبك في قطر مجاناً. قطر بدون ضريبة دخل شخصية. احسب راتبك الصافي فوراً. محاكاة مفصلة مع الاشتراكات والرسوم الاجتماعية. جداول 2026 الرسمية.',
        'احسب ضرائبك في دولة قطر مجاناً. قطر بدون ضريبة دخل شخصية على الأفراد. احسب راتبك الصافي فوراً. محاكاة مفصلة مع الاشتراكات والرسوم الاجتماعية. جداول 2026 الرسمية.',
    ),
    # cs desc=146 -> need 150+
    (
        'Vypočítejte si daně v České republice zdarma. Podrobná simulace s daní z příjmu, sociálním a zdravotním pojištěním. Výsledky ihned dle sazeb 2026.',
        'Vypočítejte si daně v České republice zcela zdarma. Podrobná simulace s daní z příjmu, sociálním a zdravotním pojištěním. Okamžité výsledky dle aktuálních sazeb 2026.',
    ),
    # da desc=147 -> need 150+
    (
        'Beregn dine skatter i Danmark gratis. Detaljeret simulering med indkomstskat, kommuneskat, AM-bidrag og sociale bidrag. Resultater med 2026-satser.',
        'Beregn dine skatter i Danmark helt gratis. Detaljeret simulering med indkomstskat, kommuneskat, AM-bidrag og sociale bidrag. Resultater med 2026-satser.',
    ),
    # el desc=144 -> need 150+
    (
        'Υπολογίστε τους φόρους σας στην Ελλάδα δωρεάν. Προσομοίωση με φόρο εισοδήματος, κοινωνικές εισφορές ΕΦΚΑ και εισφορά αλληλεγγύης. Κλίμακες 2026.',
        'Υπολογίστε τους φόρους σας στην Ελλάδα εντελώς δωρεάν. Προσομοίωση με φόρο εισοδήματος, κοινωνικές εισφορές ΕΦΚΑ και εισφορά αλληλεγγύης. Κλίμακες 2026.',
    ),
    # fr/chili title=48 -> need 50+
    (
        'Simulateur Impot Chili 2026 - Calcul Salaire Net',
        'Simulateur Impot Chili 2026 - Calcul Salaire Net Gratuit',
    ),
    # hr desc=148 -> need 150+
    (
        'Izračunajte poreze u Hrvatskoj besplatno. Detaljna simulacija s porezom na dohodak, prirezom, HZMO i HZZO doprinosima. Rezultati prema stopama 2026.',
        'Izračunajte svoje poreze u Hrvatskoj besplatno. Detaljna simulacija s porezom na dohodak, prirezom, HZMO i HZZO doprinosima. Rezultati prema stopama 2026.',
    ),
    # it desc=149 -> need 150+
    (
        'Calcola le tue tasse in Italia gratis. Simulazione con IRPEF progressiva, contributi INPS, addizionali regionali e comunali. Aliquote ufficiali 2026.',
        'Calcola le tue tasse in Italia gratis. Simulazione con IRPEF progressiva, contributi INPS, addizionali regionali e comunali. Aliquote ufficiali del 2026.',
    ),
    # no desc=149 -> need 150+
    (
        'Beregn skattene dine i Norge gratis. Detaljert simulering med trinnskatt, trygdeavgift, kommuneskatt og sosiale avgifter. Resultater med 2026-satser.',
        'Beregn skattene dine i Norge helt gratis. Detaljert simulering med trinnskatt, trygdeavgift, kommuneskatt og sosiale avgifter. Resultater med 2026-satser.',
    ),
    # tr desc=147 -> need 150+
    (
        'Türkiye vergilerinizi ücretsiz hesaplayın. Gelir vergisi, SGK primleri ve damga vergisi ile detaylı simülasyon. 2026 yılı güncel oran ve dilimleri.',
        'Türkiye vergilerinizi tamamen ücretsiz hesaplayın. Gelir vergisi, SGK primleri ve damga vergisi ile detaylı simülasyon. 2026 yılı güncel oran ve dilimleri.',
    ),
    # vi desc=145 -> need 150+
    (
        'Tính thuế của bạn tại Việt Nam miễn phí. Mô phỏng chi tiết với thuế thu nhập cá nhân TNCN, bảo hiểm xã hội BHXH và bảo hiểm y tế. Biểu thuế 2026.',
        'Tính thuế của bạn tại Việt Nam hoàn toàn miễn phí. Mô phỏng chi tiết với thuế thu nhập cá nhân TNCN, bảo hiểm xã hội BHXH và bảo hiểm y tế. Biểu thuế 2026.',
    ),
    # zh title=48 -> need 50+
    (
        '税收计算器 中国 2026年度版 - 完全免费在线计算个人所得税五险一金社保公积金和实际到手工资',
        '税收计算器 中国 2026年度版 - 完全免费在线精准计算个人所得税五险一金社保公积金和实际到手工资',
    ),
    # zh desc - remove appended French text
    (
        '完全免费计算中国的个人所得税和五险一金。包含养老保险、医疗保险、失业保险、工伤保险、生育保险和住房公积金的详细模拟计算工具。支持2026年最新个税税率表和专项附加扣除政策。即时在线查看每月税后实际到手工资金额、各项社保扣除明细和年度累计纳税总额。 Salaire net instantane. Gratuit.',
        '完全免费计算中国的个人所得税和五险一金。包含养老保险、医疗保险、失业保险、工伤保险、生育保险和住房公积金的详细模拟计算工具。支持2026年最新个税税率表和专项附加扣除政策。即时在线查看每月税后实际到手工资金额、各项社保扣除明细和年度累计纳税总额。',
    ),

    # --- CLEAN UP BAD AUTO-GENERATED TEXT ---

    # en/sweden: "Official Official" doubled
    (
        'Official Official 2026 rates included.',
        'Official 2026 rates and brackets included.',
    ),
    # en/morocco: awkward "included" at end
    (
        'The complete guide to Moroccan taxation you wish you had before working in Morocco included.',
        'The complete guide to Moroccan taxation you wish you had before working in Morocco. Updated 2026.',
    ),

    # FR pages: "officiels officiels" doubled words - fix each unique occurrence
    # fr/autriche
    (
        'Baremes 2026 officiels officiels.',
        'Baremes 2026 officiels. Resultat net.',
    ),
    # fr/belgique
    (
        "cotisations RSZ/ONSS. Baremes 2026 officiels officiels.",
        "cotisations RSZ/ONSS et precompte professionnel. Baremes 2026 officiels.",
    ),
    # fr/chili desc: "officiels officiels"
    (
        "Baremes 2026 en CLP officiels officiels.",
        "Baremes 2026 en CLP. Resultat net gratuit.",
    ),
    # fr/bresil: awkward "2026 officiels."
    (
        "Salaire net en BRL 2026 officiels.",
        "Salaire net en BRL. Baremes 2026 officiels.",
    ),
    # fr/canada desc
    (
        "Baremes 2026 en CAD inclus officiels.",
        "Baremes 2026 en CAD. Resultat net inclus.",
    ),
    # fr/croatie
    (
        "Baremes 2026 en euros inclus officiels.",
        "Baremes 2026 en euros. Resultat instantane.",
    ),
    # fr/danemark
    (
        "Baremes 2026 en DKK officiels inclus officiels.",
        "Baremes 2026 en DKK. Resultat net instantane.",
    ),
    # fr/dubai
    (
        "Barèmes 2026 inclus officiels.",
        "Barèmes 2026. Résultat net instantané.",
    ),
    # fr/egypte
    (
        "Baremes 2026 en EGP officiels.",
        "Baremes 2026 en EGP. Resultat net inclus.",
    ),
    # fr/indonesie
    (
        "Baremes 2026 officiels.",
        "Baremes 2026. Resultat net instantane.",
    ),
    # fr/italie
    (
        "Baremes 2026 inclus officiels.",
        "Baremes 2026. Resultat net instantane.",
    ),
    # fr/japon
    (
        "Net en JPY 2026 officiels.",
        "Net en JPY. Baremes 2026 officiels.",
    ),
    # fr/portugal
    (
        "Baremes 2026 en EUR inclus officiels.",
        "Baremes 2026. Resultat net en EUR inclus.",
    ),
    # fr/qatar
    (
        "Barèmes 2026 en QAR inclus officiels.",
        "Barèmes 2026 en QAR. Résultat net inclus.",
    ),
    # fr/salaire brut net
    (
        "Barèmes URSSAF 2026 inclus officiels.",
        "Barèmes URSSAF 2026. Résultat instantané.",
    ),
    # fr/indemnite licenciement
    (
        "convention collective. 2026 officiels.",
        "convention collective. Baremes 2026 officiels.",
    ),
    # fr/france/creche
    (
        "maternelle agréée. 2026 officiels.",
        "maternelle agréée en France. Barèmes 2026.",
    ),
    # fr/france/guide
    (
        "France complet. 2026 officiels.",
        "France complet et gratuit. Barèmes 2026.",
    ),
    # fr/politique-confidentialite
    (
        "Conforme RGPD. 2026 officiels.",
        "Conforme RGPD. Simulateurs gratuits 2026.",
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
    else:
        print(f"WARNING: Not found: {old[:60]}...")

with open('_fix_seo.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Manual fixes applied. Run 'python3 _fix_seo.py --check' to verify.")
