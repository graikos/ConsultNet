import tkinter as tk
import ttkbootstrap as ttk
from domain import Category, Consultant, Image, Media, Course
from course_item import CourseItem



#window
window = ttk.Window()
window.title('app')
window.geometry('1000x800')


#first row of labels
logo_frame = ttk.Frame(master = window)
# add textlabel
# make text semi bold
label1 = ttk.Label(master=logo_frame, text='Consult', font= 'Montserrat 24 bold', foreground="#080708")
label2 = ttk.Label(master=logo_frame, text='Net', font= 'Montserrat 24 bold', foreground="#8C2F39")
label1.pack(side = 'left')
label2.pack(side = 'left')

profile_label = ttk.Label(master=logo_frame, text='Profile', font= 'Montserrat 12', foreground="#ADADAD")
profile_label.bind("<Button-1>", lambda e: print("Profile clicked"))
profile_label.pack(side = 'right')
logo_frame.pack(fill = 'both')

t_label = ttk.Label(master=window, text='Revenue & Statistics', font= 'Montserrat 16 bold')
t_label.pack()

#second row of labels
options_frame = ttk.Frame(master = window)
# add textlabel
courses_label = ttk.Label(master=options_frame, text='My Courses', font= 'Montserrat 12',foreground="#ADADAD")
services_label = ttk.Label(master=options_frame, text='Services', font= 'Montserrat 12',foreground="#ADADAD")
courses_label.pack(side = 'left',padx=20)
services_label.pack(side = 'left',padx=20)

options_frame.pack()

timing_frame = ttk.Frame(master=window)
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
cb1 = ttk.Combobox(master=timing_frame, state="readonly" , values = months, width=45)
cb1.pack(side='left')


years = [
    2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
    2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033
]
cb2= ttk.Combobox(master=timing_frame, state="readonly" , values = years, width=45)
cb2.pack(side='left')
timing_frame.pack()

columns = ("Date","Client", "Category", "Request Name" , "Hours", "Revenue")

# Create a treeview with columns
my_tree = ttk.Treeview(window, bootstyle = "danger", columns=columns, show="headings")

# Define column headings
my_tree.heading("Date", text="Date")
my_tree.heading("Client", text="Client")
my_tree.heading("Category", text="Category")
my_tree.heading("Request Name", text="Request name")
my_tree.heading("Hours", text="Hours")
my_tree.heading("Revenue", text="Revenue")

# Add data to the table (sample data)
data = [
    ("2024-05-01", "Client A", "Category 1", "Request A", 5, 100),
    ("2024-05-02", "Client B", "Category 2", "Request B", 8, 200),
    ("2024-05-03", "Client C", "Category 1", "Request C", 6, 150),
]

for row in data:
    my_tree.insert("", "end", values=row)



# Pack the treeview to the window
my_tree.pack(pady=15)


#run
window.mainloop()