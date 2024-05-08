import ttkbootstrap as ttk
from course_item import CourseItem
from domain.course import courses_dict


class CoursesPage(ttk.Frame):

    def __init__(self, master, router, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

        self.router = router

    def create_widgets(self):
        # first row of labels
        logo_frame = ttk.Frame(master=self)
        # add textlabel
        # make text semi bold
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
        )
        profile_label.bind("<Button-1>", lambda e: print("Profile clicked"))
        profile_label.pack(side="right")

        logo_frame.pack(fill="both")

        # second row of labels
        options_frame = ttk.Frame(master=self)
        # add textlabel
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
            font="Montserrat 12",
            foreground="#ADADAD",
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
        courses_label.pack(side="left", padx=20)
        consultants_label.pack(side="left", padx=20)
        requests_label.pack(side="left", padx=20)

        options_frame.pack(fill="both", pady=20)

        # search bar
        search_entry = ttk.Entry(master=self, width=50)
        search_entry.insert(0, "Search")
        search_entry.bind("<FocusIn>", lambda e: search_entry.delete(0, "end"))
        search_entry.bind("<Return>", lambda e: print(e.widget.get()))
        search_entry.pack()

        # category box with Checkbuttons
        category_frame = ttk.Frame(
            master=self, width=200, height=200, borderwidth=2, relief="ridge"
        )
        categories_label = ttk.Label(
            master=category_frame,
            text="Categories",
            font="Montserrat 12",
            foreground="#ADADAD",
        )
        check1 = ttk.Checkbutton(master=category_frame, text="Category 1")
        check2 = ttk.Checkbutton(master=category_frame, text="Category 2")
        check3 = ttk.Checkbutton(master=category_frame, text="Category 3")
        check4 = ttk.Checkbutton(master=category_frame, text="Category 4")
        check5 = ttk.Checkbutton(master=category_frame, text="Category 5")
        categories_label.pack()
        check1.pack()
        check2.pack()
        check3.pack()
        check4.pack()
        check5.pack()
        category_frame.pack(side="left", padx=10)

        for course in courses_dict.values():
            CourseItem(self, course)

        # self.pack()
