import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/Dama Prasoona/OneDrive/Pictures/35.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define the lower and upper range of the color for the watch (in HSV color space)
lower_color = np.array([0, 0, 0])
upper_color = np.array([179, 50, 50])

# Create a mask based on the color range
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_color, upper_color)

# Apply morphological operations to remove noise
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Detect edges using Canny edge detection
edges = cv2.Canny(opening, 50, 200)

# Find contours in the image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and draw a rectangle around the watch
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w > 50 and h > 50: # filter out small contours that may be noise
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

# Display the results
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
