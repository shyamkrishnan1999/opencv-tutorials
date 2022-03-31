#Importing opencv library
import cv2

#Reading the image
img=cv2.imread('assets/logo.png',-1)

#Resizing the image
img=cv2.resize(img,(500,500))

#Rotating an image
img=cv2.rotate(img,cv2.ROTATE_180)

#saving image
cv2.imwrite('modlogo.png',img)

#Display the image
cv2.imshow('Logo',img)

#Close the Window
cv2.waitKey(0)
cv2.destroyAllWindows()


