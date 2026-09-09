#IMPORTS BELOW
if True:
    import os
    from tkinter import *
    from tkinter import ttk
    import tkinter as tk
    from pathlib import Path
    import json
    import time
    import datetime
    from tkcalendar import DateEntry
    import atexit
#GLOBALS BELOW
if True:
    root = Tk()
    root.geometry("800x500")
    root.title("ScoutDB")
    root.configure(bg="#f0f0f0")
    root.overrideredirect(True)
    directory = Path(__file__).resolve()
    init = False
    datecontinueflag = "none"

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
    master = ""
    attlog = ""
    invlog = ""
    masterdir = os.path.join(str(directory.parent),"Assets","master.json")
    attdir = os.path.join(str(directory.parent),"Assets","attlog.json")
    invdir = os.path.join(str(directory.parent),"Assets","invlog.json")
    print("attempting json loading...")
    print("loading from "+masterdir+", "+attdir+", "+invdir)
    try:
        with open(masterdir, "r") as f:
            master = f.read()
            master, index = jsondecoder.raw_decode(master)
        with open(attdir, "r") as f:
            attlog = f.read()
            attlog, index = jsondecoder.raw_decode(attlog)
        with open(invdir, "r") as f:
            invlog = f.read()
            invlog, index = jsondecoder.raw_decode(invlog)
    except Exception as e:
        print("ERROR:",e)
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
    global master
    jsondecoder = json.JSONDecoder()
    master = ""
    attlog = ""
    invlog = ""
    masterdir = os.path.join(str(directory.parent),"Assets","master.json")
    attdir = os.path.join(str(directory.parent),"Assets","attlog.json")
    invdir = os.path.join(str(directory.parent),"Assets","invlog.json")
    print("attempting json loading...")
    print("loading from "+masterdir+", "+attdir+", "+invdir)
    try:
        with open(masterdir, "r") as f:
            master = f.read()
            master, index = jsondecoder.raw_decode(master)
        with open(attdir, "r") as f:
            attlog = f.read()
            attlog, index = jsondecoder.raw_decode(attlog)
        with open(invdir, "r") as f:
            invlog = f.read()
            invlog, index = jsondecoder.raw_decode(invlog)
    except Exception as e:
        print("ERROR:",e)
    finally:
        print("success")

def savejson():
    global master
    global attlog
    global invlog
    timestamp  = time.time()
    master["datemodified"] = attlog["datemodified"] = invlog["datemodified"] = timestamp
    master["usrmaster"]["count"] = len(master["usrmaster"]["members"])
    master["invmaster"]["count"] = len(master["invmaster"]["members"])

    masterdir = os.path.join(str(directory.parent),"Assets","master.json")
    attdir = os.path.join(str(directory.parent),"Assets","attlog.json")
    invdir = os.path.join(str(directory.parent),"Assets","invlog.json")
    print("attempting json saving...")
    print("saving to "+masterdir+", "+attdir+", "+invdir)
    try:
        with open(masterdir, "w") as f:
            json.dump(master, f, indent=4)
        with open(attdir, "w") as f:
            json.dump(attlog, f, indent=4)
        with open(invdir, "w") as f:
            json.dump(invlog, f, indent=4)
    except Exception as e:
        print("ERROR:",e)
    finally:
        print("save success")

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
    '''
    makes a scrollable frame for use in the GUI. Returns the outer frame, inner frame, and canvas.
    (outer, inner, canvas)
    '''
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

def jsoncheckinout(event, group, inout, id, owner="N/A"):
    '''
    global function for handling json editing for check ins and outs.
    event: triggering event for entrybinds.
    group: "inv" or "att".
    inout: "in" or "out". Checks in and out.
    id: pass the product/user id.
    owner: for inventory, pass if checking out.

    returns: True, (False, error)
    '''
    global master
    global attlog
    global invlog
    if group == "att":
        pass
    elif group == "inv":
        if inout == "in":
            #checking items in
            if id in master["invmaster"]["members"]:
                print("id found")
                if master["invmaster"]["members"][id]["checkout"]["status"] == "in":
                    e = "ERROR: item already checked in"
                    invcheckinstatus.config(text="Status: "+e, fg="red")
                    invcheckinentry.delete(0, END)
                    return False, e
                else:
                    master["invmaster"]["members"][id]["checkout"]["status"] = "in"
                    invlog["members"][id]["current"] = "in"
                    invlog["members"][id][str(datetime.now().timestamp())] = {
                        "status":"in",
                        "lastexpected": master["invmaster"]["members"][id]["checkout"]["lastexpected"],
                        "notes": master["invmaster"]["members"][id]["checkout"]["notes"]
                    }
                    
                    invcheckinstatus.config(text="Status: "+master["invmaster"]["members"][id]["name"]+" Checked In Successfully", fg="green")
                    invcheckinentry.delete(0, END)
                    invlistboxupdate()
                    return True

            else:
                e = "ERROR: id not found"
                invcheckinstatus.config(text="Status: "+e, fg="red")
                invcheckinentry.delete(0, END)
                return False, e
            
        elif inout == "out":
            #checking items out
            if owner != "N/A" and owner != "":
                if id in master["invmaster"]["members"]:
                    print("id found")
                    if master["invmaster"]["members"][id]["checkout"]["status"] == "out":
                        e = "ERROR: item already checked out"
                        invcheckoutstatus.config(text="Status: "+e, fg="red")
                        invcheckoutentry.delete(0, END)
                        return False, e
                    else:
                        if invcheckoutdueby.get() != "":
                            master["invmaster"]["members"][id]["checkout"]["status"] = "out"
                            dt = invcheckoutdueby.get_date()
                            dt = dt.isoformat()
                            dt = datetime.fromisoformat(dt)
                            dt = datetime.combine(dt, time())
                            dt = dt.timestamp()
                            master["invmaster"]["members"][id]["checkout"]["lastcheckout"] = {owner: datetime.now().timestamp()}
                            master["invmaster"]["members"][id]["checkout"]["lastexpected"] = str(dt)


                            invlog["members"][id]["current"] = "out"
                            invlog["members"][id][str(datetime.now().timestamp())] = {
                                "status":"out",
                                "lastexpected": master["invmaster"]["members"][id]["checkout"]["lastexpected"],
                                "owner": owner,
                                "notes": master["invmaster"]["members"][id]["checkout"]["notes"]
                            }
                            invcheckoutentry.delete(0, END)
                            invcheckoutownerentry.delete(0, END)
                            invcheckoutstatus.config(text="Status: Checked Out Successfully", fg="green")
                            invlistboxupdate()
                            return True
                        else:
                            e = "ERROR: due date not set"
                            invcheckoutstatus.config(text="Status: "+e, fg="red")
                            invcheckoutentry.delete(0, END)
                            return False, e
                else:
                    e = "ERROR: id not found"
                    invcheckoutstatus.config(text="Status: "+e, fg="red")
                    invcheckoutentry.delete(0, END)
                    return False, e
            else:
                e = "ERROR: owner not set"
                invcheckoutstatus.config(text="Status: "+e, fg="red")
                invcheckoutentry.delete(0, END)
                return False, e
        invlistboxupdate()
        


            


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

    #CUSTOM TITLE BAR BELOW
    if True:
        def startmove(event):
            root.x = event.x
            root.y = event.y

        def movewindow(event):
            x = event.x_root - root.x
            y = event.y_root - root.y
            root.geometry(f"+{x}+{y}")

        def minimizewindow():
            root.overrideredirect(False)
            root.iconify()

        def restorewindow():
            root.overrideredirect(True)
            root.deiconify()

        titlebar = Frame(root, bg="#B7B5B5", relief="raised", bd=0)

        titlebar.bind("<Button-1>", startmove)
        titlebar.bind("<B1-Motion>", movewindow)
        titlelabel = Label(titlebar, text="ScoutDB", bg="#B7B5B5", fg="white")
        titlelabel.pack(side="left", padx=10)
        closebutton = Button(titlebar, text="X", command=root.destroy, bg="#B7B5B5", fg="white", relief="flat")
        closebutton.pack(side="right", padx=5)

        minimizebutton = Button(titlebar, text="_", command=minimizewindow, bg="#B7B5B5", fg="white", relief="flat")
        minimizebutton.pack(side="right")
        titlebar.grid(row=0, column=0, columnspan=12, sticky=NSEW)

        root.bind("<Map>", lambda event: root.overrideredirect(True) if root.state() == "normal" else None)

        



    invbutton = Button(root, text="Inventory", command=lambda:windowtoggle(True, "inv"))
    attbutton = Button(root, text="Attendance", command=lambda:windowtoggle(True, "att"))
    manbutton = Button(root, text="Management", command=lambda:windowtoggle(True, "man"))
    welcomelabel = Label(root, text="ScoutDB", font=("Helvetica", 20, "bold", "italic"))
    syncbutton = Button(root, text="Sync...")
    secbutton = Button(root, text="Security")
    savebutton = Button(root, text="Save", command=savejson)

    invbutton.grid(row=4, column=1,sticky=NSEW, columnspan=3)
    attbutton.grid(row=4, column=4, sticky=NSEW, columnspan=3)
    manbutton.grid(row=4, column=7, sticky=NSEW, columnspan=3)
    welcomelabel.grid(row=1,column=0)
    syncbutton.grid(row=1, column=11, sticky=NSEW)
    secbutton.grid(row=1, column=10, sticky=NSEW)
    savebutton.grid(row=1, column=9, sticky=NSEW)

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
        invcheckinintro = Label(invcheckincontent, text="In the \"Check In\" page, you can check in gear by either using a barcode scanner or by manually entering the id in the entry below and pressing enter. Note that your barcode scanner must be configured to press enter after each scan to work.", font=("Helvetica", 12), wraplength=430, justify="left" )
        invcheckinlabel1 = Label(invcheckincontent, text="Enter item ID:")
        invcheckinentry = Entry(invcheckincontent)
        invcheckinstatus = Label(invcheckincontent, text="Status: N/A", font=("Helvetica", 12, "bold"))


        invcheckintitle.grid(row=0, column=0, sticky=NW)
        invcheckinintro.grid(row=1, column=0, sticky=NW)
        invcheckinlabel1.grid(row=2, column=0, sticky=NW)
        invcheckinentry.grid(row=3, column=0, sticky=NW)
        invcheckinstatus.grid(row=4, column=0, sticky=NW)
        invcheckinentry.bind("<Return>", lambda event: jsoncheckinout(event, "inv", "in", invcheckinentry.get()))



    #CHECK OUT FRAME ELEMENTS BELOW
    if True:
        invcheckouttitle = Label(invcheckoutcontent, text="Check Out", font=("Helvetica", 14, "bold", "italic"))
        invcheckoutintro = Label(invcheckoutcontent, text="In the \"Check Out\" page, you can check out gear by either using a barcode scanner or by manually entering the id in the entry below and pressing enter. Note that your barcode scanner must be configured to press enter after each scan to work, and that you need to set a due date for the item.", font=("Helvetica", 12), wraplength=430, justify="left" )
        invcheckoutlabel1 = Label(invcheckoutcontent, text="Enter item ID:")
        invcheckoutentry = Entry(invcheckoutcontent)
        invcheckoutstatus = Label(invcheckoutcontent, text="Status: N/A", font=("Helvetica", 12, "bold"))
        invcheckoutdueby = DateEntry(
            invcheckoutcontent,
            width=18,
            background="darkblue", 
            foreground="white",
            borderwidth=2,
            date_pattern="yyyy-mm-dd"
        )
        invcheckoutlabel2 = Label(invcheckoutcontent, text="Due By:")
        invcheckoutownerlabel = Label(invcheckoutcontent, text="Owner ID:")
        invcheckoutownerentry = Entry(invcheckoutcontent)

        invcheckouttitle.grid(row=0, column=0, sticky=NW)
        invcheckoutintro.grid(row=1, column=0, sticky=NW)
        invcheckoutlabel1.grid(row=2, column=0, sticky=NW)
        invcheckoutentry.grid(row=3, column=0, sticky=NW)
        invcheckoutownerlabel.grid(row=4, column=0, sticky=NW)
        invcheckoutownerentry.grid(row=5, column=0, sticky=NW)
        invcheckoutlabel2.grid(row=6, column=0, sticky=NW)
        invcheckoutdueby.grid(row=7, column=0, sticky=NW)
        invcheckoutstatus.grid(row=8, column=0, sticky=NW)
        invcheckoutownerentry.bind("<Return>", lambda event: jsoncheckinout(event, "inv", "out", invcheckoutentry.get(), invcheckoutownerentry.get()))
        invcheckoutentry.bind("<Return>", lambda event: invcheckoutownerentry.focus_set())


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
        global master
        compsel = invlistbox.curselection() #[index num]
        select = invlistbox.get(compsel[0]) #"987654:THING"
        select = select.split(":")[0]
        if select in master["invmaster"]["members"]:
            tagflag = False
            view = master["invmaster"]["members"][select]
            checkoutview = master["invmaster"]["members"][select]["checkout"]

            invdetailsname.config(text="Name: " + view["name"])
            for tag in view["tags"]:
                if tagflag == False:
                    tagbuild = "Tags: "+tag
                    tagflag = True
                else:
                    tagbuild += ", "+tag
            invdetailstag.config(text=tagbuild)
                
            if view["tracked"] == 1:
                invdetailstracked.config(text="Tracked: Yes")
            else:
                invdetailstracked.config(text="Tracked: No")
            invdetailsstatus.config(text="Status: "+checkoutview["status"])
            builduser = next(iter(checkoutview["lastcheckout"])) #"123456"
            buildmember = master["usrmaster"]["members"][builduser]["firstname"]+" "+master["usrmaster"]["members"][builduser]["lastname"] 
            buildtime = datetime.fromtimestamp(checkoutview["lastcheckout"][builduser]).isoformat()
            buildtime = buildtime.split(".")[0]
            buildtime = buildtime.replace("T",", ")
            invdetailslastcheckout.config(text="Last Checkout: "+buildtime+", to "+buildmember)
            invdetailsnotes.config(text="Notes: "+checkoutview["notes"])
            invtab.select(invdetailsframe)

        else:
            print("ERROR: inv member not found",select)

    def invlistboxupdate():
        global master, init

        if init == False:  
            refreshjson()
            init = True

        invlistbox.delete(0, END)
        confignum = 0

        for item in master["invmaster"]["members"]:
            if master["invmaster"]["members"][item]["tracked"] == 1:
                invlistbox.insert(END, str(item)+":"+master["invmaster"]["members"][item]["name"])
                if master["invmaster"]["members"][item]["checkout"]["status"] == "in":
                    invlistbox.itemconfig(confignum, bg="green")
                elif master["invmaster"]["members"][item]["checkout"]["status"] == "out":
                    invlistbox.itemconfig(confignum, bg="red")
            else:
                invlistbox.insert(END, str(item)+": "+item["name"])
                invlistbox.itemconfig(confignum, bg="gray")
            confignum += 1
        """
        for item in master["invmaster"]["members"].values():
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

    attinitializeframe, attinitializecontent, attinitializecanvas = makescrollable(atttab)
    attcheckinframe, attcheckincontent, attcheckincanvas = makescrollable(atttab)
    attcheckoutframe, attcheckoutcontent, attcheckoutcanvas = makescrollable(atttab)
    attissuesframe, attissuescontent, attissuescanvas = makescrollable(atttab)
    attdetailsframe, attdetailscontent, attdetailscanvas = makescrollable(atttab)

    atttab.add(attinitializeframe, text="Initialize")
    attlistbox = Listbox(attwindow)

    #DATE EXISTS WINDOW BELOW
    if True:
        attdateexistwindow = Toplevel(attwindow)
        attdateexistwindow.title("Date Exists")
        attdateexistwindow.geometry("400x200")
        attdateexistwindow.withdraw()

        def dateexistoverwrite():
            global datecontinueflag
            datecontinueflag = "over"
            attdateexistwindow.withdraw()
            attinit()
        def dateexistcontinue():
            global datecontinueflag
            datecontinueflag = "cont"
            attdateexistwindow.withdraw()
            attinit()
        def dateexistcancel():
            global datecontinueflag
            datecontinueflag = "none"
            attdateexistwindow.withdraw()

        attdateexistlabel1 = Label(attdateexistwindow, text="The date you selected already exists in the attendance log. Do you want to overwrite or continue it?",font=("Helvetica", 12), wraplength=320, justify="center")
        attdateexistoverwritebutton = Button(attdateexistwindow, text="Overwrite", command=dateexistoverwrite)
        attdateexistcontinuebutton = Button(attdateexistwindow, text="Continue", command=dateexistcontinue)
        attdateexistcancelbutton = Button(attdateexistwindow, text="Cancel", command=dateexistcancel)

        #GRIDS
        if True:
            attdateexistwindow.rowconfigure(0, weight=1)
            attdateexistwindow.rowconfigure(1, weight=1)
            attdateexistwindow.columnconfigure(0, weight=1)
            attdateexistwindow.columnconfigure(1, weight=1)
            attdateexistwindow.columnconfigure(2, weight=1)

            attdateexistlabel1.grid(row=0, column=0, sticky=NSEW, columnspan=3)
            attdateexistcontinuebutton.grid(row=1, column=0, sticky=NSEW)
            attdateexistoverwritebutton.grid(row=1, column=1, sticky=NSEW)
            attdateexistcancelbutton.grid(row=1, column=2, sticky=NSEW)

        #note: datecontinueflag has 3 properties: None:overwrite, True:continue, False:cancel
        
    '''
    save these for later
    atttab.add(attcheckinframe, text="Check In")
    atttab.add(attcheckoutframe, text='Check Out')
    atttab.add(attissuesframe, text='Issues')
    atttab.add(attdetailsframe, text='Details')
    '''

    #INITIALIZE FRAME ELEMENTS BELOW
    if True:

        def initsuccess():
            atttab.add(attcheckinframe, text="Check In")
            atttab.add(attcheckoutframe, text='Check Out')
            atttab.add(attissuesframe, text='Issues')
            atttab.add(attdetailsframe, text='Details')

        def attlistboxupdate(epoch):
            global attlog, master
            #epoch = '1789023600', example
            if epoch in attlog["dates"]:
                #okay here we go aghhhhh
                confignum = 0
                attlistbox.delete(0, END)
                #ASSSEMBLEEE THE LISSSSTTT!!!!
                for tag in master["usrmaster"]["tags"]:
                    tagcompile = []
                    attlistbox.insert(END, tag)
                    attlistbox.itemconfig(confignum, bg="blue")
                    confignum += 1
                    for member in master["usrmaster"]["members"]:
                        if tag in master["usrmaster"]["members"][member]["tags"]:
                            tagcompile.append(master["usrmaster"]["members"][member]["lastname"]+", "+master["usrmaster"]["members"][member]["firstname"]+" ("+member+")")       
                    tagcompile.sort()
                    #now we have a sorted list, enter them in one by one while checking status
                    for item in tagcompile:
                        attlistbox.insert(END, item)
                        #check status
                        id = item.split("(")[1].split(")")[0]
                        if id in attlog["dates"][epoch]:
                            if attlog["dates"][epoch][id]["status"] == "in":
                                attlistbox.itemconfig(confignum, bg="green")
                            elif attlog["dates"][epoch][id]["status"] == "out":
                                attlistbox.itemconfig(confignum, bg="red")
                            else:
                                print("no status match in attlog[\"dates\"]["+epoch+"]["+id+"][\"status\"]!")
                                attlistbox.itemconfig(confignum, bg="purple")
                        else:
                            #person is out and hasn't checked out yet
                            attlistbox.itemconfig(confignum, bg="grey")
                        confignum += 1
            else:
                print("no match in attlistboxupdate()!")
            print("attlistboxupdate success")
        def attinit():
            global attlog, datecontinueflag
            epochdate = attinitializedate.get_date()
            #stupid datetime.date object doesn't have .timestamp(), so we have to convert it to a datetime.datetime object first
            epochdate = str(round(datetime.datetime.combine(epochdate, datetime.datetime.min.time()).timestamp()))
            print(epochdate, type(epochdate))
            #after listbox updating we need to sweep attlog for any custom entries and throw that object to the user.
            #if str(epochdate) in attlog:
            try:
                if epochdate in attlog["dates"] and datecontinueflag == "none":
                    #user hasn't acknowledged match
                    attdateexistwindow.deiconify()
                elif datecontinueflag != "none":
                    #user is aware of match and has responded
                    if datecontinueflag == "over":
                        #create new entry
                        attlog["dates"][epochdate] = {}
                        attlistboxupdate(epochdate)
                        if not datecontinueflag == "none":
                            #its an overwrite, revert to none after operation
                            datecontinueflag = "none"
                    elif datecontinueflag == "cont":
                        #continue original entry
                        attlistboxupdate(epochdate)
                    datecontinueflag = "none"
                    initsuccess()
                else:
                    #create new entry
                    attlog["dates"][epochdate] = {}
                    initsuccess()      
            except Exception as e:
                print("Error: "+e)
            
            
#########################################################################CONTINUE HERE

        attinitializetitle = Label(attinitializecontent, text="Initialize Attendance", font=("Helvetica", 14, "bold", "italic"))
        attinitializeintro = Label(attinitializecontent, text="In the \"Initialize\" page, you can initialize attendance for a specific date. This will create a new entry in the attendance log for that date, and will allow you to check in members for that date.", font=("Helvetica", 12), wraplength=430, justify="left" )
        attinitializelabel1 = Label(attinitializecontent, text="Enter date:")
        attinitializedate = DateEntry(
            attinitializecontent,
            width=18,
            background="darkblue", 
            foreground="white",
            borderwidth=2,
            date_pattern="yyyy-mm-dd"
        )
        attinitializebutton = Button(attinitializecontent, text="Initialize", command=attinit)

        attinitializetitle.grid(row=0,column=0, sticky=NW)
        attinitializeintro.grid(row=1,column=0, sticky=NW)
        attinitializelabel1.grid(row=2,column=0, sticky=NW)
        attinitializedate.grid(row=3,column=0, sticky=NW)
        attinitializebutton.grid(row=4,column=0, sticky=NW)
    #CHECK IN FRAME ELEMENTS BELOW
    if True:
        attcheckintitle = Label(attcheckincontent, text="Check In", font=("Helvetica", 14, "bold", "italic"))
        attcheckinintro = Label(attcheckincontent, text="In the \"Check In\" page, you can also check in members by either using a barcode scanner or by manually entering the id in the entry below and pressing enter. Make sure to select a date to initialize the check-in.", font=("Helvetica", 12), wraplength=430, justify="left" )
        attcheckinlabel1 = Label(attcheckincontent, text="Enter date:")
        attcheckindate = DateEntry(
            attcheckincontent,
            width=18,
            background="darkblue", 
            foreground="white",
            borderwidth=2,
            date_pattern="yyyy-mm-dd"
        )        
    #CHECK OUT FRAME ELEMENTS BELOW
    if True:
        pass

    #ISSUES FRAME ELEMENTS BELOW
    if True:
        pass
        
    #DETAILS FRAME ELEMENTS BELOW
    if True:
        pass

    attlabel.grid(row=0,column=0)
    attbackbutton.grid(row=0,column=11, sticky=NSEW)
    atttab.grid(row=1, column=1, sticky=NSEW, rowspan=7, columnspan=10)
    attlistbox.grid(row=1, column=0)

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

def exitcatcher():
    savejson()
    print("goodbye world...")
atexit.register(exitcatcher)

root.mainloop()
