# RoadEye

## Description

A computer vision program that differentiates cars and bikes from the traffic in the video file, using only OpenCV and NumPy for image processing. Different training algorithms are provided in the comments of the `train.py` file for you to try out. 

## Process

In summary:

- Tidy the data
    - read video and cancel background from moving objects
    - select the targeted moving objects
- Train
- Run and Test!

### Step 1: Read video file and cancel background

Used the KNN segmentation background cancellation object provided by OpenCV and converted the color space of the frame to YCrCb. Then applied the BackgroundSubtractorKNN object to the frame, obtaining a binary mask where moving objects are highlighted. Also applied median filtering to the binary mask to reduce noise.

![Image 1](md_assets/background%20cancel.png)
*Moving objects are marked white and static is black*

## Step 2: Select the export the correct objects in the video

Find each highlighted moving object that is bigger than 100 pixels and export the images as raw images.

### Subheading 2.1

![Image 2](https://example.com/image2.png)
*Image Description 2: A cute cat with big eyes.*

### Subheading 2.2

- [Link 1](https://example.com/link1) - This is a link to a website.
- [Link 2](https://example.com/link2) - Another link with a different URL.

## Heading 3

![Animated GIF](https://example.com/animation.gif)
*GIF Description: An animated GIF demonstrating a funny dance.*

### Subheading 3.1

This is a paragraph with indented text. Ut sed elit eu neque tempus congue eu at odio. Sed tempus, erat non ultrices bibendum, justo est rhoncus ipsum, eu laoreet elit neque sit amet quam.

### Subheading 3.2

![Image 3](https://example.com/image3.jpg)
*Image Description 3: A colorful abstract artwork.*

## Conclusion

In this template, we've included headings and subheadings to organize content effectively. We used bullet points for listing items, and paragraphs with indented text to provide additional information. Additionally, we added images with descriptions, a GIF, and href links to external websites.

Feel free to customize this template for your own needs!