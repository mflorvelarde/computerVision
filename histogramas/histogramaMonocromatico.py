import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

img = cv.imread('goat.jpeg',0)
plt.hist(img.ravel(),256,[0,256])
plt.show()


cap = cv.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    plt.hist(frame.ravel(), 256, [0, 256])
    plt.show()
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
