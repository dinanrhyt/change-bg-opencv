

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:47:42 2019

@author: Toshiba
"""
import cv2 as cv
import numpy as np

# Load the aerial image and convert to HSV colourspace
image = cv.imread("result.png")
image = np.array(image, dtype=np.uint8)
hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)

# Define lower and uppper limits of what we call "red"
lower = np.array([0,100,100])
upper = np.array([20,255,255])


# Mask image to only select browns
mask=cv.inRange(hsv,lower,upper)

# Change image to purple where we found red
image[mask>0]=(205,0,205)

cv.imwrite("result2.png",image)