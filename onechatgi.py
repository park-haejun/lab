import numpy as np
import cv2

def houghCircle():
    img1 = cv2.imread('shape.jpg')
    img2 = img1.copy()

    img2 = cv2.GaussianBlur(img2, (3,3), 0)
    imgray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=50, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            cv2.circle(img1, (i[0], i[1]), i[2], (255, 255, 0), 1)

            cv2.imshow('HoughCircles', img1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print('원을 찾지 못했습니다.')

houghCircle()