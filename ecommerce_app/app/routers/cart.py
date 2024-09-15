from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, dependencies

router = APIRouter()

@router.post("/add", response_model=schemas.CartItem)
def add_to_cart(cart_item: schemas.CartItem, db: Session = Depends(dependencies.get_db), user=Depends(dependencies.get_current_seller)):
    db_cart_item = models.Cart(buyer_id=user.id, product_id=cart_item.product_id, quantity=cart_item.quantity)
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

@router.delete("/remove/{cart_item_id}")
def remove_from_cart(cart_item_id: int, db: Session = Depends(dependencies.get_db), user=Depends(dependencies.get_current_seller)):
    db_cart_item = db

