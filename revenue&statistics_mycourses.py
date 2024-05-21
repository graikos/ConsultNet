import ttkbootstrap as ttk
from course_item import CourseItem
from domain.course import courses_dict


class ServicesCoursesPage(ttk.Frame):

    def __init__(self, master, router, **kwargs):
        super().__init__(master, **kwargs)
        self.course_widgets = []
        self.router = router

        self.create_widgets()

    def create_widgets(self):
       #first row of labels
        logo_frame = ttk.Frame(master = self)
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

        t_label = ttk.Label(master=self, text='Revenue & Statistics', font= 'Montserrat 16 bold')
        t_label.pack(pady=40)

        #second row of labels
        options_frame = ttk.Frame(master = self)
        # add textlabel
        courses_label = ttk.Label(master=options_frame, text='My Courses', font= 'Montserrat 12',foreground="#ADADAD")
        services_label = ttk.Label(master=options_frame, text='Services', font= 'Montserrat 12 underline bold')
        courses_label.pack(side = 'left',padx=40,pady=50)
        services_label.pack(side = 'left',padx=40,pady=50)

        options_frame.pack()

        for course in courses_dict.values():
            self.course_widgets.append(
                CourseItem(
                    self,
                    course,
                    0,
                    controller=self
                )
            )

        # self.pack()

    def show(self, context=None):
        self.pack(expand=True, fill="both")

    def hide(self):
        self.pack_forget()
