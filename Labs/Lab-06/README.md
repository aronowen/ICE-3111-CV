---
title: Lab 6 -- Background subtraction and motion detection.
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision
date: Week 7
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

# Lab 6 -- Background subtraction and motion detection

- (worth 25% of Assignment 2)
- Deadline: 24/11/2022 at 23:59
- Write your answers in the template provided: [questionnaire.docx](https://github.com/effepivi/ICE-3111-Computer_Vision/raw/main/Labs/Lab-06/questionnaire.docx)

This lab relies on the lecture of Week 8: Motion Detection and Tracking (I know it's next week, but you'll see a practical introduction in this lab).
Look at the ellipses in the mindmap. It illustrates which concepts we are discussing this week.

![Week 7 mindmap](mindmap.png)


The techniques you will use today and next week are:

- Open a video from a camera,
- Save a video into a file,
- Open a video from a file,
- Implement the background subtraction algorithm,
    - Absolute difference between two images,
    - Binary thresholding.

# Preliminaries

There are 3 video files ([one_moving_object.avi](https://www.fpvidal.net/ICE3111/one_moving_object.avi), [change_of_lighting_conditions.avi](https://www.fpvidal.net/ICE3111/change_of_lighting_conditions.avi), and [two_moving_objects.avi](https://www.fpvidal.net/ICE3111/two_moving_objects.avi)) to test your code.

- [![one_moving_object.gif](./one_moving_object.gif)](https://www.fpvidal.net/ICE3111/one_moving_object.avi)
- [![change_of_lighting_conditions.gif](./change_of_lighting_conditions.gif)](https://www.fpvidal.net/ICE3111/change_of_lighting_conditions.avi)
- [![two_moving_objects.gif](./two_moving_objects.gif)](https://www.fpvidal.net/ICE3111/two_moving_objects.avi)

Download them and save them on your disk.


# Instructions

- [Click here for instructions in C/C++](C-CXX.md)
- [Click here for instructions in Python](Python.md)

# Don't forget

To complete the lab report and to submit it.

# Next week

We'll improve the computer vision pipeline next week in light of the deficiencies that you'll highlight in your report and that we will discuss in the next lecture.
