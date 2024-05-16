import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog
from domain.category import categories_dict, Category
from calendar_frame import CalendarFrame


class CreateProfilePage(ttk.Frame):
    def __init__(self, master, router, **kwargs):
        super().__init__(master, **kwargs)

        self.router = router
        self.pic_path = ""
        self.pic_path_label = None

        self.exp_entries = []
        self.edu_entries = []

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

        # CreateProfile Frame
        CreateProfileFrame = ttk.Frame(master=self)
        intro_label = ttk.Label(
            master=CreateProfileFrame,
            text="Create your Profile",
            font="Montserrat 16 bold",
        )
        intro_label.pack(pady=30)

        FirstNameFrame = ttk.Frame(master=CreateProfileFrame)
        first_name_label = ttk.Label(
            master=FirstNameFrame, text="First name:", font="Montserrat 9 bold"
        )
        first_name_label.pack(side="left", padx=(0, 8))
        self.first_name_entry = ttk.Entry(master=FirstNameFrame, width=30)
        self.first_name_entry.insert(0, "")
        self.first_name_entry.bind("<FocusIn>", lambda e: self.first_name_entry.delete(0, "end"))
        self.first_name_entry.bind("<Return>", lambda e: print(e.widget.get()))
        self.first_name_entry.pack(side="left")
        FirstNameFrame.pack(anchor="w", pady=5, padx=53)

        LastNameFrame = ttk.Frame(master=CreateProfileFrame)
        last_name_label = ttk.Label(
            master=LastNameFrame, text="Last name:", font="Montserrat 9 bold"
        )
        last_name_label.pack(side="left", padx=(0, 8))
        self.last_name_entry = ttk.Entry(master=LastNameFrame, width=30)
        self.last_name_entry.insert(0, "")
        self.last_name_entry.bind("<FocusIn>", lambda e: self.last_name_entry.delete(0, "end"))
        self.last_name_entry.bind("<Return>", lambda e: print(e.widget.get()))
        self.last_name_entry.pack(side="left")
        LastNameFrame.pack(anchor="w", pady=5, padx=55)

        PicFrame = ttk.Frame(master=CreateProfileFrame)
        pic_label = ttk.Label(
            master=PicFrame, text="Profile Picture:", font="Montserrat 9 bold"
        )
        pic_label.pack(side="left", padx=(0, 8))
        pic_entry = ttk.Button(
            master=PicFrame,
            text="Select picture",
            width=30,
            command=lambda: self.open_file_dialog(CreateProfileFrame, PicFrame),
        )
        pic_entry.pack(side="left")
        PicFrame.pack(anchor="w", pady=5, padx=27)

        CatFrame = ttk.Frame(master=CreateProfileFrame)
        cat_label = ttk.Label(
            master=CatFrame, text="Field of Expertise:", font="Montserrat 9 bold"
        )
        cat_label.pack(side="left", padx=(0, 8))
        categories = list(categories_dict.keys())
        self.cb = ttk.Combobox(
            master=CatFrame, state="readonly", values=categories, width=28
        )
        self.cb.pack(side="left")
        add_cat = ttk.Button(
            master=CatFrame, text="+", command=lambda: self.show_add_category_entry(CreateProfileFrame, CatFrame, self.cb)
        )
        add_cat.pack(side="left")
        CatFrame.pack(anchor="w", pady=5, padx=10)

        EduFrame = ttk.Frame(master=CreateProfileFrame)
        edu_label = ttk.Label(
            master=EduFrame, text="Education:", font="Montserrat 9 bold"
        )
        edu_label.pack(side="left", padx=(0, 8))
        edu_entry = ttk.Entry(master=EduFrame, width=30)
        edu_entry.insert(0, "")
        edu_entry.bind("<FocusIn>", lambda e: edu_entry.delete(0, "end"))
        edu_entry.bind("<Return>", lambda e: self.confirm_add_edu(CreateProfileFrame, EduFrame, e.widget))
        edu_entry.pack(side="left")
        EduFrame.pack(anchor="w", pady=5, padx=56)

        ExpFrame = ttk.Frame(master=CreateProfileFrame)
        exp_label = ttk.Label(
            master=ExpFrame, text="Experience:", font="Montserrat 9 bold"
        )
        exp_label.pack(side="left", padx=(0, 8))
        exp_entry = ttk.Entry(master=ExpFrame, width=30)
        exp_entry.insert(0, "")
        exp_entry.bind("<FocusIn>", lambda e: exp_entry.delete(0, "end"))
        exp_entry.bind("<Return>", lambda e: self.confirm_add_exp(CreateProfileFrame, ExpFrame, e.widget))
        exp_entry.pack(side="left")
        ExpFrame.pack(anchor="w", pady=5, padx=48)

        RFrame = ttk.Frame(master=CreateProfileFrame)
        r_label = ttk.Label(
            master=RFrame, text="Hourly rate ($):", font="Montserrat 9 bold"
        )
        r_label.pack(side="left", padx=(0, 8))
        self.r_entry = ttk.Entry(master=RFrame, width=30)
        self.r_entry.insert(0, "")
        self.r_entry.bind("<FocusIn>", lambda e: self.r_entry.delete(0, "end"))
        self.r_entry.bind("<Return>", lambda e: print(e.widget.get()))
        self.r_entry.pack(side="left")
        RFrame.pack(anchor="w", pady=5, padx=30)

        CreateProfileFrame.pack()

        # Available Hours Frame

        availableCalendar = CalendarFrame(master=self)
        availableCalendar.pack()

        # Rest Frame

        RestFrame = ttk.Frame(master=self)

        exc_label = ttk.Label(
            master=RestFrame, text="Exceptions", font="Montserrat 12 bold"
        )
        exc_label.pack(pady=(40, 20))

        ExcFrame = ttk.Frame(master=RestFrame)
        f_entry = ttk.Entry(master=ExcFrame, width=13)
        f_entry.insert(0, "YYYY/MM/DD")
        f_entry.bind("<FocusIn>", lambda e: f_entry.delete(0, "end"))
        f_entry.bind("<Return>", lambda e: print(e.widget.get()))
        f_entry.pack(side="left", padx=4)

        s_entry = ttk.Entry(master=ExcFrame, width=3)
        s_entry.insert(0, "HH")
        s_entry.bind("<FocusIn>", lambda e: s_entry.delete(0, "end"))
        s_entry.bind("<Return>", lambda e: print(e.widget.get()))
        s_entry.pack(side="left", padx=4)

        t_entry = ttk.Entry(master=ExcFrame, width=3)
        t_entry.insert(0, "HH")
        t_entry.bind("<FocusIn>", lambda e: t_entry.delete(0, "end"))
        t_entry.bind("<Return>", lambda e: print(e.widget.get()))
        t_entry.pack(side="left", padx=4)

        ExcFrame.pack(pady=(0, 40))

        bank_label = ttk.Label(
            master=RestFrame, text="Bank Account Details:", font="Montserrat 12 bold"
        )
        bank_label.pack(pady=(0, 20))

        AccFrame = ttk.Frame(master=RestFrame)
        acc_label = ttk.Label(
            master=AccFrame, text="Account: ", font="Montserrat 9 bold"
        )
        acc_label.pack(side="left")
        acc_entry = ttk.Entry(master=AccFrame, width=30)
        acc_entry.insert(0, "")
        acc_entry.bind("<FocusIn>", lambda e: acc_entry.delete(0, "end"))
        acc_entry.bind("<Return>", lambda e: print(e.widget.get()))
        acc_entry.pack(side="left")
        AccFrame.pack(anchor="w", pady=(0, 10))

        IbanFrame = ttk.Frame(master=RestFrame)
        iban_label = ttk.Label(
            master=IbanFrame, text="IBAN: ", font="Montserrat 9 bold"
        )
        iban_label.pack(side="left")
        iban_entry = ttk.Entry(master=IbanFrame, width=30)
        iban_entry.insert(0, "")
        iban_entry.bind("<FocusIn>", lambda e: iban_entry.delete(0, "end"))
        iban_entry.bind("<Return>", lambda e: print(e.widget.get()))
        iban_entry.pack(side="left")
        IbanFrame.pack(pady=(0, 10), padx=20)

        terms = ttk.Checkbutton(
            master=RestFrame, text="I have read and accept the Terms & Conditions"
        )

        # Create a custom style for rounded borders
        style = ttk.Style()
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
        terms.pack(pady=(20, 30))
        style.configure("Custom3.TButton", background="#8C2F39", foreground="white")
        p_button = ttk.Button(
            master=RestFrame, text="Create Profile", width=25, style="Custom3.TButton"
        )
        p_button.pack(pady=(0, 60))
        RestFrame.pack(pady=(0, 10), padx=20)

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()

    def open_file_dialog(self, master_frame, cur_frame):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("All files", "*.*"),
            ]
        )
        if file_path:
            if self.pic_path_label is not None:
                self.pic_path_label.pack_forget()
            self.pic_path = file_path
            self.pic_path_label = ttk.Label(
                master=master_frame, text=file_path.split("/")[-1], font="Montserrat 12"
            )
            self.pic_path_label.pack(after=cur_frame, anchor="e")

    def show_add_category_entry(self, master_frame, cur_frame, cb):
        AddCatFrame = ttk.Frame(master=master_frame)
        cat_label = ttk.Label(
            master=AddCatFrame, text="Add new category:", font="Montserrat 9 bold"
        )
        cat_label.pack(side="left", padx=(0, 8))
        cat_entry = ttk.Entry(master=AddCatFrame, width=30)
        cat_entry.insert(0, "")
        cat_entry.bind("<FocusIn>", lambda e: cat_entry.delete(0, "end"))
        com = lambda: self.add_category_confirm(cat_entry, cat_entry.get(), cb)
        cat_entry.bind("<Return>", lambda e: com())
        cat_entry.pack(side="left")
        cat_btn = ttk.Button(master=AddCatFrame, text="Add", command=com)
        cat_btn.pack(side="left")
        AddCatFrame.pack(anchor="w", pady=5, padx=53, after=cur_frame)

    def add_category_confirm(self, entry, cat, cb):
        entry.delete(0, "end")
        self.add_category(cat, cb)

    def add_category(self, new_cat, combobox):
        # check if exists
        if not new_cat or new_cat.lower() in map(lambda x: x.lower(), list(categories_dict.keys())):
            return

        new_cat_obj = Category(new_cat)
        categories_dict[new_cat] = new_cat_obj

        combobox["values"] = combobox["values"] + (new_cat,)


    def show_add_exp(self, master_frame, cur_frame, confirm_command, label_text):
        AddFrame = ttk.Frame(master=master_frame)
        add_label = ttk.Label(
            master=AddFrame, text=label_text, font="Montserrat 9 bold"
        )
        add_label.pack(side="left", padx=(0, 8))
        add_entry
        add_entry = ttk.Entry(master=AddFrame, width=30)
        add_entry.insert(0, "")
        add_entry.bind("<FocusIn>", lambda e: add_entry.delete(0, "end"))
        add_entry.bind("<Return>", lambda e: print(e.widget.get()))
        add_entry.pack(side="left")
        add_confirm_btn = ttk.Button(master=AddFrame, text="Add", command=confirm_command)
        add_confirm_btn.pack(side="left")
        AddFrame.pack(anchor="w", pady=5, padx=53, after=cur_frame)

    def confirm_add_edu(self, master_frame, cur_frame, wid):
        if not wid.get():
            return
        new_exp = ttk.Label(
            master=master_frame, text="• " + wid.get(), font="Montserrat 12"
        )
        self.edu_entries.append(wid.get())
        wid.delete(0, "end")
        new_exp.pack(after=cur_frame, anchor="w")

    def confirm_add_exp(self, master_frame, cur_frame, wid):
        if not wid.get():
            return
        new_exp = ttk.Label(
            master=master_frame, text="• " + wid.get(), font="Montserrat 12"
        )
        self.exp_entries.append(wid.get())
        wid.delete(0, "end")
        new_exp.pack(after=cur_frame, anchor="w")

    def add_list_entry(self, master_frame, cur_frame, val):
        print(val)


if __name__ == "__main__":
    # window
    window = ttk.Window(themename="journal")
    window.title("app")
    window.geometry("1920x1200")

    # Create a Canvas widget
    canvas = tk.Canvas(window)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a Scrollbar widget
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to contain your widgets
    frame = ttk.Frame(canvas)
    canvas.create_window((960, 0), window=frame, anchor="n")

    # Update the scroll region when the frame size changes
    frame.bind(
        "<Configure>",
        lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")),
    )

    createProfilePage = CreateProfilePage(master=frame, router=None)
    createProfilePage.show()

    window.mainloop()
