import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/Dama Prasoona/Downloads/22.png", 0)

# Define the structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

# Perform the Top-hat transform
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Top-hat Transform', tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
