import cv2
import numpy as np

#cap = cv2.VideoCapture(0)		#0表摄像头
cap = cv2.VideoCapture('dataset/公路来往车辆2.mp4')		#读取视频
cv2.namedWindow("video",0)		#使得窗口名为video的窗口可以改变大小
#创建背景差分器对象
#mog = cv2.createBackgroundSubtractorMOG2()	#OpenCV有两种实现，分别命名为：cv2.BackgroundSubtractorMOG 和 cv2.BackgroundSubtractorMOG2，后者是最新改进的实现，增加了对阴影检测的支持,此算法结合了静态背景图像估计和每个像素的贝叶斯分割，detectShadows = True(默认值)，它就会检测并将影子标记出来，但是这样做会降低处理速度。影子会被标记为灰色。
mog = cv2.createBackgroundSubtractorKNN()	#knn分割，实验结果发现KNN的结果要明显优于MOG2算法。
ii=1
flag=0
while True:
	ret,frame = cap.read()
	if ret:
		gray = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)	#Y是亮度通道，Cr是红色分量，Cb是蓝色分量
		fgmask = mog.apply(gray, learningRate = 0.05)
		#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
		#img1 = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=1)
		img1 = cv2.medianBlur(fgmask,15)		#中值滤波，第2个值必须对2取余==1
		if flag==1:
			contours,hierarchy = cv2.findContours(img1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
			for contour in contours:
				area = cv2.contourArea(contour)
				if area>100:
					x,y,w,h = cv2.boundingRect(contour)
					img2 = img1[y:y+h,x:x+w]
					imgPath = "cars/%d.jpg"%(ii)
					ii += 1
					cv2.imwrite(imgPath,img2)
					#cv2.rectangle(img1, (x,y) , (x+w , y+h) ,(255,255,255) , 1)
		cv2.imshow('video',img1)		#显示前景
		key = cv2.waitKey(20)
		if key == 32:	#按空格键开始生成图片
			flag=1
			print(flag)
		elif key == 27:	#esc退出
			break

#释放资源
cap.release()
cv2.destroyAllWindows()
