from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta, engine

users = Table(
    "users", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),  # nombre de la mascota
    # Column("color", String(255)),   # color de la mascota
    # Column("birth", Date),   # color de la mascota
    # Column("sexo", String(1)),      # sexo de la mascota
    # Column("especie", String(255)), # especie de la mascota
    # Column("raza", String(255)),    # raza de la mascota
    # Column("fecha_nacimiento", Date), # fecha de nacimiento de la mascota
    # Column("propietario", String(255)) # propietario de la mascota
)

meta.create_all(engine)
