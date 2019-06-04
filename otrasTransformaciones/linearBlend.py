import cv2

cielo = cv2.imread('cielo.jpeg')

alpha = 0.8
beta = (1.0 - alpha)
cieloResize = cv2.resize(cielo,(400,300))


cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    frameResize = cv2.resize(frame, (400,300))
    dst = cv2.addWeighted(cieloResize, alpha, frameResize, beta, 0.0)

    cv2.imshow('Linear blend', dst)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
