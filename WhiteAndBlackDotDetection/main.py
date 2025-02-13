# White and Black Dot detection using OpenCV

import cv2

# path = "black-dot1.jpg"
path = "white-dot.png"

gray = cv2.imread(path,0)


# threshold

# th, threshed = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
th, threshed = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# contour function takes 3 arguments - first one is source image and second one is contour retrieval and contour approval and third one is contour approximation

cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

# filter by area

s1 = 3
s2 = 20
xcnts = []

for cnt in cnts:
    if s1 < cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)

# print(f"Total number of black dots is {len(xcnts)}")
print(f"Total number of white dots is {len(xcnts)}")