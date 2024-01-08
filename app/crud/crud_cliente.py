from sqlalchemy.orm import Session
from app.db.models.cliente import Cliente

def get_cliente(db: Session, id: int):
    return db.query(Cliente).filter(Cliente.id == id).first()