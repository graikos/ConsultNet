import ttkbootstrap as ttk
from course_item import CourseItem
from domain.course import courses_dict
from domain.category import categories_dict


class CoursesPage(ttk.Frame):

    def __init__(self, master, router, **kwargs):
        super().__init__(master, **kwargs)
        self.course_widgets = []
        self.categories_vars = {}
        self.active_categories = {}
        self.active_search_term = ""
        self.router = router

        self.create_widgets()

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
        profile_label.pack(side="right", padx=75)

        logo_frame.pack(fill="both")

        # second row of labels
        options_frame = ttk.Frame(master=self)
        # add textlabel
        courses_label = ttk.Label(
            master=options_frame,
            text="Courses",
            font="Montserrat 12 bold underline",
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
        requests_label.bind("<Button-1>", lambda e: self.router("requests"))
        courses_label.pack(side="left", padx=20)
        consultants_label.pack(side="left", padx=20)
        requests_label.pack(side="left", padx=20)

        options_frame.pack(fill="both", pady=20)

        # search bar
        search_entry = ttk.Entry(master=self, width=50)
        search_entry.insert(0, "Search")
        search_entry.bind("<FocusIn>", lambda e: search_entry.delete(0, "end"))
        search_entry.bind("<Return>", lambda e: self.filter_by_search(e))
        search_entry.pack()

        # category box with Checkbuttons
        category_frame = ttk.Frame(
            master=self, width=200, height=200, borderwidth=2, relief="ridge"
        )

        categories_label = ttk.Label(
            master=category_frame, text="Categories", font="Montserrat 12 bold"
        )
        categories_label.pack(pady=(10, 5))  # Center the title

        for cat in categories_dict.values():
            chvar = ttk.IntVar()
            ch = ttk.Checkbutton(
                master=category_frame,
                text=cat.name,
                command=lambda cat=cat: self.filter_courses_by_category(
                    cat
                ),  # capture category
                variable=chvar,
            )
            self.categories_vars[cat] = chvar
            ch.state(["!alternate"])
            ch.pack(anchor="w", padx=20, pady=5)  # Align left and add padding
        category_frame.pack(anchor="nw", side="left", padx=40, pady=40)
        
        style = ttk.Style()
        style.configure('Rep.TButton', background='#ADADAD', foreground = 'black', font=('Montserrat', 8),relief = 'flat',borderwith=0)
        rep_cont_button = ttk.Button(self, text="🚩 Report content", style = 'Rep.TButton')
        rep_cont_button.place(x=65, y=800)

        for course in courses_dict.values():
            self.course_widgets.append(
                CourseItem(
                    self,
                    course,
                    1,
                    command=lambda course=course: self.router(
                        "course_purchase", {"course": course, "consultant": course.cons},
                    ),
                    controller=self,
                )
            )

        # self.pack()

    def filter_courses_by_category(self, category):

        # if this is not a plain search with no active category
        if category is not None:
            is_now_active = self.categories_vars[category].get() == 1

            if is_now_active:
                self.active_categories[category] = True
            else:
                del self.active_categories[category]

        # filter all course widgets
        cnt = 0
        for cwid in self.course_widgets:

            # if all categories unchecked, show all
            if not self.active_categories:
                # show only those who also match the search term
                if not self.active_search_term or (
                    self.active_search_term in cwid.course.name.lower()
                ):
                    cwid.show()
                else:
                    # else hide those that do not match the term
                    cnt += 1
                    cwid.hide()
            else:
                # else filter
                for cat in self.active_categories.keys():
                    # category filter also respects search term
                    if (
                        cat.name in cwid.course.categories
                        and self.active_search_term in cwid.course.name.lower()
                    ):
                        cwid.show()
                        break
                else:
                    cnt += 1
                    cwid.hide()
            if cnt == len(self.course_widgets):
                # all course_widgets were hidden, meaning no results
                # TODO: here show text that says "No results." and has link to "requests"
                print("not found")
            else:
                # TODO: here hide this text
                pass

    def filter_by_search(self, ev):
        self.active_search_term = ev.widget.get().lower()

        # no active category, search through everything
        if not self.active_categories:
            self.filter_courses_by_category(None)

        # filter with every currently active category with added search term
        for cat in self.active_categories.keys():
            self.filter_courses_by_category(cat)

    def show(self, context=None):
        self.pack(expand=True, fill="both")

    def hide(self):
        self.pack_forget()