import cv2
import numpy as np
import face_recognition
import os
from _datetime import datetime
# bring new image maualyy is tidy task->create list[] to get our imgaes automatically->genrate encoding automatically for it ->and try to find it in our webcam

path='img'# path to imgaes folder
images=[]# list of images
className=[] # store the names of each student
mylist=os.listdir(path) # it will give names list to mylist from imgeas folder
print(mylist)

for cl in mylist:
    curImg=cv2.imread(f'{path}')
    images.append(curImg)
    className.append(os.path.splitext(cl)[0])# us eto split name into root and xtension
print(className)