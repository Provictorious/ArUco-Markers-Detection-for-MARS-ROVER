import cv2 as cv
from cv2 import aruco

marker_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

param_markers = aruco.DetectorParameters()

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_ids, reject = aruco.detectMarkers(gray_frame, marker_dict, parameters=param_markers)
    print(marker_ids)

    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()