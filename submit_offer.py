import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class SubmitOffer(ttk.Frame):

    def __init__(self, master, request, **kwargs):
        super().__init__(master, **kwargs)
        self.request = request
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        SubmitOfferFrame =  ttk.Frame(master = self.master)
        intro_label = ttk.Label(master=SubmitOfferFrame, text='Submitting an offer for : '+ str(self.request.name), font= 'Montserrat 16 bold')
        intro_label.pack()
        top_frame = ttk.Frame(master=SubmitOfferFrame)
        right_frame = ttk.Frame(master = top_frame)
        left_frame = ttk.Frame(master = top_frame)
        rest_frame = ttk.Frame(master=SubmitOfferFrame)

        #left frame
        created_label = ttk.Label(master=left_frame, text= 'Created by:', font= 'Montserrat 12 bold')
        created_label.pack()
        name_label = ttk.Label(master=left_frame, text= self.request.user.name, font= 'Montserrat 12 bold')
        name_label.pack()

        #right frame
        details_label = ttk.Label(master=right_frame, text= 'Request Details', font= 'Montserrat 12 bold')
        details_label.pack()
        description_label = ttk.Label(master=right_frame, text='Description : '+ self.request.description, font= 'Montserrat 7 bold')
        description_label.pack()
        esth_label =  ttk.Label(master=right_frame, text='Estimated Hours: ' + str(self.request.esth), font= 'Montserrat 7 bold')
        esth_label.pack()
        comp_label =  ttk.Label(master=right_frame, text='Compensation: ' + str(self.request.compensation), font= 'Montserrat 7 bold')
        comp_label.pack()        
        posted_on_label = ttk.Label(master=right_frame, text='Posted on: ' + self.request.posted_on, font= 'Montserrat 7',foreground="#ADADAD")
        posted_on_label.pack()
        reqcat_label = ttk.Label(master=right_frame, text='Request Category: ' + self.request.category, font= 'Montserrat 7',foreground="#ADADAD")
        reqcat_label.pack()
        
        #rest

        offer_details_label = ttk.Label(master=rest_frame, text= 'Add Offer Details (Optional)', font= 'Montserrat 9 bold',foreground='white', background='black')
        offer_details_label.pack()

        EHFrame = ttk.Frame(master=rest_frame)
        eh_label = ttk.Label(master=EHFrame, text='Estimated Hours (counteroffer): ', font= 'Montserrat 9 bold')
        eh_label.pack(side='left')
        eh_entry = ttk.Entry(master = EHFrame, width = 50)
        eh_entry.insert(0, '')
        eh_entry.bind("<FocusIn>", lambda e: eh_entry.delete(0, 'end'))
        eh_entry.bind("<Return>", lambda e: print(e.widget.get()))
        eh_entry.pack(side='left')
        EHFrame.pack()

        CMPFrame = ttk.Frame(master=rest_frame)
        cmp_label = ttk.Label(master=CMPFrame, text='Compensation (counteroffer): ', font= 'Montserrat 9 bold')
        cmp_label.pack(side='left')
        cmp_entry = ttk.Entry(master = CMPFrame, width = 50)
        cmp_entry.insert(0, '')
        cmp_entry.bind("<FocusIn>", lambda e: cmp_entry.delete(0, 'end'))
        cmp_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cmp_entry.pack(side='left')
        CMPFrame.pack()

        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        offer_button = ttk.Button(master=rest_frame, text= "Submit Offer" , style='Custom.TButton')
        offer_button.pack()

        left_frame.pack(side='left')
        right_frame.pack(side='left')
        top_frame.pack()
        rest_frame.pack()

        SubmitOfferFrame.pack(pady=20)


    