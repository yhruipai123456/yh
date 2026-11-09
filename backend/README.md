# backend 后端服务

## 目录结构
```
backend/
├── app/
│   ├── main.py            # FastAPI 入口
│   ├── config.py          # 配置（读 .env）
│   ├── database.py        # SQLAlchemy 引擎与 Session
│   ├── models.py          # Admin / Article 数据模型
│   ├── schemas.py         # Pydantic 校验模型
│   ├── security.py        # 密码哈希 + JWT
│   ├── deps.py            # 登录依赖注入
│   └── routers/
│       ├── auth.py        # 登录接口
│       └── articles.py    # 文章增删改查
├── init_db.py             # 建表 + 初始管理员
├── requirements.txt
└── .env                   # 本地配置（已 gitignore）
```

## 启动步骤
```bash
# 1. 安装依赖（Windows 用 py 启动器）
cd backend
py -m pip install -r requirements.txt

# 2. 初始化数据库（建表 + 创建初始管理员 admin / admin123456）
py init_db.py

# 3. 启动服务（默认 http://127.0.0.1:8000）
py -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 接口速览
- `POST /api/auth/login`  登录，返回 JWT（表单字段 username / password）
- `GET  /api/articles`    前台公开文章列表（仅已发布）
- `GET  /api/articles/{id}` 前台读取单篇
- `POST /api/articles`    创建文章（需 Bearer Token）
- `PUT  /api/articles/{id}` 更新文章（需登录）
- `DELETE /api/articles/{id}` 删除文章（需登录）
- `GET  /api/health`      健康检查

交互文档：启动后访问 http://127.0.0.1:8000/docs