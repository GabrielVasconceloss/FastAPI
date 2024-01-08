from pydantic import BaseModel
from typing import List

class AprovadoresClienteBase(BaseModel):
    id_cliente: int
    cargo_aprovador: str
    login_aprovador: str
    perfil_aprovador: str
    percentual_peso_aprovador: float

class AprovadoresClienteCreate(BaseModel):
    cargo_aprovador: str
    login_aprovador: str
    perfil_aprovador: str
    percentual_peso_aprovador: float

class AprovadoresClienteUpdate(AprovadoresClienteBase):
    pass

class AprovadoresClienteInDB(AprovadoresClienteBase):
    id: int

    class Config:
        orm_mode = True

class AprovadoresCliente(AprovadoresClienteInDB):
    pass