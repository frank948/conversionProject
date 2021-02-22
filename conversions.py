from tkinter import *
from tkinter import ttk

def lbtokg(*args):
    try:
        value = float(lb.get())
        kg.set(int(value / 2.205))
    except ValueError:
        pass
def kgtolb(*args):
    try:
        value = float(kg2.get())
        lb2.set(int(value * 2.205))
    except ValueError:
        pass
def mphtokph(*args):
    try:
        value = float(mph.get())
        kph.set(int(value * 1.609))
    except ValueError:
        pass
def kphtomph(*args):
    try:
        value = float(kph2.get())
        mph2.set(int(value / 1.609))
    except ValueError:
        pass
def celctofahr(*args):
    try:
        value = float(celc.get())
        fahr.set(int((value * (9/5)) + 32))
    except ValueError:
        pass
def fahrtocelc(*args):
    try:
        value = float(fahr2.get())
        celc2.set(int(value - 32) * (5/9))
    except ValueError:
        pass

window = Tk()
window.title("Conversions")

mainframe = ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

lb = StringVar()
lb_entry = ttk.Entry(mainframe, width=7, textvariable=lb)
lb_entry.grid(column=2, row=1, sticky=(W, E))
kg = StringVar()
ttk.Label(mainframe, textvariable=kg).grid(column=2,row=2,sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=lbtokg).grid(column=3, row=3, sticky=(W))
ttk.Label(mainframe, text="lb\'s").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="kg\'s").grid(column=3, row=2, sticky=W)

kg2 = StringVar()
kg2_entry = ttk.Entry(mainframe, width=7, textvariable=kg2)
kg2_entry.grid(column=2, row=4, sticky=(W, E))
lb2 = StringVar()
ttk.Label(mainframe, textvariable=lb2).grid(column=2, row=5, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=kgtolb).grid(column=3, row=6, sticky=(W))
ttk.Label(mainframe, text="kg\'s").grid(column=3, row=4, sticky= W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="lb\'s").grid(column=3, row=5, sticky=W)

mph = StringVar()
mph_entry = ttk.Entry(mainframe, width=7, textvariable=mph)
mph_entry.grid(column=2,row=7, sticky=(W, E))
kph = StringVar()
ttk.Label(mainframe, textvariable=kph).grid(column=2, row=8, sticky=(E, W))
ttk.Button(mainframe, text="Calculate", command=mphtokph).grid(column=3, row=9, sticky=W)
ttk.Label(mainframe, text="mph\'s").grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=8, sticky=E)
ttk.Label(mainframe, text="kph\'s").grid(column=3, row=8, sticky=W)

kph2 = StringVar()
kph2_entry = ttk.Entry(mainframe, width=7, textvariable=kph2)
kph2_entry.grid(column=2, row=10, sticky=(W, E))
mph2 = StringVar()
ttk.Label(mainframe, textvariable=mph2).grid(column=2, row=11, sticky=(E, W))
ttk.Button(mainframe, text="Calculate", command=kphtomph).grid(column=3, row=12,sticky=W)
ttk.Label(mainframe, text="kph\'s").grid(column=3, row=10, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=11, sticky=E)
ttk.Label(mainframe, text="mph\'s").grid(column=3,row=11,sticky=W)

celc = StringVar()
celc_entry = ttk.Entry(mainframe, width=7, textvariable=celc)
celc_entry.grid(column=2, row=13, stick=(W, E))
fahr = StringVar()
ttk.Label(mainframe, textvariable=fahr).grid(column=2, row=14, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=celctofahr).grid(column=3, row=14, sticky=W)
ttk.Label(mainframe, text="Celcius").grid(column=3, row=13, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=14,sticky=E)
ttk.Label(mainframe, text="fahrenheit").grid(column=3, row=15,sticky=W)

fahr2 = StringVar()
fahr2_entry = ttk.Entry(mainframe, width=7, textvariable=fahr2)
fahr2_entry.grid(column=2, row=16, sticky=(W, E))
celc2 = StringVar()
ttk.Label(mainframe, textvariable=celc2).grid(column=2, row=17, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=fahrtocelc).grid(column=3, row=18, sticky=W)
ttk.Label(mainframe, text="fahrenheit").grid(column=3, row=16, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=17, sticky=E)
ttk.Label(mainframe, text="Celsius").grid(column=3,row=17, sticky=W)


window.mainloop()