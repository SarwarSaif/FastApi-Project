from models.database import SessionLocal
from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="DB_CONN")
# Dependency
class DbConn:
    def get_db():
        db = SessionLocal()
        try:
            yield db
        except Exception as err:
            # on rollback, the same closure of state
            # as that of commit proceeds.
            db.rollback()
            custom_logger.critical(err)
            raise err
        finally:
            db.close()
            custom_logger.info("Successfull closed the DB.")