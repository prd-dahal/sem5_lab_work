import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('download.png')
cv2.imshow('image',img)
img1 = cv2.imread('download.png',0)
cv2.imshow('g',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
print(img[:,:,0])