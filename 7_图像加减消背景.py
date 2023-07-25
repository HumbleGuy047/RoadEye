import cv2
import numpy as np

def showImg(imgName,img):
	cv2.imshow(imgName, img)
	while True:
		if cv2.getWindowProperty(imgName,0)==-1:
			break
		cv2.waitKey(20)
	cv2.destroyAllWindows()

img1 = cv2.imread('../dataset/imgs/pai/du3.png')
img2 = cv2.imread('../dataset/imgs/pai/du4.png')
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#img = cv2.subtract(gray1,gray2)	#减去得比较彻底，减没了就是黑的。
img = cv2.subtract(img1,(150,150,150,0))	#每个像素都减去那么多，变黑。
#img = img1 - img2				#直接减，背景花了。如果直接计算的结果小于0，得到的结果不会出现负数，而是在这个负数的基础上加上256，比如0-109=-109，实际的像素值则为-109+256=147，和符号+运算一样也是对256求模的结果。
#img = img1 + img2					#加完重影
#img = cv2.add(img1,img2)			#重影干净些
#img =  cv2.absdiff(gray1,gray2)	#2个图像间像素的绝对差值。减没了是白的。
showImg('img',img)