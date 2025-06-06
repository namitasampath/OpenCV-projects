import cv2

hercescad = "haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)
count = 0

while True:
    success, img=cap.read()

    plate_cascade = cv2.CascadeClassifier(hercescad)

    img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates= plate_cascade.detectMultiScale(img_gray, 1.1,4)
    # contains all rectangular points(x,y,w,h)

    for(x,y,w,h) in plates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img, "Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)
        img_roi = img[y:y+h, x:x+w]
        cv2.imshow("ROI", img_roi)

    cv2.imshow("car Plate",img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Plates/Car_plate"+str(count)+".jpg",img_roi)
        cv2.rectangle(img, (0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
        cv2.imshow("Success",img)
        cv2.waitKey(500)
        count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
