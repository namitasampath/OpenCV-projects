import cv2
import numpy as np

def emptyFunction():
    pass
# this is a placeholder function because cv2.createTrackbar requires a callback function


# creating blank image
image = np.zeros((512,512,3),np.uint8)
# 512,512 is screen resolution, 3 is bgr 3 color channel
# doc type is np.uint8
windowName = "Open CV color Palette"

cv2.namedWindow(windowName)


#creating trace bar
cv2.createTrackbar('Blue',windowName,0,255,emptyFunction)
cv2.createTrackbar('Green',windowName,0,255,emptyFunction)
cv2.createTrackbar('Red',windowName,0,255,emptyFunction)
# min value = 0 and max value = 255



while(True):
    cv2.imshow(windowName, image)
    if cv2.waitKey(1) == 27:
    # 27 ascii code for esc,if you press esc it is going to break the load
        break
    blue = cv2.getTrackbarPos('Blue',windowName)
    green = cv2.getTrackbarPos('Green',windowName)
    red = cv2.getTrackbarPos('Red',windowName)

    image[:]=[blue,green,red]
    #used to fill the entire image with a specific color.
    print(blue,green,red)