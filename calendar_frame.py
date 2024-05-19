import ttkbootstrap as ttk
import tkinter as tk
from domain.consultant_schedule import ConsultantSchedule


class CalendarFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.consultant_schedule = ConsultantSchedule()

        self.slot_labels = []
        self.batch_checkboxes = []
        self.batch_vars = []
        self.active_batch = [False for x in range(24)]

        self.create_widgets()

    def toggle_slot_widget(self, widget, day_idx, hour_idx):
        is_active = self.consultant_schedule.is_marked_available(day_idx, hour_idx)
        widget.configure(style=("Custom3.TButton" if not is_active else "Custom.TLabel"))
        self.consultant_schedule.toggle_availability(day_idx, hour_idx)

        self.batch_vars[hour_idx] = False
        self.active_batch[hour_idx] = True
        self.batch_checkboxes[hour_idx].state(["!selected"])

        if self.consultant_schedule.check_if_all_active_in_row(hour_idx):
            self.active_batch[hour_idx] = True
            self.batch_vars[hour_idx] = 1
            self.batch_checkboxes[hour_idx].state(["selected"])



    def create_widgets(self):
        intro2_label = ttk.Label(
            master=self, text="Available Hours", font="Montserrat 16 bold"
        )
        intro2_label.pack(pady=(40, 10))

        # Create a frame for the schedule selection
        schedule_frame = ttk.Frame(self)
        schedule_frame.pack(pady=10)


        style = ttk.Style()
        style.configure("Custom3.TButton", background="#8C2F39", foreground="white")
        # Add labels for days of the week
        days_of_week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        style.configure(
            "Custom.TLabel",
            borderwidth=1,
            relief="solid",
            padding=7,
            background="#FFFFFF",
            foreground="#000000",
            font=("Montserrat", 7),
            anchor="center",
        )

        # Create a custom style for rounded borders
        # Add labels for each hour and day
        for day in range(7):
            self.slot_labels.append([])
            for hour in range(24):
                hour_text = f"{hour}:00 - {hour+1}:00"
                label = ttk.Label(schedule_frame, text=hour_text, style="Custom.TLabel", cursor="hand2")
                label.bind("<Button-1>", lambda e, day=day, hour=hour: self.toggle_slot_widget(e.widget, day, hour))
                label.grid(row=hour + 1, column=day + 1, padx=15, pady=2, ipadx=25)
                self.slot_labels[day].append(label)

        for day, day_name in enumerate(days_of_week):
            day_label = ttk.Label(schedule_frame, text=day_name, font=("Montserrat", 7))
            day_label.grid(row=0, column=day + 1, padx=15, pady=2)

        # Add a label for "Batch Select"
        batch_select_label = ttk.Label(
            schedule_frame, text="Batch Select", font=("Montserrat", 7)
        )
        batch_select_label.grid(row=0, column=0, padx=2, pady=2)

        # Add checkboxes for batch selection
        for hour in range(24):
            batch_var = ttk.IntVar()
            batch_checkbox = ttk.Checkbutton(
                schedule_frame,
                text="",
                command=lambda hour=hour: self.batch_select_row(hour),
                variable=batch_var,
                onvalue=1,
                offvalue=0,
            )
            batch_checkbox.grid(row=hour + 1, column=0, padx=2, pady=2)
            batch_checkbox.state(["!alternate"])
            self.batch_checkboxes.append(batch_checkbox)
            self.batch_vars.append(batch_var)

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()

    def batch_select_row(self, hour_idx):
        should_activate = self.consultant_schedule.check_if_one_inactive_in_row(hour_idx)
        self.consultant_schedule.batch_mark_hour_availability(hour_idx, should_activate)
        st = "Custom3.TButton" if should_activate else "Custom.TLabel"
        self.active_batch[hour_idx] = not self.active_batch[hour_idx]

        for x in range(7):
            self.slot_labels[x][hour_idx].configure(style=st)

