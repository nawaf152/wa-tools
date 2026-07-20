"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const menuButton = document.querySelector("[data-menu-button]");
    const mainNav = document.querySelector("[data-main-nav]");
    const yearElements = document.querySelectorAll("[data-current-year]");

    yearElements.forEach((element) => {
        element.textContent = new Date().getFullYear();
    });

    if (menuButton && mainNav) {
        menuButton.addEventListener("click", () => {
            const isOpen = mainNav.classList.toggle("is-open");
            menuButton.setAttribute("aria-expanded", String(isOpen));
        });
    }
});

async function copyText(text, button = null) {
    try {
        await navigator.clipboard.writeText(text);

        if (button) {
            const oldText = button.textContent;
            button.textContent = "تم النسخ";

            setTimeout(() => {
                button.textContent = oldText;
            }, 1600);
        }

        return true;
    } catch (error) {
        console.error("تعذر نسخ النص:", error);
        return false;
    }
}

function convertArabicDigits(value) {
    const arabicDigits = "٠١٢٣٤٥٦٧٨٩";
    const persianDigits = "۰۱۲۳۴۵۶۷۸۹";

    return String(value)
        .replace(/[٠-٩]/g, (digit) => arabicDigits.indexOf(digit))
        .replace(/[۰-۹]/g, (digit) => persianDigits.indexOf(digit));
}

function sanitizePhoneCharacters(value) {
    return convertArabicDigits(value).replace(/[^\d+]/g, "");
}