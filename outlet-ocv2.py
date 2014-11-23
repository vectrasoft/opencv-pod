import cv2, sys

faceCascade = cv2.CascadeClassifier("outlet.xml")
image = cv2.imread("outlet-test.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 127), 2)
cv2.imshow("Output" ,image)
cv2.waitKey(0)
