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

**2.1.**  Image statistics 
In this stage, we extract the **blue, green, and red channels** from the image, calculate the requested statistics for each channel (including minimum, maximum, mean, median, skewness, range, standard deviation, variance, and mode), visualize the results for each channel, organize the calculated data into a Pandas DataFrame, and use Matplotlib to generate a plot displaying a heatmap of the channel intensity alongside a clearly formatted data table.

<img width="640" height="480" alt="Statics_Channels" src="https://github.com/user-attachments/assets/36be6a18-baa5-4b6a-860d-02a5105ed8b2" />


  2.  Convert and save the image to greyscale, binary, and different color spaces (HSV, CIELAB, and HLS).
  3.  On the HSV converted image, normalize the lighting by performing histogram equalization across the V (value) channel.
  4.  Convert the normalized image back to RGB and save it.
  5.  You should now have 7 images.
  6.  Perform random affine transformations on each image (you should perform 14 total transformations - 2 for each image). Affine transformations can be translation, rotation, scaling, or shear as long as each is unique in either transformation type or transformation value (rotate 90 degrees vs rotate 186 degrees). No two images should be transformed in the exact same way. Save each of those images to new files.
  7.  You should now have 21 images.
  8.  Apply a Gaussian blur to each image using the levels of sigma: 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5. Discuss how the level of sigma changes the image. Save each of those images to new files.
  9.  You should now have 168 images.

---

Part 3: You decide that detecting the edges of the unknown figure would be useful, so you do the following: 

  1.  Randomly create 4 equally sized subsets of the images from part 1.

    Each subset should have 42 images.

  2.  Choose a subset to use in the remaining steps.

  3.  You should now have 42 images.
    
  4.  Perform these edge detection techniques on that subset:

    a.  Sobel
    b.  Laplacian
    c.  Canny
    d.  Prewitt

  5.  Discuss the pros and cons of each edge detection technique and perform an analysis of which of these techniques works best for this image set.

    Reminder – Canny may be the most used and applied, but it may not be the best in your case. Make sure your analysis fits your results.
    
  6.  Save each image before and after adding edges with each technique.
     
  7.  You should now have 210 images.
  
  8.  Create 42, 5-image plots of the input image (from the start of part 3) next to the edge-detected images and output 6 random plots to add to the readme. Include information on what processing techniques were used on the images. Your plots should look similar to this:

<img width="1425" height="1483" alt="image" src="https://github.com/user-attachments/assets/8059bb6e-c001-4bc0-94d0-3f9ae71e8844" />

---

Part 4: You officially get bored with this and go back to your actual job…..after watching a few dozen YouTube videos. 


**Submit your github repository link on BB.**

---
  
**[HOMEWORK ONE IMAGE DOWNLOAD](https://wichitaedu-my.sharepoint.com/:i:/g/personal/u577g584_wichita_edu/IQDhM0PY2yapTI1qxl_aPAHKAVPzCgBXEmIK3u-yQR3VP2I?e=NULzW5)**

<img width="1017" height="555" alt="image for homework 1" src="https://github.com/user-attachments/assets/1920f37b-f2b0-4816-88d0-d3e339a8df3d" />
