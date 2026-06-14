"""
Homework One
Maria Paula Baron Rodriguez 
Wsu ID: J858Q278
"""

import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import scipy.stats as sp

plt.close('all')
#load the image
Image_Alien = cv2.imread(r"C:\Users\Paula\.spyder-py3\MariaBaron-CS898BA-Project1\MariaBaron-CS898BA-Project1\HW1_IMG_CS898BA.png")
Image_Alien_RGB = cv2.cvtColor(Image_Alien, cv2.COLOR_BGRA2RGB)
plt.imshow(Image_Alien_RGB)
plt.title("Original")
plt.axis("off")
plt.tight_layout()
plt.show()


#2.1 Channels image statics
Blue, Green, Red = cv2.split(Image_Alien)

BlueChannel = cv2.cvtColor(Blue, cv2.COLOR_BGRA2RGB)
Statics_BlueChannel = {
    "Min": BlueChannel.min(),
    "Max": BlueChannel.max(),
    "Average": BlueChannel.mean(),
    "Median": np.median(BlueChannel),
    "Skew": sp.skew(BlueChannel.flatten()),
    "Range": (BlueChannel.max() - BlueChannel.min()),
    "Standard Deviation": (BlueChannel.std()),
    "Variance": (BlueChannel.var()),
}

modo = sp.mode(BlueChannel.flatten(), keepdims=False)
Statics_BlueChannel["Mode"] = int(modo.mode)

#creates a full image with the values and the respective image in the color 
df = pd.DataFrame(Statics_BlueChannel.items(),columns=["Statics","value"])
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(BlueChannel, cmap='viridis')
ax1.axis('off') 
tabla = ax2.table(cellText=df.values, 
                  colLabels=df.columns, 
                  cellLoc='center', 
                  loc='center')
tabla.scale(1, 0.85) 
ax2.axis('off') 
fig.suptitle('Blue Channel',y=0.75)
plt.tight_layout()
plt.show()

RedChannel = cv2.cvtColor(Red, cv2.COLOR_BGRA2RGB)
Statics_RedChannel = {
    "Min": RedChannel.min(),
    "Max": RedChannel.max(),
    "Average": RedChannel.mean(),
    "Median": np.median(RedChannel),
    "Skew": sp.skew(RedChannel.flatten()),
    "Range": (RedChannel.max() - RedChannel.min()),
    "Standard Deviation": (RedChannel.std()),
    "Variance": (RedChannel.var()),
}
modo = sp.mode(RedChannel.flatten(), keepdims=False)
Statics_RedChannel["Mode"] = int(modo.mode)

#creates a full image with the values and the respective image in the color 
df1 = pd.DataFrame(Statics_RedChannel.items(),columns=["Statics","value"])
fig1, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(RedChannel, cmap='viridis')
ax1.axis('off') 
tabla1 = ax2.table(cellText=df1.values, 
                  colLabels=df1.columns, 
                  cellLoc='center', 
                  loc='center')
tabla1.scale(1, 0.85) 
ax2.axis('off') 
fig1.suptitle('Red Channel',y=0.75)
plt.tight_layout()
plt.show()

GreenChannel = cv2.cvtColor(Green, cv2.COLOR_BGRA2RGB)
Statics_GreenChannel = {
    "Min": GreenChannel.min(),
    "Max": GreenChannel.max(),
    "Average": GreenChannel.mean(),
    "Median": np.median(GreenChannel),
    "Skew": sp.skew(GreenChannel.flatten()),
    "Range": (GreenChannel.max() - GreenChannel.min()),
    "Standard Deviation": (GreenChannel.std()),
    "Variance": (GreenChannel.var()),
}
modo = sp.mode(GreenChannel.flatten(), keepdims=False)
Statics_GreenChannel["Mode"] = int(modo.mode)

#creates a full image with the values and the respective image in the color 
df2 = pd.DataFrame(Statics_GreenChannel.items(),columns=["Statics","value"])
fig2, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(GreenChannel, cmap='viridis')
ax1.axis('off') 
tabla2 = ax2.table(cellText=df2.values, 
                  colLabels=df2.columns, 
                  cellLoc='center', 
                  loc='center')
tabla2.scale(1, 0.85) 
ax2.axis('off') 
fig2.suptitle('Green Channel',y=0.75)
plt.tight_layout()
plt.show()