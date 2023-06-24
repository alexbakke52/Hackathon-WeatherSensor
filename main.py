from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from matplotlib import*
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import portreader

#declaring root window
root = Tk()

def precipitation_warning ():
    messagebox.showerror("PRECIPITATION WARNING!", "RAIN WARNING!") 

#initializing window
root.title("Weather App") #window title
root.configure(background="grey")
root.minsize(200, 200)  # width, height
root.maxsize(500, 500)  # setting (arbitrary) max size
root.geometry("300x300+50+50")  # width x height + x + y

#label1 = ttk.Label(main_window, text="Temperature Data: ").grid(column=0, row=0, sticky=W)

def temperature_button_click():
   # Plot figure
    fig = Figure(figsize = (5, 5), dpi = 100)
  
    # data
    y = portreader.get_data()
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(y)
  
    # creating the Tkinter canvas with matplotlib
    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

#creating button to call graph
temperature_button = Button(root, activebackground="black", bd=4, command=temperature_button_click)

temperature_button.pack()


precipitation_warning()

root.mainloop()
