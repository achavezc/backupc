from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import crud, schemas
from app.api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.RecomendacionOut])
def list_recomendaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_recomendaciones(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.RecomendacionOut)
def crear_recomendacion(data: schemas.RecomendacionCreate, db: Session = Depends(get_db)):
    return crud.create_recomendacion(db, data)

@router.put("/{recomendacion_id}", response_model=schemas.RecomendacionOut)
def actualizar_recomendacion(recomendacion_id: int, data: schemas.RecomendacionUpdate, db: Session = Depends(get_db)):
    result = crud.update_recomendacion(db, recomendacion_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Recomendacion no encontrada")
    return result

@router.delete("/{recomendacion_id}")
def eliminar_recomendacion(recomendacion_id: int, db: Session = Depends(get_db)):
    result = crud.delete_recomendacion(db, recomendacion_id)
    if not result:
        raise HTTPException(status_code=404, detail="Recomendacion no encontrada")
    return {"message": "Eliminado correctamente"}

@router.get("/combo/tipoaccion", response_model=List[schemas.ComboOut])
def listar_tipoaccion(db: Session = Depends(get_db)):
    return crud.list_tipo_accion(db)

@router.get("/combo/frecuencia", response_model=List[schemas.ComboOut])
def listar_frecuencia(db: Session = Depends(get_db)):
    return crud.list_frecuencia(db)
