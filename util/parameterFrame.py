import tkinter as tk
from tkinter import ttk

class ParameterFrame(tk.Frame):
    def __init__(self, parent, text, n):
        super().__init__(parent)

        self.option = ttk.Label(self, text=text)
        self.entry = ttk.Entry(self)
        self.option.grid(column=0, row=0, pady=4, sticky="w")
        self.entry.grid(column=0, row=1)

        self.grid(column=0, row=0+n, sticky="nsew", padx=20, pady=20)

class FileSelector(tk.Frame):
    def __init__(self, parent, text, n):
        super().__init__(parent)

        label = tk.Label(self, text=text)
        label.grid(column=0, row=0, sticky="w", pady=4)

        file_button = ttk.Button(self, text="Select File", command=lambda: self.opendialog())
        file_button.grid(column=0, row=1)

        self.grid(column=0, row=0+n, sticky="nsew", padx=20, pady=20)


