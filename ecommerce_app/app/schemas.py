from pydantic import BaseModel
from typing import Optional, List

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    seller_id: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class CartItem(BaseModel):
    product_id: int
    quantity: int


class OrderBase(BaseModel):
    status: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    buyer_id: int
    status: str
    products: List[CartItem]

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    rating: int
    review: Optional[str] = None

class ReviewCreate(ReviewBase):
    product_id: int

