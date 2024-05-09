import tkinter as tk
import ttkbootstrap as ttk
from domain import Category, Consultant, Image, Media, Course
from course_item import CourseItem



#window
window = ttk.Window(themename='journal')
window.title('app')
window.geometry('1920x1200')

# Create a Canvas widget
canvas = tk.Canvas(window)
canvas.pack(side="left",fill="both", expand=True)

# Add a Scrollbar widget
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to contain your widgets
frame = ttk.Frame(canvas)
canvas.create_window((960, 0), window=frame,anchor='n')

# Update the scroll region when the frame size changes
frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))


#first row of labels
logo_frame = ttk.Frame(master = frame)
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

#CreateProfile Frame
CreateProfileFrame = ttk.Frame(master=frame)
intro_label = ttk.Label(master=CreateProfileFrame, text='Create your Profile', font= 'Montserrat 16 bold')
intro_label.pack(pady=30)

FirstNameFrame = ttk.Frame(master=CreateProfileFrame)
first_name_label = ttk.Label(master=FirstNameFrame, text='First name:', font= 'Montserrat 9 bold')
first_name_label.pack(side='left',padx=(0,8))
first_name_entry = ttk.Entry(master = FirstNameFrame, width = 30)
first_name_entry.insert(0, '')
first_name_entry.bind("<FocusIn>", lambda e: first_name_entry.delete(0, 'end'))
first_name_entry.bind("<Return>", lambda e: print(e.widget.get()))
first_name_entry.pack(side='left')
FirstNameFrame.pack(anchor="w",pady=5,padx=53)

LastNameFrame = ttk.Frame(master=CreateProfileFrame)
last_name_label = ttk.Label(master=LastNameFrame, text='Last name:', font= 'Montserrat 9 bold')
last_name_label.pack(side='left',padx=(0,8))
last_name_entry = ttk.Entry(master = LastNameFrame, width = 30)
last_name_entry.insert(0, '')
last_name_entry.bind("<FocusIn>", lambda e: last_name_entry.delete(0, 'end'))
last_name_entry.bind("<Return>", lambda e: print(e.widget.get()))
last_name_entry.pack(side='left')
LastNameFrame.pack(anchor="w",pady=5,padx=55)

PicFrame = ttk.Frame(master=CreateProfileFrame)
pic_label = ttk.Label(master=PicFrame, text='Profile Picture:', font= 'Montserrat 9 bold')
pic_label.pack(side='left',padx=(0,8))
last_name_entry = ttk.Entry(master = PicFrame, width = 30)
last_name_entry.insert(0, '')
last_name_entry.bind("<FocusIn>", lambda e: last_name_entry.delete(0, 'end'))
last_name_entry.bind("<Return>", lambda e: print(e.widget.get()))
last_name_entry.pack(side='left')
PicFrame.pack(anchor="w",pady=5,padx=27)

CatFrame = ttk.Frame(master=CreateProfileFrame)
cat_label = ttk.Label(master=CatFrame, text='Field of Expertise:', font= 'Montserrat 9 bold')
cat_label.pack(side='left',padx=(0,8))
categories = ["Technology", "Food", "Travel", "Music", "Sports"]
cb = ttk.Combobox(master=CatFrame, state="readonly" , values = categories, width=28)
cb.pack(side='left')
CatFrame.pack(anchor="w",pady=5,padx=10)

EduFrame = ttk.Frame(master=CreateProfileFrame)
edu_label = ttk.Label(master=EduFrame, text='Education:', font= 'Montserrat 9 bold')
edu_label.pack(side='left',padx=(0,8))
edu_entry = ttk.Entry(master = EduFrame, width = 30)
edu_entry.insert(0, '')
edu_entry.bind("<FocusIn>", lambda e: edu_entry.delete(0, 'end'))
edu_entry.bind("<Return>", lambda e: print(e.widget.get()))
edu_entry.pack(side='left')
EduFrame.pack(anchor="w",pady=5,padx=56)

ExpFrame = ttk.Frame(master=CreateProfileFrame)
exp_label = ttk.Label(master=ExpFrame, text='Experience:', font= 'Montserrat 9 bold')
exp_label.pack(side='left',padx=(0,8))
exp_entry = ttk.Entry(master = ExpFrame, width = 30)
exp_entry.insert(0, '')
exp_entry.bind("<FocusIn>", lambda e: exp_entry.delete(0, 'end'))
exp_entry.bind("<Return>", lambda e: print(e.widget.get()))
exp_entry.pack(side='left')
ExpFrame.pack(anchor="w",pady=5,padx=48)

RFrame = ttk.Frame(master=CreateProfileFrame)
r_label = ttk.Label(master=RFrame, text='Hourly rate ($):', font= 'Montserrat 9 bold')
r_label.pack(side='left',padx=(0,8))
r_entry = ttk.Entry(master = RFrame, width = 30)
r_entry.insert(0, '')
r_entry.bind("<FocusIn>", lambda e: r_entry.delete(0, 'end'))
r_entry.bind("<Return>", lambda e: print(e.widget.get()))
r_entry.pack(side='left')
RFrame.pack(anchor="w",pady=5,padx=30)

CreateProfileFrame.pack()

#Available Hours Frame

AvailableHFrame = ttk.Frame(master=frame)

intro2_label = ttk.Label(master=AvailableHFrame, text='Available Hours', font= 'Montserrat 16 bold')
intro2_label.pack(pady=(40,10))

# Create a frame for the schedule selection
schedule_frame = ttk.Frame(AvailableHFrame)
schedule_frame.pack(pady=10)

# Create a custom style for rounded borders
style = ttk.Style()
style.configure("Custom.TLabel", borderwidth=1, relief="solid", padding=7, background="#FFFFFF", foreground="#000000", font=("Montserrat", 7),anchor='center')

# Add labels for each hour and day
for hour in range(24):
    for day in range(7):
        hour_text = f"{hour}:00 - {hour+1}:00"
        label = ttk.Label(schedule_frame, text=hour_text, style="Custom.TLabel")
        label.grid(row=hour+1, column=day+1, padx=15, pady=2,ipadx=25)

# Add labels for days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day, day_name in enumerate(days_of_week):
    day_label = ttk.Label(schedule_frame, text=day_name, font=("Montserrat", 7))
    day_label.grid(row=0, column=day+1, padx=15, pady=2)

# Add a label for "Batch Select"
batch_select_label = ttk.Label(schedule_frame, text="Batch Select", font=("Montserrat", 7))
batch_select_label.grid(row=0, column=0, padx=2, pady=2)

# Add checkboxes for batch selection
batch_vars = []
for hour in range(24):
    batch_var = ttk.BooleanVar()
    batch_checkbox = ttk.Checkbutton(schedule_frame, variable=batch_var)
    batch_checkbox.grid(row=hour+1, column=0, padx=2, pady=2)
    batch_vars.append(batch_var)
AvailableHFrame.pack()

#Rest Frame

RestFrame = ttk.Frame(master=frame)

exc_label = ttk.Label(master=RestFrame, text='Exceptions', font= 'Montserrat 12 bold')
exc_label.pack(pady=(40,20))

ExcFrame = ttk.Frame(master=RestFrame)
f_entry = ttk.Entry(master = ExcFrame, width = 13)
f_entry.insert(0, 'YYYY/MM/DD')
f_entry.bind("<FocusIn>", lambda e: f_entry.delete(0, 'end'))
f_entry.bind("<Return>", lambda e: print(e.widget.get()))
f_entry.pack(side='left',padx=4)

s_entry = ttk.Entry(master = ExcFrame, width = 3)
s_entry.insert(0, 'HH')
s_entry.bind("<FocusIn>", lambda e: s_entry.delete(0, 'end'))
s_entry.bind("<Return>", lambda e: print(e.widget.get()))
s_entry.pack(side='left',padx=4)

t_entry = ttk.Entry(master = ExcFrame, width = 3)
t_entry.insert(0, 'HH')
t_entry.bind("<FocusIn>", lambda e: t_entry.delete(0, 'end'))
t_entry.bind("<Return>", lambda e: print(e.widget.get()))
t_entry.pack(side='left',padx=4)

ExcFrame.pack(pady=(0,40))

bank_label = ttk.Label(master=RestFrame, text='Bank Account Details:', font= 'Montserrat 12 bold')
bank_label.pack(pady=(0,20))

AccFrame = ttk.Frame(master=RestFrame)
acc_label = ttk.Label(master=AccFrame, text='Account: ', font= 'Montserrat 9 bold')
acc_label.pack(side='left')
acc_entry = ttk.Entry(master = AccFrame, width = 30)
acc_entry.insert(0, '')
acc_entry.bind("<FocusIn>", lambda e: acc_entry.delete(0, 'end'))
acc_entry.bind("<Return>", lambda e: print(e.widget.get()))
acc_entry.pack(side='left')
AccFrame.pack(anchor='w',pady=(0,10))

IbanFrame = ttk.Frame(master=RestFrame)
iban_label = ttk.Label(master=IbanFrame, text='IBAN: ', font= 'Montserrat 9 bold')
iban_label.pack(side='left')
iban_entry = ttk.Entry(master = IbanFrame, width = 30)
iban_entry.insert(0, '')
iban_entry.bind("<FocusIn>", lambda e: iban_entry.delete(0, 'end'))
iban_entry.bind("<Return>", lambda e: print(e.widget.get()))
iban_entry.pack(side='left')
IbanFrame.pack(pady=(0,10),padx=20)

terms = ttk.Checkbutton(master = RestFrame, text = 'I have read and accept the Terms & Conditions')
terms.pack(pady=(20,30))
style.configure('Custom3.TButton', background='#8C2F39', foreground = 'white')
p_button = ttk.Button(master=RestFrame, text= "Create Profile" , width=25 ,style='Custom3.TButton')
p_button.pack(pady=(0,60))

RestFrame.pack()

#run
window.mainloop()