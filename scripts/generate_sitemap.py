from __future__ import annotations

from datetime import date
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom


PROJECT_ROOT = Path(__file__).resolve().parent.parent

BASE_URL = "https://example.pages.dev"

EXCLUDED_FILES = {
    "404.html",
}

EXCLUDED_DIRECTORIES = {
    "venv",
    ".git",
    "__pycache__",
}


def should_include(path: Path) -> bool:
    relative_path = path.relative_to(PROJECT_ROOT)

    if path.name in EXCLUDED_FILES:
        return False

    if any(part in EXCLUDED_DIRECTORIES for part in relative_path.parts):
        return False

    return path.suffix.lower() == ".html"


def html_path_to_url(path: Path) -> str:
    relative_path = path.relative_to(PROJECT_ROOT).as_posix()

    if relative_path == "index.html":
        return f"{BASE_URL}/"

    return f"{BASE_URL}/{relative_path}"


def get_priority(path: Path) -> str:
    relative_path = path.relative_to(PROJECT_ROOT).as_posix()

    if relative_path == "index.html":
        return "1.0"

    if relative_path.startswith("tools/"):
        return "0.9"

    if relative_path.startswith("guides/"):
        return "0.8"

    return "0.5"


def get_change_frequency(path: Path) -> str:
    relative_path = path.relative_to(PROJECT_ROOT).as_posix()

    if relative_path.startswith("tools/"):
        return "monthly"

    if relative_path.startswith("guides/"):
        return "monthly"

    return "yearly"


def build_sitemap() -> str:
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"

    urlset = Element(
        "urlset",
        {
            "xmlns": namespace,
        },
    )

    html_files = sorted(
        path
        for path in PROJECT_ROOT.rglob("*.html")
        if should_include(path)
    )

    today = date.today().isoformat()

    for html_file in html_files:
        url_element = SubElement(urlset, "url")

        location = SubElement(url_element, "loc")
        location.text = html_path_to_url(html_file)

        last_modified = SubElement(url_element, "lastmod")
        last_modified.text = today

        change_frequency = SubElement(url_element, "changefreq")
        change_frequency.text = get_change_frequency(html_file)

        priority = SubElement(url_element, "priority")
        priority.text = get_priority(html_file)

    rough_xml = tostring(
        urlset,
        encoding="utf-8",
        xml_declaration=True,
    )

    parsed_xml = minidom.parseString(rough_xml)

    return parsed_xml.toprettyxml(
        indent="  ",
        encoding="utf-8",
    ).decode("utf-8")


def main() -> None:
    sitemap_content = build_sitemap()
    sitemap_path = PROJECT_ROOT / "sitemap.xml"

    sitemap_path.write_text(
        sitemap_content,
        encoding="utf-8",
    )

    print(f"تم إنشاء خريطة الموقع: {sitemap_path}")


if __name__ == "__main__":
    main()