#importing libraries
import mahotas
import numpy as np
import cv2

#code
img=mahotas.imread("dog.jpeg")[:,:,0]
kernel=np.array([[-1,0,-1],[0,5,0],[-1,0,-1]])
img=cv2.filter2D(img,kernel=kernel,ddepth=-1)
img_haar=mahotas.haar(img)
cv2.imwrite("dog_haar.jpeg",img)



