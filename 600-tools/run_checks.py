#!/usr/bin/env python3
"""Run the repository checks expected before viewer or deck changes are considered done."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", action="store_true", help="Also run the Playwright viewer smoke test")
    args = parser.parse_args()

    commands = []
    node = shutil.which("node")
    if node:
        commands.append([node, "600-tools/check_viewer.mjs"])
    else:
        print("node is required for viewer JavaScript syntax checks", file=sys.stderr)
        return 1

    commands.append([sys.executable, "600-tools/validate_deck.py", "200-demos", "--require-notes"])
    commands.append(["git", "diff", "--check"])
    if args.browser:
        commands.append([sys.executable, "600-tools/smoke_viewer.py"])

    for command in commands:
        print("+ " + " ".join(command))
        result = subprocess.run(command)
        if result.returncode:
            return result.returncode

    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
