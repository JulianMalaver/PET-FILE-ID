from fastapi import APIRouter, Response, status, HTTPException
from sqlalchemy.orm import Session
from config.db import conn
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT


user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

# Crear un nuevo usuario
@user.post("/users")
def create_user(user: User):
        new_user = {"name": user.name}
        result = conn.execute(users.insert().values(new_user))
        print (result.lastrowid)
        return "done"

@user.get("/users/{id}")
def heloww(id: str):
   return conn.execute(users.select().where(users.c.id == id)).first()
