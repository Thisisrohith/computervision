import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/Dama Prasoona/Downloads/22.png", cv2.IMREAD_GRAYSCALE)

# Define the kernel size and shape
kernel_size = 3
kernel_shape = cv2.MORPH_RECT

# Define the opening operation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((kernel_size, kernel_size), np.uint8))

# Display the result
cv2.imshow('Opening', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
