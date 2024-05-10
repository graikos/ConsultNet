import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageDraw
import ttkbootstrap as ttk

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

class CoursePurchase(ttk.Frame):

    def __init__(self, master, course, **kwargs):
        super().__init__(master, **kwargs)
        self.course = course
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        titleFrame = ttk.Frame(master=self)
        intro_label1 = ttk.Label(master=titleFrame, text='Purchasing course: ', font= 'Montserrat 16 bold')
        intro_label2 = ttk.Label(master=titleFrame, text= str(self.course.name), font= 'Montserrat 16 bold',foreground='#8C2F39')
        intro_label1.pack(side='left')
        intro_label2.pack(side='left')
        titleFrame.pack()
        right_frame = ttk.Frame(master = self)
        left_frame = ttk.Frame(master = self)

        image_size = 200  # Specify the desired size for the circular image
        # Create a circular image label
        self.image = make_circle(self.course.cons.photo.path, image_size)

        #left frame
        f_label = ttk.Label(master=left_frame, text= 'Created by:', font= 'Montserrat 12 bold')
        f_label.pack()
        left_down_frame = ttk.Frame(master=left_frame,borderwidth=2, relief="ridge")
        empty_label = ttk.Label(master=left_down_frame , text='')
        empty_label.pack()
        for cat in self.course.cons.categories:
            category_label = ttk.Label(master=left_down_frame, text= cat, font= 'Montserrat 9 bold',foreground='white', background='black')
            category_label.pack(pady=(0,10))
        image_label = ttk.Label(left_down_frame, image=self.image)
        image_label.pack()    
        name_label = ttk.Label(master=left_down_frame, text= self.course.cons.name, font= 'Montserrat 12 bold')
        name_label.pack(pady=4)
        experience_label = ttk.Label(master=left_down_frame, text="Experience:  "+ self.course.cons.experience, font= 'Montserrat 8 ')
        experience_label.pack(anchor="w",padx=22,pady=10)
        education_label = ttk.Label(master=left_down_frame,  text="Education:  "+ self.course.cons.education, font= 'Montserrat 8 ')
        education_label.pack(anchor="w",padx=28,pady=(0,10))
        price_label = ttk.Label(master=left_down_frame, text='$' + str(self.course.cons.rate), font= 'Montserrat 10')
        price_label.pack()
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        price_button = ttk.Button(master=left_down_frame, text= "Hire now" , style='Custom.TButton')
        price_button.pack()
        left_down_frame.pack(pady=20,ipady=10)
        
        # right frame
        title_label = ttk.Label(master=right_frame, text='Course Details', font= 'Montserrat 15 bold', foreground="#ADADAD")
        title_label.pack()
        right_down_frame = ttk.Frame(master=right_frame)
        description_frame = ttk.Frame(master=right_down_frame)
        description_frame.pack(anchor='w',padx=(10,0))
        description_label1 = ttk.Label(master=description_frame, text='Description:', font='Montserrat 9 bold')
        description_label1.pack(anchor='nw', side='left',padx=(0,20))
        description_paragraph = ttk.Label(master=description_frame, text=self.course.description, font='Montserrat 9', wraplength=600)
        description_paragraph.pack(anchor='w', side='left')
        sales_frame = ttk.Frame(master=right_down_frame)
        sales_label1 = ttk.Label(sales_frame, text='Purchased by:', font= 'Montserrat 9 bold')
        sales_label1.pack(anchor='w',padx=(0,20),side='left')
        sales_label2 = ttk.Label(sales_frame, text= str(self.course.num_of_sales), font= 'Montserrat 9')
        sales_label2.pack(anchor='w',side='left')
        sales_frame.pack(anchor='w')
        posted_on_frame = ttk.Frame(master=right_down_frame)
        posted_on_label1 = ttk.Label(master=posted_on_frame, text='Posted on:', font= 'Montserrat 9 bold')
        posted_on_label1.pack(anchor='w',side='left',padx=(0,20))
        posted_on_label2 = ttk.Label(master=posted_on_frame, text=self.course.posted_on, font= 'Montserrat 9 ')
        posted_on_label2.pack(anchor='w',side='left')
        posted_on_frame.pack(anchor='w',padx=(22,0))
        final_exam_frame = ttk.Frame(master=right_down_frame)    
        final_exam_label1 = ttk.Label(master=final_exam_frame, text='Final Exam:', font= 'Montserrat 9 bold')
        final_exam_label1.pack(anchor='w',side='left',padx=(0,20))
        final_exam_label2 = ttk.Label(master=final_exam_frame, text=self.course.final_exam, font= 'Montserrat 9')
        final_exam_label2.pack(anchor='w',side='left')
        final_exam_frame.pack(anchor='w',padx=(16,0))
        category_frame = ttk.Frame(master=right_down_frame)
        category_label1 =  ttk.Label(master=category_frame, text="Category:", font= 'Montserrat 9 bold')
        category_label1.pack(anchor='w',side='left',padx=(0,20))
        for cat in self.course.categories:
            category_label2 = ttk.Label(master=category_frame, text= cat, font= 'Montserrat 9')
            category_label2.pack(anchor='w',side='left')
        category_frame.pack(anchor='w',padx=(28,0))
        media_frame = ttk.Frame(master=right_down_frame)    
        media_label1 = ttk.Label(master=media_frame, text='Media:', font= 'Montserrat 9 bold')
        media_label1.pack(anchor='w',side='left',padx=(0,20))
        media_label2 = ttk.Label(master=media_frame, text=str(self.course.media.type), font= 'Montserrat 9')
        media_label2.pack(anchor='w',side='left')
        media_frame.pack(anchor='w',padx=(46,0))        
        right_down_frame.pack(pady=20)

        left_frame.pack(side='left',pady=60, padx=40)
        right_frame.pack(side='left',pady=60,padx=40)

        add_label = ttk.Label(master=right_frame,text='Course Add-Ons', font= 'Montserrat 15 bold' )
        add_label.pack(pady=10)

        chvar = tk.IntVar()
        ch = ttk.Checkbutton(
                master=right_frame,
                text=self.course.add_ons,
                variable=chvar,
            )
        ch.state(["!alternate"])
        ch.pack(anchor="w", padx=20, pady=15)

        total_frame = ttk.Frame(master=right_frame)
        total_label1 = ttk.Label(master=total_frame, text='Total:', font= 'Montserrat 10 bold')
        total_label1.pack(side='left' ,padx=(0,10))
        total_label2 = ttk.Label(master=total_frame, text='$' + str(self.course.price), font= 'Montserrat 9 ')
        total_label2.pack(side='left')
        total_frame.pack(pady=15)       


        self.pack(pady=20)


    