import numpy as np
import cv2
import os

# def showImg(imgName,img):
# 	cv2.imshow(imgName, img)
# 	while True:
# 		if cv2.getWindowProperty(imgName,0)==-1:
# 			break
# 		cv2.waitKey(20)
# 	cv2.destroyAllWindows()

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

ww = 233
hh = 222

rpath = 'raw_data'
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
		savePath = 'train_data/%s/%s'%(categ,fileName)
		cv2.imwrite(savePath,I)
		#showImg('img',I)
