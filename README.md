# computerVision

To run dnn

python faceDetection/dnn.py --prototxt faceDetection/deploy.prototxt.txt --model faceDetection/model.caffemodel


To run face recognition

python faceRecognition/train_model.py --embeddings faceRecognition/output/embeddings.pickle \
	--recognizer faceRecognition/output/recognizer.pickle \
	--le faceRecognition/output/le.pickle


python faceRecognition/recognize.py --detector faceRecognition/face_detection_model \
	--embedding-model faceRecognition/openface_nn4.small2.v1.t7 \
	--recognizer faceRecognition/output/recognizer.pickle \
	--le faceRecognition/output/le.pickle

To run facial landmarks

python facialLandmarks/facial_landmarks.py --shape-predictor facialLandmarks/shape_predictor_68_face_landmarks.dat


To run semantic segmentation:

python opencv-semantic-segmentation/segment_video.py --model opencv-semantic-segmentation/enet-cityscapes/enet-model.net \
	--classes opencv-semantic-segmentation/enet-cityscapes/enet-classes.txt \
	--colors opencv-semantic-segmentation/enet-cityscapes/enet-colors.txt \
	--video opencv-semantic-segmentation/videos/austral2.mp4 \
	--output opencv-semantic-segmentation/output/austral_output.avi


python opencv-semantic-segmentation/segment_video.py --model opencv-semantic-segmentation/enet-cityscapes/enet-model.net \
	--classes opencv-semantic-segmentation/enet-cityscapes/enet-classes.txt \
	--colors opencv-semantic-segmentation/enet-cityscapes/enet-colors.txt \
	--video opencv-semantic-segmentation/videos/pana.mp4 \
	--output opencv-semantic-segmentation/output/austral_output.avi



To detect license plates

python Extraction.py --image
