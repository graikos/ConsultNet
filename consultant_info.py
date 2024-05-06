import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image

class ConsultantInfo(ttk.Frame):

    def __init__(self, master, consultant, **kwargs):
        super().__init__(master, **kwargs)
        self.consultant = consultant
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        ConsultantInfoFrame =  ttk.Frame(master = self.master ,width=500, height=500, borderwidth=2, relief="ridge")

        for cat in self.consultant.categories:
            category_label = ttk.Label(master=ConsultantInfoFrame, text= cat, font= 'Montserrat 9 bold',foreground='white', background='black')
            category_label.pack()
        self.image = tk.PhotoImage(file='myimage_100.png')
        image_label = ttk.Label(ConsultantInfoFrame, image=self.image)
        image_label.pack()    
        name_label = ttk.Label(master=ConsultantInfoFrame, text= self.consultant.name, font= 'Montserrat 12 bold')
        name_label.pack()
        experience_label = ttk.Label(master=ConsultantInfoFrame, text= self.consultant.experience, font= 'Montserrat 7 bold')
        experience_label.pack()
        education_label = ttk.Label(master=ConsultantInfoFrame, text= self.consultant.education, font= 'Montserrat 7 bold')
        education_label.pack()
        price_label = ttk.Label(master=ConsultantInfoFrame, text='$' + str(self.consultant.rate), font= 'Montserrat 10')
        price_label.pack()
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white')
        price_button = ttk.Button(master=ConsultantInfoFrame, text= "Hire now" , style='Custom.TButton')
        price_button.pack()

        ConsultantInfoFrame.pack()


    