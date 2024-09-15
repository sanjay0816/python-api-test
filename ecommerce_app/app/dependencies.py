from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app import models
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_seller(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Dummy function to get seller from token
    # Implement JWT token validation and check seller role
    return models.User(id=1, role="seller")

