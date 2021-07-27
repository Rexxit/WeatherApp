# importing tkinter for the UI
import tkinter as tk
# importing requests for the json files
import requests
# importing time to format date variables
import time

# Defining the UI for the app, the size(geometry), and the title
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

# Defining fonts for the App
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# Getting the City name from the user and setting the font size to t
textfield = tk.Entry(canvas, font=t)
# Setting a padding for the textfield UI
textfield.pack(pady=20)
# Having the textfield remained focused so user doesn't need to user their mouse
textfield.focus()

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
