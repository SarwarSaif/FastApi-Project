from config2 import Config


def get_settings():
    return Config.SQLALCHEMY_DATABASE_URI


print(get_settings())