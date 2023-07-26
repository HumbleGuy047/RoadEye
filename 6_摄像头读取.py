import cv2
import numpy as np

cap = cv2.VideoCapture(0)		#0表摄像头
cap = cv2.VideoCapture('dataset/公路来往车辆2.mp4')		#读取视频
cv2.namedWindow("video",0)		#使得窗口名为video的窗口可以改变大小
while True:
	ret,frame = cap.read()
	if ret:
		cv2.imshow('video',frame)		#显示前景
		key = cv2.waitKey(20)
		if key == 27:	#esc
			break

#释放资源
cap.release()
cv2.destroyAllWindows()
