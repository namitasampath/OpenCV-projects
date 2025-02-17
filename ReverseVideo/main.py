import cv2

cap = cv2.VideoCapture('video.mp4')

check, vid = cap.read()
# vid holds img of each frame, check is a boolean value
counter = 0
frame_list = []

# storing every frame 
while(check == True):
    cv2.imwrite("frame%d.jpg" % counter,vid)
    check, vid = cap.read()
    frame_list.append(vid)
    counter+=1
# remove the null value
frame_list.pop()
frame_list.reverse()

# showing reverse frame list
for frame in frame_list:
    cv2.imshow("Frame",frame)
    if cv2.waitKey(25) and 0xff ==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()