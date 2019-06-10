import cv2
import numpy as np


def f(x): print(x)

video_capture = cv2.VideoCapture(0)

params = cv2.SimpleBlobDetector_Params()
cv2.namedWindow("Keypoints")
cv2.createTrackbar("Min Threshold", "Keypoints", 10, 100, f)
cv2.createTrackbar("Max Threshold", "Keypoints", 200, 200, f)
while True:
    ret, frame = video_capture.read()
    minThreshold = cv2.getTrackbarPos('Min Threshold', 'Keypoints')
    maxThreshold = cv2.getTrackbarPos('Max Threshold', 'Keypoints')
    params.minThreshold = minThreshold
    params.maxThreshold = maxThreshold

    detector = cv2.SimpleBlobDetector_create(params)
    # Detect blobs.
    keypoints = detector.detect(frame)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()