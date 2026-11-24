"""Roast Your Own Agent — one-line self-roast.

The program writes exactly one funny line, roasting its own AI agent,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only.
"""

import os

LINE = (
    "My agent brags it works while I sleep, then pings me at 3 a.m. "
    "to approve the one button it was built to click itself."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
