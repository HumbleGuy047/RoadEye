import cv2
import numpy as np
import joblib

rf=joblib.load('vehicle_lr.pkl')
font=cv2.FONT_HERSHEY_SIMPLEX
ww = 233
hh = 222

def copyImg(img1, img2, x, y):
    dim = img2.shape
    colNum = dim[0]
    rowNum = dim[1]
    ii = 0
    jj = 0
    for i in range(x, min(x + colNum, img1.shape[0])):
        jj = 0
        for j in range(y, min(y + rowNum, img1.shape[1])):
            img1[i, j] = img2[ii, jj]
            jj += 1
        ii += 1

cap = cv2.VideoCapture('dataset/公路来往车辆2.mp4')
cv2.namedWindow("video",0)		
mog = cv2.createBackgroundSubtractorKNN()
while True:
	ret,frame = cap.read()
	if ret:
		gray = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)
		fgmask = mog.apply(gray, learningRate = 0.05)
		img1 = cv2.medianBlur(fgmask,15)		
		contours,hierarchy = cv2.findContours(img1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		arrX = []
		arrC = []
		for contour in contours:
			area = cv2.contourArea(contour)
			if area>100:
				x,y,w,h = cv2.boundingRect(contour)
				if w<ww and h<hh:
					img2 = img1[y:y+h,x:x+w]		# detect object
					I=np.zeros((hh,ww),dtype=np.uint8)
					copyImg(I,img2,0,0)
					ximg2 = I.flatten()
					arrX.append(ximg2)
					arrC.append([x,y])
					cv2.rectangle(frame, (x,y) , (x+w , y+h) ,(255,255,255) , 1)
		if len(arrX)>0:
			yarr = rf.predict(arrX)
			ii = 0
			for y in yarr:
				xx,yy = arrC[ii]
				ii += 1
				cv2.putText(frame,y,(xx,yy),font,1,(255,255,255),2,cv2.LINE_AA)	# add text
		cv2.imshow('video',frame)		
		key = cv2.waitKey(20)
		if key == 27:	
			break

cap.release()
cv2.destroyAllWindows()
