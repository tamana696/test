
import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "fa",
        "format": "json"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        raise ValueError("شهر پیدا نشد . ")
    result = data['results'][0]
    return result['latitude'], result['longitude']





def get_weather(city):
    latitude, longitude = get_coordinates(city)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


#city = input("inter city name:")
#print(get_weather(city)['current']['temperature_2m'])


import tkinter as tk
from tkinter import messagebox



def show_weather():
    city_entry = tk.Entry(
    window,
    font=("Arial", 14),
    justify="center"
)
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("لطفاً نام شهر را وارد کنید.")
        return None
    try:
        result = get_weather(city)

        if result is None:
            messagebox.showerror ("شهر موردنظر پیدا نشد.")
            return None

        city_name, country, temperature, humidity, wind_speed = result

        city_label.config(text=f"📍 {city_name} - {country}")

        temperature_label.config(text=f"🌡 دما: {temperature} °C")

        humidity_label.config(text=f"💧 رطوبت: {humidity} %")

        wind_label.config(text=f"💨 سرعت باد: {wind_speed} km/h")

    except Exception as e:

        messagebox.showerror(f"خطایی رخ داد:\n{e}")

window=tk.Tk()
window.title("Gajet weather")
window.config(background="green")
window.resizable(False,False)

window.geometry("400x400")




title_label = tk.Label(
    window,
    text="🌤 برنامه هواشناسی",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=25)


instruction_label = tk.Label(
    window,
    text="نام شهر را وارد کنید:",
    font=("Arial", 12)
)

instruction_label.pack()

city_entry = tk.Entry(
    window,
    font=("Arial", 14),
    justify="center"
)

city_entry.pack(
    pady=10,
    ipadx=30,
    ipady=5
)


weather_button = tk.Button(
    window,
    text="نمایش هوا",
    font=("Arial", 12, "bold"),
    command=show_weather
)

weather_button.pack(
    pady=15,
    ipadx=20,
    ipady=5
)


city_label = tk.Label(
    window,
    text="📍 ---",
    font=("Arial", 15, "bold")
)

city_label.pack(pady=10)


temperature_label = tk.Label(
    window,
    text="🌡 دما: ---",
    font=("Arial", 14)
)

temperature_label.pack(pady=5)

humidity_label = tk.Label(
    window,
    text="💧 رطوبت: ---",
    font=("Arial", 14)
)

humidity_label.pack(pady=5)

wind_label = tk.Label(
    window,
    text="💨 سرعت باد: ---",
    font=("Arial", 14)
)

wind_label.pack(pady=5)

window.mainloop()
tk.mainloop()
