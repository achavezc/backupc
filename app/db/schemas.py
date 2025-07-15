from pydantic import BaseModel, EmailStr, constr, validator
from datetime import date, time, timedelta, datetime
from typing import Optional, List

class Token(BaseModel):
    access_token: str
    token_type: str

# --- Usuarios ---

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str
    profile_id: int
    is_active: Optional[bool] = True

    @validator('password')
    def password_strength(cls, v):
        import re
        if len(v) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Debe contener al menos una letra mayúscula')
        if not re.search(r'[a-z]', v):
            raise ValueError('Debe contener al menos una letra minúscula')
        if not re.search(r'\d', v):
            raise ValueError('Debe contener al menos un número')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Debe contener al menos un carácter especial')
        if ' ' in v:
            raise ValueError('No debe contener espacios')
        return v

class UserUpdate(BaseModel):
    full_name: Optional[str]
    profile_id: Optional[int]
    is_active: Optional[bool]

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ProfileBase(BaseModel):
    name: str

class ProfileOut(ProfileBase):
    id: int

    class Config:
        orm_mode = True

class UserOut(UserBase):
    id: int
    is_active: bool
    profile_id: int
    profile: ProfileOut  
    class Config:
        orm_mode = True

# --- Perfiles ---



class ProfileCreate(ProfileBase):
    privileges: List[int]

    @validator('privileges')
    def must_have_privileges(cls, v):
        if len(v) == 0:
            raise ValueError('Debe seleccionar al menos un privilegio')
        return v

class ProfileUpdate(BaseModel):
    name: Optional[str]
    privileges: Optional[List[int]]


### incidente.py

class SistemaOut(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True

class ProyectoModuloOut(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True

class IncidenteBase(BaseModel):
    fecha: date
    hora: time
    sistema_id: int
    proyectomodulo_id: int
    usuario_reportador: Optional[str]
    descripcion: Optional[str]
    tiempo_estimado: Optional[int]
    fecha_solucion: Optional[date]
    hora_solucion: Optional[time]
    usuario_registro: Optional[str]
    fecha_registro: Optional[datetime]
    usuario_actualizacion: Optional[str]
    fecha_actualizacion: Optional[datetime]

class IncidenteCreate(IncidenteBase):
    pass

class IncidenteUpdate(BaseModel):
    fecha: Optional[date]
    hora: Optional[time]
    sistema_id: Optional[int]
    proyectomodulo_id: Optional[int]
    usuario_reportador: Optional[str]
    descripcion: Optional[str]
    tiempo_estimado: Optional[int]
    fecha_solucion: Optional[date]
    hora_solucion: Optional[time]
    usuario_actualizacion: Optional[str]
    fecha_actualizacion: Optional[datetime]

class IncidenteOut(IncidenteBase):
    id: int
    sistema: SistemaOut
    proyecto_modulo: ProyectoModuloOut
    class Config:
        orm_mode = True

class SistemaOut(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True


class ProyectoModuloOut(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

# clasificacionincidente.py
class FaseProyectoOut(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True

class ImpactoOut(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True

class TipoOut(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True

class IncidenteComboOut(BaseModel):
    id: int
    descripcion: str
    class Config:
        orm_mode = True

class ClasificacionIncidenteBase(BaseModel):
    incidente_id: int
    faseproyecto_id: int
    impacto_id: int
    tipo_id: int
    usuario_registro: Optional[str]
    fecha_registro: Optional[datetime]
    usuario_actualizacion: Optional[str]
    fecha_actualizacion: Optional[datetime]

class ClasificacionIncidenteCreate(ClasificacionIncidenteBase):
    pass

class ClasificacionIncidenteUpdate(BaseModel):
    faseproyecto_id: Optional[int]
    impacto_id: Optional[int]
    tipo_id: Optional[int]
    usuario_actualizacion: Optional[str]
    fecha_actualizacion: Optional[datetime]

class ClasificacionIncidenteOut(ClasificacionIncidenteBase):
    id: int
    incidente: IncidenteOut
    faseproyecto: FaseProyectoOut
    impacto: ImpactoOut
    tipo: TipoOut
    
    class Config:
        orm_mode = True

#proyecto.py
class PrioridadOut(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True

class EstadoOut(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True

class ProyectoBase(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_fin: date
    prioridad_id: int
    faseproyecto_id: int
    estado_id: int

class ProyectoCreate(ProyectoBase):
    usuario_registro: str

class ProyectoUpdate(BaseModel):
    nombre: Optional[str]
    fecha_inicio: Optional[date]
    fecha_fin: Optional[date]
    prioridad_id: Optional[int]
    faseproyecto_id: Optional[int]
    estado_id: Optional[int]
    usuario_actualizacion: Optional[str]

class ProyectoOut(ProyectoBase):
    id: int
    usuario_registro: str
    fecha_registro: datetime
    usuario_actualizacion: Optional[str]
    fecha_actualizacion: Optional[datetime]
    prioridad: PrioridadOut
    fase_proyecto: PrioridadOut  # Aprovecha el mismo esquema
    estado: EstadoOut
    class Config:
        orm_mode = True

#recomendaciones
class RecomendacionBase(BaseModel):
    incidente_id: int
    prioridad_id: int
    faseproyecto_id: int
    tipoaccion_id: int
    frecuencia_id: int
    recomendacion: str

class RecomendacionCreate(RecomendacionBase):
    usuario_registro: str

class RecomendacionUpdate(BaseModel):
    prioridad_id: Optional[int]
    faseproyecto_id: Optional[int]
    tipoaccion_id: Optional[int]
    frecuencia_id: Optional[int]
    recomendacion: Optional[str]
    usuario_actualizacion: Optional[str]


class TipoAccionOut(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True

class FrecuenciaOut(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True


class RecomendacionOut(RecomendacionBase):
    id: int
    usuario_registro: Optional[str]
    fecha_registro: Optional[datetime]
    usuario_actualizacion: Optional[str]
    fecha_actualizacion: Optional[datetime]
    incidente: IncidenteOut
    prioridad: PrioridadOut
    fase_proyecto: PrioridadOut  # Aprovecha el mismo esquema
    tipo_accion: TipoAccionOut
    frecuencia: FrecuenciaOut
    class Config:
        orm_mode = True

class ComboOut(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

