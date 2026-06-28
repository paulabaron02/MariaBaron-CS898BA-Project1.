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
import numpy as np
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
cv2.imwrite(os.path.join(Results_2, "Part2_Red_Channel.png"), RedChannel)
cv2.imwrite(os.path.join(Results_2, "Part2_Green_Channel.png"), GreenChannel)
cv2.imwrite(os.path.join(Results_2, "Part2_Blue_Channel.png"), BlueChannel)
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

cv2.imwrite(os.path.join(Results_2, "Part2_Image_RGB_Equalization.png"), Image_BRG_EQ)
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

cv2.imwrite(os.path.join(Results_2,"Part3_Results_HW2_Otsu_Mask.png"), Otsu_Mask)
cv2.imwrite(os.path.join(Results_2,"Part3_Results_HW2_Adaptive_Mask.png"), Adaptive_Mask)

Otsu_Foreground = cv2.bitwise_and(Image_BRG_EQ, Image_BRG_EQ, mask=Otsu_Mask)
Adaptive_Foreground = cv2.bitwise_and(Image_BRG_EQ, Image_BRG_EQ, mask=Adaptive_Mask)
print("3.2 Foreground_Complete")

# Save foreground extractions
cv2.imwrite(os.path.join(Results_2,"Part3_Results_HW2_Otsu_Foreground.png"), Otsu_Foreground)
cv2.imwrite(os.path.join(Results_2,"Part3_Results_HW2_Adaptive_Foreground.png"), Adaptive_Foreground)

# %% Part 4 
# 4.1. Color-Space Clustering (K-Means):
# - Convert the normalized color image to the HSV color space.

Alien_HSV = cv2.cvtColor(Image_BRG_EQ, cv2.COLOR_BGR2HSV)
cv2.imwrite(os.path.join(Results_2,"_Part4_Alien_HSV.png"), Alien_HSV)
print("4.1 Complete Hsv")

# - Apply K-Means clustering to segment the image into K distinct regions (test and select an optimal K value between 3 and 5).

HSV_Pixels = Alien_HSV.reshape((-1,3))
HSV_Pixels = np.float32(HSV_Pixels)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

for K in [3, 4, 5]:
    
    print("Processing K =", K)

    retk, labelsk, centersk = cv2.kmeans(HSV_Pixels,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centersk)

    # Rebuild segmented HSV image
    Segmented_HSV = centers[labelsk.flatten()]
    Segmented_HSV = Segmented_HSV.reshape(Alien_HSV.shape)

    # Convert segmented image back to BGR for saving
    Segmented_BGR = cv2.cvtColor(Segmented_HSV, cv2.COLOR_HSV2BGR)
    cv2.imwrite(os.path.join(Results_2, f"Part4_K{K}_Segmented.png"),Segmented_BGR)
    
print("4.1 Complete Kmeans")

# - Isolate the cluster that most closely captures the "unknown figure."
# Save the resulting binary masks and the segmented foreground extractions for both methods.

K4 = 4

ret, labels, centers = cv2.kmeans(HSV_Pixels,K4,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

Alien_K4 = labels.reshape(Alien_HSV.shape[:2])

for cluster in range(K4):

    # Binary mask
    Cluster_Mask = np.uint8(Alien_K4 == cluster) * 255
    cv2.imwrite(os.path.join( Results_2,f"Part4_Cluster_{cluster}_Mask.png"),Cluster_Mask)

    # Foreground extraction
    Cluster_Foreground = cv2.bitwise_and(Image_BRG_EQ,Image_BRG_EQ,mask=Cluster_Mask)
    cv2.imwrite(os.path.join(Results_2,f"Part4_Cluster_{cluster}_Foreground.png"),Cluster_Foreground)

print("4.1 Complete Clusters")





