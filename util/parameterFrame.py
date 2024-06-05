import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ParameterFrame(tk.Frame):
    def __init__(self, parent, text, n):
        super().__init__(parent)

        self.option = ttk.Label(self, text=text)
        self.entry = ttk.Entry(self)
        self.option.grid(column=0, row=0, pady=4, sticky="w")
        self.entry.grid(column=0, row=1)

        self.grid(column=0, row=0+n, sticky="nsew", padx=20, pady=20)

image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
audio_extensions = ['.mp3', '.wav']
class FileSelector(tk.Frame):
    def __init__(self, parent, text, n):
        super().__init__(parent)

        label = tk.Label(self, text=text)
        label.grid(column=0, row=0, sticky="w", pady=4)

        file_button = ttk.Button(self, text="Browse", command=lambda: self.opendialog(parent))
        file_button.grid(column=0, row=1)

        self.grid(column=0, row=0+n, sticky="nsew", padx=20, pady=20)

    def opendialog(self, parent):
        path = filedialog.askopenfilename(title="Select Audio or Image File", filetypes=[("Image Files", image_extensions), ("Audio Files", audio_extensions)])
        parent.input = path

class EnterButton(ttk.Button):
    def __init__(self, parent, text, command, n):
        super().__init__(parent, text=text, command=command)
        
        self.grid(column=0, row=0+n, sticky="nsew", padx=20, pady=20)
