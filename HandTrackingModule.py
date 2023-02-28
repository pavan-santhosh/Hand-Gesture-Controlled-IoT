import cv2
import mediapipe as mp

from google.protobuf.json_format import MessageToDict

class handTracker():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def handsFinder(self,image,draw=True):
        imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image
        
    def positionFinder(self,image, handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            Hand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(Hand.landmark):
                h,w,c = image.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(image,(cx,cy), 15 , (255,0,255), cv2.FILLED)
        return lmlist

    def handsDistinguish(self, image, draw=True):
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)
        handLabel = []
        if self.results.multi_hand_landmarks:
            if len(self.results.multi_handedness) == 2:
                handLabel.append("two")
                cv2.putText(image, 'Both Hands', (250, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
            else:
                for i in self.results.multi_handedness:
                    label = MessageToDict(i)['classification'][0]['label']
                    if label == 'Left':
                        handLabel.append("left")
                        cv2.putText(image, label+' Hand', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                    if label == 'Right':
                        handLabel.append("right")
                        cv2.putText(image, label+' Hand', (460, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
        return handLabel
        
def main():
    cap = cv2.VideoCapture(1)
    tracker = handTracker()
    while True:
        success,image = cap.read()
        image = tracker.handsFinder(image)
        lmList = tracker.positionFinder(image)
        if len(lmList) != 0:
            print(lmList[4])
        cv2.imshow("Video",image)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()