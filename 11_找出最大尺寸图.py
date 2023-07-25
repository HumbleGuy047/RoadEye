import os
import cv2
rpath = './cars'
maxH = 0
maxW = 0
for dirpath, dirnames, filenames in os.walk(rpath):
	#print(dirpath,dirnames,filenames)
	for fileName in filenames:
		imgPath = '%s/%s'%(rpath,fileName)
		img = cv2.imread(imgPath)
		h,w,_ = img.shape
		if maxH<h:
			maxH = h
		if maxW<w:
			maxW = w
print(maxH,maxW)
		