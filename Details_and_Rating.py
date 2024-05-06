import tkinter as tk
import ttkbootstrap as ttk
from domain import Category, Consultant, Image, Media, Course
from course_info import CourseInfo



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

testCategory = Category("Test Category")
testImage = Image(10, 10, "VLSI.png")
testConsultant = Consultant("Pol",testImage,testCategory,"Harvard","VERY BIG",8.5,"Monday","Visa Card")
testMedia = Media(3) 
testCourse = Course('Test Course', ["testCategory"], testImage, "testMedia",testConsultant, 2.3,32,342,"Description Here","24/03/2001","29/03/2001",["Test Add-On"])
TestCourseObject = CourseInfo(window, testCourse)

#run
window.mainloop()