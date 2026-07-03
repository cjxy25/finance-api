from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.category import Category

router = APIRouter()


class CreateCategoryRequest(BaseModel):
    category_name: str


@router.get("/categories")
def list_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories


@router.post("/categories")
def create_category(req: CreateCategoryRequest, db: Session = Depends(get_db)):
    cat = Category(category_name=req.category_name, user_id=1)
    db.add(cat)
    db.commit()
    return {"msg": "创建成功"}


@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    cat = db.query(Category).filter(Category.category_id == category_id).first()
    if not cat:
        return {"error": "分类不存在"}
    db.delete(cat)
    db.commit()
    return {"msg": "删除成功"}
