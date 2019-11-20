import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('horse.png',0)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
titles = ['Original Image','BINARY_INV']
images = [img, thresh2]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()