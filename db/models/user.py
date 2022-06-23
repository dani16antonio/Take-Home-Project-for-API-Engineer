from db.db import Base
class UserDB:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password