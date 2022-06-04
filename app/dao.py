from error_code import ErrorCode
from coreException import CoreException
from sqlalchemy.orm import Session
import typing as t
import copy

#from . import models, schemas
from models.models import User, Parent
from session import Base, get_dbSessionConn


class Dao:

    def __init__(self):
        self.dbSessionConn = get_dbSessionConn(True)
        
    def drop_all(self):
        """ destroys the whole database
        """
        with get_dbSessionConn(True) as session:
            engine = session.get_bind()
            return Base.metadata.drop_all(engine)
    #drop_all(None)
    
    def create_all(self):
        """ create all the tables in this database
        """
        with get_dbSessionConn(True) as session:
            engine = session.get_bind()
            return Base.metadata.create_all(engine)

    # def drop_table(self, Model):
    #     """ Attempts to drop the specified table from db 
    #     """
    #     Model.__table__.drop(self.engine)
    
    
    def count(self, T) -> int: #count()    
        with get_dbSessionConn(False) as session:
            return session.query(T).count()  #must use generic

    # Python is not statically typed.
    # Python is dynamic so it does not need generics.
    def find_all(self, T): #findAll() 
        #10/0 
        #open("demofile.txt", "r") 
        #raise FileNotFoundError("This is not a file")  
        #raise CoreException(ErrorCode.B2002)
        with get_dbSessionConn(False) as session:
            return session.query(T).all()  #must use generic

    #def find_one()
    ##Return an instance based on the given primary key identifier, or None if not found.
    def find_by_id(self, T, id):
        with get_dbSessionConn(False) as session:
            t = session.query(T).get(id) #query(T).filter(T.id == id).first()
            #print(">>>>>>>" + t.email)
            if not t: #if None
                print("TODO: handle no item exist")#   raise HTTPException(status_code=404, detail="User not found")
            #if session.query(t.exists()):
            #    print("EXIST")
            #session.expunge_all() #no need to call commit- since commit will be called in the backend, using this as walkaround
            return t
            
    #def find_by_xyz query(T).filter(T.name == name)
    #def merge

    #def find(self, t): see if find by obkect exist

    def get_user_by_email(self, email: str) -> User:
        return self.dbSessionConn.query(User).filter(User.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100) -> t.List[User]: #findRange()
        return self.dbSessionConn.query(User).offset(skip).limit(limit).all()




    def create(self, t):
        #kind of like detaching the object, TODO: use out of the box detach
        t2 = copy.deepcopy(t)
        with get_dbSessionConn(True) as session:
            session.add(t2)
            session.flush()
            session.refresh(t2)
            return t2
        
    def bulk_insert(self, records):
        """ performs a bulk insert on a list of records 
        
        Arguments:
            records {list} -- obj records in list of dicts format 
        """
        with get_dbSessionConn(True) as session:
            session.bulk_save_objects(records)

#TODO
# session.add_all(order_list)
#   session.commit()


    #dao.query(User).all() #.first() .delete()
    def remove(self, t):
        t1 = copy.deepcopy(t)
        with get_dbSessionConn(True) as session:
            #session.query(Parent).filter(Parent.id == 5)
            tr = session.query(type(t)).get(t.id) #.get(t.id)
            # if not user:
            #raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found") #TODO
            session.delete(tr)
            return t1


   

    def remove_by_id(self, t, id):
        t = self.find(t, id)
        # if not user: #TODO: search standard result or exception type if DB dont find result
        #     raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found") 
        #q = session.query(User).filter(User.name == 'fred')
        #session.query(q.exists())
        with get_dbSessionConn(True) as session:
            session.delete(t)
            return t


    #delete_all
    #session.query(Model).delete()
    

    #merge
#     Session.merge() examines the primary key attributes of the source instance, and attempts to reconcile it with an instance of the same primary key in the session. If not found locally, it attempts to load the object from the database based on primary key, and if none can be located, creates a new instance. The state of each attribute on the source instance is then copied to the target instance. The resulting target instance is then returned by the method; the original source instance is left unmodified, and un-associated with the Session if not already.

# This operation cascades to associated instances if the association is mapped with cascade="merge".




 


    def edit_user(self, user_id: int, user: User) -> User:
        db_user = find(self.dbSessionConn, user_id)
        # if not db_user:
        #     raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
        update_data = user.dict(exclude_unset=True)


        for key, value in update_data.items():
            setattr(db_user, key, value)

        self.dbSessionConn.add(db_user)
       # session.flush()
        self.dbSessionConn.commit()
        self.dbSessionConn.refresh(db_user)
        return db_user

#------------------------------------------------------
#q = Query([User, Address], session=some_session)
    #The above is equivalent to:
#q = some_session.query(User, Address)
#------------------------------------------------------

    #  item1 = session.query(Item).get(1)

    # # second query.  the same Connection/Transaction
    # # are used.
    # item2 = session.query(Item).get(2)

    # # pending changes are created.
    # item1.foo = 'bar'
    # item2.bar = 'foo'

    # session.commit() #will update objects in the DB


# int count()
# List<T> findRange(int[] range)
# remove(T entity)
# void edit(T entity) 
# void create(T entity)
# List<T> findAll()
# T find(Object id)

#   public T merge(T entity) 

#  public T edit(T entity) {
#         T dbObject = find(getId(entity));
#         return edit(entity, dbObject);
#     }

#   public Object getId(T entity) {
#         return getEntityManager().getEntityManagerFactory().getPersistenceUnitUtil().getIdentifier(entity);
#     }


#   public void detach(T entity) {
#         getEntityManager().detach(entity);

    # public String getTableName() {
    #     Table annotation = this.entityClass.getAnnotation(Table.class);
    #     return annotation.name();
    # }

    # sqlAlchemy ORM
    #sqlalchemy.orm.query.Query.group_by(*criterion)

    #q = session.query(User).join(User.addresses)
    #q = session.query(User).join(Address)
    #q = session.query(User).join(Address, User.id==Address.user_id)
    #q = session.query(User).join(Address, User.addresses)

    #sqlalchemy.orm.query.Query.having(criterion)
    #q = session.query(User.id).join(User.addresses).group_by(User.id).having(func.count(Address.id) > 2)
    #sqlalchemy.orm.query.Query.intersect_all(*q)
    # Query.union().
    #sqlalchemy.orm.query.Query.order_by
    #sqlalchemy.orm.query.Query.outerjoin(*props, **kwargs)¶


    # sqlalchemy.orm.query.Query.limit(limit)
    #Query.first()

    # sqlalchemy.orm.query.Query.one() 
         #Return exactly one result or NoResultFound execption if the query selects no rows.
         #MultipleResultsFound if multiple object identities

    #sqlalchemy.orm.query.Query.one_or_none()
            #Returns None if the query selects no rows. 
            # Raises sqlalchemy.orm.exc.MultipleResultsFound if multiple object