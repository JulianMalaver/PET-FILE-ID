from typing import Optional
from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    id: str | None = None
    name: str
    #color: Optional[str]
    #sexo: str
    #especie: str
    #raza: str
    #birth: Optional[str]
    #propietario: Optional[str]


