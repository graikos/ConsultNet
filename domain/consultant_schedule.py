class ConsultantSchedule:
    # 24 bit mask
    mask = 0xffffff
    day_map = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }

    def __init__(self) -> None:
        self.schedule = [[False for i in range(24)] for x in range(7)]

        self.exceptions = {}

    def toggle_availability(self, day_idx, hour_idx):
        self.schedule[day_idx][hour_idx] = not self.schedule[day_idx][hour_idx]

    def batch_mark_hour_availability(self, hour_idx, mark):
        for x in range(7):
            self.schedule[x][hour_idx] = mark

    def is_marked(self, day_idx, hour_idx):
        return self.schedule[day_idx][hour_idx]

    # checks if at least one day this hour slot inactive
    def check_if_one_inactive_in_row(self, hour_idx):
        for x in range(7):
            if not self.schedule[x][hour_idx]:
                return True
        return False


    def check_if_all_active_in_row(self, hour_idx):
        for x in range(7):
            if not self.schedule[x][hour_idx]:
                return False
        return True

    def add_exception(self,date_key, h1, h2):
        # all 1s, number equal to hours
        b1 = (1<<h1) - 1
        b2 = (1<<h2) - 1

        # keep in between
        new_b = b2 - b1

        try:
            old_b = self.exceptions[date_key]
            old_b ^= new_b

        except KeyError:
            self.exceptions[date_key] = new_b




