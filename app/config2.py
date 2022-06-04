#settings.py
#load .env to enviromnent variables on the machine
from dotenv import load_dotenv
load_dotenv(verbose=True) #load_dotenv()


#config.py
import os
class Settings(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
    TWITTER_API_SECRET_KEY = os.environ.get("TWITTER_API_SECRET_KEY")
    FACEBOOK_API_CLIENT_ID = os.environ.get("FACEBOOK_API_CLIENT_ID")
    FACEBOOK_API_SECRET_KEY = os.environ.get("FACEBOOK_API_SECRET_KEY")
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProductionSettings(Settings):
    DEBUG = False
    SECRET_KEY = "prod_secret_asdf8980as8df9809sf6a6ds4f3435fa64" #must be in bashrc
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentSettings(Settings):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = "dev_secret_asdf8980as8df9809sf6a6ds4f3435fa64" #must be in bashrc
    OAUTHLIB_INSECURE_TRANSPORT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    

#_________________________________________________________
###settings.py
###load .env
# from dotenv import load_dotenv
# load_dotenv(verbose=True) 

def get_settings2():
    env_state = (os.environ.get("ENV_STATE"))
    if env_state == "dev":
        return DevelopmentSettings()
    elif env_state == "prod":
        return ProductionSettings()
    else:
      raise ValueError("prod or dev was not found in ENV_STATE")
  

print(get_settings2().SECRET_KEY)
print(get_settings2())

#Set in bashrc file for permnanent or execute in terminal for testing
#export ENV_STATE='prod'
#export ENV_STATE='dev'


