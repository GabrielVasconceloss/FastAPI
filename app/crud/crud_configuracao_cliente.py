from sqlalchemy.orm import Session
from app.db.models.configuracao_cliente import ConfiguracaoCliente
from app.db.models.cliente import Cliente
from app.db.models.aprovadores_cliente import AprovadoresCliente
from app.db.models.tipos_rating_cliente import TiposRatingCliente
from app.db.models.alcadas_cliente import AlcadasCliente
from app.schemas.configuracao_cliente import ConfiguracaoClienteCreate
from sqlalchemy.orm import joinedload


def get_configuracao_cliente(db: Session, configuracao_cliente_id: int):
    return db.query(ConfiguracaoCliente).filter(ConfiguracaoCliente.id_cliente == configuracao_cliente_id).first()


def get_configuracao_cliente_join(db: Session, id_cliente: int):
    cliente = (
        db.query(Cliente)
        .options(
            joinedload(Cliente.configuracao_cliente),
            joinedload(Cliente.aprovadores_cliente),
            joinedload(Cliente.tipos_rating_cliente),
            joinedload(Cliente.alcadas_cliente),
        )
        .filter(Cliente.id == id_cliente)
        .first()
    )
    return cliente


def get_multi_configuracao_cliente(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ConfiguracaoCliente).offset(skip).limit(limit).all()


def get_configuracao_cliente_by_id_cliente(db: Session, id_cliente: int) -> ConfiguracaoCliente:
    return db.query(ConfiguracaoCliente).filter(ConfiguracaoCliente.id_cliente == id_cliente).first()


def get_configuracao_cliente_by_cliente_id(db: Session, cliente_id: int):
    return db.query(ConfiguracaoCliente).filter(ConfiguracaoCliente.id_cliente == cliente_id).first()


def create_configuracao_cliente(db: Session, obj_in: ConfiguracaoClienteCreate):
    db_configuracao_cliente = ConfiguracaoCliente(**obj_in.dict())
    db.add(db_configuracao_cliente)
    db.commit()
    db.refresh(db_configuracao_cliente)
    return db_configuracao_cliente


def update_configuracao_cliente(db: Session, db_obj: ConfiguracaoCliente, obj_in: dict):
    for key, value in obj_in.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_configuracao_cliente(db: Session, configuracao_cliente: ConfiguracaoCliente):
    db.delete(configuracao_cliente)
    db.commit()