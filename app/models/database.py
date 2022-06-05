from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="DB_ENGINE")
from core import config
import time
from sqlalchemy import event
from sqlalchemy.engine import Engine
@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    conn.info.setdefault('query_start_time', []).append(time.time())
    custom_logger.info("Start Query: %s" % statement)

@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    custom_logger.info("Query Complete!")
    custom_logger.info("Total Time: %f" % total)
    
engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI, echo=False
) #echo will print all statements but not time taken

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #default-reccomeded is false for both  autocommit and autoflush

Base = declarative_base()
