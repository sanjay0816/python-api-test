from sqlalchemy.orm import Session
from app import models, schemas

def create_product(db: Session, product: schemas.ProductCreate, seller_id: int):
    db_product = models.Product(**product.dict(), seller_id=seller_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def update_product(db: Session, product_id: int, product: schemas.ProductUpdate, seller_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id, models.Product.seller_id == seller_id).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int, seller_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id, models.Product.seller_id == seller_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()

