# IMPORT 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE URL
DATABASE_URL = "mysql+pymysql://root:1410@localhost/pets"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)