from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, false
from app.db.models.cliente import Cliente

from app.db.base_class import Base

class PropostaContraparte(Base):
    __tablename__ = "propostas_contraparte"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_cliente = Column(Integer(), ForeignKey("clientes.id"))
    id_contraparte = Column(Integer)
    data_aprovacao_limite = Column(DateTime(timezone=False), nullable=True)
    grupo = Column(String)
    tipo_limite = Column(Integer)
    data_proposta = Column(DateTime(timezone=False), server_default=func.now(), nullable=True)
    tipo_analise = Column(Integer)
    status = Column(Integer)
    valor_utilizado_conversao = Column(DECIMAL)

    cliente = relationship("Cliente", back_populates="propostas_contraparte")
    proposta = relationship("Proposta", back_populates="propostas_contraparte")
    limites_proposta = relationship("LimitesProposta", back_populates="propostas_contraparte")
    observacoes_proposta = relationship("ObservacoesProposta", back_populates="propostas_contraparte")