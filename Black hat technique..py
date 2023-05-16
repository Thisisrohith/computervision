import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/Dama Prasoona/Downloads/22.png", 0)

# Define the structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

# Perform the Black-hat transform
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Black-hat Transform', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
