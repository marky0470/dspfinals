import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from util.parameterFrame import ParameterFrame
from main_window import MainWindow
import lowpass
from lowpass import lowpass_filter
import highpass
from highpass import highpass_filter
from util.parameterFrame import FileSelector
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import os

class lhc(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.passType = None

        self.columnconfigure(0, weight=20)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        # Header
        self.headerFrame = tk.Frame(self, background="darkslategray1")
        self.headerFrame.grid(column=0,row=0,columnspan=2, sticky="nsew")
        title = ttk.Label(self.headerFrame, text="Lowpass and Highpass Converter", font=("Helvetica", 18), background="darkslategray1")
        title.pack(side="left", padx=20)
        backButton = ttk.Button(self.headerFrame, text="Back", command=lambda: controller.show_frame(MainWindow))
        backButton.pack(side="right", padx=20)
        
        # Options side panel
        self.optionsFrame = tk.Frame(self, background="slateblue")
        self.optionsFrame.grid(column=1,row=1, sticky="nsew")
        self.optionsFrame.input = None
        
        lowpassButton = ttk.Radiobutton(self.optionsFrame, text="Lowpass", variable=self.passType, value="low", command=lambda: self.pickPassType("low"))
        lowpassButton.grid(column=0,row=2, sticky="nsew", padx=5, pady=5)
        highpassButton = ttk.Radiobutton(self.optionsFrame, text="Highpass", variable=self.passType, value="high", command=lambda: self.pickPassType("high"))
        highpassButton.grid(column=1,row=2, sticky="nsew", padx=5, pady=5)
        
        #cutFreq = ParameterFrame(self.optionsFrame, "Frequency", 0)
        fileSelectorButton = ttk.Button(self.optionsFrame, text = "Select File", command = lambda: self.select_audio_file(parent))
        fileSelectorButton.grid(column=0,row=3, sticky="nsew", padx=20, pady=20)
        
        enterButton = ttk.Button(self.optionsFrame, text="Convert", command=lambda: self.process(parent.input))
        enterButton.grid(column=1,row=3, sticky="nsew", padx=20, pady=20)
        
        self.errorLabel = ttk.Label(self.optionsFrame, text="", foreground="red")
        self.errorLabel.grid(column=0, row=5, sticky="nsew", pady=20, padx=20)
        
        # Output frame
        self.outputFrame = tk.Frame(self, background="paleturquoise1")
        self.outputFrame.grid(column=0, row=1, sticky="nsew")

        # Where the any output images should go
        self.outputLabel = ttk.Label(self.outputFrame, text="Output")
        self.outputLabel.pack(expand=True)
        
    def pickPassType(self, type):
        self.passType = type
    
    def select_audio_file(self, parent):
        file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("WAV files", "*.wav")])
        parent.input = file_path
        
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
            
    def process(self, parent):
        file = self.getInputs()
        
        file_path = self.outputFrame.input
        if file_path:
            extension = os.path.splitext(file_path)[1].lower()
        else:
            self.errorLabel.config(text="File required")
            return
        isLowpass = extension in audio_extensions
        
        if self.optionsFrame.input is None:
            self.errorLabel.config(text="File required")
            return
        
        self.errorLabel.config(text="")
        
        if self.optionsFrame.input.get() == "Lowpass":
            inputs = self.getInputs()
            audioPlot = lowpass.lowpass_filter(input_wav_path, output_lowpass_path, cutoff_freq)
            self.updateImage(audioPlot, True)

            filteredAudioPlot = lowpass.lowpass_filter(path, self.passType, int(inputs[0]), int(inputs[1]))
            self.updateImage(filteredAudioPlot, False)

        elif self.optionsFrame.input.get() == "Highpass":
            inputs = self.getInputs()
            filteredAudioPlot = highpass.highpass_filter(path, self.passType, int(inputs[0]), int(inputs[1]))
            self.updateImage(filteredAudioPlot, False)
        
        lowpass_filter(parent, 'filtered_lowpass.wav', 1000)
        highpass_filter(parent, 'filtered_highpass.wav', 1000)
        
        plot = Image.open('lowpass.png')
        plot = ImageTk.PhotoImage(plot)
        self.outputLabel.config(image = plot)
        self.outputLabel.image = plot
        
        plot = Image.open('highpass.png')
        plot = ImageTk.PhotoImage(plot)
        self.outputLabel.config(image = plot)
        self.outputLabel.image = plot
            
audio_extensions = [".wav"]