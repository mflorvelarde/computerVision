import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('goat.jpeg',0)
plt.hist(img.ravel(),256,[0,256])
plt.show()


