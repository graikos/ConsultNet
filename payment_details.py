import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image

class PaymentInfo(ttk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        AddDetailsFrame = ttk.Frame (master=self)
        details_label = ttk.Label(master=AddDetailsFrame, text='Add payment details', font= 'Montserrat 12', foreground="#ADADAD")
        details_label.pack(side='left')
        AddDetailsFrame.pack()
        payment_label = ttk.Label(master=self, text='Payment method', font= 'Montserrat 9 bold')
        payment_label.pack()
        ChooseOptionFrame = ttk.Frame(master=self)
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        creditcard_button = ttk.Button(master=ChooseOptionFrame, text= "Credit Card" , style='Custom.TButton')
        style.configure('Custom2.TButton', background='white', foreground = 'black')
        banktransfer_button = ttk.Button(master=ChooseOptionFrame, text= "Bank Transfer" , style='Custom2.TButton')
        creditcard_button.pack(side='left')
        banktransfer_button.pack(side='left')
        ChooseOptionFrame.pack()
        paymentdetails_label = ttk.Label(master=self, text='Payment details', font= 'Montserrat 9 bold')
        paymentdetails_label.pack()
        cardholder_entry = ttk.Entry(master = self, width = 50)
        cardholder_entry.insert(0, 'Cardholder name')
        cardholder_entry.bind("<FocusIn>", lambda e: cardholder_entry.delete(0, 'end'))
        cardholder_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cardholder_entry.pack()
        cardnumber_entry = ttk.Entry(master = self, width = 50)
        cardnumber_entry.insert(0, 'Card number')
        cardnumber_entry.bind("<FocusIn>", lambda e: cardnumber_entry.delete(0, 'end'))
        cardnumber_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cardnumber_entry.pack()

        CVVEXPrame = ttk.Frame(master=self)

        cvv_entry = ttk.Entry(master = CVVEXPrame, width = 50)
        cvv_entry.insert(0, 'CVV')
        cvv_entry.bind("<FocusIn>", lambda e: cvv_entry.delete(0, 'end'))
        cvv_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cvv_entry.pack(side='left')
        exp_label = ttk.Label(master=CVVEXPrame, text='Exp.date', font= 'Montserrat 9', foreground="#ADADAD")
        exp_label.pack(side='left')
        MMYY_entry = ttk.Entry(master = CVVEXPrame, width = 50)
        MMYY_entry.insert(0, 'CVV')
        MMYY_entry.bind("<FocusIn>", lambda e: MMYY_entry.delete(0, 'end'))
        MMYY_entry.bind("<Return>", lambda e: print(e.widget.get()))
        MMYY_entry.pack(side='left')
        CVVEXPrame.pack()
        terms = ttk.Checkbutton(master = self, text = 'I have read and accept the Terms & Conditions')
        terms.pack()
        style.configure('Custom3.TButton', background='#8C2F39', foreground = 'white')
        price_button = ttk.Button(master=self, text= "Confirm payment" , style='Custom3.TButton')
        price_button.pack()

        self.pack()


    