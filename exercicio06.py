import cv2
import numpy as np

color = cv2.imread('einsteinColor.webp')
gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
grayImageBGRspace = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImageBGRspace, 127, 255, cv2.THRESH_BINARY)
horizontalAppendedIGrayImg = np.hstack((color, grayImageBGRspace, blackAndWhiteImage))
cv2.imshow('Horizontal Appended Gray Img', horizontalAppendedIGrayImg)


# cv2.imshow('Einstein Colorido', color)


# horizontalAppendedIGrayImg = np.hstack((color, grayImageBGRspace))
# cv2.imshow('Horizontal Appended Gray Img', horizontalAppendedIGrayImg)
# cv2.imshow('Preto e Branco', blackAndWhiteImage)


cv2.waitKey(0)

