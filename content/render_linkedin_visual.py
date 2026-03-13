#!/usr/bin/env python3
"""
Render a LinkedIn editorial card from the HTML/CSS template.

Usage:
  python3 content/render_linkedin_visual.py \
    --html tmp/linkedin-visual.html \
    --output content/accounts/<account-slug>/visuals/linkedin/YYYY-MM-DD-slug.png
"""

import argparse
import sys
from pathlib import Path


def render_with_playwright(html_path: Path, output_path: Path) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 1200}, device_scale_factor=2)
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        page.screenshot(path=str(output_path), full_page=True)
        browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Render LinkedIn visual card to PNG")
    parser.add_argument("--html", required=True, help="Path to prepared HTML file")
    parser.add_argument("--output", required=True, help="Path to output PNG file")
    args = parser.parse_args()

    html_path = Path(args.html)
    output_path = Path(args.output)

    if not html_path.exists():
        print(f"❌ HTML input not found: {html_path}")
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        render_with_playwright(html_path, output_path)
    except ImportError:
        print("❌ Playwright is not installed. Install it before rendering visuals.")
        return 1
    except Exception as exc:
        print(f"❌ Failed to render visual: {exc}")
        return 1

    print(f"✅ Rendered visual: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
