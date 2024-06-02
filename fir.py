import tkinter as tk
from tkinter import ttk

class fir(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Finite Impulse Response", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Back to Main Window", command=lambda: controller.show_frame(MainWindow))
        button.pack()

from main_window import MainWindow
