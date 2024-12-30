const translations = {
    zh: {
        'password_login': '密码登录',
        'qrcode_login': '二维码登录',
        'phone_placeholder': '请输入手机号码',
        'password_placeholder': '请输入密码',
        'verification_placeholder': '验证码',
        'remember_me': '记住我',
        'forgot_password': '忘记密码？',
        'login_button': '登录',
        'register': '注册',
        'other_login_methods': '其他登录方式',
        'scan_tip': '请使用APP扫码登录',
        'refresh_qrcode': '刷新二维码',
        'qr_scanned': '已扫描，请在手机上确认',
        'qr_expired': '二维码已过期，请点击刷新',
        'login_success': '登录成功',
        'login_failed': '登录失败，请稍后重试',
        'server_error': '服务器错误',
        'invalid_captcha': '验证码错误或已过期',
        'invalid_credentials': '手机号或密码错误'
    },
    en: {
        'password_login': 'Password Login',
        'qrcode_login': 'QR Code Login',
        'phone_placeholder': 'Enter phone number',
        'password_placeholder': 'Enter password',
        'verification_placeholder': 'Verification code',
        'remember_me': 'Remember me',
        'forgot_password': 'Forgot password?',
        'login_button': 'Login',
        'register': 'Register',
        'other_login_methods': 'Other login methods',
        'scan_tip': 'Scan with APP to login',
        'refresh_qrcode': 'Refresh QR Code',
        'qr_scanned': 'Scanned, please confirm on your phone',
        'qr_expired': 'QR code expired, click to refresh',
        'login_success': 'Login successful',
        'login_failed': 'Login failed, please try again',
        'server_error': 'Server error',
        'invalid_captcha': 'Invalid or expired verification code',
        'invalid_credentials': 'Invalid phone number or password'
    },
    ja: {
        'password_login': 'パスワードログイン',
        'qrcode_login': 'QRコードログイン',
        'phone_placeholder': '電話番号を入力',
        'password_placeholder': 'パスワードを入力',
        'verification_placeholder': '認証コード',
        'remember_me': 'ログイン状態を保持',
        'forgot_password': 'パスワードをお忘れですか？',
        'login_button': 'ログイン',
        'register': '登録',
        'other_login_methods': 'その他のログイン方法',
        'scan_tip': 'アプリでスキャンしてログイン',
        'refresh_qrcode': 'QRコードを更新',
        'qr_scanned': 'スキャン完了、スマートフォンで確認してください',
        'qr_expired': 'QRコードの有効期限が切れました。クリックして更新してください',
        'login_success': 'ログイン成功',
        'login_failed': 'ログインに失敗しました。後でもう一度お試しください',
        'server_error': 'サーバーエラー',
        'invalid_captcha': '無効または期限切れの認証コード',
        'invalid_credentials': '電話番号またはパスワードが無効です'
    },
    th: {
        'password_login': 'เข้าสู่ระบบด้วยรหัสผ่าน',
        'qrcode_login': 'เข้าสู่ระบบด้วย QR Code',
        'phone_placeholder': 'กรุณากรอกหมายเลขโทรศัพท์',
        'password_placeholder': 'กรุณากรอกรหัสผ่าน',
        'verification_placeholder': 'รหัสยืนยัน',
        'remember_me': 'จดจำฉัน',
        'forgot_password': 'ลืมรหัสผ่าน?',
        'login_button': 'เข้าสู่ระบบ',
        'register': 'ลงทะเบียน',
        'other_login_methods': 'วิธีการเข้าสู่ระบบอื่นๆ',
        'scan_tip': 'กรุณาสแกน QR Code ด้วยแอพ',
        'refresh_qrcode': 'รีเฟรช QR Code',
        'qr_scanned': 'สแกนแล้ว กรุณายืนยันบนโทรศัพท์',
        'qr_expired': 'QR Code หมดอายุ คลิกเพื่อรีเฟรช',
        'login_success': 'เข้าสู่ระบบสำเร็จ',
        'login_failed': 'เข้าสู่ระบบล้มเหลว กรุณาลองอีกครั้ง',
        'server_error': 'เซิร์ฟเวอร์ผิดพลาด',
        'invalid_captcha': 'รหัสยืนยันไม่ถูกต้องหรือหมดอายุ',
        'invalid_credentials': 'หมายเลขโทรศัพท์หรือรหัสผ่านไม่ถูกต้อง'
    },
    my: {
        'password_login': 'စကားဝှက်ဖြင့်ဝင်ရန်',
        'qrcode_login': 'QR ကုဒ်ဖြင့်ဝင်ရန်',
        'phone_placeholder': 'ဖုန်းနံပါတ်ထည့်ပါ',
        'password_placeholder': 'စကားဝှက်ထည့်ပါ',
        'verification_placeholder': 'အတည်ပြုကုဒ်',
        'remember_me': 'မှတ်ထားရန်',
        'forgot_password': 'စကားဝှက်မေ့နေပါသလား?',
        'login_button': 'ဝင်ရန်',
        'register': 'မှတ်ပုံတင်ရန်',
        'other_login_methods': 'အခြားဝင်ရောက်နည်းများ',
        'scan_tip': 'APP ဖြင့် QR ကုဒ်ကိုစကင်ဖတ်ပါ',
        'refresh_qrcode': 'QR ကုဒ်ပြန်လည်စတင်ရန်',
        'qr_scanned': 'စကင်ဖတ်ပြီးပါပြီ၊ ဖုန်းပေါ်တွင်အတည်ပြုပါ',
        'qr_expired': 'QR ကုဒ်သက်တမ်းကုန်ဆုံးသွားပါပြီ၊ ပြန်လည်စတင်ရန်နှိပ်ပါ',
        'login_success': 'အောင်မြင်စွာဝင်ရောက်ပြီးပါပြီ',
        'login_failed': 'ဝင်ရောက်မှုမအောင်မြင်ပါ၊ ထပ်မံကြိုးစားပါ',
        'server_error': 'ဆာဗာအမှား',
        'invalid_captcha': 'အတည်ပြုကုဒ်မှားယွင်းနေပါသည် သို့မဟုတ် သက်တမ်းကုန်ဆုံးသွားပါပြီ',
        'invalid_credentials': 'ဖုန်းနံပါတ် သို့မဟုတ် စကားဝှက်မှားယွင်းနေပါသည်'
    }
};

// 当前语言
let currentLang = 'zh';

// 更改语言函数
function changeLanguage(lang) {
    currentLang = lang;
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            if (element.tagName === 'INPUT') {
                element.placeholder = translations[lang][key];
            } else {
                element.textContent = translations[lang][key];
            }
        }
    });

    // 更新页面标题
    document.title = translations[lang]['login_title'] || 'Login';
}

// 获取翻译文本的辅助函数
function getTranslation(key) {
    return translations[currentLang][key] || key;
}

// 初始化语言
document.addEventListener('DOMContentLoaded', () => {
    // 获取浏览器语言设置
    const browserLang = navigator.language.split('-')[0];
    // 如果支持该语言，则使用它，否则默认使用中文
    const initialLang = translations[browserLang] ? browserLang : 'zh';
    changeLanguage(initialLang);
}); 