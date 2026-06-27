# Homework Two: Image Segmentation

CS 898BA – Image Analysis and Computer Vision 

Maria Paula Baron Rodriguez

**Wsu ID:** J858Q278

**Purpose:** To apply and evaluate classical and optimization-based image segmentation techniques.

This script is the same one the professor provided for the assignment, but modified to display the results, the setup, and the execution of the steps.

## Part 1: Repository Maintenance & Logistics

1. **Branching:** Do not overwrite your Homework One code. Create a new branch in your existing repository named `Feature-Segmentation`.
2. **AI Log:** Continue tracking all AI usage in your `AI_Log.md` file following the exact same format as Homework One.
3. **Commit Strategy:** Perform incremental commits with clear, professional messages as you complete each segmentation task.

---

## Part 1.1: Image Preprocessing & Multi-Channel Normalization

For the first part of the second assignment, we use the same image as in the previous task; the code performs channel-based color normalization to enhance the contrast of the alien image. 

First, the image is separated into its three independent RGB channels using the `cv2` library's `split` function, with each channel saved individually. Next, histogram equalization is applied to each channel separately using `cv2.equalizeHist`, thereby boosting the contrast and illumination of each color component. 

Finally, the three enhanced channels are recombined into a single, fully normalized color image, which is saved as the master file for subsequent project stages. However, in the book *Mastering OpenCV 4 with Python* by Alberto Fernández Villán, the authors note that "Equalizing the three channels is not a good approach because the color shade changes dramatically." Instead, they propose a better method: converting the BGR image to a color space that includes a luminance or intensity channel (such as YUV, Lab, HSV, or HSL) and then performing equalization on that channel.

---

## Part 3: Threshold-Based Segmentation

Using the normalized color image produced in Part 2, implement the following baseline techniques using OpenCV:

1. **Otsu’s Global Thresholding:**
   * Convert your normalized color image to grayscale.
   * Apply Otsu's automatic thresholding to separate the foreground object from the background.
2. **Adaptive Thresholding:**
   * Apply adaptive thresholding (Gaussian window) to the grayscale version of your normalized image to handle local illumination variations.

*Save the resulting binary masks and the segmented foreground extractions for both methods.*

---

## Part 4: Classical & Optimization-Based Segmentation

To handle the complex textures and shadows of the outdoor scene, move beyond simple pixel intensities. Use the fully normalized color image from Part 2 as the input for these methods:

1. **Color-Space Clustering (K-Means):**
   * Convert the normalized color image to the HSV color space.
   * Apply K-Means clustering to segment the image into $K$ distinct regions (test and select an optimal $K$ value between 3 and 5). 
   * Isolate the cluster that most closely captures the "unknown figure."

*Save the resulting binary masks and the segmented foreground extractions for both methods.*

---

## Part 5: Evaluation and Analysis

You now have 3 distinct segmentation outputs (Otsu, Adaptive, and K-Means).

1. **Qualitative Analysis:**
   * Discuss the pros and cons of each approach regarding background noise (e.g., leaves, porch structures) and edge preservation of the central figure. Specifically note how color normalization across all three channels impacted the final segmentation compared to the raw image results from Homework One.
2. **Quantitative Comparison (Pseudo-Ground Truth):**
   * Manually create or define a clean reference mask of the "figure" to serve as your ground truth.
   * Calculate and print the **Intersection over Union (IoU) / Jaccard Index** and the **Dice Coefficient** for each of the 3 segmentation methods against your reference mask.

$$IoU = \frac{|A \cap B|}{|A \cup B|}$$

3. **Visualization:**
   * Create a multi-image comparison plot displaying the original image, the multi-channel normalized color image, and the 4 final segmented masks side-by-side. Include this plot in your updated `README.md`.

---

## Part 6: Submission

**Submit your updated GitHub repository link on BB.** Ensure your master/main branch or pull request clearly reflects the additions made for Homework Two.
