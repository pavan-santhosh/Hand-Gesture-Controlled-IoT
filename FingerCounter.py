import cv2
import time
import HandTrackingModule as htm
import serial


cap = cv2.VideoCapture(0)

detector = htm.handTracker(detectionCon=0.75)

ser = serial.Serial('COM4', 115200)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.handsFinder(img)
    lmList = detector.positionFinder(img, draw=False)

    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = fingers.count(1)
        print(totalFingers)
        if(totalFingers == 0):
            ser.write(b'G')
        elif(totalFingers == 1):
            ser.write(b'H')
        elif(totalFingers == 2):
            ser.write(b'I')
        elif(totalFingers == 3):
            ser.write(b'J')
        elif(totalFingers == 4):
            ser.write(b'K')
        elif(totalFingers == 5):
            ser.write(b'L')

    cv2.imshow("Video", img)
    cv2.waitKey(1)