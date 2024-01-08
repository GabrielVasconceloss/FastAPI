from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from app.db.base_class import Base
from app.db.models.cliente import Cliente


class ConfiguracaoCliente(Base):
    __tablename__ = "configuracao_cliente"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_cliente = Column(Integer(), ForeignKey("clientes.id"))
    id_tipo_limite = Column(Integer)
    id_limite = Column(Integer)
    id_input_carteira = Column(Integer)
    id_conversao = Column(Integer)
    valor_base_proprietaria = Column(DECIMAL)
    qtd_dias_validade_analise = Column(Integer)
    qtd_dias_intervalo_minimo_aprovacoes = Column(Integer)
    qtd_dias_intervalo_maximo_aprovacoes = Column(Integer)

    cliente = relationship("Cliente", back_populates="configuracao_cliente")


