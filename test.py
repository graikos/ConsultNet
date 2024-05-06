import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Sample data
categories = ['1', '2', '3','4','5']
values = [25, 30, 20, 35,40]

# Define colors
darker_orange = '#FFCE21'  # Slightly darker shade of orange
gray = '#ADADAD'  # Gray color for text

# Create tkinter window
root = tk.Tk()
root.title('Bar Plot Example')

# Create a figure and plot
fig, ax = plt.subplots()
bars = ax.barh(categories, values, color=darker_orange)  # Use barh for horizontal bar plot

# Add text annotations with padding and formatting
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'({width})', va='center', color=gray)

ax.xaxis.set_visible(False)
# Create a canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Place the canvas on the tkinter window
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Run the tkinter event loop
root.mainloop()
