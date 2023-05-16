import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/Dama Prasoona/Downloads/22.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image to reduce noise
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply the Sobel kernel to the blurred image to detect the edges
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(sobelx**2 + sobely**2)

# Threshold the output of the Sobel filter to create a binary image where the edges are white and the background is black
thresh = cv2.threshold(sobel, 50, 255, cv2.THRESH_BINARY)[1]

# Apply a dilation operation to thicken the edges
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations=1)

# Apply an erosion operation to remove any small gaps in the edges
erosion = cv2.erode(dilation, kernel, iterations=1)

# Subtract the eroded image from the dilated image to obtain the boundary
boundary = cv2.absdiff(dilation, erosion)

# Show the result
cv2.imshow('Boundary', boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()
