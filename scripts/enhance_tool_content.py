from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


TOOL_CONTENT = {
    "tools/whatsapp-link.html": """
<section class="content-section tool-guide" aria-labelledby="guide-title">
    <h2 id="guide-title">ما هو رابط واتساب المباشر؟</h2>

    <p>
        رابط واتساب المباشر هو عنوان إلكتروني يفتح محادثة مع رقم محدد دون
        الحاجة إلى حفظ الرقم في جهات الاتصال أولًا. يمكن أيضًا تضمين رسالة
        جاهزة داخل الرابط لتظهر تلقائيًا في مربع الكتابة عند فتح المحادثة.
    </p>

    <p>
        يفيد هذا النوع من الروابط المتاجر ومقدمي الخدمات وأصحاب الحسابات
        التجارية، لأنه يقلل عدد الخطوات التي يحتاجها العميل للوصول إلى
        المحادثة وإرسال استفساره.
    </p>

    <h2>طريقة استخدام مولد رابط واتساب</h2>

    <ol>
        <li>اختر رمز الدولة المناسب من القائمة.</li>
        <li>اكتب رقم الجوال دون مسافات أو رموز إضافية.</li>
        <li>أضف رسالة افتتاحية اختيارية.</li>
        <li>اضغط زر إنشاء الرابط.</li>
        <li>انسخ الرابط أو افتحه للتأكد من صحته.</li>
    </ol>

    <h2>مثال عملي</h2>

    <p>
        عند إدخال رقم سعودي مثل <strong>0551234567</strong> ورسالة مثل
        <strong>السلام عليكم، أرغب في معرفة تفاصيل الخدمة</strong>، تنشئ
        الأداة رابطًا يفتح محادثة مباشرة مع الرقم بعد تحويله إلى الصيغة
        الدولية الصحيحة.
    </p>

    <h2>أين يمكن استخدام الرابط؟</h2>

    <ul>
        <li>في الملف التعريفي على إنستغرام أو تيك توك.</li>
        <li>داخل موقع إلكتروني أو صفحة هبوط.</li>
        <li>في الحملات الإعلانية والرسائل النصية.</li>
        <li>على الفواتير والعروض وبطاقات العمل.</li>
        <li>داخل رمز QR مطبوع في المتجر.</li>
    </ul>

    <h2>أخطاء شائعة</h2>

    <p>
        أكثر الأخطاء شيوعًا هي كتابة الرقم بصفر البداية بعد رمز الدولة،
        أو إدخال شرطات ومسافات غير لازمة، أو استخدام رقم غير مرتبط بحساب
        واتساب. الأداة تنظف الرقم قدر الإمكان، لكن يفضل دائمًا اختبار الرابط
        قبل مشاركته مع العملاء.
    </p>

    <h2>الأسئلة الشائعة</h2>

    <details>
        <summary>هل يجب حفظ الرقم في جهات الاتصال؟</summary>
        <p>لا، الرابط يفتح المحادثة مباشرة دون حفظ الرقم.</p>
    </details>

    <details>
        <summary>هل يتم إرسال الرسالة تلقائيًا؟</summary>
        <p>
            لا. تظهر الرسالة في مربع الكتابة، ويجب على المستخدم الضغط على
            زر الإرسال بنفسه.
        </p>
    </details>

    <details>
        <summary>هل تخزن الأداة الرقم أو الرسالة؟</summary>
        <p>
            لا، تتم المعالجة داخل المتصفح ولا يرسل الموقع البيانات إلى
            قاعدة بيانات.
        </p>
    </details>
</section>
""",

    "tools/saudi-phone-formatter.html": """
<section class="content-section tool-guide" aria-labelledby="guide-title">
    <h2 id="guide-title">لماذا يحتاج الرقم السعودي إلى تنسيق؟</h2>

    <p>
        قد يُكتب رقم الجوال السعودي بصيغ مختلفة، مثل الصيغة المحلية التي
        تبدأ بـ05 أو الصيغة الدولية التي تبدأ بـ966. كثير من الأنظمة وروابط
        واتساب تحتاج الرقم بصيغة دولية موحدة دون الصفر الأول.
    </p>

    <h2>الصيغة الصحيحة للرقم السعودي</h2>

    <p>
        الرقم المحلي مثل <strong>0551234567</strong> يتحول عادة إلى
        <strong>966551234567</strong>. يتم حذف الصفر الأول وإضافة رمز
        المملكة العربية السعودية 966.
    </p>

    <h2>طريقة استخدام الأداة</h2>

    <ol>
        <li>اكتب رقم الجوال في الحقل المخصص.</li>
        <li>اضغط زر التنسيق.</li>
        <li>راجع الصيغة المحلية والدولية الناتجة.</li>
        <li>انسخ الصيغة المناسبة لاستخدامك.</li>
    </ol>

    <h2>متى تحتاج الصيغة الدولية؟</h2>

    <ul>
        <li>عند إنشاء رابط واتساب مباشر.</li>
        <li>عند استيراد العملاء إلى نظام إدارة علاقات العملاء.</li>
        <li>عند تجهيز قوائم اتصال أو رسائل.</li>
        <li>عند إدخال الرقم في منصات دولية.</li>
    </ul>

    <h2>أخطاء شائعة</h2>

    <p>
        من الأخطاء المتكررة كتابة الرقم بالشكل
        <strong>9660551234567</strong>. هذه الصيغة غير صحيحة لأن الصفر
        المحلي يجب حذفه بعد إضافة رمز الدولة.
    </p>

    <h2>الأسئلة الشائعة</h2>

    <details>
        <summary>هل تقبل الأداة المسافات والشرطات؟</summary>
        <p>
            نعم، تحاول الأداة إزالة الرموز غير الضرورية قبل التحقق من الرقم.
        </p>
    </details>

    <details>
        <summary>هل تتحقق الأداة من أن الرقم يعمل فعلًا؟</summary>
        <p>
            لا، الأداة تتحقق من الصيغة فقط ولا تستطيع معرفة ما إذا كان الرقم
            نشطًا أو مسجلًا في واتساب.
        </p>
    </details>

    <details>
        <summary>هل يمكن استخدام الناتج في واتساب؟</summary>
        <p>
            نعم، الصيغة الدولية مناسبة عادة لإنشاء روابط واتساب المباشرة.
        </p>
    </details>
</section>
""",

    "tools/bulk-phone-formatter.html": """
<section class="content-section tool-guide" aria-labelledby="guide-title">
    <h2 id="guide-title">ما فائدة تنسيق قائمة أرقام دفعة واحدة؟</h2>

    <p>
        عند جمع أرقام العملاء من نماذج أو ملفات مختلفة، تكون الصيغ غالبًا
        غير موحدة. قد تتضمن بعض الأرقام مسافات أو شرطات أو رمز الدولة، بينما
        تبدأ أرقام أخرى بصفر محلي. تساعد هذه الأداة على تنظيف القائمة وتحويل
        الأرقام إلى صيغة موحدة.
    </p>

    <h2>طريقة الاستخدام</h2>

    <ol>
        <li>الصق الأرقام، بحيث يكون كل رقم في سطر مستقل.</li>
        <li>اختر صيغة الإخراج المناسبة.</li>
        <li>اضغط زر التنسيق.</li>
        <li>راجع الأرقام الصحيحة وغير الصحيحة.</li>
        <li>انسخ النتيجة أو نزّل الملف.</li>
    </ol>

    <h2>مثال على قائمة قبل التنسيق</h2>

    <pre><code>0551234567
+966 56 987 6543
053-111-2233
966501234567</code></pre>

    <p>
        بعد التنسيق، تصبح الأرقام في صورة موحدة وأسهل للاستخدام في ملفات
        العملاء أو الأنظمة الداخلية.
    </p>

    <h2>نصائح لجودة البيانات</h2>

    <ul>
        <li>احذف الملاحظات النصية الموجودة بجانب الأرقام.</li>
        <li>ضع كل رقم في سطر مستقل.</li>
        <li>راجع الأرقام المرفوضة قبل حذفها.</li>
        <li>احتفظ بنسخة من الملف الأصلي قبل إجراء أي تعديل.</li>
    </ul>

    <h2>الخصوصية</h2>

    <p>
        تتم معالجة القائمة داخل المتصفح. مع ذلك، لا تستخدم قوائم العملاء
        إلا للأغراض التي وافقوا عليها، والتزم بالأنظمة المتعلقة بالخصوصية
        والرسائل التسويقية.
    </p>

    <h2>الأسئلة الشائعة</h2>

    <details>
        <summary>كم رقمًا يمكنني تنسيقه؟</summary>
        <p>
            يعتمد ذلك على قدرة الجهاز والمتصفح، لكن القوائم المعتادة تعمل
            بسرعة لأن المعالجة محلية.
        </p>
    </details>

    <details>
        <summary>هل يتم حذف الأرقام المكررة؟</summary>
        <p>
            يعتمد ذلك على إعدادات الأداة الحالية. راجع النتيجة قبل التنزيل
            للتأكد من القائمة النهائية.
        </p>
    </details>

    <details>
        <summary>هل يتم إرسال القائمة إلى الخادم؟</summary>
        <p>لا، تتم المعالجة داخل متصفحك.</p>
    </details>
</section>
""",

    "tools/qr-generator.html": """
<section class="content-section tool-guide" aria-labelledby="guide-title">
    <h2 id="guide-title">ما هو رمز QR؟</h2>

    <p>
        رمز QR هو رمز بصري يمكن مسحه بكاميرا الهاتف لفتح رابط أو عرض نص.
        يستخدم في المتاجر والمطاعم وبطاقات العمل والإعلانات المطبوعة لأنه
        يختصر كتابة الروابط الطويلة.
    </p>

    <h2>طريقة إنشاء رمز QR</h2>

    <ol>
        <li>الصق الرابط أو النص في الحقل.</li>
        <li>اختر الحجم المناسب.</li>
        <li>اضغط زر إنشاء الرمز.</li>
        <li>اختبر الرمز بكاميرا هاتف مختلف.</li>
        <li>نزّل الصورة واستخدمها في التصميم.</li>
    </ol>

    <h2>استخدامات عملية</h2>

    <ul>
        <li>فتح محادثة واتساب مباشرة.</li>
        <li>إرسال العميل إلى صفحة متجر أو منتج.</li>
        <li>عرض قائمة الطعام الرقمية.</li>
        <li>مشاركة موقع أو نموذج حجز.</li>
        <li>إضافة رابط إلى بطاقة عمل مطبوعة.</li>
    </ul>

    <h2>نصائح للطباعة</h2>

    <p>
        اترك مساحة بيضاء حول الرمز، ولا تصغره بدرجة كبيرة. تجنب وضعه فوق
        خلفية مزدحمة أو منخفضة التباين، واختبر النسخة المطبوعة قبل توزيعها.
    </p>

    <h2>الأسئلة الشائعة</h2>

    <details>
        <summary>هل تنتهي صلاحية رمز QR؟</summary>
        <p>
            الرمز نفسه لا تنتهي صلاحيته، لكن سيتوقف عن العمل إذا تغير الرابط
            الذي يشير إليه أو تم حذفه.
        </p>
    </details>

    <details>
        <summary>هل يمكن إنشاء رمز QR لرابط واتساب؟</summary>
        <p>
            نعم، أنشئ رابط واتساب أولًا ثم الصقه في هذه الأداة.
        </p>
    </details>

    <details>
        <summary>هل يتم رفع الرمز أو الرابط إلى الخادم؟</summary>
        <p>
            لا، يتم إنشاء الرمز داخل المتصفح باستخدام مكتبة محلية.
        </p>
    </details>
</section>
""",

    "tools/message-generator.html": """
<section class="content-section tool-guide" aria-labelledby="guide-title">
    <h2 id="guide-title">لماذا تستخدم قوالب رسائل الأعمال؟</h2>

    <p>
        تساعد القوالب على الرد بسرعة وبأسلوب ثابت وواضح. وهي مفيدة للمتاجر
        والعيادات ومقدمي الخدمات عند إرسال تأكيدات الطلبات والمواعيد
        والتنبيهات ورسائل المتابعة.
    </p>

    <h2>طريقة استخدام مولد الرسائل</h2>

    <ol>
        <li>اختر نوع الرسالة المناسب.</li>
        <li>أدخل اسم العميل أو رقم الطلب والبيانات المطلوبة.</li>
        <li>راجع النص الناتج وعدله بما يناسب نشاطك.</li>
        <li>انسخ الرسالة وأرسلها عبر واتساب.</li>
    </ol>

    <h2>صفات الرسالة الجيدة</h2>

    <ul>
        <li>تبدأ بتحية مناسبة.</li>
        <li>توضح الغرض من الرسالة مباشرة.</li>
        <li>تتضمن البيانات المهمة مثل الموعد أو رقم الطلب.</li>
        <li>تقدم خطوة تالية واضحة للعميل.</li>
        <li>تتجنب الإطالة والعبارات المبهمة.</li>
    </ul>

    <h2>مثال لرسالة تأكيد طلب</h2>

    <blockquote>
        مرحبًا، تم استلام طلبك رقم 1254 بنجاح، وسيتم تجهيز الطلب خلال يومي
        عمل. سنرسل لك تحديثًا فور خروجه للتوصيل.
    </blockquote>

    <h2>نصائح قبل الإرسال</h2>

    <p>
        راجع الاسم والموعد والمبلغ ورقم الطلب. تجنب إرسال معلومات حساسة،
        ولا ترسل رسائل تسويقية متكررة إلى أشخاص لم يوافقوا على استقبالها.
    </p>

    <h2>الأسئلة الشائعة</h2>

    <details>
        <summary>هل يمكن تعديل الرسالة الناتجة؟</summary>
        <p>نعم، الرسالة مجرد قالب ويمكنك تعديلها قبل النسخ.</p>
    </details>

    <details>
        <summary>هل تحفظ الأداة أسماء العملاء؟</summary>
        <p>لا، تتم صياغة الرسالة داخل المتصفح ولا يتم تخزين البيانات.</p>
    </details>

    <details>
        <summary>هل القوالب مناسبة لكل الأنشطة؟</summary>
        <p>
            هي نقطة بداية عامة، ويجب تعديلها لتناسب سياسة نشاطك ونبرة
            التواصل مع عملائك.
        </p>
    </details>
</section>
""",
}


STYLE_BLOCK = """
<style id="tool-content-style">
    .tool-guide {
        max-width: 860px;
        margin: 42px auto 0;
        padding: 30px;
        border: 1px solid var(--border);
        border-radius: var(--radius);
        background: var(--surface);
        box-shadow: var(--shadow);
        line-height: 1.9;
    }

    .tool-guide h2 {
        margin-top: 34px;
        margin-bottom: 12px;
        font-size: 1.45rem;
    }

    .tool-guide h2:first-child {
        margin-top: 0;
    }

    .tool-guide p,
    .tool-guide li {
        color: var(--text-muted);
    }

    .tool-guide ol,
    .tool-guide ul {
        padding-right: 24px;
    }

    .tool-guide pre {
        overflow-x: auto;
        padding: 18px;
        border-radius: 12px;
        background: #102a26;
        color: #fff;
        direction: ltr;
        text-align: left;
    }

    .tool-guide blockquote {
        margin: 20px 0;
        padding: 18px;
        border-right: 4px solid var(--primary);
        border-radius: 10px;
        background: var(--primary-light);
    }

    .tool-guide details {
        margin-top: 12px;
        border: 1px solid var(--border);
        border-radius: 10px;
        background: #fff;
    }

    .tool-guide summary {
        padding: 14px 16px;
        cursor: pointer;
        font-weight: 800;
    }

    .tool-guide details p {
        margin: 0;
        padding: 0 16px 16px;
    }

    .ad-slot {
        min-height: 110px;
        margin: 32px auto;
        display: grid;
        place-items: center;
        border: 1px dashed var(--border);
        border-radius: 12px;
        color: var(--text-muted);
        background: #fafafa;
        font-size: 0.9rem;
    }

    @media (max-width: 600px) {
        .tool-guide {
            padding: 22px;
        }
    }
</style>
"""


AD_PLACEHOLDER = """
<div class="ad-slot" aria-label="مساحة إعلانية مستقبلية">
    مساحة مخصصة لإعلان مستقبلي
</div>
"""


def update_page(relative_path: str, content: str) -> None:
    path = ROOT / relative_path

    if not path.exists():
        print(f"SKIP: {relative_path}")
        return

    document = path.read_text(encoding="utf-8-sig")

    document = re.sub(
        r"\s*<!-- TOOL-CONTENT-START -->.*?<!-- TOOL-CONTENT-END -->\s*",
        "\n",
        document,
        flags=re.DOTALL | re.IGNORECASE,
    )

    if 'id="tool-content-style"' not in document:
        document = document.replace(
            "</head>",
            STYLE_BLOCK + "\n</head>",
            1,
        )

    enhanced_content = (
        "\n<!-- TOOL-CONTENT-START -->\n"
        + AD_PLACEHOLDER
        + content
        + "\n<!-- TOOL-CONTENT-END -->\n"
    )

    if "</main>" not in document:
        raise RuntimeError(f"Missing </main> in {relative_path}")

    document = document.replace(
        "</main>",
        enhanced_content + "\n</main>",
        1,
    )

    path.write_text(document, encoding="utf-8", newline="\n")
    print(f"UPDATED: {relative_path}")


def main() -> None:
    for relative_path, content in TOOL_CONTENT.items():
        update_page(relative_path, content)

    print("\nTool content enhancement completed.")


if __name__ == "__main__":
    main()