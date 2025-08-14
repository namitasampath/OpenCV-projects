import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# 0 - default webcam, capturing the video

#FourCC is 4-byte code that specifies the video codec(compression format)
#'XVID' is a popular format for .avi files
FourCC = cv2.VideoWriter_fourcc(*'XVID')
#vid format


out = cv2.VideoWriter('output.avi', FourCC, 20.0, (640,480))
#filename, codec used, fps, frame size

while (True):
    ret, frame = cap.read()
    #reads frame from the webcam
    #ret is True if a frame was read successfully
    #frame is the actual image(numpy array)
    out.write(frame)
    #saves the current frame into video file.
    cv2.imshow('Live',frame)#display in window titled live
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()#frees the webcam
out.release()#closes the video file

cv2.destroyAllWindows() #closes all opencv windows