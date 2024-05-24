import cv2
import numpy as np

# 画像を読み込む
image = cv2.imread("spheroids293T_Snapshot_20240423_01.vsi")

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

# 検出された円があれば描画する
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        cv2.circle(image, center, radius, (0, 255, 0), 2)

# 結果を表示する
cv2.imshow("Detected Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
num_circles = len(circles[0])
print("Number of circles detected:", num_circles)