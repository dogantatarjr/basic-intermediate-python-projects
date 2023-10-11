import cv2 as cv
import numpy as np

jesse = cv.imread('opencv_jesse.png')
walter = cv.imread('opencv_walter.png')
jesse_kesit = jesse[40:95,60:200]
walter[102:157,52:192] = jesse_kesit

cv.imshow("Walter Pinkman",walter)

cv.waitKey(0)
cv.destroyAllWindows()