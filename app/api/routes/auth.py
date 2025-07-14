from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud, schemas
from app.api.deps import get_db
from app.utils.password import verify_password
from app.core.security import create_access_token
from datetime import timedelta
from app.core.config import settings
from app.utils.password import hash_password

router = APIRouter()

@router.post("/login", response_model=schemas.Token)
def login(user_in: schemas.UserLogin, db: Session = Depends(get_db)):
    print(user_in.email)
    print(user_in.password)
    user = crud.get_user_by_email(db, user_in.email)
    print("HASH EN BD:", user.password_hash)
    print("INTENTANDO CONTRA:", user_in.password)
    print("VERIFICACIÓN:", verify_password(user_in.password, user.password_hash))
    if not user or not verify_password(user_in.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    access_token = create_access_token(
        data={"user_id": user.id, "profile": user.profile.name},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}


""" @router.post("/register", response_model=schemas.UserOut)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    hashed_password = hash_password(user_in.password)

    user_data = user_in.dict()
    user_data["password_hash"] = hashed_password
    del user_data["password"]  # eliminamos campo sensible

    user_data["is_active"] = True

    user = crud.create_user(db, user_data)
    return user """