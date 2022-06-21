import models
from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="DAO")
from sqlalchemy.orm import Session
from common.session import Base, get_dbSessionConn
from entities.models import User
from .dao import Dao
from datetime import datetime
import models 
from entities.auth_user import AuthUser
from lib.hasher import Hasher

import bcrypt
class AuthUserDao:

    def find_by_username(db: Session, name: str):
        return db.query(AuthUser).filter(AuthUser.username == name).first()
    # Before creating a new user check if username already exits

    def create_auth_user(db: Session, user: models.auth_user.AuthUserModelIn):
        # fake_hashed_password = user.password + "notreallyhashed"
        custom_logger.info(user.password1)
        hasherObj = Hasher()
        hashed_password = hasherObj.get_password_hash(user.password1)
        db_user = AuthUser(
            username=user.username,
            email=user.email_address,
            hashed_password=hashed_password,
            first_name=user.first_name,
            last_name=user.last_name,
            is_active=True,
            is_superuser=False,
            date=datetime.now() #datetime.utcnow
            #hashed_password=hashed_password,
        )
        custom_logger.debug(db_user)
        # db.add(db_user)
        # db.commit()
        # db.refresh(db_user)
        return db_user

    def get_all_user(db: Session, table: models.user.UserModel):
        return db.query(table).all()

    
    
