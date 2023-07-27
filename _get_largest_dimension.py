import os
import cv2
rpath = 'raw_data'
maxH = 0
maxW = 0

# get largest image and use its dimension for all other images
for dirpath, dirnames, filenames in os.walk(rpath):
	for fileName in filenames:
		imgPath = '%s/%s'%(rpath,fileName)
		img = cv2.imread(imgPath)
		h,w,_ = img.shape
		if maxH<h:
			maxH = h
		if maxW<w:
			maxW = w
print(maxH,maxW)
		