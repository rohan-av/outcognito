from picamera import PiCamera
import time
import numpy as np
import socket

s = socket.socket()

def initialize(s):
    try:
        host = 'xxx.xx.xx.xxx'
        port = xxxxx
        s.connect((host,port))
        print("Connection Established")
        return True

    except Exception as e:
        print(e)
        return False

def send_alert(state):
    # s = safe, d = danger
    try:
        print("sending")
        s.send(bytes('d','UTF-8'))
        #s.send(bytes('d','UTF-8')) if state else s.send(bytes('s','UTF-8'))
    except Exception as e:
        print(e)
    

init = False

while not init:
    init = initialize(s)

def compare_arr(a,b):
    threshold = 40
    for i in range(64):
        for j in range(64):
            for k in range(3):
                if abs(int(a[i][j][k]) - int(b[i][j][k])) > threshold:
                    print(i,j,k)
                    print("count: ", count, "current: ", a[i][j][k], " previous: ", b[i][j][k])
                    send_alert(True)
                    data = s.recv(1024)
                    print("Received")
                    return True
    return False
                            

camera = PiCamera()
camera.resolution=(64,64)
camera.framerate = 80

default = np.empty((64,64,3), dtype = np.uint8)
output = np.empty((64,64,3), dtype = np.uint8)
count = 0
#for i,j in enumerate(range(100)):
while 1:
    #camera.start_preview()
    time.sleep(0.5)       
    camera.capture(output, 'yuv',use_video_port=True)
    #camera.stop_preview()
    #time.sleep(3)
    
    if not count:
        default = output.copy()
        
    if not compare_arr(output,default):
        default = output.copy()
        count += 1
    else:
        count = 0
        
    
    #camera.capture('/home/pi/Desktop/images/image%s.jpg' % i)   
    #print(i)
s.close()


##arr = []
##
##arr[5] = new
##
##if (new - arr[5] > threshold):
##    changed = True
##    break

