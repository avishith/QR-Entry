import numpy as np
from pyzbar.pyzbar import decode
import cv2

img=cv2.imread('code.png')
code=decode(img)
for qrCode in code:
    mytext=qrCode.data
    print(mytext)