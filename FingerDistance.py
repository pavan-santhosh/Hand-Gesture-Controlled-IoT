import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import serial

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handTracker(detectionCon=0.7)


ser = serial.Serial('COM4', 115200)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.handsFinder(img)
    lmList = detector.positionFinder(img, draw=False)
    handList = detector.handsDistinguish(img, draw=False)

    if len(lmList) != 0:
        #print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        #cx, cy = (x1+x2) // 2, (y1+y2) // 2

        #cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        #cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        #cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)

        cv2.putText(img, str(length), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
        if(length<50):
            ser.write(b'Z')
        if(length>50 and length<75):
            ser.write(b'A')
        if(length>75 and length<100):
            ser.write(b'B')
        if(length>100 and length<150):
            ser.write(b'C')
        if(length>150 and length<175):
            ser.write(b'D')
        if(length>175 and length<200):
            ser.write(b'E')
        if(length>200 and length<225):
            ser.write(b'F')


    cv2.imshow("Video", img)
    cv2.waitKey(1)
