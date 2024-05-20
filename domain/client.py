from domain.user import User


class Client(User):
    def __init__(self, id, name):
        super().__init__(id, name)
