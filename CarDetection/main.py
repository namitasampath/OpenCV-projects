import cv2

cascade= 'cars.xml'
video = 'cars.mp4'

cap = cv2.VideoCapture(video)
#opens video
car_cascade = cv2.CascadeClassifier(cascade)
#loads trained car detection model

while True:
    Success, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    #scans image for matching cars

    for(x,y,w,h) in cars:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow('Cars', img)

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()