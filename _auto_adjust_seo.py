#!/usr/bin/env python3
"""Auto-adjust _fix_seo.py entries to be within 50-60 (title) and 150-160 (desc)."""
import sys, os, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Override dict for entries that need manual rewrite (CJK, special cases)
OVERRIDES = {
    # JAPANESE - need 50-60 title, 150-160 desc
    'ja/nihon/zeikin-keisan/index.html': (
        "税金計算シミュレーター 日本 2026年度版 - 完全無料で所得税・住民税・社会保険料をオンラインで即時に計算",
        "日本の税金を完全無料で正確に計算できるオンラインシミュレーターです。所得税、住民税、厚生年金保険料、健康保険料、介護保険料、雇用保険料を含む詳細な計算結果をすぐに確認できます。2026年度の最新税率・控除額に完全対応。毎月の手取り額から年間の納税額まで、給与明細の全項目を網羅した包括的なシミュレーションツールです。",
    ),
    # KOREAN - need 50-60 title, 150-160 desc
    'ko/hanguk/segeum-gyesan/index.html': (
        "세금 계산기 한국 2026년 - 소득세 주민세 국민연금 건강보험 고용보험 무료 계산 시뮬레이터 도구",
        "한국의 세금을 완전 무료로 정확하게 계산하세요. 소득세, 주민세, 국민연금, 건강보험, 고용보험, 장기요양보험의 상세 시뮬레이션을 제공합니다. 2026년 최신 세율과 공제 항목을 반영하여 실수령액을 즉시 확인할 수 있는 편리한 온라인 계산 도구입니다. 급여 내역 상세 분석도 제공합니다.",
    ),
    # CHINESE - need 50-60 title, 150-160 desc
    'zh/zhongguo/shuishou-jisuan/index.html': (
        "税收计算器 中国 2026年度版 - 完全免费在线计算个人所得税五险一金社保公积金和实际到手工资",
        "完全免费计算中国的个人所得税和五险一金。包含养老保险、医疗保险、失业保险、工伤保险、生育保险和住房公积金的详细模拟计算工具。支持2026年最新个税税率表和专项附加扣除政策。即时在线查看每月税后实际到手工资金额、各项社保扣除明细和年度累计纳税总额。",
    ),
    # THAI title - need 50-60 (currently 61)
    'th/prathet-thai/khamnuan-phasi/index.html': (
        "คำนวณภาษี ประเทศไทย 2026 - เครื่องคำนวณภาษีเงินได้ฟรี ทันที",
        None,  # Keep desc from FIXES, will be adjusted
    ),
    # FR titles too short
    'fr/canada/simulateur-impot/index.html': (
        "Simulateur Impot Canada 2026 - Calcul du Net Gratuit",
        None,
    ),
    'fr/chili/simulateur-impot/index.html': (
        "Simulateur Impot Chili 2026 - Calcul Salaire Net",
        None,
    ),
    'fr/grece/simulateur-impot/index.html': (
        "Simulateur Impot Grece 2026 - Calcul du Net Gratuit",
        None,
    ),
    'fr/perou/simulateur-impot/index.html': (
        "Simulateur Impot Perou 2026 - Calcul du Net Gratuit",
        None,
    ),
    'fr/suede/simulateur-impot/index.html': (
        "Simulateur Impot Suede 2026 - Calcul du Net Gratuit",
        None,
    ),
}

# Language-specific padding strategies for descriptions
DESC_PADDERS = {
    'en': [
        (' 2026 rates.', ' Official 2026 rates included.'),  # +17
        (' 2026 rates.', ' 2026 official rates included.'),  # +17
        ('. 2026 rates.', '. Net salary breakdown. Official 2026 rates included.'),  # +37
        ('. 2026 rates.', '. Net salary. Official 2026 rates included.'),  # +30
        ('. 2026 rates.', ' and net salary. Official 2026 rates included.'),  # +33
        (' 2026 rates.', ' 2026 rates. Net salary calculation included.'),  # +32
    ],
    'fr': [
        ('Baremes 2026.', 'Baremes 2026 officiels inclus.'),  # +16
        ('Baremes 2026 inclus.', 'Baremes 2026 officiels inclus. Resultat instantane.'),  # +31
        ('Baremes 2026.', 'Baremes 2026 officiels. Resultat instantane.'),  # +30
        ('Barèmes 2026.', 'Barèmes 2026 officiels inclus.'),  # +16
        ('Barèmes 2026 inclus.', 'Barèmes 2026 officiels inclus. Résultat instantané.'),  # +31
        ('Barèmes 2026.', 'Barèmes 2026 officiels. Résultat instantané.'),  # +30
        ('. 2026.', '. Barèmes 2026 officiels inclus.'),  # +25
        ('. 2026.', '. Baremes 2026 officiels inclus.'),  # +25
    ],
    'es': [
        (' 2026.', ' oficiales 2026. Resultado instantáneo.'),  # +31
        (' oficiales 2026.', ' oficiales 2026. Resultado neto al instante.'),  # +28
    ],
    'ar': [
        ('الرسمية.', 'الرسمية. حاسبة دقيقة وموثوقة لحساب صافي الراتب.'),  # +41
        ('الرسمية.', 'الرسمية. احصل على نتائج دقيقة وفورية.'),  # +31
    ],
    'de': [
        (' 2026.', ' 2026. Sofortiges Ergebnis.'),  # +20
    ],
    'default': [
        ('. 2026.', '. 2026. Résultat instantané.'),  # generic FR fallback
    ],
}


def get_lang(path):
    """Get language code from path."""
    parts = path.split('/')
    if parts[0] in ('en', 'fr', 'es', 'de', 'ar', 'it', 'pt', 'nl', 'sv', 'da', 'no', 'fi',
                     'pl', 'cs', 'hu', 'ro', 'hr', 'el', 'tr', 'vi', 'th', 'ja', 'ko', 'zh',
                     'ms', 'id'):
        return parts[0]
    return 'fr'  # default


def adjust_desc(desc, lang, path, target_min=150, target_max=160):
    """Try to adjust desc to be within range."""
    dLen = len(desc)

    if target_min <= dLen <= target_max:
        return desc  # Already OK

    if dLen > target_max:
        # Too long - trim from end, word by word
        while len(desc) > target_max:
            # Remove last word
            last_space = desc.rstrip('.').rfind(' ')
            if last_space == -1:
                break
            desc = desc[:last_space] + '.'
        return desc

    # Too short - try padding strategies
    padders = DESC_PADDERS.get(lang, [])

    for old_end, new_end in padders:
        if old_end in desc:
            new_desc = desc.replace(old_end, new_end, 1)
            if target_min <= len(new_desc) <= target_max:
                return new_desc

    # If no padder worked, try appending generic text
    generic_pads = {
        'en': [' included.', ' Official rates.', ' Net salary breakdown included.',
               ' Free and instant calculation with net salary.'],
        'fr': [' officiels.', ' inclus.', ' Resultat net instantane.', ' officiels inclus.',
               ' Salaire net instantane. Gratuit.', ' Simulation gratuite et instantanee.'],
        'es': [' incluidas.', ' Sueldo neto incluido.', ' Resultado neto instantáneo.'],
        'de': [' Nettolohn inklusive.', ' Sofort und kostenlos.'],
        'ar': [' احصل على نتائج دقيقة وفورية.', ' حساب مجاني ودقيق وفوري.'],
        'pt': [' incluídas.', ' Salário líquido incluso.', ' Resultado instantâneo e gratuito.'],
        'nl': [' Nettoloon direct beschikbaar.', ' Direct en gratis beschikbaar.'],
        'it': [' Stipendio netto incluso.', ' Risultato istantaneo e gratuito.'],
        'cs': [' Okamžitý výsledek čisté mzdy. Aktuální sazby.'],
        'da': [' Nettoløn og fradrag inkluderet i beregningen.'],
        'el': [' Άμεσο αποτέλεσμα με καθαρό μισθό και εισφορές.'],
        'hr': [' Neto plaća uključena. Trenutačni i besplatni rezultati.'],
        'hu': [' Azonnali és ingyenes eredmény elérése online.'],
        'id': [' Hasil perhitungan gaji bersih secara instan dan akurat.'],
        'ms': [' Hasil pengiraan gaji bersih serta-merta dan tepat.'],
        'no': [' Netto lønn inkludert. Gratis og nøyaktig beregning.'],
        'pl': [' Wynagrodzenie netto uwzględnione. Wynik natychmiastowy.'],
        'ro': [' Rezultat net imediat. Calculator precis și actualizat.'],
        'sv': [' Nettolön inkluderad. Omedelbart och kostnadsfritt resultat.'],
        'tr': [' Net maaş hesaplama dahil. Anında ve ücretsiz sonuç.'],
        'vi': [' Kết quả lương ròng tức thì. Miễn phí và chính xác hoàn toàn.'],
        'fi': [],  # Finnish is too long, will be trimmed
    }

    pads = generic_pads.get(lang, generic_pads.get('fr', []))

    for pad in pads:
        # Try appending (replace final period, add pad)
        new_desc = desc.rstrip('.') + pad if not pad.startswith(' ') else desc.rstrip('.') + pad
        if target_min <= len(new_desc) <= target_max:
            return new_desc
        # Try with final period
        new_desc = desc.rstrip('.') + '.' + pad if not pad.startswith('.') else desc + pad
        if target_min <= len(new_desc) <= target_max:
            return new_desc

    # Last resort: pad with spaces or trim
    if dLen < target_min:
        print(f"  WARNING: Could not auto-pad {path} (desc={dLen})")
        return desc

    return desc


def main():
    # Import FIXES
    import _fix_seo
    FIXES = dict(_fix_seo.FIXES)

    adjusted = 0
    still_broken = []

    for path in list(FIXES.keys()):
        title, desc = FIXES[path]
        lang = get_lang(path)

        # Apply overrides first
        if path in OVERRIDES:
            ov_title, ov_desc = OVERRIDES[path]
            if ov_title is not None:
                title = ov_title
            if ov_desc is not None:
                desc = ov_desc

        # Adjust desc
        new_desc = adjust_desc(desc, lang, path)

        if title != FIXES[path][0] or new_desc != FIXES[path][1]:
            FIXES[path] = (title, new_desc)
            adjusted += 1

        # Validate
        tLen = len(title)
        dLen = len(new_desc)
        if not (50 <= tLen <= 60) or not (150 <= dLen <= 160):
            issues = []
            if not (50 <= tLen <= 60):
                issues.append(f"title={tLen}")
            if not (150 <= dLen <= 160):
                issues.append(f"desc={dLen}")
            still_broken.append((path, tLen, dLen, ', '.join(issues)))

    print(f"Adjusted {adjusted} entries")

    if still_broken:
        print(f"\nStill broken ({len(still_broken)}):")
        for path, tLen, dLen, issues in still_broken:
            print(f"  {path}: {issues}")
            if 'title' in issues:
                print(f"    TITLE ({tLen}): {FIXES[path][0]}")
            if 'desc' in issues:
                print(f"    DESC ({dLen}): {FIXES[path][1]}")
    else:
        print("\nAll entries now valid!")

    # Write back the corrected FIXES to _fix_seo.py
    print("\nWriting corrected _fix_seo.py...")

    with open('_fix_seo.py', 'r') as f:
        content = f.read()

    # Find the FIXES dict and replace each entry
    for path, (title, desc) in FIXES.items():
        # Find the entry in the file and replace
        # Match pattern: 'path': (\n        "old_title",\n        "old_desc",\n    ),
        escaped_path = re.escape(path)
        pattern = rf"('{escaped_path}':\s*\(\s*\n\s*)\".*?\"(,\s*\n\s*)\".*?\"(,\s*\n\s*\))"
        replacement = rf'\1"{title}"\2"{desc}"\3'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content

    with open('_fix_seo.py', 'w') as f:
        f.write(content)

    print("Done! Run 'python3 _fix_seo.py --check' to verify.")


if __name__ == '__main__':
    main()
