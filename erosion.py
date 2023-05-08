#  Read Image and Display it in Gray scale,
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "C:/Users/Dama Prasoona/Downloads/harrypotter.png"
img =  cv2.imread(path)
imgEroded = cv2.erode(imgDilation,kernel,iterations=2)
cv2.imshow("Img Erosion",imgEroded)
cv2.waitKey(0)
