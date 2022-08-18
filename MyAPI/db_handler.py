from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DATABASE_URL = 'mysql+pymysql://root:Abcd1234!@localhost:3306/inference_db'

db_engine =  create_engine(DATABASE_URL)
Session_Local =  sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()