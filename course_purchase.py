import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import ttkbootstrap as ttk
from payment_details import PaymentInfoFrame


def make_circle(image_path, size):
    # Load the image
    image = Image.open(image_path)
    image = image.resize((size, size))  # Resize the image to the desired size

    # Create a circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply the circular mask to the image
    image.putalpha(mask)

    return ImageTk.PhotoImage(image)


class CoursePurchasePage(ttk.Frame):

    def __init__(
        self, master, course=None, router=None, controller=None, context=None, **kwargs
    ):
        super().__init__(master, **kwargs)

        try:
            if context is None:
                raise ValueError
            self.course = context["course"]
        except (KeyError, ValueError):
            self.course = course

        self.controller = controller
        self.win_master = master
        self.add_on_cb = []
        self.router = router

        self.create_widgets()

    def create_widgets(self):

        self.current_total = self.course.price
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
        )
        profile_label.bind("<Button-1>", lambda e: print("Profile clicked"))
        profile_label.pack(side="right", padx=75)
        logo_frame.pack(fill="both")

        # Second row of labels
        options_frame = ttk.Frame(master=self)
        courses_label = ttk.Label(
            master=options_frame, text="Courses", font="Montserrat 12 underline bold"
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
            font="Montserrat 12",
            foreground="#ADADAD",
        )
        courses_label.pack(side="left", padx=20)
        consultants_label.pack(side="left", padx=20)
        requests_label.pack(side="left", padx=20)
        options_frame.pack(fill="both", pady=20)

        # Load the back arrow image
        self.back_arrow_image = tk.PhotoImage(file="./back_arrow.png")

        # Create a button with the arrow image
        self.back_button = ttk.Button(
            self.win_master,
            image=self.back_arrow_image,
            cursor="hand2",
            command=lambda: self.router("courses"),
        )
        self.back_button.place(x=50, y=150)

        # Get the window background color
        window_bg_color = 'white'

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
        titleFrame = ttk.Frame(master=self)
        intro_label1 = ttk.Label(
            master=titleFrame, text="Purchasing course: ", font="Montserrat 16 bold"
        )
        intro_label2 = ttk.Label(
            master=titleFrame,
            text=str(self.course.name),
            font="Montserrat 16 bold",
            foreground="#8C2F39",
        )
        intro_label1.pack(side="left")
        intro_label2.pack(side="left")
        titleFrame.pack(pady=(16,0))
        right_frame = ttk.Frame(master=self)
        left_frame = ttk.Frame(master=self)

        image_size = 200  # Specify the desired size for the circular image
        # Create a circular image label
        self.image = make_circle(self.course.cons.photo.path, image_size)

        # left frame
        f_label = ttk.Label(
            master=left_frame, text="Created by:", font="Montserrat 12 bold"
        )
        f_label.pack()
        left_down_frame = ttk.Frame(master=left_frame, borderwidth=2, relief="ridge")
        empty_label = ttk.Label(master=left_down_frame, text="")
        empty_label.pack()
        for cat in self.course.cons.categories:
            category_label = ttk.Label(
                master=left_down_frame,
                text=cat,
                font="Montserrat 9 bold",
                foreground="white",
                background="black",
            )
            category_label.pack(pady=(0, 10))
        image_label = ttk.Label(left_down_frame, image=self.image)
        image_label.pack()
        name_label = ttk.Label(
            master=left_down_frame,
            text=self.course.cons.name,
            font="Montserrat 12 bold",
        )
        name_label.pack(pady=4)
        experience_label = ttk.Label(
            master=left_down_frame,
            text="Experience:  " + self.course.cons.experience,
            font="Montserrat 8 ",
        )
        experience_label.pack(anchor="w", padx=22, pady=10)
        education_label = ttk.Label(
            master=left_down_frame,
            text="Education:  " + self.course.cons.education,
            font="Montserrat 8 ",
        )
        education_label.pack(anchor="w", padx=28, pady=(0, 10))
        price_label = ttk.Label(
            master=left_down_frame,
            text="$" + str(self.course.cons.rate),
            font="Montserrat 10",
        )
        price_label.pack()
        style = ttk.Style()
        style.configure("Custom.TButton", background="#8C2F39", foreground="white")
        price_button = ttk.Button(
            master=left_down_frame, text="Hire now", style="Custom.TButton"
        )
        price_button.pack()
        left_down_frame.pack(pady=20, ipady=10)

        # right frame
        title_label = ttk.Label(
            master=right_frame,
            text="Course Details",
            font="Montserrat 15 bold",
            foreground="#ADADAD",
        )
        title_label.pack()
        right_down_frame = ttk.Frame(master=right_frame)
        description_frame = ttk.Frame(master=right_down_frame)
        description_frame.pack(anchor="w", padx=(10, 0))
        description_label1 = ttk.Label(
            master=description_frame, text="Description:", font="Montserrat 9 bold"
        )
        description_label1.pack(anchor="nw", side="left", padx=(0, 20))
        description_paragraph = ttk.Label(
            master=description_frame,
            text=self.course.description,
            font="Montserrat 9",
            wraplength=600,
        )
        description_paragraph.pack(anchor="w", side="left")
        sales_frame = ttk.Frame(master=right_down_frame)
        sales_label1 = ttk.Label(
            sales_frame, text="Purchased by:", font="Montserrat 9 bold"
        )
        sales_label1.pack(anchor="w", padx=(0, 20), side="left")
        sales_label2 = ttk.Label(
            sales_frame, text=str(self.course.num_of_sales), font="Montserrat 9"
        )
        sales_label2.pack(anchor="w", side="left")
        sales_frame.pack(anchor="w")
        posted_on_frame = ttk.Frame(master=right_down_frame)
        posted_on_label1 = ttk.Label(
            master=posted_on_frame, text="Posted on:", font="Montserrat 9 bold"
        )
        posted_on_label1.pack(anchor="w", side="left", padx=(0, 20))
        posted_on_label2 = ttk.Label(
            master=posted_on_frame, text=self.course.posted_on, font="Montserrat 9 "
        )
        posted_on_label2.pack(anchor="w", side="left")
        posted_on_frame.pack(anchor="w", padx=(22, 0))
        final_exam_frame = ttk.Frame(master=right_down_frame)
        final_exam_label1 = ttk.Label(
            master=final_exam_frame, text="Final Exam:", font="Montserrat 9 bold"
        )
        final_exam_label1.pack(anchor="w", side="left", padx=(0, 20))
        final_exam_label2 = ttk.Label(
            master=final_exam_frame, text=self.course.final_exam, font="Montserrat 9"
        )
        final_exam_label2.pack(anchor="w", side="left")
        final_exam_frame.pack(anchor="w", padx=(16, 0))
        category_frame = ttk.Frame(master=right_down_frame)
        category_label1 = ttk.Label(
            master=category_frame, text="Category:", font="Montserrat 9 bold"
        )
        category_label1.pack(anchor="w", side="left", padx=(0, 20))
        for cat in self.course.categories:
            category_label2 = ttk.Label(
                master=category_frame, text=cat, font="Montserrat 9"
            )
            category_label2.pack(anchor="w", side="left")
        category_frame.pack(anchor="w", padx=(28, 0))
        media_frame = ttk.Frame(master=right_down_frame)
        media_label1 = ttk.Label(
            master=media_frame, text="Media:", font="Montserrat 9 bold"
        )
        media_label1.pack(anchor="w", side="left", padx=(0, 20))
        media_label2 = ttk.Label(
            master=media_frame, text=str(self.course.media.type), font="Montserrat 9"
        )
        media_label2.pack(anchor="w", side="left")
        media_frame.pack(anchor="w", padx=(46, 0))
        right_down_frame.pack(pady=20)

        left_frame.pack(side="left", pady=60, padx=40)
        right_frame.pack(side="left", pady=60, padx=40)

        add_label = ttk.Label(
            master=right_frame, text="Course Add-Ons", font="Montserrat 15 bold"
        )
        add_label.pack(pady=10)

        for i, ao in enumerate(self.course.add_ons):
            chvar = tk.IntVar()
            ch = ttk.Checkbutton(
                master=right_frame,
                text=ao.name + f" (${ao.price})",
                variable=chvar,
                onvalue=1,
                offvalue=0,
                command=lambda idx=i: self.add_on_toggle(idx),
            )
            ch.state(["!alternate"])
            ch.pack(anchor="w", padx=20, pady=15)
            self.add_on_cb.append((ch, chvar))

        total_frame = ttk.Frame(master=right_frame)
        total_label1 = ttk.Label(
            master=total_frame, text="Total:", font="Montserrat 10 bold"
        )
        total_label1.pack(side="left", padx=(0, 10))
        self.total_label2 = ttk.Label(
            master=total_frame, text=f"${self.current_total:.2f}"
        )
        self.total_label2.pack(side="left")
        total_frame.pack(pady=15)

        self.payment_details = PaymentInfoFrame(self.win_master, "course", controller=self)

    
    def get_add_ons(self):
        return list(map(lambda x: x[0], filter(lambda x: x[1][1].get() == 1,enumerate(self.add_on_cb))))

    def add_on_toggle(self, idx):
        var = self.add_on_cb[idx][1]
        ao = self.course.add_ons[idx]
        if var.get() == 1:
            self.update_current_total(self.current_total + ao.price)
            return
        self.update_current_total(self.current_total - ao.price)

    def update_current_total(self, new_total):
        self.total_label2.config(text=(f"${new_total:.2f}"))
        self.current_total = new_total

    def get_current_total(self):
        return self.current_total

    def show(self, context=None):
        if context is not None and context["course"] != self.course:
            self.course = context["course"]
            self.create_widgets()
        self.pack(pady=20)
        self.back_button.place(x=50, y=150)
        self.payment_details.show()

    def hide(self):
        self.back_button.place_forget()
        self.payment_details.hide()
        self.pack_forget()

    def complete_purchase(self):
        self.after(2000, lambda: self.router("courses"))
