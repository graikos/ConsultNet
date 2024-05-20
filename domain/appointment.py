from domain.client import Client
from domain.payment import Payment

class Appointment:

    def __init__(self, payment, client, consultant, type, hours) -> None:
        self.payment = payment
        self.client = client
        self.consultant = consultant
        self.type = type
        self.hours = hours


appointments = []