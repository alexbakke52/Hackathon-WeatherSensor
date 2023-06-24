from tkinter import*
#from tkinter import ttk
#from tkinter import messagebox
#from tkinter.messagebox import showinfo
#from matplotlib import*
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
#NavigationToolbar2Tk)
#import matplotlib.pyplot as pplt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.pyplot as pplt





import personal_functions
import vlc
import queue

# Declaring root window
root = Tk()

# Declaring global variables
altitude = 0
x=[]
y = []
temperatures = []
pascals = []
player = vlc.MediaPlayer("alarm.mp3")
# Queue for the weather data
weather_data = queue.Queue(180)






# Triggered on click of temperature_button. Displays the measurement data
# in two matplotlib plots.
def temperature_button_click():
   # Plot figure
    fig = Figure(figsize = (5, 5), dpi = 100)
  
    # data
    personal_functions.get_measurements()

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










################################################################################
################################### GUI ########################################
#------------------------------------------------------------------------------#

# Initializing values for root/window
root.title("Weather App") #window title
root.configure(background="grey")
root.minsize(800, 800)  # width, height
root.maxsize(1920, 1080)  # setting (arbitrary) max size
root.geometry("600x600+150+150")  # width x height + x + y


# Creating button to call graph
temperature_button = Button(root, activebackground="dark gray", bd=4, command = temperature_button_click(), width=20, height=5, text="Display temperature data")


# Initialize entry fields for lat/long user input
entry_field1 = Entry(root, textvariable="Latitude: ")
entry_field2 = Entry(root, textvariable="Longitude: ")


# Initialize button for altitude calculation trigger
height_button = Button(root, activebackground="dark gray", bd=4, 
                            command=personal_functions.get_alt, 
                            width=20, height=5, text="Get height at location")


# Placing the different widgets in the window
entry_field1.place(x=400, y=150)
entry_field2.place(x=400, y =400)
temperature_button.place(x=150, y=150)
height_button.place(x=150, y=400)
















# Call runtime function
personal_functions.runtime()


# After method for tk objects to allow code to be run during window uptime
root.after(0, personal_functions.runtime)


# Displays the window
root.mainloop()