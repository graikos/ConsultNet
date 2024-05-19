import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from datetime import datetime, timedelta
from YearChangerApp import YearChangerApp

class ScheduleAppointment(ttk.Frame):

    def __init__(self, master, consultant, **kwargs):
        super().__init__(master, **kwargs)
        self.consultant = consultant
        self.create_widgets()

    def create_widgets(self):
        # Create title frame
        title_frame = ttk.Frame(self)
        title_frame.pack()

        # Title labels
        intro_label1 = ttk.Label(title_frame, text='Scheduling an appointment with: ', font='Montserrat 16 bold')
        intro_label2 = ttk.Label(title_frame, text=str(self.consultant.name), font='Montserrat 16 bold', foreground='#8C2F39')
        intro_label1.pack(side='left',pady=15)
        intro_label2.pack(side='left')

        # Introduction label
        intro_label3 = ttk.Label(self, text='Select appointment hours: ', font='Montserrat 16 bold', foreground="#ADADAD")
        intro_label3.pack()

        # Year frame
        year_frame = ttk.Frame(self)
        YearChangerApp(year_frame)
        year_frame.pack()

        # Create schedule frame
        schedule_frame = ttk.Frame(self)
        schedule_frame.pack(padx=10, pady=10)

        # Define days of the week
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Get the current date
        current_date = datetime.now()

        # Create a custom style for rounded borders
        style = ttk.Style()
        style.configure("Schedule.TLabel", borderwidth=1, relief="solid", padding=7, background="#FFFFFF", foreground="#000000", font=("Montserrat", 7),anchor='center')
        
        # Add labels for days of the week with dates
        for i, day in enumerate(days_of_week):
            day_date = current_date + timedelta(days=i)
            # Split the day label into day name and date
            day_name_label = ttk.Label(schedule_frame, text=day, font=("Montserrat", 12, "bold"), anchor="center")
            day_name_label.grid(row=0, column=i+1, padx=(10, 2), pady=5, ipadx=10, ipady=5, sticky="ew")
            day_date_label = ttk.Label(schedule_frame, text=day_date.strftime('%m/%d'), font=("Montserrat", 10), anchor="center")
            day_date_label.grid(row=1, column=i+1, padx=(10, 2), pady=(0, 5), ipadx=10, ipady=5, sticky="ew")

        # Add labels for each hour from 9 AM to 9 PM
        for hour in range(9, 21):  # From 9 to 21 (9 AM to 9 PM)
            for day in range(7):
                hour_text = f"{hour}:00 - {hour+1}:00"
                label = ttk.Label(schedule_frame, text=hour_text, font=("Montserrat", 10), anchor="center", style="Schedule.TLabel")
                label.grid(row=hour+2, column=day+1, padx=15, pady=2, ipadx=25)

        tot_label =  ttk.Label(self, text='Total: $' + ' ($'+str(self.consultant.rate)+'/h)', font=("Montserrat", 12, "bold"), anchor="center") 
        tot_label.pack()      

        self.pack(pady=20)