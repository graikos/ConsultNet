import tkinter as tk
from tkinter import ttk

class YearChangerApp:
    def __init__(self, root):
        self.root = root

        # Initial year and month
        self.year = 2024
        self.month_index = 0
        self.months = ["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December"]

        # Style configuration
        style = ttk.Style()
        style.configure("TButton", foreground='black', background='white', relief='flat', borderwidth=0)
        style.map('TButton', background=[('active', 'white')], foreground=[('active', 'black')])
        style.configure("YearButton.TButton", font=("Montserrat", 8))
        style.configure("MonthButton.TButton", font=("Montserrat", 12))

        # Create year frame and widgets
        self.year_frame = ttk.Frame(self.root)
        self.left_year_button = ttk.Button(self.year_frame, text="◀", command=self.decrease_year, style="YearButton.TButton")
        self.right_year_button = ttk.Button(self.year_frame, text="▶", command=self.increase_year, style="YearButton.TButton")
        self.year_label = ttk.Label(self.year_frame, text=self.year, font=("Montserrat", 12))

        # Place year widgets
        self.left_year_button.grid(row=0, column=0, padx=4)
        self.year_label.grid(row=0, column=1, padx=4)
        self.right_year_button.grid(row=0, column=2, padx=4)

        # Create month frame and widgets
        self.month_frame = ttk.Frame(self.root)
        self.left_month_button = ttk.Button(self.month_frame, text="◀", command=self.decrease_month, style="MonthButton.TButton")
        self.right_month_button = ttk.Button(self.month_frame, text="▶", command=self.increase_month, style="MonthButton.TButton")
        self.month_label = ttk.Label(self.month_frame, text=self.months[self.month_index], font=("Montserrat", 16))

        # Place month widgets
        self.left_month_button.grid(row=0, column=0, padx=10)
        self.month_label.grid(row=0, column=1, padx=10)
        self.right_month_button.grid(row=0, column=2, padx=10)

        # Place frames
        self.year_frame.pack(pady=10)
        self.month_frame.pack(pady=10)

    def decrease_year(self):
        self.year -= 1
        self.year_label.config(text=self.year)

    def increase_year(self):
        self.year += 1
        self.year_label.config(text=self.year)

    def decrease_month(self):
        self.month_index = (self.month_index - 1) % 12
        self.month_label.config(text=self.months[self.month_index])

    def increase_month(self):
        self.month_index = (self.month_index + 1) % 12
        self.month_label.config(text=self.months[self.month_index])