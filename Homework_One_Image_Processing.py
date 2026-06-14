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
import random


plt.close('all')
#load the image
Image_Alien = cv2.imread(r"C:\Users\Paula\.spyder-py3\MariaBaron-CS898BA-Project1\MariaBaron-CS898BA-Project1\HW1_IMG_CS898BA.png")
Image_Alien_RGB = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2RGB)
plt.imshow(Image_Alien_RGB)
plt.title("Original")
plt.axis("off")
plt.tight_layout()
plt.show()
plt.savefig("Results/Original.png")

# %%
#2.1 Find and print basic image statistics of the original image for each 
#individual channel (min, max, average, median, mode, skew, range, standard
# deviation, variance)

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
#2.2 Convert and save the image to greyscale, binary, and different color 
#spaces (HSV, CIELAB, and HLS).
Results = r"C:\Users\Paula\.spyder-py3\MariaBaron-CS898BA-Project1\MariaBaron-CS898BA-Project1\Results"


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

HSV_Image = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2HSV)
HSV_Image_plt = cv2.cvtColor(HSV_Image, cv2.COLOR_BGR2RGB)
Fig5 = plt.figure() 
plt.imshow(HSV_Image_plt )
plt.title("HSV")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/HSV.png")

CIELAB_Image = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2LAB)
CIELAB_Imag_plt = cv2.cvtColor(CIELAB_Image, cv2.COLOR_BGR2RGB)
Fig6 = plt.figure() 
plt.imshow(CIELAB_Imag_plt)
plt.title("CIELAB")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/CIELAB.png")

HLS_Image = cv2.cvtColor(Image_Alien, cv2.COLOR_BGR2HLS)
HLS_Image_plt = cv2.cvtColor(HLS_Image, cv2.COLOR_BGR2RGB)
Fig5 = plt.figure() 
plt.imshow(HLS_Image_plt)
plt.title("HLS")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/HLS.png")

# %%
#2.3 On the HSV converted image, normalize the lighting by performing histogram
# equalization across the V (value) channel.

H_Channel, S_Channel, V_Channel = cv2.split(HSV_Image)
V_Equalized = cv2.equalizeHist(V_Channel)

HSV_Normalized = cv2.merge([H_Channel, S_Channel, V_Equalized])
HSV_Normalized_plt = cv2.cvtColor(HSV_Normalized, cv2.COLOR_BGR2RGB)
Fig6 = plt.figure() 
plt.imshow(HSV_Normalized_plt)
plt.title("HSV_Normalized")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/HSV_Normalized.png")

# %%
#2.4 Convert the normalized image back to RGB and save it.

Normalized_RGB = cv2.cvtColor(HSV_Normalized, cv2.COLOR_HSV2RGB)
Fig7 = plt.figure() 
plt.imshow(Normalized_RGB)
plt.title("HSV_Normalized_RGB")
plt.axis("off")
plt.tight_layout()
plt.savefig("Results/HSV_Normalized_RGB.png")

# %%
#2.6. Perform random affine transformations on each image (you should perform 14 
#total transformations - 2 for each image). Affine transformations can be 
#translation, rotation, scaling, or shear as long as each is unique in either 
#transformation type or transformation value (rotate 90 degrees vs rotate 186 
#degrees). No two images should be transformed in the exact same way. Save each
# of those images to new files.

Images_List = [
    ("Original", Image_Alien),
    ("Greyscale", Grey_Image),
    ("Binary", Binary_Image),
    ("HSV", HSV_Image),
    ("CIELAB", CIELAB_Image),
    ("HLS", HLS_Image),
    ("HSV_Normalized_RGB",  cv2.cvtColor(Normalized_RGB, cv2.COLOR_RGB2BGR))
]

for name, image in Images_List:
    
    height, width = image.shape[:2]
    
    # Rotation
    angle = np.random.randint(15, 180)
    scale = np.random.uniform(0.8, 1.2)
    
    Rotation_Matrix = cv2.getRotationMatrix2D( (width // 2, height // 2), angle, scale )
    Rotated_Image = cv2.warpAffine(image, Rotation_Matrix, (width, height))
    
    cv2.imwrite(os.path.join(Results, name + "_Rotation.png"),Rotated_Image)
    
    # Translation
    tx = np.random.randint(-1000, 500)
    ty = np.random.randint(-500, 200)
    
    Translation_Matrix = np.float32([[1, 0, tx],[0, 1, ty]])
    
    Translated_Image = cv2.warpAffine(image, Translation_Matrix, (width, height),borderMode=cv2.BORDER_CONSTANT,borderValue=(0, 0, 0))
    
    cv2.imwrite(os.path.join(Results, name + "_Translation.png"),Translated_Image)
# %%
# 2.8. Apply a Gaussian blur to each image using the 
#levels of sigma: 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5. 
#Discuss how the level of sigma changes the image. 
#Save each of those images to new files.

Sigma_Levels = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]

# Combine the 7 converted images and the 14 affine images

for Image_Gaussian in os.listdir(Results):
    
    Full_Path = os.path.join(Results, Image_Gaussian)
    
    image = cv2.imread(Full_Path, cv2.IMREAD_UNCHANGED)
    
    image_name = os.path.splitext(os.path.basename(Image_Gaussian))[0]
    
    for sigma in Sigma_Levels:
        
        Blurred_Image = cv2.GaussianBlur(image,(0, 0),sigmaX=sigma,sigmaY=sigma)
        
        cv2.imwrite(os.path.join(Results,  image_name + "_GaussianBlur_Sigma_" + str(sigma) + ".png"),Blurred_Image)


























