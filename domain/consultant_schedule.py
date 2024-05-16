class ConsultantSchedule:
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

