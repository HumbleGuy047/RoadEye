import cv2
import numpy as np

cap = cv2.VideoCapture(0)		#0表摄像头
#cap = cv2.VideoCapture('../dataset/公路来往车辆2.mp4')		#读取视频
cv2.namedWindow("video",0)		#使得窗口名为video的窗口可以改变大小
#创建背景差分器对象
#mog = cv2.createBackgroundSubtractorMOG2()	#OpenCV有两种实现，分别命名为：cv2.BackgroundSubtractorMOG 和 cv2.BackgroundSubtractorMOG2，后者是最新改进的实现，增加了对阴影检测的支持,此算法结合了静态背景图像估计和每个像素的贝叶斯分割，detectShadows = True(默认值)，它就会检测并将影子标记出来，但是这样做会降低处理速度。影子会被标记为灰色。
mog = cv2.createBackgroundSubtractorKNN()	#knn分割，实验结果发现KNN的结果要明显优于MOG2算法。
while True:
	ret,frame = cap.read()
	if ret:
		#fgmask = mog.apply(frame)
		gray = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)	#Y是亮度通道，Cr是红色分量，Cb是蓝色分量
		fgmask = mog.apply(gray, learningRate = 0.05)
		cv2.imshow('video',fgmask)		#显示前景
		key = cv2.waitKey(20)
		if key == 27:	#esc
			break

#释放资源
cap.release()
cv2.destroyAllWindows()