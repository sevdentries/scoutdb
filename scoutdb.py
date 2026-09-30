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
    import math
#GLOBALS BELOW
if True:
    root = Tk()
    root.geometry("960x600")
    root.minsize(800, 500)
    root.title("ScoutDB")
    palette = {
        "background": "#111820",
        "surface": "#19232d",
        "surface_alt": "#202d38",
        "border": "#2e3d49",
        "text": "#e6edf2",
        "muted": "#91a2ae",
        "accent": "#42c6a5",
        "accent_hover": "#32ad90",
        "danger": "#d95c63",
    }
    root.configure(bg=palette["background"])
    root.option_add("*Font", "{Segoe UI} 10")
    root.option_add("*Background", palette["surface"])
    root.option_add("*Foreground", palette["text"])
    root.option_add("*Button.Relief", "flat")
    root.option_add("*Button.BorderWidth", 0)
    root.option_add("*Button.ActiveBackground", palette["border"])
    root.option_add("*Button.ActiveForeground", palette["text"])
    root.option_add("*Entry.Background", palette["surface_alt"])
    root.option_add("*Entry.Foreground", palette["text"])
    root.option_add("*Entry.InsertBackground", palette["text"])
    root.option_add("*Entry.Relief", "flat")
    root.option_add("*Entry.BorderWidth", 1)
    root.option_add("*Entry.HighlightBackground", palette["border"])
    root.option_add("*Entry.HighlightColor", palette["accent"])
    root.option_add("*Listbox.Background", palette["surface_alt"])
    root.option_add("*Listbox.Foreground", palette["text"])
    root.option_add("*Listbox.SelectBackground", palette["accent"])
    root.option_add("*Listbox.SelectForeground", palette["background"])
    root.option_add("*Listbox.Relief", "flat")
    root.option_add("*Listbox.BorderWidth", 1)
    root.option_add("*Listbox.HighlightBackground", palette["border"])
    root.option_add("*Listbox.HighlightColor", palette["accent"])
    root.option_add("*Listbox.Activestyle", "none")
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TNotebook", background=palette["background"], borderwidth=0)
    style.configure("TNotebook.Tab", background=palette["surface_alt"], foreground=palette["muted"], font=("Segoe UI", 10, "bold"), padding=(16, 9), borderwidth=0)
    style.map("TNotebook.Tab", background=[("selected", palette["accent"]), ("active", palette["border"])], foreground=[("selected", palette["background"]), ("active", palette["text"])])
    style.configure("TEntry", fieldbackground=palette["surface_alt"], foreground=palette["text"], bordercolor=palette["border"], padding=7)
    style.map("TEntry", bordercolor=[("focus", palette["accent"])])
    style.configure("TCombobox", fieldbackground=palette["surface_alt"], background=palette["surface_alt"], foreground=palette["text"], arrowcolor=palette["text"], bordercolor=palette["border"], padding=6)
    style.map("TCombobox", fieldbackground=[("readonly", palette["surface_alt"])], foreground=[("readonly", palette["text"])])
    style.configure("TButton", background=palette["surface_alt"], foreground=palette["text"], font=("Segoe UI", 10), padding=(12, 8), borderwidth=0)
    style.map("TButton", background=[("active", palette["border"]), ("pressed", palette["accent"])], foreground=[("pressed", palette["background"])])
    style.configure("TScrollbar", background=palette["surface_alt"], troughcolor=palette["background"], bordercolor=palette["background"], arrowcolor=palette["muted"], relief="flat")
    style.configure("Treeview", background=palette["surface_alt"], fieldbackground=palette["surface_alt"], foreground=palette["text"], rowheight=30, borderwidth=0)
    style.configure("Treeview.Heading", background=palette["surface"], foreground=palette["muted"], padding=8, borderwidth=0)
    style.map("Treeview", background=[("selected", palette["accent"])], foreground=[("selected", palette["background"])])
    root.overrideredirect(True)
    directory = Path(__file__).resolve()
    init = False
    datecontinueflag = "none"
    epochframe = ""

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
    invwindow.configure(bg=palette["background"])

    attwindow = Toplevel(root)
    attwindow.title("Attendance")
    attwindow.geometry("800x500")
    attwindow.configure(bg=palette["background"])

    manwindow = Toplevel(root)
    manwindow.title("Management")
    manwindow.geometry("800x500")
    manwindow.configure(bg=palette["background"])

    secwindow = Toplevel(root)
    secwindow.title("Security")
    secwindow.geometry("500x300")
    secwindow.configure(bg=palette["background"])

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
    global epochframe
    if a == True:
        root.withdraw()
        if str == "att":
            attwindow.deiconify()
            if epochframe == "":
                attlistboxupdate()
            else:
                attlistboxmemberupdate(epochframe)
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
    outer = Frame(parent, bg=palette["background"])
    outer.columnconfigure(0, weight=1)
    outer.rowconfigure(0, weight=1)
    canvas = Canvas(outer, bg=palette["surface"], highlightthickness=0, bd=0)
    scrollbar = ttk.Scrollbar(outer, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.grid(row=0, column=0, sticky=NSEW)
    scrollbar.grid(row=0, column=1, sticky=NS)
    inner = Frame(canvas, bg=palette["surface"])
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
    global attlog, epochframe
    global invlog

    if group == "att":
        if id in master["usrmaster"]["members"]:
            if id in attlog["dates"][epochframe]:
                #if id exists on that day, get the latest timestamp
                greatcompile = []
                for ts in attlog["dates"][epochframe][id]:
                    greatcompile.append(int(ts))
                greatcompile.sort(reverse=True)
                current = str(greatcompile[0])
                current = attlog["dates"][epochframe][id][current]["status"]
            elif not id in attlog["dates"][epochframe] and inout == "in":
                #if id doesn't exist in day but inout is in, we must be checking in new user
                current = "out"
                attlog["dates"][epochframe][id] = {}
            elif not id in attlog["dates"][epochframe] and inout == "out":
                #if id doesn't exist in day but inout is out, we must be checking out new user, which is an error
                print("Error: Member was never checked in today!"+inout)
                attcheckoutstatus.config(text="Status: Error, Member was never checked in today")
                attcheckoutentry.delete(0, END)
                return False, "Error: Member was never checked in today!"+inout

            else:
                print("Error: Unexpected value inout: "+inout)
                attcheckoutentry.delete(0, END)
                return False, "Error: Unexpected value inout: "+inout

            
            if inout == "in":
                #checking person in
                if current == "out":
                    newtime = str(math.floor(time.time()))
                    note = attcheckinnotes.get()
                    attlog["dates"][epochframe][id][newtime] = {
                        "status":"in",
                        "notes":note
                    }
                    humantime = datetime.datetime.fromtimestamp(int(newtime))
                    humantime = humantime.isoformat()
                    humantime = humantime.split(".")[0]
                    humantime = humantime.replace("T",", ")
                    attcheckinstatus.config(text="Status: Checked in successfully at "+humantime+".", fg=palette["accent"])
                    root.after(3000, lambda: attcheckinstatus.config(text="Status: ", fg=palette["text"]))
                    attlistboxmemberupdate(epochframe)
                    attcheckinentry.delete(0, END)
                    return True
                elif current == "in":
                    print("Error: User is already checked in")
                    attcheckinstatus.config(text="Error: User is already checked in",fg=palette["danger"])
                    attcheckinentry.delete(0, END)
                    return False, "Error: User is already checked in"
                else:
                    print("Error: Unexpected value inout: "+inout)
                    attcheckinentry.delete(0, END)
                    return False, "Error: Unexpected value inout: "+inout
            elif inout == "out":
                #signing person out
                if current == "in":
                    if id in attlog["dates"][epochframe]:
                        newtime = str(math.floor(time.time()))
                        note = attcheckoutnotes.get()
                        attlog["dates"][epochframe][id][newtime] = {
                            "status":"out",
                            "notes":note
                        }
                        humantime = datetime.datetime.fromtimestamp(int(newtime))
                        humantime = humantime.isoformat()
                        humantime = humantime.split(".")[0]
                        humantime = humantime.replace("T",", ")
                        attcheckoutstatus.config(text="Status: Signed out successfully at "+humantime+".", fg=palette["accent"])
                        root.after(3000, lambda: attcheckoutstatus.config(text="Status: ", fg=palette["text"]))
                        attlistboxmemberupdate(epochframe)
                        attcheckoutentry.delete(0, END)
                        return True
                    else:
                        print("Error: Member was never checked in today!"+inout)
                        attcheckoutstatus.config(text="Status: Error, Member was never checked in today")
                        attcheckoutentry.delete(0, END)
                        return False, "Error: Unexpected value inout: "+inout
                elif current == "out":
                    print("Error: User is already checked out")
                    attcheckoutstatus.config(text="Status: Error, User is already signed out",fg=palette["danger"])
                    attcheckoutentry.delete(0, END)
                    return False, "Error: User is already checked out"
                else:
                    print("Error: Unexpected value inout: "+inout)
                    attcheckoutentry.delete(0, END)
                    return False, "Error: Unexpected value inout: "+inout
            else:
                print("Error: Unexpected value inout: "+inout)
                attcheckoutentry.delete(0, END)
                return False, "Error: Unexpected value inout: "+inout
            
        else:
            print("Error: member id not found")
            if inout == "out":
                attcheckoutstatus.config(text="Error: member id not found",fg=palette["danger"])
            else:
                attcheckinstatus.config(text="Error: member id not found",fg=palette["danger"])
            return False, "Error: member id not found"
    elif group == "inv":
        if inout == "in":
            #checking items in
            if id in master["invmaster"]["members"]:
                print("id found")
                if master["invmaster"]["members"][id]["checkout"]["status"] == "in":
                    e = "ERROR: item already checked in"
                    invcheckinstatus.config(text="Status: "+e, fg=palette["danger"])
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
                    
                    invcheckinstatus.config(text="Status: "+master["invmaster"]["members"][id]["name"]+" Checked In Successfully", fg=palette["accent"])
                    invcheckinentry.delete(0, END)
                    invlistboxupdate()
                    return True

            else:
                e = "ERROR: id not found"
                invcheckinstatus.config(text="Status: "+e, fg=palette["danger"])
                invcheckinentry.delete(0, END)
                return False, e
            
        elif inout == "out":
            #checking items out
            if owner != "N/A" and owner != "":
                if id in master["invmaster"]["members"]:
                    print("id found")
                    if master["invmaster"]["members"][id]["checkout"]["status"] == "out":
                        e = "ERROR: item already checked out"
                        invcheckoutstatus.config(text="Status: "+e, fg=palette["danger"])
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
                            invcheckoutstatus.config(text="Status: Checked Out Successfully", fg=palette["accent"])
                            invlistboxupdate()
                            return True
                        else:
                            e = "ERROR: due date not set"
                            invcheckoutstatus.config(text="Status: "+e, fg=palette["danger"])
                            invcheckoutentry.delete(0, END)
                            return False, e
                else:
                    e = "ERROR: id not found"
                    invcheckoutstatus.config(text="Status: "+e, fg=palette["danger"])
                    invcheckoutentry.delete(0, END)
                    return False, e
            else:
                e = "ERROR: owner not set"
                invcheckoutstatus.config(text="Status: "+e, fg=palette["danger"])
                invcheckoutentry.delete(0, END)
                return False, e
        else:
            print("Error: Unexpected value inout: "+inout)
            return False, "Error: Unexpected value inout: "+inout
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
    for row in range(9):
        root.rowconfigure(row, weight=0)
    root.rowconfigure(4, weight=1)
    for rcol in range(7):
        secwindow.columnconfigure(rcol, weight=1)
        secwindow.rowconfigure(rcol, weight=1)
        
    
#MAIN WINDOW ELEMENTS BELOW
if True:

    def rounded_shape_points(width, height, radius):
        radius = min(radius, width / 2, height / 2)
        points = []
        for center_x, center_y, start_angle in ((width - radius, radius, -90), (width - radius, height - radius, 0), (radius, height - radius, 90), (radius, radius, 180)):
            for step in range(5):
                angle = math.radians(start_angle + step * 22.5)
                points.extend((center_x + radius * math.cos(angle), center_y + radius * math.sin(angle)))
        return points

    def make_rounded_button(parent, text, command, fill, hover_fill, foreground, width=140, height=40):
        button = Canvas(parent, width=width, height=height, bg=parent.cget("bg"), bd=0, highlightthickness=0, takefocus=True, cursor="hand2")
        shape = button.create_polygon(*rounded_shape_points(width, height, 10), fill=fill, outline="")
        caption = button.create_text(width / 2, height / 2, text=text, fill=foreground, font=("Segoe UI", 9, "bold"))

        def resize(event):
            button.coords(shape, *rounded_shape_points(event.width, event.height, 10))
            button.coords(caption, event.width / 2, event.height / 2)

        button.bind("<Configure>", resize)
        button.bind("<Enter>", lambda event: button.itemconfigure(shape, fill=hover_fill))
        button.bind("<Leave>", lambda event: button.itemconfigure(shape, fill=fill))
        button.bind("<Button-1>", lambda event: command())
        button.bind("<Return>", lambda event: command())
        button.bind("<space>", lambda event: command())
        return button

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

        titlebar = Canvas(root, bg=palette["background"], height=48, bd=0, highlightthickness=0)
        titlebar_shape = titlebar.create_polygon(*rounded_shape_points(960, 48, 14), fill=palette["surface"], outline="")
        titlecontent = Frame(titlebar, bg=palette["surface"], bd=0)
        titlebar_window = titlebar.create_window(10, 4, window=titlecontent, anchor=NW, width=940, height=40)

        def resizetitlebar(event):
            titlebar.coords(titlebar_shape, *rounded_shape_points(event.width, event.height, 14))
            titlebar.itemconfigure(titlebar_window, width=max(event.width - 20, 1), height=max(event.height - 8, 1))

        titlebar.bind("<Configure>", resizetitlebar)
        titlebar.bind("<Button-1>", startmove)
        titlebar.bind("<B1-Motion>", movewindow)
        titlecontent.bind("<Button-1>", startmove)
        titlecontent.bind("<B1-Motion>", movewindow)
        titlelabel = Label(titlecontent, text="ScoutDB", bg=palette["surface"], fg=palette["text"], font=("Segoe UI", 11, "bold"))
        titlelabel.pack(side="left", padx=(18, 10))
        titlelabel.bind("<Button-1>", startmove)
        titlelabel.bind("<B1-Motion>", movewindow)
        closebutton = make_rounded_button(titlecontent, "X", root.destroy, palette["danger"], "#bd4b52", "white", width=34, height=28)
        closebutton.pack(side="right", padx=(6, 12), pady=6)
        minimizebutton = make_rounded_button(titlecontent, "-", minimizewindow, palette["surface_alt"], palette["border"], palette["text"], width=34, height=28)
        minimizebutton.pack(side="right", pady=6)
        titlebar.grid(row=0, column=0, columnspan=12, sticky=NSEW, padx=12, pady=(10, 0))

        root.bind("<Map>", lambda event: root.overrideredirect(True) if root.state() == "normal" else None)

    homeheader = Frame(root, bg=palette["background"])
    homeheader.columnconfigure(0, weight=1)
    welcomelabel = Label(homeheader, text="Workspace", font=("Segoe UI", 24, "bold"), bg=palette["background"], fg=palette["text"])
    workspacedescription = Label(homeheader, text="Scout operations and records", font=("Segoe UI", 10), bg=palette["background"], fg=palette["muted"])
    syncbutton = make_rounded_button(homeheader, "Sync...", lambda: None, palette["surface_alt"], palette["border"], palette["text"], width=96, height=38)
    savebutton = make_rounded_button(homeheader, "Save data", savejson, palette["accent"], palette["accent_hover"], palette["background"], width=100, height=38)
    welcomelabel.grid(row=0, column=0, sticky=SW, padx=(0, 8), pady=(34, 2))
    workspacedescription.grid(row=1, column=0, sticky=NW, padx=(0, 8))
    syncbutton.grid(row=0, column=1, rowspan=2, sticky=E, padx=(6, 6), pady=(34, 0))
    savebutton.grid(row=0, column=2, rowspan=2, sticky=E, padx=(6, 0), pady=(34, 0))
    homeheader.grid(row=1, column=0, columnspan=12, sticky=EW, padx=40)

    homecontent = Frame(root, bg=palette["background"])
    for column in range(3):
        homecontent.columnconfigure(column, weight=1, uniform="homecards")
    homecontent.rowconfigure(0, weight=1)

    inventorycard = Frame(homecontent, bg=palette["surface"], highlightbackground=palette["border"], highlightthickness=1, padx=18, pady=18)
    attendancecard = Frame(homecontent, bg=palette["surface"], highlightbackground=palette["border"], highlightthickness=1, padx=18, pady=18)
    managementcard = Frame(homecontent, bg=palette["surface"], highlightbackground=palette["border"], highlightthickness=1, padx=18, pady=18)
    for card in (inventorycard, attendancecard, managementcard):
        card.grid_propagate(False)
        card.columnconfigure(0, weight=1)

    Label(inventorycard, text="01  /  EQUIPMENT", bg=palette["surface"], fg=palette["accent"], font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky=W)
    Label(inventorycard, text="Track gear, checkouts, and returns.", bg=palette["surface"], fg=palette["muted"], font=("Segoe UI", 10), wraplength=200, justify=LEFT).grid(row=1, column=0, sticky=NW, pady=(12, 20))
    invbutton = make_rounded_button(inventorycard, "Open inventory", lambda:windowtoggle(True, "inv"), palette["surface_alt"], palette["border"], palette["text"])
    invbutton.grid(row=2, column=0, sticky=EW)

    Label(attendancecard, text="02  /  PEOPLE", bg=palette["surface"], fg=palette["accent"], font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky=W)
    Label(attendancecard, text="Manage attendance and member activity.", bg=palette["surface"], fg=palette["muted"], font=("Segoe UI", 10), wraplength=200, justify=LEFT).grid(row=1, column=0, sticky=NW, pady=(12, 20))
    attbutton = make_rounded_button(attendancecard, "Open attendance", lambda:windowtoggle(True, "att"), palette["surface_alt"], palette["border"], palette["text"])
    attbutton.grid(row=2, column=0, sticky=EW)

    Label(managementcard, text="03  /  ADMIN", bg=palette["surface"], fg=palette["accent"], font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky=W)
    Label(managementcard, text="Maintain members, equipment, and records.", bg=palette["surface"], fg=palette["muted"], font=("Segoe UI", 10), wraplength=200, justify=LEFT).grid(row=1, column=0, sticky=NW, pady=(12, 20))
    manbutton = make_rounded_button(managementcard, "Open management", lambda:windowtoggle(True, "man"), palette["surface_alt"], palette["border"], palette["text"])
    manbutton.grid(row=2, column=0, sticky=EW)

    Label(root, text="LOCAL DATABASE  |  READY", bg=palette["background"], fg=palette["muted"], font=("Segoe UI", 8, "bold")).grid(row=7, column=0, columnspan=12, sticky=S, pady=(0, 16))
    inventorycard.grid(row=0, column=0, sticky=NSEW, padx=(0, 6), pady=8, ipady=8)
    attendancecard.grid(row=0, column=1, sticky=NSEW, padx=6, pady=8, ipady=8)
    managementcard.grid(row=0, column=2, sticky=NSEW, padx=(6, 0), pady=8, ipady=8)
    homecontent.grid(row=4, column=0, columnspan=12, sticky=NSEW, padx=40, pady=(18, 24))

#INV WINDOW ELEMENTS BELOW
if True:

    

    invlabel = Label(invwindow, text="Inventory", font=("Segoe UI", 14, "bold"))
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
        invcheckintitle = Label(invcheckincontent, text="Check In", font=("Segoe UI", 14, "bold"))
        invcheckinintro = Label(invcheckincontent, text="In the \"Check In\" page, you can check in gear by either using a barcode scanner or by manually entering the id in the entry below and pressing enter. Note that your barcode scanner must be configured to press enter after each scan to work.", font=("Segoe UI", 10), wraplength=430, justify="left" )
        invcheckinlabel1 = Label(invcheckincontent, text="Enter item ID:")
        invcheckinentry = Entry(invcheckincontent)
        invcheckinstatus = Label(invcheckincontent, text="Status: N/A", font=("Segoe UI", 10, "bold"))


        invcheckintitle.grid(row=0, column=0, sticky=NW)
        invcheckinintro.grid(row=1, column=0, sticky=NW)
        invcheckinlabel1.grid(row=2, column=0, sticky=NW)
        invcheckinentry.grid(row=3, column=0, sticky=NW)
        invcheckinstatus.grid(row=4, column=0, sticky=NW)
        invcheckinentry.bind("<Return>", lambda event: jsoncheckinout(event, "inv", "in", invcheckinentry.get()))



    #CHECK OUT FRAME ELEMENTS BELOW
    if True:
        invcheckouttitle = Label(invcheckoutcontent, text="Check Out", font=("Segoe UI", 14, "bold"))
        invcheckoutintro = Label(invcheckoutcontent, text="In the \"Check Out\" page, you can check out gear by either using a barcode scanner or by manually entering the id in the entry below and pressing enter. Note that your barcode scanner must be configured to press enter after each scan to work, and that you need to set a due date for the item.", font=("Segoe UI", 10), wraplength=430, justify="left" )
        invcheckoutlabel1 = Label(invcheckoutcontent, text="Enter item ID:")
        invcheckoutentry = Entry(invcheckoutcontent)
        invcheckoutstatus = Label(invcheckoutcontent, text="Status: N/A", font=("Segoe UI", 10, "bold"))
        invcheckoutdueby = DateEntry(
            invcheckoutcontent,
            width=18,
            background=palette["surface_alt"],
            foreground=palette["text"],
            borderwidth=0,
            selectbackground=palette["accent"],
            selectforeground=palette["background"],
            headersbackground=palette["surface"],
            headersforeground=palette["muted"],
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
        invissuestitle = Label(invissuescontent, text="Issues", font=("Segoe UI", 14, "bold"))
        invissuestitle.grid(row=0, column=0, sticky=NW)

    #DETAILS FRAME ELEMENTS BELOW
    if True:
        invdetailstitle = Label(invdetailscontent, text="Details", font=("Segoe UI", 14, "bold"))
        invdetailsintro = Label(invdetailscontent, text="Welcome to the details page, here you can examine inventory items in greater detail, as well as viewing timestamps such as checkouts and owners. If you wish to modify items, do so in the \"Management\" section.", font=("Segoe UI", 10), wraplength=450, justify="left")
        invdetailsname = Label(invdetailscontent, text="Name: ", font=("Segoe UI", 10))
        invdetailstag = Label(invdetailscontent, text="Tags: ", font=("Segoe UI", 10))
        invdetailsstatus = Label(invdetailscontent, text="Status: ", font=("Segoe UI", 10))
        invdetailstracked = Label(invdetailscontent, text="Tracked: ", font=("Segoe UI", 10))
        invdetailslastcheckout = Label(invdetailscontent, text="Last Checkout: ", font=("Segoe UI", 10))
        invdetailslastexpected = Label(invdetailscontent, text="Last Expected Return: ", font=("Segoe UI", 10))
        invdetailsnotes = Label(invdetailscontent, text="Notes: ", font=("Segoe UI", 10))

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
            buildtime = datetime.datetime.fromtimestamp(checkoutview["lastcheckout"][builduser]).isoformat()
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
                    invlistbox.itemconfig(confignum, bg="#18372f", fg=palette["text"])
                elif master["invmaster"]["members"][item]["checkout"]["status"] == "out":
                    invlistbox.itemconfig(confignum, bg="#3b252c", fg=palette["text"])
            else:
                invlistbox.insert(END, str(item)+": "+item["name"])
                invlistbox.itemconfig(confignum, bg=palette["surface"], fg=palette["muted"])
            confignum += 1
        """
        for item in master["invmaster"]["members"].values():
            invlistbox.insert(END, item["name"])
            if item["checkout"]["status"] == "in":
                invlistbox.itemconfig(confignum, bg="#18372f", fg=palette["text"])
            elif item["checkout"]["status"] == "out":
                invlistbox.itemconfig(confignum, bg="#3b252c", fg=palette["text"])
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
    atttab.add(attdetailsframe, text='Details')
    attlistbox = Listbox(attwindow)

    #DATE EXISTS WINDOW BELOW
    if True:
        attdateexistwindow = Toplevel(attwindow, bg=palette["background"])
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

        attdateexistlabel1 = Label(attdateexistwindow, text="The date you selected already exists in the attendance log. Do you want to overwrite or continue it?",font=("Segoe UI", 10), wraplength=320, justify="center")
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
        

    #INITIALIZE FRAME ELEMENTS BELOW
    if True:

        def initsuccess():
            atttab.add(attcheckinframe, text="Check In")
            atttab.add(attcheckoutframe, text='Check Out')
            atttab.add(attissuesframe, text='Issues')
            atttab.forget(attinitializeframe)
            atttab.forget(attdetailsframe)
            atttab.add(attdetailsframe, text='Details')
            attbackoutbutton.grid(row=0, column=10,sticky=NSEW)

        def backout():
            global epochframe
            atttab.forget(attcheckinframe)
            atttab.forget(attcheckoutframe)
            atttab.forget(attissuesframe)
            atttab.forget(attdetailsframe)
            atttab.add(attinitializeframe, text="Initialize")
            atttab.add(attdetailsframe, text='Details')
            attbackoutbutton.grid_forget()
            epochframe = ""
            attlistboxupdate()
        attbackoutbutton = Button(attwindow, text="Close date", command=backout)
        def attlistboxupdate():
                #okay here we go aghhhhh
            global master
            confignum = 0
            attlistbox.delete(0, END)
            #ASSSEMBLEEE THE LISSSSTTT!!!!
            for tag in master["usrmaster"]["tags"]:
                tagcompile = []
                attlistbox.insert(END, tag)
                attlistbox.itemconfig(confignum, bg=palette["accent"], fg=palette["background"])
                confignum += 1
                for member in master["usrmaster"]["members"]:
                    if tag in master["usrmaster"]["members"][member]["tags"]:
                        tagcompile.append(master["usrmaster"]["members"][member]["lastname"]+", "+master["usrmaster"]["members"][member]["firstname"]+" ("+member+")")       
                tagcompile.sort()
                #now we have a sorted list, enter them in one by one while checking status
                for item in tagcompile:
                    attlistbox.insert(END, item)
                    attlistbox.itemconfig(confignum, bg="grey")
                    confignum += 1
            print("attlistboxupdate success")
            

        def attlistboxmemberupdate(epoch):
            global attlog, master, epochframe
            #epoch = '1789023600', example
            if epoch in attlog["dates"]:
                #okay here we go aghhhhh
                confignum = 0
                attlistbox.delete(0, END)
                epochframe = epoch
                #ASSSEMBLEEE THE LISSSSTTT!!!!
                for tag in master["usrmaster"]["tags"]:
                    tagcompile = []
                    attlistbox.insert(END, tag)
                    attlistbox.itemconfig(confignum, bg=palette["accent"], fg=palette["background"])
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
                            #new function now needs highest timestamp in day
                            greatcompile = []
                            for timestamp in attlog["dates"][epoch][id]:
                                greatcompile.append(int(timestamp))
                            greatcompile.sort(reverse=True)
                            mostrecentepoch = str(greatcompile[0])
                            print(mostrecentepoch)

                            if attlog["dates"][epoch][id][mostrecentepoch]["status"] == "in":
                                attlistbox.itemconfig(confignum, bg="#18372f", fg=palette["text"])
                            elif attlog["dates"][epoch][id][mostrecentepoch]["status"] == "out":
                                attlistbox.itemconfig(confignum, bg="#3b252c", fg=palette["text"])
                            else:
                                print("no status match in attlog[\"dates\"]["+epoch+"]["+id+"]["+mostrecentepoch+"][\"status\"]!")
                                attlistbox.itemconfig(confignum, bg="purple")
                        else:
                            #person is out and hasn't checked out yet
                            attlistbox.itemconfig(confignum, bg="grey")
                        confignum += 1
            else:
                print("no match in attlistboxmemberupdate()!")
            print("attlistboxmemberupdate finished")
        def attinit():
            global attlog, datecontinueflag, epochframe
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
                        attlistboxmemberupdate(epochdate)
                        if not datecontinueflag == "none":
                            #its an overwrite, revert to none after operation
                            datecontinueflag = "none"
                    elif datecontinueflag == "cont":
                        #continue original entry
                        attlistboxmemberupdate(epochdate)
                    datecontinueflag = "none"
                    attcheckintitle.config(text="Check In - "+datetime.datetime.fromtimestamp(int(epochdate)).isoformat().split("T")[0])
                    attcheckouttitle.config(text="Check Out - "+datetime.datetime.fromtimestamp(int(epochdate)).isoformat().split("T")[0])
                    initsuccess()
                else:
                    #create new entry
                    attlog["dates"][epochdate] = {}
                    epochframe = epochdate
                    initsuccess()      
            except Exception as e:
                print("Error: "+e)
            
            
#########################################################################CONTINUE HERE

        attinitializetitle = Label(attinitializecontent, text="Initialize Attendance", font=("Segoe UI", 14, "bold"))
        attinitializeintro = Label(attinitializecontent, text="In the \"Initialize\" page, you can initialize attendance for a specific date. This will create a new entry in the attendance log for that date, and will allow you to check in members for that date.", font=("Segoe UI", 10), wraplength=430, justify="left" )
        attinitializelabel1 = Label(attinitializecontent, text="Enter date:")
        attinitializedate = DateEntry(
            attinitializecontent,
            width=18,
            background=palette["surface_alt"],
            foreground=palette["text"],
            borderwidth=0,
            selectbackground=palette["accent"],
            selectforeground=palette["background"],
            headersbackground=palette["surface"],
            headersforeground=palette["muted"],
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
        attcheckintitle = Label(attcheckincontent, text="Check In", font=("Segoe UI", 14, "bold"))
        attcheckinintro = Label(attcheckincontent, text="In the \"Check In\" page, you can also check in members by either using a barcode scanner or by manually entering the id in the entry below and pressing enter.", font=("Segoe UI", 10), wraplength=430, justify="left" )
        attcheckinlabel1 = Label(attcheckincontent, text="Enter member ID:")
        attcheckinentry = Entry(attcheckincontent)
        attcheckinlabel2 = Label(attcheckincontent, text="Notes:")
        attcheckinnotes = Entry(attcheckincontent)
        attcheckinstatus = Label(attcheckincontent, text="Status:")

        attcheckintitle.grid(row=0,column=0, sticky=NW)
        attcheckinintro.grid(row=1,column=0, sticky=NW)
        attcheckinlabel1.grid(row=2,column=0, sticky=NW)
        attcheckinentry.grid(row=3,column=0, sticky=NW)
        attcheckinlabel2.grid(row=4,column=0, sticky=NW)
        attcheckinnotes.grid(row=5,column=0, sticky=NW)
        attcheckinstatus.grid(row=6,column=0, sticky=NW)

        attcheckinentry.bind("<Return>", lambda event: jsoncheckinout(event, "att", "in", attcheckinentry.get()))
    #CHECK OUT FRAME ELEMENTS BELOW
    if True:
        attcheckouttitle = Label(attcheckoutcontent, text="Check Out", font=("Segoe UI", 14, "bold"))
        attcheckoutintro = Label(attcheckoutcontent, text="In the \"Check Out\" page, you can sign out members by either using a barcode scanner or by manually entering the id in the entry below and pressing enter.", font=("Segoe UI", 10), wraplength=430, justify="left" )
        attcheckoutlabel1 = Label(attcheckoutcontent, text="Enter member ID:")
        attcheckoutentry = Entry(attcheckoutcontent)
        attcheckoutlabel2 = Label(attcheckoutcontent, text="Notes:")
        attcheckoutnotes = Entry(attcheckoutcontent)
        attcheckoutstatus = Label(attcheckoutcontent, text="Status:")

        attcheckouttitle.grid(row=0,column=0, sticky=NW)
        attcheckoutintro.grid(row=1,column=0, sticky=NW)
        attcheckoutlabel1.grid(row=2,column=0, sticky=NW)
        attcheckoutentry.grid(row=3,column=0, sticky=NW)
        attcheckoutlabel2.grid(row=4,column=0, sticky=NW)
        attcheckoutnotes.grid(row=5,column=0, sticky=NW)
        attcheckoutstatus.grid(row=6,column=0, sticky=NW)

        attcheckoutentry.bind("<Return>", lambda event: jsoncheckinout(event, "att", "out", attcheckoutentry.get()))
    #ISSUES FRAME ELEMENTS BELOW
    if True:
        pass   
    #DETAILS FRAME ELEMENTS BELOW
    if True:
        attdetailstitle = Label(attdetailscontent, text="Details", font=("Segoe UI", 14, "bold"))
        attdetailsintro = Label(attdetailscontent, text="Welcome to the details page, here you can examine attendance records in greater detail, as well as viewing timestamps such as checkins and checkouts. If you wish to modify records, do so in the \"Management\" section.", font=("Segoe UI", 10), wraplength=450, justify="left")
        attdetailsname = Label(attdetailscontent, text="Name: ", font=("Segoe UI", 10))
        attdetailsbirthdate = Label(attdetailscontent, text="DOB: ", font=("Segoe UI", 10))
        attdetailstele = Label(attdetailscontent, text="Telephone/Guardian #: ", font=("Segoe UI", 10))
        attdetailstag = Label(attdetailscontent, text="Tags: ", font=("Segoe UI", 10))
        attdetailsstatus = Label(attdetailscontent, text="Status: ", font=("Segoe UI", 10))
        attdetailstracked = Label(attdetailscontent, text="Tracked: ", font=("Segoe UI", 10))
        attdetailslastcheckin = Label(attdetailscontent, text="Last Check In: ", font=("Segoe UI", 10))
        attdetailslastcheckout = Label(attdetailscontent, text="Last Check Out: ", font=("Segoe UI", 10))
        attdetailsnotes = Label(attdetailscontent, text="Notes: ", font=("Segoe UI", 10))

        def attlistboxviewdetails(event):
            global master, attlog, epochframe
            compsel = attlistbox.curselection()
            select = attlistbox.get(compsel[0])
            try:
                id = select.split("(")[1].split(")")[0]
                if id in master["usrmaster"]["members"]:
                    namecompile = master["usrmaster"]["members"][id]["firstname"]+" "+master["usrmaster"]["members"][id]["lastname"]
                    attdetailsname.config(text="Name: "+namecompile)
                    attdetailsbirthdate.config(text="DOB: "+master["usrmaster"]["members"][id]["birthdate"])
                    attdetailstele.config(text="Telephone/Guardian #: "+master["usrmaster"]["members"][id]["telephone"])
                    tagflag = False
                    for tag in master["usrmaster"]["members"][id]["tags"]:
                        if tagflag == False:
                            tagbuild = "Tags: "+tag
                            tagflag = True
                        else:
                            tagbuild += ", "+tag
                    attdetailstag.config(text=tagbuild)
                    incompile = []
                    outcompile = []
                    for epoch in attlog["dates"]:
                        if id in attlog["dates"][epoch]:
                            greatcompile = []
                            for timestamp in attlog["dates"][epoch][id]:
                                greatcompile.append(int(timestamp))
                            greatcompile.sort(reverse=True)
                            mostrecentepoch = str(greatcompile[0])
                            print(mostrecentepoch)

                            if attlog["dates"][epoch][id][mostrecentepoch]["status"] == "in":
                                attdetailsstatus.config(text="Status: In", fg=palette["accent"])
                            elif attlog["dates"][epoch][id][mostrecentepoch]["status"] == "out":
                                attdetailsstatus.config(text="Status: Out", fg=palette["danger"])
                            else:
                                print("no status match in attlog[\"dates\"]["+epoch+"]["+id+"]["+mostrecentepoch+"][\"status\"]!")
                                attdetailsstatus.config(text="Status: Unknown")

                            for date in attlog["dates"]:
                                if id in attlog["dates"][date]:
                                    for epoch2 in attlog["dates"][date][id]:
                                        if attlog["dates"][date][id][epoch2]["status"] == "in":
                                            incompile.append(epoch2)
                                        else:
                                            outcompile.append(epoch2)

                            outcompile.sort(reverse=True, key=int)
                            incompile.sort(reverse=True, key=int)
                            if len(incompile) == 0:
                                attdetailslastcheckin.config(text="Last Check In: N/A")
                            else:
                                lastin = incompile[0]
                                buildin = datetime.datetime.fromtimestamp(int(lastin)).isoformat()
                                buildin = buildin.split(".")[0]
                                buildin = buildin.replace("T",", ")
                                attdetailslastcheckin.config(text="Last Check In: "+buildin)
                            if len(outcompile) == 0:
                                attdetailslastcheckout.config(text="Last Check Out: N/A")
                            else:
                                lastout = outcompile[0]
                                buildout = datetime.datetime.fromtimestamp(int(lastout)).isoformat()
                                buildout = buildout.split(".")[0]
                                buildout = buildout.replace("T",", ")
                                attdetailslastcheckout.config(text="Last Check Out: "+buildout)
                        else:
                            attdetailsstatus.config(text="Status: Out (no records found)",fg=palette["danger"])
                            attdetailslastcheckin.config(text="Last Check In: N/A")
                            attdetailslastcheckout.config(text="Last Check Out: N/A")
                    atttab.select(attdetailsframe)
                    print("attlistboxviewdetails success")
            except IndexError:
                print("Error: No ID found in selection, did you select the category?")
                return False
                
            
            
            
        attdetailstitle.grid(row=0,column=0, sticky=NW)
        attdetailsintro.grid(row=1,column=0, sticky=NW)
        attdetailsname.grid(row=2,column=0, sticky=NW)
        attdetailsbirthdate.grid(row=3,column=0, sticky=NW)
        attdetailstele.grid(row=4,column=0, sticky=NW)
        attdetailstag.grid(row=5,column=0, sticky=NW)
        attdetailsstatus.grid(row=6,column=0, sticky=NW)
        attdetailstracked.grid(row=7,column=0, sticky=NW)
        attdetailslastcheckin.grid(row=8,column=0, sticky=NW)
        attdetailslastcheckout.grid(row=9,column=0, sticky=NW)
        attdetailsnotes.grid(row=10,column=0, sticky=NW)
        attlistbox.bind("<Double-Button-1>", attlistboxviewdetails)

    

    attlabel.grid(row=0,column=0)
    attbackbutton.grid(row=0,column=11, sticky=NSEW)
    atttab.grid(row=1, column=1, sticky=NSEW, rowspan=7, columnspan=10)
    attlistbox.grid(row=1, column=0, rowspan=8, sticky=NSEW)

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
