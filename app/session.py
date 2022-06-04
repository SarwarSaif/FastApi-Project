import imp
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from app.core import config
import config
from contextlib import contextmanager
#THIS MODULE SHOULD BE GLOBAL, just like CONFIG file



def create_db_if_not_exist():
    engine = create_engine(config.SQLALCHEMY_URI, echo=False)                          
    existing_databases = engine.execute("SELECT datname FROM pg_database;")
    
    # Results are a list of single item tuples, so unpack each tuple
    existing_databases = [d[0] for d in existing_databases]

    #created_database = False
    db_name = config.DBConfig().getdb_name()
    
    if db_name not in existing_databases:
        with engine.connect() as conn:
            conn = engine.connect()
            conn.execute('commit')
            #conn.execute("SELECT 'CREATE DATABASE rwdb' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'rwdb')")
            conn.execute("CREATE DATABASE {0};".format(db_name))
            print("****** Created database {0}".format(db_name))
            #created_database = True
    #return created_database

create_db_if_not_exist()

#Drop DB by 
# dropdb rwdb
# ----------------------------------------------------------------------------------
#TODO
# where to put INIT
import time
from sqlalchemy import event
from sqlalchemy.engine import Engine
@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    conn.info.setdefault('query_start_time', []).append(time.time())
    print("Start Query: %s" % statement)

@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    print("Query Complete!")
    print("Total Time: %f" % total)
    

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=False) #echo will print all statements but not time taken
#engine = create_engine('postgresql://{0}:{1}@{2}:{3}/{4}'.format(config.db_user, config.db_password, config.db_host, config.db_port, config.database)) 




# ----------------------------------------------------------------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #default-reccomeded is false for both  autocommit and autoflush
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False) 
#If your app is multithreaded, we recommend making sure the Session in use is local to...something. 
# scoped_session() by default makes it local to the current thread. 
# In a web app, local to the request is in fact even better. 
#"create new Session on request start" idea continues to look like the most straightforward way to keep things straight.
# TODO: might bet better to move "sessionmaker" inside th efunction "get_dbSessionConn"
# https://stackoverflow.com/questions/12223335/sqlalchemy-creating-vs-reusing-a-session

 
Base = declarative_base()
Base.metadata.schema = 'public' #everything working without it //TODO read about it and move it to config file

#Base.metadata.create_all(engine)


#Must read -->  https://docs.sqlalchemy.org/en/13/orm/session_basics.html
# Session.commit() is used to commit the current transaction. 
# It always issues Session.flush() beforehand to flush any remaining state to the database; this is independent of the “autoflush” setting. 
# If no transaction is present, it raises an error. 
# Note that the default behavior of the Session is that a “transaction” is always present; 
# This behavior can be disabled by setting autocommit=True. 
# In autocommit mode, a transaction can be initiated by calling the Session.begin() method.
@contextmanager
def get_dbSessionConn(with_commit):
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session
        #session.expunge_all()
        if with_commit:
            session.commit()
        
        # commit.  The pending changes above
        # are flushed via flush(), the Transaction
        # is committed, the Connection object closed
        # and discarded, the underlying DBAPI connection
        # returned to the connection pool.

        #The call to Session.commit() is optional, and is only needed if the work we’ve done with 
        #the Session includes new data to be persisted to the database. 
        #If we were only issuing SELECT calls and did not need to write any changes, 
        #then the call to Session.commit() would be unnecessary.
    #except gevent.Timeout:
    #    session.invalidate()
    #    raise
    except:
        # on rollback, the same closure of state
        # as that of commit proceeds.
        session.rollback()
        raise
    finally:
        # close the Session.  This will expunge any remaining
        # objects as well as reset any existing SessionTransaction
        # state.  Neither of these steps are usually essential.
        # However, if the commit() or rollback() itself experienced
        # an unanticipated internal failure (such as due to a mis-behaved
        # user-defined event handler), .close() will ensure that
        # invalid state is removed.
        session.close()

#session.expunge_all()
# #If you want a bunch of objects produced by querying a session to be usable outside the scope of the session, you need to expunge them
#The close() method issues a expunge_all(), and releases any transactional/connection resources.

