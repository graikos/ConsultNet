import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class CoursePurchase(ttk.Frame):

    def __init__(self, master, course, **kwargs):
        super().__init__(master, **kwargs)
        self.course = course
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        CoursePurchaseFrame =  ttk.Frame(master = self.master)
        intro_label = ttk.Label(master=CoursePurchaseFrame, text='Purchasing course: '+ str(self.course.name), font= 'Montserrat 16 bold')
        intro_label.pack()
        right_frame = ttk.Frame(master = CoursePurchaseFrame)
        left_frame = ttk.Frame(master = CoursePurchaseFrame)

        #left frame
        for cat in self.course.cons.categories:
            category_label = ttk.Label(master=left_frame, text= cat, font= 'Montserrat 9 bold',foreground='white', background='black')
            category_label.pack()
        self.image = tk.PhotoImage(file=self.course.cons.photo.path)
        image_label = ttk.Label(left_frame, image=self.image)
        image_label.pack()    
        name_label = ttk.Label(master=left_frame, text= self.course.cons.name, font= 'Montserrat 12 bold')
        name_label.pack()
        experience_label = ttk.Label(master=left_frame, text= self.course.cons.experience, font= 'Montserrat 7 bold')
        experience_label.pack()
        education_label = ttk.Label(master=left_frame, text= self.course.cons.education, font= 'Montserrat 7 bold')
        education_label.pack()
        price_label = ttk.Label(master=left_frame, text='$' + str(self.course.cons.rate), font= 'Montserrat 10')
        price_label.pack()
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        price_button = ttk.Button(master=left_frame, text= "Hire now" , style='Custom.TButton')
        price_button.pack()
        
        # left frame
        title_label = ttk.Label(master=right_frame, text='Course Details', font= 'Montserrat 15 bold')
        title_label.pack()
        description_label = ttk.Label(master=right_frame, text='Description : '+ self.course.description, font= 'Montserrat 7 bold')
        description_label.pack()
        sales_label = ttk.Label(master=right_frame, text='Purchased by: '+ str(self.course.num_of_sales), font= 'Montserrat 7',foreground="#ADADAD")
        sales_label.pack()
        posted_on_label = ttk.Label(master=right_frame, text='Posted on: ' + self.course.posted_on, font= 'Montserrat 7',foreground="#ADADAD")
        posted_on_label.pack()
        final_exam_label = ttk.Label(master=right_frame, text='Final Exam: ' + self.course.final_exam, font= 'Montserrat 7',foreground="#ADADAD")
        final_exam_label.pack()
        for cat in self.course.categories:
            category_label = ttk.Label(master=right_frame, text= cat, font= 'Montserrat 9 bold',foreground='white', background='black')
            category_label.pack()
        media_label = ttk.Label(master=right_frame, text='Media: ' +  str(self.course.media.type), font= 'Montserrat 7',foreground="#ADADAD")
        media_label.pack()

        left_frame.pack(side='left',pady=60, padx=40)
        right_frame.pack(side='left',pady=30,padx=40)

        add_label = ttk.Label(master=right_frame,text='Course Add-Ons', font= 'Montserrat 15 bold' )
        add_label.pack()
 
        addon_label = ttk.Label(master=right_frame, text= self.course.add_ons, font= 'Montserrat 9 bold',foreground='white', background='black')
        addon_label.pack()

        total_label = ttk.Label(master=right_frame, text='Total:' + str(self.course.price), font= 'Montserrat 9 bold',foreground='white', background='black')
        total_label.pack()


        CoursePurchaseFrame.pack(pady=20)


    