import numpy as np
import cv2
import argparse
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
    help = "Path to the query image")
args = vars(ap.parse_args())

frame = cv2.imread(args["query"])
# Switch image from BGR colorspace to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
greenMin = (32, 100, 100)
greenMax = (52, 255, 255)
# Sets pixels to white if in purple range, else will be set to black
mask = cv2.inRange(hsv, greenMin, greenMax)
    
# Bitwise-AND of mask and purple only image - only used for display
res = cv2.bitwise_and(frame, frame, mask= mask)

mask = cv2.erode(mask, None, iterations=1)
# commented out erode call, detection more accurate without it

# dilate makes the in range areas larger
mask = cv2.dilate(mask, None, iterations=1)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 2)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_bg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

params = cv2.SimpleBlobDetector_Params()
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
reversesure_bg=255-sure_bg
keypoints = detector.detect(reversesure_bg)

if keypoints:
    print ("found %d blobs" % len(keypoints))
    if len(keypoints) > 4:
        # if more than four blobs, keep the four largest
        keypoints.sort(key=(lambda s: s.size))
        keypoints=keypoints[0:3]
else:
    print ("no blobs")

markers = cv2.watershed(frame,markers)

cv2.imshow('Sure FG',sure_fg)
#cv2.imwrite("Sure FG.jpg", sure_bg) 
cv2.imshow('Sure BG',sure_bg)
cv2.imshow('Markers',markers)
cv2.imshow('Frame',frame)
cv2.waitKey(0)