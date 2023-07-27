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

rpath = 'train_data'
categ = 'null'
xtrain = []
ytrain = []
for dirpath, dirnames, filenames in os.walk(rpath):
	for dname in dirnames:
		cpath = '%s/%s'%(rpath,dname)
		for dirpath, dirnames, filenames in os.walk(cpath):
			for fileName in filenames:
				imgPath = '%s/%s'%(cpath,fileName)
				img1 = cv2.imread(imgPath)
				gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
				x_img1 = gray1.flatten()
				xtrain.append(x_img1)
				ytrain.append(dname)
	break

import joblib

'''
# knn
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)		
trainRs = knn.fit(xtrain,ytrain)
joblib.dump(trainRs,'vehicle_knn.pkl')

rf=joblib.load('vehicle_knn.pkl')
from sklearn.metrics import accuracy_score
y_model = rf.predict(xtrain)
score = accuracy_score(ytrain, y_model)
print(score)
'''
'''
# Naive Bayes
#1. Gausian distribution：
from sklearn.naive_bayes import GaussianNB 
gnb=GaussianNB() 
trainRs = gnb.fit(xtrain,ytrain)
joblib.dump(trainRs,'vehicle_nb.pkl')
from sklearn.metrics import accuracy_score
y_model = gnb.predict(xtrain)
score = accuracy_score(ytrain, y_model)
print(score)
'''
'''
#svm
from sklearn.svm import SVC
clf = SVC(kernel='rbf', C=1E6)
trainRs = clf.fit(xtrain,ytrain)
joblib.dump(trainRs,'vehicle_svm.pkl')
from sklearn.metrics import accuracy_score
y_model = clf.predict(xtrain)
score = accuracy_score(ytrain, y_model)
print(score)
'''
#logistic regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
trainRs = lr.fit(xtrain,ytrain)
joblib.dump(trainRs,'vehicle_lr.pkl')

from sklearn.metrics import accuracy_score
y_model = lr.predict(xtrain)
score = accuracy_score(ytrain, y_model)
print(score)
