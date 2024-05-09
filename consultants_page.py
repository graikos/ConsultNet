import ttkbootstrap as ttk
from consultant_info import ConsultantInfo
from domain.consultant import consultants_dict
from domain.category import categories_dict


class ConsultantsPage(ttk.Frame):

    def __init__(self, master, router, **kwargs):
        super().__init__(master, **kwargs)

        self.cons_widgets = []
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
            font="Montserrat 12",
            foreground="#ADADAD",
            cursor="hand2",
        )
        courses_label.bind("<Button-1>", lambda e: self.router("courses"))
        consultants_label = ttk.Label(
            master=options_frame,
            text="Consultants",
            font="Montserrat 12 bold underline",
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
        # TODO: Add request button functionality
        courses_label.pack(side="left", padx=20)
        consultants_label.pack(side="left", padx=20)
        requests_label.pack(side="left", padx=20)

        options_frame.pack(fill="both", pady=20)

        # search bar
        search_entry = ttk.Entry(master=self, width=50)
        search_entry.insert(0, "Search through consultants")
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

        categories_label.pack(pady=(10, 5))
        for cat in categories_dict.values():
            chvar = ttk.IntVar()
            ch = ttk.Checkbutton(
                master=category_frame,
                text=cat.name,
                command=lambda cat=cat: self.filter_consultants_by_category(
                    cat
                ),  # capture category
                variable=chvar,
            )
            self.categories_vars[cat] = chvar
            ch.state(["!alternate"])
            ch.pack(anchor="w", padx=20, pady=5)  # Align left and add padding
        category_frame.pack(anchor="nw", side="left", padx=40, pady=30)

        consultant_frame = ttk.Frame(master=self, width=400, height=400)
        for i, cons in enumerate(consultants_dict.values()):
            self.cons_widgets.append(ConsultantInfo(consultant_frame, cons, i))
        consultant_frame.pack(fill="both", padx=275)

        # self.pack()

    def filter_consultants_by_category(self, category):

        # if this is not a plain search with no active category
        if category is not None:
            is_now_active = self.categories_vars[category].get() == 1

            if is_now_active:
                self.active_categories[category] = True
            else:
                del self.active_categories[category]

        i = 0
        # filter all consultant widgets
        for cwid in self.cons_widgets:
            # if all categories unchecked, show all
            if not self.active_categories:
                if not self.active_search_term or (
                    self.active_search_term in cwid.consultant.name.lower()
                ):
                    cwid.number = i
                    i += 1
                    cwid.show()
                else:
                    # else hide those that do not match the term
                    cwid.hide()
            else:
                # else filter
                for cat in self.active_categories.keys():
                    if (
                        cat.name in cwid.consultant.categories
                        and self.active_search_term in cwid.consultant.name.lower()
                    ):
                        cwid.number = i
                        i += 1
                        cwid.show()
                        break
                else:
                    cwid.hide()

    def filter_by_search(self, ev):
        self.active_search_term = ev.widget.get().lower()

        # no active category, search through everything
        if not self.active_categories:
            self.filter_consultants_by_category(None)

        # filter with every currently active category with added search term
        for cat in self.active_categories.keys():
            self.filter_consultants_by_category(cat)
