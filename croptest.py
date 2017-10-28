import cv2
import numpy as np
import math


cap = cv2.VideoCapture(0)
while(1):
    # read image
    ret, img = cap.read()

    # get hand data from the rectangle sub window on the screen
    cv2.rectangle(img, (300,300), (100,100), (0,255,0),0)
    crop_img = img[100:300, 100:300]
    cv2.imshow("dfdf",crop_img)
    k = cv2.waitKey(10)
    if k == 27:
        break
