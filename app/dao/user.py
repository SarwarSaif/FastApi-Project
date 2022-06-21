from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="DAO")
from sqlalchemy.orm import Session
from common.session import Base, get_dbSessionConn
from entities.models import User
from .dao import Dao
from datetime import datetime
import models 
from entities.models import User

class userDao:

    def find_by_name(db: Session, name: str):
        return db.query(User).filter(User.name == name).first()
    # Before creating a new user check if username already exits

    def create_user(db: Session, user: models.user.UserIn):
        # fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(
            name=user.name,
            is_active=True,
            date=datetime.now() #datetime.utcnow
            #hashed_password=hashed_password,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_all_user(db: Session, table: models.user.UserModel):
        return db.query(table).all()

    
    
