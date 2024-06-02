import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Main Window", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)

        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=10)

        button1 = ttk.Button(buttons_frame, text="Go to Frame 1", command=lambda: controller.show_frame(adc))
        button2 = ttk.Button(buttons_frame, text="Go to Frame 2", command=lambda: controller.show_frame(fir))
        button3 = ttk.Button(buttons_frame, text="Go to Frame 3", command=lambda: controller.show_frame(mov))
        button4 = ttk.Button(buttons_frame, text="Go to Frame 4", command=lambda: controller.show_frame(lhc))

        button1.grid(row=0, column=0, padx=5)
        button2.grid(row=0, column=1, padx=5)
        button3.grid(row=0, column=2, padx=5)
        button4.grid(row=0, column=3, padx=5)

from adc import adc
from fir import fir
from mov import mov
from lhc import lhc

