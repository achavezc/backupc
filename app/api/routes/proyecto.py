from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import crud, schemas
from app.api.deps import get_db

router = APIRouter()

@router.get("/prioridades", response_model=List[schemas.PrioridadOut])
def lista_prioridades(db: Session = Depends(get_db)):
    return crud.get_prioridades(db)

@router.get("/estados", response_model=List[schemas.EstadoOut])
def lista_estados(db: Session = Depends(get_db)):
    return crud.get_estados(db)

@router.get("/", response_model=List[schemas.ProyectoOut])
def listar_proyectos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_proyectos(db, skip, limit)

@router.post("/", response_model=schemas.ProyectoOut, status_code=status.HTTP_201_CREATED)
def crear_proyecto(proyecto: schemas.ProyectoCreate, db: Session = Depends(get_db)):
    return crud.create_proyecto(db, proyecto)

@router.get("/{id}", response_model=schemas.ProyectoOut)
def ver_proyecto(id: int, db: Session = Depends(get_db)):
    p = crud.get_proyecto(db, id)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe")
    return p

@router.put("/{id}", response_model=schemas.ProyectoOut)
def modificar_proyecto(id: int, data: schemas.ProyectoUpdate, db: Session = Depends(get_db)):
    p = crud.update_proyecto(db, id, data)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe")
    return p

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_proyecto(id: int, db: Session = Depends(get_db)):
    p = crud.delete_proyecto(db, id)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe")
    return None
