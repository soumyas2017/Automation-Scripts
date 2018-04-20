#check config file existence
import os,sys
from pathlib import Path
import numpy as np
import cv2 as cv
import socket
import tempfile
import errno
config_file_location = Path("E:\\Img_reckognition_Config\\config.mlt")
if config_file_location.is_file() :
    print ("File Exists")
else:
    print ("Config File Not existing !!!")
#check write access in the pic directory
path = "C:\\Program Files (x86)"
print ("file mode {}" .format(os.access(path, os.W_OK)))
#check internet connection
try:
    socket.create_connection(("www.google.com", 80))
    print ("True")
except OSError:
    print ("False")
#check camera
def camera_test():
    try:
        cap = cv.VideoCapture(0)
        if cap.isOpened():
            print("Webcam online.")
        cap.release()
        cv.destroyAllWindows()
    except:
        print ("Either you don't have camera or there was some error trying to use camera")
#check mandatory values in config file
with open("E:\\Img_reckognition_Config\\config.mlt","r") as reading_config:
    #data = reading_config.readline()
    #print (data)
    data_dict = dict()
    while(True):
        data = reading_config.readline()
        if data != "":
            key_val = data.split("=")
            if key_val[1] not in ['',None,"",'""']:
                data_dict.update({key_val[0]:key_val[1]})
            else:
                print("{} doesn't have value".format(key_val[0]))
        else:
            print (data_dict)
            camera_test()
            exit()
    