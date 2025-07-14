from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, Text, Date, Time, Interval,TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.database import Base

profile_privileges = Table(
    "profile_privileges", Base.metadata,
    Column("profile_id", ForeignKey("profiles.id"), primary_key=True),
    Column("privilege_id", ForeignKey("privileges.id"), primary_key=True)
)

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    privileges = relationship("Privilege", secondary=profile_privileges, back_populates="profiles")
    users = relationship("User", back_populates="profile")

class Privilege(Base):
    __tablename__ = "privileges"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    profiles = relationship("Profile", secondary=profile_privileges, back_populates="privileges")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    profile = relationship("Profile", back_populates="users")


### incidente.py

class Sistema(Base):
    __tablename__ = "sistema"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class ProyectoModulo(Base):
    __tablename__ = "proyecto_modulo"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Incidente(Base):
    __tablename__ = "incidente"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    sistema_id = Column(Integer, ForeignKey("sistema.id"))
    proyectomodulo_id = Column(Integer, ForeignKey("proyecto_modulo.id"))
    usuario_reportador = Column(String)
    descripcion = Column(Text)
    tiempo_estimado = Column(Integer)
    fecha_solucion = Column(Date)
    hora_solucion = Column(Time)
    usuario_registro = Column(String)
    fecha_registro = Column(TIMESTAMP)
    usuario_actualizacion = Column(String)
    fecha_actualizacion = Column(TIMESTAMP)

    sistema = relationship("Sistema")
    proyecto_modulo = relationship("ProyectoModulo")

# clasificacion.py
class FaseProyecto(Base):
    __tablename__ = "fase_proyecto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

class Impacto(Base):
    __tablename__ = "impacto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

class Tipo(Base):
    __tablename__ = "tipo"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)


class ClasificacionIncidente(Base):
    __tablename__ = "clasificacion_incidente"
    id = Column(Integer, primary_key=True)
    incidente_id = Column(Integer, ForeignKey("incidente.id"))
    faseproyecto_id = Column(Integer, ForeignKey("fase_proyecto.id"))
    impacto_id = Column(Integer, ForeignKey("impacto.id"))
    tipo_id = Column(Integer, ForeignKey("tipo.id"))
    usuario_registro = Column(String)
    fecha_registro = Column(TIMESTAMP)
    usuario_actualizacion = Column(String)
    fecha_actualizacion = Column(TIMESTAMP)

    incidente = relationship("Incidente")
    faseproyecto = relationship("FaseProyecto")
    impacto = relationship("Impacto")
    tipo = relationship("Tipo")

# proyecto 
class Prioridad(Base):
    __tablename__ = "prioridad"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)

class Estado(Base):
    __tablename__ = "estado"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)

class Proyecto(Base):
    __tablename__ = "proyecto"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    sistema_id = Column(Integer)  # si luego es FK, agregarlo
    prioridad_id = Column(Integer, ForeignKey("prioridad.id"))
    faseproyecto_id = Column(Integer, ForeignKey("fase_proyecto.id"))
    estado_id = Column(Integer, ForeignKey("estado.id"))
    usuario_registro = Column(String(100), nullable=False)
    fecha_registro = Column(TIMESTAMP, nullable=False)
    usuario_actualizacion = Column(String(100))
    fecha_actualizacion = Column(TIMESTAMP)

    prioridad = relationship("Prioridad")
    fase_proyecto = relationship("FaseProyecto")
    estado = relationship("Estado")