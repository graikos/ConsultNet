import ttkbootstrap as ttk
import tkinter as tk
from domain.consultant import CURRENT_USER


class StatsServicesPage(ttk.Frame):

    def __init__(self, master, router, context=None, **kwargs):
        super().__init__(master, **kwargs)
        self.course_widgets = []
        self.router = router
        self.consultant = context["consultant"]

        self.create_widgets()

    def create_widgets(self):
        # first row of labels
        logo_frame = ttk.Frame(master=self)
        # add textlabel
        # make text semi bold
        label1 = ttk.Label(
            master=logo_frame,
            text="Consult",
            font="Montserrat 24 bold",
            foreground="#080708",
        )
        label2 = ttk.Label(
            master=logo_frame,
            text="Net",
            font="Montserrat 24 bold",
            foreground="#8C2F39",
        )
        label1.pack(side="left")
        label2.pack(side="left")

        profile_label = ttk.Label(
            master=logo_frame,
            text="Profile",
            font="Montserrat 12",
            foreground="#ADADAD",
        )
        profile_label.bind(
            "<Button-1>",
            lambda e: self.router("stats_courses", {"consultant": CURRENT_USER}),
        )
        profile_label.pack(side="right", padx=75)
        logo_frame.pack(fill="both")

        t_label = ttk.Label(
            master=self, text="Revenue & Statistics", font="Montserrat 16 bold"
        )
        t_label.pack(pady=40)

        # second row of labels
        options_frame = ttk.Frame(master=self)
        # add textlabel
        courses_label = ttk.Label(
            master=options_frame,
            text="My Courses",
            font="Montserrat 12",
            foreground="#ADADAD",
            cursor="hand2",
        )
        courses_label.bind(
            "<Button-1>",
            lambda e: self.router("stats_courses", {"consultant": CURRENT_USER}),
        )
        services_label = ttk.Label(
            master=options_frame,
            text="Services",
            font="Montserrat 12 underline bold",
            cursor="hand2",
        )
        services_label.bind(
            "<Button-1>",
            lambda e: self.router("stats_services", {"consultant": CURRENT_USER}),
        )
        courses_label.pack(side="left", padx=40, pady=50)
        services_label.pack(side="left", padx=40, pady=50)

        options_frame.pack()

        timing_frame = ttk.Frame(master=self)
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        cb1 = ttk.Combobox(
            master=timing_frame, state="readonly", values=months, width=20
        )
        cb1.set("Pick a month")
        cb1.pack(side="left", padx=10)

        years = [
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
            2021,
            2022,
            2023,
            2024,
            2025,
            2026,
            2027,
            2028,
            2029,
            2030,
            2031,
            2032,
            2033,
        ]
        cb2 = ttk.Combobox(
            master=timing_frame, state="readonly", values=years, width=20
        )
        cb2.set("Pick a year")
        cb2.pack(side="left", padx=10)
        timing_frame.pack()

        columns = ("Date", "Client", "Category", "Request Name", "Hours", "Revenue")

        # Create a style object
        style = ttk.Style()

        # Configure the Treeview style
        style.configure(
            "Custom.Treeview",
            background="#fafafa",
            foreground="black",
            fieldbackground="lightgray",
            borderwidth=0,
        )

        # Configure the Treeview heading style
        style.configure(
            "Custom.Treeview.Heading",
            background="#8C2F39",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )

        # Create the Treeview with the custom style
        my_tree = ttk.Treeview(
            self, style="Custom.Treeview", columns=columns, show="headings"
        )

        # Define the column headings and center the data
        my_tree.heading("Date", text="Date", anchor=tk.CENTER)
        my_tree.heading("Client", text="Client", anchor=tk.CENTER)
        my_tree.heading("Category", text="Category", anchor=tk.CENTER)
        my_tree.heading("Request Name", text="Request name", anchor=tk.CENTER)
        my_tree.heading("Hours", text="Hours", anchor=tk.CENTER)
        my_tree.heading("Revenue", text="Revenue", anchor=tk.CENTER)

        # Configure the columns to center the data
        my_tree.column("Date", anchor=tk.CENTER)
        my_tree.column("Client", anchor=tk.CENTER)
        my_tree.column("Category", anchor=tk.CENTER)
        my_tree.column("Request Name", anchor=tk.CENTER)
        my_tree.column("Hours", anchor=tk.CENTER)
        my_tree.column("Revenue", anchor=tk.CENTER)

        # Add data to the table (sample data)
        data = [
            ("2024-05-01", "Client A", "Category 1", "Request A", 5, 100),
            ("2024-05-02", "Client B", "Category 2", "Request B", 8, 200),
            ("2024-05-03", "Client C", "Category 1", "Request C", 6, 150),
        ]

        for row in data:
            my_tree.insert("", "end", values=row)

        my_tree.pack(pady=35)

    def show(self, context=None):
        self.pack(expand=True, fill="both")

    def hide(self):
        self.pack_forget()
