import cv2

faceCascade = cv2.CascadeClassifier("face.xml")
cap = cv2.VideoCapture(0)

while True:
	_, image = cap.read()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
	cv2.imshow("Faces found" ,image)
	if (cv2.waitKey(10) == 27):
		cap.close()
		quit()

