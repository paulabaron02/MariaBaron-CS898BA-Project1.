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

## Part 2: Image Preprocessing & Multi-Channel Normalization

For the first part of the second assignment, we use the same image as in the previous task; the code performs channel-based color normalization to enhance the contrast of the alien image. 

First, the image is separated into its three independent RGB channels using the `cv2` library's `split` function, with each channel saved individually. Next, histogram equalization is applied to each channel separately using `cv2.equalizeHist`, thereby boosting the contrast and illumination of each color component. 

Finally, the three enhanced channels are recombined into a single, fully normalized color image, which is saved as the master file for subsequent project stages. However, in the book *Mastering OpenCV 4 with Python* by Alberto Fernández Villán, the authors note that "Equalizing the three channels is not a good approach because the color shade changes dramatically." Instead, they propose a better method: converting the BGR image to a color space that includes a luminance or intensity channel (such as YUV, Lab, HSV, or HSL) and then performing equalization on that channel.

---

## Part 3: Threshold-Based Segmentation

For this part of the task, two thresholding segmentation techniques are applied to separate the alien from the background using the previously normalized image. First, the image is converted to grayscale and the global Otsu method is applied; this automatically calculates the optimal overall intensity threshold to create a binary mask. Second, Adaptive Thresholding (Gaussian) is applied, analyzing illumination in small image blocks to recover details in areas with local shadows. Finally, the program uses these masks to "cut out" and extract the original alien using the `cv2.bitwise_and` function, saving both the black-and-white masks and the results with the background removed.

---

## Part 4: Classical & Optimization-Based Segmentation

For optimization-based segmentation, first convert the image to HSV. According to the chapter "Machine Learning with OpenCV" in the book *Mastering OpenCV4 with Python*, "the k-means clustering algorithm is used for color quantization; in this process, each data element consists of three features corresponding to the B, G, and R values ​​of each pixel. Therefore, a key step is transforming the image into data" specifically by using `reshape` and `float32` to obtain a list of pixel coordinates for the algorithm to process. Next, a `for` loop tests three different values ​​of K (3, 4, and 5); in each iteration, K-Means automatically groups pixels with similar colors and replaces them with the group's average color (the centroid). Finally, the image is reconstructed to its original shape, converted back to BGR, and the three segmented results are saved so you can compare which K-value best separates the alien from its surroundings.

Based on the results, K=4 (shown below) was selected because the alien retains a uniform appearance, the grass has a distinct tone, and the houses also appear to belong to separate groups.

<img width="2816" height="1536" alt="Part4_K4_Segmented" src="https://github.com/user-attachments/assets/ec58e864-b705-4625-b59a-436e1b03bcfc" />

The code fixes K=4 as the optimal value, recalculates the groups, and independently generates four binary masks and four background extractions (one for each color cluster); however, it fails to completely isolate the distinct elements of the scene. 

Among the results, the first option offers the best visualization—despite the issues—because the alien's full figure is more clearly visible, even though the houses in the background are still heavily emphasized.
<img width="2816" height="1536" alt="Part4_Cluster_2_Mask" src="https://github.com/user-attachments/assets/c7741e45-7720-452a-b2e9-700fb48954a4" />

The second option provides a good view of the alien but shows too much of the grass. Finally, I saved all the clusters into the "results 2" folder as individual image files

<img width="2816" height="1536" alt="Part4_Cluster_0_Mask" src="https://github.com/user-attachments/assets/fb4b775a-b1ea-4545-849f-937cd637aeb1" />

---

## Part 5: Evaluation and Analysis

## Part 5.1 Qualitative analysis

1. Otsu's global thresholding

Advantages: It is simpler; it separates bright foreground regions from the darker background and produces a clean mask with defined edges in high-contrast areas.

Disadvantages: Several background regions (houses, lights, and grass) are incorrectly classified as foreground; parts of the figure are lost due to shadows and variations in luminosity.

2. Adaptive thresholding

Advantages: It handles local lighting changes better than Otsu's method, preserves more details of the unknown figure, and detects body contours even in the darkest areas of the image.

Disadvantages: It generates significant background noise; grass texture and small objects are treated as foreground pixels.

3. K-Means clustering (HSV, K = 4)

Advantages: It uses color information instead of relying solely on pixel intensity.
Cluster 2 captures the majority of the unknown figure and reduces background interference.

Disadvantages

Some background regions remain within the selected cluster, Noise persists because the original image exhibits considerable grain in low-light conditions.

Effect of multi-channel normalization

Applying histogram equalization independently to the R, G, and B channels significantly improved the overall image contrast prior to segmentation.

Compared to the original image from the first task:

- The figure became more distinguishable from the background.
- Dark areas gained detail.
- Color differences were accentuated, allowing the K-Means method to generate more meaningful clusters.
- Thresholding methods detected more object edges and contours. However, equalization also amplified image noise, making adaptive thresholding particularly sensitive to grass texture and background details.

Overall, multi-channel normalization improved segmentation performance, particularly for the color-based K-Means approach.

5.2. **Quantitative Comparison (Pseudo-Ground Truth):**

To begin, I load a reference mask that I created manually using editing software; in this mask, the figure to be isolated the alien is white, while the background is black. This serves as the ideal "ground truth," allowing the precision of the methods to be calculated using two mathematical metrics: IoU (which measures mask overlap or intersection) and Dice (which measures overall similarity). The program organizes these values ​​into a table and saves it as an image. Finally, it generates a visual grid using Matplotlib that displays the original image, the normalized image, the ideal reference mask, and the three black-and-white segmentation results.

<img width="1777" height="718" alt="Part5_Quantitative_Comparison_Table" src="https://github.com/user-attachments/assets/3729d8d7-019c-4844-bf71-c7215cf532c6" />

     Otsu produced the highest IoU and Dice score, meaning it had the greatest overlap with the manually created reference mask. However, all three methods produced relatively low scores because the outdoor scene contains uneven lighting, shadows, grass texture, and bright background structures. These factors caused the segmentation methods to include background pixels or miss parts of the central figure.

3. **Visualization:**
   * Create a multi-image comparison plot displaying the original image, the multi-channel normalized color image, and the 4 final segmented masks side-by-side. Include this plot in your updated `README.md`.

<img width="4470" height="2166" alt="Part5_Visualization_Comparison" src="https://github.com/user-attachments/assets/ee3319b4-f5fc-4ffd-adb0-3ce2e302208a" />


---

## Part 6: Submission

**Submit your updated GitHub repository link on BB.** Ensure your master/main branch or pull request clearly reflects the additions made for Homework Two.
