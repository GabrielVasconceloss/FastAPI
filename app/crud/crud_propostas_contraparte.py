from sqlalchemy.orm import Session
from app.db.models.proposta_contraparte import PropostaContraparte
from app.schemas.propostas_contraparte import PropostaContraparteCreate


def get_multi_propostas_contraparte(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PropostaContraparte).offset(skip).limit(limit).all()


def get_all_propostas_contraparte(db: Session, id_cliente: int):
    propostas_contraparte = db.query(PropostaContraparte).filter(PropostaContraparte.id_cliente == id_cliente).all()
    if not propostas_contraparte:
        return None
    return propostas_contraparte

def create_propostas_contraparte(db: Session, propostas_contraparte: PropostaContraparteCreate, id_cliente: int):
    db_propostas_contraparte = PropostaContraparte(id_cliente=id_cliente, **propostas_contraparte.dict())
    db.add(db_propostas_contraparte)
    db.commit()
    db.refresh(db_propostas_contraparte)
    return db_propostas_contraparte




def get_unic_propostas_contraparte(db: Session, id_proposta: int):
        return db.query(PropostaContraparte).filter(PropostaContraparte.id == id_proposta).first()


def update_propostas_contraparte(db: Session, db_obj: PropostaContraparte, obj_in: dict):
    for key, value in obj_in.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_aprovadores_cliente(db: Session, id_proposta: int):
    return db.query(PropostaContraparte).filter(PropostaContraparte.id == id_proposta).first()


def delete_aprovadores_cliente(db: Session, aprovadores_cliente: PropostaContraparte):
    db.delete(aprovadores_cliente)
    db.commit()
