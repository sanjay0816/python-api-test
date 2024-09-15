from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, dependencies

router = APIRouter()

@router.post("/add", response_model=schemas.Category)
def add_category(category: schemas.CategoryCreate, db: Session = Depends(dependencies.get_db)):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/list", response_model=list[schemas.Category])
def list_categories(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    return db.query(models.Category).offset(skip).limit(limit).all()

