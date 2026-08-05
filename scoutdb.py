#IMPORTS BELOW
if True:
    import os
    from tkinter import *
    from tkinter import ttk
    import tkinter as tk
    from pathlib import Path
    import json
    from datetime import datetime
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
    if a == True:
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
        if str == "att":
            attwindow.withdraw()
        elif str == "inv":
            invwindow.withdraw()
        elif str == "man":
            manwindow.withdraw()
        elif str == "sec":
            secwindow.withdraw()
        root.deiconify()

def makescrollable(parent):
    outer = Frame(parent)
    outer.columnconfigure(0, weight=1)
    outer.rowconfigure(0, weight=1)
    canvas = Canvas(outer)
    scrollbar = Scrollbar(outer, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.grid(row=0, column=0, sticky=NSEW)
    scrollbar.grid(row=0, column=1, sticky=NS)
    inner = Frame(canvas)
    canvas_window = canvas.create_window((0, 0), window=inner, anchor=NW)
    def on_inner_configure(event):
        canvas.configure(scrollregion=canvas.bbox(ALL))
    def on_canvas_configure(event):
        canvas.itemconfig(canvas_window, width=event.width)
    inner.bind("<Configure>", on_inner_configure)
    canvas.bind("<Configure>", on_canvas_configure)
    return outer, inner, canvas

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

    invcheckinframe, invcheckincontent, invcheckincanvas = makescrollable(invtab)
    invcheckoutframe, invcheckoutcontent, invcheckoutcanvas = makescrollable(invtab)
    invissuesframe, invissuescontent, invissuescanvas = makescrollable(invtab)
    invdetailsframe, invdetailscontent, invdetailscanvas = makescrollable(invtab)

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
        invcheckintitle = Label(invcheckincontent, text="Check In", font=("Helvetica", 14, "bold", "italic"))
        invcheckintitle.grid(row=0, column=0, sticky=NW)

    #CHECK OUT FRAME ELEMENTS BELOW
    if True:
        invcheckouttitle = Label(invcheckoutcontent, text="Check Out", font=("Helvetica", 14, "bold", "italic"))
        invcheckouttitle.grid(row=0, column=0, sticky=NW)

    #ISSUES FRAME ELEMENTS BELOW
    if True:
        invissuestitle = Label(invissuescontent, text="Issues", font=("Helvetica", 14, "bold", "italic"))
        invissuestitle.grid(row=0, column=0, sticky=NW)

    #DETAILS FRAME ELEMENTS BELOW
    if True:
        invdetailstitle = Label(invdetailscontent, text="Details", font=("Helvetica", 14, "bold", "italic"))
        invdetailsintro = Label(invdetailscontent, text="Welcome to the details page, here you can examine inventory items in greater detail, as well as viewing timestamps such as checkouts and owners. If you wish to modify items, do so in the \"Management\" section.", font=("Helvetica", 12), wraplength=450, justify="left")
        invdetailsname = Label(invdetailscontent, text="Name: ", font=("Helvetica", 12))
        invdetailstag = Label(invdetailscontent, text="Tags: ", font=("Helvetica", 12))
        invdetailsstatus = Label(invdetailscontent, text="Status: ", font=("Helvetica", 12))
        invdetailstracked = Label(invdetailscontent, text="Tracked: ", font=("Helvetica", 12))
        invdetailslastcheckout = Label(invdetailscontent, text="Last Checkout: ", font=("Helvetica", 12))
        invdetailslastexpected = Label(invdetailscontent, text="Last Expected Return: ", font=("Helvetica", 12))
        invdetailsnotes = Label(invdetailscontent, text="Notes: ", font=("Helvetica", 12))

        invdetailstitle.grid(row=0,column=0, sticky=NW)
        invdetailsintro.grid(row=1,column=0, sticky=NW)
        invdetailsname.grid(row=2,column=0, sticky=NW)
        invdetailstag.grid(row=3,column=0, sticky=NW)
        invdetailsstatus.grid(row=4,column=0, sticky=NW)
        invdetailstracked.grid(row=5,column=0, sticky=NW)
        invdetailslastcheckout.grid(row=6,column=0, sticky=NW)
        invdetailslastexpected.grid(row=7,column=0, sticky=NW)
        invdetailsnotes.grid(row=8,column=0, sticky=NW)

        invdetailscanvas.configure(width=600)

    def invlistboxviewdetails(event):
        global jsono
        compsel = invlistbox.curselection() #[index num]
        select = invlistbox.get(compsel[0]) #"987654:THING"
        select = select.split(":")[0]
        if select in jsono["invmaster"]["members"]:
            tagflag = False
            view = jsono["invmaster"]["members"][select]
            checkoutview = jsono["invmaster"]["members"][select]["checkout"]

            invdetailsname.config(text="Name: " + view["name"])
            for tag in view["tags"]:
                if tagflag == False:
                    tagbuild = "Tags: "+tag
                    tagflag = True
                tagbuild += ", "+tag
            if view["tracked"] == 1:
                invdetailstracked.config(text="Tracked: Yes")
            else:
                invdetailstracked.config(text="Tracked: No")
            invdetailsstatus.config(text="Status: "+checkoutview["status"])
            buildmember = next(iter(checkoutview["lastcheckout"])) #"123456"
            buildmember = jsono #################################################################################
                    

        else:
            print("ERROR: inv member not found",select)

    def invlistboxupdate():
        global jsono
        refreshjson()
        invlistbox.delete(0, END)
        confignum = 0

        for item in jsono["invmaster"]["members"]:
            if jsono["invmaster"]["members"][item]["tracked"] == 1:
                invlistbox.insert(END, str(item)+":"+jsono["invmaster"]["members"][item]["name"])
                if jsono["invmaster"]["members"][item]["checkout"]["status"] == "in":
                    invlistbox.itemconfig(confignum, bg="green")
                elif jsono["invmaster"]["members"][item]["checkout"]["status"] == "out":
                    invlistbox.itemconfig(confignum, bg="red")
            else:
                invlistbox.insert(END, str(item)+": "+item["name"])
                invlistbox.itemconfig(confignum, bg="gray")
            confignum += 1
        """
        for item in jsono["invmaster"]["members"].values():
            invlistbox.insert(END, item["name"])
            if item["checkout"]["status"] == "in":
                invlistbox.itemconfig(confignum, bg="green")
            elif item["checkout"]["status"] == "out":
                invlistbox.itemconfig(confignum, bg="red")
            confignum += 1        
        """

    invlistbox.grid(row=1, column=0, sticky=NSEW, rowspan=7, columnspan=2)
    invlistbox.bind("<Double-Button-1>", invlistboxviewdetails)
    invlabel.grid(row=0,column=0)
    invbackbutton.grid(row=0,column=11, sticky=NSEW)
    invtab.grid(row=1, column=2, sticky=NSEW, rowspan=6, columnspan=10)

#ATT WINDOW ELEMENTS BELOW
if True:
    attlabel = Label(attwindow, text="Attendance")
    attbackbutton = Button(attwindow, text="Back", command=lambda:windowtoggle(False, "att"))
    atttab = ttk.Notebook(attwindow)

    attcheckinframe, attcheckincontent, attcheckincanvas = makescrollable(atttab)
    attcheckoutframe, attcheckoutcontent, attcheckoutcanvas = makescrollable(atttab)
    attissuesframe, attissuescontent, attissuescanvas = makescrollable(atttab)

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

    manattframe, manattcontent, manattcanvas = makescrollable(mantab)
    manatttab = ttk.Notebook(manattcontent)
    manattnew, manattnewcontent, manattnewcanvas = makescrollable(manatttab)
    manattmod, manattmodcontent, manattmodcanvas = makescrollable(manatttab)
    manattsearch, manattsearchcontent, manattsearchcanvas = makescrollable(manatttab)
    manatttab.add(manattnew, text="Add")
    manatttab.add(manattmod, text="Modify")
    manatttab.add(manattsearch, text="Search")

    maninvframe, maninvcontent, maninvcanvas = makescrollable(mantab)

    maninvtab = ttk.Notebook(maninvcontent)
    maninvnew, maninvnewcontent, maninvnewcanvas = makescrollable(maninvtab)
    maninvmod, maninvmodcontent, maninvmodcanvas = makescrollable(maninvtab)
    maninvsearch, maninvsearchcontent, maninvsearchcanvas = makescrollable(maninvtab)
    maninvtab.add(maninvnew, text="Add")
    maninvtab.add(maninvmod, text="Modify")
    maninvtab.add(maninvsearch, text="Search")

    manatttab.grid(row=0, column=0, sticky=NSEW, rowspan=9, columnspan=11, pady=5)
    maninvtab.grid(row=0, column=0, sticky=NSEW, rowspan=9, columnspan=11, pady=5)

    mantab.add(manattframe, text="Members")
    mantab.add(maninvframe, text="Inventory")

    manlistbox = Listbox(manwindow)

    manlistbox.grid(row=1, column=0, sticky=NSEW, rowspan=7)
    mantab.grid(row=1, column=1, sticky=NSEW, rowspan=7, columnspan=10)






root.mainloop()
