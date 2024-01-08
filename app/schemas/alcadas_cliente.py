from pydantic import BaseModel
from typing import List

class AlcadasClienteBase(BaseModel):
    limite_minimo_aprovacao: float
    limite_maximo_aprovacao: float
    perfil_aprovador: str
    percentual_aprovacao: float

class AlcadasClienteCreate(BaseModel):
    limite_minimo_aprovacao: float
    limite_maximo_aprovacao: float
    perfil_aprovador: str
    percentual_aprovacao: float

class AlcadasClienteUpdate(AlcadasClienteBase):
    pass

class AlcadasClienteInDB(AlcadasClienteBase):
    id: int
    id_cliente: int
    id_tipo_rating: int

    class Config:
        orm_mode = True

class AlcadasCliente(AlcadasClienteInDB):
    pass