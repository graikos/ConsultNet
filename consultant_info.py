import ttkbootstrap as ttk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from RoundedLabel import RoundedLabel

def make_circle(image_path, size):
    # Load the image
    image = Image.open(image_path)
    image = image.resize((size, size))  # Resize the image to the desired size
    
    # Create a circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    
    # Apply the circular mask to the image
    image.putalpha(mask)

    return ImageTk.PhotoImage(image)
  
class ConsultantInfo(ttk.Frame):

    def __init__(self, master, consultant, number, command=None, **kwargs):
        super().__init__(master,borderwidth=2, relief="ridge", **kwargs)
        self.consultant = consultant
        self.number = number
        self.command = command
        # self.master = master
        self.create_widgets()


    
    def create_widgets(self):
        # TODO: change this text
        row, column = divmod(self.number, 3)
        self.grid(row=row, column=column, padx=(0,25), pady=5,ipadx=30,ipady=5)
        
        image_size = 200  # Specify the desired size for the circular image
        # Create a circular image label
        self.image = make_circle(self.consultant.photo.path, image_size)
        category_frame = ttk.Frame(master=self)
        for cat in self.consultant.categories:
            category_label = RoundedLabel(
                category_frame,
                text=cat,
                radius=25,
                padding=10,
                bg="black",
                fg="white",
                font='Montserrat 9 bold',
                border_width=0
            )
            category_label.pack(pady=10, side="left", padx=10)
        category_frame.pack()    


        image_label = ttk.Label(self, image=self.image)
        image_label.pack(pady=10)    
        name_label = ttk.Label(master=self, text= self.consultant.name, font= 'Montserrat 15 bold')
        name_label.pack(pady=(5,10))
        experience_label = ttk.Label(master=self, text="Experience: "+ self.consultant.experience, font= 'Montserrat 9')
        experience_label.pack(anchor="w",padx=(30,0),pady=10)
        education_label = ttk.Label(master=self, text="Education: "+ self.consultant.education, font= 'Montserrat 9' )
        education_label.pack(anchor="w",padx=(30,0),pady=10)
        price_label = ttk.Label(master=self, text='$' + str(self.consultant.rate) + "/h", font= 'Montserrat 10')
        price_label.pack(pady=5)
        style = ttk.Style()
        style.configure('Custom.TButton', background='#8C2F39', foreground = 'white',anchor='center')
        person_edit_icon = tk.PhotoImage(file="./resources/person_edit.png")
        price_button = ttk.Button(master=self, text= "Hire now" ,width=20, style='Custom.TButton', command=self.command,image=person_edit_icon,compound=tk.LEFT)
        price_button.image = person_edit_icon
        price_button.pack(pady=5)

    def show(self):
        row, column = divmod(self.number, 3)
        self.grid(row=row, column=column, padx=(0,25), pady=5,ipadx=30,ipady=5)

    def hide(self):
        self.grid_forget()
    