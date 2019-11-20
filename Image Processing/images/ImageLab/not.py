  
import cv2  
import numpy as np   
image1 = cv2.imread('input1.jpg')  
image2 = cv2.imread('input2.jpg') 
  

dest_not1 = cv2.bitwise_not(image1, mask = None) 
dest_not2 = cv2.bitwise_not(image2, mask = None) 
  
cv2.imshow('Bitwise NOT on image 1', dest_not1) 
cv2.imshow('Bitwise NOT on image 2', dest_not2)
cv2.waitKey(0)
cv2.destroyAllWindows()