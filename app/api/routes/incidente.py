from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import crud, schemas
from app.api.deps import get_db

router = APIRouter()

@router.get("/incidentes", response_model=List[schemas.IncidenteOut])
def list_incidentes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_incidentes(db, skip=skip, limit=limit)

@router.post("/incidentes", response_model=schemas.IncidenteOut, status_code=status.HTTP_201_CREATED)
def create_incidente(incidente_in: schemas.IncidenteCreate, db: Session = Depends(get_db)):
    return crud.create_incidente(db, incidente_in)

@router.put("/incidentes/{incidente_id}", response_model=schemas.IncidenteOut)
def update_incidente(incidente_id: int, incidente_update: schemas.IncidenteUpdate, db: Session = Depends(get_db)):
    incidente = crud.update_incidente(db, incidente_id, incidente_update)
    if not incidente:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    return incidente

@router.delete("/incidentes/{incidente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incidente(incidente_id: int, db: Session = Depends(get_db)):
    incidente = crud.delete_incidente(db, incidente_id)
    if not incidente:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    return None

@router.get("/sistemas", response_model=List[schemas.SistemaOut])
def list_sistemas(db: Session = Depends(get_db)):
    return crud.get_sistemas(db)


@router.get("/proyectos-modulo", response_model=List[schemas.ProyectoModuloOut])
def list_proyectos_modulo(db: Session = Depends(get_db)):
    return crud.get_proyectos_modulo(db)