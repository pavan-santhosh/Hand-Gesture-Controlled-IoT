import enum
import cv2
import time
import mediapipe as mp

wCam, hCam = 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #since mp accepts only rgb image
    results = hands.process(imgRGB) #process the image after conversion

    #print(results.multi_handedness) #detects hands
    #print(results.multi_hand_landmarks) #prints landmarks
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm) #prints landmarks in decimal values
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h) #converts landmarks from decimal to pixels
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0 , 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)