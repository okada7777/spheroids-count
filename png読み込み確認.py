import cv2

# 画像ファイルを読み込む
image = cv2.imread('./spheroids293T_Snapshot_20240423_01.vsi')

# 読み込んだ画像がNoneでないことを確認する
if image is not None:
    print("画像が正常に読み込まれました。")
else:
    print("画像の読み込みに失敗しました。")
