import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class ReviewReport(ttk.Frame):

    def __init__(self, master, report, **kwargs):
        super().__init__(master, **kwargs)
        self.report = report
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        ReviewReportFrame =  ttk.Frame(master = self.master)
        intro_label = ttk.Label(master=ReviewReportFrame, text='Reviewing report', font= 'Montserrat 16 bold')
        intro_label.pack()
        top_frame = ttk.Frame(master=ReviewReportFrame)
        right_frame = ttk.Frame(master = top_frame)
        left_frame = ttk.Frame(master = top_frame)
        rest_frame = ttk.Frame(master=ReviewReportFrame)

        #left frame
        created_label = ttk.Label(master=left_frame, text= 'Submitted by:', font= 'Montserrat 12 bold')
        created_label.pack()
        name_label = ttk.Label(master=left_frame, text= self.report.posted_by.name, font= 'Montserrat 12 bold')
        name_label.pack()

        #right frame
        details_label = ttk.Label(master=right_frame, text= 'Report Details', font= 'Montserrat 12 bold')
        details_label.pack()
        subject_label = ttk.Label(master=right_frame, text='Subject : '+ self.report.subject, font= 'Montserrat 7 bold')
        subject_label.pack()        
        description_label = ttk.Label(master=right_frame, text='Description : '+ self.report.description, font= 'Montserrat 7 bold')
        description_label.pack()
        attachment_label = ttk.Label(master=right_frame, text='Attachments : '+ self.report.media, font= 'Montserrat 7 bold')
        attachment_label.pack()
        posted_on_label = ttk.Label(master=right_frame, text='Posted on: ' + self.report.posted_on, font= 'Montserrat 7',foreground="#ADADAD")
        posted_on_label.pack()
        posted_for_label = ttk.Label(master=right_frame, text='Concerning user: ' + self.report.posted_for.name, font= 'Montserrat 7',foreground="#ADADAD")
        posted_for_label.pack()
        
        #rest

        actions_label = ttk.Label(master=rest_frame, text= 'Actions', font= 'Montserrat 9 bold',foreground='white', background='black')
        actions_label.pack()
        check1 = ttk.Checkbutton(master = rest_frame, text = 'Ban user from platform')
        check2 = ttk.Checkbutton(master = rest_frame, text = 'Just remove relevant content')
        check1.pack()
        check2.pack()
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        review_button = ttk.Button(master=rest_frame, text= "Complete Review" , style='Custom.TButton')
        review_button.pack()


        left_frame.pack(side='left')
        right_frame.pack(side='left')
        top_frame.pack()
        rest_frame.pack()

        ReviewReportFrame.pack(pady=20)
