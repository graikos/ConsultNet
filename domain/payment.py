from datetime import datetime


class Payment:
    def __init__(self, id, amount, client_id, consultant_id) -> None:
        self.id = id
        self.amount = amount
        self.client_id = client_id
        self.consultant_id = consultant_id
        self.timestamp = datetime.now()

class CoursePayment(Payment):
    def __init__(self, id, amount, client_id, consultant_id, course, add_on_idx) -> None:
        super().__init__(id, amount, client_id, consultant_id)
        self.course = course
        self.add_on_idx = add_on_idx


course_payments = []