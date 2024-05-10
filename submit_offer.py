import tkinter as tk
import ttkbootstrap as ttk
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
        intro_label = ttk.Label(master=self, text='Submitting an offer for: '+ str(self.request.name), font= 'Montserrat 16 bold')
        intro_label.pack(pady=(20,40))
        top_frame = ttk.Frame(master=self)
        right_frame = ttk.Frame(master = top_frame)
        left_frame = ttk.Frame(master = top_frame)
        rest_frame = ttk.Frame(master=self)

        #left frame
        created_label = ttk.Label(master=left_frame, text= 'Created by:', font= 'Montserrat 9')
        created_label.pack()
        name_label = ttk.Label(master=left_frame, text= self.request.user.name, font= 'Montserrat 15 bold')
        name_label.pack()

        #right frame
        details_label = ttk.Label(master=right_frame, text= 'Request Details', font= 'Montserrat 15',foreground="#ADADAD")
        details_label.pack(pady=(0,20))
        description_frame = ttk.Frame(master=right_frame)
        description_frame.pack(anchor='w',padx=(38,0))
        description_label1 = ttk.Label(master=description_frame, text='Description:', font='Montserrat 9 bold')
        description_label1.pack(anchor='nw', side='left',padx=(0,20))
        description_paragraph = ttk.Label(master=description_frame,  text=self.request.description, font='Montserrat 9', wraplength=600)
        description_paragraph.pack(anchor='w', side='left')

        esth_frame = ttk.Frame(master=right_frame)
        esth_frame.pack(anchor='w',padx=(10,0))
        esth_label1 = ttk.Label(master=esth_frame, text='Estimated hours:', font='Montserrat 9 bold')
        esth_label1.pack(anchor='w', side='left',padx=(0,20))
        esth_label2 = ttk.Label(master=esth_frame,  text= str(self.request.esth), font='Montserrat 9', wraplength=600)
        esth_label2.pack(anchor='w', side='left')

        comp_frame = ttk.Frame(master=right_frame)
        comp_frame.pack(anchor='w',padx=(20,0))
        comp_label1 = ttk.Label(master=comp_frame, text='Compensation:', font='Montserrat 9 bold')
        comp_label1.pack(anchor='w', side='left',padx=(0,20))
        comp_label2 = ttk.Label(master=comp_frame,  text=str(self.request.compensation), font='Montserrat 9', wraplength=600)
        comp_label2.pack(anchor='w', side='left')
     


        posted_on_frame = ttk.Frame(master=right_frame)
        posted_on_frame.pack(anchor='w',padx=(50,0))
        posted_on_label1 = ttk.Label(master=posted_on_frame, text='Posted on:', font='Montserrat 9 bold')
        posted_on_label1.pack(anchor='w', side='left',padx=(0,20))
        posted_on_label2 = ttk.Label(master=posted_on_frame,  text=self.request.posted_on, font='Montserrat 9', wraplength=600)
        posted_on_label2.pack(anchor='w', side='left')

        reqcat_frame = ttk.Frame(master=right_frame)
        reqcat_frame.pack(anchor='w')
        reqcat_label1 = ttk.Label(master=reqcat_frame, text='Request Category:', font='Montserrat 9 bold')
        reqcat_label1.pack(anchor='w', side='left',padx=(0,20))
        reqcat_label2 = ttk.Label(master=reqcat_frame,  text=self.request.category, font='Montserrat 9', wraplength=600)
        reqcat_label2.pack(anchor='w', side='left')
        
        #rest

        offer_details_label = ttk.Label(master=rest_frame, text= 'Add Offer Details', font= 'Montserrat 15',foreground="#ADADAD")
        offer_details_label.pack(fill='x', anchor='center',pady=20,padx=(0,300))

        EHFrame = ttk.Frame(master=rest_frame)
        eh_label = ttk.Label(master=EHFrame, text='Estimated Hours (counteroffer): ', font= 'Montserrat 9 bold')
        eh_label.pack(side='left',padx=(0,20))
        eh_entry = ttk.Entry(master = EHFrame, width = 20)
        eh_entry.insert(0, '')
        eh_entry.bind("<FocusIn>", lambda e: eh_entry.delete(0, 'end'))
        eh_entry.bind("<Return>", lambda e: print(e.widget.get()))
        eh_entry.pack(side='left')
        EHFrame.pack(pady=5,padx=(0,404))

        CMPFrame = ttk.Frame(master=rest_frame)
        cmp_label = ttk.Label(master=CMPFrame, text='Compensation (counteroffer): ', font= 'Montserrat 9 bold')
        cmp_label.pack(side='left',padx=(10,20))
        cmp_entry = ttk.Entry(master = CMPFrame, width = 20)
        cmp_entry.insert(0, '')
        cmp_entry.bind("<FocusIn>", lambda e: cmp_entry.delete(0, 'end'))
        cmp_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cmp_entry.pack(side='left')
        CMPFrame.pack(pady=5,padx=(0,404))

        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white', font='Montserrat 11 bold')
        offer_button = ttk.Button(master=rest_frame, text= "Submit Offer" , style='Custom.TButton',width= 26)
        offer_button.pack(pady=(20,0))

        left_frame.pack(anchor='nw',side='left',pady=35)
        right_frame.pack(side='left',padx=300)
        top_frame.pack()
        rest_frame.pack(fill='both',pady=30)

        self.pack(pady=20)


    