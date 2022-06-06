
import bcrypt

class Hasher:
    def __init__(self) -> None:
        self.salt = bcrypt.gensalt()

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password
