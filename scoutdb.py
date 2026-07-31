import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from pathlib import Path
#GLOBALS BELOW
root = Tk()
root.geometry("800x500")
root.title("ScoutDB")
root.configure(bg="#f0f0f0")
directory = Path(__file__).resolve()

#WINDOWS BELOW
invwindow = Toplevel(root)
invwindow.title("Inventory")
invwindow.geometry("800x500")
attwindow = Toplevel(root)
attwindow.title("Attendance")
attwindow.geometry("800x500")
manwindow = Toplevel(root)
manwindow.title("Management")
manwindow.geometry("800x500")

invwindow.withdraw()
attwindow.withdraw()
manwindow.withdraw()
#WINDOWFUNCS BELOW
def windowtoggle(a, str):
    '''
    toggle the attendance window by providing a bool to this function, along with the window name ("man", "att", or "inv").
    '''
    if a == True:
        #SHOW
        root.withdraw()
        if str == "att":
            attwindow.deiconify()
        elif str == "inv":
            invwindow.deiconify()
        elif str == "man":
            manwindow.deiconify()
    else:
        #HIDE
        if str == "att":
            attwindow.withdraw()
        elif str == "inv":
            invwindow.withdraw()
        elif str == "man":
            manwindow.withdraw()
        root.deiconify()


for col in range(11):
    invwindow.columnconfigure(col, weight=1)
    attwindow.columnconfigure(col, weight=1)
    manwindow.columnconfigure(col, weight=1)
    root.columnconfigure(col, weight=1)
for row in range(9):
    invwindow.rowconfigure(row, weight=1)
    attwindow.rowconfigure(row, weight=1)
    manwindow.rowconfigure(row, weight=1)
    root.rowconfigure(row, weight=1)
    
#MAIN WINDOW ELEMENTS BELOW
invbutton = Button(root, text="Inventory", command=lambda:windowtoggle(True, "inv"))
attbutton = Button(root, text="Attendance", command=lambda:windowtoggle(True, "att"))
manbutton = Button(root, text="Management", command=lambda:windowtoggle(True, "man"))
welcomelabel = Label(root, text="ScoutDB")

#INV WINDOW ELEMENTS BELOW
invlabel = Label(invwindow, text="Inventory")
invbackbutton = Button(invwindow, text="Back", command=lambda:windowtoggle(False, "inv"))

#ATT WINDOW ELEMENTS BELOW
attlabel = Label(attwindow, text="Attendance")
attbackbutton = Button(attwindow, text="Back", command=lambda:windowtoggle(False, "att"))

#MAN WINDOW ELEMENTS BELOW
manlabel = Label(manwindow, text="Management")
manbackbutton = Button(manwindow, text="Back", command=lambda:windowtoggle(False, "man"))

#GRIDS BELOW

invbutton.grid(row=4, column=2,sticky=NSEW, columnspan=3)
attbutton.grid(row=4, column=5, sticky=NSEW, columnspan=3)
manbutton.grid(row=4, column=8, sticky=NSEW, columnspan=3)
welcomelabel.grid(row=1,column=2)

invlabel.grid(row=0,column=0)
invbackbutton.grid(row=0,column=11, sticky=NSEW)

attlabel.grid(row=0,column=0)
attbackbutton.grid(row=0,column=11, sticky=NSEW)

manlabel.grid(row=0,column=0)
manbackbutton.grid(row=0,column=11, sticky=NSEW)


root.mainloop()
