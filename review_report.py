import tkinter as tk
import ttkbootstrap as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class ReviewReportPage(ttk.Frame):

    def __init__(self, master, report, **kwargs):
        super().__init__(master, **kwargs)
        self.report = report
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        intro_label = ttk.Label(master=self, text='Reviewing report', font= 'Montserrat 16 bold')
        intro_label.pack(pady=(20,40))
        top_frame = ttk.Frame(master=self)
        right_frame = ttk.Frame(master = top_frame)
        left_frame = ttk.Frame(master = top_frame)
        rest_frame = ttk.Frame(master=self)


        #left frame
        created_label = ttk.Label(master=left_frame, text= 'Submitted by:', font= 'Montserrat 9')
        created_label.pack()
        name_label = ttk.Label(master=left_frame, text= self.report.posted_by.name, font= 'Montserrat 15 bold')
        name_label.pack()

        #right frame
        details_label = ttk.Label(master=right_frame, text= 'Report Details',font= 'Montserrat 15',foreground="#ADADAD")
        details_label.pack(pady=(0,20),padx=(0,140))

        
        subject_frame = ttk.Frame(master=right_frame)
        subject_frame.pack(anchor='w',padx=(68,0))
        subject_label1 = ttk.Label(master=subject_frame, text='Subject:', font='Montserrat 9 bold')
        subject_label1.pack(anchor='nw', side='left',padx=(0,20))
        subject_label2 = ttk.Label(master=subject_frame, text=self.report.subject, font='Montserrat 9', wraplength=600)
        subject_label2 .pack(anchor='w', side='left')

        description_frame = ttk.Frame(master=right_frame)
        description_frame.pack(anchor='w',padx=(42,0))
        description_label1 = ttk.Label(master=description_frame, text='Description:', font='Montserrat 9 bold')
        description_label1.pack(anchor='nw', side='left',padx=(0,20))
        description_paragraph = ttk.Label(master=description_frame,  text=self.report.description, font='Montserrat 9', wraplength=600)
        description_paragraph.pack(anchor='w', side='left')

        attatchments_frame= ttk.Frame(master=right_frame)
        attatchments_frame.pack(anchor='w',padx=(34,0))
        attatchments_label1 = ttk.Label(master=attatchments_frame, text='Attachments:', font='Montserrat 9 bold')
        attatchments_label1.pack(anchor='w', side='left',padx=(0,20))
        attatchments_label2 = ttk.Label(master=attatchments_frame,  text= self.report.media, font='Montserrat 9', wraplength=600)
        attatchments_label2.pack(anchor='w', side='left')

        posted_on_frame = ttk.Frame(master=right_frame)
        posted_on_frame.pack(anchor='w',padx=(52,0))
        posted_on_label1 = ttk.Label(master=posted_on_frame, text='Posted on:', font='Montserrat 9 bold')
        posted_on_label1.pack(anchor='w', side='left',padx=(0,20))
        posted_on_label2 = ttk.Label(master=posted_on_frame,  text=self.report.posted_on, font='Montserrat 9', wraplength=600)
        posted_on_label2.pack(anchor='w', side='left')

        posted_for_frame = ttk.Frame(master=right_frame)
        posted_for_frame.pack(anchor='w',padx=(50,0))
        posted_for_label1 = ttk.Label(master=posted_for_frame, text='Posted for:', font='Montserrat 9 bold')
        posted_for_label1.pack(anchor='w', side='left',padx=(0,20))
        posted_for_label2 = ttk.Label(master=posted_for_frame,  text=self.report.posted_for.name, font='Montserrat 9', wraplength=600)
        posted_for_label2.pack(anchor='w', side='left')
        
        #rest

        actions_label = ttk.Label(master=rest_frame, text= 'Actions', font= 'Montserrat 15',foreground="#ADADAD")
        actions_label.pack(fill='x', anchor='center',pady=20,padx=(24,0))

        check1 = ttk.Checkbutton(master = rest_frame, text = 'Ban user from platform')
        check2 = ttk.Checkbutton(master = rest_frame, text = 'Just remove relevant content')
        check1.pack(anchor='center',pady=(4,10),padx=(0,248))
        check2.pack(anchor='center',pady=(0,10),padx=(0,218))
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        review_button = ttk.Button(master=rest_frame, text= "Complete Review" , style='Custom.TButton',width= 26)
        review_button.pack(pady=(30,0))


        left_frame.pack(anchor='nw',side='left',pady=35)
        right_frame.pack(side='left',padx=300)
        top_frame.pack()
        rest_frame.pack(fill='both',pady=30)

        self.pack(pady=20)




    
