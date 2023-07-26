import cv2
import numpy as np

# cap = cv2.VideoCapture(0)							   # 0 means computer camera
cap = cv2.VideoCapture('dataset/公路来往车辆2.mp4')		# read video
cv2.namedWindow("video",0)		# enable resizing of window
while True:
	ret,frame = cap.read()
	if ret:
		cv2.imshow('video',frame)		# show image
		key = cv2.waitKey(20)
		if key == 27:	#esc
			break

#release resource
cap.release()
cv2.destroyAllWindows()
