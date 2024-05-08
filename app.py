import ttkbootstrap as ttk
from courses_page import CoursesPage
from consultants_page import ConsultantsPage


class App(ttk.Window):
    def __init__(self, themename="journal"):
        super().__init__(themename=themename)
        self.title("ConsultNet")
        self.geometry("300x200")

        self.routes = {
            "courses": CoursesPage,
            "consultants": ConsultantsPage
        }

        self.current_frame = None

        self.frames = {}

        for F in self.routes.values():
            frame = F(self, self.router)
            self.frames[F] = frame
            # frame.grid(row=0, column=0, sticky="nsew")
 

        self.show_frame(CoursesPage)

    def show_frame(self, context):
        frame = self.frames[context]
        if frame == self.current_frame:
            return
        if self.current_frame is not None:
            print("forget", self.current_frame)
            self.current_frame.pack_forget()
        frame.pack(expand=True, fill='both')
        self.current_frame = frame
        print("showing", context)

    def router(self, loc):
        print("routing ", loc)
        self.show_frame(self.routes[loc])




if __name__ == "__main__":
    app = App()
    app.mainloop()