import ttkbootstrap as ttk
from courses_page import CoursesPage
from consultants_page import ConsultantsPage
from course_purchase import CoursePurchasePage


class App(ttk.Window):
    def __init__(self, themename="journal"):
        super().__init__(themename=themename)
        self.title("ConsultNet")
        self.geometry("800x600")

        # classname and if new object should be created for each view
        self.routes = {
            "courses": (CoursesPage, False),
            "consultants": (ConsultantsPage, False),
            "course_purchase": (CoursePurchasePage, True),
        }

        self.current_frame = None

        self.frames = {}

        for tup in filter(lambda x: not x[1], self.routes.values()):
            F = tup[0]
            frame = F(self, router=self.router)
            self.frames[F] = frame
            # frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(self.routes["consultants"])

    def show_frame(self, r, context=None):
        loc, should_create_new = r
        # if new page should be created each time for this route, replace frame with this
        # old one will be garbage collected
        if should_create_new:
            self.frames[loc] = loc(self, router=self.router, context=context)
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
