import numpy as np
import cv2

goatImage = cv2.imread('goat.jpeg')
cv2.imshow('Imagen',goatImage)

invertedImage = cv2.flip(goatImage,0)
cv2.imshow('Imagen invertida', invertedImage)

cv2.waitKey(0)

# close the windows
cv2.destroyAllWindows()