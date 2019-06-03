import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image

def f(x): print(x)

cap = cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorKNN()
cv2.namedWindow('Mask')
cv2.createTrackbar('Learning rate', 'Mask', 0, 100, f)
cv2.createTrackbar('Shadow rate', 'Mask', 0, 127, f)
cv2.createTrackbar('Algorithm - 0:KNN 1:MOG2 2:CNT', 'Mask', 0, 2, f)
algorithmNumber = 0
algorithmName = 'KNN'

while(True):
    ret, frame = cap.read()
    learningRate = cv2.getTrackbarPos('Learning rate', 'Mask')
    shadow = cv2.getTrackbarPos('Shadow rate', 'Mask')
    algorithm = cv2.getTrackbarPos('Algorithm - 0:KNN 1:MOG2 2:CNT', 'Mask')

    if algorithmNumber != algorithm:
        if algorithm == 0:
            fgbg = cv2.createBackgroundSubtractorKNN()
            fgbg.setShadowValue(shadow)
            algorithmName = 'KNN'
        elif algorithm == 1:
            fgbg = cv2.createBackgroundSubtractorMOG2()
            fgbg.setShadowValue(shadow)
            algorithmName = 'MOG2'
        elif algorithm == 2:
            fgbg = cv2.bgsegm.createBackgroundSubtractorCNT()
            algorithmName = 'CNT'

    fgmask = fgbg.apply(frame, learningRate/100)
    fondo = fgbg.getBackgroundImage()

    cv2.imshow('Background',fondo)
    cv2.imshow('Mask',fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
