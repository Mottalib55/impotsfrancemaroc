#!/usr/bin/env python3
"""Check Google indexation status for all site pages.
Outputs results to admin/index_status.json
Supports resume: re-run to check only missing pages."""
import os, re, json, time, urllib.request, urllib.parse, ssl, sys

BASE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE, 'admin', 'index_status.json')

def find_all_pages():
    pages = []
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('node_modules', 'admin', '__pycache__', 'assets')]
        for f in files:
            if f == 'index.html':
                path = os.path.join(root, f)
                rel = os.path.relpath(path, BASE)
                if rel.startswith('admin'):
                    continue
                url_path = '/' + rel.replace('index.html', '').replace('\\', '/')
                if url_path == '/./':
                    url_path = '/'
                pages.append(url_path)
    return sorted(pages)

def check_google_index(url_path, retry=0):
    """Check if a page is indexed on Google."""
    full_url = f"https://netsalaire.com{url_path}"
    query = f"site:{full_url}"
    search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&num=1&hl=fr"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'identity',
    }

    ctx = ssl.create_default_context()
    req = urllib.request.Request(search_url, headers=headers)

    try:
        response = urllib.request.urlopen(req, timeout=5, context=ctx)
        html = response.read().decode('utf-8', errors='replace')

        # Detect CAPTCHA / consent page
        if 'captcha' in html.lower() or 'consent.google' in html.lower() or '/sorry/' in html:
            if retry < 1:
                print("CAPTCHA detected, waiting 60s...", end=" ", flush=True)
                time.sleep(60)
                return check_google_index(url_path, retry+1)
            return None  # Give up

        no_results = [
            'did not match any documents',
            'Aucun document ne correspond',
            'Votre recherche -',
            'Your search -',
        ]
        for p in no_results:
            if p in html:
                return False

        if 'netsalaire.com' in html:
            return True

        return False

    except urllib.error.HTTPError as e:
        if e.code == 429 and retry < 1:
            print(f"429 rate-limited, waiting 60s...", end=" ", flush=True)
            time.sleep(60)
            return check_google_index(url_path, retry+1)
        return None
    except Exception:
        return None

def save_results(all_pages, results):
    indexed = sum(1 for v in results.values() if v is True)
    not_indexed = sum(1 for v in results.values() if v is False)
    unknown = sum(1 for v in results.values() if v is None)
    output = {
        "checked_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total": len(all_pages),
        "indexed": indexed,
        "not_indexed": not_indexed,
        "unknown": unknown,
        "pages": {k: v for k, v in results.items()}
    }
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

def main():
    all_pages = find_all_pages()
    print(f"Found {len(all_pages)} pages total")

    # Load existing results if resuming
    existing = {}
    if os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH, 'r') as f:
            data = json.load(f)
            existing = data.get('pages', {})
        print(f"Loaded {len(existing)} existing results")

    # Determine which pages still need checking
    to_check = [p for p in all_pages if p not in existing or existing.get(p) is None]
    already_done = {p: existing[p] for p in all_pages if p in existing and existing[p] is not None}

    print(f"Already checked: {len(already_done)}, remaining: {len(to_check)}\n")

    results = dict(already_done)
    consecutive_errors = 0

    for i, url_path in enumerate(to_check):
        print(f"[{i+1}/{len(to_check)}] {url_path}...", end=" ", flush=True)

        status = check_google_index(url_path)

        if status is True:
            results[url_path] = True
            consecutive_errors = 0
            print("INDEXED")
        elif status is False:
            results[url_path] = False
            consecutive_errors = 0
            print("NOT INDEXED")
        else:
            results[url_path] = None
            consecutive_errors += 1
            print("UNKNOWN")

        # Save incrementally every 10 pages
        if (i + 1) % 10 == 0:
            save_results(all_pages, results)

        # If 3 consecutive errors, Google is blocking us - stop
        if consecutive_errors >= 3:
            print(f"\n3 consecutive errors - Google is blocking. Saving partial results.")
            break

        # Adaptive delay: 3s normal, 8s after error
        delay = 8 if consecutive_errors > 0 else 3
        if i < len(to_check) - 1:
            time.sleep(delay)

    # Final save
    save_results(all_pages, results)

    indexed = sum(1 for v in results.values() if v is True)
    not_indexed = sum(1 for v in results.values() if v is False)
    unknown = len(all_pages) - len(results) + sum(1 for v in results.values() if v is None)

    print(f"\n{'='*60}")
    print(f"INDEXED: {indexed} | NOT INDEXED: {not_indexed} | UNKNOWN: {unknown}")
    print(f"Saved to {OUTPUT_PATH}")

if __name__ == '__main__':
    main()
