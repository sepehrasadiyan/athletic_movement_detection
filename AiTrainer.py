import cv2
import numpy as np
import time
import BodyMovementModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        angle = detector.findAngle(img, 23, 25, 27)
        per = np.interp(angle, (86, 181), (0, 100))
        int(per)
        if per == 100 or per == 99 or per == 98 or per == 97 or per == 96 or per == 95 or per == 94 or per == 93 or per == 92:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0 or per == 1 or per == 2 or per == 3 or per == 4 or per == 5 or per == 6 or per == 7 or per == 8 or per == 9:
            if dir == 1:
                count += 0.5
                dir = 0
        cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
