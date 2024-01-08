from typing import List, Optional
from pydantic import BaseModel

class AprovadoresClienteResponse(BaseModel):
    cargo_aprovador: str
    login_aprovador: str
    perfil_aprovador: str
    percentual_peso_aprovador: float

class TiposRatingClienteResponse(BaseModel):
    codigo_rating: str
    descricao_rating: str
    prob_default_inicial: float
    prob_default_final: float

class AlcadasClienteResponse(BaseModel):
    limite_minimo_aprovacao: float
    limite_maximo_aprovacao: float
    perfil_aprovador: str
    percentual_aprovacao: float

class ConfiguracaoClienteBase(BaseModel):
    id_tipo_limite: int
    id_limite: int
    id_input_carteira: int
    id_conversao: int
    valor_base_proprietaria: float
    qtd_dias_validade_analise: int
    qtd_dias_intervalo_minimo_aprovacoes: int
    qtd_dias_intervalo_maximo_aprovacoes: int


class ClienteResponseBase(BaseModel):
    id_tipo_limite: int
    id_limite: int
    id_input_carteira: int
    id_conversao: int
    valor_base_proprietaria: float
    qtd_dias_validade_analise: int
    qtd_dias_intervalo_minimo_aprovacoes: int
    qtd_dias_intervalo_maximo_aprovacoes: int
    aprovadores_cliente: List[AprovadoresClienteResponse] = []
    tipos_rating_cliente: List[TiposRatingClienteResponse] = []
    alcadas_cliente: List[AlcadasClienteResponse] = []

    class Config:
        orm_mode = True
        from_orm = True

class ClienteResponse(BaseModel):
    id: int
    configuracao_cliente: ClienteResponseBase

    class Config:
        orm_mode = True
        from_orm = True

