# Chapter 5 on Edge and line (and circle) detection

## Content

- notebooks
    - in C/C++:
        1. [Edge detection using the gradient magnitude](notebooks/1-Edge-detection-using-gradient-magnitude.ipynb)
        2. [Edge detection using the Canny operator](notebooks/2-Edge-detection-using-canny.ipynb)
        3. [Line detection using my own implementation of the Hough transform](notebooks/3-line-detection-using-hough-transform.ipynb)
        4. [Straightening an image using my own implementation of the Hough transform](notebooks/4-straighten-image-using-hough-transform.ipynb)
    - in Python:
        1. [Edge detection using the gradient magnitude](notebooks/1-python-Edge-detection-using-gradient-magnitude.ipynb)
        2. [Edge detection using the Canny operator](notebooks/2-python-Edge-detection-using-canny.ipynb)
        3. [Line detection using my own implementation of the Hough transform](notebooks/3-python-line-detection-using-hough-transform.ipynb)
        4. [Straightening an image using my own implementation of the Hough transform](notebooks/4-python-straighten-image-using-hough-transform.ipynb)
- `CMakeLists.txt`: Script for CMake
- `hough_transform.cxx`: Own implementation of the Hough transform
- `sobel_image.cxx`: Skeleton to implement an edge detection using the Sobel operators and a binary threshold
- `lines.png`: A test image for the Hough transform
    ![`lines.png` here](img/lines.png)

When running `hough_transform` five windows will be created:

- The input image as a RGB image,
- The input image as a greyscale image,
- The output of a Canny operator on the greyscale image,
- The Hough transform accumulator:
    - The x-axis corresponds to *theta* from 0 to 179 degrees (the angle of the lines),
    - The y-axis corresponds to *r*, the distance of the line from the centre.
- An image showing the RGB input with red lines.

When using the program with
 `lines.png` as an argument, you will see

![Screenshot here](img/hough_screenshot.png)

As you can observe, there are four local maxima (the bright spots) in the accumulator. Each of them corresponds to a line found using the Canny operator.

Copyright (c) 2021, Dr Franck P. Vidal (f.vidal@bangor.ac.uk) [http://www.fpvidal.net/](http://www.fpvidal.net/), [Module ICE-3111:
Computer Vision (20cr)](https://www.bangor.ac.uk/computer-science-and-electronic-engineering/undergraduate-modules/ICE-3111), All rights reserved.
