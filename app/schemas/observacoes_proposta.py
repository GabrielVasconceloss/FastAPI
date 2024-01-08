from pydantic import BaseModel
from typing import List

class ObservacoesPropostaBase(BaseModel):
    id_cliente: int
    id_proposta: int
    id_contraparte: int
    tipo_observacao: int
    observacao_vigente: str
    observacao_sugerido: str
    observacao_aprovado: str


class ObservacoesPropostaCreate(BaseModel):
    id_proposta: int
    tipo_observacao: int
    observacao_vigente: str
    observacao_sugerido: str
    observacao_aprovado: str

class ObservacoesPropostaUpdate(ObservacoesPropostaBase):
    pass

class ObservacoesPropostaInDB(ObservacoesPropostaBase):
    id: int

    class Config:
        orm_mode = True

class ObservacoesProposta(ObservacoesPropostaInDB):
    pass