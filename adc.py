import tkinter as tk
from tkinter import ttk
from util.parameterFrame import ParameterFrame
from main_window import MainWindow
from util.parameterFrame import FileSelector
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import ImageTk, Image

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
        ampField = ParameterFrame(self.optionsFrame, "Amplitude", 2)

        enterButton = ttk.Button(self.optionsFrame, text="Convert", command=lambda: self.process())
        enterButton.grid(column=0,row=3, sticky="nsew", padx=20, pady=20)

        # Output frame
        self.outputFrame = tk.Frame(self, background="pink")
        self.outputFrame.grid(column=0, row=1, sticky="nsew")

        # Where the any output images should go
        self.outputLabel = ttk.Label(self.outputFrame, text="Output")
        self.outputLabel.pack(expand=True)

        
    # Retrieves all input values from all ParameterFrames, returned as a list
    def getInputs(self):
        parameterFrames = [child for child in self.optionsFrame.winfo_children() if isinstance(child, ParameterFrame)]
        inputs = [child.entry.get() for child in parameterFrames]
        return inputs
        
    def testInt(self, input):
        try:
            text = int(input)
            return text
        except ValueError:
            print("not an integer.")
    
    def getAnalogSignal(self, ampl, freq, time):
        anSig = ampl * np.sin(2 * math.pi * freq * time)
        return anSig

    def getIndex(self, samprate, t):
        sampleCount =int(len(t) * (samprate / (t[-1] - t[0])))
        index = np.linspace(0, len(t) - 1, sampleCount, dtype=int)
        return index

    def digitizeSig(self, anSig, index, threshold):
        sampledSig = anSig[index]
        digitalSig = np.where(sampledSig > threshold, 1, 0)
        return digitalSig
    
    def plotTwo(self, anSig, index, digiSig, t):
        plt.figure(figsize=(6, 6))

        plt.subplot(2, 1, 1)
        plt.plot(t,anSig)
        plt.grid(True)
        plt.title('Generated Analog Signal')
        plt.xlabel('Time(s)')
        plt.ylabel('Amplitude(amp)')

        plt.subplot(2, 1, 2)
        plt.step(t[index], digiSig)
        plt.grid(True)
        plt.title('Converted Digital Signal')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude(amp)')
        
        plt.tight_layout()
        
        plt.savefig('plot.png')
    
    def process(self):
        data = self.getInputs()
        
        time_int = self.testInt(data[0])
        freq_int = self.testInt(data[1])
        ampl_int = self.testInt(data[2])
        
        t = np.linspace(0, time_int, 1000)
        f = freq_int
        amp = ampl_int
        samplingRate = 100
        threshold = 0
        
        print(time_int, f, amp, samplingRate, threshold)
        
        anSig = self.getAnalogSignal(amp, f, t)
        index = self.getIndex(samplingRate, t)
        digiSig = self.digitizeSig(anSig, index, threshold)
    
        self.plotTwo(anSig, index, digiSig, t)
        
        plot = Image.open('plot.png')
        plot = ImageTk.PhotoImage(plot)
        self.outputLabel.config(image = plot)
        self.outputLabel.image = plot

# if __name__ == "__main__":
#     root = tk.Tk()
#     controller = tk.Toplevel(root)
#     root.geometry("1280x720")
#     frame = ADC(root, controller)
#     frame.pack(fill="both", expand=True)
#     root.mainloop()







