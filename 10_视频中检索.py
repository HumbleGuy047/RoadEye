import cv2
import numpy as np

#cap = cv2.VideoCapture(0)		# 0 means webcam
cap = cv2.VideoCapture('dataset/公路来往车辆2.mp4')	# read video file
cv2.namedWindow("video",0)		# enable resizing video window
# Create BackgroundSubtraction object
# OpenCV's two implementations of MOG：...MOG and ...rMOG2，latter is 
# newer and includes shadow detection, combining static background 
# approximation and naive bayes segmentation，detectShadows = True (default) 
# to mark shadow but also reduces the speed, where shadows are marked grey.
# mog = cv2.createBackgroundSubtractorMOG2()	
mog = cv2.createBackgroundSubtractorKNN()	# knn segmentation，better result than MOG2 from observation
ii=1
flag=0
while True:
	ret,frame = cap.read()
	if ret:
		#fgmask = mog.apply(frame)
		gray = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)	#Y是亮度通道，Cr是红色分量，Cb是蓝色分量
		fgmask = mog.apply(gray, learningRate = 0.05)
		#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
		#img1 = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=1)
		img1 = cv2.medianBlur(fgmask,15)		# median filtering，second param % 2 ==1
		if flag==1:
			contours,hierarchy = cv2.findContours(img1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
			for contour in contours:
				area = cv2.contourArea(contour)
				if area>100:
					x,y,w,h = cv2.boundingRect(contour)
					img2 = img1[y:y+h,x:x+w]
					imgPath = "raw_data/%d.jpg"%(ii)
					ii += 1
					cv2.imwrite(imgPath,img2)
		cv2.imshow('video',img1)		# show vid
		key = cv2.waitKey(20)
		if key == 32:	# in the video window press blankspace to start generating images
			flag=1
			print(flag)
		elif key == 27:	# esc to exit the program
			break

# release resource
cap.release()
cv2.destroyAllWindows()
