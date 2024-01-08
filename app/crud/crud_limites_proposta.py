from sqlalchemy.orm import Session
from app.db.models.limites_proposta import LimitesProposta
from app.crud.crud_configuracao_cliente import get_configuracao_cliente
from app.schemas.limites_proposta import LimitesPropostaCreate




def get_multi_limites_proposta(db: Session, skip: int = 0, limit: int = 10):
    return db.query(LimitesProposta).offset(skip).limit(limit).all()

def get_all_limites_proposta(db: Session, id_cliente: int):
    limites_proposta = db.query(LimitesProposta).filter(LimitesProposta.id_cliente == id_cliente).all()
    if not limites_proposta:
        return None
    return limites_proposta

def create_limites_proposta(db: Session, limites_proposta: LimitesPropostaCreate, id_cliente: int, id_contraparte: int):
    db_aprovadores_cliente = LimitesProposta(id_cliente=id_cliente, id_contraparte=id_contraparte,**limites_proposta.dict())
    db.add(db_aprovadores_cliente)
    db.commit()
    db.refresh(db_aprovadores_cliente)
    return db_aprovadores_cliente

def get_limites_proposta(db: Session, id_aprovador: int):
    return db.query(LimitesProposta).filter(LimitesProposta.id == id_aprovador).first()


def get_unic_limites_proposta(db: Session, id_limites: int):
    return db.query(LimitesProposta).filter(LimitesProposta.id == id_limites).first()

def update_limites_proposta(db: Session, db_obj: LimitesProposta, obj_in: dict):
    for key, value in obj_in.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_limites_proposta(db: Session, aprovadores_cliente: LimitesProposta):
    db.delete(aprovadores_cliente)
    db.commit()
