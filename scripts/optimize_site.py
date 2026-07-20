from __future__ import annotations

import html
import json
import re
import shutil
import urllib.request
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://ramfqconnect.shop"

SITE_NAME = (
    "\u0623\u062f\u0648\u0627\u062a "
    "\u0648\u0627\u062a\u0633\u0627\u0628 "
    "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"
)

DEFAULT_DESCRIPTION = (
    "\u0623\u062f\u0648\u0627\u062a "
    "\u0648\u0634\u0631\u0648\u062d\u0627\u062a "
    "\u0639\u0631\u0628\u064a\u0629 "
    "\u0645\u062c\u0627\u0646\u064a\u0629 "
    "\u0644\u0627\u0633\u062a\u062e\u062f\u0627\u0645 "
    "\u0648\u0627\u062a\u0633\u0627\u0628 "
    "\u0628\u0633\u0647\u0648\u0644\u0629 "
    "\u0648\u0643\u0641\u0627\u0621\u0629."
)

PAGES = [
    ("index.html", "", "WebSite"),
    ("about.html", "about.html", "WebPage"),
    ("contact.html", "contact.html", "WebPage"),
    ("privacy.html", "privacy.html", "WebPage"),
    ("terms.html", "terms.html", "WebPage"),

    (
        "tools/whatsapp-link.html",
        "tools/whatsapp-link.html",
        "WebApplication",
    ),
    (
        "tools/saudi-phone-formatter.html",
        "tools/saudi-phone-formatter.html",
        "WebApplication",
    ),
    (
        "tools/bulk-phone-formatter.html",
        "tools/bulk-phone-formatter.html",
        "WebApplication",
    ),
    (
        "tools/qr-generator.html",
        "tools/qr-generator.html",
        "WebApplication",
    ),
    (
        "tools/message-generator.html",
        "tools/message-generator.html",
        "WebApplication",
    ),

    (
        "guides/create-whatsapp-link.html",
        "guides/create-whatsapp-link.html",
        "Article",
    ),
    (
        "guides/saudi-phone-number-format.html",
        "guides/saudi-phone-number-format.html",
        "Article",
    ),
    (
        "guides/whatsapp-business-messages.html",
        "guides/whatsapp-business-messages.html",
        "Article",
    ),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def extract_title(document: str) -> str:
    match = re.search(
        r"<title[^>]*>(.*?)</title>",
        document,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if not match:
        return SITE_NAME

    return re.sub(r"\s+", " ", match.group(1)).strip()


def extract_description(document: str) -> str:
    patterns = [
        (
            r'<meta[^>]+name=["\']description["\'][^>]+'
            r'content=["\'](.*?)["\'][^>]*>'
        ),
        (
            r'<meta[^>]+content=["\'](.*?)["\'][^>]+'
            r'name=["\']description["\'][^>]*>'
        ),
    ]

    for pattern in patterns:
        match = re.search(
            pattern,
            document,
            flags=re.IGNORECASE | re.DOTALL,
        )

        if match:
            return re.sub(r"\s+", " ", match.group(1)).strip()

    return DEFAULT_DESCRIPTION


def canonical_url(url_path: str) -> str:
    if not url_path:
        return f"{BASE_URL}/"

    return f"{BASE_URL}/{url_path.lstrip('/')}"


def create_structured_data(
    page_type: str,
    title: str,
    description: str,
    url: str,
) -> dict:
    if page_type == "WebSite":
        return {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": SITE_NAME,
            "url": f"{BASE_URL}/",
            "description": description,
            "inLanguage": "ar",
        }

    if page_type == "WebApplication":
        return {
            "@context": "https://schema.org",
            "@type": "WebApplication",
            "name": title,
            "url": url,
            "description": description,
            "applicationCategory": "UtilitiesApplication",
            "operatingSystem": "Any",
            "browserRequirements": "Modern web browser with JavaScript",
            "inLanguage": "ar",
            "offers": {
                "@type": "Offer",
                "price": "0",
                "priceCurrency": "SAR",
            },
        }

    if page_type == "Article":
        return {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": description,
            "url": url,
            "mainEntityOfPage": url,
            "inLanguage": "ar",
            "author": {
                "@type": "Organization",
                "name": SITE_NAME,
            },
            "publisher": {
                "@type": "Organization",
                "name": SITE_NAME,
                "url": f"{BASE_URL}/",
            },
        }

    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "url": url,
        "description": description,
        "inLanguage": "ar",
        "isPartOf": {
            "@type": "WebSite",
            "name": SITE_NAME,
            "url": f"{BASE_URL}/",
        },
    }


def remove_old_seo_block(document: str) -> str:
    return re.sub(
        r"\s*<!-- SEO-START -->.*?<!-- SEO-END -->\s*",
        "\n",
        document,
        flags=re.IGNORECASE | re.DOTALL,
    )


def update_page(
    relative_path: str,
    url_path: str,
    page_type: str,
) -> None:
    path = PROJECT_ROOT / relative_path

    if not path.exists():
        print(f"SKIP missing: {relative_path}")
        return

    document = read_text(path)
    document = remove_old_seo_block(document)

    title = extract_title(document)
    description = extract_description(document)
    url = canonical_url(url_path)

    if relative_path.startswith(("tools/", "guides/")):
        favicon_path = "../favicon.svg"
    else:
        favicon_path = "favicon.svg"

    structured_data = create_structured_data(
        page_type=page_type,
        title=title,
        description=description,
        url=url,
    )

    json_ld = json.dumps(
        structured_data,
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("</", "<\\/")

    safe_title = html.escape(title, quote=True)
    safe_description = html.escape(description, quote=True)
    safe_site_name = html.escape(SITE_NAME, quote=True)
    safe_url = html.escape(url, quote=True)

    og_type = "article" if page_type == "Article" else "website"

    seo_block = f"""
    <!-- SEO-START -->
    <link rel="canonical" href="{safe_url}">
    <link rel="icon" href="{favicon_path}" type="image/svg+xml">

    <meta property="og:locale" content="ar_SA">
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="{safe_site_name}">
    <meta property="og:title" content="{safe_title}">
    <meta property="og:description" content="{safe_description}">
    <meta property="og:url" content="{safe_url}">

    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{safe_title}">
    <meta name="twitter:description" content="{safe_description}">

    <script type="application/ld+json">{json_ld}</script>
    <!-- SEO-END -->
"""

    if not re.search(r"</head\s*>", document, flags=re.IGNORECASE):
        raise RuntimeError(f"Missing </head> in {relative_path}")

    document = re.sub(
        r"</head\s*>",
        seo_block + "\n</head>",
        document,
        count=1,
        flags=re.IGNORECASE,
    )

    write_text(path, document)
    print(f"UPDATED: {relative_path}")


def create_backup() -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = PROJECT_ROOT / f"backup-{timestamp}"
    backup.mkdir(parents=True, exist_ok=False)

    items = [
        "index.html",
        "about.html",
        "contact.html",
        "privacy.html",
        "terms.html",
        "tools",
        "guides",
        "assets",
        "robots.txt",
        "sitemap.xml",
        ".htaccess",
        "favicon.svg",
        "404.html",
    ]

    for item in items:
        source = PROJECT_ROOT / item

        if not source.exists():
            continue

        destination = backup / item

        if source.is_dir():
            shutil.copytree(source, destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    return backup


def localize_qr_library() -> None:
    vendor_directory = PROJECT_ROOT / "assets/js/vendor"
    vendor_directory.mkdir(parents=True, exist_ok=True)

    qr_file = vendor_directory / "qrcode.min.js"
    qr_url = (
        "https://cdnjs.cloudflare.com/ajax/libs/"
        "qrcodejs/1.0.0/qrcode.min.js"
    )

    print("Downloading QR library...")
    urllib.request.urlretrieve(qr_url, qr_file)

    if qr_file.stat().st_size < 1000:
        raise RuntimeError("Downloaded QR library is incomplete.")

    page = PROJECT_ROOT / "tools/qr-generator.html"

    if not page.exists():
        raise FileNotFoundError(page)

    document = read_text(page)

    document = document.replace(
        qr_url,
        "../assets/js/vendor/qrcode.min.js",
    )

    write_text(page, document)
    print("QR library localized.")


def create_favicon() -> None:
    favicon = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="16" fill="#128c7e"/>
  <path d="M18 18h8l6 20 6-20h8L36 48h-8L18 18z"
        fill="#ffffff"/>
</svg>
"""

    write_text(PROJECT_ROOT / "favicon.svg", favicon)


def create_404_page() -> None:
    page_title = (
        "\u0627\u0644\u0635\u0641\u062d\u0629 "
        "\u063a\u064a\u0631 "
        "\u0645\u0648\u062c\u0648\u062f\u0629"
    )

    paragraph = (
        "\u0631\u0628\u0645\u0627 "
        "\u062a\u0645 "
        "\u062a\u063a\u064a\u064a\u0631 "
        "\u0639\u0646\u0648\u0627\u0646 "
        "\u0627\u0644\u0635\u0641\u062d\u0629 "
        "\u0623\u0648 "
        "\u062d\u0630\u0641\u0647\u0627."
    )

    home_text = (
        "\u0627\u0644\u0639\u0648\u062f\u0629 "
        "\u0625\u0644\u0649 "
        "\u0627\u0644\u0635\u0641\u062d\u0629 "
        "\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629"
    )

    document = f"""\
<!doctype html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{page_title} | {SITE_NAME}</title>
    <meta name="robots" content="noindex, follow">
    <meta name="theme-color" content="#128c7e">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
    <main>
        <section class="hero">
            <div class="container hero-content">
                <div>
                    <span class="eyebrow">404</span>
                    <h1>{page_title}</h1>
                    <p>{paragraph}</p>
                    <div class="hero-actions">
                        <a class="button button-primary" href="/">
                            {home_text}
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
"""

    write_text(PROJECT_ROOT / "404.html", document)


def create_htaccess() -> None:
    content = """\
Options -Indexes

DirectoryIndex index.html
ErrorDocument 404 /404.html

<IfModule mod_headers.c>
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Permissions-Policy "camera=(), microphone=(), geolocation=()"
</IfModule>

<IfModule mod_expires.c>
    ExpiresActive On

    ExpiresByType text/css "access plus 7 days"
    ExpiresByType application/javascript "access plus 7 days"
    ExpiresByType text/javascript "access plus 7 days"

    ExpiresByType image/svg+xml "access plus 30 days"
    ExpiresByType image/png "access plus 30 days"
    ExpiresByType image/jpeg "access plus 30 days"
    ExpiresByType image/webp "access plus 30 days"

    ExpiresByType text/html "access plus 1 hour"
    ExpiresByType application/xml "access plus 1 hour"
    ExpiresByType text/plain "access plus 1 hour"
</IfModule>

<IfModule mod_headers.c>
    <FilesMatch "\\.(css|js)$">
        Header set Cache-Control "public, max-age=604800"
    </FilesMatch>

    <FilesMatch "\\.(svg|png|jpg|jpeg|webp|ico)$">
        Header set Cache-Control "public, max-age=2592000"
    </FilesMatch>

    <FilesMatch "\\.(html|xml|txt)$">
        Header set Cache-Control "public, max-age=3600, must-revalidate"
    </FilesMatch>
</IfModule>
"""

    write_text(PROJECT_ROOT / ".htaccess", content)


def update_gitignore() -> None:
    path = PROJECT_ROOT / ".gitignore"

    existing = ""

    if path.exists():
        existing = read_text(path)

    line = "backup-*"

    if line not in existing.splitlines():
        if existing and not existing.endswith("\n"):
            existing += "\n"

        existing += line + "\n"
        write_text(path, existing)


def verify() -> None:
    problems: list[str] = []

    for relative_path, _, _ in PAGES:
        path = PROJECT_ROOT / relative_path

        if not path.exists():
            continue

        document = read_text(path)

        if 'rel="canonical"' not in document:
            problems.append(f"Missing canonical: {relative_path}")

        if "application/ld+json" not in document:
            problems.append(f"Missing JSON-LD: {relative_path}")

    qr_page = read_text(
        PROJECT_ROOT / "tools/qr-generator.html"
    )

    if "cdnjs.cloudflare.com" in qr_page:
        problems.append("External QR CDN link still exists.")

    if not (
        PROJECT_ROOT / "assets/js/vendor/qrcode.min.js"
    ).exists():
        problems.append("Local QR library is missing.")

    if problems:
        print("\nVerification problems:")

        for problem in problems:
            print(f"- {problem}")

        raise SystemExit(1)

    print("\nVerification passed.")


def main() -> None:
    print(f"Project: {PROJECT_ROOT}")

    backup = create_backup()
    print(f"Backup: {backup}")

    localize_qr_library()

    for relative_path, url_path, page_type in PAGES:
        update_page(
            relative_path=relative_path,
            url_path=url_path,
            page_type=page_type,
        )

    create_favicon()
    create_404_page()
    create_htaccess()
    update_gitignore()
    verify()

    print("\nOptimization completed successfully.")


if __name__ == "__main__":
    main()