import ttkbootstrap as ttk
import tkinter as tk
from schedule_appointment import ScheduleAppointment
from payment_details import PaymentInfo
from domain.consultant import consultants_dict

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
canvas.create_window((1000, 0), window=frame,anchor='n')

# Update the scroll region when the frame size changes
frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))


# First row of labels
logo_frame = ttk.Frame(master=frame)
label1 = ttk.Label(master=logo_frame, text='Consult', font='Montserrat 24 bold', foreground="#080708")
label2 = ttk.Label(master=logo_frame, text='Net', font='Montserrat 24 bold', foreground="#8C2F39")
label1.pack(side='left')
label2.pack(side='left')

profile_label = ttk.Label(master=frame, text='Profile', font='Montserrat 12', foreground="#ADADAD")
profile_label.bind("<Button-1>", lambda e: print("Profile clicked"))
profile_label.pack(side='right',anchor='ne',padx=75,pady=20)
logo_frame.pack(fill='both')

# Second row of labels
options_frame = ttk.Frame(master=frame)
courses_label = ttk.Label(master=options_frame, text='Courses', font='Montserrat 12 ', foreground="#ADADAD")
consultants_label = ttk.Label(master=options_frame, text='Consultants', font='Montserrat 12 underline bold')
requests_label = ttk.Label(master=options_frame, text='Requests', font='Montserrat 12', foreground="#ADADAD")
courses_label.pack(side='left', padx=20)
consultants_label.pack(side='left', padx=20)
requests_label.pack(side='left', padx=20)
options_frame.pack(fill='both', pady=20)

# Load the back arrow image
back_arrow_image = tk.PhotoImage(file="back_arrow.png")

# Create a button with the arrow image
back_button = ttk.Button(frame, image=back_arrow_image)
back_button.pack(side='left', anchor='nw', padx= 20 ,pady=30)
back_button.lift()
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



TestConsultantObject = ScheduleAppointment(frame,consultants_dict["Alice"])
TestPayment = PaymentInfo(frame)


#run
window.mainloop()