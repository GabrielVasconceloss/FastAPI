from app.db import SessionLocal, engine
from app.db.base_class import Base
from app.initial_data import create_configuracao_cliente
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Criando as tabelas no PostgreSQL...")
Base.metadata.create_all(bind=engine)
logger.info("Tabelas criadas com sucesso.")

db = SessionLocal()
