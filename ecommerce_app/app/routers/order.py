from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, dependencies

router = APIRouter()

@router.post("/place", response_model=schemas.Order)
def place_order(order: schemas.OrderCreate, db: Session = Depends(dependencies.get_db), user=Depends(dependencies.get_current_seller)):
    db_order = models.Order(buyer_id=user.id, status="Pending")
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    for item in order.products:
        product_order = models.ProductOrder(order_id=db_order.id, product_id=item.product_id, quantity=item.quantity)
        db.add(product_order)
    db.commit()
    return db_order

@router.get("/view", response_model=list[schemas.Order])
def view_orders(db: Session = Depends(dependencies.get_db), user=Depends(dependencies.get_current_seller)):
    return db.query(models.Order).filter(models.Order.buyer_id == user.id).all()

@router.put("/update_status/{order_id}")
def update_order_status(order_id: int, status: str, db: Session = Depends(dependencies.get_db), user=Depends(dependencies.get_current_seller)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id, models.Order.buyer_id == user.id).first()
    if db_order:
        db_order.status = status
        db.commit()
        db.refresh(db_order)
    return db_order

