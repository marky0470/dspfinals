import tkinter as tk
from tkinter import ttk



class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # self.columnconfigure(0, weight=1)
        # # self.columnconfigure(1, weight=1)

        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=4)

        # Header
        # self.headerFrame = tk.Frame(self, background="red")
        # self.headerFrame.grid(column=0, row=0, sticky="nsew")

        self.mainFrame = tk.Frame(self, background = "black")
        label = ttk.Label(self, text="DSP Finals", font=("Helvetica", 18))
        label.pack(pady=100, padx=10)

        buttons_frame = tk.Frame(self, background = "yellow")
        buttons_frame.pack(pady=10)

        LARGEFONT = ("Verdana", 20)

        button1 = ttk.Button(buttons_frame, width=40, text="Analog to Digital Converter", command=lambda: controller.show_frame(ADC))
        button2 = ttk.Button(buttons_frame, width=40, text="Finite Impulse Response", command=lambda: controller.show_frame(fir))
        button3 = ttk.Button(buttons_frame, width=40, text="Moving Average", command=lambda: controller.show_frame(mov))
        button4 = ttk.Button(buttons_frame, width=40, text="Low-Pass <-> High-Pass", command=lambda: controller.show_frame(lhc))

        button1.pack(padx=5, pady=5)
        button2.pack(padx=5, pady=5)
        button3.pack(padx=5, pady=5)
        button4.pack(padx=5, pady=5)

        self.pack(expand=True)

from adc import ADC
from fir import fir
from mov import mov
from lhc import lhc
