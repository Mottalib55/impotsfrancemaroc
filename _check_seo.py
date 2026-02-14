#!/usr/bin/env python3
"""Find all pages with title not 50-60 chars or description not 150-160 chars."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

def extract_seo(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content="([^"]*)"', content, re.DOTALL)

    title = title_match.group(1).strip() if title_match else ''
    desc = desc_match.group(1).strip() if desc_match else ''
    return title, desc

def find_all_pages():
    pages = []
    for root, dirs, files in os.walk(BASE):
        # Skip hidden dirs, node_modules, .git
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        for f in files:
            if f == 'index.html':
                path = os.path.join(root, f)
                rel = os.path.relpath(path, BASE)
                # Skip admin
                if rel.startswith('admin'):
                    continue
                pages.append(path)
    return sorted(pages)

pages = find_all_pages()
bad = []
good = 0

for p in pages:
    title, desc = extract_seo(p)
    rel = os.path.relpath(p, BASE)
    url = '/' + rel.replace('index.html', '').replace('\\', '/')

    tLen = len(title)
    dLen = len(desc)
    tOk = 50 <= tLen <= 60
    dOk = 150 <= dLen <= 160

    if tOk and dOk:
        good += 1
    else:
        issues = []
        if not tOk:
            issues.append(f"title={tLen}")
        if not dOk:
            issues.append(f"desc={dLen}")
        bad.append((url, rel, title, tLen, desc, dLen, issues))

print(f"TOTAL: {len(pages)} pages")
print(f"OK: {good} pages")
print(f"A CORRIGER: {len(bad)} pages\n")

for url, rel, title, tLen, desc, dLen, issues in bad:
    print(f"{'='*80}")
    print(f"URL: {url}")
    print(f"FILE: {rel}")
    print(f"TITLE ({tLen} chars): {title}")
    print(f"DESC ({dLen} chars): {desc}")
    print(f"ISSUES: {', '.join(issues)}")
    print()
