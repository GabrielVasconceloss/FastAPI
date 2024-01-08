from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class LimitesPropostaResponse(BaseModel):
    id: int
    id_cliente: int
    id_proposta: int
    id_contraparte: int
    tipo_limite: int
    rating: int
    valor_limite: float
    valor_carteira: float
    carteira_mwm: float

class ObservacoesPropostaResponse(BaseModel):
    id: int
    id_cliente: int
    id_proposta: int
    id_contraparte: int
    tipo_observacao: int
    observacao_vigente: str
    observacao_sugerido: str
    observacao_aprovado: str



class PropostaResponseBase(BaseModel):
    id: int
    data_aprovacao_limite: datetime
    grupo: str
    tipo_limite: int
    data_proposta: datetime
    tipo_analise: int
    status: int
    valor_utilizado_conversao: float
    proposta_response: List
    observacoes_proposta: List



class PropostaResponse(BaseModel):
    id_cliente: int
    propostas_contraparte: List[PropostaResponseBase] = []


    class Config:
        orm_mode = True
        from_orm = True





