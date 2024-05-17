"""
Payment gateway interface stub
"""
from random import randint
class PaymentGatewayInterface():
    def __init__(self) -> None:
        pass

    def process_payment(self, name, num, cvv, exp, total_amount):
        return [True, randint(0, 999999999)]