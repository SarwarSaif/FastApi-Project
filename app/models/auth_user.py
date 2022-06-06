from sqlalchemy import Boolean, Column, Integer, String, DateTime
from .database import Base

### Add Authenticated User Model            
class AuthUser(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String(50))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    date = Column(DateTime)
    
    def __repr__(self):
        return "<User(id=%s username=%s, email=%s, hashed_password=%s, first_name=%s, lastname=%s, is_active=%s, is_superuser=%s, date=%s)>" % (self.id, self.username, self.email, self.hashed_password, self.first_name, self.last_name, self.is_active, self.is_superuser, self.date)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "hashed_password": self.hashed_password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
            "is_superuser": self.is_superuser,
            "date": self.date
        }
            

    