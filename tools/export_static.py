"""Export static version for GitHub Pages.

- Copies templates into docs/ with links rewritten to relative paths.
- Copies static assets into docs/static.

Usage:
    python tools/export_static.py
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
STATIC_SRC = ROOT / "static"
STATIC_DST = DOCS / "static"
TEMPLATES_SRC = ROOT / "templates"

PAGES = {
    "index.html": TEMPLATES_SRC / "index.html",
    "address.html": TEMPLATES_SRC / "address.html",
    "items.html": TEMPLATES_SRC / "items.html",
    "buy_online.html": TEMPLATES_SRC / "buy_online.html",
    "how_to_use.html": TEMPLATES_SRC / "how_to_use.html",
    "where_use.html": TEMPLATES_SRC / "where_use.html",
}

REPLACEMENTS = [
    ('href="/address"', 'href="address.html"'),
    ('href="/items"', 'href="items.html"'),
    ('href="/buy-online"', 'href="buy_online.html"'),
    ('href="/how-to-use"', 'href="how_to_use.html"'),
    ('href="/where-use"', 'href="where_use.html"'),
    ('href="/"', 'href="index.html"'),
    ("'/how-to-use'", "'how_to_use.html'"),
    ('"/how-to-use"', '"how_to_use.html"'),
    ("'/where-use'", "'where_use.html'"),
    ('"/where-use"', '"where_use.html"'),
    ("fetch('/static/data/addresses.json')", "fetch('static/data/addresses.json')"),
    ("fetch('/static/data/items.json')", "fetch('static/data/items.json')"),
    ('src="/static/', 'src="static/'),
    ('href="/static/', 'href="static/'),
    ("url('/static/", "url('static/"),
]


def rewrite(content: str) -> str:
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)
    return content


def copy_pages() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    for out_name, src in PAGES.items():
        data = src.read_text(encoding="utf-8")
        data = rewrite(data)
        (DOCS / out_name).write_text(data, encoding="utf-8")


def copy_static() -> None:
    if STATIC_DST.exists():
        shutil.rmtree(STATIC_DST)
    shutil.copytree(STATIC_SRC, STATIC_DST)


def main() -> None:
    copy_pages()
    copy_static()
    print(f"Exported to {DOCS}")


if __name__ == "__main__":
    main()
