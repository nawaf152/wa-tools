from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PRIVACY_FILE = ROOT / "privacy.html"

SECTION = """
<!-- ANALYTICS-PRIVACY-START -->
<section class="content-section">
    <h2>خدمات التحليلات والإحصاءات</h2>

    <p>
        يستخدم هذا الموقع خدمة Google Analytics لفهم كيفية استخدام الزوار
        للموقع، مثل الصفحات التي تتم زيارتها، ونوع الجهاز والمتصفح، والمدة
        التقريبية للزيارة. تساعدنا هذه المعلومات على تحسين أداء الموقع
        وتجربة المستخدم.
    </p>

    <p>
        قد تستخدم Google ملفات تعريف الارتباط أو تقنيات مشابهة لجمع بيانات
        استخدام عامة. لا نستخدم Google Analytics لجمع أسماء المستخدمين أو
        أرقام الهواتف أو محتوى البيانات التي يدخلونها في أدوات الموقع.
    </p>

    <p>
        تتم معالجة بيانات الأدوات مثل الأرقام والرسائل داخل المتصفح قدر
        الإمكان، ولا يتم إرسال محتوى هذه البيانات إلى Google Analytics.
    </p>

    <h2>ملفات تعريف الارتباط</h2>

    <p>
        قد يستخدم الموقع ملفات تعريف الارتباط الضرورية أو ملفات مرتبطة
        بخدمات التحليلات. يمكن للمستخدم تعطيل ملفات تعريف الارتباط من إعدادات
        المتصفح، مع احتمال تأثر بعض الوظائف أو دقة الإحصاءات.
    </p>

    <h2>إدارة بيانات Google Analytics</h2>

    <p>
        يمكن للمستخدم منع جمع بيانات Google Analytics من خلال إعدادات
        المتصفح أو أدوات منع التتبع المتاحة له.
    </p>
</section>
<!-- ANALYTICS-PRIVACY-END -->
"""

document = PRIVACY_FILE.read_text(encoding="utf-8-sig")

document = re.sub(
    r"\s*<!-- ANALYTICS-PRIVACY-START -->.*?<!-- ANALYTICS-PRIVACY-END -->\s*",
    "\n",
    document,
    flags=re.IGNORECASE | re.DOTALL,
)

if "</main>" not in document:
    raise RuntimeError("Missing </main> in privacy.html")

document = document.replace(
    "</main>",
    SECTION + "\n</main>",
    1,
)

PRIVACY_FILE.write_text(document, encoding="utf-8", newline="\n")

print("Privacy policy updated for Google Analytics.")