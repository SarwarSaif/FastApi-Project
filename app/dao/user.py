from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="DAO")
from session import Base, get_dbSessionConn
from models.models import User
from .dao import Dao
from datetime import datetime
dao = Dao()
class userDao:
    def create_user(self, user):
        custom_logger.info(user)
        db_user = User(
            name=user.name,
            is_active=True,
            date=datetime.now() #datetime.utcnow
            #hashed_password=hashed_password,
        )
        # user_list=User(user)
        custom_logger.info(db_user)
        # custom_logger.info("user-> {}".format(res))
        return Dao().user_insert(db_user)
