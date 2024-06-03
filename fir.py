import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import firImage
from PIL import Image, ImageTk



class fir(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.input = None
        self.filtered = None

        label = tk.Label(self, text="Finite Impulse Response", font=("Helvetica", 18))
        label.grid(column=0, row=0, pady=10, padx=10, columnspan=2)

        file_button = ttk.Button(self, text="Select File", command=lambda: self.opendialog())
        file_button.grid(column=0, row=1, pady=10, padx=10, columnspan=2)

        label1 = tk.Label(self)
        self.input_label = label1
        label1.grid(column=0, row=2, pady=10, padx=10)

        label2 = tk.Label(self)
        self.output_label = label2
        label2.grid(column=1, row=2, pady=10, padx=10)

        button = ttk.Button(self, text="Back to Main Window", command=lambda: controller.show_frame(MainWindow))
        button.grid(column=0, row=3, pady=10, padx=10, columnspan=2)
    
    def opendialog(self):
        path = filedialog.askopenfilename(title="Select Audio or Image File",
                                          filetypes=[("Image Files", image_extensions), ("Audio Files", audio_extensions)])
        
        extension = os.path.splitext(path)[1].lower()
        if extension in image_extensions:

            input_image = Image.open(path)
            
            photo = ImageTk.PhotoImage(input_image)
            self.input_label.config(image=photo)
            self.input_label.image = photo

            filtered_image = ImageTk.PhotoImage(firImage.filterImage(path))
            self.output_label.config(image=filtered_image)
            self.output_label.image = filtered_image

        elif extension in audio_extensions:

            audio_plot = FIRscript.plotAudio(path)

            photo = ImageTk.PhotoImage(audio_plot)
            self.input_label.config(image=photo)
            self.input_label.image = photo

            filtered_audio_plot = FIRscript.filterAudio(path)

            photo = ImageTk.PhotoImage(filtered_audio_plot)
            self.output_label.config(image=photo)
            self.output_label.image = photo
        

image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
audio_extensions = ['.mp3', '.wav']

from main_window import MainWindow
import FIRscript
