from pydantic.types import conint, constr
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy import ForeignKey,inspect
from datetime import datetime

from sqlalchemy.orm import relationship, with_polymorphic
from sqlalchemy.ext.declarative import declared_attr

#from .session import Base
from common.session import Base, get_dbSessionConn


from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field, EmailStr, validator, root_validator

class User(Base):
    __tablename__ = "user"
   # __table_args__ = db.UniqueConstraint('b_id', 'e_id', name='unique_constraint_bid_eid')
   # __table_args__ = {'schema': 'my_new_schema'} #if a schema other than the default "public" schema was used
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    date = Column(DateTime)#date = Column(DateTime, default=datetime.utcnow)
    
    
    def __repr__(self):
        return "<User(id=%s name=%s, is_active=%s, date=%s)>" % (self.id, self.name, self.is_active, self.date)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_active": self.is_active,
            "date": self.date
            #"product": self.product.to_json()
        } 

    
# class UserModel(BaseModel):
#     id: int
#     name: str
#     is_active: bool
    
#     class Config:
#         orm_mode = True
        
#checkfirst=True:  will not try to create table if already exist
with get_dbSessionConn(True) as session:
    User.__table__.create(session.get_bind(), checkfirst=True)


#session = next(get_dbSessionConn()))
#engine = session.get_bind()
#User.__table__.create(engine)

# --------------- ------------ --------------- 
# create all the tables
#Base.metadata.create_all(bind=engine)

# --------------- One-to-Many --------------- 

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String(50))
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    children = relationship("Child", cascade="all", lazy='joined')  #lazy='select' / lazy='joined'
    #cascade-all means all operations such as CRUD on the parent will be cascaded to the children eg deleting a parent
    #should delete all children
    
    #def __repr__(self):
    #    return 'id: {}, e-mail address: {}'.format(self.id, self.email)

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    child_name = Column(String)
    date = Column(DateTime, default=datetime.utcnow)


with get_dbSessionConn(True) as session:
    Parent.__table__.create(session.get_bind(), checkfirst=True) 
    Child.__table__.create(session.get_bind(), checkfirst=True) 

# --------------- ------------ --------------- 
#Enity Models mapping

# class ChildModel(BaseModel):
#     #id: int
#     #parent_id: int
#     child_name: str
#     date: datetime
#     class Config:
#         orm_mode = True
        
# class ParentModel(BaseModel):
#     #id: int
#     #parent_id: int
#     email: str
#     first_name: str
#     last_name: str
#     children: List[ChildModel] = []
#     class Config:
#         orm_mode = True



# --------------- ------------ --------------- 
#Custom Models

# class CustomModel(BaseModel):
#     name: str
#     users: List[UserModel] = []
#     parents: List[ParentModel] = []
#     class Config:
#         orm_mode = True


# --------------- ------------ --------------- 
class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    employees = relationship("Person", back_populates="company", cascade="all, delete-orphan")

    def __repr__(self):
        return "Company %s" % self.name


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(ForeignKey("company.id"))
    name = Column(String(50))
    type = Column(String(50))

    company = relationship("Company", back_populates="employees")

    __mapper_args__ = {
        "polymorphic_identity": "person",
        "polymorphic_on": type,
    }

    def __repr__(self):
        return "Ordinary person %s" % self.name


class Engineer(Person):

    engineer_name = Column(String(30))
    primary_language = Column(String(30))

    # illustrate a single-inh "conflicting" column declaration;
    # see http://docs.sqlalchemy.org/en/latest/orm/extensions/
    #       declarative/inheritance.html#resolving-column-conflicts
    @declared_attr
    def status(cls):
        return Person.__table__.c.get("status", Column(String(30)))

    __mapper_args__ = {"polymorphic_identity": "engineer"}

    def __repr__(self):
        return (
            "Engineer %s, status %s, engineer_name %s, "
            "primary_language %s"
            % (
                self.name,
                self.status,
                self.engineer_name,
                self.primary_language,
            )
        )


class Manager(Person):
    manager_name = Column(String(30))

    @declared_attr
    def status(cls):
        return Person.__table__.c.get("status", Column(String(30)))

    __mapper_args__ = {"polymorphic_identity": "manager"}

    def __repr__(self):
        return "Manager %s, status %s, manager_name %s" % (
            self.name,
            self.status,
            self.manager_name,
        )
