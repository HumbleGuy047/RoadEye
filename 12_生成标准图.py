import numpy as np
import cv2
import os

def showImg(imgName,img):
	cv2.imshow(imgName, img)
	while True:
		if cv2.getWindowProperty(imgName,0)==-1:
			break
		cv2.waitKey(20)
	cv2.destroyAllWindows()

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

ww = 200
hh = 160
#I=np.zeros((h,w),dtype=np.uint8)
#showImg('img',I)
rpath = 'cars'
categ = 'null'
for dirpath, dirnames, filenames in os.walk(rpath):
	for fileName in filenames:
		imgPath = '%s/%s'%(rpath,fileName)
		img1 = cv2.imread(imgPath)
		h,w,_ = img1.shape
		v = h/w
		if v<1.6:
			categ = 'car'
		elif v>1.9:
			categ = 'bike'
		#print(categ)
		gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
		I=np.zeros((hh,ww),dtype=np.uint8)
		copyImg(I,gray1,0,0)
		savePath = 'cars1/%s/%s'%(categ,fileName)
		cv2.imwrite(savePath,I)
		#showImg('img',I)
