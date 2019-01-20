import ctypes
import subprocess

user32 = ctypes.windll.user32

res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
user32.SetProcessDPIAware()

handle = user32.FindWindowW(u'Notepad', None) #Notepad
#handle = user32.FindWindowW(u'GLFW30', 0) #minecraft
#handle = user32.FindWindowW(u'MozillaWindowClass', 0) #firefox

#print(handle) #for debugging purposes

def send_alert(): #minimize
    user32.ShowWindow(handle,6)
    result = user32.MessageBoxW(0, "ALERT", "Entry Detected",0)
    handle2 = user32.FindWindowW(u'#32770',0)
    user32.ShowWindow(handle2,5)
    print(result)
    if result == 1:
        user32.ShowWindow(handle,9)

def send_alert2(): #lower brightness
    subprocess.Popen(['powershell.exe','(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,10)'])
    result = user32.MessageBoxW(0, "ALERT", "Entry Detected",0)
    handle2 = user32.FindWindowW(u'#32770',0)
    user32.ShowWindow(handle2,5)
    print(result)
    if result == 1:
        subprocess.Popen(['powershell.exe','(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,70)'])
    
def send_alert3(): #open random wikipedia article
    new = subprocess.Popen(['C:\Program Files\internet explorer\iexplore.exe','https://en.wikipedia.org/wiki/Special:Random'])
    result = user32.MessageBoxW(0, "ALERT", "Entry Detected",0)
    handle2 = user32.FindWindowW(u'#32770',0)
    user32.ShowWindow(handle2,5)
    print(result)
    if result == 1:
        new.terminate()
