import tkinter as tk
from tkinter import ttk
from main_window import MainWindow
from adc import ADC
from fir import fir
from mov import mov
from lhc import lhc

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DSP Finals")
        self.geometry("1280x720")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.create_frames()

        self.show_frame(MainWindow)

    def create_frames(self):
        for F in (MainWindow, ADC, fir, mov, lhc):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    
    app.mainloop()
