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
import altitudemeasurement

#declaring root window
root = Tk()

altitude = 0
y = []
temperatures = []
pascals = []

def precipitation_warning ():
    messagebox.showerror("PRECIPITATION WARNING!", "RAIN WARNING!") 

#initializing window
root.title("Weather App") #window title
root.configure(background="grey")
root.minsize(800, 800)  # width, height
root.maxsize(1920, 1080)  # setting (arbitrary) max size
root.geometry("600x600+150+150")  # width x height + x + y

#label1 = ttk.Label(main_window, text="Temperature Data: ").grid(column=0, row=0, sticky=W)

def get_measurements():
    y = portreader.get_data()

    i=0
    j=0
    x=[]

    while i<len(y):
        if i%2==0:
            temperatures.append(y[i])
            j+=1
            x.append(j)
        else:
            pascals.append(y[i])

        i+=1
    return [temperatures, pascals]

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

    pplt.plot(x, pascals)
    pplt.xlabel("Time: ")
    pplt.ylabel("Air pressure in pascals ")
    pplt.title("Air pressure measurements: ")
    pplt.show()


def get_alt():
    altitude = altitudemeasurement.get_altitude(entry_field1.get(), entry_field2.get())
    messagebox.showwarning("Altitude at lat, long", altitude) 
    return altitude

#creating button to call graph
temperature_button = Button(root, activebackground="dark gray", bd=4, command=temperature_button_click, width=20, height=5, text="Display temperature data")
entry_field1 = Entry(root, textvariable="Latitude: ")
entry_field2 = Entry(root, textvariable="Longitude: ")
height_button = Button(root, activebackground="dark gray", bd=4, 
                            command=get_alt, 
                            width=20, height=5, text="Get height at location")

entry_field1.place(x=400, y=150)
entry_field2.place(x=400, y =400)
temperature_button.place(x=150, y=150)
height_button.place(x=150, y=400)

root.mainloop()

precipitation_warning()