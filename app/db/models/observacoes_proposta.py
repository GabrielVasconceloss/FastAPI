from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.db.models.cliente import Cliente
from app.db.models.proposta_contraparte import PropostaContraparte

class ObservacoesProposta(Base):
    __tablename__ = "observacoes_proposta"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    id_cliente = Column(Integer(), ForeignKey("clientes.id"))
    id_proposta = Column(Integer())
    id_contraparte = Column(Integer(), ForeignKey("propostas_contraparte.id"))
    tipo_observacao = Column(Integer)
    observacao_vigente = Column(String)
    observacao_sugerido = Column(String)
    observacao_aprovado = Column(String)

    cliente = relationship("Cliente", back_populates="observacoes_proposta")
    propostas_contraparte = relationship("PropostaContraparte", back_populates="observacoes_proposta")


