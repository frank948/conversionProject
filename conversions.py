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

'''
def kphToMph(x):
    mph = round((x / 1.609), 2)
    print(mph, 'mph')
kphToMph(float(input('Enter kph')))

def mphToKph(x):
    kph = round((x * 1.609), 2)
    print(kph, 'kph')
mphToKph(float(input('Enter mph')))

'''

window.mainloop()