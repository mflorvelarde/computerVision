import cv2

def f(x): print(x)


video_capture = cv2.VideoCapture(0)
threshold = 50
detector = cv2.ORB_create()
detectorName = "ORB"
detectorHasChanged = True

cv2.namedWindow("Keypoints")
cv2.createTrackbar("Threshold", "Keypoints", 0, 100, f)
cv2.createTrackbar("Matcher - 0 = FLANN, 1 = Brute force", "Keypoints", 0, 1, f)

referenceImage = video_capture.read()[1]
while True:
    ret, frame = video_capture.read()
    threshold = cv2.getTrackbarPos('Threshold', 'Keypoints')

    key = cv2.waitKey(1)
    if key == ord('1'):
        detector = cv2.AKAZE_create(threshold=threshold)
        detectorName = "AKAZE"
        detectorHasChanged = True
    elif key == ord('2'):
        detector = cv2.ORB_create()
        detectorName = "ORB"
        detectorHasChanged = True
    elif key == ord('f'):
        referenceImage = frame
    elif key == ord('q'):
        break

    matcher = cv2.getTrackbarPos('Matcher - 0 = FLANN, 1 = Brute force', 'Keypoints')
    if matcher == 0:
        if detectorHasChanged:
            print("Chosen detector for brute force: " + detectorName)
        kp1, des1 = detector.detectAndCompute(frame, None)
        kp2, des2 = detector.detectAndCompute(referenceImage, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors.
        matches = bf.match(des1, des2)
        # Sort them in the order of their distance.
        matches = sorted(matches, key=lambda x: x.distance)

        # Draw first 10 matches.
        matchesImage = cv2.drawMatches(frame, kp1, referenceImage, kp2, matches[:10], flags=2, outImg=None)

        #detector = cv2.ORB_create()
    elif matcher == 1:
        # Initiate SIFT detector
        sift = cv2.xfeatures2d.SIFT_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(frame, None)
        kp2, des2 = sift.detectAndCompute(referenceImage, None)

        # FLANN parameters
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)  # or pass empty dictionary

        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(des1, des2, k=2)

        # Need to draw only good matches, so create a mask
        matchesMask = [[0, 0] for i in range(len(matches))]

        # ratio test as per Lowe's paper
        for i, (m, n) in enumerate(matches):
            if m.distance < 0.7 * n.distance:
                matchesMask[i] = [1, 0]

        draw_params = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), matchesMask=matchesMask, flags=0)

        matchesImage = cv2.drawMatchesKnn(frame, kp1, referenceImage, kp2, matches, None, **draw_params)


    cv2.imshow('Keypoints', matchesImage)
    detectorHasChanged = False
cv2.destroyAllWindows()