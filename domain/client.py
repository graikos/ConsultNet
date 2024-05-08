
class Client:
    def __init__(self, name,bank_details):
        self.name = name
        self.bank_details = bank_details

client1 = Client("David White", ("David White", "IBAN1111111111"))
client2 = Client("Sophia Lee", ("Sophia Lee", "IBAN2222222222"))
client3 = Client("James Wilson", ("James Wilson", "IBAN3333333333"))

# Creating a client dictionary
client_dict = {
    "David":client1,
    "Sophia": client2,
    "James": client3
}
