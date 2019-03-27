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

ret, thresh = cv2.threshold(image, 190, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
'''
cx = int(M['m10']/M'm00'])
cx = int(M['m01']/M'm00'])
'''
area = cv2.contourArea(cnt)
cv2.imshow("Gray scalled", thresh)
cv2.waitKey(0)