from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from matplotlib import*
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.pyplot as pplt
import portreader
import vlc
import altitudemeasurement
import queue
import pressure_at_sealevel
import time 

#declaring root window
root = Tk()

#declaring needed variables
player = vlc.MediaPlayer("alarm.mp3")
altitude = 0
x=[]
y = []
temperatures = []
pascals = []

#function for displaying rain warning popup
def precipitation_warning ():
    player.play()
    messagebox.showerror("PRECIPITATION WARNING!", "RAIN WARNING!")
    player.stop()

#initializing values for root/window
root.title("Weather App") #window title
root.configure(background="grey")
root.minsize(800, 800)  # width, height
root.maxsize(1920, 1080)  # setting (arbitrary) max size
root.geometry("600x600+150+150")  # width x height + x + y

#Get's measurement data from portreader and separates temperature measurements
#from air pressure measurements and returns a 'touple' of lists (temp, ap)
# !!WILL MAKE VARIABLES t AND p IN "pressure_at_sealevel.py" UNLIMITED LONG!! IMPLEMENT QUEUE TO STORE NEWEST IF USED FOR LONG TERM MEASUREMENTS !!
def get_measurements():
    y = portreader.get_data()

    i=0
    j=0

    while i<len(y):
        if i%2==0:
            temperatures.append(y[i])
            j+=1
            x.append(j)
        else:
            pascals.append(y[i])

        i+=1
    return [temperatures, pascals]

#Triggered on click of temperature_button. Displays the measurement data
#in two matplotlib plots.
def temperature_button_click():
   # Plot figure
    fig = Figure(figsize = (5, 5), dpi = 100)
  
    # data
    get_measurements()

    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(x, temperatures)

  
    # creating the Tkinter canvas with matplotlib
    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().place(x=50,y=50)

    #plotting the second graph, i.e air pressure graph.
    pplt.plot(x, pascals)
    pplt.xlabel("Time: ")
    pplt.ylabel("Air pressure in pascals ")
    pplt.title("Air pressure measurements: ")
    pplt.show()


#Get's user-input and finds altitude for that specific latitude and logitude.
#field1 = lat, field2=long. Returns altitude (as string)
def get_alt():
    altitude = altitudemeasurement.get_altitude(entry_field1.get(), entry_field2.get())
    messagebox.showwarning("Altitude at lat, long", altitude) 
    return float(altitude)

#creating button to call graph
temperature_button = Button(root, activebackground="dark gray", bd=4, command=temperature_button_click, width=20, height=5, text="Display temperature data")

#Initialize entry fields for lat/long user input
entry_field1 = Entry(root, textvariable="Latitude: ")
entry_field2 = Entry(root, textvariable="Longitude: ")

#initialize button for altitude calculation trigger
height_button = Button(root, activebackground="dark gray", bd=4, 
                            command=get_alt, 
                            width=20, height=5, text="Get height at location")

#Placing the different widgets in the window
entry_field1.place(x=400, y=150)
entry_field2.place(x=400, y =400)
temperature_button.place(x=150, y=150)
height_button.place(x=150, y=400)

# runtime function, to calculate forecast values

weather_data = queue.Queue(180)

def runtime():
    
    timeout = time.time()+60
    
    P0 = pressure_at_sealevel(altitude)

    while timeout > time.time():
        weather_data.get_nowait()
        weather_data.put_nowait(P0)

    weather_data_span = max(weather_data) - min(weather_data)

    if weather_data_span < 1.6:
        Zf = round(temp_zf = 127 - 0.12 * P0)

        if Zf > 4:
            precipitation_warning()

    elif weather_data_span > 1.6:
        Zr = round(temp_zr = 185 - 0.16 * P0)


    else:
        Zs = round(temp_zs = 144 - 0.13 * P0)

        if Zs > 11:
            precipitation_warning()


#after method for tk objects to allow code to be run during window uptime
root.after(0, runtime)

#displays the window
root.mainloop()


precipitation_warning()