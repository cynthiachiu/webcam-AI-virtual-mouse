import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import numpy as np
import time

wCam, hCam = 640, 480
frameR = 100  # Frame reduction
smoothening = 10

INDEX_FINGER_TIP = 8
MIDDLE_FINGER_TIP = 12
INDEX_FINGER = 1
MIDDLE_FINGER = 2

pTime = 0
plocX, plocY = 0,0
clocX, clocY = 0,0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # set width of capture window
cap.set(4, hCam)  # set height of capture window

detector = HandDetector(maxHands=1)
wScr, hScr = pyautogui.size()

while True:
    # Find the hand landmarks
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]  # list of 21 landmark points
        bbox = hand["bbox"]  # bounding box info x, y, w, h

        # Get the tip of the index and middle fingers
        if len(lmList) != 0:
            x1, y1 = lmList[INDEX_FINGER_TIP]
            x2, y2 = lmList[MIDDLE_FINGER_TIP]

        # Check which fingers are up
        fingers = detector.fingersUp(hand)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # If only index finger which means in Mouse Moving Mode
        if fingers[INDEX_FINGER] == 1 and fingers[MIDDLE_FINGER] == 0:
            # Convert coordinates from webcam coords to screen coords for correct position
            scrCoordX = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            scrCoordY = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # Smoothen the values
            clocX = plocX + (scrCoordX - plocX) / smoothening
            clocY = plocY + (scrCoordY - plocY) / smoothening

            # Move the Mouse
            pyautogui.moveTo(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # If both index and middle fingers are up, it is Mouse Clicking Mode
        if fingers[INDEX_FINGER] == 1 and fingers[MIDDLE_FINGER] == 1:
            # Find distance between the fingers
            length, lineInfo, img = detector.findDistance(lmList[INDEX_FINGER_TIP], lmList[MIDDLE_FINGER_TIP], img)

            # Click mouse if distance is short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()

    # Frame Rate
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)

