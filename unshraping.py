import cv2
import numpy as np

# Read the image
img = cv2.imread("C:/Users/Dama Prasoona/OneDrive/Pictures/ss.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the Laplacian filter with an extension of diagonal neighbors
laplacian_kernel = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])
laplacian = cv2.filter2D(gray, -1, laplacian_kernel)

# Add the Laplacian image to the original grayscale image to obtain the sharpened image
sharpened = cv2.add(gray, laplacian)

# Display the original and sharpened images
cv2.imshow('Original Image', gray)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
