import cv2
from random import randint

for a in range(1,5):
	faceCascade = cv2.CascadeClassifier("face.xml")
	image = cv2.imread(str(a) + ".jpg")
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
	for (x, y, w, h) in faces:
		b = randint(0,255)
		g = randint(0,255)
		r = randint(0,255)
		cv2.rectangle(image, (x, y), (x+w, y+h), (b, g, r), 2)
	cv2.imshow("Faces found" ,image)
	cv2.waitKey(0)
