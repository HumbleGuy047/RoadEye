import cv2
import numpy as np

cap = cv2.VideoCapture('dataset/公路来往车辆2.mp4')		
cv2.namedWindow("video",0)		
mog = cv2.createBackgroundSubtractorKNN()	
while True:
	ret,frame = cap.read()
	if ret:
		gray = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)	
		fgmask = mog.apply(gray, learningRate = 0.05)
		cv2.imshow('video',fgmask)		
		key = cv2.waitKey(20)
		if key == 27:	
			break

cap.release()
cv2.destroyAllWindows()