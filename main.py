from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

root = Tk()

root.title("Weather App")
main_window = ttk.Frame(root, padding="100 100 150 150")
main_window.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(main_window, text="Temperature Data: ").grid(column=1, row=1, sticky=E)

def precipitation_warning ():
    messagebox.showerror("PRECIPITATION WARNING!", "RAIN WARNING!")


precipitation_warning()

root.mainloop()
