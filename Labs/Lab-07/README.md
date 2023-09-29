---
title: Lab 7 --  From motion detection to motion tracking and motion estimation.
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision
date: Week 8
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

# Lab 7 -- From motion detection to motion tracking and motion estimation in Python

- (worth 25% of Assignment 2)
- Deadline: 08/12/2022 at 23:59
- Write your answers in the template provided: [questionnaire.docx](https://github.com/effepivi/ICE-3111-Computer_Vision/raw/main/Labs/Lab-07/questionnaire.docx)

This lab relies on the lecture of Week 8: Motion Detection and Tracking. It also relies on the [lab from last week](../Lab-06) as we are going to improve it. **Make sure you completed it!**

![Week 8 mindmap](mindmap.png)


The techniques we used last week in `motionDetection.cxx` and `motionDetection.py` were:

- Open a video from a file,
- Implement the background subtraction algorithm,
    - Absolute difference between two images,
    - Binary thresholding.

This week we want to replicate a computer vision pipeline similar to this YouTube video

[![Traffic Monitoring Application - Background Subtraction - 1](https://img.youtube.com/vi/KOsgEsY8UWI/0.jpg)](https://youtu.be/KOsgEsY8UWI)

In order to achieve this, we will take last week's program and

- Handle changes of illumination,
- "clean" the foreground mask to fill holes and remove tiny islands. This is often performed using mathematical morphology (opening and closing),
- Identify the number of moving objects in the video by analysing the foreground mask,
- Track the position of each moving object,
- Highlight in the original video where the moving objects are, and
- Compute the velocity of each object.

# Instructions

- [Click here for instructions in C/C++](C-CXX.md)
- [Click here for instructions in Python](Python.md)

# Don't forget

To complete the lab report and to submit it.

# Next week

We will use the feature detection and tracking framework to stitch images together and produce a panorama. That will be the final topic we will cover in the lab.
