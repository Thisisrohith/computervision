import cv2
import numpy as np

image = cv2.imread("C:/Users/Dama Prasoona/OneDrive/Pictures/255.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gradient_x = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)
gradient_y = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3)
gradient = cv2.subtract(gradient_x, gradient_y)
cv2.imwrite('sharpened_image.jpg', gradient)
