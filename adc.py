import tkinter as tk
from tkinter import ttk
from util.parameterFrame import ParameterFrame
from main_window import MainWindow
from util.parameterFrame import FileSelector

class ADC(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.columnconfigure(0, weight=20)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        # Header
        self.headerFrame = tk.Frame(self, background="red")
        self.headerFrame.grid(column=0,row=0,columnspan=2, sticky="nsew")
        title = ttk.Label(self.headerFrame, text="Analog To Digital Converter", font=("Helvetica", 18), background="red")
        title.pack(side="left", padx=20)
        backButton = ttk.Button(self.headerFrame, text="Back", command=lambda: controller.show_frame(MainWindow))
        backButton.pack(side="right", padx=20)
        
        # Options side panel
        self.optionsFrame = tk.Frame(self, background="blue")
        self.optionsFrame.grid(column=1,row=1, sticky="nsew")
        
        timeField = ParameterFrame(self.optionsFrame, "Time", 0)
        freqFieldy = ParameterFrame(self.optionsFrame, "Frequency", 1)

        enterButton = ttk.Button(self.optionsFrame, text="Test", command=lambda: self.process())
        enterButton.grid(column=0,row=3, sticky="nsew", padx=20, pady=20)

        # Output frame
        self.outputFrame = tk.Frame(self, background="pink")
        self.outputFrame.grid(column=0, row=1, sticky="nsew")

        # Where the any output images should go
        outputLabel = ttk.Label(self.outputFrame, text="Output")
        outputLabel.pack(expand=True)

        
    # Retrieves all input values from all ParameterFrames, returned as a list
    def getInputs(self):
        parameterFrames = [child for child in self.optionsFrame.winfo_children() if isinstance(child, ParameterFrame)]
        inputs = [child.entry.get() for child in parameterFrames]
        return inputs
    
    def process(self):
        data = self.getInputs()
        # data is a list, access through indexes

# if __name__ == "__main__":
#     root = tk.Tk()
#     controller = tk.Toplevel(root)
#     root.geometry("1280x720")
#     frame = ADC(root, controller)
#     frame.pack(fill="both", expand=True)
#     root.mainloop()







