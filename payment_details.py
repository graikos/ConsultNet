import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image
import re
from datetime import datetime
from interface.payment_gateway import PaymentGatewayInterface
from domain.payment import CoursePayment, course_payments
from enum import Enum


class PaymentInfoFrame(ttk.Frame):
    cardholder_str = "Cardholder name"
    card_num_str = "Card number"
    cvv_str = "CVV"
    exp_str = "MM/YY"

    @staticmethod
    def luhn_check(card_number):
        # Implement the Luhn algorithm to validate the card number
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10 == 0

    @staticmethod
    def validate_card_info(name, card_number, cvv, exp_date):
        # Validate cardholder name
        if not re.match(r"^[a-zA-Z\s]+$", name):
            return False, "Invalid cardholder name"

        # Validate card number
        if not re.match(r"^\d{13,19}$", card_number):
            return False, "Invalid card number format"
        if not PaymentInfoFrame.luhn_check(card_number):
            return False, "Invalid card number"

        # Validate CVV
        if not re.match(r"^\d{3,4}$", cvv):
            return False, "Invalid CVV format"

        # Validate expiration date
        if not re.match(r"^(0[1-9]|1[0-2])/\d{2}$", exp_date):
            return False, "Invalid expiration date format"
        exp_month, exp_year = exp_date.split("/")
        exp_year = "20" + exp_year
        exp_month = int(exp_month)
        exp_year = int(exp_year)
        now = datetime.now()
        if exp_year < now.year or (exp_year == now.year and exp_month < now.month):
            return False, "Card is expired"

        return True, "Card information is valid"

    def __init__(self, master, type, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.active_msg = None
        self.type = type
        self.controller = controller
        self.create_widgets()

    def in_focus_entry(self, widget, message):
        if len(widget.get()) != 0 and widget.get() != message:
            return
        widget.delete(0, "end")

    def out_focus_entry(self, widget, message):
        if len(widget.get()) != 0:
            return
        widget.insert(0, message)

    def create_widgets(self):
        # TODO: change this text
        AddDetailsFrame = ttk.Frame(master=self)
        details_label = ttk.Label(
            master=AddDetailsFrame,
            text="Add payment details",
            font="Montserrat 15 bold",
            foreground="#ADADAD",
        )
        details_label.pack(side="left")
        AddDetailsFrame.pack(pady=(0,20))
        payment_label = ttk.Label(
            master=self, text="Payment method", font="Montserrat 9 bold"
        )
        payment_label.pack(pady=10)
        ChooseOptionFrame = ttk.Frame(master=self)
        style = ttk.Style()
        style.configure('Payment.TButton', background='#8C2F39', foreground = 'white', font=('Montserrat', 8),relief='ridge', borderwidth =2 )
        style.map('TButton', background=[('active', '#eb6864')], foreground=[('active', 'black')])
        creditcard_button = ttk.Button(
            master=ChooseOptionFrame, text="Credit Card", style="Payment.TButton"
        )
        style.configure('Payment2.TButton', background='white', foreground = 'black', font=('Montserrat', 8), relief='ridge', borderwidth =2 )
        style.map('TButton', background=[('active', '#eb6864')], foreground=[('active', 'black')])
        banktransfer_button = ttk.Button(
            master=ChooseOptionFrame, text="Bank Transfer", style="Payment2.TButton"
        )
        creditcard_button.pack(side="left", padx=5)
        banktransfer_button.pack(side="left", padx=5)
        ChooseOptionFrame.pack(pady=10)
        paymentdetails_label = ttk.Label(
            master=self, text="Payment details", font="Montserrat 9 bold"
        )
        paymentdetails_label.pack(pady=15)
        cardholder_entry = ttk.Entry(
            master=self, width=50, foreground="#ADADAD", font="Montserrat 7"
        )
        cardholder_entry.insert(0, PaymentInfoFrame.cardholder_str)
        cardholder_entry.bind(
            "<FocusIn>",
            lambda e: self.in_focus_entry(e.widget, PaymentInfoFrame.cardholder_str),
        )
        cardholder_entry.bind(
            "<FocusOut>",
            lambda e: self.out_focus_entry(e.widget, PaymentInfoFrame.cardholder_str),
        )
        cardholder_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cardholder_entry.pack(pady=10)
        cardnumber_entry = ttk.Entry(
            master=self, width=50, foreground="#ADADAD", font="Montserrat 7"
        )
        cardnumber_entry.insert(0, PaymentInfoFrame.card_num_str)
        cardnumber_entry.bind(
            "<FocusIn>",
            lambda e: self.in_focus_entry(e.widget, PaymentInfoFrame.card_num_str),
        )
        cardnumber_entry.bind(
            "<FocusOut>",
            lambda e: self.out_focus_entry(e.widget, PaymentInfoFrame.card_num_str),
        )
        cardnumber_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cardnumber_entry.pack(pady=(0, 10))

        CVVEXPrame = ttk.Frame(master=self)

        cvv_entry = ttk.Entry(
            master=CVVEXPrame,
            width=15,
            foreground="#ADADAD",
            font="Montserrat 7",
        )
        cvv_entry.insert(0, PaymentInfoFrame.cvv_str)
        cvv_entry.bind(
            "<FocusIn>",
            lambda e: self.in_focus_entry(e.widget, PaymentInfoFrame.cvv_str),
        )
        cvv_entry.bind(
            "<FocusOut>",
            lambda e: self.out_focus_entry(e.widget, PaymentInfoFrame.cvv_str),
        )
        cvv_entry.bind("<Return>", lambda e: print(e.widget.get()))
        cvv_entry.pack(side="left", padx=(0, 30))
        exp_label = ttk.Label(
            master=CVVEXPrame,
            text="Exp.date:",
            font="Montserrat 9",
            foreground="#ADADAD",
        )
        exp_label.pack(side="left")
        MMYY_entry = ttk.Entry(
            master=CVVEXPrame, width=18, foreground="#ADADAD", font="Montserrat 7"
        )
        MMYY_entry.insert(0, PaymentInfoFrame.exp_str)
        MMYY_entry.bind(
            "<FocusIn>",
            lambda e: self.in_focus_entry(e.widget, PaymentInfoFrame.exp_str),
        )
        MMYY_entry.bind(
            "<FocusOut>",
            lambda e: self.out_focus_entry(e.widget, PaymentInfoFrame.exp_str),
        )
        MMYY_entry.bind("<Return>", lambda e: print(e.widget.get()))
        MMYY_entry.pack(side="left")
        CVVEXPrame.pack()
        self.terms_var = ttk.IntVar()
        self.terms = ttk.Checkbutton(
            master=self,
            text="I have read and accept the Terms & Conditions",
            variable=self.terms_var,
            onvalue=1,
            offvalue=0,
        )
        self.terms.pack(pady=20)
        style.configure('Payment3.TButton', background='#8C2F39', foreground = 'white',font=('Montserrat', 8))
        self.price_button = ttk.Button(
            master=self,
            text="Confirm payment",
            style="Payment3.TButton",
            command=lambda: self.submit_payment(
                cardholder_entry.get(),
                cardnumber_entry.get(),
                cvv_entry.get(),
                MMYY_entry.get(),
            ),
        )
        self.price_button.pack(pady=(0, 50))

    def submit_payment(self, holder, num, cvv, exp):
        is_valid, msg = PaymentInfoFrame.validate_card_info(holder, num, cvv, exp)
        if not is_valid:
            self.show_error_msg(self, self.price_button, msg)
            return

        if self.terms_var.get() != 1:
            self.show_error_msg(
                self, self.price_button, "Terms must be accepted to proceed."
            )
            return

        total = self.controller.get_current_total()
        print(total)
        gateway = PaymentGatewayInterface()
        valid_process, payment_id = gateway.process_payment(
            holder, num, cvv, exp, total
        )
        if not valid_process:
            self.show_error_msg(self, self.price_button, "Payment processing failed.")
            return

        # succesful payment
        if self.type == "course":
            new_payment = CoursePayment(
                payment_id,
                total,
                0,
                self.controller.course.cons.get_id(),
                self.controller.course,
                self.controller.get_add_ons(),
            )
            course_payments.append(new_payment)
        elif self.type == "consultant":
            pass
        else:
            self.show_error_msg(self, self.price_button, "Invalid payment type.")
            return

        self.show_success_msg(self, self.price_button, "Successfully purchased course.")

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()

    def show_error_msg(self, master, btn, msg):
        self.hide_msg()
        self.active_msg = ttk.Label(
            master=master, text=msg, font="Montserrat 12 bold", foreground="#FF0000"
        )
        self.active_msg.pack(before=btn)

    def show_success_msg(self, master, btn, msg):
        self.hide_msg()
        self.active_msg = ttk.Label(
            master=master, text=msg, font="Montserrat 12 bold", foreground="#00FF00"
        )
        self.active_msg.pack(before=btn)

    def hide_msg(self):
        if self.active_msg:
            self.active_msg.pack_forget()
