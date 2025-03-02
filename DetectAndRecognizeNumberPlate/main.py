import cv2

hercescad = "haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

while True:
    success, img=cap.read()

    plate_cascade = cv2.CascadeClassifier(hercescad)

    img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates= plate_cascade.detectMultiScale(img_gray, 1.1,4)
    # contains all rectangular points(x,y,w,h)

    for(x,y,w,h) in plates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img, "Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)

    cv2.imshow("car Plate",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
