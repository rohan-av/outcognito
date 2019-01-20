import socket
import ctypes
from tkinter import *
import time
import subprocess

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
root.mainloop()
time.sleep(2)
guard = get_guard()


user32 = ctypes.windll.user32
res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
user32.SetProcessDPIAware()

handle = user32.FindWindowW(u'Notepad', None) #identifies window to minimize
#open Notepad to test
#handle = user32.FindWindowW(u'GLFW30', 0) #minecraft
#handle = user32.FindWindowW(u'MozillaWindowClass', 0) #firefox

#print(handle) #for debugging purposes

def send_alert1(): #minimize
    user32.ShowWindow(handle,6)
    result = user32.MessageBoxW(0, "ALERT", "Entry Detected",0)
    handle2 = user32.FindWindowW(u'#32770',0)
    user32.ShowWindow(handle2,5)
    print(result)
    if result == 1:
        user32.ShowWindow(handle,9)

def send_alert2(): #lower brightness
    subprocess.Popen(['powershell.exe','(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,0)'])
    result = user32.MessageBoxW(0, "ALERT", "Entry Detected",0)
    handle2 = user32.FindWindowW(u'#32770',0)
    user32.ShowWindow(handle2,5)
    print(result)
    if result == 1:
        subprocess.Popen(['powershell.exe','(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,100)'])

def send_alert3(): #open random wikipedia article
    new = subprocess.Popen(['C:\Program Files\internet explorer\iexplore.exe','https://en.wikipedia.org/wiki/Special:Random'])
    result = user32.MessageBoxW(0, "ALERT", "Entry Detected",0)
    handle2 = user32.FindWindowW(u'#32770',0)
    user32.ShowWindow(handle2,5)
    print(result)
    if result == 1:
        new.terminate()

while(1):
    try:
        s = socket.socket()
        host = 'xxx.xxx.xxx.xxx' #ip of host
        port = 12345
        s.bind((host, port))

        s.listen(5)
        c, addr = s.accept() #client, address
        print ('Got connection from',addr)


        while True: ## @ck: to change communication
            data = c.recv(1024)
            if data:
                if guard == 1:
                    send_alert1()
                elif guard == 2:
                    send_alert2()
                else:
                    send_alert3()
            guard += 1 #for demo
            guard %= 3 #for demo
            print("closing")
            print("sending")
            c.send(bytes("s","UTF-8"))

    except Exception as e:
        print(e)
