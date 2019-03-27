from skimage import exposure
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
    help = "Path to the query image")
args = vars(ap.parse_args())

fname = cv2.imread(args["query"])
orig_img = fname

# Blur image to remove noise
frame=cv2.GaussianBlur(fname, (3, 3), 0)

# Switch image from BGR colorspace to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of purple color in HSV
purpleMin = (115,50,10)
purpleMax = (160, 255, 255)

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

# Set up the SimpleBlobdetector with default parameters.
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 0;
params.maxThreshold = 256;

 
# Filter by Area.
params.filterByArea = True
params.minArea = 200
params.maxArea = 400

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.5
 
# Filter by Convexity
params.filterByConvexity = False
#params.minConvexity = 0.87
	 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.8

# Distance Between Blobs
params.minDistBetweenBlobs = 200

detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
reversemask=255-mask
keypoints = detector.detect(reversemask)

crops = cv2.countNonZero(mask ) 
print ("None Zero: %i" % crops)

if keypoints:
    print ("found %d blobs" % len(keypoints))
    if len(keypoints) > 4:
        # if more than four blobs, keep the four largest
        keypoints.sort(key=(lambda s: s.size))
        keypoints=keypoints[0:3]
else:
    print ("no blobs")


edged = cv2.Canny(mask, 30, 200)
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
count = len(contours)
print ("Contours are: %i" %count)
#cv2.drawContours(mask, contours, -1, (0,255,0), 3)

# Draw green circles around detected blobs
im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (25,5,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
# open windows with original image, mask, res, and image with keypoints marked
cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)  
cv2.imshow('Edged',edged)    
cv2.imshow("Keypoints for ", im_with_keypoints)            
    
cv2.waitKey(0)
cv2.destroyAllWindows()
