"""
Homework Two
Maria Paula Baron Rodriguez 
Wsu ID: J858Q278
"""
import sys
print(sys.executable)

import cv2
import matplotlib.pyplot as plt
#import pandas as pd
#import numpy as np
import os
#import scipy.stats as sp
#import random
import shutil
#import re


plt.close('all')

Results_2 = r"C:\Users\Paula\.spyder-py3\MariaBaron-CS898BA-Project1\MariaBaron-CS898BA-Project1\Results_2"

if os.path.exists(Results_2):shutil.rmtree(Results_2)
os.makedirs(Results_2)


# %% Part 2
# Multi-Channel Color Normalization:
# 2.1. Load the original image from Homework One.
Image_Alien = cv2.imread(r"C:\Users\Paula\.spyder-py3\MariaBaron-CS898BA-Project1\MariaBaron-CS898BA-Project1\HW1_IMG_CS898BA.png")
cv2.imwrite(os.path.join(Results_2, "Original.png"), Image_Alien)
#Image_Alien_RGB = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2RGB)
#plt.imshow(Image_Alien_RGB)
#plt.title("Original")
#plt.axis("off")
#plt.tight_layout()
#plt.show()
#plt.savefig("Results_2/Original.png")

# 2.2. Split the image into its three color channels (e.g., R, G, and B or 
# via the V channel in HSV/ L channel in LAB).

BlueChannel, GreenChannel, RedChannel = cv2.split(Image_Alien)
cv2.imwrite(os.path.join(Results_2, "Red_Channel.png"), RedChannel)
cv2.imwrite(os.path.join(Results_2, "Green_Channel.png"), GreenChannel)
cv2.imwrite(os.path.join(Results_2, "Blue_Channel.png"), BlueChannel)
print("2.2 Complete")

# 2.3. Apply Histogram Equalization independently to all three channels to 
# normalize illumination and maximize contrast across the entire color spectrum.

Red_EQ = cv2.equalizeHist(RedChannel)
Green_EQ = cv2.equalizeHist(GreenChannel)
Blue_EQ = cv2.equalizeHist(BlueChannel)
print("2.3 Complete")

# 2.4. Merge the channels back together to create a fully normalized color image.

Image_BRG_EQ = cv2.merge((Blue_EQ, Green_EQ, Red_EQ))
print("2.4 Complete")

# 2.5. Save this normalized color image; it will serve as the primary input 
# for all subsequent segmentation tasks.

cv2.imwrite(os.path.join(Results_2, "Image_RGB_Equalization.png"), Image_BRG_EQ)
print("2.5 Complete")

# %% Part 3 
# 3.1. Otsu’s Global Thresholding:
# Convert your normalized color image to grayscale.

Image_Gray_Normalized = cv2.cvtColor(Image_BRG_EQ, cv2.COLOR_RGB2GRAY)

# Apply Otsu's automatic thresholding to separate the foreground object from the background.

_, Otsu_Mask = cv2.threshold(Image_Gray_Normalized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("3.1 Complete")

# 3.2. Adaptive Thresholding:
# Apply adaptive thresholding (Gaussian window) to the grayscale version of your normalized image to handle local illumination variations.

Adaptive_Mask = cv2.adaptiveThreshold(Image_Gray_Normalized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
print("3.2 Complete")

# Save the resulting binary masks and the segmented foreground extractions for both methods.

cv2.imwrite(os.path.join(Results_2,"Results_HW2_Part3_Otsu_Mask.png"), Otsu_Mask)
cv2.imwrite(os.path.join(Results_2,"Results_HW2_Part3_Adaptive_Mask.png"), Adaptive_Mask)

Otsu_Foreground = cv2.bitwise_and(Image_BRG_EQ, Image_BRG_EQ, mask=Otsu_Mask)
Adaptive_Foreground = cv2.bitwise_and(Image_BRG_EQ, Image_BRG_EQ, mask=Adaptive_Mask)


# Save foreground extractions
cv2.imwrite(os.path.join(Results_2,"Results_HW2_Part_Otsu_Foreground.png"), Otsu_Foreground)
cv2.imwrite(os.path.join(Results_2,"Results_HW2_Part3_Adaptive_Foreground.png"), Adaptive_Foreground)


