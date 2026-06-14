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

# %%
#2.1 Find and print basic image statistics of the original image for each individual channel (min, max, average, median, mode, skew, range, standard deviation, variance)
BlueChannel, GreenChannel, RedChannel = cv2.split(Image_Alien)
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
fig, axes = plt.subplots(3,2)
axes = axes.flatten()
ax1, ax2, ax3, ax4, ax5, ax6 = axes
ax1.imshow(BlueChannel, cmap='gray')
ax1.axis('off') 
ax1.set_title('Blue Channel', fontsize=9)
tabla = ax2.table(cellText=df.values, 
                  colLabels=df.columns, 
                  cellLoc='center', 
                  loc='center')
tabla.scale(0.85, 0.7) 
ax2.axis('off') 
ax2.set_title('Blue Channel Statics', fontsize=9)
plt.tight_layout()


# %%
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

ax3.imshow(RedChannel, cmap='gray')
ax3.axis('off') 
ax3.set_title('Red Channel', fontsize=9)
tabla1 = ax4.table(cellText=df1.values, 
                  colLabels=df1.columns, 
                  cellLoc='center', 
                  loc='center')
tabla1.scale(0.85, 0.7) 
ax4.axis('off') 
ax4.set_title('Red Channel Statics', fontsize=9)
plt.tight_layout()

# %%
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
ax5.imshow(GreenChannel, cmap='gray')
ax5.axis('off') 
ax5.set_title('Green Channel', fontsize=9)
tabla2 = ax6.table(cellText=df2.values, 
                  colLabels=df2.columns, 
                  cellLoc='center',
                  loc='center')
tabla2.scale(0.85, 0.7) 
ax6.axis('off') 
ax6.set_title('Green Channel Statics', fontsize=9)
plt.tight_layout()


# %%
#2.2 Convert and save the image to greyscale, binary, and different color spaces (HSV, CIELAB, and HLS).

Grey_Image = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2GRAY)
Fig3 = plt.figure() 
plt.imshow(Grey_Image, cmap='gray')
plt.title("GreyScale")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/GreyScale.png")

_,Binary_Image = cv2.threshold(Grey_Image, 127, 255, cv2.THRESH_BINARY)
Fig4 = plt.figure() 
plt.imshow(Binary_Image, cmap='gray')
plt.title("Binary")
plt.axis("off")
plt.tight_layout()

plt.savefig("Results/Binary.png")

HSV_Image_BGR = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2HSV)
HSV_Image = cv2.cvtColor(HSV_Image_BGR, cv2.COLOR_BGRA2RGB)
Fig5 = plt.figure() 
plt.imshow(HSV_Image)
plt.title("HSV")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/HSV.png")

CIELAB_Image_BRG = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2LAB)
CIELAB_Image = cv2.cvtColor(CIELAB_Image_BRG, cv2.COLOR_BGRA2RGB)
Fig6 = plt.figure() 
plt.imshow(CIELAB_Image)
plt.title("CIELAB")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/CIELAB.png")

HLS_Image_BGR = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2HLS)
HLS_Image = cv2.cvtColor(HLS_Image_BGR, cv2.COLOR_BGRA2RGB)
Fig5 = plt.figure() 
plt.imshow(HLS_Image)
plt.title("HLS")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/HLS.png")

# %%
#2.3 On the HSV converted image, normalize the lighting by performing histogram equalization across the V (value) channel.

H_Channel, S_Channel, V_Channel = cv2.split(HSV_Image)
V_Equalized = cv2.equalizeHist(V_Channel)

HSV_Normalized = cv2.merge([H_Channel, S_Channel, V_Equalized])
Fig6 = plt.figure() 
plt.imshow(HSV_Normalized)
plt.title("HSV_Normalized")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/HSV_Normalized.png")

Normalized_RGB = cv2.cvtColor(HSV_Normalized, cv2.COLOR_HSV2BGR)
Fig7 = plt.figure() 
plt.imshow(Normalized_RGB)
plt.title("HSV_Normalized_RGB")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/HSV_Normalized_RGB.png")

























