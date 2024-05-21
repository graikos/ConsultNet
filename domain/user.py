from datetime import datetime

class User:
    u_id = 0
    def __init__(self, id, name) -> None:
        if id is None:
            self.id = User.u_id
            User.u_id += 1
        else:
            self.id = id
        self.name = name
        self.creation_date = datetime.now()

    def get_id(self):
        return self.id