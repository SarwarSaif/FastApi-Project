from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="DAO")
from sqlalchemy.orm import Session
from session import Base, get_dbSessionConn
from models.models import User
from .dao import Dao
from datetime import datetime
from models import schemas
from models.auth_user import AuthUser

class AuthUserDao:

    def find_by_username(db: Session, name: str):
        return db.query(AuthUser).filter(AuthUser.username == name).first()
    # Before creating a new user check if username already exits

    def create_auth_user(db: Session, user: schemas.user.UserIn):
        # fake_hashed_password = user.password + "notreallyhashed"
        db_user = AuthUser(
            usernamename=user.username,
            is_active=True,
            date=datetime.now() #datetime.utcnow
            #hashed_password=hashed_password,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_all_user(db: Session, table: schemas.user.UserModel):
        return db.query(table).all()

    
    
