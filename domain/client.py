from domain.user import User


class Client(User):
    def __init__(self, name, id=None):
        super().__init__(id, name)


client1 = Client("David White")
client2 = Client("Sophia Lee")
client3 = Client("James Wilson")
client_dict = {"David": client1, "Sophia": client2, "James": client3}
