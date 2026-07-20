from __future__ import annotations

from pathlib import Path
from html import escape
import re


ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://ramfqconnect.shop"
SITE_NAME = "أدوات واتساب العربية"


GUIDES = {
    "whatsapp-link-instagram.html": {
        "title": "طريقة إضافة رابط واتساب إلى إنستغرام",
        "description": (
            "شرح عملي لإنشاء رابط واتساب وإضافته إلى الملف الشخصي "
            "في إنستغرام لتسهيل تواصل العملاء."
        ),
        "heading": "طريقة إضافة رابط واتساب إلى إنستغرام",
        "content": """
<p>
يتيح وضع رابط واتساب في حساب إنستغرام للزائر الانتقال مباشرة من الملف
الشخصي إلى المحادثة، دون الحاجة إلى نسخ الرقم أو حفظه في جهات الاتصال.
ويفيد ذلك المتاجر المنزلية ومقدمي الخدمات والحسابات التجارية.
</p>

<h2>الخطوة الأولى: تجهيز رقم واتساب</h2>
<p>
استخدم رقمًا مخصصًا للعمل إن أمكن، وتأكد من أن الرقم مرتبط بحساب واتساب
نشط. يجب كتابة الرقم بصيغته الدولية عند إنشاء الرابط.
</p>

<h2>الخطوة الثانية: إنشاء رابط واتساب</h2>
<p>
بالنسبة للرقم السعودي، احذف الصفر الأول وأضف رمز الدولة 966. يمكن استخدام
مولد رابط واتساب في الموقع لإنشاء الرابط وإضافة رسالة افتتاحية جاهزة.
</p>

<p>
<a class="button button-primary" href="../tools/whatsapp-link.html">
إنشاء رابط واتساب
</a>
</p>

<h2>الخطوة الثالثة: إضافة الرابط إلى إنستغرام</h2>
<ol>
<li>افتح حسابك في تطبيق إنستغرام.</li>
<li>انتقل إلى تعديل الملف الشخصي.</li>
<li>افتح قسم الروابط.</li>
<li>اختر إضافة رابط خارجي.</li>
<li>الصق رابط واتساب واكتب عنوانًا واضحًا.</li>
<li>احفظ التغييرات واختبر الرابط.</li>
</ol>

<h2>اختيار رسالة افتتاحية مناسبة</h2>
<p>
اجعل الرسالة قصيرة وتوضح سبب التواصل، مثل: السلام عليكم، أرغب في معرفة
تفاصيل المنتج. لا تضع بيانات شخصية أو معلومات حساسة داخل الرابط.
</p>

<h2>أخطاء شائعة</h2>
<ul>
<li>إضافة رقم محلي دون تحويله إلى الصيغة الدولية.</li>
<li>استخدام رابط طويل أو غير مكتمل.</li>
<li>عدم اختبار الرابط من حساب أو جهاز آخر.</li>
<li>وضع عنوان غير واضح للرابط.</li>
</ul>

<h2>الأسئلة الشائعة</h2>
<details>
<summary>هل يمكن إضافة أكثر من رابط في إنستغرام؟</summary>
<p>
تعتمد الخيارات المتاحة على إعدادات حساب إنستغرام الحالية، ويمكن ترتيب
الروابط بحيث يظهر رابط التواصل بوضوح.
</p>
</details>

<details>
<summary>هل يمكن تغيير الرسالة الجاهزة لاحقًا؟</summary>
<p>نعم، أنشئ رابطًا جديدًا ثم استبدل الرابط السابق في الملف الشخصي.</p>
</details>
""",
    },

    "create-whatsapp-qr-code.html": {
        "title": "طريقة إنشاء رمز QR لرابط واتساب",
        "description": (
            "تعلم إنشاء رمز QR يفتح محادثة واتساب مباشرة، مع نصائح "
            "للاختبار والطباعة والاستخدام التجاري."
        ),
        "heading": "طريقة إنشاء رمز QR لرابط واتساب",
        "content": """
<p>
يمكن استخدام رمز QR لتحويل رابط واتساب إلى رمز قابل للمسح بكاميرا الهاتف.
وهو مناسب للمتاجر وبطاقات العمل والفواتير والإعلانات وقوائم الطعام.
</p>

<h2>إنشاء رابط واتساب أولًا</h2>
<p>
ابدأ بإنشاء رابط مباشر للرقم المطلوب. تأكد من صحة رمز الدولة، ويمكنك إضافة
رسالة جاهزة تظهر للعميل عند فتح المحادثة.
</p>

<h2>تحويل الرابط إلى رمز QR</h2>
<ol>
<li>انسخ رابط واتساب بعد اختباره.</li>
<li>افتح مولد رمز QR.</li>
<li>الصق الرابط في الحقل.</li>
<li>أنشئ الرمز ثم نزّله.</li>
<li>اختبر الصورة بكاميرا هاتف مختلف.</li>
</ol>

<p>
<a class="button button-primary" href="../tools/qr-generator.html">
فتح مولد رمز QR
</a>
</p>

<h2>نصائح للطباعة</h2>
<ul>
<li>استخدم خلفية فاتحة ورمزًا داكنًا.</li>
<li>اترك مساحة فارغة حول الرمز.</li>
<li>لا تمدد الصورة بطريقة تشوه أبعادها.</li>
<li>اختبر النسخة المطبوعة قبل توزيعها.</li>
<li>ضع وصفًا مثل امسح الرمز للتواصل عبر واتساب.</li>
</ul>

<h2>هل يتغير رمز QR؟</h2>
<p>
الرمز الثابت يحتفظ بالرابط الذي أُنشئ منه. إذا غيرت رقم واتساب أو الرابط،
فستحتاج عادة إلى إنشاء رمز جديد وطباعة النسخة الجديدة.
</p>

<h2>الأسئلة الشائعة</h2>
<details>
<summary>هل يحتاج العميل إلى تطبيق خاص لمسح الرمز؟</summary>
<p>غالبية الهواتف الحديثة تستطيع قراءة رمز QR باستخدام تطبيق الكاميرا.</p>
</details>

<details>
<summary>هل يتم حفظ الرابط في الموقع؟</summary>
<p>لا، يتم إنشاء رمز QR داخل المتصفح دون تخزين الرابط في قاعدة بيانات.</p>
</details>
""",
    },

    "customer-service-whatsapp-templates.html": {
        "title": "قوالب رسائل خدمة العملاء عبر واتساب",
        "description": (
            "نماذج عملية لرسائل الترحيب وتأكيد الطلبات والمواعيد "
            "والتوصيل والمتابعة عبر واتساب."
        ),
        "heading": "قوالب رسائل خدمة العملاء عبر واتساب",
        "content": """
<p>
تساعد قوالب الرسائل على توحيد أسلوب التواصل وتسريع الرد، لكنها تحتاج إلى
تخصيص الاسم ورقم الطلب والموعد بما يناسب كل عميل.
</p>

<h2>رسالة ترحيب</h2>
<blockquote>
مرحبًا بك، شكرًا لتواصلك معنا. يسعدنا خدمتك، فضلاً وضح طلبك وسنرد عليك
في أقرب وقت ممكن.
</blockquote>

<h2>رسالة تأكيد طلب</h2>
<blockquote>
مرحبًا، تم استلام طلبك رقم 1254 بنجاح. سنرسل لك تحديثًا عند اكتمال التجهيز
وخروج الطلب للتوصيل.
</blockquote>

<h2>رسالة تأكيد موعد</h2>
<blockquote>
مرحبًا، تم تأكيد موعدك يوم الثلاثاء الساعة 5 مساءً. يرجى إبلاغنا مبكرًا
عند الحاجة إلى تعديل الموعد.
</blockquote>

<h2>رسالة خروج الطلب للتوصيل</h2>
<blockquote>
طلبك الآن مع مندوب التوصيل. يرجى التأكد من توفر الهاتف وإرسال وصف الموقع
عند الحاجة.
</blockquote>

<h2>رسالة متابعة بعد الخدمة</h2>
<blockquote>
شكرًا لاختيارك خدمتنا. نأمل أن تكون تجربتك مرضية، ويسعدنا استقبال ملاحظاتك.
</blockquote>

<h2>نصائح لاستخدام القوالب</h2>
<ul>
<li>راجع جميع البيانات قبل الإرسال.</li>
<li>اجعل الرسالة واضحة ومختصرة.</li>
<li>تجنب إرسال معلومات حساسة.</li>
<li>لا ترسل رسائل تسويقية دون موافقة العميل.</li>
<li>استخدم نبرة تتناسب مع هوية النشاط.</li>
</ul>

<p>
<a class="button button-primary" href="../tools/message-generator.html">
إنشاء رسالة أعمال
</a>
</p>

<h2>الأسئلة الشائعة</h2>
<details>
<summary>هل يجب استخدام اسم العميل؟</summary>
<p>استخدام الاسم يجعل الرسالة أكثر تخصيصًا، بشرط التأكد من كتابته صحيحًا.</p>
</details>

<details>
<summary>هل يمكن إرسال القالب كما هو؟</summary>
<p>يفضل مراجعته وتخصيصه وفق نوع النشاط وحالة العميل قبل الإرسال.</p>
</details>
""",
    },

    "clean-customer-phone-list.html": {
        "title": "طريقة تنظيف وتنسيق قائمة أرقام العملاء",
        "description": (
            "دليل لتنظيف قائمة أرقام العملاء وتوحيد الصيغة وإزالة "
            "المسافات والتكرار قبل استخدامها."
        ),
        "heading": "طريقة تنظيف وتنسيق قائمة أرقام العملاء",
        "content": """
<p>
تأتي قوائم الأرقام غالبًا من مصادر متعددة، مثل النماذج وملفات Excel
والمتاجر الإلكترونية، ولذلك قد تحتوي على مسافات أو شرطات أو صيغ مختلفة.
</p>

<h2>احتفظ بنسخة أصلية</h2>
<p>
قبل التنظيف، احتفظ بنسخة من الملف الأصلي. يتيح ذلك الرجوع إلى البيانات
إذا حُذف رقم بالخطأ أو احتاجت بعض السجلات إلى مراجعة يدوية.
</p>

<h2>ضع كل رقم في سطر مستقل</h2>
<p>
يساعد وضع كل رقم في سطر منفصل على معالجة القائمة بسهولة. احذف أسماء
العملاء والملاحظات من عمود الرقم، وضعها في أعمدة منفصلة.
</p>

<h2>توحيد الصيغة</h2>
<p>
حدد ما إذا كنت تحتاج إلى الصيغة المحلية أو الدولية. عند استخدام الرقم
السعودي في روابط واتساب، تكون الصيغة الدولية دون الصفر الأول هي الأنسب.
</p>

<h2>مراجعة الأرقام المرفوضة</h2>
<p>
لا تحذف الأرقام المرفوضة مباشرة. قد يكون الخطأ بسيطًا مثل نقص رقم أو وجود
رمز إضافي. راجعها يدويًا قبل اتخاذ القرار.
</p>

<h2>إزالة التكرار</h2>
<p>
بعد توحيد الصيغة، يصبح اكتشاف الأرقام المكررة أكثر دقة؛ فقد يظهر الرقم
نفسه مرة بالصيغة المحلية ومرة بالصيغة الدولية.
</p>

<p>
<a class="button button-primary" href="../tools/bulk-phone-formatter.html">
تنسيق قائمة أرقام
</a>
</p>

<h2>حماية بيانات العملاء</h2>
<ul>
<li>لا تشارك القائمة مع أشخاص غير مخولين.</li>
<li>استخدم البيانات فقط للغرض الذي جُمعت من أجله.</li>
<li>تجنب إرسال الرسائل المزعجة أو غير المطلوبة.</li>
<li>احذف النسخ غير الضرورية بعد انتهاء العمل.</li>
</ul>

<h2>الأسئلة الشائعة</h2>
<details>
<summary>هل التنسيق يثبت أن الرقم نشط؟</summary>
<p>لا، التنسيق يتحقق من الشكل العام ولا يؤكد أن الرقم نشط أو مسجل بواتساب.</p>
</details>

<details>
<summary>لماذا يجب توحيد الصيغة قبل إزالة التكرار؟</summary>
<p>
لأن الرقم نفسه قد يظهر بأكثر من شكل، وتوحيد الصيغة يساعد على اكتشافه.
</p>
</details>
""",
    },
}


STYLE = """
<style>
.article-page {
    max-width: 880px;
    margin: 40px auto;
    padding: 32px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    line-height: 1.95;
}

.article-page h1 {
    margin-bottom: 18px;
}

.article-page h2 {
    margin-top: 34px;
    margin-bottom: 12px;
}

.article-page p,
.article-page li {
    color: var(--text-muted);
}

.article-page ol,
.article-page ul {
    padding-right: 25px;
}

.article-page blockquote {
    margin: 18px 0;
    padding: 18px;
    border-right: 4px solid var(--primary);
    border-radius: 10px;
    background: var(--primary-light);
}

.article-page details {
    margin-top: 12px;
    border: 1px solid var(--border);
    border-radius: 10px;
}

.article-page summary {
    padding: 14px;
    cursor: pointer;
    font-weight: 800;
}

.article-page details p {
    padding: 0 14px 14px;
}

@media (max-width: 600px) {
    .article-page {
        padding: 22px;
        margin-top: 20px;
    }
}
</style>
"""


def create_page(filename: str, guide: dict[str, str]) -> None:
    url = f"{BASE_URL}/guides/{filename}"
    title = guide["title"]
    description = guide["description"]

    structured_data = f"""
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{escape(title)}",
  "description": "{escape(description)}",
  "url": "{url}",
  "mainEntityOfPage": "{url}",
  "inLanguage": "ar",
  "author": {{
    "@type": "Organization",
    "name": "{SITE_NAME}"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "{SITE_NAME}",
    "url": "{BASE_URL}/"
  }}
}}
""".strip()

    document = f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>{escape(title)} | {SITE_NAME}</title>
    <meta name="description" content="{escape(description)}">
    <meta name="theme-color" content="#128c7e">

    <link rel="canonical" href="{url}">
    <link rel="icon" href="../favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="../assets/css/style.css">

    <meta property="og:locale" content="ar_SA">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="{SITE_NAME}">
    <meta property="og:title" content="{escape(title)}">
    <meta property="og:description" content="{escape(description)}">
    <meta property="og:url" content="{url}">

    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{escape(title)}">
    <meta name="twitter:description" content="{escape(description)}">

    <script type="application/ld+json">{structured_data}</script>
    {STYLE}
</head>

<body>
<header class="site-header">
    <div class="container header-content">
        <a class="logo" href="../index.html">
            <span class="logo-mark">و</span>
            <span>{SITE_NAME}</span>
        </a>

        <nav class="main-nav" aria-label="التنقل الرئيسي">
            <a href="../index.html">الرئيسية</a>
            <a href="../index.html#tools">الأدوات</a>
            <a href="../index.html#guides">الأدلة</a>
            <a href="../about.html">من نحن</a>
        </nav>
    </div>
</header>

<main class="container">
    <article class="article-page">
        <p><a href="../index.html">الرئيسية</a> ← الأدلة</p>
        <h1>{escape(guide["heading"])}</h1>
        <p>{escape(description)}</p>

        {guide["content"]}
    </article>
</main>

<footer class="site-footer">
    <div class="container">
        <p>© 2026 {SITE_NAME}</p>
        <p>
            <a href="../privacy.html">الخصوصية</a> ·
            <a href="../terms.html">الشروط</a> ·
            <a href="../contact.html">التواصل</a>
        </p>
    </div>
</footer>

<script src="../assets/js/common.js" defer></script>
</body>
</html>
"""

    path = ROOT / "guides" / filename
    path.write_text(document, encoding="utf-8", newline="\n")
    print(f"CREATED: guides/{filename}")


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    document = path.read_text(encoding="utf-8-sig")

    additions = []

    for filename in GUIDES:
        url = f"{BASE_URL}/guides/{filename}"

        if url in document:
            continue

        additions.append(
            f"""  <url>
    <loc>{url}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>"""
        )

    if additions:
        block = "\n" + "\n".join(additions) + "\n"
        document = re.sub(
            r"</urlset>\s*$",
            block + "</urlset>\n",
            document,
        )
        path.write_text(document, encoding="utf-8", newline="\n")

    print(f"SITEMAP: added {len(additions)} URLs")


def main() -> None:
    for filename, guide in GUIDES.items():
        create_page(filename, guide)

    update_sitemap()
    print("\nNew guides created successfully.")


if __name__ == "__main__":
    main()