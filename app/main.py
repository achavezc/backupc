from fastapi import FastAPI
from app.api.routes import auth
from app.api.routes import admin
from app.api.routes import incidente
from app.api.routes import proyecto
from app.api.routes import clasificacion
from app.api.routes import recomendacion
from app.db.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O solo los dominios que necesitas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(incidente.router, prefix="/incidente", tags=["incidente"])
app.include_router(clasificacion.router, prefix="/clasificacion", tags=["clasificacion"])
app.include_router(proyecto.router, prefix="/proyecto", tags=["proyecto"])
app.include_router(recomendacion.router, prefix="/recomendacion", tags=["recomendacion"])

