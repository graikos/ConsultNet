import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image
from RoundedLabel import RoundedLabel


class CourseItem(ttk.Frame):

    def __init__(self, master, course, command=None, **kwargs):
        super().__init__(
            master, width=500, height=1000, borderwidth=2, relief="ridge", **kwargs
        )
        self.course = course
        self.command=command
        # self.master = master
        self.create_widgets()

    def create_widgets(self):
        # TODO: change this text
        right_frame = ttk.Frame(master=self)
        middle_frame = ttk.Frame(master=self)
        left_frame = ttk.Frame(master=self)

        # left frame
        self.image = tk.PhotoImage(file=self.course.image.path)
        image_label = ttk.Label(left_frame, image=self.image)
        sales_label = ttk.Label(
            master=left_frame,
            text="Sales: " + str(self.course.num_of_sales),
            font="Montserrat 7",
            foreground="#ADADAD",
        )
        posted_on_label = ttk.Label(
            master=left_frame,
            text="Posted on: " + self.course.posted_on,
            font="Montserrat 7",
            foreground="#ADADAD",
        )
        final_exam_label = ttk.Label(
            master=left_frame,
            text="Final Exam: " + self.course.final_exam,
            font="Montserrat 7",
            foreground="#ADADAD",
        )

        if self.course.add_ons:
            a_text = ", ".join([x.name for x in self.course.add_ons])[:-2]
            add_ons_label = ttk.Label(
                master=left_frame,
                text="Add-ons: " + a_text,
                font="Montserrat 7",
                foreground="#ADADAD",
            )

        media_label = ttk.Label(
            master=left_frame,
            text="Media: " + str(self.course.media.type),
            font="Montserrat 7",
            foreground="#ADADAD",
        )
        image_label.pack(anchor="w", pady=(0, 15))
        sales_label.pack(anchor="w", padx=10)
        posted_on_label.pack(anchor="w", padx=10)
        final_exam_label.pack(anchor="w", padx=10)
        if self.course.add_ons:
            add_ons_label.pack(anchor="w", padx=10)
        media_label.pack(anchor="w", padx=10, pady=(0, 10))

        # middle frame
        for cat in self.course.categories:
            category_label = RoundedLabel(middle_frame, text=cat, radius=25, padding=10, bg="black", fg="white", font='Montserrat 8 bold', border_width=0)
            category_label.pack(anchor="w", pady=10)

            
        title_label = ttk.Label(
            master=middle_frame, text=self.course.name, font="Montserrat 15 bold"
        )
        title_label.pack(anchor="w")
        description_label = ttk.Label(
            master=middle_frame,
            text=self.course.description,
            font="Montserrat 7",
            wraplength=600,
        )
        description_label.pack(anchor="w", pady=10)
        author_label = ttk.Label(
            master=middle_frame,
            text="👤: " + self.course.cons.name,
            font="Montserrat 9",
        )
        author_label.pack(anchor="w")

        # right frame

        rating_label = ttk.Label(
            master=right_frame,
            text=str(self.course.rating) + "/5",
            font="Montserrat 9",
            foreground="#ADADAD",
        )
        rating_label.pack(pady=(0, 60))
        price1_label = ttk.Label(
            master=right_frame, text="Starting from", font="Montserrat 11"
        )
        price2_label = ttk.Label(
            master=right_frame,
            text="$" + str(self.course.price),
            font="Montserrat 12 bold",
        )
        price1_label.pack()
        price2_label.pack()
        style = ttk.Style()
        style.configure("Custom.TButton", background="#8C2F39", foreground="white",anchor='center')
        # Load the image
        shop_icon = tk.PhotoImage(file="shop.png")

        # Create the button with the image
        price_button = ttk.Button(
            master=right_frame,
            text="Buy now",
            width=14,  # Adjust the width as needed
            style="Custom.TButton",
            command=self.command,
            image=shop_icon,
            compound=tk.LEFT  # Use tk.LEFT instead of ttk.LEFT
        )
        price_button.image = shop_icon  # Retain a reference to the image to prevent it from being garbage collected
        price_button.pack(pady=(20, 0))  # Adjust padding as needed

        left_frame.pack(side="left")
        middle_frame.pack(side="left", anchor="n", padx=20)
        right_frame.pack(side="left", anchor="n", padx=20)
        self.show()

    def show(self):
        self.pack(side="top", pady=30, fill="x", padx=(300, 116))

    def hide(self):
        self.pack_forget()
