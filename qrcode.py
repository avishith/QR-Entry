import os
try:
    import cv2
except ModuleNotFoundError:
    os.system('pip install opencv-python')
try:
    import numpy as np
except ModuleNotFoundError:
    os.system('pip install numpy')
try:
    from pyzbar.pyzbar import decode
except ModuleNotFoundError:
    os.system('pip install pyzbar')

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    succes,img=cap.read()
    code=decode(img)
    for qr in code:
        val=qr.data.decode('utf-8')
        points=np.array([qr.polygon],np.int32)
        cv2.polylines(img,[points],True,(0,255,0),3)
        rec=qr.rect
        cv2.putText(img,val,(rec[0],rec[1]),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),1)
        print(val)
    cv2.imshow('QR-Enrty',img)
    cv2.waitKey(2)

#img=cv2.imread('code1.png')

