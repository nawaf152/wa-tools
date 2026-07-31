<?php
declare(strict_types=1);

session_start();

header('Content-Type: text/html; charset=UTF-8');

const CONTACT_RECIPIENT = 'info@halaktech.com';
const SITE_NAME = 'أدوات واتساب العربية';
const SITE_URL = 'https://ramfqconnect.shop';
const MIN_SUBMIT_SECONDS = 3;
const MAX_MESSAGE_LENGTH = 5000;

function redirectWithStatus(string $status): never
{
    header(
        'Location: ' . SITE_URL .
        '/contact.html?status=' . rawurlencode($status)
    );
    exit;
}

function cleanSingleLine(string $value): string
{
    $value = trim($value);
    $value = str_replace(["\r", "\n"], ' ', $value);

    return preg_replace('/\s+/u', ' ', $value) ?? '';
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    redirectWithStatus('invalid_request');
}

$honeypot = trim((string) ($_POST['website'] ?? ''));

if ($honeypot !== '') {
    redirectWithStatus('success');
}

$startedAt = (int) ($_POST['started_at'] ?? 0);

if ($startedAt <= 0 || (time() - $startedAt) < MIN_SUBMIT_SECONDS) {
    redirectWithStatus('too_fast');
}

$name = cleanSingleLine((string) ($_POST['name'] ?? ''));
$email = cleanSingleLine((string) ($_POST['email'] ?? ''));
$requestType = cleanSingleLine(
    (string) ($_POST['request_type'] ?? '')
);
$subject = cleanSingleLine((string) ($_POST['subject'] ?? ''));
$message = trim((string) ($_POST['message'] ?? ''));

$allowedRequestTypes = [
    'الإبلاغ عن خطأ',
    'اقتراح أداة',
    'مشكلة تقنية',
    'استفسار عام',
    'استفسار عن الخصوصية',
];

if (
    mb_strlen($name) < 2 ||
    mb_strlen($name) > 100
) {
    redirectWithStatus('invalid_name');
}

if (
    !filter_var($email, FILTER_VALIDATE_EMAIL) ||
    mb_strlen($email) > 190
) {
    redirectWithStatus('invalid_email');
}

if (!in_array($requestType, $allowedRequestTypes, true)) {
    redirectWithStatus('invalid_type');
}

if (
    mb_strlen($subject) < 3 ||
    mb_strlen($subject) > 150
) {
    redirectWithStatus('invalid_subject');
}

$messageLength = mb_strlen($message);

if (
    $messageLength < 15 ||
    $messageLength > MAX_MESSAGE_LENGTH
) {
    redirectWithStatus('invalid_message');
}

$ipAddress = $_SERVER['REMOTE_ADDR'] ?? 'غير متاح';
$userAgent = cleanSingleLine(
    (string) ($_SERVER['HTTP_USER_AGENT'] ?? 'غير متاح')
);

$mailSubject = sprintf(
    '[%s] %s: %s',
    SITE_NAME,
    $requestType,
    $subject
);

$mailBody = implode(PHP_EOL, [
    'رسالة جديدة من نموذج التواصل',
    '--------------------------------',
    'الاسم: ' . $name,
    'البريد الإلكتروني: ' . $email,
    'نوع الطلب: ' . $requestType,
    'العنوان: ' . $subject,
    '',
    'نص الرسالة:',
    $message,
    '',
    '--------------------------------',
    'عنوان IP: ' . $ipAddress,
    'المتصفح: ' . $userAgent,
    'التاريخ: ' . date('Y-m-d H:i:s'),
]);

$headers = [
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'From: ' . SITE_NAME . ' <no-reply@ramfqconnect.shop>',
    'Reply-To: ' . $name . ' <' . $email . '>',
    'X-Mailer: PHP/' . PHP_VERSION,
];

$sent = mail(
    CONTACT_RECIPIENT,
    '=?UTF-8?B?' . base64_encode($mailSubject) . '?=',
    $mailBody,
    implode("\r\n", $headers)
);

redirectWithStatus($sent ? 'success' : 'send_failed');