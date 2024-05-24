import cv2
import numpy as np

# 画像を読み込む
image = cv2.imread("correct.vsi")

# グレースケールに変換する
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ノイズを減らすためにぼかす
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# HoughCircles関数を使用して円を検出する
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=20,
    param1=50,
    param2=30,
    minRadius=20,
    maxRadius=25
)

# 検出された円の数を数える
if circles is not None:
    num_circles = len(circles[0])
    print("Number of circles detected:", num_circles)
else:
    print("No circles detected.")
