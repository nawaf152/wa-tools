from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
path = root / "privacy.html"

html = path.read_text(encoding="utf-8-sig")

# تعديل صنف قسم التحليلات فقط.
html = re.sub(
    r'(<!-- ANALYTICS-PRIVACY-START -->\s*)'
    r'<section class="content-section">',
    r'\1<section class="analytics-privacy">',
    html,
    count=1,
    flags=re.IGNORECASE,
)

style = """
<style id="analytics-privacy-style">
    .analytics-privacy {
        width: min(100% - 32px, 860px);
        margin: 32px auto;
        padding: 30px;
        background: var(--surface, #ffffff);
        border: 1px solid var(--border, #dce6e2);
        border-radius: var(--radius, 16px);
        box-shadow: var(--shadow, 0 12px 30px rgba(0, 0, 0, 0.06));
        line-height: 1.9;
    }

    .analytics-privacy h2 {
        margin-top: 30px;
        margin-bottom: 12px;
        font-size: 1.45rem;
    }

    .analytics-privacy h2:first-child {
        margin-top: 0;
    }

    .analytics-privacy p {
        margin-bottom: 14px;
        color: var(--text-muted, #455a54);
    }

    @media (max-width: 600px) {
        .analytics-privacy {
            width: min(100% - 20px, 860px);
            padding: 22px;
            margin: 20px auto;
        }

        .analytics-privacy h2 {
            font-size: 1.25rem;
        }
    }
</style>
"""

# إزالة نسخة قديمة من التنسيق إن وجدت.
html = re.sub(
    r'\s*<style id="analytics-privacy-style">.*?</style>\s*',
    "\n",
    html,
    flags=re.IGNORECASE | re.DOTALL,
)

html = html.replace("</head>", style + "\n</head>", 1)

path.write_text(html, encoding="utf-8", newline="\n")

print("Privacy layout fixed successfully.")