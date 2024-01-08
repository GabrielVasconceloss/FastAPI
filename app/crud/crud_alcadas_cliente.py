from sqlalchemy.orm import Session
from app.db.models.alcadas_cliente import AlcadasCliente
from app.crud.crud_configuracao_cliente import get_configuracao_cliente
from app.schemas.alcadas_cliente import AlcadasClienteCreate


def create_alcadas_cliente(db: Session, alcadas_cliente: AlcadasClienteCreate, id_cliente: int, id_tipo_rating:int):
    db_aprovadores_cliente = AlcadasCliente(id_cliente=id_cliente, id_tipo_rating=id_tipo_rating, **alcadas_cliente.dict())
    db.add(db_aprovadores_cliente)
    db.commit()
    db.refresh(db_aprovadores_cliente)
    return db_aprovadores_cliente

def get_multi_alcadas_cliente(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AlcadasCliente).offset(skip).limit(limit).all()


def get_all_alcadas_cliente(db: Session, id_cliente: int):
    alcadas_cliente = db.query(AlcadasCliente).filter(AlcadasCliente.id_cliente == id_cliente).all()
    if not alcadas_cliente:
        return None
    return alcadas_cliente

def get_unic_alcadas_cliente(db: Session, id_alcadas: int):
    return db.query(AlcadasCliente).filter(AlcadasCliente.id == id_alcadas).first()


def update_alcadas_cliente(db: Session, db_obj: AlcadasCliente, obj_in: dict):
    for key, value in obj_in.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_alcadas_cliente(db: Session, id_alcadas: int):
    return db.query(AlcadasCliente).filter(AlcadasCliente.id == id_alcadas).first()


def delete_alcadas_cliente(db: Session, alcadas_cliente: AlcadasCliente):
    db.delete(alcadas_cliente)
    db.commit()
