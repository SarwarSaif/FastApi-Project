
from typing import List, Optional
from pydantic import BaseModel, BaseSettings, Field
from pydantic.networks import PostgresDsn
import os

class AppSettings(BaseModel):
    """Application configurations - extending BaseModel.
    Configs related to your application’s internal logic should either be explicitly mentioned in the same 
    configs.py or imported from a different app_configs.py file. 
    You shouldn’t pollute your .env files with the internal global variables necessitated by your application’s core logic.
    """
    APP_NAME: str = "Yandex.Cloud Netinfra API"
    APP_DESCRIPTION: str = "A bundled API for Yandex.Cloud Netinfra team tools"
    VAR_A: int = 33
    VAR_B: float = 22.0
    

#Using Pydantic to load environment variables, no need to use 'os.environ.get()'
class Settings(BaseSettings):
    """Common Environment configurations. - extending BaseSettings"""
    # These variables will be loaded from the .env file. However, if
    # there is a shell environment variable having the same name,
    # that will take precedence.
    
    APP_CONFIG: AppSettings = AppSettings()
    
    # define global variables with the Field class - will not conform to ENV prefix(DEV_/PROD_)
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")
    
     # Environment specific(DEV/PROD) variables do not need the Field class
    debug: bool = False
    debug_exceptions: bool = False
    testing: bool = False
    csrf_enabled: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    database_url: str             # = os.environ.get("DATABASE_URL")
    twitter_api_key: str          # = os.environ.get("TWITTER_API_KEY")
    twitter_api_secret_key: str   # = os.environ.get("TWITTER_API_SECRET_KEY")
    facebook_api_client_id: str   # = os.environ.get("FACEBOOK_API_CLIENT_ID")
    facebook_api_secret_key: str  # = os.environ.get("FACEBOOK_API_SECRET_KEY")
    SESSION_COOKIE_SECURE: bool = True
    SESSION_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SAMESITE: str = 'None'
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_PORT: int = 465
    MAIL_USE_TLS: bool = False
    MAIL_USE_SSL: bool = True
    mail_username: str # = os.environ.get("MAIL_USERNAME")
    mail_password: str # = os.environ.get("MAIL_PASSWORD")
    backend_cors_origins_str: str = ""  # Should be a comma-separated list of origins
    
    PG_DSN: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
    
    @property
    def backend_cors_origins(self) -> List[str]:
        return [x.strip() for x in self.backend_cors_origins_str.split(",") if x]
    
    class Config:
        env_file = ".env"
        #env_prefix = ""
        #env_file_encoding = 'utf-8'

        
class DevSettings(Settings):
    """Development configurations."""
    ENV: str = "development"
    DEVELOPMENT: bool = True
    SECRET_KEY: str = "dev_secret_asdf8980as8df9809sf6a6ds4f3435fa64" #must be in bashrc
    OAUTHLIB_INSECURE_TRANSPORT: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = True
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("DATABASE_URL")
    class Config:
        env_prefix: str = "DEV_"


class ProdSettings(Settings):
    """Production configurations."""
    class Config:
        env_prefix: str = "PROD_"
    


#using pydantic
from functools import lru_cache

@lru_cache() # if cache not used, each time request will read valae from the file which is costly
def get_settings() -> Settings:
    env_state = Settings().ENV_STATE # os.environ.get("ENV_STATE")
    if env_state == "dev":
        return DevSettings()
    elif env_state == "prod":
        return ProdSettings()
    else:
      raise ValueError("prod or dev was not found in ENV_STATE")
  
  
print(get_settings())
  
