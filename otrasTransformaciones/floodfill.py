import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()


def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        src = param.copy()
        th, im_th = cv2.threshold(src, 220, 255, cv2.THRESH_BINARY_INV);
        im_floodfill = im_th.copy()

        # Mask used to flood filling.
        # Notice the size needs to be 2 pixels than the image.
        h, w = im_th.shape[:2]
        mask = np.zeros((h + 2, w + 2), np.uint8)

        # Floodfill from point (0, 0)
        cv2.floodFill(im_floodfill, mask, (0, 0), 255);

        # Invert floodfilled image
        im_floodfill_inv = cv2.bitwise_not(im_floodfill)

        # Display images.
        cv2.imshow("Thresholded Image", im_th)
        cv2.imshow("Floodfilled Image", im_floodfill)
        cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
        cv2.waitKey(0)

while True:
    ret, frame = video_capture.read()
    cv2.setMouseCallback('Source Image', on_mouse, frame)
    cv2.imshow('Source Image', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

