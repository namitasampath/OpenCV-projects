import cv2 as cv

def FrameCapture(path):
    vidobj=cv.VideoCapture(path)


    count=0
    success = 1

    while success:
        success,image = vidobj.read()
        cv.imwrite("Frame%d.jpg" % count, image)
        count+=1

if __name__=='__main__':
    FrameCapture("video1.mp4")
