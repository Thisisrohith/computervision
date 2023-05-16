import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/Dama Prasoona/OneDrive/Pictures/35.png")

# Draw a rectangle on the image
x, y, w, h = 100, 100, 200, 200
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Extract the object inside the rectangle
object_roi = img[y:y+h, x:x+w]

# Display the original image and the extracted object
cv2.imshow('Original Image', img)
cv2.imshow('Extracted Object', object_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
