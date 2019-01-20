#with reference from https://pythonspot.com/tk-dropdown-example/

#current status: Selection of screenguard
#potential update: Selection of window to close?

from tkinter import *

root = Tk()
root.title("OutCognito")

mainframe = Frame(root)

mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

tkvar = StringVar(root)

choices = {"Minimize","Lower Brightness","Open Resource Site"}
tkvar.set("Minimize") #default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe,text="Select a screenguard:").grid(row = 0, column = 1)
popupMenu.grid(row = 2, column = 1)

choices_id = {"Minimize":1,"Lower Brightness":2,"Open Resource Site":3}
screenguard = [1] #minimize function by default

#on change dropdown value
def change_dropdown(*args):
    print(tkvar.get())
    screenguard[0] = choices_id[tkvar.get()]

def get_guard():
    return screenguard[0]

#link fn to change dropdown
tkvar.trace('w',change_dropdown)

guard = get_guard()

#necessary alert functions will be carried out depending on the value of guard
