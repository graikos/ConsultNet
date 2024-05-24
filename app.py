import ttkbootstrap as ttk
import tkinter as tk
from courses_page import CoursesPage
from consultants_page import ConsultantsPage
from course_purchase import CoursePurchasePage
from schedule_appointment import ScheduleAppointmentPage
from requests_page import RequestsPage
from revenue_statistics_mycourses import StatsCoursesPage
from revenue_statistics_services import StatsServicesPage
from course_info import CourseInfoPage



class App(ttk.Window):
    def __init__(self, themename="journal"):
        super().__init__(themename=themename)
        self.title("ConsultNet")
        self.geometry("1920x1200")
        # Create a Canvas widget
        canvas = tk.Canvas(self)
        canvas.pack(side="left", fill="both", expand=True)

        # Add a Scrollbar widget
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to contain your widgets
        myframe = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=myframe, anchor="n")

        # Update the scroll region when the frame size changes
        myframe.bind(
            "<Configure>",
            lambda event, canvas=canvas: canvas.configure(
                scrollregion=canvas.bbox("all")
            ),
        )

        # classname and if new object should be created for each view
        self.routes = {
            "courses": (CoursesPage, False),
            "consultants": (ConsultantsPage, False),
            "requests": (RequestsPage, False),
            "course_purchase": (CoursePurchasePage, True),
            "schedule_appointment": (ScheduleAppointmentPage, True),
            "stats_courses": (StatsCoursesPage, True),
            "stats_services": (StatsServicesPage, True),
            "course_info": (CourseInfoPage, True),
        }

        self.current_frame = None

        self.frames = {}

        self.godframe = myframe

        for tup in filter(lambda x: not x[1], self.routes.values()):
            F = tup[0]
            frame = F(myframe, router=self.router)
            self.frames[F] = frame
            # frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(self.routes["consultants"])

    def show_frame(self, r, context=None):
        loc, should_create_new = r
        # if new page should be created each time for this route, replace frame with this
        # old one will be garbage collected
        if should_create_new:
            frame = loc(self.godframe, router=self.router, context=context)
            self.frames[loc] = frame
        frame = self.frames[loc]
        if frame == self.current_frame:
            return
        if self.current_frame is not None:
            self.current_frame.hide()
        frame.show(context=context)
        self.current_frame = frame

    def router(self, loc, context=None):
        self.show_frame(self.routes[loc], context)


if __name__ == "__main__":
    app = App()
    app.mainloop()
