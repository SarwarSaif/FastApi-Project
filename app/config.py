import os
from sqlalchemy.engine.url import URL

### Bring my Logger
from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="CONFIG")

# from logging.config import dictConfig
# import logging
# from core.logging_conf import LogConfig
# dictConfig(LogConfig().dict())
# logger = logging.getLogger("mycoolapp")


PROJECT_NAME = "{{cookiecutter.project_name}}"

#uvicorn.run(app, host="0.0.0.0", port=8000)
LISTENING_HOST = "0.0.0.0"
LISTENING_PORT = 8000

#Schema name: public
# Database name: rwdb


# postgres_info_db = {
#     'drivername': 'postgres',
#     'username': 'postgres',
#     'password': 'postgres',
#     'host': 'localhost',
#     'port': 5432,
#     'database': 'rwdb'
# }

# #DATABASE="rwdb"
# from dataclasses import dataclass
# @dataclass
# class DBConfig2:
#     drivername: str = "postgres"
#     username: str = "postgres"
#     password: str = "postgres"
#     host: str = "localhost"
#     port: int = 5432
    
# class DBConfig3:
#     def __init__(self):
#         self.drivername = "postgres"
#         self.username = "postgres"
#         self.password = "postgres"
#         self.host = "localhost"
#         self.port = 5432
        
#     def getdb_name(self):
#         return 'rwdb'
    
#     def getdb_uri(self):
#         self.database = self.getdb_name() #append to the dict - "self.database = 'rwdb'"
#         return self
  
  
class DBConfig:
    def __init__(self):
        self.drivername = "postgres"
        self.username = "postgres"
        self.password = "postgres" # None
        
        self.database = "my_ygdb"
        #self.schema = "my_ygschema"
        
        self.host = "localhost"
        self.port = 5433
        
    def getdb_name(self):
        return self.database

    def set_dbname(self, dbname):
        self.database = dbname
    
    def getdb_uri(self):
        self.database = self.getdb_name() #append to the dict - "self.database = 'rwdb'"
        #self.schema = "scm"
        return self
  
SQLALCHEMY_URI = URL(**DBConfig().__dict__) #can manually create dict object or use "Class.__dict__"
SQLALCHEMY_DATABASE_URI = URL(**DBConfig().getdb_uri().__dict__) 
#SQLALCHEMY_DATABASE_URI = URL(**postgres_info_db) 

print(SQLALCHEMY_URI)
print(SQLALCHEMY_DATABASE_URI)
custom_logger.info("SQL Alchemy uri {}".format(SQLALCHEMY_URI))
#the Default Schema in the newly created database "rwdb" is the "public" schema
# so if no schema is indicated when running sql queries, they will be executed in the "public" schema
#SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/rwdb"


API_V1_STR = "/api/v1"




