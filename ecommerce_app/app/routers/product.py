from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, dependencies

router = APIRouter()

@router.post("/add", response_model=schemas.Product)
def add_product(product: schemas.ProductCreate, db: Session = Depends(dependencies.get_db), user=Depends(dependencies.get_current_seller)):
    return crud.create_product(db, product, seller_id=user.id)

@router.put("/update/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(dependencies.get_db), user=Depends(dependencies.get_current_seller)):
    return crud.update_product(db, product_id, product, seller_id=user.id)

@router.delete("/delete/{product_id}")
def delete_product(product_id: int, db: Session = Depends(dependencies.get_db), user=Depends(dependencies.get_current_seller)):
    crud.delete_product(db, product_id, seller_id=user.id)
    return {"msg": "Product deleted"}

@router.get("/list", response_model=list[schemas.Product])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

