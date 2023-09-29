---
title: Lab 5 -- Introduction to Spatial Filtering in C/C++: Application to sharpening.
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision
date: Week 5
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

# Introduction to Spatial Filtering in C/C++: Application to sharpening

We'll create three programs today. They all rely on `rgb2grey.cxx` that we wrote last time. I suggest that you put all the code in the same folder at last lab.

## Contents

1. [Gaussian filtering](#2-gaussian-filtering)
2. [Image sharpening](#2-image-sharpening)
<!-- 3. [Edge detection](#3-edge-detection) -->

# 1. Gaussian filtering

Answer the following questions in your lab report:

- Is a Gaussian filter a point operator?
    - YES/NO

- Is a Gaussian filter a linear filter?
    - YES/NO

- Is a Gaussian filter a convolution filter?
    - YES/NO

- Explain in your own terms the main difference(s) between a point operator and a convolution filter.



## Imaging pipeline:

- Open an image
- Convert it to greyscale (keep it as unsigned byte)
- Filter it with a Gaussian filter (you may adjust the radius of the filter)
- Save the output image
- Display the output image

## Preliminaries

1. Copy `rgb2grey.cxx` into `gaussianFilter.cxx`.
    - Make sure you update your preamble to change the date and the purpose of the file.
2. Edit `CMakeLists.txt` to add the new program.
    - You have to add three lines:

```cmake
ADD_EXECUTABLE (gaussianFilter   gaussianFilter.cxx)
TARGET_INCLUDE_DIRECTORIES(gaussianFilter PUBLIC ${OpenCV_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES (gaussianFilter   ${OpenCV_LIBS})
```

## Filter the greyscale image with a fixed kernel radius

The function we will use is

```cpp
void cv::GaussianBlur 	( 	InputArray  	src,
		OutputArray  	dst,
		Size  	ksize,
		double  	sigmaX,
		double  	sigmaY = 0,
		int  	borderType = BORDER_DEFAULT
	)
```

- It is declared in `<opencv2/imgproc.hpp>`. Make sure you include this file at the top of your file when you included the other headers.
Now, look at the parameters of the function.
You may have noticed a pattern: the 1st parameter is often the input image, and the 2nd parameter is often the output image.

Parameters:

- `src`	input image; the image can have any number of channels, which are processed independently, but the depth should be `CV_8U`, `CV_16U`, `CV_16S`, `CV_32F` or `CV_64F`.
- `dst`	output image of the same size and type as `src`.
- `ksize`	Gaussian kernel size. `ksize.width` and `ksize.height` can differ but they both must be positive and odd. Or, they can be zero's and then they are computed from sigma.
- `sigmaX`	Gaussian kernel standard deviation in X direction.
- `sigmaY`	Gaussian kernel standard deviation in Y direction; if `sigmaY` is zero, it is set to be equal to `sigmaX`, if both sigmas are zeros, they are computed from `ksize.width` and `ksize.height`, respectively (see [`getGaussianKernel`](https://docs.opencv.org/4.5.3/d4/d86/group__imgproc__filter.html#gac05a120c1ae92a6060dd0db190a61afa) for details); to fully control the result regardless of possible future modifications of all this semantics, it is recommended to specify all of `ksize`, `sigmaX`, and `sigmaY`.
- `borderType`	pixel extrapolation method, see [`BorderTypes`](https://docs.opencv.org/4.5.3/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5). [`BORDER_WRAP`](https://docs.opencv.org/4.5.3/d2/de8/group__core__array.html#gga209f2f4869e304c82d07739337eae7c5a697c1b011884a7c2bdc0e5caf7955661) is not supported.

- For our application, we can use `grey_image` as both the input and output.
- Declare a variable, `filter_radius`, that is an integer (`int`). Initialise it to 1.
- The kernel size is `1 + 2 * filter_radius`.
    - If the radius is 1, the kernel size is 3x3;
    - If the radius is 2, the kernel size is 5x5;
    - If the radius is 3, the kernel size is 7x7; and
    - If the radius is 7, the kernel size is 15x15.
- To filter our image, just use:

```cpp
cv::GaussianBlur(grey_image,
                 grey_image,
                 Size(1 + 2 * filter_radius, 1 + 2 * filter_radius),
                 0);
```
after the conversion to greyscale and before saving and displaying the image.
- Compile and test your code.
- **In your report, include evidence of testing, e.g. filtering two different images.** (note that you must show the original images in greyscale if you want to prove it has been blurred using your program)


## Update the command line

- Once it works, let's make our program more flexible. We want to be able to change the radius via the command line.
- `argc` must be equal to 3 or 4, with:
    - `argv[0]` the program
    - `argv[1]` the input file
    - `argv[2]` the output file
    - `argv[3]` an optional parameter controlling the kernel radius
- Update the error check accordingly (`if (argc != 3)` becomes `if (argc != 3 && argc != 4)`)
- Update the error message.
- After the initialisation of `filter_radius`, and before the application of the Gaussian filter, update the value of `filter_radius` if `argc` is equal to 4. To convert `argv[3]` into an integer, we can use the `atoi` function declared in `<cstdlib>` (don't forget to include the header file).
- Compile and test your code.
- **In your report, include the code of your program and evidence of testing, e.g. filtering an image with various filter radius.** (again add the original images in greyscale)

# 2. Image sharpening

## Imaging pipeline:

- Open an image (`image`)
- Filter it with a Gaussian filter (`blur_image`) (you may adjust the radius of the filter)
- Subtract the new image from the original image (image of the details) (`details_image = image - blur_image`) (the subtraction must allow negative numbers to be saved)
- Multiply the image of details (`details_image`) with a constant number (`alpha`)
- Add the resulting image to the original image (`sharpen_image = image + alpha * details_image`)
- Clamp the pixel values to preserve the same dynamic range as the input image
- Convert the data in unsigned byte
- Display the output image
- Save the output image


## Preliminaries

1. Copy `rgb2grey.cxx` into `sharpen.cxx`.
    - Make sure you update your preamble to change the date and the purpose of the file.
2. Edit `CMakeLists.txt` to add the new program.
    - You have to add three lines:

```cmake
ADD_EXECUTABLE (sharpen   sharpen.cxx)
TARGET_INCLUDE_DIRECTORIES(sharpen PUBLIC ${OpenCV_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES (sharpen   ${OpenCV_LIBS})
```

3. Get rid of the code on the greyscale conversion, it's redundant. I just want to keep the skeleton of the program, including how the command line is processed.

4. Declare the new variables that we'll need:

```cpp
int filter_radius = 1;
int alpha = 1;
Mat sharpen_image;
```

5. Replace `grey_image` with `sharpen_image` when you display and save the output image.

6. Compile your code until it's free of errors.

## A new function to sharpen an image

1. We'll declare a new function `sharpen`. It has 3 parameters: an input image, a filter radius and alpha.
It returns the output image.
```cpp
Mat sharpen(const Mat& anInputImage, int aFilterRadius, int anAlphaValue)
```
Make sure it is declared after the header inclusion and after `using namespace...`.

2. Back to the main function, before you write and display the output image, call `sharpen` with the appropriate parameters (e.g. `sharpen_image = sharpen(image, filter_radius, alpha);`).

3. Add an empty definition of the function (I tend to add them after the `main` function):

```cpp
Mat sharpen(const Mat& anInputImage, int aFilterRadius, int anAlphaValue)
{
    Mat sharpen_image;


    return sharpen_image;
}
```

4. Compile your code until it's free of errors.

5. In the `sharpen` function, filter `anInputImage` with a Gaussian filter of appropriate filter size, just like we did in the previous program. Save the blurry image in `blur_image` (don't forget to declare it).

6. Convert `blur_image` and `anInputImage` in floating-point number:

```cpp
Mat blur_image_32;
blur_image.convertTo(blur_image_32, CV_32F);

Mat input_image_32;
anInputImage.convertTo(input_image_32, CV_32F);
```

7. Compile your code until it's free of errors.

8. Create the image of details (`Mat details_image = input_image_32 - blur_image_32;`).

9. Add the details to the input image:

```cpp
sharpen_image = input_image_32 + anAlphaValue * details_image;
```

10. Compile your code until it's free of errors. When you run your code, if you see and save a weird image, mostly white, then it's fine.

11. Clamp the pixel values within the range [0-255] and convert the data to unsigned char with `sharpen_image.convertTo(sharpen_image, CV_8UC3);`

12. Compile your code until it's free of errors and test it with different images.

13. **In your report, include evidence of testing, e.g. sharpening two different images.** (note that you must show the original images if you want to prove it has been sharpened using your program)

14. To further increase your mark, change the way the command line argument works to support two additional parameters:
    - `argv[3]` an optional parameter controlling the kernel radius
    - `argv[4]` an optional parameter controlling alpha.
    - **In your report, include evidence of testing, e.g. sharpening an image with different combination of radius and alpha.** (note that you must show the original image and you must state what the radius and alpha values are)

15. Include the listing of `sharpen.cxx` in your report.


## Don't forget

To complete the lab report and to submit it.
