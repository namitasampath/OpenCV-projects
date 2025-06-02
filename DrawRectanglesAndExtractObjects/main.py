import cv2
import argparse

ref_point = []
crop = False

def shape_selection(event, x, y, flags, param):
    global ref_point, crop, image
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):  # Reset
        image = clone.copy()
    elif key == ord("c"):  # Continue
        break

if len(ref_point) == 2:
    x1, y1 = ref_point[0]
    x2, y2 = ref_point[1]
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    crop_img = clone[y1:y2, x1:x2]
    cv2.imshow("crop_image", crop_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
