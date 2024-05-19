import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image

class RequestItem(ttk.Frame):

    def __init__(self, master, request, **kwargs):
        super().__init__(master, width=500, height=1000, borderwidth=2, relief="ridge", **kwargs)
        self.request = request
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        right_frame = ttk.Frame(master=self)
        left_frame = ttk.Frame(master = self)

        #left frame
        for cat in self.request.category:
            category_label = ttk.Label(master=left_frame, text= cat, font= 'Montserrat 9 bold',foreground='white', background='black')
            category_label.pack(anchor="w",pady=(0,10))
        title_label = ttk.Label(master=left_frame, text= self.request.name, font= 'Montserrat 15 bold')
        title_label.pack(anchor="w")
        description_label = ttk.Label(master=left_frame, text= self.request.description, font= 'Montserrat 7',wraplength=600)
        description_label.pack(anchor="w",pady=10)
        author_label = ttk.Label(master=left_frame, text='AuthorIcon: ' + self.request.user.name, font= 'Montserrat 9')
        author_label.pack(anchor="w")

        #right frame 
        EHFrame = ttk.Frame(master=right_frame)
        eh_label1 = ttk.Label(master=EHFrame, text='Estimated Hours: ', font= 'Montserrat 9 bold', foreground="#ADADAD")
        eh_label1.pack(side='left')
        eh_label2 = ttk.Label(master=EHFrame, text= self.request.esth, font= 'Montserrat 9 bold', foreground="#ADADAD")
        eh_label2.pack(side='left',padx=(0,20))
        eh_label2.pack(side='left')
        EHFrame.pack()
        cmp_label1 =  ttk.Label(master=right_frame, text='Compensation ', font= 'Montserrat 11 bold', foreground="#ADADAD")
        cmp_label1.pack(padx=(0,20),pady=(50,4))
        cmp_label2 =  ttk.Label(master=right_frame, text=self.request.compensation, font= 'Montserrat 14 bold')
        cmp_label2.pack(padx=(0,20))
        left_frame.pack(side = 'left',padx=20)
        right_frame.pack(side = 'left',anchor="n", padx=20)

        self.show()

    def show(self):
        self.pack(side='top',pady=30,fill='x',padx=(320,480),ipady=10)

    def hide(self):
        self.pack_forget()



    