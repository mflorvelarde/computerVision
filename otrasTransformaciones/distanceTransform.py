import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)


while True:
    ret, frame = video_capture.read()
    # Esto deberia ser con el threshold
    grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    th, im_th = cv2.threshold(grayimg, 220, 255, cv2.THRESH_BINARY_INV);
    dist_img = cv2.distanceTransform(im_th, cv2.DIST_L2, 5).astype(np.uint8)

    cv2.imshow('Distance Transform', dist_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
