import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
import numpy as np
from skimage.filters import threshold_otsu


import glob

time = 0
time_list=[]
area_list=[]



img = cv.imread("C:/Users/skacar/OneDrive - Indiana University/Desktop/others 2-3-23/PYTHON/AI/oneimgeverygroup/resized_SKR4_Day 7_83R.JPG")
output = img.copy()


entropy_img = entropy(img, disk(10))
plt.imshow(entropy_img)






gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 1, param1=30, param2=20, minRadius=0, maxRadius=0)

detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 255, 0), 3)
    cv.circle(output, (x, y), r, (0, 255, 255), 3)

   # cv.circle(output, (x, y), r, (0, 255, 255), 3)

  
cv.imshow("output", output)
cv.waitKey(0)

# Extract the x, y, and radius of the circle found by the Hough Circle Transform
x, y, r = detected_circles[0, 0]

# Load the second image
img2 = cv.imread('C:/Users/skacar/OneDrive - Indiana University/Desktop/others 2-3-23/PYTHON/AI/oneimgeverygroup/resized_SKR4_Day 3_83R.JPG')

# Draw the circle on the second image
cv.circle(img2, (x, y), r, (0, 255, 0), 2)

# Display or save the final image
cv.imshow('Circle on second image', img2)
cv.waitKey(0)
cv.destroyAllWindows()





#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated /UXXXXXXXX escape