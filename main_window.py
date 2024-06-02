import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="DSP Finals", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)

        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=10)

        button1 = tk.Button(buttons_frame, font=("Consolas", 20), width=40, height=8, relief="groove", text="Analog to Digital Converter", command=lambda: controller.show_frame(adc))
        button2 = tk.Button(buttons_frame, font=("Consolas", 20), width=40, height=8, relief="groove", text="Finite Impulse Response", command=lambda: controller.show_frame(fir))
        button3 = tk.Button(buttons_frame, font=("Consolas", 20), width=40, height=8, relief="groove", text="Moving Average", command=lambda: controller.show_frame(mov))
        button4 = tk.Button(buttons_frame, font=("Consolas", 20), width=40, height=8, relief="groove", text="Low-Pass <-> High-Pass", command=lambda: controller.show_frame(lhc))

        button1.grid(row=0, column=0, pady=10, padx=10)
        button2.grid(row=0, column=1, pady=10, padx=10)
        button3.grid(row=1, column=0, pady=10, padx=10)
        button4.grid(row=1, column=1, pady=10, padx=10)

from adc import adc
from fir import fir
from mov import mov
from lhc import lhc

