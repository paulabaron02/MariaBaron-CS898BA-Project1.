Homework One 

CS 898BA – Image Analysis and Computer Vision 

Maria Paula Baron Rodriguez

**Wsu ID:** J858Q278

**Purpose:** To apply basic image analysis and processing techniques. 

This script is the same one the professor provided for the assignment, but modified to display the results, the setup, and the execution of the steps.

**Used Libraries** 
- Cv2
- Matplotlib.pyplot
- Pandas
- Numpy
- Scipy.stats

**2.1.**  Image statistics.

In this stage, we extract the **blue, green, and red channels** from the image, calculate the requested statistics for each channel (including minimum, maximum, mean, median, skewness, range, standard deviation, variance, and mode), visualize the results for each channel, organize the calculated data into a Pandas DataFrame, and use Matplotlib to generate a plot displaying a heatmap of the channel intensity alongside a clearly formatted data table.

<img width="640" height="480" alt="Statics_Channels" src="https://github.com/user-attachments/assets/36be6a18-baa5-4b6a-860d-02a5105ed8b2" />


  **2.2.** Greyscale, binary, and different color spaces (HSV, CIELAB, and HLS).
  
For this part of the course, the code transforms the image's color spaces. First, it converts the image to grayscale and applies a binary threshold; this turns almost the entire scene black—since the original photograph is very dark—while preserving only the bright lights of the houses.

  **2.3.**  Histogram equalization across the V (value) channel.
  
Next, the lighting is normalized by isolating the V (brightness) channel from the HSV color space and applying histogram equalization to brighten dark areas and reveal hidden details in the image.

  **2.4.**  Convert the normalized image back to RGB and save it.
  
  The result of the imagen in RGB is clearly more visible 
  
  <img width="640" height="480" alt="HSV_Normalized_RGB" src="https://github.com/user-attachments/assets/5c8e00df-60f1-469b-9ec8-159279de1241" />


  **2.5.**  The Results 7 images.
  
   The results of the previous parts are in the folder called results and they correpond to the files named 
   - Binary
   - CIELAB
   - GreyScale
   - HLS
   - HSV
   - HSV_Normalized
   - HSV_Normalized_RGB
     
**2.6.**  Perform random affine transformations on each image (you should perform 14 total transformations - 2 for each image). Affine transformations can be translation, rotation, scaling, or shear as long as each is unique ineither transformation type or transformation value (rotate 90 degrees vs rotate 186 degrees). No two images should be transformed in the exact same way. Save each of those images to new files.

* Rotation: Rotates the image by a random angle (between 15 and 180 degrees) while slightly changing its size (applying a slight zoom-in or zoom-out effect).
* Translation: Shifts or moves the image sideways, up, or down using random coordinates. Any empty spaces resulting from the movement are filled with black borders.

 **2.8.**  You should now have 21 images.
 
  The results of the previous parts are in the folder called results and they correpond to the files named 
   - Original_Rotation, Original_Traslation
   - Binary_Rotation, Binary_Traslation
   - CIELAB_Rotation, CIELAB_Traslation
   - GreyScale_Rotation, GreyScale_Traslation
   - HLS_Rotation, HLS_Traslation
   - HSV_Rotation, HSV_Traslation
   - HSV_Normalized_RGB_Rotation, HSV_Normalized_RGB_Traslation
  
  **2.9.**  Apply a Gaussian blur to each image using the levels of sigma: 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5. Discuss how the level of sigma changes the image. Save each of those images to new files.
     
In this step, we take all the images saved in the results folder (21 images in total) and apply a Gaussian blur filter using seven different intensity levels, defined by the Sigma ($\sigma$) value. The program iterates through each image in the folder and, for each Sigma level, generates a new blurred version, automatically saving it with the Sigma value included in the filename. It is evident that at lower Sigma values, the image retains most of its fine details and sharp edges, whereas as the value increases, small details are completely lost, and the alien's silhouette becomes soft and diffuse.

  **2.10.**  You should now have 168 images.
  
  The results of the previous parts are in the folder called results and they correpond to the files named 
   - Original_GaussianBlur_Sigma_(0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5.), Seven Version of this picture 
   - Binary_GaussianBlur_Sigma_(0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5.), Seven Version of this picture 
   - CIELAB_GaussianBlur_Sigma_(0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5.), Seven Version of this picture 
   - GreyScale_GaussianBlur_Sigma_(0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5.), Seven Version of this picture 
   - HLS_GaussianBlur_Sigma_(0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5.), Seven Version of this picture 
   - HSV_GaussianBlur_Sigma_(0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5.), Seven Version of this picture 
   - HSV_Normalized_RGB_GaussianBlur_Sigma_(0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5.), Seven Version of this picture 
---
**3.1.** Randomly4 equally sized subsets of the images.

In this step, all images from the "results" folder are taken, shuffled completely at random, and divided into four equal-sized subsets; the first group is then assigned to `My_Subset` for later use.

**3.2.**  Choose a subset to use in the remaining steps.
 
 The variable called My_subset
 
**3.4.**  Perform these edge detection techniques on that subset:
    a.  Sobel
    b.  Laplacian
    c.  Canny
    d.  Prewitt
    
Since there are already many images in the results folder, we create a new subfolder named `Edge_Detection` and apply the four techniques required by the assignment; all processed versions are automatically saved in the new folder, named according to the respective technique.

**3.5** Discuss the pros and cons of each edge detection technique and perform an analysis of which of these techniques works best for this image set.

I believe it is difficult to generalize across all images; however:

- Sobel: This one successfully detected the main outlines of some figures—primarily those with more colors. However, the resulting lines are quite thick and include some texture, which can be helpful depending on the image.

- Laplacian: This method detected intensity changes, but the resulting image showed very faint edge responses. Due to the original image's low lighting, it was difficult to distinguish many important elements. This method provided the least effective visual separation between the figure and the background.

- Canny: Performed the best, producing the cleanest and most well-defined lines. The silhouettes of the alien and the houses are clearly visible, and—best of all—it eliminated almost all the background "noise" and dark spots. As a result, the output is very easy to interpret and highlights only the most important features of the image.

- Prewitt: The results very similar to Sobel. It did manage to outline the alien and the houses in some of the more colorful images, but the lines appear blurrier, and more background "noise" or spotting remained. While it works well, the result is nowhere near as sharp or defined as that of the Canny method.

I believe that applying these methods after already using CIELAB complicates image visualization. However, it's clear that the descriptions I've given don't generalize, because in my opinion, Laplacian works better for CIELAB; even though it's blurry, I can see more.
    
**3.7**  You should now have 210 images.

this images These images are in the edge detection folder created earlier.
  
**3.8**  5-image plots of the input image 

There is another folder called "plot" where you can get a better view.

<img width="990" height="896" alt="Plot_033" src="https://github.com/user-attachments/assets/de8f953b-3583-423d-925a-79ee70109962" />
<img width="990" height="896" alt="Plot_029" src="https://github.com/user-attachments/assets/7daeb956-a23c-4107-b4d0-90d1d6cc64f2" />
<img width="990" height="896" alt="Plot_020 - Copy" src="https://github.com/user-attachments/assets/94118047-87ca-42fd-89cd-89ca380ca8ad" />
<img width="990" height="895" alt="Plot_013 - Copy" src="https://github.com/user-attachments/assets/8c1f41ce-f09b-40d9-86c1-9a2e8c617794" />
<img width="990" height="896" alt="Plot_004 - Copy" src="https://github.com/user-attachments/assets/a6370115-70b3-4783-9437-d8174bc26a2f" />
<img width="990" height="896" alt="Plot_058" src="https://github.com/user-attachments/assets/5bf39f0a-8c56-49a4-a8d1-2ce3986502b3" />
