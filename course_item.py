import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image

class CourseItem(ttk.Frame):

    def __init__(self, master, course, **kwargs):
        super().__init__(master, width=500, height=1000, borderwidth=2, relief="ridge", **kwargs)
        self.course = course
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        right_frame = ttk.Frame(master=self)
        middle_frame = ttk.Frame(master=self)
        left_frame = ttk.Frame(master = self)
        
        # left frame
        self.image = tk.PhotoImage(file=self.course.image.path)
        image_label = ttk.Label(left_frame, image=self.image)
        sales_label = ttk.Label(master=left_frame, text='Sales: '+ str(self.course.num_of_sales), font= 'Montserrat 7',foreground="#ADADAD")
        posted_on_label = ttk.Label(master=left_frame, text='Posted on: ' + self.course.posted_on, font= 'Montserrat 7',foreground="#ADADAD")
        final_exam_label = ttk.Label(master=left_frame, text='Final Exam: ' + self.course.final_exam, font= 'Montserrat 7',foreground="#ADADAD")
        add_ons_label = ttk.Label(master=left_frame, text='Add-ons: ' + self.course.add_ons, font= 'Montserrat 7',foreground="#ADADAD")
        media_label = ttk.Label(master=left_frame, text='Media: ' + str(self.course.media.type), font= 'Montserrat 7',foreground="#ADADAD")
        image_label.pack(anchor="w",pady=(0,15))
        sales_label.pack(anchor="w",padx=10)
        posted_on_label.pack(anchor="w",padx=10)
        final_exam_label.pack(anchor="w",padx=10)
        add_ons_label.pack(anchor="w",padx=10)
        media_label.pack(anchor="w",padx=10,pady=(0,10))

        #middle frame
        for cat in self.course.categories:
            category_label = ttk.Label(master=middle_frame, text= cat, font= 'Montserrat 9 bold',foreground='white', background='black')
            category_label.pack(anchor="w",pady=10)
        title_label = ttk.Label(master=middle_frame, text= self.course.name, font= 'Montserrat 15 bold')
        title_label.pack(anchor="w")
        description_label = ttk.Label(master=middle_frame, text= self.course.description, font= 'Montserrat 7',wraplength=600)
        description_label.pack(anchor="w",pady=10)
        author_label = ttk.Label(master=middle_frame, text='AuthorIcon: ' + self.course.cons.name, font= 'Montserrat 9')
        author_label.pack(anchor="w")

        #right frame 

        rating_label = ttk.Label(master=right_frame, text=str(self.course.rating) + '/5', font= 'Montserrat 9', foreground="#ADADAD")
        rating_label.pack(pady=(0,60))
        price1_label = ttk.Label(master=right_frame, text='Starting from', font= 'Montserrat 11')
        price2_label = ttk.Label(master=right_frame, text='$' + str(self.course.price), font= 'Montserrat 12 bold')
        price1_label.pack()
        price2_label.pack()
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        price_button = ttk.Button(master=right_frame, text= "Buy now",width=13, style='Custom.TButton',)
        price_button.pack(pady=(20,0))

        left_frame.pack(side = 'left')
        middle_frame.pack(side = 'left',anchor="n",padx=20)
        right_frame.pack(side = 'left',anchor="n", padx=20)
        self.show()

    def show(self):
        self.pack(side='top',pady=30,fill='x',padx=(300,350))

    def hide(self):
        self.pack_forget()


    