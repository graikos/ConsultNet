import ttkbootstrap as ttk
from consultant_info import ConsultantInfo
from domain.consultant import consultants_dict
from domain.category import categories_dict
from PIL import Image, ImageTk, ImageDraw

class ConsultantsPage(ttk.Frame):

    def __init__(self, master, router, **kwargs):
        super().__init__(master, **kwargs)
        self.cons_widgets = []
        self.categories_vars = {}
        self.active_categories = {}
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
        profile_label.pack(side="right",padx=75)

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
        search_entry.bind("<Return>", lambda e: print(e.widget.get()))
        search_entry.pack()

        # category box with Checkbuttons
        category_frame = ttk.Frame(
            master=self, width=200, height=200, borderwidth=2, relief="ridge"
        )

        categories_label = ttk.Label(
            master=category_frame,
            text="Categories",
            font="Montserrat 12 bold"
        )
        categories_label.pack(pady=(10, 5))  # Center the title

        for cat in categories_dict.values():
            chvar = ttk.IntVar()
            ch = ttk.Checkbutton(
                master=category_frame,
                text=cat.name,
                command=lambda cat=cat: self.filter_courses_by_category(cat), # capture category
                variable=chvar,
            )
            self.categories_vars[cat.name] = chvar
            ch.state(["!alternate"])
            ch.pack(anchor="w", padx=20, pady=5)  # Align left and add padding
        category_frame.pack(anchor="nw",side='left', padx=40, pady=30)

        consultant_frame = ttk.Frame(master=self, width=400, height=400)
        for i,cons in enumerate(consultants_dict.values()):
            self.cons_widgets.append(ConsultantInfo(consultant_frame,cons,i))
        consultant_frame.pack(fill='both', padx=275)    
        # self.pack()

    def filter_courses_by_category(self, category):
        is_now_active = self.categories_vars[category.name].get() == 1

        if is_now_active:
            self.active_categories[category.name] = True
        else:
            del self.active_categories[category.name]

        # filter all course widgets
        for cwid in self.cons_widgets:

            # if all categories unchecked, show all
            if not self.active_categories:

                cwid.pack(side='top',pady=30,fill='x',padx=(300,350))
            else:
                # else filter
                for cat in self.active_categories.keys():
                    if cat in cwid.consultant.categories:
                        cwid.pack(side='top',pady=30,fill='x',padx=(300,350))
                        break
                else:
                    cwid.pack_forget()

