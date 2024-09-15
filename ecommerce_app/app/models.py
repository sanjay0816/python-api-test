from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from app import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    price = Column(Float)
    stock = Column(Integer)
    seller_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    seller = relationship('User')
    category = relationship('Category')
    reviews = relationship('Review', back_populates='product')


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    products = relationship('Product', back_populates='category')


class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    buyer = relationship('User')
    product = relationship('Product')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String)

    buyer = relationship('User')
    products = relationship('ProductOrder', back_populates='order')


class ProductOrder(Base):
    __tablename__ = 'product_orders'

    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer)

    order = relationship('Order', back_populates='products')
    product = relationship('Product')


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer)
    review = Column(Text)

    product = relationship('Product', back_populates='reviews')

