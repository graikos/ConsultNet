from datetime import datetime

class User:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.creation_date = datetime.now()

    def get_id(self):
        return self.id