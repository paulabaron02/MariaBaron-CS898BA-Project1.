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


# %% Part 1 
# Multi-Channel Color Normalization:
# 1.1. Load the original image from Homework One.
Image_Alien = cv2.imread(r"C:\Users\Paula\.spyder-py3\MariaBaron-CS898BA-Project1\MariaBaron-CS898BA-Project1\HW1_IMG_CS898BA.png")
Image_Alien_RGB = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2RGB)
plt.imshow(Image_Alien_RGB)
plt.title("Original")
plt.axis("off")
plt.tight_layout()
plt.show()
plt.savefig("Results/Original.png")

# 1.2. Split the image into its three color channels (e.g., R, G, and B or 
# via the V channel in HSV/ L channel in LAB).

BlueChannel, GreenChannel, RedChannel = cv2.split(Image_Alien)
cv2.imwrite(os.path.join(Results_2, "Red_Channel.png"), RedChannel)
cv2.imwrite(os.path.join(Results_2, "Green_Channel.png"), GreenChannel)
cv2.imwrite(os.path.join(Results_2, "Blue_Channel.png"), BlueChannel)
print("1.2 Complete")

# 1.3. Apply Histogram Equalization independently to all three channels to 
# normalize illumination and maximize contrast across the entire color spectrum.

Red_EQ = cv2.equalizeHist(RedChannel)
Green_EQ = cv2.equalizeHist(GreenChannel)
Blue_EQ = cv2.equalizeHist(BlueChannel)
print("1.3 Complete")

# 1.4. Merge the channels back together to create a fully normalized color image.

Image_RGB_EQ = cv2.merge((Red_EQ, Green_EQ, Blue_EQ))

# 1.5. Save this normalized color image; it will serve as the primary input 
# for all subsequent segmentation tasks.

cv2.imwrite(os.path.join(Results_2, "Image_RGB_Equalization.png"), Image_RGB_EQ)
print("1.4 Complete")




