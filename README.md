# FastApi-Project
A simple but well organized FastAPI project.

# Project Setup
#### Install the python modules and packages in the virtaul env
```
# Create Virtual Environment
python3 -m venv venv
# Activate the virtual env
source venv/bin/activate
# Check python version
which python3
# Install the requirements
pip3 install -r requirements.txt 
```
### Deploy your DB (Yugabyte)
#### Installation 
```
docker-compose -f ./docker-yb/docker-compose.yaml up -d
```
- YSQL API at localhost:5433 
- YCQL API at localhost:9042. 
- Admin Page at localhost:7000
- The yb-master admin service at 
  curl http://localhost:7000

#### Connect to YSQL
```
docker exec -it yb-tserver-n1 /home/yugabyte/bin/ysqlsh -h yb-tserver-n1
\l    			  #list databases
create database my_ygdb WITH ENCODING='UTF8'; # Create database
\c my_ygdb       #connect to the db my_ygdb
\dt  			 #list tables in that db
```
#### Connect using VSCODE
1. Add the Postgresql Extension
2. Connect the DB
    {
    "label": "my_ygdb",
    "host": "localhost",
    "user": "yugabyte",
    "port": 5433,
    "ssl": false,
    "database": "my_ygdb",
    "password": "yugabyte"
    }

### Deploy Application
```
python3 app/main.py
```

### Test the Endpoints
http://localhost:8000/docs



### Ref
https://github.com/Kludex/fastapi-microservices
https://github.com/GavriloviciEduard/fastapi-microservices
