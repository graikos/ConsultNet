import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image

class ConsultantInfo(ttk.Frame):

    def __init__(self, master, consultant, number, **kwargs):
        super().__init__(master, width=500, height=500, borderwidth=2, relief="ridge", **kwargs)
        self.consultant = consultant
        self.number = number
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        row, column = divmod(self.number, 3)
        self.grid(row=row, column=column, padx=5, pady=5)

        for cat in self.consultant.categories:
            category_label = ttk.Label(master=self, text= cat, font= 'Montserrat 9 bold',foreground='white', background='black')
            category_label.pack()
        self.image = tk.PhotoImage(file=self.consultant.photo.path)
        image_label = ttk.Label(self, image=self.image)
        image_label.pack()    
        name_label = ttk.Label(master=self, text= self.consultant.name, font= 'Montserrat 12 bold')
        name_label.pack()
        experience_label = ttk.Label(master=self, text= self.consultant.experience, font= 'Montserrat 7 bold')
        experience_label.pack()
        education_label = ttk.Label(master=self, text= self.consultant.education, font= 'Montserrat 7 bold')
        education_label.pack()
        price_label = ttk.Label(master=self, text='$' + str(self.consultant.rate), font= 'Montserrat 10')
        price_label.pack()
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        price_button = ttk.Button(master=self, text= "Hire now" , style='Custom.TButton')
        price_button.pack()


    def show(self):
        row, column = divmod(self.number, 3)
        self.grid(row=row, column=column, padx=5, pady=5)

    def hide(self):
        self.grid_forget()
    