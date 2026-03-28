#!/usr/bin/env python3
"""
Update favicon tags and navbar logo across all HTML pages.

1. Replace existing favicon <link> tags with the new set (SVG + PNG + apple-touch)
2. Replace the "N." text logo in the navbar with the favicon.svg image
"""

import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# New favicon tags to insert
NEW_FAVICON_TAGS = """\
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
    <link rel="icon" type="image/png" sizes="512x512" href="/favicon-512x512.png">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">"""

# Regex to match existing favicon/apple-touch-icon lines
FAVICON_LINE_RE = re.compile(
    r'^\s*<link\s+rel="(?:icon|apple-touch-icon|shortcut icon)"[^>]*>\s*$'
)

# Regex to match the "N." logo div (multiline)
LOGO_RE = re.compile(
    r'<div class="w-8 h-8 bg-slate-900 rounded flex items-center justify-center '
    r'text-white font-semibold tracking-tighter shadow-md group-hover:bg-indigo-600 '
    r'transition-colors duration-300">\s*N\.\s*</div>',
    re.DOTALL
)

NEW_LOGO = '<img src="/favicon.svg" alt="NetSalaire" class="w-8 h-8">'


def update_favicons(lines):
    """Remove old favicon lines and insert new ones at the first occurrence."""
    favicon_indices = []
    for i, line in enumerate(lines):
        if FAVICON_LINE_RE.match(line):
            favicon_indices.append(i)

    if not favicon_indices:
        return lines, 0

    # Insert new tags at position of first old tag, remove all old ones
    first_idx = favicon_indices[0]
    new_lines = []
    inserted = False
    for i, line in enumerate(lines):
        if i in favicon_indices:
            if not inserted:
                new_lines.append(NEW_FAVICON_TAGS + '\n')
                inserted = True
            # Skip old favicon line
        else:
            new_lines.append(line)

    return new_lines, len(favicon_indices)


def update_logo(content):
    """Replace the N. logo div with an img tag."""
    new_content, count = LOGO_RE.subn(NEW_LOGO, content)
    return new_content, count


def process_file(filepath):
    """Process a single HTML file: update favicons and logo."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines(keepends=True)

    # Step 1: Update favicon lines
    new_lines, favicon_count = update_favicons(lines)
    new_content = ''.join(new_lines)

    # Step 2: Update logo
    new_content, logo_count = update_logo(new_content)

    changes = favicon_count + logo_count
    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return favicon_count, logo_count


def main():
    # Find all HTML files in the project
    html_files = glob.glob(os.path.join(BASE_DIR, '**', '*.html'), recursive=True)
    # Also check root level
    html_files += glob.glob(os.path.join(BASE_DIR, '*.html'))
    # Deduplicate
    html_files = sorted(set(html_files))

    total_favicon = 0
    total_logo = 0
    files_with_favicon = []
    files_with_logo = []

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, BASE_DIR)
        favicon_count, logo_count = process_file(filepath)

        if favicon_count > 0:
            files_with_favicon.append(rel_path)
            total_favicon += 1
        if logo_count > 0:
            files_with_logo.append(rel_path)
            total_logo += 1

    print(f"Favicon updated: {total_favicon} files")
    print(f"Logo updated: {total_logo} files")
    print(f"\n{'='*60}")

    if files_with_favicon:
        print(f"\nFavicon changes ({total_favicon} files):")
        for f in files_with_favicon[:10]:
            print(f"  {f}")
        if len(files_with_favicon) > 10:
            print(f"  ... and {len(files_with_favicon) - 10} more")

    if files_with_logo:
        print(f"\nLogo changes ({total_logo} files):")
        for f in files_with_logo[:10]:
            print(f"  {f}")
        if len(files_with_logo) > 10:
            print(f"  ... and {len(files_with_logo) - 10} more")


if __name__ == '__main__':
    main()
