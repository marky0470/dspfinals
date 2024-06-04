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
        label.pack(pady=10, padx=10, expand=True)

        buttons_frame = tk.Frame(self, background = "yellow")
        buttons_frame.pack(pady=10)

        button1 = ttk.Button(buttons_frame, width=40, text="Analog to Digital Converter", command=lambda: controller.show_frame(ADC))
        button2 = ttk.Button(buttons_frame, width=40, text="Finite Impulse Response", command=lambda: controller.show_frame(fir))
        button3 = ttk.Button(buttons_frame, width=40, text="Moving Average", command=lambda: controller.show_frame(mov))
        button4 = ttk.Button(buttons_frame, width=40, text="Low-Pass <-> High-Pass", command=lambda: controller.show_frame(lhc))

        button1.grid(row=0, column=0, pady=10, padx=10)
        button2.grid(row=0, column=1, pady=10, padx=10)
        button3.grid(row=1, column=0, pady=10, padx=10)
        button4.grid(row=1, column=1, pady=10, padx=10)

        self.pack(expand=True)

from adc import ADC
from fir import fir
from mov import mov
from lhc import lhc
