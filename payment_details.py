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
        details_label = ttk.Label(master=AddDetailsFrame, text='Add payment details', font= 'Montserrat 15 bold', foreground="#ADADAD")
        details_label.pack(side='left')
        AddDetailsFrame.pack(pady=20)
        payment_label = ttk.Label(master=self, text='Payment method', font= 'Montserrat 9 bold')
        payment_label.pack(pady=10)
        ChooseOptionFrame = ttk.Frame(master=self)
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        creditcard_button = ttk.Button(master=ChooseOptionFrame, text= "Credit Card" , style='Custom.TButton')
        style.configure('Custom2.TButton', background='white', foreground = 'black')
        banktransfer_button = ttk.Button(master=ChooseOptionFrame, text= "Bank Transfer" , style='Custom2.TButton')
        creditcard_button.pack(side='left',padx=5)
        banktransfer_button.pack(side='left',padx=5)
        ChooseOptionFrame.pack(pady=10)
        paymentdetails_label = ttk.Label(master=self, text='Payment details', font= 'Montserrat 9 bold')
        paymentdetails_label.pack(pady=15)
        cardholder_entry = ttk.Entry(master = self, width = 50 , foreground="#ADADAD",font= 'Montserrat 7')
        cardholder_entry.insert(0, 'Cardholder name')
        cardholder_entry.bind("<FocusIn>", lambda e: cardholder_entry.delete(0, 'end'))
        cardholder_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cardholder_entry.pack(pady=10)
        cardnumber_entry = ttk.Entry(master = self, width = 50, foreground="#ADADAD",font= 'Montserrat 7')
        cardnumber_entry.insert(0, 'Card number')
        cardnumber_entry.bind("<FocusIn>", lambda e: cardnumber_entry.delete(0, 'end'))
        cardnumber_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cardnumber_entry.pack(pady=(0,10))

        CVVEXPrame = ttk.Frame(master=self)

        cvv_entry = ttk.Entry(master = CVVEXPrame, width = 15, foreground="#ADADAD",font= 'Montserrat 7')
        cvv_entry.insert(0, 'CVV')
        cvv_entry.bind("<FocusIn>", lambda e: cvv_entry.delete(0, 'end'))
        cvv_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cvv_entry.pack(side='left',padx=(0,30))
        exp_label = ttk.Label(master=CVVEXPrame, text='Exp.date:', font= 'Montserrat 9', foreground="#ADADAD")
        exp_label.pack(side='left')
        MMYY_entry = ttk.Entry(master = CVVEXPrame, width = 18, foreground="#ADADAD",font= 'Montserrat 7')
        MMYY_entry.insert(0, 'MM/YY')
        MMYY_entry.bind("<FocusIn>", lambda e: MMYY_entry.delete(0, 'end'))
        MMYY_entry.bind("<Return>", lambda e: print(e.widget.get()))
        MMYY_entry.pack(side='left')
        CVVEXPrame.pack()
        terms = ttk.Checkbutton(master = self, text = 'I have read and accept the Terms & Conditions')
        terms.pack(pady=20)
        style.configure('Custom3.TButton', background='#8C2F39', foreground = 'white')
        price_button = ttk.Button(master=self, text= "Confirm payment" , style='Custom3.TButton')
        price_button.pack(pady=(0,50))

        self.pack()


    