from .session import SessionLocal
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
# from sqlalchemy.orm import sessionmaker
#
# current_dir = os.path.dirname(os.path.abspath(__file__))
# DATABASE_URL = f"sqlite:///{os.path.join(current_dir, 'test.db')}"
#
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base: DeclarativeMeta = declarative_base()
#
# # Create tables
# Base.metadata.create_all(bind=engine)
