import datetime
import re
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog
from domain.category import categories_dict, Category
from calendar_frame import CalendarFrame
from bank_details_frame import BankDetailsFrame
from domain.consultant import Consultant, consultants_dict
from domain.image import Image


class CreateProfilePage(ttk.Frame):
    def __init__(self, master, router, **kwargs):
        super().__init__(master, **kwargs)

        self.router = router
        self.pic_path = ""
        self.pic_path_label = None

        self.exp_entries = []
        self.edu_entries = []

        self.active_msg = None
        self.created = False

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
        self.first_name_entry.bind(
            "<FocusIn>", lambda e: self.first_name_entry.delete(0, "end")
        )
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
        self.last_name_entry.bind(
            "<FocusIn>", lambda e: self.last_name_entry.delete(0, "end")
        )
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
            master=CatFrame,
            text="+",
            command=lambda: self.show_add_category_entry(
                CreateProfileFrame, CatFrame, self.cb
            ),
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
        edu_entry.bind(
            "<Return>",
            lambda e: self.confirm_add_edu(CreateProfileFrame, EduFrame, e.widget),
        )
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
        exp_entry.bind(
            "<Return>",
            lambda e: self.confirm_add_exp(CreateProfileFrame, ExpFrame, e.widget),
        )
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

        self.available_calendar = CalendarFrame(master=self)
        self.available_calendar.pack()

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
        f_entry.pack(side="left", padx=4)

        s_entry = ttk.Entry(master=ExcFrame, width=3)
        s_entry.insert(0, "HH")
        s_entry.bind("<FocusIn>", lambda e: s_entry.delete(0, "end"))
        s_entry.pack(side="left", padx=4)

        t_entry = ttk.Entry(master=ExcFrame, width=3)
        t_entry.insert(0, "HH")
        t_entry.bind("<FocusIn>", lambda e: t_entry.delete(0, "end"))
        t_entry.pack(side="left", padx=4)

        exc_btn = ttk.Button(
            master=ExcFrame,
            text="Add",
            command=lambda: self.confirm_add_exception(
                ExcFrame, f_entry, s_entry, t_entry, exc_btn
            ),
        )

        f_entry.bind(
            "<Return>",
            lambda e: self.confirm_add_exception(
                ExcFrame, f_entry, s_entry, t_entry, exc_btn
            ),
        )
        s_entry.bind(
            "<Return>",
            lambda e: self.confirm_add_exception(
                ExcFrame, f_entry, s_entry, t_entry, exc_btn
            ),
        )
        t_entry.bind(
            "<Return>",
            lambda e: self.confirm_add_exception(
                ExcFrame, f_entry, s_entry, t_entry, exc_btn
            ),
        )

        exc_btn.pack(side="left")

        ExcFrame.pack(pady=(0, 40))

        self.bankDetailsFrame = BankDetailsFrame(RestFrame)
        self.bankDetailsFrame.show()

        self.terms_var = tk.IntVar()
        self.terms = ttk.Checkbutton(
            master=RestFrame,
            text="I have read and accept the Terms & Conditions",
            variable=self.terms_var,
            onvalue=1,
            offvalue=0,
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
        self.terms.pack(pady=(20, 30))
        style.configure("Custom3.TButton", background="#8C2F39", foreground="white")
        self.submit_button = ttk.Button(
            master=RestFrame,
            text="Create Profile",
            width=25,
            style="Custom3.TButton",
            command=lambda: self.submit(RestFrame),
        )
        self.submit_button.pack(pady=(0, 60))
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
        if not new_cat or new_cat.lower() in map(
            lambda x: x.lower(), list(categories_dict.keys())
        ):
            return

        new_cat_obj = Category(new_cat)
        categories_dict[new_cat] = new_cat_obj

        combobox["values"] = combobox["values"] + (new_cat,)

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

    def confirm_add_exception(self, master, date_f, h1_f, h2_f, btn):
        date = date_f.get().strip()
        h1 = h1_f.get().strip()
        h2 = h2_f.get().strip()
        if not date or not h1 or not h2:
            print("not")
            return

        current_date = datetime.datetime.now()
        if len(date) != 10:
            print("wrong date len")
            return

        date = date.split("/")
        if len(date) != 3:
            print("wrong split lent")
            return

        try:
            year = int(date[0])
            month = int(date[1])
            day = int(date[2])
            hour1 = int(h1)
            hour2 = int(h2)
            if hour1 >= hour2:
                raise ValueError
            exc_dt_1 = datetime.datetime(year, month, day, hour1, 0)
            exc_dt_2 = datetime.datetime(year, month, day, hour2, 0)
            if not exc_dt_1 > current_date:
                raise ValueError
        except ValueError:
            print("value error")
            return

        self.available_calendar.consultant_schedule.add_exception(
            (year, month, day), hour1, hour2
        )
        exc_label = ttk.Label(
            master=master,
            text="• " + "/".join(date) + " " + h1 + ":00-" + h2 + ":00",
            font="Montserrat 12",
        )
        date_f.delete(0, "end")
        h1_f.delete(0, "end")
        h2_f.delete(0, "end")
        exc_label.pack(side="top", after=btn)

    @staticmethod
    def is_valid_dollar_amount(amount):
        pattern = r"(\d{1,3})(,\d{3})*(\.\d{2})?$"

        match = re.fullmatch(pattern, amount)

        return bool(match)

    def submit(self, master):
        if self.created:
            return
        if not self.first_name_entry.get():
            self.show_error_msg(
                master, self.submit_button, "First name cannot be empty."
            )
            return
        if not self.last_name_entry.get():
            self.show_error_msg(
                master, self.submit_button, "Last name cannot be empty."
            )
            return
        if not self.is_valid_dollar_amount(self.r_entry.get()):
            self.show_error_msg(master, self.submit_button, "Invalid rate.")
            return
        if not self.is_valid_dollar_amount(self.r_entry.get()):
            self.show_error_msg(master, self.submit_button, "Invalid rate.")
            return

        if not self.bankDetailsFrame.validate_iban():
            self.show_error_msg(master, self.submit_button, "Invalid IBAN.")
            return

        if self.terms_var.get() != 1:
            self.show_error_msg(
                master, self.submit_button, "Terms must be accepted to create profile."
            )
            return

        self.hide_msg()

        # NOTE: dims left empty
        new_consultant = Consultant(
            self.first_name_entry.get() + " " + self.last_name_entry.get(),
            Image(self.pic_path, 0, 0),
            [self.cb.get()],
            self.edu_entries,
            self.exp_entries,
            float(self.r_entry.get()),
            self.available_calendar.consultant_schedule,
            self.bankDetailsFrame.get_details(),
        )

        consultants_dict[new_consultant.name] = new_consultant
        self.show_success_msg(master, self.submit_button, "Consultant profile successfully created.")
        self.created = True


    def show_error_msg(self, master, btn, msg):
        self.hide_msg()
        self.active_msg = ttk.Label(
            master=master, text=msg, font="Montserrat 12 bold", foreground="#FF0000"
        )
        self.active_msg.pack(before=btn)
        pass

    def show_success_msg(self, master, btn, msg):
        self.hide_msg()
        self.active_msg = ttk.Label(
            master=master, text=msg, font="Montserrat 12 bold", foreground="#00FF00"
        )
        self.active_msg.pack(before=btn)
        pass

    def hide_msg(self):
        if self.active_msg:
            self.active_msg.pack_forget()


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
