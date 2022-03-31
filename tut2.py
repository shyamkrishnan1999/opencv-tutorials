import cv2
import random

img=cv2.imread('assets/logo.png')

tag=img[150:250,150:250]
img[0:100,0:100]=tag

cv2.imshow('mod',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
