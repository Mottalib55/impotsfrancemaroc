#!/usr/bin/env python3
"""
Exhaustive audit of hreflang and canonical tags across all HTML pages.

Checks:
1. Every page has a self-referential canonical
2. Every hreflang link is reciprocal (if A→B exists, B→A must exist)
3. Every canonical URL matches the page's own URL
4. No orphan pages (pages without hreflang)
"""

import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOMAIN = 'https://netsalaire.com'

# Skip redirect-only pages
SKIP_FILES = {'index.html'}  # root redirect


def url_from_path(filepath):
    """Convert file path to URL path."""
    rel = os.path.relpath(filepath, BASE_DIR).replace('\\', '/')
    if rel.endswith('/index.html'):
        return '/' + rel[:-len('index.html')]
    return '/' + rel


def extract_tags(filepath):
    """Extract canonical and hreflang tags from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Only look in <head>
    head_match = re.search(r'<head[^>]*>(.*?)</head>', content, re.DOTALL)
    if not head_match:
        return None, {}

    head = head_match.group(1)

    # Canonical
    canon_match = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', head)
    canonical = canon_match.group(1) if canon_match else None

    # Hreflang
    hreflangs = {}
    for m in re.finditer(r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"', head):
        lang, url = m.group(1), m.group(2)
        hreflangs[lang] = url

    return canonical, hreflangs


def main():
    html_files = sorted(glob.glob(os.path.join(BASE_DIR, '**', '*.html'), recursive=True))

    pages = {}  # url_path -> {canonical, hreflangs, filepath}
    errors = []
    warnings = []

    # Phase 1: Collect all data
    for filepath in html_files:
        rel = os.path.relpath(filepath, BASE_DIR)
        if rel in SKIP_FILES or rel == '404.html':
            continue

        url_path = url_from_path(filepath)
        full_url = DOMAIN + url_path
        canonical, hreflangs = extract_tags(filepath)

        if canonical is None and not hreflangs:
            warnings.append(f"NO TAGS: {rel}")
            continue

        pages[full_url] = {
            'canonical': canonical,
            'hreflangs': hreflangs,
            'filepath': rel,
        }

    print(f"Pages analyzed: {len(pages)}")

    # Phase 2: Check canonical self-reference
    print(f"\n{'='*60}")
    print("CHECK 1: Canonical self-reference")
    canon_ok = 0
    for url, data in pages.items():
        if data['canonical'] != url:
            errors.append(f"CANONICAL MISMATCH: {data['filepath']}\n"
                          f"  Expected: {url}\n"
                          f"  Got:      {data['canonical']}")
        else:
            canon_ok += 1
    print(f"  OK: {canon_ok}/{len(pages)}")

    # Phase 3: Check hreflang reciprocity
    print(f"\n{'='*60}")
    print("CHECK 2: Hreflang reciprocity")
    recip_ok = 0
    recip_fail = 0
    for url, data in pages.items():
        for lang, target_url in data['hreflangs'].items():
            if lang == 'x-default':
                continue
            if target_url == url:
                continue  # Self-reference, OK

            # Check that target page links back
            if target_url not in pages:
                errors.append(f"BROKEN HREFLANG: {data['filepath']}\n"
                              f"  hreflang={lang} points to {target_url}\n"
                              f"  But that page does not exist!")
                recip_fail += 1
                continue

            target_data = pages[target_url]
            # Find this page's lang in the target's hreflangs
            found_back = False
            for back_lang, back_url in target_data['hreflangs'].items():
                if back_url == url:
                    found_back = True
                    break

            if found_back:
                recip_ok += 1
            else:
                errors.append(f"NO RECIPROCITY: {data['filepath']}\n"
                              f"  hreflang={lang} → {target_url}\n"
                              f"  But {target_data['filepath']} does NOT link back to {url}")
                recip_fail += 1

    print(f"  OK: {recip_ok} reciprocal links")
    print(f"  FAIL: {recip_fail} broken reciprocities")

    # Phase 4: Check pages without hreflang
    print(f"\n{'='*60}")
    print("CHECK 3: Pages without hreflang")
    no_hreflang = [data['filepath'] for url, data in pages.items() if not data['hreflangs']]
    if no_hreflang:
        for f in no_hreflang:
            warnings.append(f"NO HREFLANG: {f}")
        print(f"  {len(no_hreflang)} pages without hreflang")
    else:
        print(f"  All {len(pages)} pages have hreflang tags")

    # Phase 5: Check self-hreflang
    print(f"\n{'='*60}")
    print("CHECK 4: Self-hreflang (page includes itself)")
    self_ok = 0
    for url, data in pages.items():
        has_self = any(href_url == url for href_url in data['hreflangs'].values())
        if has_self:
            self_ok += 1
        else:
            if data['hreflangs']:
                warnings.append(f"NO SELF-HREFLANG: {data['filepath']}\n"
                                f"  Page {url} not in its own hreflang set")
    print(f"  OK: {self_ok}/{len(pages)}")

    # Phase 6: Cluster analysis
    print(f"\n{'='*60}")
    print("CHECK 5: Cluster analysis")
    # Group pages into clusters
    visited = set()
    clusters = []
    for url in pages:
        if url in visited:
            continue
        cluster = set()
        stack = [url]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            cluster.add(current)
            if current in pages:
                for href_url in pages[current]['hreflangs'].values():
                    if href_url in pages and href_url not in visited:
                        stack.append(href_url)
        clusters.append(cluster)

    print(f"  {len(clusters)} hreflang clusters found")
    size_dist = {}
    for c in clusters:
        size = len(c)
        size_dist[size] = size_dist.get(size, 0) + 1
    for size in sorted(size_dist):
        print(f"    Size {size}: {size_dist[size]} clusters")

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"  Total pages: {len(pages)}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")

    if errors:
        print(f"\n{'='*60}")
        print("ERRORS (must fix):")
        for e in errors:
            print(f"\n  {e}")

    if warnings:
        print(f"\n{'='*60}")
        print("WARNINGS:")
        for w in warnings:
            print(f"  {w}")


if __name__ == '__main__':
    main()
