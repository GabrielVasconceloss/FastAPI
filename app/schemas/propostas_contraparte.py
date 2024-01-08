from pydantic import BaseModel
from typing import List
from datetime import datetime

class PropostaContraparteBase(BaseModel):
    data_aprovacao_limite: datetime
    grupo: str
    tipo_limite: int
    data_proposta: datetime
    tipo_analise: int
    status: int
    valor_utilizado_conversao: float

class PropostaContraparteCreate(BaseModel):
    data_aprovacao_limite: datetime
    grupo: str
    tipo_limite: int
    data_proposta: datetime
    tipo_analise: int
    status: int
    valor_utilizado_conversao: float

class PropostaContraparteUpdate(PropostaContraparteBase):
    pass

class PropostaContraparteInDB(PropostaContraparteBase):
    id: int
    id_cliente: int


class PropostaContraparte(PropostaContraparteInDB):
    pass