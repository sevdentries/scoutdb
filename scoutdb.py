#IMPORTS BELOW
if True:
    import os
    from tkinter import *
    from tkinter import ttk
    import tkinter as tk
    from pathlib import Path
    import json
#GLOBALS BELOW
if True:
    root = Tk()
    root.geometry("800x500")
    root.title("ScoutDB")
    root.configure(bg="#f0f0f0")
    directory = Path(__file__).resolve()

#JSONLOADER BELOW
if True:
    jsondecoder = json.JSONDecoder()
    jsono = ""
    jsondir = os.path.join(str(directory.parent),"Assets","master.json")
    print("attempting json loading...")
    print("loading from "+jsondir)
    try:
        with open(jsondir, "r") as f:
            jsono = f.read()
            jsono, index = jsondecoder.raw_decode(jsono)
    except Exception as e:
        print("error",e)
    finally:
        print("success")

#WINDOWS BELOW
if True:
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

if True: #WINDOWCONFIG
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
if True:
    invbutton = Button(root, text="Inventory", command=lambda:windowtoggle(True, "inv"))
    attbutton = Button(root, text="Attendance", command=lambda:windowtoggle(True, "att"))
    manbutton = Button(root, text="Management", command=lambda:windowtoggle(True, "man"))
    welcomelabel = Label(root, text="ScoutDB", font=("Helvetica", 20, "bold", "italic"))
    syncbutton = Button(root, text="Sync...")

    invbutton.grid(row=4, column=1,sticky=NSEW, columnspan=3)
    attbutton.grid(row=4, column=4, sticky=NSEW, columnspan=3)
    manbutton.grid(row=4, column=7, sticky=NSEW, columnspan=3)
    welcomelabel.grid(row=0,column=0)
    syncbutton.grid(row=0, column=11, sticky=NSEW)

#INV WINDOW ELEMENTS BELOW
if True:
    invlabel = Label(invwindow, text="Inventory", font=("Helvetica", 14, "bold", "italic"))
    invbackbutton = Button(invwindow, text="Back", command=lambda:windowtoggle(False, "inv"))
    invtab = ttk.Notebook(invwindow)

    invcheckinframe = Frame(invtab)
    invcheckoutframe = Frame(invtab)
    invissuesframe = Frame(invtab)

    invtab.add(invcheckinframe, text="Check In")
    invtab.add(invcheckoutframe, text="Check Out")
    invtab.add(invissuesframe, text="Issues")

    invlabel.grid(row=0,column=0)
    invbackbutton.grid(row=0,column=11, sticky=NSEW)
    invtab.grid(row=1, column=1, sticky=NSEW, rowspan=7, columnspan=10)

#ATT WINDOW ELEMENTS BELOW
if True:
    attlabel = Label(attwindow, text="Attendance")
    attbackbutton = Button(attwindow, text="Back", command=lambda:windowtoggle(False, "att"))

    attlabel.grid(row=0,column=0)
    attbackbutton.grid(row=0,column=11, sticky=NSEW)

#MAN WINDOW ELEMENTS BELOW
if True:
    manlabel = Label(manwindow, text="Management")
    manbackbutton = Button(manwindow, text="Back", command=lambda:windowtoggle(False, "man"))

    manlabel.grid(row=0,column=0)
    manbackbutton.grid(row=0,column=11, sticky=NSEW)




root.mainloop()
