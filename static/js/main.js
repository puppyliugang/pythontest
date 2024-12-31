document.addEventListener('DOMContentLoaded', function() {
    // 标签页切换
    const tabs = document.querySelectorAll('.tab');
    
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // 移除所有活动状态
            tabs.forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.login-form').forEach(form => {
                form.classList.remove('active');
                form.style.display = 'none';  // 确保完全隐藏
            });
            
            // 添加新的活动状态
            tab.classList.add('active');
            const targetForm = document.getElementById(`${tab.dataset.tab}LoginForm`);
            if (targetForm) {
                targetForm.classList.add('active');
                targetForm.style.display = 'block';  // 显示目标表单
                
                // 如果切换到二维码登录，生成二维码
                if (tab.dataset.tab === 'qrcode') {
                    generateQRCode();
                }
            }
        });
    });

    // 密码登录表单提交
    const passwordForm = document.getElementById('passwordLoginForm');
    if (passwordForm) {
        passwordForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = {
                phone: document.getElementById('phone').value,
                password: document.getElementById('password').value,
                remember: document.getElementById('remember').checked,
                language: document.getElementById('languageSelect').value
            };

            try {
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });

                const data = await response.json();
                if (data.success) {
                    // 登录成功后直接跳转到仪表板页面
                    window.location.href = '/dashboard';
                } else {
                    // 显示错误消息
                    alert(getTranslation(data.message) || getTranslation('login_failed'));
                }
            } catch (error) {
                console.error('登录失败:', error);
                alert(getTranslation('server_error'));
            }
        });
    }
});

// 生成二维码
async function generateQRCode() {
    try {
        const response = await fetch('/api/qrcode/generate');
        const data = await response.json();
        
        if (data.success) {
            const qrcodeContainer = document.getElementById('qrcode');
            if (qrcodeContainer) {
                qrcodeContainer.innerHTML = '';  // 清除旧的二维码
                
                // 创建图片元素显示二维码
                const img = document.createElement('img');
                img.src = data.image;
                img.alt = getTranslation('qrcode_login');
                img.style.width = '200px';
                img.style.height = '200px';
                qrcodeContainer.appendChild(img);

                // 开始轮询检查扫码状态
                startQRCodeStatusCheck(data.qrcode);
            }
        }
    } catch (error) {
        console.error('生成二维码失败:', error);
        const tipElement = document.querySelector('.qrcode-tip');
        if (tipElement) {
            tipElement.textContent = getTranslation('qr_expired');
        }
    }
}

// 检查二维码扫描状态
function startQRCodeStatusCheck(qrcodeId) {
    const checkInterval = setInterval(async () => {
        try {
            const response = await fetch(`/api/qrcode/check/${qrcodeId}`);
            const data = await response.json();
            
            const tipElement = document.querySelector('.qrcode-tip');
            if (!tipElement) return;

            if (data.status === 'scanned') {
                tipElement.textContent = getTranslation('qr_scanned');
            } else if (data.status === 'confirmed') {
                clearInterval(checkInterval);
                alert(getTranslation('login_success'));
                window.location.href = '/dashboard';
            } else if (data.status === 'expired') {
                clearInterval(checkInterval);
                tipElement.textContent = getTranslation('qr_expired');
            }
        } catch (error) {
            console.error('检查二维码状态失败:', error);
            clearInterval(checkInterval);
        }
    }, 2000);
}

// 刷新二维码
function refreshQRCode() {
    generateQRCode();
}

async function handleLogin(formType) {
    const form = document.getElementById(`${formType}LoginForm`);
    const phone = form.querySelector('input[name="phone"]').value;
    const password = form.querySelector('input[name="password"]').value;
    const selectedLanguage = document.getElementById('languageSelect').value;

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                phone: phone,
                password: password,
                language: selectedLanguage
            })
        });

        const data = await response.json();
        if (data.success) {
            window.location.href = '/dashboard';
        } else {
            // 使用 i18n.js 中的翻译
            alert(translations[currentLanguage][data.message] || translations[currentLanguage]['login_failed']);
        }
    } catch (error) {
        console.error('登录失败:', error);
        // 使用 i18n.js 中的翻译
        alert(translations[currentLanguage]['server_error']);
    }
} 