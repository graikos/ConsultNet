import tkinter as tk
import ttkbootstrap as ttk
from domain import Category, Consultant, Image, Media, Course
from course_item import CourseItem

def on_label_clicked(event):
    if course_label.cget("bg") == "white":
        course_label.config(bg="#8C2F39", fg="white")  # Change to red background with white text
    else:
        course_label.config(bg="white", fg="black")  # Change to white background with black text

def on_label_clicked2(event):
    if consultant_label.cget("bg") == "white":
        consultant_label.config(bg="#8C2F39", fg="white")  # Change to red background with white text
    else:
        consultant_label.config(bg="white", fg="black")  # Change to white background with black text

#window
window = ttk.Window(themename='journal')
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
profile_label.pack(side = 'right',padx=75)


logo_frame.pack(fill = 'both')

#second row of labels
options_frame = ttk.Frame(master = window)
# add textlabel
courses_label = ttk.Label(master=options_frame, text='Courses', font= 'Montserrat 12',foreground="#ADADAD")
consultants_label = ttk.Label(master=options_frame, text='Consultants', font= 'Montserrat 12',foreground="#ADADAD")
requests_label = ttk.Label(master=options_frame, text='Requests', font= 'Montserrat 12 bold underline')
courses_label.pack(side = 'left', padx = 20)
consultants_label.pack(side = 'left',padx= 20)
requests_label.pack(side = 'left',padx=20)

options_frame.pack(fill='both', pady=20)

# Load the back arrow image
back_arrow_image = tk.PhotoImage(file="back_arrow.png")

# Create a button with the arrow image
back_button = ttk.Button(window, image=back_arrow_image)
back_button.place(x=50, y=150)

# Get the window background color
window_bg_color = window.cget('bg')

# Define a custom style for the button
s = ttk.Style()
s.theme_use('journal')  # Use the default theme
s.configure('Back.TButton', background=window_bg_color, relief='flat')

# Configure button style for hover state
s.map('Back.TButton',
      background=[('active', window_bg_color),
                  ('disabled', window_bg_color),
                  ('pressed', window_bg_color)])

back_button.config(style='Back.TButton')

intro_label = ttk.Label(master=window, text='Submitting a request', font= 'Montserrat 15 bold')
intro_label.pack(pady=(40,80))

TFrame = ttk.Frame(master=window)
t_label = ttk.Label(master=TFrame, text='Request Title:', font= 'Montserrat 9 bold')
t_label.pack(anchor='w',side='left',padx=(0,10))
t_entry = ttk.Entry(master =TFrame, width = 30)
t_entry.insert(0, '')
t_entry.bind("<FocusIn>", lambda e: t_entry.delete(0, 'end'))
t_entry.bind("<Return>", lambda e: print(e.widget.get()))
t_entry.pack(side='left')
TFrame.pack(pady=(0,14),padx=(0,70))

TyFrame = ttk.Frame(master=window)
ty_label = ttk.Label(master=TyFrame, text='Request Type:', font= 'Montserrat 9 bold')
ty_label.pack(anchor='w',side='left',padx=(0,10))
course_label = tk.Label(TyFrame, text="Course", relief="groove", padx=10, pady=5, borderwidth=2, bg="#8C2F39", fg="white")
course_label.pack(side='left',padx=(0,8))
consultant_label = tk.Label(TyFrame, text="Consultant", relief="groove", padx=10, pady=5, borderwidth=2, bg="white", fg="black")
consultant_label.pack(side='left')
TyFrame.pack(pady=(0,14),padx=(0,114))

RFrame = ttk.Frame(master=window)
r_label = ttk.Label(master=RFrame, text='Request Description:', font= 'Montserrat 9 bold')
r_label.pack(anchor='nw',side='left',padx=(0,10))
r_textbox = tk.Text(master=RFrame,width=30,height=6)
r_textbox.pack(side='left')
RFrame.pack(pady=(0,14),padx=(0,116))

CatFrame = ttk.Frame(master=window)
cat_label = ttk.Label(master=CatFrame, text='Category:', font= 'Montserrat 9 bold')
cat_label.pack(anchor='w',side='left',padx=(0,10))
categories = ["Technology", "Food", "Travel", "Music", "Sports"]
cb = ttk.Combobox(master=CatFrame, state="readonly" , values = categories, width=28)
cb.pack(side='left')
CatFrame.pack(pady=(0,14),padx=(0,44))

CompFrame = ttk.Frame(master=window)
cmp_label = ttk.Label(master=CompFrame, text='Compensation ($):', font= 'Montserrat 9 bold')
cmp_label.pack(anchor='w',side='left',padx=(0,10))
cmp_entry = ttk.Entry(master = CompFrame, width = 8)
cmp_entry.insert(0, '')
cmp_entry.bind("<FocusIn>", lambda e: cmp_entry.delete(0, 'end'))
cmp_entry.bind("<Return>", lambda e: print(e.widget.get()))
cmp_entry.pack(side='left')
CompFrame.pack(pady=(0,40),padx=(0,232))

style = ttk.Style()
style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
p_button = ttk.Button(master=window, text= "Submit Request" , style='Custom.TButton')
p_button.pack(pady=(0,14))

# Bind left mouse button click event to the label
course_label.bind("<Button-1>", on_label_clicked)
consultant_label.bind("<Button-1>", on_label_clicked2)

#run
window.mainloop()