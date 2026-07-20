from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


GUIDE_CONTENT = {
    "guides/create-whatsapp-link.html": """
<section class="content-section article-extra">
    <h2>متى يكون رابط واتساب المباشر مفيدًا؟</h2>
    <p>
        يكون الرابط مفيدًا عندما تريد تقليل الخطوات بين العميل والمحادثة.
        بدل أن ينسخ العميل الرقم ويحفظه ثم يبحث عنه داخل واتساب، يستطيع فتح
        المحادثة مباشرة من زر أو رابط واحد.
    </p>

    <h2>الصيغة الأساسية للرابط</h2>
    <p>
        يعتمد الرابط على كتابة الرقم بصيغته الدولية دون علامة زائد أو مسافات.
        بالنسبة للرقم السعودي، يجب حذف الصفر الأول وإضافة رمز الدولة 966.
    </p>

    <h2>إضافة رسالة جاهزة</h2>
    <p>
        يمكن تضمين رسالة افتتاحية داخل الرابط، مثل طلب تفاصيل خدمة أو حجز
        موعد. تظهر الرسالة داخل مربع الكتابة، لكنها لا تُرسل تلقائيًا.
    </p>

    <h2>أفضل ممارسات الاستخدام</h2>
    <ul>
        <li>اختبر الرابط من هاتف مختلف قبل نشره.</li>
        <li>اجعل الرسالة قصيرة وواضحة.</li>
        <li>تجنب وضع بيانات حساسة داخل الرسالة الجاهزة.</li>
        <li>استخدم وصفًا واضحًا للزر مثل تواصل معنا عبر واتساب.</li>
    </ul>

    <h2>أخطاء يجب تجنبها</h2>
    <ul>
        <li>إبقاء الصفر المحلي بعد رمز الدولة.</li>
        <li>كتابة الرقم مع شرطات أو أقواس.</li>
        <li>استخدام رقم غير مرتبط بحساب واتساب.</li>
        <li>مشاركة الرابط قبل اختباره.</li>
    </ul>

    <h2>الأسئلة الشائعة</h2>
    <details>
        <summary>هل يعمل الرابط على الجوال والكمبيوتر؟</summary>
        <p>
            نعم، يفتح تطبيق واتساب على الجوال أو واتساب ويب على الكمبيوتر
            حسب الجهاز وإعداداته.
        </p>
    </details>

    <details>
        <summary>هل يمكن تغيير الرسالة لاحقًا؟</summary>
        <p>
            نعم، يمكنك إنشاء رابط جديد برسالة مختلفة في أي وقت.
        </p>
    </details>
</section>
""",

    "guides/saudi-phone-number-format.html": """
<section class="content-section article-extra">
    <h2>الفرق بين الصيغة المحلية والدولية</h2>
    <p>
        تبدأ الصيغة المحلية عادة بالصفر، مثل 0551234567، بينما تبدأ الصيغة
        الدولية برمز الدولة 966 دون الصفر الأول، مثل 966551234567.
    </p>

    <h2>لماذا تختلف الأنظمة في قبول الأرقام؟</h2>
    <p>
        بعض الأنظمة المحلية تقبل الصيغة التي تبدأ بـ05، بينما تعتمد الأنظمة
        العالمية وروابط واتساب غالبًا على الصيغة الدولية الموحدة.
    </p>

    <h2>أمثلة صحيحة وغير صحيحة</h2>
    <ul>
        <li>صحيح محليًا: 0551234567</li>
        <li>صحيح دوليًا: 966551234567</li>
        <li>غير صحيح: 9660551234567</li>
        <li>غير مفضل: +966 55 123 4567 عند الأنظمة التي تقبل أرقامًا فقط</li>
    </ul>

    <h2>نصائح عند تجهيز قوائم العملاء</h2>
    <ul>
        <li>استخدم صيغة واحدة لجميع الأرقام.</li>
        <li>احذف المسافات والشرطات.</li>
        <li>راجع الأرقام القصيرة أو الطويلة بشكل غير طبيعي.</li>
        <li>احتفظ بنسخة أصلية قبل التنظيف.</li>
    </ul>

    <h2>الأسئلة الشائعة</h2>
    <details>
        <summary>هل علامة + ضرورية؟</summary>
        <p>
            تعتمد على النظام المستخدم. روابط واتساب تقبل الرقم الدولي دون
            علامة زائد داخل الرابط.
        </p>
    </details>

    <details>
        <summary>هل يمكن معرفة أن الرقم نشط؟</summary>
        <p>
            تنسيق الرقم لا يثبت أنه نشط أو مسجل في واتساب؛ هو فقط يوحد الصيغة.
        </p>
    </details>
</section>
""",

    "guides/whatsapp-business-messages.html": """
<section class="content-section article-extra">
    <h2>أهم أنواع رسائل الأعمال</h2>
    <ul>
        <li>رسائل الترحيب.</li>
        <li>تأكيد الطلبات.</li>
        <li>تأكيد المواعيد.</li>
        <li>إشعارات الشحن والتوصيل.</li>
        <li>رسائل المتابعة بعد تقديم الخدمة.</li>
    </ul>

    <h2>كيف تكتب رسالة واضحة؟</h2>
    <p>
        ابدأ بتحية مناسبة، ثم وضح سبب الرسالة مباشرة. أضف المعلومات الضرورية
        فقط، مثل رقم الطلب أو الموعد، واختم بخطوة واضحة يتوقع تنفيذها من العميل.
    </p>

    <h2>نبرة الرسالة</h2>
    <p>
        استخدم لغة محترمة وبسيطة تناسب جمهورك. تجنب العبارات المبالغ فيها
        والضغط على العميل، وابتعد عن إرسال رسائل متكررة دون موافقة.
    </p>

    <h2>مثال لتأكيد موعد</h2>
    <blockquote>
        مرحبًا، نذكرك بموعدك غدًا الساعة 5 مساءً. نرجو تأكيد الحضور أو طلب
        تعديل الموعد قبل ساعتين على الأقل.
    </blockquote>

    <h2>أخطاء شائعة</h2>
    <ul>
        <li>نسيان اسم العميل أو رقم الطلب.</li>
        <li>إرسال معلومات غير دقيقة.</li>
        <li>استخدام رسالة طويلة جدًا.</li>
        <li>إرسال الرسائل التسويقية دون موافقة.</li>
    </ul>

    <h2>الأسئلة الشائعة</h2>
    <details>
        <summary>هل الأفضل استخدام رسالة قصيرة؟</summary>
        <p>
            نعم، الرسائل القصيرة والواضحة أسهل قراءة، خصوصًا على الهاتف.
        </p>
    </details>

    <details>
        <summary>هل يمكن استخدام نفس القالب لجميع العملاء؟</summary>
        <p>
            يمكن استخدام قالب أساسي، لكن يفضل تخصيص الاسم والطلب أو الموعد.
        </p>
    </details>
</section>
""",
}


STYLE = """
<style id="article-extra-style">
    .article-extra {
        max-width: 860px;
        margin: 40px auto 0;
        padding: 30px;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        line-height: 1.9;
    }

    .article-extra h2 {
        margin-top: 32px;
        margin-bottom: 12px;
        font-size: 1.45rem;
    }

    .article-extra h2:first-child {
        margin-top: 0;
    }

    .article-extra p,
    .article-extra li {
        color: var(--text-muted);
    }

    .article-extra ul {
        padding-right: 24px;
    }

    .article-extra blockquote {
        margin: 20px 0;
        padding: 18px;
        border-right: 4px solid var(--primary);
        border-radius: 10px;
        background: var(--primary-light);
    }

    .article-extra details {
        margin-top: 12px;
        border: 1px solid var(--border);
        border-radius: 10px;
        background: #fff;
    }

    .article-extra summary {
        padding: 14px 16px;
        cursor: pointer;
        font-weight: 800;
    }

    .article-extra details p {
        margin: 0;
        padding: 0 16px 16px;
    }

    @media (max-width: 600px) {
        .article-extra {
            padding: 22px;
        }
    }
</style>
"""


def update_page(relative_path: str, extra_content: str) -> None:
    path = ROOT / relative_path
    document = path.read_text(encoding="utf-8-sig")

    document = re.sub(
        r"\s*<!-- ARTICLE-EXTRA-START -->.*?<!-- ARTICLE-EXTRA-END -->\s*",
        "\n",
        document,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if 'id="article-extra-style"' not in document:
        document = document.replace("</head>", STYLE + "\n</head>", 1)

    block = (
        "\n<!-- ARTICLE-EXTRA-START -->\n"
        + extra_content
        + "\n<!-- ARTICLE-EXTRA-END -->\n"
    )

    document = document.replace("</main>", block + "\n</main>", 1)
    path.write_text(document, encoding="utf-8", newline="\n")

    print(f"UPDATED: {relative_path}")


def main() -> None:
    for relative_path, content in GUIDE_CONTENT.items():
        update_page(relative_path, content)

    print("\nGuide enhancement completed.")


if __name__ == "__main__":
    main()