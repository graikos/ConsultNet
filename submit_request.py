import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import ttkbootstrap as ttk
from payment_details import PaymentInfoFrame
from domain.consultant import CURRENT_USER
from domain.category import categories_dict
from RoundedLabel import RoundedLabel


class SubmitRequestPage(ttk.Frame):

    def __init__(self, master, router=None, controller=None, context=None, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.router = router
        self.win_master = master

        self.create_widgets()

    def create_widgets(self):

        # First row of labels
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
        )
        courses_label.bind("<Button-1>", lambda e: self.router("courses"))
        consultants_label = ttk.Label(
            master=options_frame,
            text="Consultants",
            font="Montserrat 12",
            foreground="#ADADAD",
        )
        consultants_label.bind("<Button-1>", lambda e: self.router("consultants"))
        requests_label = ttk.Label(
            master=options_frame,
            text="Requests",
            font="Montserrat 12 underline bold",
        )
        courses_label.pack(side="left", padx=20)
        consultants_label.pack(side="left", padx=20)
        requests_label.pack(side="left", padx=20)
        options_frame.pack(fill="both", pady=20)

        # Load the back arrow image
        self.back_arrow_image = tk.PhotoImage(file="./resources/back_arrow.png")

        # Create a button with the arrow image
        self.back_button = ttk.Button(
            self.win_master,
            image=self.back_arrow_image,
            cursor="hand2",
            command=lambda: self.router("requests"),
        )
        self.back_button.place(x=50, y=150)

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
        # self.master = master
        # TODO: change this text
        intro_label = ttk.Label(
            master=self, text="Submitting a request", font="Montserrat 15 bold"
        )
        intro_label.pack(pady=(40, 80))

        TFrame = ttk.Frame(master=self)
        t_label = ttk.Label(
            master=TFrame, text="Request Title:", font="Montserrat 9 bold"
        )
        t_label.pack(anchor="w", side="left", padx=(0, 10))
        t_entry = ttk.Entry(master=TFrame, width=30)
        t_entry.insert(0, "")
        t_entry.bind("<FocusIn>", lambda e: t_entry.delete(0, "end"))
        t_entry.bind("<Return>", lambda e: print(e.widget.get()))
        t_entry.pack(side="left")
        TFrame.pack(pady=(0, 14), padx=(0, 70))

        TyFrame = ttk.Frame(master=self)
        ty_label = ttk.Label(
            master=TyFrame, text="Request Type:", font="Montserrat 9 bold"
        )
        ty_label.pack(anchor="w", side="left", padx=(0, 10))
        course_label = tk.Label(
            TyFrame,
            text="Course",
            relief="groove",
            padx=10,
            pady=5,
            borderwidth=2,
            bg="#8C2F39",
            fg="white",
        )
        course_label.pack(side="left", padx=(0, 8))
        consultant_label = tk.Label(
            TyFrame,
            text="Consultant",
            relief="groove",
            padx=10,
            pady=5,
            borderwidth=2,
            bg="white",
            fg="black",
        )
        consultant_label.pack(side="left")
        TyFrame.pack(pady=(0, 14), padx=(0, 114))

        RFrame = ttk.Frame(master=self)
        r_label = ttk.Label(
            master=RFrame, text="Request Description:", font="Montserrat 9 bold"
        )
        r_label.pack(anchor="nw", side="left", padx=(0, 10))
        r_textbox = tk.Text(master=RFrame, width=30, height=6)
        r_textbox.pack(side="left")
        RFrame.pack(pady=(0, 14), padx=(0, 116))

        CatFrame = ttk.Frame(master=self)
        cat_label = ttk.Label(
            master=CatFrame, text="Category:", font="Montserrat 9 bold"
        )
        cat_label.pack(anchor="w", side="left", padx=(0, 10))
        categories = [c.name for c in categories_dict.values()]
        cb = ttk.Combobox(
            master=CatFrame, state="readonly", values=categories, width=28
        )
        cb.pack(side="left")
        CatFrame.pack(pady=(0, 14), padx=(0, 44))

        EstFrame = ttk.Frame(master=self)
        est_label = ttk.Label(
            master=EstFrame, text="Estimated hours:", font="Montserrat 9 bold"
        )
        est_label.pack(anchor="w", side="left", padx=(0, 10))
        est_entry = ttk.Entry(master=EstFrame, width=8)
        est_entry.insert(0, "")
        est_entry.bind("<FocusIn>", lambda e: est_entry.delete(0, "end"))
        est_entry.bind("<Return>", lambda e: print(e.widget.get()))
        est_entry.pack(side="left")
        EstFrame.pack(pady=(0, 40), padx=(0, 232))

        CompFrame = ttk.Frame(master=self)
        cmp_label = ttk.Label(
            master=CompFrame, text="Compensation ($):", font="Montserrat 9 bold"
        )
        cmp_label.pack(anchor="w", side="left", padx=(0, 10))
        cmp_entry = ttk.Entry(master=CompFrame, width=8)
        cmp_entry.insert(0, "")
        cmp_entry.bind("<FocusIn>", lambda e: cmp_entry.delete(0, "end"))
        cmp_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cmp_entry.pack(side="left")
        CompFrame.pack(pady=(0, 40), padx=(0, 232))

        style = ttk.Style()
        style.configure("Custom.TButton", background="#8C2F39", foreground="white")
        p_button = ttk.Button(
            master=self, text="Submit Request", style="Custom.TButton"
        )
        p_button.pack(pady=(0, 14))

        # Bind left mouse button click event to the label
        # course_label.bind("<Button-1>", on_label_clicked)
        # consultant_label.bind("<Button-1>", on_label_clicked2)

    def show(self, context=None):
        if context is not None:
            self.create_widgets()
        self.pack(pady=20)
        self.back_button.place(x=50, y=150)

    def hide(self):
        self.back_button.place_forget()
        self.pack_forget()
