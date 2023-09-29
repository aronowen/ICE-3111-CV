---
title: Lab 3 -- Introduction to OpenCV in C/C++ and Python, and Point Operators.
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision
date: Week 3
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

# Instructions in Python

## Contents

2. [Load an image](#2-and-3-load-and-display-an-image)
3. [Display an image](#2-and-3-load-and-display-an-image)
4. [Convert a RGB image in a greyscale image](#4-convert-a-rgb-image-in-a-greyscale-image)
5. [Find the smallest and largest pixel values in an image](#5-find-the-smallest-and-largest-pixel-values-in-an-image)
6. [Improve the contrast of an image:](#6-improve-the-contrast-of-an-image)
    1. [by hand using the equation seen in the lecture](#by-hand-using-the-equation-seen-in-the-lecture)
    2. [using OpenCV's function](#using-opencvs-function)
<!-- 7. [Change the dynamic range using a log transform](#7-change-the-dynamic-range-using-a-log-transform)
8. [Blend two images in a for loop to create an animation](#8-blend-two-images-in-a-for-loop-to-create-an-animation) -->

## 2. and 3. Load and display an image

Before we start, the technical documentation is available at: [https://docs.opencv.org/4.5.4/index.html](https://docs.opencv.org/4.5.4/index.html). The OpenCV's functions we will use are:

```cpp
imread() // To read an image from a file
imshow() // To display an image in a window
```
Both functions are available in C, C++ and Python. Find them in the online documentation and read the corresponding text. I often consult the documentation when I forget the name of a function or when I need to find the right sequence of parameters. This is what I get:

```Python
cv2.imread( filename[, flags] ) -> 	retval

cv2.imshow( winname, mat ) -> 	None
```

### Our first OpenCV program

1. Create a new file (`displayImage.py`). Make sure the file extension is correct. MS Windows tend to hide them. **If you are using MS Windows, make sure you show the file extensions in the file explorer!**.

2. Open the `displayImage.py` in your favourite text editor.

3. Add the shebang line (useful for Unix computers).

```bash
#!/usr/bin/env python3
```

4. Add a preamble.

Using Python comments, add a preamble at the top of your file.
It must describe the program:

    1. the author of the program (you),
    2. the date,
    3. the purpose of the file (inc. the command line options),
    4. the todo-list if anything is missing.

5. Package inclusion

```python
import sys # to read the command line arguments
import cv2 # cv2 library
import numpy as np # numpy library
```

6. Create the `NoneType`. It is useful when checking errors.

```python
NoneType = type(None)
```

7. Arguments of the Command Line

The first program only takes one parameter. It corresponds to the path
of an image file. To make sure the number of arguments is correct, we use:

```python
# Check the command line, do we have two arguments?
# argv[0] is always the executable file
# In our case argv[1] should be the name of an image file
if len(sys.argv) != 2:
    # Create an error message
    error_message  = "usage: "
    error_message += sys.argv[0]
    error_message += " <input_image>"

    # Throw an error
    raise Exception(error_message)
```

If there was no error, you can use to get the file name:

```python
input_filename = sys.argv[1]
```

8. Reading the File

In OpenCV 4, the image is loaded using:

```python
# Open and read the image
image = cv2.imread( input_filename )
```

It is a good practice to check if any error occurred, e.g. to avoid
unspecified behaviours and crashed. If the image is not loaded, `cv2.imread` returns `None`.
`data` field is empty. If it is the case we can throw an error as
follows:

```python
# The image has not been loaded
if isinstance(image, NoneType):
    # Create an error message
    error_message  = "Could not open or find the image \""
    error_message += input_filename
    error_message += "\"."

    # Throw an error
    raise Exception(error_message)
```

9. Displaying the Image

There are four steps to create a window and display and image:

    1.  Create a string to contain the window title (it is used to identify
        the window);
    2.  Create the window;
    3.  Show the image in the window;
    4.  Wait for a user input to leave the window.

It can be done as follows:

```python
# Create a string to contain the window title
window_title  = "My OpenCV Display \""
window_title += input_filename
window_title += "\""

# Create the window
cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)

# Show the image in the window
cv2.imshow(window_title, image)

# Wait for a user input to leave the window
cv2.waitKey(0)
```

The program is now complete. You run it with
different image files to test it.
In your lab report, you must include a listing of your program and put three screenshots (with three different images).


## 4. Convert a RGB image in a greyscale image.

1. Copy paste your previous program in a new one that you call `rgb2grey.py`.

2. The command line is:

```bash
rgb2grey.py  input_filename  output_filename
```

Change the code appropriately.

```python
# Check the command line, do we have three arguments?
# argv[0] is always the executable file
# In our case argv[1] should be the name of an input image file
# In our case argv[2] should be the name of an output image file
if len(sys.argv) != 3:
    # Create an error message
    error_message  = "usage: "
    error_message += sys.argv[0]
    error_message += " <input_image>"
    error_message += " <output_image>"

    # Throw an error
    raise Exception(error_message)

input_filename = sys.argv[1]
output_filename = sys.argv[2]
```

Make sure you change the `2` into `3`, and that you retreive filename of the output image (`argv[2]`).
In future, I may not provide the same level of guidance for this task as I will assume it is something you know now.

3. After you read the image and checked that the image was loaded, and before displaying the image, convert it into a greyscale image:

```python
grey_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
```

4. Don't forget to display the right image, i.e. `grey_image` not `image`. `imshow` will take care of the change of pixel type (RGB->greyscale).

5. Save the image

The function to save an image is `cv2.imwrite(file_name, image)`. It
returns true if the file has been successfully written; false otherwise.
We can use the return value to handle possible errors:

```python
# Write the image
if not cv2.imwrite(output_filename, grey_image):
    # The image has not been written

    # Create an error message
    error_message  = "Could not write the image \""
    error_message += output_filename
    error_message += "\"."

    # Throw an error
    raise Exception(error_message)
```

When you detect an error, it is good practive to throw an error. Again, I will assume from now on that you know how to do it.

The program is now complete. You run it with different image files to test it. In your lab report, you must include a listing of your program and put three screenshots (with three different images).

## 5. Find the smallest and largest pixel values in an image.

### Create a test image

- Choose an image of your choice.
- If it looks nice (i.e. has a good contrast/brightness in our case), we will make it dull, sorry.
- Open the image in ImageJ.
- Go to the menu `Image->Type` and choose `8-bits` to convert it to greyscale.
    - In the lab report, add the histogram of this image.
- In the menu `Process->Math`, choose `Divide`. Use `3` or `4`.
    - In the lab report, add the histogram of this new image.
    - See the histogram? You just altered the contrast. Ooops.
- In the menu `Process->Math`, choose `Add`. Use `25` or something along these lines.
    - In the lab report, add the histogram of this new image.
    - See the histogram? You just altered the brightness. Ooops.
- Save the image as a `TIFF` file.
- In the lab report, add a screenshot of this new image.

### OpenCV code

- To create the new program, copy paste `rgb2grey.py` into `contrastStretchingManual.py`.
- To retrieve the smallest and largest pixel values in `grey_image`, we will use
```python
	cv2.minMaxLoc(	src[, mask]	) -> 	minVal, maxVal, minLoc, maxLoc
```
We can use  it as follows:
`minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(grey_image)`
- After you called `minMaxLoc` with the appropriate parameters, output the value with something like:
```cpp
print("min value:",  minVal)
print("max value:",  maxVal)
```
- To test your program, run your program with your new test image.
- In your lab report, add a screenshot of the console with the output.
- Open test image with ImageJ. Go to the menu `Analyze -> Measure`.
- In your lab report, add a screenshot of the table from ImageJ that displays the min and max values.
- Are the values identical?

## 6. Improve the contrast of an image


### by hand using the equation seen in the lecture

You need to be familiar with the histogram stretching method we saw in the lecture. It's equation is

![Contrast stretching equation](https://github.com/effepivi/ICE-3111-Computer_Vision/raw/main/Labs/Lab-02/img/visualisation-eq.png)

In our case,

- `g` is a new `numpy.array` to store the new image,
- `f` is `grey_image`,
- *min(g) = 0*
- *max(g) = 255*
- *Tlow = minVal*
- *Thigh = maxVal*

- Remember `1 / 2 = 0`, and `1.0 / 2.0 = 0.5`. Due to the division, we *MUST* make sure floating-point divisions are used instead of integer division.
- For this purpose we must convert the numpy array that contains the image. It's the `astype` method:
```python
float_image = grey_image.astype(np.single)
```
- Now we can apply the equation:
    - Subtraction: `float_image -= minVal`
    - Division: `float_image /= maxVal - minVal`
    - Product: `float_image *= 255`
- Display `float_image` using `imshow`.
- Add a screenshot in your report.
- Why was the image (mostly) white?
    - Hint, look at [http://scikit-image.org/docs/dev/user_guide/data_types.html](http://scikit-image.org/docs/dev/user_guide/data_types.html) and find the corresponding data type.
    - For an image in floating-point numbers, by convention what is the value of white?
- We must convert the image from floating-point numbers to unsigned bytes (UINT8).
- Create a new image that you call `uint8_image`.
- Call `uint8_image = float_image.astype(np.uint8)`.
- Display `uint8_image` using `imshow`.
- Add a screenshot in your report.
- Alter the call to `imwrite` to save `uint8_image` into a file.

The program is now complete. You run it with your test image.
In your lab report, you must include a listing of your program.

### using OpenCV's function

- There is a function in OpenCV to perform the histogram stretching operation. It's called "min-max normalisation":

```python
cv2.normalize(	src, dst[, alpha[, beta[, norm_type[, dtype[, mask]]]]]	) -> 	dst
```

In our context, `alpha` is 255, and `norm_type` is `cv2.NORM_MINMAX`.

- To create the new program, copy paste `contrastStretchingManual.py` into `contrastStretchingCV.py`.

- Remove the code that you added for the histogram stretching. It includes the call to `cv::minMaxLoc` as it will done internally by `cv::normalize`. Remove all the variables that you no longer need.

- All we need to do is:

```cpp
float_image = np.zeros(grey_image.shape)
float_image = cv2.normalize(grey_image, dst=float_image, alpha=255, beta=0, norm_type=cv2.NORM_MINMAX)
uint8_image = float_image.astype(np.uint8)
```

The program is now complete. You run it with your test image.
In your lab report, you must include:

- a listing of your program,
- a screenshot of the new image after histogram stretching, and
- a screenshot of its histogram in ImageJ.

<!-- ## 7. Change the dynamic range using a log transform.

## 8. Blend two images in a for loop to create an animation. -->


## Don't forget

To complete the lab report and to submit it.

## Next time

We will use spatial filters to blur an image, find edges, etc.
