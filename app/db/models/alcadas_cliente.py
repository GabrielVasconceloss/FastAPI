from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db.models.cliente import Cliente

from app.db.base_class import Base

class AlcadasCliente(Base):
    __tablename__ = "alcadas_cliente"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_cliente = Column(Integer(), ForeignKey("clientes.id"))
    id_tipo_rating = Column(Integer(), ForeignKey("tipos_rating_cliente.id"))
    limite_minimo_aprovacao = Column(DECIMAL)
    limite_maximo_aprovacao = Column(DECIMAL)
    perfil_aprovador = Column(String)
    percentual_aprovacao = Column(DECIMAL)

    cliente = relationship("Cliente", back_populates="alcadas_cliente")
    tipos_rating_cliente = relationship("TiposRatingCliente", back_populates="alcadas_cliente")