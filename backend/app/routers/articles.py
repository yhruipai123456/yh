# backend/app/routers/articles.py
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from ..database import get_db
from ..deps import get_current_admin
from ..models import Admin, Article
from ..schemas import ArticleCreate, ArticleOut, ArticleUpdate

router = APIRouter(prefix="/api/articles", tags=["articles"])


# —— 前台公开接口（只读、仅已发布）——
@router.get("", response_model=list[ArticleOut])
def list_articles(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    items = (
        db.query(Article)
        .filter(Article.is_published.is_(True))
        .order_by(Article.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return items


@router.get("/{article_id}", response_model=ArticleOut)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = (
        db.query(Article)
        .filter(Article.id == article_id, Article.is_published.is_(True))
        .first()
    )
    if article is None:
        raise HTTPException(status_code=404, detail="文章不存在")
    return article


# —— 后台管理接口（需登录）——
@router.post("", response_model=ArticleOut, status_code=status.HTTP_201_CREATED)
def create_article(
    payload: ArticleCreate,
    db: Session = Depends(get_db),
    _: Admin = Depends(get_current_admin),
):
    article = Article(**payload.model_dump())
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


@router.put("/{article_id}", response_model=ArticleOut)
def update_article(
    article_id: int,
    payload: ArticleUpdate,
    db: Session = Depends(get_db),
    _: Admin = Depends(get_current_admin),
):
    article = db.get(Article, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="文章不存在")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(article, key, value)
    db.commit()
    db.refresh(article)
    return article


@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(
    article_id: int,
    db: Session = Depends(get_db),
    _: Admin = Depends(get_current_admin),
):
    article = db.get(Article, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="文章不存在")
    db.delete(article)
    db.commit()