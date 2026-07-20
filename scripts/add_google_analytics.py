from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MEASUREMENT_ID = "G-122WQ1BJ20"

START_MARKER = "<!-- GOOGLE-ANALYTICS-START -->"
END_MARKER = "<!-- GOOGLE-ANALYTICS-END -->"

TRACKING_CODE = f"""
    {START_MARKER}
    <script async src="https://www.googletagmanager.com/gtag/js?id={MEASUREMENT_ID}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{MEASUREMENT_ID}');
    </script>
    {END_MARKER}
"""


def update_html_file(path: Path) -> bool:
    document = path.read_text(encoding="utf-8-sig")

    # Skip the Google Search Console verification file.
    if path.name.startswith("google") and "site-verification" in document:
        print(f"SKIPPED verification file: {path.relative_to(ROOT)}")
        return False

    # Remove any previously inserted Analytics block.
    document = re.sub(
        rf"\s*{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}\s*",
        "\n",
        document,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Remove an existing copy of this specific GA tag, if present.
    document = re.sub(
        rf'\s*<script\s+async\s+src=["\']https://www\.googletagmanager\.com/'
        rf'gtag/js\?id={re.escape(MEASUREMENT_ID)}["\']></script>\s*'
        rf'<script>.*?gtag\(["\']config["\'],\s*["\']'
        rf'{re.escape(MEASUREMENT_ID)}["\']\);.*?</script>\s*',
        "\n",
        document,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if not re.search(r"<head(?:\s[^>]*)?>", document, flags=re.IGNORECASE):
        print(f"SKIPPED missing head: {path.relative_to(ROOT)}")
        return False

    document = re.sub(
        r"(<head(?:\s[^>]*)?>)",
        r"\1\n" + TRACKING_CODE,
        document,
        count=1,
        flags=re.IGNORECASE,
    )

    path.write_text(document, encoding="utf-8", newline="\n")
    print(f"UPDATED: {path.relative_to(ROOT)}")
    return True


def verify(files: list[Path]) -> None:
    problems: list[str] = []

    for path in files:
        document = path.read_text(encoding="utf-8-sig")

        if path.name.startswith("google") and "site-verification" in document:
            continue

        count = document.count(MEASUREMENT_ID)

        # The ID normally appears twice: once in the script URL and once in config.
        if count != 2:
            problems.append(
                f"{path.relative_to(ROOT)} contains GA ID {count} times"
            )

    if problems:
        print("\nVerification problems:")
        for problem in problems:
            print(f"- {problem}")
        raise SystemExit(1)

    print("\nAnalytics verification passed.")


def main() -> None:
    files = sorted(ROOT.rglob("*.html"))
    updated_files: list[Path] = []

    for path in files:
        # Ignore backup directories.
        if any(part.startswith("backup-") for part in path.parts):
            continue

        if update_html_file(path):
            updated_files.append(path)

    verify(updated_files)

    print(f"\nUpdated {len(updated_files)} HTML pages.")
    print("Google Analytics installation completed.")


if __name__ == "__main__":
    main()