import cv2
import numpy as np

# 画像のパスを指定
image_path = 'spheroids_Snapshot_20240406_01_rgb.ome'

# 画像を読み込む
image = cv2.imread(image_path, cv2.IMREAD_COLOR)
if image is None:
    print(f"Failed to load image at {image_path}")
    exit()

# 画像をグレースケールに変換
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 画像をぼかす
blurred_image = cv2.medianBlur(gray_image, 5)

# 円の検出
Rmin = 20  # 円の最小半径
Rmax = 100  # 円の最大半径
circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=50, param2=30, minRadius=Rmin, maxRadius=Rmax)

# 検出された円が存在する場合
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # 円の中心と半径を取得
        center = (i[0], i[1])
        radius = i[2]
        # 円の外周を描画
        cv2.circle(image, center, radius, (0, 255, 0), 2)
        # 円の中心を描画
        cv2.circle(image, center, 2, (0, 0, 255), 3)

# 画像を表示する
cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


