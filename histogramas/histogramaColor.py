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
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv.calcHist([frame], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()




