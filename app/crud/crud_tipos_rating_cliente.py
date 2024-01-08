from sqlalchemy.orm import Session
from app.db.models.tipos_rating_cliente import TiposRatingCliente
from app.schemas.tipos_rating_cliente import TiposRatingClienteCreate


def create_tipos_rating_cliente(db: Session, tipos_rating_cliente_in: TiposRatingClienteCreate, id_cliente: int):
    db_tipos_rating_cliente = TiposRatingCliente(id_cliente=id_cliente, **tipos_rating_cliente_in.dict())
    db.add(db_tipos_rating_cliente)
    db.commit()
    db.refresh(db_tipos_rating_cliente)
    return db_tipos_rating_cliente


def get_multi_tipos_rating_cliente(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TiposRatingCliente).offset(skip).limit(limit).all()


def get_all_tipos_rating_cliente(db: Session, id_cliente: int):
    aprovadores_cliente = db.query(TiposRatingCliente).filter(TiposRatingCliente.id_cliente == id_cliente).all()
    if not aprovadores_cliente:
        return None
    return aprovadores_cliente


def get_unic_tipos_rating_cliente(db: Session, id_tipo_rating: int):
    return db.query(TiposRatingCliente).filter(TiposRatingCliente.id == id_tipo_rating).first()


def update_tipos_rating_cliente(db: Session, db_obj: TiposRatingCliente, obj_in: dict):
    for key, value in obj_in.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_tipos_rating_cliente(db: Session, id_tipo_rating: int):
    return db.query(TiposRatingCliente).filter(TiposRatingCliente.id == id_tipo_rating).first()


def delete_tipos_rating_cliente(db: Session, tipos_rating_cliente: TiposRatingCliente):
    db.delete(tipos_rating_cliente)
    db.commit()

