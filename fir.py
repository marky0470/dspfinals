import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import firImage
from PIL import Image, ImageTk
from util.parameterFrame import EnterButton
from util.parameterFrame import FileSelector
from util.parameterFrame import ParameterFrame

class fir(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.passType = None

        self.columnconfigure(0, weight=20)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        # Header
        self.headerFrame = tk.Frame(self, background="red")
        self.headerFrame.grid(column=0,row=0,columnspan=2, sticky="nsew")
        title = ttk.Label(self.headerFrame, text="Custom Frame", font=("Helvetica", 18), background="red")
        title.pack(side="left", padx=20)
        backButton = ttk.Button(self.headerFrame, text="Back", command=lambda: controller.show_frame(MainWindow))
        backButton.pack(side="right", padx=20)
        
        # Options side panel
        self.optionsFrame = tk.Frame(self)
        self.optionsFrame.grid(column=1,row=1, sticky="nsew")
        self.optionsFrame.input = None
      
        selectedFile = FileSelector(self.optionsFrame, "Input File", 0)
        self.field1 = ParameterFrame(self.optionsFrame, "Cutoff Frequency", 1)
        self.field2 = ParameterFrame(self.optionsFrame, "Number of Taps", 2)
        enterButton = EnterButton(self.optionsFrame, "Enter", command=lambda: self.process(), n=4)

        self.passTypeFrame = tk.Frame(self.optionsFrame)
        self.passTypeFrame.grid(column=0,row=3, sticky="nsew", padx=20, pady=20)
        self.lowPassButton = ttk.Radiobutton(self.passTypeFrame, text="Low Pass", variable=self.passType, value="low", command=lambda: self.setPassType("low"))
        self.lowPassButton.pack(side="left", anchor="w")
        self.highPassButton = ttk.Radiobutton(self.passTypeFrame, text="High Pass", variable=self.passType, value="high", command=lambda: self.setPassType("high"))
        self.highPassButton.pack(side="left", anchor="w")

        self.errorLabel = ttk.Label(self.optionsFrame, text="", foreground="red")
        self.errorLabel.grid(column=0, row=5, sticky="nsew", pady=20, padx=20)

        # Output frame
        self.outputFrame = tk.Frame(self, background="pink")
        self.outputFrame.grid(column=0, row=1, sticky="nsew")

        self.inputLabel = ttk.Label(self.outputFrame, text="")
        self.inputLabel.pack(expand=True,side="left")
        self.outputLabel = ttk.Label(self.outputFrame, text="")
        self.outputLabel.pack(expand=True,side="right")

    def setPassType(self, type):
        self.passType = type

    def getInputs(self):
        optionsChildren = self.optionsFrame.winfo_children()
        parameterFrames = [child for child in optionsChildren if isinstance(child, ParameterFrame)]
        inputs = [child.entry.get() for child in parameterFrames]
        return inputs
    
    def opendialog(self):
        path = filedialog.askopenfilename(title="Select Audio or Image File", filetypes=[("Image Files", image_extensions), ("Audio Files", audio_extensions)])
        self.input = path

    def process(self):
        inputs = self.getInputs()

        path = self.optionsFrame.input
        if path:
            extension = os.path.splitext(path)[1].lower()
        else:
            self.errorLabel.config(text="File required")
            return
        isImage = extension in image_extensions

        if self.passType is None:
            self.errorLabel.config(text="Missing pass type")
            return
        if self.optionsFrame.input is None:
            self.errorLabel.config(text="File required")
            return
        if '' in inputs and not isImage:
            self.errorLabel.config(text="Missing parameters")
            return
        
        self.errorLabel.config(text="")

        if isImage:
            with Image.open(path) as inputImage:
                self.updateImage(inputImage, True)

            filteredImage = firImage.filterImage(path, self.passType)
            self.updateImage(filteredImage, False)

        elif not isImage:
            inputs = self.getInputs()
            print(inputs)

            audioPlot = FIRscript.plotAudio(path)
            self.updateImage(audioPlot, True)

            filteredAudioPlot = FIRscript.filterAudio(path, self.passType, int(inputs[0]), int(inputs[1]))
            self.updateImage(filteredAudioPlot, False)
    
    def updateImage(self, image, isInput):
        photo = ImageTk.PhotoImage(image)
        if not isInput:
            self.outputLabel.config(image=None)
            self.outputLabel.config(image=photo)
            self.outputLabel.image = photo
        else:
            self.inputLabel.config(image=photo)
            self.inputLabel.image = photo


        

image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
audio_extensions = ['.mp3', '.wav']

from main_window import MainWindow
import FIRscript
