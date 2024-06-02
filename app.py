import tkinter as tk
from tkinter import ttk
from main_window import MainWindow
from adc import adc
from fir import fir
from mov import mov
from lhc import lhc

# from frame2 import Frame2
# from frame3 import Frame3
# from frame4 import Frame4

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Frame Stacking Example")
        self.geometry("800x600")

        # Create a container to hold all frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        self.create_frames()

        self.show_frame(MainWindow)

    def create_frames(self):
        for F in (MainWindow, adc, fir, mov, lhc):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
