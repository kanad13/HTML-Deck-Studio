#!/usr/bin/env python3
"""Run a small Playwright smoke test against 100-viewer.html and 200-demos."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover - exercised by users without dev deps
    print("Playwright is not installed. Run: python3 -m pip install -r 600-tools/requirements/dev.txt", file=sys.stderr)
    raise SystemExit(2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--headed", action="store_true", help="Run with a visible browser")
    parser.add_argument("--viewer", type=Path, default=Path("100-viewer.html"))
    parser.add_argument("--deck", type=Path, default=Path("200-demos"))
    args = parser.parse_args()

    viewer = args.viewer.resolve()
    deck = args.deck.resolve()
    slides = sorted(deck.glob("slide*.html"))
    if not viewer.is_file():
        print(f"{viewer} does not exist", file=sys.stderr)
        return 1
    if len(slides) < 2:
        print(f"{deck} must contain at least two slide*.html files", file=sys.stderr)
        return 1

    errors: list[str] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not args.headed)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(viewer.as_uri())

        page.set_input_files("#fileInput", [str(slide) for slide in slides])
        page.wait_for_selector("#app:not(.hidden)")
        expect_text(page, "#counter", f"1 / {len(slides)}")
        expect_text(page, "#deckMeta", f"{len(slides)} slides loaded")

        page.click("#nextBtn")
        expect_text(page, "#counter", f"2 / {len(slides)}")

        page.click("#notesBtn")
        page.wait_for_selector("#notesDrawer:not(.hidden)")
        notes_text = page.locator("#notesBody").inner_text(timeout=5000)
        if "aside" in notes_text.lower() and "no speaker notes" in notes_text.lower():
            raise AssertionError("speaker notes drawer did not find slide notes")

        page.click("#overviewBtn")
        page.wait_for_selector("#overviewOverlay:not(.hidden)")
        thumb_count = page.locator("#overviewGrid .thumb").count()
        if thumb_count != len(slides):
            raise AssertionError(f"expected {len(slides)} overview thumbs, found {thumb_count}")

        page.click("[data-close='overviewOverlay']")
        page.click("#themeBtn")
        theme = page.locator("body").get_attribute("data-theme")
        if theme != "light":
            raise AssertionError(f"theme toggle did not switch to light mode, got {theme!r}")

        if errors:
            raise AssertionError("page errors: " + "; ".join(errors))

        browser.close()

    print("viewer smoke test passed")
    return 0


def expect_text(page, selector: str, expected: str) -> None:
    try:
        text = page.locator(selector).inner_text(timeout=5000)
    except PlaywrightTimeoutError as error:
        raise AssertionError(f"{selector} was not readable") from error
    if text.strip() != expected:
        raise AssertionError(f"{selector} expected {expected!r}, got {text!r}")


if __name__ == "__main__":
    raise SystemExit(main())
