# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import articles, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="亿鸿官网后台 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(articles.router)


@app.get("/api/health", tags=["health"])
def health():
    return {"status": "ok"}