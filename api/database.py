from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv('../api.env')
host = os.environ['DB_HOST']
database = os.environ['DB_NAME']
user = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=3, max_overflow=0
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
