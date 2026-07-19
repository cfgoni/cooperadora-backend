from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Railway va a inyectar esta variable automáticamente
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
