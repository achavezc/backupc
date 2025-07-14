from sqlalchemy.orm import Session
from app.db import models, schemas
from app.utils.password import hash_password
from sqlalchemy.orm import joinedload
from datetime import datetime

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user_data: dict):
    db_user = models.User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).options(joinedload(models.User.profile)).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, update_data: dict):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user


def get_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profile).offset(skip).limit(limit).all()

def get_profile_by_id(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()

def create_profile(db: Session, profile_data: dict):
    profile = models.Profile(**profile_data)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def update_profile(db: Session, profile_id: int, update_data: dict):
    profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if not profile:
        return None
    for key, value in update_data.items():
        setattr(profile, key, value)
    db.commit()
    db.refresh(profile)
    return profile

def delete_profile(db: Session, profile_id: int):
    profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if not profile:
        return None
    # Verificar que no existan usuarios con este perfil antes de eliminar
    users = db.query(models.User).filter(models.User.profile_id == profile_id).count()
    if users > 0:
        raise Exception("No se puede eliminar perfil, existen usuarios asociados.")
    db.delete(profile)
    db.commit()
    return profile


#incidente crud.py

def get_incidentes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Incidente).options(joinedload(models.Incidente.sistema), joinedload(models.Incidente.proyecto_modulo)).offset(skip).limit(limit).all()

def get_incidente_by_id(db: Session, incidente_id: int):
    return db.query(models.Incidente).filter(models.Incidente.id == incidente_id).first()

def create_incidente(db: Session, incidente_in: schemas.IncidenteCreate):
    incidente = models.Incidente(**incidente_in.dict())
    db.add(incidente)
    db.commit()
    db.refresh(incidente)
    return incidente

def update_incidente(db: Session, incidente_id: int, incidente_update: schemas.IncidenteUpdate):
    incidente = db.query(models.Incidente).filter(models.Incidente.id == incidente_id).first()
    if not incidente:
        return None
    for key, value in incidente_update.dict(exclude_unset=True).items():
        setattr(incidente, key, value)
    db.commit()
    db.refresh(incidente)
    return incidente

def delete_incidente(db: Session, incidente_id: int):
    incidente = db.query(models.Incidente).filter(models.Incidente.id == incidente_id).first()
    if not incidente:
        return None
    db.delete(incidente)
    db.commit()
    return incidente

def get_sistemas(db: Session):
    return db.query(models.Sistema).all()


def get_proyectos_modulo(db: Session):
    return db.query(models.ProyectoModulo).all()

# clasificacionincidente.py
def get_clasificaciones(db: Session):
    return db.query(models.ClasificacionIncidente).all()

def create_clasificacion(db: Session, data: schemas.ClasificacionIncidenteCreate):
    obj = models.ClasificacionIncidente(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_clasificacion_by_id(db: Session, id: int):
    return db.query(models.ClasificacionIncidente).filter(models.ClasificacionIncidente.id == id).first()

def update_clasificacion(db: Session, id: int, update_data: schemas.ClasificacionIncidenteUpdate):
    obj = db.query(models.ClasificacionIncidente).filter(models.ClasificacionIncidente.id == id).first()
    if not obj:
        return None
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_clasificacion(db: Session, id: int):
    obj = db.query(models.ClasificacionIncidente).filter(models.ClasificacionIncidente.id == id).first()
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj

def get_fase_proyectos(db: Session):
    return db.query(models.FaseProyecto).all()

def get_impactos(db: Session):
    return db.query(models.Impacto).all()

def get_tipos(db: Session):
    return db.query(models.Tipo).all()

def get_incidentecombo(db: Session):
    return db.query(models.Incidente).all()

#proyectocrud.py
def get_prioridades(db: Session):
    return db.query(models.Prioridad).all()

def get_estados(db: Session):
    return db.query(models.Estado).all()

def get_proyectos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Proyecto).offset(skip).limit(limit).all()

def get_proyecto(db: Session, proyecto_id: int):
    return db.query(models.Proyecto).filter(models.Proyecto.id == proyecto_id).first()

def create_proyecto(db: Session, data: schemas.ProyectoCreate):
    db_p = models.Proyecto(**data.dict(), fecha_registro=datetime.now())
    db.add(db_p); db.commit(); db.refresh(db_p)
    return db_p

def update_proyecto(db: Session, proyecto_id: int, data: schemas.ProyectoUpdate):
    p = db.query(models.Proyecto).filter(models.Proyecto.id == proyecto_id).first()
    if not p: return None
    for k,v in data.dict(exclude_unset=True).items():
        setattr(p, k, v)
    p.fecha_actualizacion = datetime.now()
    db.commit(); db.refresh(p)
    return p

def delete_proyecto(db: Session, proyecto_id: int):
    p = db.query(models.Proyecto).filter(models.Proyecto.id == proyecto_id).first()
    if not p: return None
    db.delete(p); db.commit()
    return p