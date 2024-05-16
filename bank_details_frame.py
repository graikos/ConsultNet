import ttkbootstrap as ttk
import tkinter as tk


class BankDetailsFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.invalid_IBAN = True

        self.create_widgets()

    def get_details(self):
        return (self.acc_entry.get(), self.iban_entry.get())


    def create_widgets(self):
        bank_label = ttk.Label(
            master=self, text="Bank Account Details:", font="Montserrat 12 bold"
        )
        bank_label.pack(pady=(0, 20))

        AccFrame = ttk.Frame(master=self)
        acc_label = ttk.Label(
            master=AccFrame, text="Account Holder: ", font="Montserrat 9 bold"
        )
        acc_label.pack(side="left")
        self.acc_entry = ttk.Entry(master=AccFrame, width=30)
        self.acc_entry.insert(0, "")
        self.acc_entry.bind("<FocusIn>", lambda e: self.acc_entry.delete(0, "end"))
        self.acc_entry.bind("<Return>", lambda e: print(e.widget.get()))
        self.acc_entry.pack(side="left")
        AccFrame.pack(anchor="w", pady=(0, 10))

        IbanFrame = ttk.Frame(master=self)
        iban_label = ttk.Label(
            master=IbanFrame, text="IBAN: ", font="Montserrat 9 bold"
        )
        iban_label.pack(anchor="w")
        self.iban_entry = ttk.Entry(master=IbanFrame, width=30)
        self.iban_entry.insert(0, "")
        self.iban_entry.bind("<FocusIn>", lambda e: self.iban_entry.delete(0, "end"))
        self.iban_entry.bind("<Return>", lambda e: print(e.widget.get()))
        self.iban_entry.pack(side="left")
        IbanFrame.pack(pady=(0, 10), padx=20)


    def validate_iban(self):

        iban = self.iban_entry.get()

        # Remove spaces and convert to uppercase
        iban = iban.replace(' ', '').upper()
        
        # Check the length of the IBAN
        if len(iban) < 15 or len(iban) > 34:
            return False
        
        # Move the first four characters to the end of the string
        iban_rearranged = iban[4:] + iban[:4]
        
        # Replace each letter in the string with two digits
        iban_numeric = ''
        for char in iban_rearranged:
            if char.isdigit():
                iban_numeric += char
            else:
                iban_numeric += str(ord(char) - 55)
        
        # Convert the string to an integer
        iban_int = int(iban_numeric)
        
        # Compute the remainder of the number divided by 97
        return iban_int % 97 == 1

    def show(self):
        self.pack()
    
    def hide(self):
        self.pack_forget()
