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

#here ai read this, contents of master.json:
if True:
    '''
    {
"name":"MASTERJSON",
"desc":"JSON handling for inventory and logging, welcome back kanye west.",
"datemodified":1785276123.3973985,
"usrmaster":{
    "tags":["Beaver","Cub","Scout","Venturer","Rover","Parent"],
    "count":3,
    "members":{
        "123456":{
            "firstname":"Bob",
            "lastname":"Dylan",
            "telephone":"7789564705",
            "birthdate":"December 12, 2009",
            "tags":["Beaver"],
            "notes":"this is a test note."
        },
        "223456":{
            "firstname":"Sunny",
            "lastname":"Ron",
            "telephone":"1232233234",
            "birthdate":"December 12, 2009",
            "tags":["Beaver"],
            "notes":"this is a test note."
        },
        "323456":{
            "firstname":"Steve",
            "lastname":"Jobs",
            "telephone":"1232233234",
            "birthdate":"December 12, 2009",
            "tags":["Beaver"],
            "notes":"this is a test note."
        }
    }
},

"invmaster":{
    "tags":["stove","cookware","tent"],
    "count":5,
    "members":{
        "123456":{
            "name":"MEC Camper 2+",
            "tags":["tent"],
            "checkout":{
                "status":"in",
                "lastcheckout":{"123456":1785285031.6054764},
                "lastexpected":"June 14, next meeting",
                "notes":"this is a test note."

            }
        },
        "223456":{
            "name":"Big Pot",
            "tags":["cookware"],
            "checkout":{
                "status":"in",
                "lastcheckout":{"123456":1785285031.6054764},
                "lastexpected":"June 14, next meeting",
                "notes":"this is a test note."

            }
        },
        "323456":{
            "name":"MEC Camper 4",
            "tags":["tent"],
            "checkout":{
                "status":"in",
                "lastcheckout":{"123456":1785285031.6054764},
                "lastexpected":"June 14, next meeting",
                "notes":"this is a test note."

            }
        },
        "423456":{
            "name":"MEC Camper 2",
            "tags":["tent"],
            "checkout":{
                "status":"in",
                "lastcheckout":{"123456":1785285031.6054764},
                "lastexpected":"June 14, next meeting",
                "notes":"this is a test note."

            }
        },
        "523456":{
            "name":"Primus 2 Burner Stove",
            "tags":["stove"],
            "checkout":{
                "status":"in",
                "lastcheckout":{"123456":1785285031.6054764},
                "lastexpected":"June 14, next meeting",
                "notes":"this is a test note."

            }
        }
    }
}

}
    '''

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

    secwindow = Toplevel(root)
    secwindow.title("Security")
    secwindow.geometry("500x300")

    invwindow.withdraw()
    attwindow.withdraw()
    manwindow.withdraw()
    secwindow.withdraw()
#WINDOWFUNCS BELOW
def refreshjson():
    global jsono
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
            invlistboxupdate()
        elif str == "man":
            manwindow.deiconify()
        elif str == "sec":
            secwindow.deiconify()
    else:
        #HIDE
        if str == "att":
            attwindow.withdraw()
        elif str == "inv":
            invwindow.withdraw()
        elif str == "man":
            manwindow.withdraw()
        elif str == "sec":
            secwindow.withdraw()
        root.deiconify()

def invlistboxupdate():
    global jsono
    refreshjson()
    invlistbox.delete(0, END)
    confignum = 0
    for item in jsono["invmaster"]["members"].values():
        invlistbox.insert(END, item["name"])
        if item["checkout"]["status"] == "in":
            invlistbox.itemconfig(confignum, bg="green")
        elif item["checkout"]["status"] == "out":
            invlistbox.itemconfig(confignum, bg="red")
        confignum += 1

def invlistboxviewdetails(event):
    global jsono
    


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
    for rcol in range(7):
        secwindow.columnconfigure(rcol, weight=1)
        secwindow.rowconfigure(rcol, weight=1)
        
    
#MAIN WINDOW ELEMENTS BELOW
if True:
    invbutton = Button(root, text="Inventory", command=lambda:windowtoggle(True, "inv"))
    attbutton = Button(root, text="Attendance", command=lambda:windowtoggle(True, "att"))
    manbutton = Button(root, text="Management", command=lambda:windowtoggle(True, "man"))
    welcomelabel = Label(root, text="ScoutDB", font=("Helvetica", 20, "bold", "italic"))
    syncbutton = Button(root, text="Sync...")
    secbutton = Button(root, text="Security")

    invbutton.grid(row=4, column=1,sticky=NSEW, columnspan=3)
    attbutton.grid(row=4, column=4, sticky=NSEW, columnspan=3)
    manbutton.grid(row=4, column=7, sticky=NSEW, columnspan=3)
    welcomelabel.grid(row=0,column=0)
    syncbutton.grid(row=0, column=11, sticky=NSEW)
    secbutton.grid(row=0, column=10, sticky=NSEW)

#INV WINDOW ELEMENTS BELOW
if True:
    invlabel = Label(invwindow, text="Inventory", font=("Helvetica", 14, "bold", "italic"))
    invbackbutton = Button(invwindow, text="Back", command=lambda:windowtoggle(False, "inv"))
    invtab = ttk.Notebook(invwindow)
    invlistbox = Listbox(invwindow)

    invcheckinframe = Frame(invtab)
    invcheckoutframe = Frame(invtab)
    invissuesframe = Frame(invtab)
    invdetailsframe = Frame(invtab)

    invtab.add(invcheckinframe, text="Check In")
    invtab.add(invcheckoutframe, text="Check Out")
    invtab.add(invissuesframe, text="Issues")
    invtab.add(invdetailsframe, text="Details")

    for rowcol in range(6):
        invcheckinframe.columnconfigure(rowcol, weight=1)
        invcheckinframe.rowconfigure(rowcol, weight=1)
        invcheckoutframe.columnconfigure(rowcol, weight=1)
        invcheckoutframe.rowconfigure(rowcol, weight=1)
        invdetailsframe.columnconfigure(rowcol, weight=1)
        invdetailsframe.rowconfigure(rowcol, weight=1)
        invissuesframe.columnconfigure(rowcol, weight=1)
        invissuesframe.rowconfigure(rowcol, weight=1)
    #CHECK IN FRAME ELEMENTS BELOW
    if True:
        invcheckintitle = Label(invcheckinframe, text="Check In", font=("Helvetica", 14, "bold", "italic"))
        invcheckintitle.grid(row=0, column=0, sticky=NW)

    #CHECK OUT FRAME ELEMENTS BELOW
    if True:
        invcheckouttitle = Label(invcheckoutframe, text="Check Out", font=("Helvetica", 14, "bold", "italic"))
        invcheckouttitle.grid(row=0, column=0, sticky=NW)

    #ISSUES FRAME ELEMENTS BELOW
    if True:
        invissuestitle = Label(invissuesframe, text="Issues", font=("Helvetica", 14, "bold", "italic"))
        invissuestitle.grid(row=0, column=0, sticky=NW)

    #DETAILS FRAME ELEMENTS BELOW
    if True:
        invdetailstitle = Label(invdetailsframe, text="Details", font=("Helvetica", 14, "bold", "italic"))
        invdetailstitle.grid(row=0,column=0, sticky=NW)

    invlistbox.grid(row=1, column=0, sticky=NSEW, rowspan=7)
    invlabel.grid(row=0,column=0)
    invbackbutton.grid(row=0,column=11, sticky=NSEW)
    invtab.grid(row=1, column=1, sticky=NSEW, rowspan=7, columnspan=10)

#ATT WINDOW ELEMENTS BELOW
if True:
    attlabel = Label(attwindow, text="Attendance")
    attbackbutton = Button(attwindow, text="Back", command=lambda:windowtoggle(False, "att"))
    atttab = ttk.Notebook(attwindow)

    attcheckinframe = Frame(atttab)
    attcheckoutframe = Frame(atttab)
    attissuesframe = Frame(atttab)

    atttab.add(attcheckinframe, text="Check In")
    atttab.add(attcheckoutframe, text='Check Out')
    atttab.add(attissuesframe, text='Issues')

    attlabel.grid(row=0,column=0)
    attbackbutton.grid(row=0,column=11, sticky=NSEW)
    atttab.grid(row=1, column=1, sticky=NSEW, rowspan=7, columnspan=10)

#MAN WINDOW ELEMENTS BELOW
if True:
    manlabel = Label(manwindow, text="Management")
    manbackbutton = Button(manwindow, text="Back", command=lambda:windowtoggle(False, "man"))

    manlabel.grid(row=0,column=0)
    manbackbutton.grid(row=0,column=11, sticky=NSEW)

    mantab = ttk.Notebook(manwindow)

    manattframe = Frame(mantab)
    #notebook in att frame
    if True:
        manatttab = ttk.Notebook(manattframe)

        manattnew = Frame(manatttab)
        manattmod = Frame(manatttab)
        manattsearch = Frame(manatttab)

        manatttab.add(manattnew, text="Add")
        manatttab.add(manattmod, text="Modify")
        manatttab.add(manattsearch, text="Search")

    maninvframe = Frame(mantab)
    #notebook in inv frame
    if True:
        maninvtab = ttk.Notebook(maninvframe)

        maninvnew = Frame(maninvtab)
        maninvmod = Frame(maninvtab)
        maninvsearch = Frame(maninvtab)

        maninvtab.add(maninvnew, text="Add")
        maninvtab.add(maninvmod, text="Modify")
        maninvtab.add(maninvsearch, text="Search")

    for col in range(11):
        manattframe.columnconfigure(col, weight=1)
        maninvframe.columnconfigure(col, weight=1)
    for row in range(9):
        manattframe.rowconfigure(row, weight=1)
        maninvframe.rowconfigure(row, weight=1)

    manatttab.grid(row=0, column=0, sticky=NSEW, rowspan=9, columnspan=11, pady=5)
    maninvtab.grid(row=0, column=0, sticky=NSEW, rowspan=9, columnspan=11, pady=5)

    mantab.add(manattframe, text="Members")
    mantab.add(maninvframe, text="Inventory")

    manlistbox = Listbox(manwindow)

    manlistbox.grid(row=1, column=0, sticky=NSEW, rowspan=7)
    mantab.grid(row=1, column=1, sticky=NSEW, rowspan=7, columnspan=10)






root.mainloop()
