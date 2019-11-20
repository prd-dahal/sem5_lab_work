import cv2  
import numpy as np  
     

image1 = cv2.imread('input1.jpg')  
image2 = cv2.imread('input2.jpg') 
img1 = cv2.resize(image1,(256,256))
img2 = cv2.resize(image2,(256,256))
  
  
dest_and = cv2.bitwise_xor(img2, img1, mask = None) 
  
cv2.imshow('Bitwise XOR', dest_and) 
   
   
cv2.waitKey(0)   
cv2.destroyAllWindows() 