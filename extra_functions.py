import numpy as np
import cv2

# Define color selection criteria
red_threshold = 200
green_threshold = 200
blue_threshold = 175

rgb_threshold = (red_threshold, green_threshold, blue_threshold)

def color_thresh(img, rgb_thresh=(0, 0, 0)):
    ###### TODO:
    # Create an empty array the same size in x and y as the image 
    # but just a single channel
    color_select = np.zeros_like(img[:,:,0])
    # Apply the thresholds for RGB and assign 1's 
    # where threshold was exceeded
    # Return the single-channel binary image
    for (x, y) in np.ndindex(img.shape[:2]):
        color = np.average(list(map(lambda ch,mask: 0 if ch<=mask else 255, img[x-1,y-1,:], rgb_thresh)))
        color_select[x,y] = color

    return color_select


# Define a box in source (original) and 
# destination (desired) coordinates
# Right now source and destination are just 
# set to equal the four corners
# of the image so no transform is taking place
# Try experimenting with different values!
source = np.float32([[14, 140], 
                 [120, 96], 
                 [200, 96], 
                 [300, 140]])
destination = np.float32([[140, 150], 
                 [140, 120], 
                 [170, 120], 
                 [170, 150]])

def perspect_transform(img, src, dst):

    # Get transform matrix using cv2.getPerspectivTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    # Warp image using cv2.warpPerspective()
    # keep same size as input image
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    # Return the result
    return warped
