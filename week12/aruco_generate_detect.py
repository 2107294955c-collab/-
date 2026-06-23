import os

import cv2
import numpy as np


os.makedirs("img", exist_ok=True)

print("Week 12: ArUco ID 6 生成、识别与距离估算")
print("----------------------------------------")

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

marker_id = 6
marker_size = 300

if hasattr(aruco, "generateImageMarker"):
    marker_img = aruco.generateImageMarker(dictionary, marker_id, marker_size)
else:
    marker_img = aruco.drawMarker(dictionary, marker_id, marker_size)

canvas = np.ones((500, 600), dtype=np.uint8) * 255
canvas[100:400, 150:450] = marker_img
color_img = cv2.cvtColor(canvas, cv2.COLOR_GRAY2BGR)

if hasattr(aruco, "ArucoDetector"):
    parameters = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(dictionary, parameters)
    corners, ids, rejected = detector.detectMarkers(canvas)
else:
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(canvas, dictionary, parameters=parameters)

detected_img = color_img.copy()

if ids is not None:
    aruco.drawDetectedMarkers(detected_img, corners, ids)

    for i, detected_id in enumerate(ids.flatten()):
        pts = corners[i][0]
        edge1 = np.linalg.norm(pts[0] - pts[1])
        edge2 = np.linalg.norm(pts[2] - pts[3])
        pixel_width = (edge1 + edge2) / 2

        real_marker_size_m = 0.05
        focal_length_px = 700
        distance_m = real_marker_size_m * focal_length_px / pixel_width

        cv2.putText(
            detected_img,
            f"ID: {detected_id}",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )
        cv2.putText(
            detected_img,
            f"Distance: {distance_m:.2f} m",
            (30, 85),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 128, 0),
            2,
        )

        print(f"识别成功: ArUco ID = {detected_id}")
        print(f"像素宽度: {pixel_width:.2f} px")
        print(f"估算距离: {distance_m:.2f} m")
else:
    print("未识别到 ArUco 标记")

cv2.imwrite("img/aruco_detect.png", detected_img)
cv2.imwrite("img/distance_demo.png", detected_img)

print("----------------------------------------")
print("已生成: img/aruco_detect.png")
print("已生成: img/distance_demo.png")
print("程序结束")
