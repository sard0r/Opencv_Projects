import cv2 

img = cv2.imread("photo.jpg")
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def empty():
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)






cv2.imshow("Hsv", imgHSV)
cv2.waitKey(0)