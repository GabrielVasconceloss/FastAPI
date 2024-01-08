from typing import List
from pydantic import BaseModel

class TiposRatingClienteBase(BaseModel):
    codigo_rating: str
    descricao_rating: str
    prob_default_inicial: float
    prob_default_final: float

class TiposRatingClienteCreate(TiposRatingClienteBase):
    pass


class TiposRatingClienteUpdate(TiposRatingClienteBase):
    pass

class TiposRatingClienteInDB(TiposRatingClienteBase):
    id: int
    id_cliente: int



class TiposRatingCliente(TiposRatingClienteInDB):
    pass
