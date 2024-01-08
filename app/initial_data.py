from app.db.models.configuracao_cliente import ConfiguracaoCliente
from app.db.models.alcadas_cliente import AlcadasCliente
from app.db.models.aprovadores_cliente import AprovadoresCliente
from app.db.models.tipos_rating_cliente import TiposRatingCliente
from app.db.models.proposta_contraparte import PropostaContraparte
from app.db.models.cliente import Cliente

def create_cliente(db_session, data):
    db_cliente = Cliente(**data)
    db_session.add(db_cliente)
    db_session.commit()
    db_session.refresh(db_cliente)
    return db_cliente

def create_configuracao_cliente(db_session, data):
    db_configuracao_cliente = ConfiguracaoCliente(**data)
    db_session.add(db_configuracao_cliente)
    db_session.commit()
    db_session.refresh(db_configuracao_cliente)
    return db_configuracao_cliente

def create_aprovadores_cliente(db_session, data):
    db_aprovadores_cliente = AprovadoresCliente(**data)
    db_session.add(db_aprovadores_cliente)
    db_session.commit()
    db_session.refresh(db_aprovadores_cliente)
    return db_aprovadores_cliente

def create_tipos_rating_cliente(db_session, data):
    db_tipos_rating_cliente = TiposRatingCliente(**data)
    db_session.add(db_tipos_rating_cliente)
    db_session.commit()
    db_session.refresh(db_tipos_rating_cliente)
    return db_tipos_rating_cliente

def create_alcadas_cliente(db_session, data):
    db_alcadas_cliente = AlcadasCliente(**data)
    db_session.add(db_alcadas_cliente)
    db_session.commit()
    db_session.refresh(db_alcadas_cliente)
    return db_alcadas_cliente

def create_propostas_contrapartee(db_session, data):
    db_propostas_contrapartee = PropostaContraparte(**data)
    db_session.add(db_propostas_contrapartee)
    db_session.commit()
    db_session.refresh(db_propostas_contrapartee)
    return db_propostas_contrapartee



