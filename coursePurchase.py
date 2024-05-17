import ttkbootstrap as ttk
import tkinter as tk
from course_purchase import CoursePurchasePage
from payment_details import PaymentInfoFrame
from domain.course import courses_dict
from domain.consultant import consultants_dict

# Create main window
window = ttk.Window()
window.title('app')
window.geometry('1000x800')

TestCourseObject = CoursePurchasePage(window,course=courses_dict["course1"])
TestCourseObject.show()



# Run the application
window.mainloop()
