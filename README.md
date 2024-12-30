# 登录系统

这是一个基于Flask的简单登录系统，包含用户认证、验证码等功能。

## 功能特点

- 用户登录/注册
- 验证码支持
- 记住密码功能
- 响应式界面设计
- SQLite数据库存储

## 安装说明

1. 克隆项目到本地
2. 创建虚拟环境（推荐）：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   .\venv\Scripts\activate  # Windows
   ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 运行项目

```bash
python app.py
```

访问 http://localhost:5000 即可看到登录界面。

## 目录结构

```
.
├── app.py              # 后端主程序
├── requirements.txt    # 项目依赖
├── static/            # 静态资源
│   ├── css/          # 样式文件
│   └── js/           # JavaScript文件
└── templates/         # HTML模板
    └── login.html    # 登录页面
```

## 技术栈

- 后端：Python Flask
- 数据库：SQLite
- 前端：HTML5 + CSS3 + JavaScript 