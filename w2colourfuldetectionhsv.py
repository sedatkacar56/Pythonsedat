import cv2
import numpy as np
import pdb

# Load the image
img = cv2.imread('C:/Users/skacar/OneDrive - Indiana University/Desktop/others 2-3-23/PYTHON/AI/oneimgeverygroup/resized_SKR4_Day 7_83R.JPG')

# Convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Show the concatenated image


# Define the lower and upper boundaries of the red color in HSV
lower_red = np.array([0, 100, 150])
upper_red = np.array([10, 255, 255])

# Threshold the image to get only red pixels
mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow("ori", img)
cv2.imshow("mask", mask)

cv2.waitKey(0)

#houghhhhhhhhhhhhhhhhhhhhhhhh


gray = cv2.medianBlur(mask, 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=20, param2=20, minRadius=0, maxRadius=0)

detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(img, (x, y), r, (0, 255, 0), 3)
    cv2.circle(img, (x, y), r, (0, 255, 255), 3)

   # cv.circle(output, (x, y), r, (0, 255, 255), 3)

  
# Show the result
cv2.imshow("mask", mask)
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
