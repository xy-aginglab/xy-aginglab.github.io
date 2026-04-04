#!/usr/bin/env python3
"""
Fetch new publications from PubMed for the Li Lab.

Filters:
  1. Affiliation: Xiangya Hospital OR Central South University
  2. Lab members must be first author OR corresponding (last) author
  3. Only papers from 2020 onwards
  4. Skips papers already in the .bib file (by PMID)

Output:
  - Appends new BibTeX entries to _bibliography/papers.bib
  - Prints a summary of new papers found
  - Exits with code 0 if no new papers, 1 if new papers added (for CI notification)
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

# ── Configuration ──

REPO_ROOT = Path(__file__).resolve().parent.parent
BIB_FILE = REPO_ROOT / "_bibliography" / "papers.bib"
MEMBERS_FILE = REPO_ROOT / "_data" / "members.yml"

PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
DOI_BIBTEX_URL = "https://doi.org/"

# Affiliation terms to match
AFFILIATIONS = [
    "Xiangya Hospital",
    "Central South University",
]

MIN_YEAR = 2026


# ── Helpers ──

def load_member_names():
    """Load lab member English names from members.yml (simple YAML parse)."""
    text = MEMBERS_FILE.read_text(encoding="utf-8")
    names = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("name_en:"):
            name = line.split(":", 1)[1].strip().strip('"').strip("'")
            if name:
                names.append(name)
    return names


def load_existing_pmids():
    """Extract all PMIDs already in the .bib file."""
    text = BIB_FILE.read_text(encoding="utf-8")
    return set(re.findall(r"pmid\s*=\s*\{(\d+)\}", text))


def pubmed_search(query, retmax=2000):
    """Search PubMed and return list of PMIDs."""
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json",
        "sort": "date",
    })
    url = f"{PUBMED_ESEARCH}?{params}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.loads(resp.read())
    return data.get("esearchresult", {}).get("idlist", [])


def pubmed_fetch(pmids):
    """Fetch full records from PubMed for given PMIDs. Returns XML root."""
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    })
    url = f"{PUBMED_EFETCH}?{params}"
    with urllib.request.urlopen(url, timeout=60) as resp:
        return ET.fromstring(resp.read())


def get_author_list(article):
    """Extract (last_name, first_name, initials, is_first, is_last) for each author."""
    author_list = article.find(".//AuthorList")
    if author_list is None:
        return []
    authors = []
    items = list(author_list.findall("Author"))
    for i, author in enumerate(items):
        last = author.findtext("LastName", "")
        fore = author.findtext("ForeName", "")
        initials = author.findtext("Initials", "")
        # Collect affiliation info for this author
        affil_parts = []
        for ai in author.findall("AffiliationInfo"):
            affil_parts.append(ai.findtext("Affiliation", ""))
        authors.append({
            "last": last,
            "fore": fore,
            "initials": initials,
            "is_first": i == 0,
            "is_last": i == len(items) - 1,
            "affiliations": " ".join(affil_parts).lower(),
        })
    return authors


def normalize_name(name):
    """Normalize a name for comparison: lowercase, strip accents, etc."""
    return re.sub(r"[^a-z]", "", name.lower())


# Terms that confirm the author belongs to our lab (not a namesake elsewhere)
LAB_AFFILIATION_TERMS = ["dermatol", "skin", "aging", "hair"]


def member_is_key_author(authors, member_name):
    """Check if a lab member is first or last (corresponding) author,
    AND their affiliation matches our lab (dermatology/aging)."""
    parts = member_name.strip().split()
    if len(parts) < 2:
        return False
    member_last = normalize_name(parts[-1])
    member_first = normalize_name(parts[0])

    for author in authors:
        if not (author["is_first"] or author["is_last"]):
            continue
        author_last = normalize_name(author["last"])
        author_fore = normalize_name(author["fore"])
        if author_last == member_last and (
            author_fore.startswith(member_first) or member_first.startswith(author_fore)
        ):
            # Verify affiliation if available
            affil = author.get("affiliations", "")
            if affil:
                if any(term in affil for term in LAB_AFFILIATION_TERMS):
                    return True
                # If affiliation exists but doesn't match our lab, skip
                continue
            # No affiliation data — accept (PubMed sometimes omits it)
            return True
    return False


def extract_paper_data(article):
    """Extract structured data from a PubMed XML article."""
    # Basic metadata
    pmid = article.findtext(".//PMID", "")
    title = article.findtext(".//ArticleTitle", "")
    abstract = article.findtext(".//AbstractText", "")
    journal = article.findtext(".//Journal/Title", "")
    journal_abbrev = article.findtext(".//Journal/ISOAbbreviation", "")
    year = article.findtext(".//Journal/JournalIssue/PubDate/Year", "")
    month = article.findtext(".//Journal/JournalIssue/PubDate/Month", "")
    volume = article.findtext(".//Journal/JournalIssue/Volume", "")
    issue = article.findtext(".//Journal/JournalIssue/Issue", "")
    pages = article.findtext(".//Pagination/MedlinePgn", "")

    # DOI
    doi = ""
    for eid in article.findall(".//ELocationID"):
        if eid.get("EIdType") == "doi":
            doi = eid.text or ""
            break
    if not doi:
        for aid in article.findall(".//ArticleId"):
            if aid.get("IdType") == "doi":
                doi = aid.text or ""
                break

    # Authors
    authors = get_author_list(article)
    author_str = " and ".join(
        f"{a['last']}, {a['initials']}." for a in authors
    )

    # First and corresponding authors
    first_authors = [f"{a['fore']} {a['last']}" for a in authors if a["is_first"]]
    corresponding_authors = [f"{a['fore']} {a['last']}" for a in authors if a["is_last"]]

    return {
        "pmid": pmid,
        "title": title.rstrip("."),
        "abstract": abstract or "",
        "journal": journal,
        "journal_abbrev": journal_abbrev,
        "year": year,
        "month": month,
        "volume": volume,
        "issue": issue,
        "pages": pages,
        "doi": doi,
        "author_str": author_str,
        "first_authors": "; ".join(first_authors),
        "corresponding_authors": "; ".join(corresponding_authors),
        "authors": authors,
    }


def generate_bib_key(paper):
    """Generate a BibTeX key like 'li2026natcommun'."""
    first_last = ""
    if paper["authors"]:
        first_last = paper["authors"][0]["last"].lower()
    year = paper["year"]
    journal_word = re.sub(r"[^a-z]", "", paper["journal_abbrev"].lower())[:10]
    # Take first meaningful word from title
    title_words = re.sub(r"[^a-z\s]", "", paper["title"].lower()).split()
    skip = {"a", "an", "the", "of", "in", "for", "and", "with", "by", "on", "to", "from", "is", "are"}
    title_word = ""
    for w in title_words:
        if w not in skip and len(w) > 2:
            title_word = w[:8]
            break
    return f"{first_last}{year}{journal_word}_{title_word}"


def escape_bibtex(text):
    """Escape special characters for BibTeX."""
    return text.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")


def format_bibtex_entry(paper):
    """Format a paper as a BibTeX entry."""
    key = generate_bib_key(paper)
    lines = [f"@article{{{key},"]
    lines.append(f"  title={{{escape_bibtex(paper['title'])}}},")
    lines.append(f"  author={{{escape_bibtex(paper['author_str'])}}},")
    lines.append(f"  first_author={{{paper['first_authors']}}},")
    lines.append(f"  corresponding_author={{{paper['corresponding_authors']}}},")
    lines.append(f"  journal={{{paper['journal']}}},")
    lines.append(f"  year={{{paper['year']}}},")
    if paper["month"]:
        lines.append(f"  month={{{paper['month']}}},")
    if paper["doi"]:
        lines.append(f"  doi={{{paper['doi']}}},")
    if paper["volume"]:
        lines.append(f"  volume={{{paper['volume']}}},")
    if paper["issue"]:
        lines.append(f"  number={{{paper['issue']}}},")
    if paper["pages"]:
        lines.append(f"  pages={{{paper['pages']}}},")
    lines.append(f"  pmid={{{paper['pmid']}}},")
    if paper["abstract"]:
        lines.append(f"  abstract={{{escape_bibtex(paper['abstract'])}}},")
    lines.append(f"  language={{en}},")
    lines.append(f"  bibtex_show={{true}},")
    lines.append(f"  author_verified={{pubmed_auto}},")
    lines.append("}")
    return "\n".join(lines)


# ── Main ──

def main():
    print("=" * 60)
    print("Li Lab Publication Fetcher")
    print("=" * 60)

    # Load data
    members = load_member_names()
    existing_pmids = load_existing_pmids()
    print(f"\nLab members: {len(members)}")
    print(f"Existing papers in .bib: {len(existing_pmids)}")

    # Build PubMed query
    affil_query = " OR ".join(f'"{a}"[Affiliation]' for a in AFFILIATIONS)
    date_filter = f"{MIN_YEAR}:3000[Date - Publication]"
    query = f"({affil_query}) AND ({date_filter})"
    print(f"\nPubMed query: {query}")

    # Search PubMed
    print("\nSearching PubMed...")
    all_pmids = pubmed_search(query)
    print(f"Found {len(all_pmids)} total results")

    # Filter out already-known papers
    new_pmids = [p for p in all_pmids if p not in existing_pmids]
    print(f"New (not in .bib): {len(new_pmids)}")

    if not new_pmids:
        print("\nNo new papers to process.")
        return 0

    # Fetch details in batches of 50
    new_papers = []
    for i in range(0, len(new_pmids), 50):
        batch = new_pmids[i:i+50]
        print(f"\nFetching details for batch {i//50 + 1} ({len(batch)} papers)...")
        root = pubmed_fetch(batch)
        time.sleep(0.5)  # Be nice to NCBI

        for article in root.findall(".//PubmedArticle"):
            paper = extract_paper_data(article.find(".//Article"))

            # Filter: lab member must be first or corresponding author
            matched_member = None
            for member in members:
                if member_is_key_author(paper["authors"], member):
                    matched_member = member
                    break

            if matched_member:
                paper["matched_member"] = matched_member
                new_papers.append(paper)

    print(f"\nPapers with lab member as first/corresponding author: {len(new_papers)}")

    if not new_papers:
        print("No qualifying new papers found.")
        return 0

    # Append to .bib file
    bib_content = BIB_FILE.read_text(encoding="utf-8")
    additions = []
    for paper in new_papers:
        entry = format_bibtex_entry(paper)
        additions.append(entry)
        print(f"\n  + [{paper['year']}] {paper['title'][:80]}...")
        print(f"    {paper['journal']}")
        print(f"    Key author: {paper['matched_member']}")
        print(f"    PMID: {paper['pmid']}, DOI: {paper['doi']}")

    # Append new entries
    separator = "\n\n% ---- Auto-fetched papers ----\n\n"
    if "Auto-fetched papers" not in bib_content:
        bib_content += separator
    bib_content += "\n\n".join(additions) + "\n"
    BIB_FILE.write_text(bib_content, encoding="utf-8")

    print(f"\n{'=' * 60}")
    print(f"Added {len(new_papers)} new paper(s) to {BIB_FILE.name}")
    print(f"{'=' * 60}")

    # Write summary for GitHub Actions
    summary_file = REPO_ROOT / "scripts" / "new_papers_summary.md"
    lines = [f"# New Publications Found ({len(new_papers)})\n"]
    for paper in new_papers:
        lines.append(f"## {paper['title']}\n")
        lines.append(f"- **Journal**: {paper['journal']}")
        lines.append(f"- **Year**: {paper['year']}")
        lines.append(f"- **Key author**: {paper['matched_member']}")
        lines.append(f"- **DOI**: {paper['doi']}")
        lines.append(f"- **PMID**: {paper['pmid']}")
        lines.append("")
    summary_file.write_text("\n".join(lines), encoding="utf-8")

    return 1  # Signal: new papers found


if __name__ == "__main__":
    sys.exit(main())
