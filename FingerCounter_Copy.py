import cv2
import time
import HandTrackingModule as htm
import serial


cap = cv2.VideoCapture(0)

detector = htm.handTracker(detectionCon=0.75)

#ser = serial.Serial('COM4', 115200)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.handsFinder(img, draw=False)
    lmList = detector.positionFinder(img, draw=False)

    if len(lmList) != 0:
        fingers = []
        if lmList[4][1] < lmList[20][1]:
            cv2.putText(img, "LEFT", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(img, "RIGHT", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                #start, end = (lmList[tipIds[id]][1]-20, lmList[tipIds[id]][2]-20), (lmList[tipIds[id]-3][1]+20, lmList[tipIds[id]-3][2]+20)
                #cv2.rectangle(img, start, end, (255, 0, 0), 2)
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = fingers.count(1)
        if(totalFingers == 0):
            cv2.putText(img, "0", (240,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
        elif(totalFingers == 1):
            cv2.putText(img, "1", (240,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
        elif(totalFingers == 2):
            cv2.putText(img, "2", (240,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
        elif(totalFingers == 3):
            cv2.putText(img, "3", (240,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
        elif(totalFingers == 4):
            cv2.putText(img, "4", (240,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
        elif(totalFingers == 5):
            cv2.putText(img, "5", (240,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Video", img)
    cv2.waitKey(1)