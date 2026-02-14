#!/usr/bin/env python3
"""Final round of fixes for the remaining 24 broken entries."""

with open('_fix_seo.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Each: (old_string, new_string) - trim or extend to hit 150-160
fixes = [
    # ar/egypte desc=161 -> trim 1
    (
        'احسب ضرائبك في جمهورية مصر العربية مجاناً. محاكاة مفصلة مع ضريبة الدخل التصاعدية والتأمينات الاجتماعية والتأمين الصحي. نتائج فورية ودقيقة حسب جداول 2026 الرسمية.',
        'احسب ضرائبك في جمهورية مصر العربية مجاناً. محاكاة مفصلة مع ضريبة الدخل التصاعدية والتأمينات الاجتماعية والتأمين الصحي. نتائج فورية حسب جداول 2026 الرسمية.',
    ),
    # ar/koweit desc=161 -> trim 1
    (
        'احسب ضرائبك في دولة الكويت مجاناً. الكويت بدون ضريبة دخل شخصية على الأفراد. محاكاة مفصلة مع الاشتراكات الاجتماعية والتأمينات. نتائج فورية حسب جداول 2026 الرسمية.',
        'احسب ضرائبك في دولة الكويت مجاناً. الكويت بدون ضريبة دخل شخصية على الأفراد. محاكاة مفصلة مع الاشتراكات الاجتماعية والتأمينات. نتائج حسب جداول 2026 الرسمية.',
    ),
    # ar/qatar desc=161 -> trim
    (
        'احسب ضرائبك في دولة قطر مجاناً. قطر بدون ضريبة دخل شخصية على الأفراد. احسب راتبك الصافي فوراً. محاكاة مفصلة مع الاشتراكات والرسوم الاجتماعية. جداول 2026 الرسمية.',
        'احسب ضرائبك في دولة قطر مجاناً. قطر بدون ضريبة دخل شخصية على الأفراد. احسب راتبك الصافي فوراً. محاكاة مع الاشتراكات والرسوم الاجتماعية. جداول 2026 الرسمية.',
    ),
    # cs desc=166 -> trim
    (
        'Vypočítejte si daně v České republice zcela zdarma. Podrobná simulace s daní z příjmu, sociálním a zdravotním pojištěním. Okamžité výsledky dle aktuálních sazeb 2026.',
        'Vypočítejte si daně v České republice zdarma. Podrobná simulace s daní z příjmu, sociálním a zdravotním pojištěním. Okamžité výsledky dle sazeb 2026.',
    ),
    # en/morocco desc=161 -> trim 1
    (
        'The complete guide to Moroccan taxation you wish you had before working in Morocco. Updated 2026.',
        'The complete guide to Moroccan taxation you wish you had before working in Morocco. Year 2026.',
    ),
    # en/sweden desc=161 -> trim 1
    (
        'Official 2026 rates and brackets included.',
        'Official 2026 rates and brackets.',
    ),
    # fr/afrique-du-sud desc=174 -> remove doubled text
    (
        'Resultat net instantane. Baremes 2026. Resultat net instantane.',
        'Resultat net instantane. Baremes 2026 officiels.',
    ),
    # fr/argentine desc=166 -> trim
    (
        'Baremes 2026. Resultat net instantane.',
        'Baremes 2026 officiels inclus.',
    ),
    # fr/autriche desc=161 -> trim 1
    (
        'Baremes 2026 officiels. Resultat net.',
        'Baremes 2026. Resultat net inclus.',
    ),
    # fr/belgique desc=171 -> major trim
    (
        'cotisations RSZ/ONSS et precompte professionnel. Baremes 2026 officiels.',
        'cotisations sociales RSZ/ONSS. Baremes 2026 officiels.',
    ),
    # fr/bresil desc=166 -> trim
    (
        'Salaire net en BRL. Baremes 2026 officiels.',
        'Net en BRL. Baremes 2026 officiels.',
    ),
    # fr/canada desc=162 -> trim 2
    (
        'Baremes 2026 en CAD. Resultat net inclus.',
        'Baremes 2026 en CAD inclus. Net.',
    ),
    # fr/croatie desc=163 -> trim 3
    (
        'Baremes 2026 en euros. Resultat instantane.',
        'Baremes 2026 en euros inclus.',
    ),
    # fr/dubai desc=164 -> trim
    (
        "Barèmes 2026. Résultat net instantané.",
        "Barèmes 2026 officiels inclus.",
    ),
    # fr/egypte desc=170 -> trim
    (
        'Baremes 2026 en EGP. Resultat net inclus.',
        'Baremes 2026 en EGP inclus.',
    ),
    # fr/france/creche desc=166 -> trim
    (
        'maternelle agréée en France. Barèmes 2026.',
        'maternelle agréée. Tarifs 2026.',
    ),
    # fr/france/guide desc=166 -> trim
    (
        'France complet et gratuit. Barèmes 2026.',
        'France complet et gratuit 2026.',
    ),
    # fr/france/indemnite desc=167 -> trim
    (
        'convention collective. Baremes 2026 officiels.',
        'convention collective. Baremes 2026.',
    ),
    # fr/salaire-brut-net desc=162 -> trim 2
    (
        "Barèmes URSSAF 2026. Résultat instantané.",
        "Barèmes URSSAF 2026 officiels.",
    ),
    # fr/japon desc=167 -> trim
    (
        'Net en JPY. Baremes 2026 officiels.',
        'Net en JPY. Baremes 2026.',
    ),
    # fr/politique desc=170 -> trim
    (
        'Conforme RGPD. Simulateurs gratuits 2026.',
        'Conforme RGPD et sécurisé.',
    ),
    # fr/portugal desc=161 -> trim 1
    (
        'Baremes 2026. Resultat net en EUR inclus.',
        'Baremes 2026 en EUR. Resultat net.',
    ),
    # fr/qatar desc=163 -> trim
    (
        "Barèmes 2026 en QAR. Résultat net inclus.",
        "Barèmes 2026 en QAR inclus.",
    ),
    # zh desc=123 -> extend to 150+
    (
        '完全免费计算中国的个人所得税和五险一金。包含养老保险、医疗保险、失业保险、工伤保险、生育保险和住房公积金的详细模拟计算工具。支持2026年最新个税税率表和专项附加扣除政策。即时在线查看每月税后实际到手工资金额、各项社保扣除明细和年度累计纳税总额。',
        '完全免费在线计算中国的个人所得税和五险一金详细金额。包含养老保险、医疗保险、失业保险、工伤保险、生育保险和住房公积金的精准模拟计算工具。完全支持2026年最新个人所得税税率表和各类专项附加扣除政策。即时在线查看每月税后实际到手工资金额、各项社保公积金扣除明细和全年度累计纳税总额。适用于工薪阶层和自由职业者。',
    ),
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new, 1)
    else:
        print(f"WARNING: Not found: {old[:60]}...")

with open('_fix_seo.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Final fixes applied.")
