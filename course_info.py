import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class CourseInfo(ttk.Frame):

    def __init__(self, master, course, **kwargs):
        super().__init__(master, **kwargs)
        self.course = course
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        intro_label = ttk.Label(master=self, text='Showing details for course: '+ str(self.course.name), font= 'Montserrat 16 bold')
        intro_label.pack()
        right_frame = ttk.Frame(master = self)
        left_frame = ttk.Frame(master = self)
        bottom_frame = ttk.Frame(master=left_frame)
        
        # left frame
        title_label = ttk.Label(master=left_frame, text='Course Details', font= 'Montserrat 15 bold')
        title_label.pack()
        description_frame = ttk.Frame(master=left_frame)
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
        sales_frame = ttk.Frame(master=left_frame)
        sales_label1 = ttk.Label(
            sales_frame, text="Purchased by:", font="Montserrat 9 bold"
        )
        sales_label1.pack(anchor="w", padx=(0, 20), side="left")
        sales_label2 = ttk.Label(
            sales_frame, text=str(self.course.num_of_sales), font="Montserrat 9"
        )
        sales_label2.pack(anchor="w", side="left")
        sales_frame.pack(anchor="w")
        posted_on_frame = ttk.Frame(master=left_frame)
        posted_on_label1 = ttk.Label(
            master=posted_on_frame, text="Posted on:", font="Montserrat 9 bold"
        )
        posted_on_label1.pack(anchor="w", side="left", padx=(0, 20))
        posted_on_label2 = ttk.Label(
            master=posted_on_frame, text=self.course.posted_on, font="Montserrat 9 "
        )
        posted_on_label2.pack(anchor="w", side="left")
        posted_on_frame.pack(anchor="w", padx=(22, 0))
        final_exam_frame = ttk.Frame(master=left_frame)
        final_exam_label1 = ttk.Label(
            master=final_exam_frame, text="Final Exam:", font="Montserrat 9 bold"
        )
        final_exam_label1.pack(anchor="w", side="left", padx=(0, 20))
        final_exam_label2 = ttk.Label(
            master=final_exam_frame, text=self.course.final_exam, font="Montserrat 9"
        )
        final_exam_label2.pack(anchor="w", side="left")
        final_exam_frame.pack(anchor="w", padx=(16, 0))
        category_frame = ttk.Frame(master=left_frame)
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
        media_frame = ttk.Frame(master=left_frame)
        media_label1 = ttk.Label(
            master=media_frame, text="Media:", font="Montserrat 9 bold"
        )
        media_label1.pack(anchor="w", side="left", padx=(0, 20))
        media_label2 = ttk.Label(
            master=media_frame, text=str(self.course.media.type), font="Montserrat 9"
        )
        media_label2.pack(anchor="w", side="left")
        media_frame.pack(anchor="w", padx=(46, 0))

        add_label = ttk.Label(
            master=left_frame, text="Course Add-Ons", font="Montserrat 15 bold"
        )
        add_label.pack(pady=10)

        for i, ao in enumerate(self.course.add_ons):
            chvar = tk.IntVar()
            ch = ttk.Label(
                master=left_frame,
                text=ao.name + f" (${ao.price})",
            )
            ch.pack(anchor="w", padx=(200,0), pady=15)

        #right frame 
        title2_label = ttk.Label(master=right_frame,text='Ratings', font= 'Montserrat 15 bold' )
        title2_label.pack(pady=10)

        content_frame = ttk.Frame(master=right_frame)
 
        categories = ['1', '2', '3','4','5']
        values = [25, 30, 20, 35,40]

        # Define colors
        darker_orange = '#FFCE21'  # Slightly darker shade of orange
        gray = '#ADADAD'  # Gray color for text

        # Create a figure and plot
        fig, ax = plt.subplots(figsize=(4, 3))
        bars = ax.barh(categories, values, color=darker_orange, height = 0.4)  # Use barh for horizontal bar plot

        # Add text annotations with padding and formatting
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height() / 2, f'({width})', va='center', color=gray)

        ax.xaxis.set_visible(False)
        ax.set_title('Avg Score/sum of all ratings')
        # Remove the spines
        for spine in ax.spines.values():
            spine.set_visible(False)

        # Adjust the font size of the y-axis labels
        ax.tick_params(axis='y', labelsize=12)  # Adjust the label size as needed

        # Remove the default ticks and gridlines to ensure no extra formatting
        ax.tick_params(left=False)
        ax.grid(False)
        # Create a canvas
        canvas = FigureCanvasTkAgg(fig, master=content_frame)
        canvas.draw()

        # Place the canvas on the tkinter window
        canvas.get_tk_widget().pack()

        content_frame.configure(borderwidth=2, relief="ridge")
        
        content_frame.pack()

        right_frame.pack(side="left", pady=60, padx=40,anchor='nw')
        left_frame.pack(side="left", pady=60, padx=40)

        #bottom frame
        price_frame = ttk.Frame(master=bottom_frame)
        price_label1 = ttk.Label(
            price_frame, text="Course price:", font="Montserrat 9 bold"
        )
        price_label1.pack(anchor="e", padx=(0, 20), side="left")
        price_label2 = ttk.Label(
            price_frame, text='$'+str(self.course.price), font="Montserrat 9"
        )
        price_label2.pack(anchor="e", side="left")
        price_frame.pack(anchor="e")

        sales_frame = ttk.Frame(master=bottom_frame)
        sales_label1 = ttk.Label(
            sales_frame, text="Purchased by:", font="Montserrat 9 bold"
        )
        sales_label1.pack(anchor="e", padx=(0, 20), side="left")
        sales_label2 = ttk.Label(
            sales_frame, text=str(self.course.num_of_sales), font="Montserrat 9"
        )
        sales_label2.pack(anchor="e", side="left")
        sales_frame.pack(anchor="e")

        dot_label1 = ttk.Label(master=bottom_frame, text="______________________________",font="Montserrat 5 bold")
        dot_label1.pack(anchor="e")

        gross_frame = ttk.Frame(master=bottom_frame)
        gross_label1 = ttk.Label(
            gross_frame, text="Gross Revenue:", font="Montserrat 9 bold"
        )
        gross_label1.pack(anchor="e", padx=(0, 20), side="left")
        gross_label2 = ttk.Label(
            gross_frame, text="$"+str(self.course.num_of_sales * self.course.price), font="Montserrat 9"
        )
        gross_label2.pack(anchor="e", side="left")
        gross_frame.pack(anchor="e")

        pl_frame = ttk.Frame(master=bottom_frame)
        pl_label1 = ttk.Label(
            pl_frame, text="Platform Fees:", font="Montserrat 9 bold",foreground="#ADADAD"
        )
        pl_label1.pack(anchor="e", padx=(0, 20), side="left")
        pl_label2 = ttk.Label(
            pl_frame, text="$"+str(self.course.num_of_sales * self.course.price*7/100), font="Montserrat 9",foreground="#ADADAD"
        )
        pl_label2.pack(anchor="e", side="left")
        pl_frame.pack(anchor="e")

        dot_label2 = ttk.Label(master=bottom_frame, text="______________________________",font="Montserrat 5 bold")
        dot_label2.pack(anchor="e")

        net_frame = ttk.Frame(master=bottom_frame)
        net_label1 = ttk.Label(
            net_frame, text="Net Revenue:", font="Montserrat 14 bold"
        )
        net_label1.pack(anchor="e", padx=(0, 20), side="left")
        net_label2 = ttk.Label(
            net_frame, text="$"+str((self.course.num_of_sales * self.course.price) -self.course.num_of_sales * self.course.price*7/100), font="Montserrat 14"
        )
        net_label2.pack(anchor="e", side="left")
        net_frame.pack(anchor="e")

        bottom_frame.pack(pady=50,anchor='se')
        self.pack(pady=60)


    