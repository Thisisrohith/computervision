import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/Dama Prasoona/Downloads/22.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to the image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Define the erosion kernel
kernel = np.ones((3, 3), np.uint8)

# Perform the erosion operation
erosion = cv2.erode(thresh, kernel, iterations=1)

# Display the original and eroded images side by side
cv2.imshow('Original', thresh)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
