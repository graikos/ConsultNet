import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class CourseInfo(ttk.Frame):

    def __init__(self, master, course, **kwargs):
        super().__init__(master, **kwargs)
        self.course = course
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        CourseInfoFrame =  ttk.Frame(master = self.master)
        intro_label = ttk.Label(master=CourseInfoFrame, text='Showing details for course: '+ str(self.course.name), font= 'Montserrat 16 bold')
        intro_label.pack()
        right_frame = ttk.Frame(master = CourseInfoFrame)
        left_frame = ttk.Frame(master = CourseInfoFrame)
        
        # left frame
        title_label = ttk.Label(master=left_frame, text='Course Details', font= 'Montserrat 15 bold')
        title_label.pack()
        description_label = ttk.Label(master=left_frame, text='Description : '+ self.course.description, font= 'Montserrat 7 bold')
        description_label.pack()
        sales_label = ttk.Label(master=left_frame, text='Purchased by: '+ str(self.course.num_of_sales), font= 'Montserrat 7',foreground="#ADADAD")
        sales_label.pack()
        posted_on_label = ttk.Label(master=left_frame, text='Posted on: ' + self.course.posted_on, font= 'Montserrat 7',foreground="#ADADAD")
        posted_on_label.pack()
        final_exam_label = ttk.Label(master=left_frame, text='Final Exam: ' + self.course.final_exam, font= 'Montserrat 7',foreground="#ADADAD")
        final_exam_label.pack()
        for cat in self.course.categories:
            category_label = ttk.Label(master=left_frame, text= cat, font= 'Montserrat 9 bold',foreground='white', background='black')
            category_label.pack()
        media_label = ttk.Label(master=left_frame, text='Media: ' + self.course.media, font= 'Montserrat 7',foreground="#ADADAD")
        media_label.pack()

        #right frame 
        title2_label = ttk.Label(master=right_frame,text='Ratings', font= 'Montserrat 15 bold' )
        title2_label.pack()

        content_frame = ttk.Frame(master=right_frame)
 
        categories = ['1', '2', '3','4','5']
        values = [25, 30, 20, 35,40]

        # Define colors
        darker_orange = '#FFCE21'  # Slightly darker shade of orange
        gray = '#ADADAD'  # Gray color for text

        # Create a figure and plot
        fig, ax = plt.subplots(figsize=(4, 3))
        bars = ax.barh(categories, values, color=darker_orange)  # Use barh for horizontal bar plot

        # Add text annotations with padding and formatting
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'({width})', va='center', color=gray)

        ax.xaxis.set_visible(False)
        ax.set_title('Avg Score/sum of all ratings')
        # Create a canvas
        canvas = FigureCanvasTkAgg(fig, master=content_frame)
        canvas.draw()

        # Place the canvas on the tkinter window
        canvas.get_tk_widget().pack()

        content_frame.configure(borderwidth=2, relief="ridge")
        
        content_frame.pack()
        right_frame.pack(side='left',pady=60,padx=40)
        left_frame.pack(side='left',pady=60, padx=40)

        add_label = ttk.Label(master=left_frame,text='Course Add-Ons', font= 'Montserrat 15 bold' )
        add_label.pack()
 
        for adds in self.course.add_ons:
            addon_label = ttk.Label(master=left_frame, text= adds, font= 'Montserrat 9 bold',foreground='white', background='black')
            addon_label.pack()


        CourseInfoFrame.pack(pady=40)


    