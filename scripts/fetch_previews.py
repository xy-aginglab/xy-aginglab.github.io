#!/usr/bin/env python3
"""Fetch missing publication preview images via DOI.

Sources tried in order:
1. OpenAlex — best_oa_location thumbnail or landing page OG image
2. CrossRef — link to publisher, then scrape OG image from landing page
3. PubMed — article thumbnail via PMID

Usage:
    python3 scripts/fetch_previews.py [--dry-run]
"""

import re
import os
import sys
import time
import urllib.request
import urllib.error
import json
import ssl

BIB_PATH = "_bibliography/papers.bib"
IMG_DIR = "assets/img/publication_preview"
EMAIL = "liji_xy@csu.edu.cn"
DELAY = 0.2  # seconds between API calls

# Skip SSL verification for some publisher sites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def parse_bib_entries(path):
    """Parse bib file, return list of (key, doi, pmid, has_preview)."""
    with open(path) as f:
        content = f.read()

    entries = []
    for match in re.finditer(r"@\w+\{(\w+),(.+?)(?=\n@|\Z)", content, re.DOTALL):
        key = match.group(1)
        block = match.group(2)
        doi_m = re.search(r"doi=\{(.+?)\}", block)
        pmid_m = re.search(r"pmid=\{(.+?)\}", block)
        has_preview = "preview=" in block
        doi = doi_m.group(1) if doi_m else None
        pmid = pmid_m.group(1) if pmid_m else None
        entries.append((key, doi, pmid, has_preview))
    return entries


def fetch_json(url):
    """Fetch URL and return parsed JSON."""
    req = urllib.request.Request(url, headers={"User-Agent": f"LiLab/1.0 (mailto:{EMAIL})"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def fetch_og_image(url):
    """Fetch a page and extract og:image URL."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    })
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            html = resp.read().decode("utf-8", errors="ignore")[:50000]
        # Look for og:image
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
        if m:
            img_url = m.group(1)
            if img_url.startswith("//"):
                img_url = "https:" + img_url
            return img_url
    except Exception:
        pass
    return None


def download_image(url, path):
    """Download image to path. Returns True on success."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    })
    try:
        with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
            data = resp.read()
            if len(data) < 2000:  # Too small, probably an error page
                return False
            content_type = resp.headers.get("Content-Type", "")
            if "html" in content_type:
                return False
            with open(path, "wb") as f:
                f.write(data)
            return True
    except Exception:
        return False


def try_openalex(doi):
    """Try OpenAlex for an OG image via the landing page."""
    data = fetch_json(f"https://api.openalex.org/works/doi:{doi}?mailto={EMAIL}")
    if not data:
        return None
    # Try best OA location landing page
    oa = data.get("best_oa_location") or {}
    landing = oa.get("landing_page_url")
    if landing:
        img = fetch_og_image(landing)
        if img:
            return img
    # Try primary location
    primary = data.get("primary_location") or {}
    landing = primary.get("landing_page_url")
    if landing:
        img = fetch_og_image(landing)
        if img:
            return img
    return None


def try_doi_landing(doi):
    """Resolve DOI and scrape og:image from landing page."""
    url = f"https://doi.org/{doi}"
    return fetch_og_image(url)


def try_pubmed(pmid):
    """Try PubMed article page for og:image."""
    if not pmid:
        return None
    return fetch_og_image(f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/")


def update_bib_preview(bib_path, key, filename):
    """Add preview={filename} to the bib entry."""
    with open(bib_path) as f:
        content = f.read()

    # Find the entry and add preview before the closing }
    pattern = rf"(@\w+\{{{key},.*?)(,\s*\n\}})"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # Add preview field before last comma+closing brace
        insertion = f",\n  preview={{{filename}}}"
        # Insert before citation_count or before the last }
        # Find a good insertion point - after the last field
        entry = match.group(0)
        # Insert preview before citation_count if it exists
        if "citation_count=" in entry:
            content = content.replace(
                f"@article{{{key},", f"@article{{{key},", 1
            )
            # More reliable: insert after basic= or selected= or bibtex_show=
            for anchor in ["bibtex_show={true},", "basic={true},", "selected={true},",
                          "clinical={true},", "language={en},"]:
                if anchor in entry:
                    content = content.replace(
                        anchor,
                        f"{anchor}\n  preview={{{filename}}},",
                        1
                    )
                    return content
        # Fallback: insert before citation_count
        cc_pattern = rf"(\n\s*citation_count=)"
        cc_match = re.search(cc_pattern, entry)
        if cc_match:
            old = entry
            new = entry[:cc_match.start()] + f"\n  preview={{{filename}}}," + entry[cc_match.start():]
            content = content.replace(old, new, 1)
            return content

    return None


def main():
    dry_run = "--dry-run" in sys.argv
    os.makedirs(IMG_DIR, exist_ok=True)

    entries = parse_bib_entries(BIB_PATH)
    missing = [(k, d, p) for k, d, p, has in entries if not has and d]

    print(f"Total entries: {len(entries)}")
    print(f"Missing previews with DOI: {len(missing)}")
    print()

    fetched = 0
    failed = []

    for i, (key, doi, pmid) in enumerate(missing):
        print(f"[{i+1}/{len(missing)}] {key} (doi:{doi})")
        ext = "jpg"
        out_path = os.path.join(IMG_DIR, f"{key}.{ext}")

        if os.path.exists(out_path):
            print(f"  Already exists, skipping")
            continue

        img_url = None

        # Strategy 1: OpenAlex → landing page OG image
        img_url = try_openalex(doi)
        if img_url:
            print(f"  Found via OpenAlex: {img_url[:80]}...")

        # Strategy 2: Direct DOI landing page
        if not img_url:
            time.sleep(DELAY)
            img_url = try_doi_landing(doi)
            if img_url:
                print(f"  Found via DOI landing: {img_url[:80]}...")

        # Strategy 3: PubMed
        if not img_url and pmid:
            time.sleep(DELAY)
            img_url = try_pubmed(pmid)
            if img_url:
                print(f"  Found via PubMed: {img_url[:80]}...")

        if img_url:
            if not dry_run:
                success = download_image(img_url, out_path)
                if success:
                    print(f"  ✓ Saved: {out_path}")
                    fetched += 1
                else:
                    print(f"  ✗ Download failed")
                    failed.append(key)
            else:
                print(f"  [dry-run] Would download: {img_url[:80]}")
                fetched += 1
        else:
            print(f"  ✗ No image found")
            failed.append(key)

        time.sleep(DELAY)

    print(f"\n--- Summary ---")
    print(f"Fetched: {fetched}")
    print(f"Failed: {len(failed)}")
    if failed:
        print(f"Failed keys: {', '.join(failed[:20])}")

    # Update bib file with preview fields
    if not dry_run and fetched > 0:
        print(f"\nUpdating {BIB_PATH} with preview fields...")
        with open(BIB_PATH) as f:
            content = f.read()

        updated = 0
        for key, doi, pmid in missing:
            img_file = f"{key}.jpg"
            img_path = os.path.join(IMG_DIR, img_file)
            if os.path.exists(img_path) and f"preview={{{img_file}}}" not in content:
                # Simple insertion: add preview after the doi line
                doi_line = f"doi={{{doi}}},"
                if doi_line in content:
                    content = content.replace(
                        doi_line,
                        f"{doi_line}\n  preview={{{img_file}}},",
                        1
                    )
                    updated += 1

        with open(BIB_PATH, "w") as f:
            f.write(content)
        print(f"Updated {updated} entries in {BIB_PATH}")


if __name__ == "__main__":
    main()
