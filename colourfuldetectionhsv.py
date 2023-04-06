import cv2
import numpy as np
import pdb

# Load the image
img = cv2.imread('C:/Users/skacar/OneDrive - Indiana University/Desktop/others 2-3-23/PYTHON/AI/oneimgeverygroup/resized_SKR4_Day 0_83L.JPG')

# Convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Show the concatenated image
cv2.imshow("Images", hsv)
cv2.waitKey(0)


# Define the lower and upper boundaries of the red color in HSV
lower_red = np.array([0, 70, 50])
upper_red = np.array([10, 255, 255])

# Threshold the image to get only red pixels
mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow("mask", mask)
cv2.imshow("ori", img)
cv2.waitKey(0)

# Find contours in the binary image
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# Find the largest contour
largest_contour = max(contours, key=cv2.contourArea)


# Draw a circle around the largest contour
(x, y), radius = cv2.minEnclosingCircle(largest_contour)
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (0, 0, 255), 2)

# Show the result
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
