from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import crud, schemas
from app.api.deps import get_db

router = APIRouter()

# ✅ Primero los combos
@router.get("/faseproyectos", response_model=List[schemas.FaseProyectoOut])
def list_fase_proyectos(db: Session = Depends(get_db)):
    return crud.get_fase_proyectos(db)

@router.get("/impactos", response_model=List[schemas.ImpactoOut])
def list_impactos(db: Session = Depends(get_db)):
    return crud.get_impactos(db)

@router.get("/tipos", response_model=List[schemas.TipoOut])
def list_tipos(db: Session = Depends(get_db)):
    return crud.get_tipos(db)

@router.get("/incidentecombo", response_model=List[schemas.IncidenteComboOut])
def list_incidentecombo(db: Session = Depends(get_db)):
    return crud.get_incidentecombo(db)

# ✅ Luego el CRUD general
@router.get("/", response_model=List[schemas.ClasificacionIncidenteOut])
def list_clasificaciones(db: Session = Depends(get_db)):
    return crud.get_clasificaciones(db)

@router.post("/", response_model=schemas.ClasificacionIncidenteOut)
def create_clasificacion(data: schemas.ClasificacionIncidenteCreate, db: Session = Depends(get_db)):
    return crud.create_clasificacion(db, data)

# ✅ Por último las rutas dinámicas
@router.get("/{id}", response_model=schemas.ClasificacionIncidenteOut)
def get_clasificacion(id: int, db: Session = Depends(get_db)):
    clasif = crud.get_clasificacion_by_id(db, id)
    if not clasif:
        raise HTTPException(status_code=404, detail="No encontrado")
    return clasif

@router.put("/{id}", response_model=schemas.ClasificacionIncidenteOut)
def update_clasificacion(id: int, data: schemas.ClasificacionIncidenteUpdate, db: Session = Depends(get_db)):
    clasif = crud.update_clasificacion(db, id, data)
    if not clasif:
        raise HTTPException(status_code=404, detail="No encontrado")
    return clasif

@router.delete("/{id}")
def delete_clasificacion(id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_clasificacion(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="No encontrado")
    return {"ok": True}
