from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import crud, schemas
from app.api.deps import get_db  # asumiendo tienes esto para obtener DB session
from app.utils.password import hash_password

router = APIRouter()
#router = APIRouter(prefix="/admin", tags=["admin"])

# --- USUARIOS ---

@router.get("/users", response_model=List[schemas.UserOut])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print(dir(crud))
    return crud.get_users(db, skip=skip, limit=limit)

@router.post("/users", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    user_data = user_in.dict()
    user_data["password_hash"] = hash_password(user_in.password)
    user_data.pop("password")  # eliminar plain password para no guardarlo
    user = crud.create_user(db, user_data)
    return user

@router.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id, user_update.dict(exclude_unset=True))
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return None

# --- PERFILES ---

@router.get("/profiles", response_model=List[schemas.ProfileOut])
def list_profiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_profiles(db, skip=skip, limit=limit)

@router.post("/profiles", response_model=schemas.ProfileOut, status_code=status.HTTP_201_CREATED)
def create_profile(profile_in: schemas.ProfileCreate, db: Session = Depends(get_db)):
    profile_data = profile_in.dict()
    profile = crud.create_profile(db, profile_data)
    return profile

@router.put("/profiles/{profile_id}", response_model=schemas.ProfileOut)
def update_profile(profile_id: int, profile_update: schemas.ProfileUpdate, db: Session = Depends(get_db)):
    profile = crud.update_profile(db, profile_id, profile_update.dict(exclude_unset=True))
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return profile

@router.delete("/profiles/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    try:
        profile = crud.delete_profile(db, profile_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return None
