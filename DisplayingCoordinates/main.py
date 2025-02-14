import cv2

# [print(i) for i in dir(cv2) if 'EVENT' in i]
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x," ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,str(x)+','+str(y),(x,y),font, 1, (255,0,0),thickness=2)
        cv2.imshow('image', img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x," ", y)


if __name__ == "__main__":
    img = cv2.imread('Cat1.jpg', 1)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
