from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

CARDS = """
<!-- EXTRA-GUIDES-START -->
<article class="card">
    <h3>إضافة رابط واتساب إلى إنستغرام</h3>
    <p>
        خطوات عملية لإضافة رابط واتساب إلى الملف الشخصي وتسهيل تواصل العملاء.
    </p>
    <a href="guides/whatsapp-link-instagram.html">قراءة الدليل</a>
</article>

<article class="card">
    <h3>إنشاء رمز QR لرابط واتساب</h3>
    <p>
        تعرف على طريقة إنشاء رمز قابل للمسح مع نصائح للاختبار والطباعة.
    </p>
    <a href="guides/create-whatsapp-qr-code.html">قراءة الدليل</a>
</article>

<article class="card">
    <h3>قوالب رسائل خدمة العملاء</h3>
    <p>
        نماذج جاهزة للترحيب وتأكيد الطلبات والمواعيد والتوصيل والمتابعة.
    </p>
    <a href="guides/customer-service-whatsapp-templates.html">قراءة الدليل</a>
</article>

<article class="card">
    <h3>تنظيف قائمة أرقام العملاء</h3>
    <p>
        دليل لتوحيد صيغ الأرقام وإزالة الأخطاء والتكرار قبل الاستخدام.
    </p>
    <a href="guides/clean-customer-phone-list.html">قراءة الدليل</a>
</article>
<!-- EXTRA-GUIDES-END -->
"""

document = INDEX.read_text(encoding="utf-8-sig")

document = re.sub(
    r"\s*<!-- EXTRA-GUIDES-START -->.*?<!-- EXTRA-GUIDES-END -->\s*",
    "\n",
    document,
    flags=re.IGNORECASE | re.DOTALL,
)

patterns = [
    r'(<section[^>]+id=["\']guides["\'][\s\S]*?<div[^>]+class=["\'][^"\']*(?:grid|cards)[^"\']*["\'][^>]*>)([\s\S]*?)(</div>)',
    r'(<div[^>]+id=["\']guides["\'][^>]*>)([\s\S]*?)(</div>)',
]

updated = False

for pattern in patterns:
    match = re.search(pattern, document, flags=re.IGNORECASE)

    if match:
        replacement = (
            match.group(1)
            + match.group(2)
            + "\n"
            + CARDS
            + "\n"
            + match.group(3)
        )

        document = (
            document[:match.start()]
            + replacement
            + document[match.end():]
        )

        updated = True
        break

if not updated:
    raise RuntimeError(
        "لم يتم العثور على قسم الأدلة في index.html. "
        "لا تعدل الملف يدويًا وأرسل نتيجة البحث."
    )

INDEX.write_text(document, encoding="utf-8", newline="\n")

print("Homepage guide links added successfully.")