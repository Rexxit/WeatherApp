# importing tkinter for the UI
import tkinter as tk
# importing requests for the json files
import requests
# importing time to format date variables
import time


# function to call the API and get all the data I need and convert it to a text and place it on the canvas
def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=751d58da7852d9510737109a25529a0e"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int((json_data['main']['temp'] - 273.15) * 9 / 5 + 32)
    min_temp = int((json_data['main']['temp_min'] - 273.15) * 9 / 5 + 32)
    max_temp = int((json_data['main']['temp_max'] - 273.15) * 9 / 5 + 32)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 14400))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 14400))
    country = json_data['sys']['country']

    # Placing the data into a text format
    final_info = condition + "\n" + description + "\n" + str(temp) + "°F"
    final_info = condition + "\n" + description + "\n" + str(temp) + "°F"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "°F" + "\n" + "Min Temp: " + str(
        min_temp) + "°F" + "\n" + "Pressure: " \
                 + str(pressure) + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Windspeed: " + str(
        wind_speed) + " mph" \
                 + "\n" + "Sunrise: " + str(sunrise) + "am" + "\n" + "Sunset: " + str(
        sunset) + "pm" + "\n" + "Country: " + str(country)
    # Assinging the text strings to the labels from the canvas
    label1.config(text=final_info)
    label2.config(text=final_data)


# Defining the UI for the app, the size(geometry), and the title
canvas = tk.Tk()
canvas.geometry("600x600")
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
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
