from typing import List
from pydantic import BaseModel

class ConfiguracaoClienteBase(BaseModel):
    id_cliente: int
    id_tipo_limite: int
    id_limite: int
    id_input_carteira: int
    id_conversao: int
    valor_base_proprietaria: float
    qtd_dias_validade_analise: int
    qtd_dias_intervalo_minimo_aprovacoes: int
    qtd_dias_intervalo_maximo_aprovacoes: int

class ConfiguracaoClienteCreate(ConfiguracaoClienteBase):
    pass

class ConfiguracaoClienteUpdate(ConfiguracaoClienteBase):
    pass

class ConfiguracaoClienteInDB(ConfiguracaoClienteBase):
    id: int

class ConfiguracaoCliente(ConfiguracaoClienteInDB):
    class Config:
        orm_mode = True


class ConfiguracaoCliente(BaseModel):
    id_cliente: int
    id_tipo_limite: int
    id_limite: int
    id_input_carteira: int
    id_conversao: int
    valor_base_proprietaria: float
    qtd_dias_validade_analise: int
    qtd_dias_intervalo_minimo_aprovacoes: int
    qtd_dias_intervalo_maximo_aprovacoes: int

    class Config:
        orm_mode = True