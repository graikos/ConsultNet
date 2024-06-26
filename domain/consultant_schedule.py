from datetime import datetime


# NOTE: maybe add cleanup of past appointment slots
class ConsultantSchedule:
    # 24 bit mask
    mask = 0xFFFFFF
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
        self.appointment_slots = {}

    def toggle_availability(self, day_idx, hour_idx):
        self.schedule[day_idx][hour_idx] = not self.schedule[day_idx][hour_idx]

    def batch_mark_hour_availability(self, hour_idx, mark):
        for x in range(7):
            self.schedule[x][hour_idx] = mark

    def is_marked_available(self, day_idx, hour_idx):
        return self.schedule[day_idx][hour_idx]

    def is_marked_available_consider_exception(self, date_key, hour_idx):
        # if appointment has been made for this, slot not available
        if (date_key + (hour_idx,)) in self.appointment_slots:
            return False
        wd = datetime(*date_key).weekday()
        normal_mark = self.is_marked_available(wd, hour_idx)
        try:
            # check if exception exists for this date and hour
            exc = self.exceptions[date_key]
        except KeyError:
            # if no exception, return normal mark
            return normal_mark

        # if exception exists for this date and hour, inverse the normal_mark
        return not normal_mark if exc & (1 << hour_idx) != 0 else normal_mark

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

    def add_exception(self, date_key, h1, h2):
        # all 1s, number equal to hours
        b1 = (1 << h1) - 1
        b2 = (1 << h2) - 1

        # keep in between
        new_b = b2 - b1

        try:
            self.exceptions[date_key] |= new_b

        except KeyError:
            self.exceptions[date_key] = new_b

    def add_appointment(self, slots):
        for k, v in slots.items():
            if k in self.appointment_slots:
                continue
            self.appointment_slots[k] = v


schedule1 = ConsultantSchedule()
schedule1.toggle_availability(ConsultantSchedule.day_map["monday"], 0)
schedule1.toggle_availability(ConsultantSchedule.day_map["monday"], 1)
schedule1.toggle_availability(ConsultantSchedule.day_map["monday"], 2)
schedule1.toggle_availability(ConsultantSchedule.day_map["monday"], 3)
schedule1.toggle_availability(ConsultantSchedule.day_map["tuesday"], 3)
schedule1.toggle_availability(ConsultantSchedule.day_map["tuesday"], 3)
schedule1.toggle_availability(ConsultantSchedule.day_map["tuesday"], 4)
schedule1.toggle_availability(ConsultantSchedule.day_map["tuesday"], 5)

schedule1.add_exception((2024, 5, 25), 8, 15)
