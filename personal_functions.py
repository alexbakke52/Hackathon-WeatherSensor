import weatherapp

import time
import serial
import requests


from tkinter import*
from tkinter import ttk 
from tkinter import messagebox
#from tkinter.messagebox import showinfo





# Grabs data from serial port and adds it to a list
def get_data():    
    baud = 115200
    ser = serial.Serial('/dev/ttyACM0', baud) # Change values here!!

    timeout = time.time() + 10 # 10 seconds into the future

    ser.close()

    temp_list = []

    ser.open()



    while True:
        try:
            data = float(ser.readline().decode().strip())
            temp_list.append(data)
        except KeyboardInterrupt:
            break    
        if time.time() > timeout:
            break
        
        
    # Close the serial port    
    ser.close()

    return temp_list




#Get's measurement data from portreader and separates temperature measurements
#from air pressure measurements and returns a 'touple' of lists (temp, ap)
# !!WILL MAKE VARIABLES t AND p IN "pressure_at_sealevel.py" UNLIMITED LONG!! IMPLEMENT QUEUE TO STORE NEWEST IF USED FOR LONG TERM MEASUREMENTS !!
def get_measurements():
    y = get_data()

    i=0
    j=0

    while i<len(y):
        if i%2==0:
            weatherapp.temperatures.append(y[i])
            j+=1
            weatherapp.x.append(j)
        else:
            weatherapp.pascals.append(y[i])

        i+=1
    return [weatherapp.temperatures, weatherapp.pascals]




# Function that calculates the sea level altitude  
def pressure_at_sealevel(height): # Height = Altitude from get_altitude()

    p = get_measurements()[1] * 0.01 # Pressure
    t = get_measurements()[0] # Temperature 

    P0 = p * pow(1 - (0.0065 * height) / (t + (0.0065 * height) + 273.15), -5.257)
    return P0




# Function for displaying rain warning popup
def precipitation_warning ():
    weatherapp.player.play()
    weatherapp.messagebox.showerror("PRECIPITATION WARNING!", "RAIN WARNING!")
    weatherapp.player.stop()









# Get's user-input and finds altitude for that specific latitude and logitude.
#field1 = lat, field2=long. Returns altitude (as string)
def get_alt():
    altitude = get_altitude(weatherapp.entry_field1.get(), weatherapp.entry_field2.get())
    messagebox.showwarning("Altitude at lat, long", altitude) 
    return float(altitude)




# Runtime function, to calculate forecast values
def runtime():
    
    timeout = time.time()+60
    
    P0 = pressure_at_sealevel(weatherapp.altitude)

    while timeout > time.time():
        weatherapp.weather_data.get_nowait()
        weatherapp.weather_data.put_nowait(P0)

    weather_data_span = max(weatherapp.weather_data) - min(weatherapp.weather_data)

    if weather_data_span < 1.6:
        Zf = round(temp_zf = 127 - 0.12 * P0)

        if Zf > 4:
            precipitation_warning()

        messagebox.showwarning("Weather severity (Scale: 1-10)", Zf)

    elif weather_data_span > 1.6:
        Zr = round(temp_zr = 185 - 0.16 * P0)  
        messagebox.showwarning("Weather severity (Scale: 1-10)", Zr)

    else:
        Zs = round(temp_zs = 144 - 0.13 * P0)

        if Zs > 11:
            precipitation_warning()
        messagebox.showwarning("Weather severity (Scale: 1-10)", Zs)



# Data scrapes the altitude from given Location

def get_altitude(latitude, longitude):
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}"
    response = requests.get(url)
    data = response.json()
    if 'results' in data and len(data['results']) > 0:
        altitude = data['results'][0]['elevation']
        return altitude
    else:
        return None