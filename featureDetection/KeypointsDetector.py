import cv2
import datetime

def f(x): print(x)

video_capture = cv2.VideoCapture(0)
threshold = 50
detector = cv2.FastFeatureDetector_create()
cv2.namedWindow("Keypoints")
cv2.createTrackbar("Threshold", "Keypoints", 0, 100, f)
detectorName = "FAST"
detectorHasChanged = True
while True:
    ret, frame = video_capture.read()
    threshold = cv2.getTrackbarPos('Threshold', 'Keypoints')

    key = cv2.waitKey(1)
    if key == ord('1'):
        detector = cv2.FastFeatureDetector_create(threshold=threshold)
        detectorName = "FAST"
        detectorHasChanged = True
    elif key == ord('2'):
        detector = cv2.AKAZE_create(threshold=threshold)
        detectorName = "AKAZE"
        detectorHasChanged = True
    elif key == ord('3'):
        detector = cv2.AgastFeatureDetector_create(threshold=threshold)
        detectorName = "AGAST"
        detectorHasChanged = True
    elif key == ord('4'):
        detector = cv2.ORB_create()
        detectorName = "ORB"
        detectorHasChanged = True
    elif key == ord('q'):
        break

    initTime = datetime.datetime.now()
    keypoints = detector.detect(frame, None)
    endTime = datetime.datetime.now()
    if detectorHasChanged:
        print("Chosen detector: " + detectorName)
        print("Calculation time for " + detectorName + " : " + str(endTime - initTime))

    keypointsDraw = cv2.drawKeypoints(frame, keypoints, None, color=(255, 0, 0))
    cv2.imshow('Keypoints', keypointsDraw)
    detectorHasChanged = False

cv2.destroyAllWindows()