import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from datetime import datetime
from dateutil.relativedelta import relativedelta
from YearChangerFrame import YearChangerFrame
from payment_details import PaymentInfoFrame
from domain.consultant import CURRENT_USER
import time


class ScheduleAppointmentPage(ttk.Frame):
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    def __init__(
        self,
        master,
        consultant=None,
        router=None,
        controller=None,
        context=None,
        **kwargs,
    ):
        super().__init__(master, **kwargs)

        try:
            if context is None:
                raise ValueError
            self.consultant = context["consultant"]
        except (KeyError, ValueError):
            self.consultant = consultant

        self.controller = controller
        self.router = router
        self.selected_slots = {}
        self.running_total = 0.0

        self.create_widgets()

    def create_widgets(self):

        logo_frame = ttk.Frame(master=self)
        label1 = ttk.Label(
            master=logo_frame,
            text="Consult",
            font="Montserrat 24 bold",
            foreground="#080708",
        )
        label2 = ttk.Label(
            master=logo_frame,
            text="Net",
            font="Montserrat 24 bold",
            foreground="#8C2F39",
        )
        label1.pack(side="left")
        label2.pack(side="left")

        profile_label = ttk.Label(
            master=logo_frame,
            text="Profile",
            font="Montserrat 12",
            foreground="#ADADAD",
            cursor="hand2",
        )
        profile_label.bind(
            "<Button-1>",
            lambda e: self.router("stats_courses", {"consultant": CURRENT_USER}),
        )
        profile_label.pack(side="right", padx=75)
        logo_frame.pack(fill="both")

        # Second row of labels
        options_frame = ttk.Frame(master=self)
        courses_label = ttk.Label(
            master=options_frame,
            text="Courses",
            font="Montserrat 12",
            foreground="#ADADAD",
            cursor="hand2",
        )
        courses_label.bind("<Button-1>", lambda e: self.router("courses"))
        consultants_label = ttk.Label(
            master=options_frame,
            text="Consultants",
            font="Montserrat 12 underline bold",
            cursor="hand2",
        )
        consultants_label.bind("<Button-1>", lambda e: self.router("consultants"))
        requests_label = ttk.Label(
            master=options_frame,
            text="Requests",
            font="Montserrat 12",
            foreground="#ADADAD",
            cursor="hand2",
        )
        requests_label.bind("<Button-1>", lambda e: self.router("requests"))
        courses_label.pack(side="left", padx=20)
        consultants_label.pack(side="left", padx=20)
        requests_label.pack(side="left", padx=20)
        options_frame.pack(fill="both", pady=20)

        # Load the back arrow image
        self.back_arrow_image = tk.PhotoImage(file="./resources/back_arrow.png")

        # Create a button with the arrow image
        self.back_button = ttk.Button(
            self.master,
            image=self.back_arrow_image,
            cursor="hand2",
            command=lambda: self.router("consultants"),
        )
        self.back_button.place(x=50, y=400)

        # Get the window background color
        window_bg_color = "white"

        # Define a custom style for the button
        s = ttk.Style()
        s.theme_use("journal")  # Use the default theme
        s.configure("Back.TButton", background=window_bg_color, relief="flat")

        # Configure button style for hover state
        s.map(
            "Back.TButton",
            background=[
                ("active", window_bg_color),
                ("disabled", window_bg_color),
                ("pressed", window_bg_color),
            ],
        )

        self.back_button.config(style="Back.TButton")
        # Create title frame
        title_frame = ttk.Frame(self)
        title_frame.pack()

        # Title labels
        intro_label1 = ttk.Label(
            title_frame,
            text="Scheduling an appointment with: ",
            font="Montserrat 16 bold",
        )
        intro_label2 = ttk.Label(
            title_frame,
            text=str(self.consultant.name),
            font="Montserrat 16 bold",
            foreground="#8C2F39",
        )
        intro_label1.pack(side="left", pady=15)
        intro_label2.pack(side="left")

        # Introduction label
        intro_label3 = ttk.Label(
            self,
            text="Select appointment hours: ",
            font="Montserrat 16 bold",
            foreground="#ADADAD",
        )
        intro_label3.pack()

        self.current_date = datetime.now()
        # Year frame
        year_frame = ttk.Frame(self)
        self.year_changer = YearChangerFrame(year_frame, self)
        year_frame.pack()

        self.tot_label = ttk.Label(
            self,
            font=("Montserrat", 12, "bold"),
            anchor="center",
            text=f"Total: ${self.running_total:.2f} (${self.consultant.rate:.2f}/h)",
        )
        self.tot_label.pack()

        # Create schedule frame
        self.draw_schedule_frame()

        self.payment_details = PaymentInfoFrame(
            self.master, "consultant", controller=self
        )

    def draw_schedule_frame(self, redraw=False):
        if redraw:
            self.schedule_frame.pack_forget()

        self.schedule_frame = ttk.Frame(self)
        self.schedule_frame.pack(padx=10, pady=10, before=self.tot_label)

        # Create a custom style for rounded borders
        style = ttk.Style()
        style.configure(
            "Schedule.TLabel",
            borderwidth=1,
            relief="solid",
            padding=7,
            background="#FFFFFF",
            foreground="#000000",
            font=("Montserrat", 7),
            anchor="center",
        )

        style.configure("Custom3.TButton", background="#8C2F39", foreground="white")
        day_date_map = []

        # Add labels for days of the week with dates
        # leftmost will be monday of current week
        self.prev_monday = self.current_date - relativedelta(
            days=(self.current_date.weekday())
        )
        for i, day in enumerate(ScheduleAppointmentPage.days_of_week):
            day_date = self.prev_monday + relativedelta(days=i)
            day_date_map.append(day_date.day)
            # Split the day label into day name and date
            day_name_label = ttk.Label(
                self.schedule_frame,
                text=day,
                font=("Montserrat", 12, "bold"),
                anchor="center",
            )
            day_name_label.grid(
                row=0,
                column=i + 1,
                padx=(10, 2),
                pady=5,
                ipadx=10,
                ipady=5,
                sticky="ew",
            )
            day_date_label = ttk.Label(
                self.schedule_frame,
                text=day_date.strftime("%m/%d"),
                font=("Montserrat", 10),
                anchor="center",
            )
            day_date_label.grid(
                row=1,
                column=i + 1,
                padx=(10, 2),
                pady=(0, 5),
                ipadx=10,
                ipady=5,
                sticky="ew",
            )

        max_total_rows = 0

        # start with -1 to avoid forgetting to increase with continue/break etc.
        temp_date = self.prev_monday - relativedelta(days=1)
        for day in range(7):
            temp_date += relativedelta(days=1)
            # don't leave blank spaces for unavailable slots
            hour_offset = 0
            total_rows = 0
            for hour in range(24):
                if (
                    self.consultant.schedule is not None
                    and not self.consultant.schedule.is_marked_available_consider_exception(
                        (
                            temp_date.year,
                            temp_date.month,
                            day_date_map[day],
                        ),
                        hour,
                    )
                ):
                    continue
                hour_text = f"{hour}:00 - {hour+1}:00"
                date_hour_key = (temp_date.year, temp_date.month, temp_date.day, hour)
                label = ttk.Label(
                    self.schedule_frame,
                    text=hour_text,
                    font=("Montserrat", 10),
                    anchor="center",
                    style=(
                        "Schedule.TLabel"
                        if not date_hour_key in self.selected_slots
                        else "Custom3.TButton"
                    ),
                    cursor="hand2",
                )
                label.bind(
                    "<Button-1>",
                    lambda e, k=date_hour_key: self.select_slot(e.widget, k),
                )
                label.grid(
                    row=hour_offset + 2, column=day + 1, padx=15, pady=2, ipadx=25
                )
                hour_offset += 1
                total_rows += 1
            if total_rows > max_total_rows:
                max_total_rows = total_rows
        middle_row = (max_total_rows // 2) + 1

        style.configure("Nav.TButton", font="Montserrat 30")
        style.map(
            "Nav.TButton",
            background=[("active", "white")],
            foreground=[("active", "black")],
        )
        left_button = ttk.Button(
            self.schedule_frame,
            text="<",
            command=self.navigate_left,
            width=10,
            style="Nav.TButton",
        )
        left_button.grid(
            row=middle_row, column=0, rowspan=2, padx=5, pady=5, sticky="ns"
        )

        right_button = ttk.Button(
            self.schedule_frame,
            text=">",
            command=self.navigate_right,
            width=10,
            style="Nav.TButton",
        )
        right_button.grid(
            row=middle_row, column=8, rowspan=2, padx=5, pady=5, sticky="ns"
        )

    def show(self, context=None):
        if context is not None and context["consultant"] != self.consultant:
            self.consultant = context["consultant"]
            self.create_widgets()
        self.pack(pady=20)
        self.back_button.place(x=50, y=150)
        self.payment_details.show()

    def hide(self):
        self.back_button.place_forget()
        self.payment_details.hide()
        self.pack_forget()

    def navigate_left(self):
        # Handle navigation to the previous week
        t = self.current_date - relativedelta(days=7)
        if t < datetime.now() - relativedelta(minutes=10):
            t = datetime.now()
        self.current_date = t
        self.draw_schedule_frame(redraw=True)
        self.year_changer.redraw()

    def navigate_right(self):
        # Handle navigation to the next week
        self.current_date += relativedelta(days=7)
        self.draw_schedule_frame(redraw=True)
        self.year_changer.redraw()

    def select_slot(self, wid, date_hour_key):
        is_active = date_hour_key in self.selected_slots
        wid.configure(style=("Custom3.TButton" if not is_active else "Schedule.TLabel"))
        if is_active:
            del self.selected_slots[date_hour_key]
            self.running_total -= self.consultant.rate
        else:
            self.selected_slots[date_hour_key] = True
            self.running_total += self.consultant.rate

        self.redraw_running_total()

    def redraw_running_total(self):
        self.tot_label.config(
            text=f"Total: ${self.running_total:.2f} (${self.consultant.rate:.2f}/h)"
        )

    def get_current_total(self):
        return self.running_total

    def validate_slots(self):
        # check if slots are past
        for k in self.selected_slots.keys():
            if datetime(*k) < datetime.now():
                return False
        return True

    def complete_scheduling(self):
        self.consultant.schedule.add_appointment(self.selected_slots)
        self.after(2000, lambda: self.router("consultants"))
