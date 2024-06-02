import tkinter
import customtkinter
# import adcWindow
m = tkinter.Tk()

m.geometry("900x460")

'''
widgets are added here
'''
label = tkinter.Label(master=m, text="DSP Finals", padx = 50, pady = 50, font = ("Consolas", 50))
label.grid(row = 0, column = 0, pady = 0)

button1 = tkinter.Button(master=m, width=20, text="ADC", font = ("Consolas", 20))
button2 = tkinter.Button(master=m, width=20, text="FIR Filter", font = ("Consolas", 20))
button3 = tkinter.Button(master=m, width=20, text="Moving Average", font = ("Consolas", 20))
button4 = tkinter.Button(master=m, width=20, text="Low-High Pass", font = ("Consolas", 20))

button1.grid(row = 1, column = 0, padx = 20, pady = 20)
button2.grid(row = 1, column = 1, padx = 20, pady = 20)
button3.grid(row = 2, column = 0, padx = 20, pady = 20)
button4.grid(row = 2, column = 1, padx = 20, pady = 20)

m.mainloop()

