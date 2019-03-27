# Standard imports
import cv2
import argparse
import numpy as np;

ap = argparse.ArgumentParser()

ap.add_argument("-q", "--query", required = True,
    help = "Path to the query image")
args = vars(ap.parse_args())

im = cv2.imread(args["query"])#, cv2.IMREAD_GRAYSCALE)
 
# Set up the detector\
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

params.blobColor = 166
params.filterByColor = True
'''
# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 200;

# Filter by Area.
params.filterByArea = True
params.minArea = 50

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
''
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
'''

detector = cv2.SimpleBlobDetector_create(params)
 
# Detect blobs.
keypoints = detector.detect(255 - im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
#cv2.imshow("Keypoints", im)
cv2.waitKey(0)