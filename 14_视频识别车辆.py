import cv2
import numpy as np
import joblib

rf=joblib.load('vehicle_lr.pkl')
font=cv2.FONT_HERSHEY_SIMPLEX
ww = 200
hh = 160
#img2向img1中拷贝
def copyImg(img1,img2,x,y):
	dim = img2.shape
	colNum = dim[0]
	rowNum = dim[1]
	ii = 0
	jj = 0
	for i in range(x,colNum):
		jj = 0
		for j in range(y,rowNum):
			img1[i,j]=img2[ii,jj]
			jj += 1
		ii += 1

#cap = cv2.VideoCapture(0)		#0表摄像头
cap = cv2.VideoCapture('../dataset/公路来往车辆2.mp4')		#读取视频
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
		#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
		#img1 = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=1)
		img1 = cv2.medianBlur(fgmask,15)		#中值滤波，第2个值必须对2取余==1
		contours,hierarchy = cv2.findContours(img1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		arrX = []
		arrC = []
		for contour in contours:
			area = cv2.contourArea(contour)
			if area>100:
				x,y,w,h = cv2.boundingRect(contour)
				if w<ww and h<hh:
					img2 = img1[y:y+h,x:x+w]		#识别对象
					I=np.zeros((hh,ww),dtype=np.uint8)
					copyImg(I,img2,0,0)
					ximg2 = I.flatten()
					arrX.append(ximg2)
					arrC.append([x,y])
					#cv2.rectangle(img1, (x,y) , (x+w , y+h) ,(255,255,255) , 1)
					cv2.rectangle(frame, (x,y) , (x+w , y+h) ,(255,255,255) , 1)
		if len(arrX)>0:
			yarr = rf.predict(arrX)
			ii = 0
			for y in yarr:
				xx,yy = arrC[ii]
				ii += 1
				#cv2.putText(img1,y,(xx,yy),font,1,(255,255,255),2,cv2.LINE_AA)	#图片上写字
				cv2.putText(frame,y,(xx,yy),font,1,(255,255,255),2,cv2.LINE_AA)	#图片上写字
		#cv2.imshow('video',img1)		#显示前景
		cv2.imshow('video',frame)		#显示前景
		key = cv2.waitKey(20)
		if key == 27:	#esc退出
			break

#释放资源
cap.release()
cv2.destroyAllWindows()
