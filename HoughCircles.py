import cv2
import numpy as np


img = cv2.imread("./spheroids293T_Snapshot_20240423_01.vsi")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=15, param1=100, param2=90, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        cv2.circle(img, center, radius, (0, 255, 0), 2)
        cv2.circle(img, center, 2, (0, 0, 255), 3)
else:
    print("No circles detected.")

cv2.imwrite("sample_after.png", img)

circles = np.uint16(np.around(circles))