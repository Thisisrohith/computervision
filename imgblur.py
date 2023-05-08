

#  Read Image and Display it in Gray scale,
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path ="C:/Users/Dama Prasoona/Downloads/harrypotter.png"
img =  cv2.imread(path)

imgBlur = cv2.GaussianBlur(img,(7,7),0)




cv2.imshow("Img Blur",imgBlur)

cv2.waitKey(0)
