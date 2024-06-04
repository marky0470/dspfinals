import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf
import matplotlib.dates as mdates
from main_window import MainWindow
import threading
import time

class mov(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Moving Average", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)

        stocks = ['TSLA', 'AAPL', 'GOOGL', 'MSFT']
        self.selected_stock = tk.StringVar()
        self.selected_stock.set(stocks[0]) 
        dropdown = ttk.Combobox(self, textvariable=self.selected_stock, values=stocks)
        dropdown.pack(side="top", padx=20, pady=20)     

        button = tk.Button(self, text="Download and Plot", command=self.download_and_plot, padx=20, pady=10, bg='white')
        button.pack(side="top", padx=10, pady=10)  

        self.canvas_widget = None

        button = ttk.Button(self, text="Back to Main Window", command=lambda: controller.show_frame(MainWindow))
        button.pack()

        # Start the update thread
        self.update_thread = threading.Thread(target=self.update_loop)
        self.update_thread.start()

    def update_loop(self):
        while True:
            # Update the graph every 60 seconds
            time.sleep(60)
            self.download_and_plot()

    def download_and_plot(self):
        if self.canvas_widget is not None:
            self.canvas_widget.destroy()

        stock = self.selected_stock.get()
        data = yf.download(stock, start='2020-01-01')
        data['MA_20'] = data['Close'].rolling(window=20).mean()

        figure = Figure(figsize=(19.2, 10.8), dpi=100)  

        plot = figure.add_subplot(1, 1, 1)
        plot.plot(data.index, data['Close'], label='Close')
        plot.plot(data.index, data['MA_20'], label='20-day moving average')
        plot.legend()
        plot.set_title(stock)

        plot.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plot.xaxis.set_major_locator(mdates.MonthLocator()) 
        for label in plot.get_xticklabels():
            label.set_fontsize(8)  
            label.set_rotation(45)  

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        self.canvas_widget = canvas.get_tk_widget()
        self.canvas_widget.pack()