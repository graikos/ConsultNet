from tkinter import *
import ttkbootstrap as tb

# Create a tkinter window
root = tb.Window()
root.title("Table Example")
root.geometry('1000x800')

columns = ("Date","Client", "Category", "Request Name" , "Hours", "Revenue")

# Create a treeview with columns
my_tree = tb.Treeview(root, bootstyle = "danger", columns=columns, show="headings")

# Define column headings
my_tree.heading("Date", text="Date")
my_tree.heading("Client", text="Client")
my_tree.heading("Category", text="Category")
my_tree.heading("Request Name", text="Request name")
my_tree.heading("Hours", text="Hours")
my_tree.heading("Revenue", text="Revenue")

# Add data to the table (sample data)
data = [
    ("2024-05-01", "Client A", "Category 1", "Request A", 5, 100),
    ("2024-05-02", "Client B", "Category 2", "Request B", 8, 200),
    ("2024-05-03", "Client C", "Category 1", "Request C", 6, 150),
]

for row in data:
    my_tree.insert("", "end", values=row)



# Pack the treeview to the window
my_tree.pack()

# Run the tkinter event loop
root.mainloop()
