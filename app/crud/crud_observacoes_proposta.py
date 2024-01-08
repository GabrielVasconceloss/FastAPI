from sqlalchemy.orm import Session
from app.db.models.observacoes_proposta import ObservacoesProposta
from app.crud.crud_configuracao_cliente import get_configuracao_cliente
from app.schemas.observacoes_proposta import ObservacoesPropostaCreate



def get_multi_observacoes_proposta(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ObservacoesProposta).offset(skip).limit(limit).all()

def get_all_observacoes_proposta(db: Session, id_cliente: int):
    observacoes_proposta = db.query(ObservacoesProposta).filter(ObservacoesProposta.id_cliente == id_cliente).all()
    if not observacoes_proposta:
        return None
    return observacoes_proposta


def get_all_observacoes_propostaid_contraparte(db: Session, id_cliente: int, id_contraparte_list: int):
    observacoes_proposta = db.query(ObservacoesProposta).filter(ObservacoesProposta.id_cliente == id_cliente, ObservacoesProposta.id_contraparte == id_contraparte_list).all()
    if not observacoes_proposta:
        return []
    return observacoes_proposta


def create_observacoes_proposta(db: Session, observacoes_proposta_in: ObservacoesPropostaCreate, id_cliente: int, id_contraparte: int):
    db_tipos_rating_cliente = ObservacoesProposta(id_cliente=id_cliente, id_contraparte=id_contraparte, **observacoes_proposta_in.dict())
    db.add(db_tipos_rating_cliente)
    db.commit()
    db.refresh(db_tipos_rating_cliente)
    return db_tipos_rating_cliente


def get_unic_observacoes_proposta(db: Session, id_tipo_rating: int):
    return db.query(ObservacoesProposta).filter(ObservacoesProposta.id == id_tipo_rating).first()


def update_observacoes_proposta(db: Session, db_obj: ObservacoesProposta, obj_in: dict):
    for key, value in obj_in.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_observacoes_proposta(db: Session, id_observacoes: int):
    return db.query(ObservacoesProposta).filter(ObservacoesProposta.id == id_observacoes).first()


def delete_observacoes_proposta(db: Session, tipos_rating_cliente: ObservacoesProposta):
    db.delete(tipos_rating_cliente)
    db.commit()