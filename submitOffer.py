import ttkbootstrap as ttk
import tkinter as tk
from submit_offer import SubmitOfferPage
from domain.request import request_dict

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
profile_label.pack(side = 'right', padx=75)


logo_frame.pack(fill = 'both')

#second row of labels
options_frame = ttk.Frame(master = window)
# add textlabel
courses_label = ttk.Label(master=options_frame, text='Courses', font= 'Montserrat 12',foreground="#ADADAD")
consultants_label = ttk.Label(master=options_frame, text='Consultants', font= 'Montserrat 12',foreground="#ADADAD")
requests_label = ttk.Label(master=options_frame, text='Requests', font= 'Montserrat 12 bold underline ')
courses_label.pack(side = 'left', padx = 20)
consultants_label.pack(side = 'left',padx= 20)
requests_label.pack(side = 'left',padx=20)

options_frame.pack(fill='both', pady=20)

# Load the back arrow image
back_arrow_image = tk.PhotoImage(file="./resources/back_arrow.png")

# Create a button with the arrow image
back_button = ttk.Button(window, image=back_arrow_image)
back_button.place(x=50, y=140)

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

TestOfferObject = SubmitOfferPage(window,request_dict["request1"])


#RUN BABY RUN
window.mainloop()
