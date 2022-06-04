from app.models.models import User, Person
from app.models.models import Parent, Child, ChildModel, ParentModel
from datetime import datetime

from app.dao import Dao




#--------------------------------
dao= Dao()

#--------------------------------
db_user = User(
            name="Sir Lewis Hamilton",
            is_active=True,
            date=datetime.now() #datetime.utcnow
            #hashed_password=hashed_password,
        )
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

parent = Parent(
            #id
            email="me@gmail.com",
            first_name="Me",
            last_name="You",
            is_active=True,
            is_superuser=True,
            hashed_password="password"
            #children=None
        )
child1 = Child(
            #id
            #parent_id
            child_name="child_name10"
            #date=
        )
child2 = Child(
            #id
            #parent_id
            child_name="child_name20"
            #date=
        )        


# <> inserting bulk
user_list=[db_user, db_user, db_user, db_user, db_user, db_user]
dao.bulk_insert(user_list)

# <> inserting a Parent with multiple children 
parent.children.extend([child1, child2]) #adding children
dao.create(parent)

# <> count
#print("xxxxxxxxx PARENT COUNT: " + str(dao.count(Parent)) + \
#    "   xxxxxxxxx CHILD COUNT: " + str(dao.count(Child)))

# <> Lazy loading count
#print("lazy loading count: " + str(len(dao.find_all(Parent.children)))) #

# <> findAll 
#print('{}{}'.format("CHILDREN SIZE: ", len(dao.find_all(Child))))

#orm find all : must use eager fetching
#print(ParentModel.from_orm(dao.find_all(Parent)[0])) #
#print(ChildModel.from_orm(dao.find_all(Child)[0]))

# <> find
#out1=dao.find_by_id(Parent, 5)


#print("xxxxxxxxvv FIND: " + out1.email)



# deletion
#dao.remove(parent)
#dao.remove_by_id(parent, 5)

#--------------------------------

# users = dao.find_all2(User)
# for user in users:
#     print(user.name + " " + user.date)

#--------------------------------

# ps = dao.find_all2(Person)
# for p in ps:
#     print(p.name + " " + p.type)
#--------------------------------




#OR
# MANUALLY INSERT DATA TO DB, TODO generate ddl file and autoload for developers
#Parent
# INSERT INTO parent (email, first_name, last_name, hashed_password, is_active, is_superuser) 
# 	VALUES ('parent1@rak.com', 'parent1_first_name', 'parent1_last_name', '1234', true, true);
	
# INSERT INTO parent (email, first_name, last_name, hashed_password, is_active, is_superuser) 
# 	VALUES ('parent2@rak.com', 'parent2_first_name', 'parent2_last_name', '1234', true, true);
	
# INSERT INTO parent (email, first_name, last_name, hashed_password, is_active, is_superuser) 
# 	VALUES ('parent3@rak.com', 'parent3_first_name', 'parent3_last_name', '1234', true, true)
	
	
# #Children
# INSERT INTO child (parent_id, child_name, "date") 
# 	VALUES (1, 'parent1_child1', CURRENT_TIMESTAMP);
# INSERT INTO child (parent_id, child_name, "date") 
# 	VALUES (1, 'parent1_child2', CURRENT_TIMESTAMP);
# INSERT INTO child (parent_id, child_name, "date") 
# 	VALUES (1, 'parent1_child3', CURRENT_TIMESTAMP);
	
# INSERT INTO child (parent_id, child_name, "date") 
# 	VALUES (2, 'parent2_child1', CURRENT_TIMESTAMP);
# INSERT INTO child (parent_id, child_name, "date") 
# 	VALUES (2, 'parent2_child2', CURRENT_TIMESTAMP);
	
# INSERT INTO child (parent_id, child_name, "date") 
# 	VALUES (3, 'parent3_child1', CURRENT_TIMESTAMP)	