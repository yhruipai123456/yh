# 后端服务镜像（FastAPI + SQLAlchemy + MySQL）
FROM python:3.14-slim

WORKDIR /app

# 防止生成 __pycache__，日志实时输出
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 先复制依赖清单，利用 Docker 层缓存
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

EXPOSE 8000

# 启动前先初始化数据库（建表 + 创建管理员），再启动 API 服务
CMD ["sh", "-c", "python init_db.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
