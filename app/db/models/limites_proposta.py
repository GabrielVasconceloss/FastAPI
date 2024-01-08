from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.db.models.cliente import Cliente
from app.db.models.proposta_contraparte import PropostaContraparte

class LimitesProposta(Base):
    __tablename__ = "limites_proposta"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    id_cliente = Column(Integer(), ForeignKey("clientes.id"))
    id_proposta = Column(Integer())
    id_contraparte = Column(Integer(), ForeignKey("propostas_contraparte.id"))
    tipo_limite = Column(Integer)
    rating = Column(String)
    valor_limite = Column(DECIMAL)
    valor_carteira = Column(DECIMAL)
    carteira_mwm = Column(DECIMAL)

    cliente = relationship("Cliente", back_populates="limites_proposta")
    propostas_contraparte = relationship("PropostaContraparte", back_populates="limites_proposta")