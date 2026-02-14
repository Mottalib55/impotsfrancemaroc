#!/usr/bin/env python3
"""Update admin/index.html seoPairs and seoNativePages with actual SEO data from HTML files."""
import os, re, json

BASE = os.path.dirname(os.path.abspath(__file__))

def extract_seo(filepath):
    """Extract title and description from an HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content="([^"]*)"', content, re.DOTALL)
    title = title_m.group(1).strip() if title_m else ''
    desc = desc_m.group(1).strip() if desc_m else ''
    return title, desc

def path_to_file(url_path):
    """Convert URL path like /fr/faq/ to filesystem path."""
    # Remove leading/trailing slashes
    p = url_path.strip('/')
    if not p:
        return os.path.join(BASE, 'index.html')
    return os.path.join(BASE, p, 'index.html')

def js_escape(s):
    """Escape a string for JS single-quoted or double-quoted string."""
    return s.replace('\\', '\\\\').replace('"', '\\"')

# Read admin page
admin_path = os.path.join(BASE, 'admin', 'index.html')
with open(admin_path, 'r', encoding='utf-8') as f:
    admin_content = f.read()

# =====================================================
# Parse seoPairs structure to get all FR/EN paths
# =====================================================
# Extract the seoPairs block
pairs_match = re.search(
    r'const seoPairs = \[(.*?)\];\s*\n\s*const seoNativePages',
    admin_content, re.DOTALL
)
if not pairs_match:
    print("ERROR: Could not find seoPairs array")
    exit(1)

pairs_block = pairs_match.group(1)

# Parse each pair entry - extract name, fr.path, en.path
pair_entries = []
# Find all objects { name: ..., fr: { path: ... }, en: { path: ... } }
pattern = r'\{\s*name:\s*"([^"]*)".*?fr:\s*\{[^}]*path:\s*"([^"]*)".*?en:\s*\{[^}]*path:\s*"([^"]*)"'
for m in re.finditer(pattern, pairs_block, re.DOTALL):
    name = m.group(1)
    fr_path = m.group(2)
    en_path = m.group(3)
    pair_entries.append((name, fr_path, en_path))

print(f"Found {len(pair_entries)} seoPairs entries")

# =====================================================
# Parse seoNativePages structure to get all native URLs
# =====================================================
native_match = re.search(
    r'const seoNativePages = \[(.*?)\];\s*\n',
    admin_content, re.DOTALL
)
if not native_match:
    print("ERROR: Could not find seoNativePages array")
    exit(1)

native_block = native_match.group(1)
native_entries = []
for m in re.finditer(r'url:\s*"([^"]*)"', native_block):
    native_entries.append(m.group(1))

print(f"Found {len(native_entries)} seoNativePages entries")

# =====================================================
# Build updated seoPairs JS
# =====================================================
pairs_lines = []
for name, fr_path, en_path in pair_entries:
    fr_file = path_to_file(fr_path)
    en_file = path_to_file(en_path)

    if os.path.exists(fr_file):
        fr_title, fr_desc = extract_seo(fr_file)
    else:
        fr_title, fr_desc = f"MISSING: {fr_path}", ""
        print(f"  WARNING: FR file not found: {fr_file}")

    if os.path.exists(en_file):
        en_title, en_desc = extract_seo(en_file)
    else:
        en_title, en_desc = f"MISSING: {en_path}", ""
        print(f"  WARNING: EN file not found: {en_file}")

    pairs_lines.append(
        f'            {{\n'
        f'                name: "{js_escape(name)}",\n'
        f'                fr: {{ path: "{fr_path}", title: "{js_escape(fr_title)}", desc: "{js_escape(fr_desc)}" }},\n'
        f'                en: {{ path: "{en_path}", title: "{js_escape(en_title)}", desc: "{js_escape(en_desc)}" }}\n'
        f'            }}'
    )

new_pairs = ',\n'.join(pairs_lines)

# =====================================================
# Build updated seoNativePages JS
# =====================================================
native_lines = []
for url in native_entries:
    filepath = path_to_file(url)

    if os.path.exists(filepath):
        title, desc = extract_seo(filepath)
    else:
        title, desc = f"MISSING: {url}", ""
        print(f"  WARNING: Native file not found: {filepath}")

    native_lines.append(
        f'            {{\n'
        f'                url: "{url}",\n'
        f'                title: "{js_escape(title)}",\n'
        f'                desc: "{js_escape(desc)}"\n'
        f'            }}'
    )

new_native = ',\n'.join(native_lines)

# =====================================================
# Replace in admin content
# =====================================================
# Replace seoPairs
new_admin = re.sub(
    r'(const seoPairs = \[)\n.*?(\];\s*\n\s*const seoNativePages)',
    rf'\1\n{new_pairs}\n        \2',
    admin_content,
    count=1,
    flags=re.DOTALL
)

# Replace seoNativePages
new_admin = re.sub(
    r'(const seoNativePages = \[)\n.*?(\];\s*\n)',
    rf'\1\n{new_native}\n        \2',
    new_admin,
    count=1,
    flags=re.DOTALL
)

with open(admin_path, 'w', encoding='utf-8') as f:
    f.write(new_admin)

print(f"\nAdmin page updated with {len(pair_entries)} seoPairs + {len(native_entries)} seoNativePages entries.")
