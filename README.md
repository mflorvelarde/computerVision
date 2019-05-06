# computerVision

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
