import cv2

src1 = cv2.imread('cielo.jpeg')
src2 = cv2.imread('goat.jpeg')

alpha = 0.8
beta = (1.0 - alpha)
resize = cv2.resize(src1,(300,168))
cv2.imshow('goat', src2)
cv2.imshow('cielo', resize)

dst = cv2.addWeighted(resize, alpha, src2, beta, 0.0)


cv2.imshow('Linear blend', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
