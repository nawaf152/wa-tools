from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PUBLISHER_ID = "ca-pub-5079491439257801"

START_MARKER = "<!-- ADSENSE-START -->"
END_MARKER = "<!-- ADSENSE-END -->"

ADSENSE_CODE = f"""
    {START_MARKER}
    <script
        async
        src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUBLISHER_ID}"
        crossorigin="anonymous">
    </script>
    {END_MARKER}
"""


def should_skip(path: Path, document: str) -> bool:
    if any(part.startswith("backup-") for part in path.parts):
        return True

    if path.name == "404.html":
        return True

    if path.name.startswith("google") and "site-verification" in document:
        return True

    return False


def update_page(path: Path) -> bool:
    document = path.read_text(encoding="utf-8-sig")

    if should_skip(path, document):
        print(f"SKIPPED: {path.relative_to(ROOT)}")
        return False

    # Remove a block previously added by this script.
    document = re.sub(
        rf"\s*{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}\s*",
        "\n",
        document,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Remove an unmarked existing AdSense loader to avoid duplication.
    document = re.sub(
        r'\s*<script[^>]*src=["\']'
        r'https://pagead2\.googlesyndication\.com/pagead/js/'
        r'adsbygoogle\.js\?client=ca-pub-\d+'
        r'["\'][^>]*>\s*</script>\s*',
        "\n",
        document,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if not re.search(r"</head\s*>", document, flags=re.IGNORECASE):
        print(f"SKIPPED missing head: {path.relative_to(ROOT)}")
        return False

    document = re.sub(
        r"</head\s*>",
        ADSENSE_CODE + "\n</head>",
        document,
        count=1,
        flags=re.IGNORECASE,
    )

    path.write_text(document, encoding="utf-8", newline="\n")
    print(f"UPDATED: {path.relative_to(ROOT)}")
    return True


def verify(updated_files: list[Path]) -> None:
    problems: list[str] = []

    for path in updated_files:
        document = path.read_text(encoding="utf-8-sig")
        count = document.count(PUBLISHER_ID)

        if count != 1:
            problems.append(
                f"{path.relative_to(ROOT)} contains publisher ID {count} times"
            )

    if problems:
        print("\nVerification problems:")

        for problem in problems:
            print(f"- {problem}")

        raise SystemExit(1)

    print("\nAdSense verification passed.")


def main() -> None:
    updated_files: list[Path] = []

    for path in sorted(ROOT.rglob("*.html")):
        if update_page(path):
            updated_files.append(path)

    verify(updated_files)

    print(f"\nUpdated {len(updated_files)} HTML pages.")
    print("AdSense code installation completed.")


if __name__ == "__main__":
    main()