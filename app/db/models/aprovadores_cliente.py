from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.db.models.cliente import Cliente

class AprovadoresCliente(Base):
    __tablename__ = "aprovadores_cliente"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    id_cliente = Column(Integer(), ForeignKey("clientes.id"))
    cargo_aprovador = Column(String)
    login_aprovador = Column(String)
    perfil_aprovador = Column(String)
    percentual_peso_aprovador = Column(DECIMAL)

    cliente = relationship("Cliente", back_populates="aprovadores_cliente")


