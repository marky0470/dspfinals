import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf
import matplotlib.dates as mdates
from main_window import MainWindow
import threading
import time

class MOV(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.columnconfigure(0, weight=20)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        self.headerFrame = tk.Frame(self, background="red")
        self.headerFrame.grid(column=0,row=0,columnspan=2, sticky="nsew")
        title = ttk.Label(self.headerFrame, text="MOV Operation", font=("Helvetica", 18), background="red")
        title.pack(side="left", padx=20)
        backButton = ttk.Button(self.headerFrame, text="Back", command=lambda: controller.show_frame(MainWindow))
        backButton.pack(side="right", padx=20)
    
        self.optionsFrame = tk.Frame(self, background="blue")
        self.optionsFrame.grid(column=1,row=1, sticky="nsew")
        
        stocks = ['TSLA', 'AAPL', 'GOOGL', 'MSFT']
        self.selected_stock = tk.StringVar()
        self.selected_stock.set(stocks[0]) 
        dropdown = ttk.Combobox(self.optionsFrame, textvariable=self.selected_stock, values=stocks)
        dropdown.grid(column=0, row=0, padx=(20, 30), pady=20)

        enterButton = ttk.Button(self.optionsFrame, text="Download and Plot", command=self.download_and_plot)
        enterButton.grid(column=0, row=1, sticky="nsew", padx=(20, 30), pady=20)

        self.outputFrame = tk.Frame(self, background="pink")
        self.outputFrame.grid(column=0, row=1, sticky="nsew")
        self.canvas_widget = None
        self.update_thread = threading.Thread(target=self.update_loop)
        self.update_thread.start()

    def update_loop(self):
        while True:
            time.sleep(60)
            self.download_and_plot()

    def download_and_plot(self):
        if self.canvas_widget is not None:
            self.canvas_widget.destroy()

        stock = self.selected_stock.get()
        data = yf.download(stock, start='2020-01-01')
        data['MA_20'] = data['Close'].rolling(window=20).mean()

        figure = Figure(figsize=(15, 4.5), dpi=100)  

        plot = figure.add_subplot(1, 1, 1)
        plot.plot(data.index, data['Close'], label='Close', color='blue')
        plot.plot(data.index, data['MA_20'], label='20-day moving average', color='pink')
        plot.legend()
        plot.set_title(stock)

        plot.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plot.xaxis.set_major_locator(mdates.MonthLocator()) 
        for label in plot.get_xticklabels():
            label.set_fontsize(8)  
            label.set_rotation(45)  

        canvas = FigureCanvasTkAgg(figure, self.outputFrame)
        canvas.draw()
        self.canvas_widget = canvas.get_tk_widget()
        self.canvas_widget.pack(expand=True, fill='both')