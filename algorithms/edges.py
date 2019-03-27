from skimage import exposure
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
    help = "Path to the query image")
args = vars(ap.parse_args())

image = cv2.imread(args["query"])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_range = np.array([35, 100, 100], dtype=np.uint8)
upper_range = np.array([55, 255, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_range, upper_range)

contours = cv2.findContours(mask, 1, 2)

#cv2.imshow("Contours", contours)
cv2.imshow("Gray scalled", mask)
cv2.waitKey(0)