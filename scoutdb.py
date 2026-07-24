import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
import csv
from pathlib import Path
#GLOBALS BELOW
root = Tk()
root.geometry("800x500")
root.title("ScoutDB")
root.configure(bg="#f0f0f0")
directory = Path(__file__).resolve()

#WINDOWS BELOW
invwindow = Toplevel(root)
attwindow = Toplevel(root)
managewindow = Toplevel(root)

for col in range(10):
    invwindow.columnconfigure(col, weight=1)
    attwindow.columnconfigure(col, weight=1)
    managewindow.columnconfigure(col, weight=1)
    root.columnconfigure(col, weight=1)
for row in range(8):
    invwindow.rowconfigure(row, weight=1)
    attwindow.rowconfigure(row, weight=1)
    managewindow.rowconfigure(row, weight=1)
    root.rowconfigure(row, weight=1)
    
#ELEMENTS BELOW
invbutton = Button(text="Inventory")


#GRIDS BELOW
root.mainloop()
