import tkinter as tk
import ttkbootstrap as ttk

class RoundedLabel(ttk.Frame):
    def __init__(self, parent, text, radius=20, padding=10, bg="lightblue", fg="black", font=("Helvetica", 16), border_width=0, **kwargs):
        super().__init__(parent, **kwargs)
        self.canvas = tk.Canvas(self, bg=bg, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.radius = radius
        self.padding = padding
        self.bg = bg
        self.fg = fg
        self.font = font
        self.border_width = border_width

        # Create text on canvas to get bounding box size
        self.text = self.canvas.create_text(padding + radius, padding + radius, text=text, fill=fg, font=font, anchor="nw")

        bbox = self.canvas.bbox(self.text)
        self.width = (bbox[2] - bbox[0] + 2 * padding)
        self.height = (bbox[3] - bbox[1] + 2 * padding) 

        self.canvas.config(width=self.width, height=self.height)

        # Draw rounded rectangle with updated size
        self.create_rounded_rectangle(0, 0, self.width, self.height, radius, fill=bg, outline=bg, width=border_width)
        self.canvas.create_text(padding, padding, text=text, fill=fg, font=font, anchor="nw")

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        return self.canvas.create_polygon(points, **kwargs, smooth=True)
