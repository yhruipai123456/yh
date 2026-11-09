# backend/init_db.py
"""初始化数据库：建表 + 创建初始管理员账号。"""
from app.database import Base, SessionLocal, engine
from app.models import Admin
from app.config import settings
from app.security import hash_password


def main() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        existing = db.query(Admin).filter(Admin.username == settings.ADMIN_USERNAME).first()
        if existing:
            print(f"管理员账号 {settings.ADMIN_USERNAME!r} 已存在，跳过创建。")
            return
        admin = Admin(
            username=settings.ADMIN_USERNAME,
            hashed_password=hash_password(settings.ADMIN_PASSWORD),
        )
        db.add(admin)
        db.commit()
        print(f"已创建管理员账号：{settings.ADMIN_USERNAME}")
    finally:
        db.close()


if __name__ == "__main__":
    main()