from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_command(command: list[str]) -> None:
    print(f"> {' '.join(command)}")

    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        check=False,
    )

    if result.returncode != 0:
        raise SystemExit(
            f"فشل الأمر برمز خروج {result.returncode}"
        )


def main() -> None:
    print("بدء تجهيز الموقع...")

    run_command(
        [
            sys.executable,
            "scripts/generate_sitemap.py",
        ]
    )

    print("تم تجهيز الموقع بنجاح.")
    print("شغّل الموقع محليًا بالأمر:")
    print("python -m http.server 8000")


if __name__ == "__main__":
    main()