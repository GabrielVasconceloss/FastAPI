from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db.models.cliente import Cliente

from app.db.base_class import Base

class TiposRatingCliente(Base):
    __tablename__ = "tipos_rating_cliente"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_cliente = Column(Integer(), ForeignKey("clientes.id"))
    codigo_rating = Column(String)
    descricao_rating = Column(String)
    prob_default_inicial = Column(DECIMAL)
    prob_default_final = Column(DECIMAL)

    cliente = relationship("Cliente", back_populates="tipos_rating_cliente")
    alcadas_cliente = relationship("AlcadasCliente", back_populates="tipos_rating_cliente")
