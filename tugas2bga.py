# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:47:42 2019

@author: Toshiba
"""
import cv2 as cv
import numpy as np

# Load the aerial image and convert to HSV colourspace
image = cv.imread("bgblack.png")
image = np.array(image, dtype=np.uint8)
hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)

# Define lower and uppper limits of what we call "brown"
brown_lo=np.array([0,0,0])
brown_hi=np.array([0,0,0])

# Mask image to only select browns
mask=cv.inRange(hsv,brown_lo,brown_hi)

# Change image to red where we found brown
image[mask>0]=(0,0,255)

cv.imwrite("bgresult.png",image)