# backend/app/schemas.py
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ArticleBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    cover_url: str | None = None
    summary: str | None = Field(default=None, max_length=500)


class ArticleCreate(ArticleBase):
    is_published: bool = True


class ArticleUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None = Field(default=None, min_length=1)
    cover_url: str | None = None
    summary: str | None = Field(default=None, max_length=500)
    is_published: bool | None = None


class ArticleOut(ArticleBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_published: bool
    created_at: datetime
    updated_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    username: str
    password: str