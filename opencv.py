import cv2 as cv
import numpy as np

walter = cv.imread('opencv_walter2.png')
jesse = cv.imread('opencv_jesse2.png')

jesse_white = cv.addWeighted(walter,0.5,jesse,0.5,0)

cv.imshow("Jesse White",jesse_white) 

cv.waitKey(0)
cv.destroyAllWindows()