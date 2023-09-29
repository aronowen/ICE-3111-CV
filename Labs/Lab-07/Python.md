---
title: Lab 7 -- From motion detection to motion tracking and motion estimation in Python
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision
date: Week 8
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

#  From motion detection to motion tracking and motion estimation in Python

We'll create 1 program only today.
I suggest that you keep in in the same folder as last week's lab as we are going to use the same data.
Copy `motionDetection.py` into `motionTracking.py`

In `motionTracking.py`, add a preamble using Python comments. The preamble must describe the program:

1. the author of the program (you),
2. the date,
3. the purpose of the file (inc. the command line options),
4. the todo-list if anything is missing.

## Contents

1. [Changes of illumination](#1-changes-of-illumination),
2. [Clean the foreground mask](#2-clean-the-foreground-mask),
3. [Identify the moving objects](#3-identify-the-moving-objects),
4. [Highlight moving objects in the original video](#5-highlight-moving-objects-in-the-original-video),
5. [Track the position of each moving object](#4-track-the-position-of-each-moving-object), and
6. [Remove static objects if any](#6-remove-static-objects-if-any).

**NOTE: You must test your new program (`motionTracking.py`) with the 3 videos I provided. You can use other videos too, but you must at least demonstrate that your code works with the one I provided."**

# 1. Changes of illumination

In the following video, the lighting condition will change.

[![../Lab-06change_of_lighting_conditions.gif](../Lab-06/change_of_lighting_conditions.gif)](https://www.fpvidal.net/ICE3111/change_of_lighting_conditions.avi)

The light was off at the beginning of the recording. I asked someone to turn it on during the recording.

|  | Light off | Light on |
|--|-----------|----------|
| Original frame | ![light-off.jpg](light-off.jpg)     | ![light-on.jpg](light-on.jpg)    |
| Greyscale | ![light-off-grey.png](light-off-grey.png)     | ![light-on-grey.png](light-on-grey.png)    |
| Histogram of greyscale | ![Histogram_of_light-off-grey.png](Histogram_of_light-off-grey.png)     | ![Histogram_of_light-on-grey.png](Histogram_of_light-on-grey.png)    |

The absolute difference between the two greyscale images is:

![absolute_difference.png](absolute_difference.png)

Bright pixels show pixels whose intensity has changed considerably.
We can see two things:

- the noise is an important factor,
- the change of illumination is also an important factor.

We must mitigate for both.

## Noise

To account for the noise, we can smooth the images with a median filter. Below I used a 5x5 filter:

|  | Light off | Light on |
|--|-----------|----------|
| Greyscale | ![light-off-grey.png](light-off-grey.png)     | ![light-on-grey.png](light-on-grey.png)    |
| Smoothed | ![light-off-grey-median.png](light-off-grey-median.png)     | ![light-on-grey-median.png](light-on-grey-median.png)    |

The absolute difference becomes:

![absolute_difference-median.png](absolute_difference-median.png)

The effect of the noise has been attenuated.

### Edit `motionTracking.py`

1. Filter the background with a median filter. You can use a 5x5 filter as follows:

```python
background = cv2.medianBlur(background, 5)
```

You may experiment different values.

2. In the `while` loop, backup the incoming frame before you process it.

    - At the beginning of your file, `import copy`.
    - Just after the call to `ret, frame = video_input.read()`, backup the frame with `frame_backup = copy.deepcopy(frame)`
    - Once the frame is backed up, filter the incoming `frame` with the same filter.

3. Run and test your program using several videos.
In your report, document what changes you made in your code and document your tests. You must add screenshots.

### Change of illumination

The zero-mean, unit-variance normalisation (or standardisation as it is called in machine learning) is a popular technique in computer vision to address changes of illumination. After this operation, the average pixel value is zero, and the standard deviation is one.

### Edit `motionTracking.py`

1. After filtering the background with the median filter, apply the normalisation with:

```python
background -= np.mean(background)
background /= np.std(background)
```

2. In the `while` loop, do the same for the incoming `frame`.
**Note that `cv2.imshow("foreground", foreground)` is going to display a black image now as the range of pixel values is  no longer valid.**

3. Keep the data in floating point number. Replace

```python
foreground = np.abs(background - frame).astype(np.uint8)
cv2.imshow("foreground", foreground)
```

with

```python
foreground = np.abs(background - frame)
cv2.imshow("foreground", (foreground - np.min(foreground)) / (np.max(foreground) - np.min(foreground)))
```

4. Change the threshold. Try `1`. Try other values until you are satisfied with the threshold.

5. Test your code and document in your report what changes you made to your code. You must add screenshots.

# 2. Clean the foreground mask

Now, we want

1. to remove tiny islands from the foreground mask, and
2. fill small holes.

as follows:


| Before cleaning | After cleaning |
|-----------------|----------------|
| ![foreground_mask_screenshot.png](foreground_mask_screenshot.png) | ![foreground_mask_screenshot_morphology.png](foreground_mask_screenshot_morphology.png) |

A median filter could do the job, however a large size might be required. We will prefer using mathematical morphology instead.

1. Make sure your binary mask is in the right format. Replace `foreground_mask = cv2.cvtColor(foreground_mask, cv2.COLOR_GRAY2BGR).astype(np.uint8)` with `foreground_mask = foreground_mask.astype(np.uint8)`. It is now a greyscale image in unsigned byte.

2. Filter `foreground_mask` as follows:

```python
element_size = 3
structuring_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                    (element_size, element_size))

foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_CLOSE, structuring_element)
foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_OPEN, structuring_element)
```
**NOTE: you can only apply these operation on the greyscale image in unsigned byte, i.e. AFTER you called `cv2.cvtColor(foreground_mask, cv2.COLOR_GRAY2BGR).astype(np.uint8)`.**

3. Change the size of the structuring element you are satisfied with its value.

**NOTE: make sure you call ` cv2.imshow("foreground_mask", foreground_mask)` AFTER the mathematical morphology operations.**
`
4. Run and test your program using several videos and several sizes of structuring element.
In your report, document what changes you made in your code and document your tests. You must add screenshots.

# 3. Identify the moving objects

To find the objects highlighted in white in `foreground_mask`, we need to find the contours:

```python
contours, hierarchy = cv2.findContours(foreground_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
```

# 4. Highlight moving objects in the original video

We will only draw a contour if it is big enough (whatever big enough might be). We will draw it over the `frame_backup`.

Your output video should look like this:

![moving_objects_rect.png](moving_objects_rect.png)

```python
for cnt in contours:
    if cv2.contourArea(cnt) > 0.1 / 100.0 * frame_backup.shape[0] * frame_backup.shape[1]:
        x,y,w,h = cv2.boundingRect(cnt)

        cv2.rectangle(frame_backup, (x,y), (x+w, y+h), (0,255,0),2)
```

In the code above, a contour is big enough if its area is larger than 0.1% of the area of the whole image.
You may have to tweak this number.

**NOTE: Make sure that this is `frame_backup` that is written in `video_output`.**

**NOTE: Make sure that this is `frame_backup` that is displayed instead of `frame` in "`Input video`". Make sure that you move the corresponding `imshow` at the end of the while loop.**



Again, document your tests in your report.

# 5. Track the position of each moving object

- I will use an `enumerate` to retrieve the ID of the contour.
`for cnt in contours:` becomes `for i, cnt in enumerate(contours):`

- Now we can display "Object 0" for the 1st object, "Object 1" for the 2nd  object, etc. with

```python
        cv2.putText(frame_backup,
                    "Object " + str(i),
                    (int(x + w / 2), int(y + h / 2)),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    2,
                    255)
```


I get something like:

![moving_objects.png](moving_objects.png)

Again, document your tests in your report.

# 6. Remove static objects if any

In the image above, you can see that `Object 0` is not actually an object that moves. You must find a way to ignore contours of all the objects that are not moving between successive frames as illustrated in:

![moving_objects_only.png](moving_objects_only.png)

You could

1. update the background, and this is something we discussed in the lecture.
2. Alternatively, for each iteration of the while loop, you could
    1. backup the centre of the contours of the previous frame
    2. for each contour of the new frame,
        - if all the contour of the previous frame are far enough,
        - then consider the object is moving,
        - else consider that it is static (hence part of the background).
