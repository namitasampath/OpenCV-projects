import cv2
import numpy as np

background = cv2.imread('bg.jpg')
background = cv2.resize(background,(640,480))

lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

cap = cv2.VideoCapture("green.mp4")

if not cap.isOpened():
    print("Video not found")
    exit()

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inverse = cv2.bitwise_not(mask)
    
    object = cv2.bitwise_and(frame, frame, mask=mask_inverse)
    background_part = cv2.bitwise_and(background, background, mask=mask)

    result = cv2.add(object , background_part)

    cv2.imshow("Demo", result)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()