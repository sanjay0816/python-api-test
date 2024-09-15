from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from app.routers import product, order, cart, category

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # or your actual DB URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI app setup
app = FastAPI()

# Include routes
app.include_router(product.router, prefix="/product", tags=["Product"])
app.include_router(order.router, prefix="/order", tags=["Order"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(category.router, prefix="/category", tags=["Category"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

