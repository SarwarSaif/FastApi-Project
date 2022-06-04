from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI, echo=False
) #echo will print all statements but not time taken

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #default-reccomeded is false for both  autocommit and autoflush

Base = declarative_base()
