import tkinter as tk
import ttkbootstrap as ttk
from domain import Category, Consultant, Image, Media, Course
from course_info import CourseInfo
from domain.course import courses_dict



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

TestCourseObject = CourseInfo(window,courses_dict["course1"])

# Load the back arrow image
back_arrow_image = tk.PhotoImage(file="back_arrow.png")

# Create a button with the arrow image
back_button = ttk.Button(window, image=back_arrow_image)
back_button.place(x=50, y=105)

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

#run
window.mainloop()