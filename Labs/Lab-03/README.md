---
title: Lab 3 -- Introduction to OpenCV in C/C++ and Python, and Point Operators.
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision
date: Week 3
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

# Lab 3 -- Introduction to OpenCV in C/C++ and Python, and Point Operators


- (worth 30% of Assignment 1)
- Deadline: 27/10/2022 at 23:59
- Write your answers in the template provided: [questionnaire.docx](https://github.com/effepivi/ICE-3111-Computer_Vision/raw/main/Labs/Lab-03/questionnaire.docx)

## Introduction

Look at the ellipses in the mindmap. It illustrates which concepts we are discussing this week.

![Week 3 mindmap](../../mindmap/Week-03/screenshot.png)

This week we studied point operators in the lecture.
For example, we saw how to improve the contrast of an image that is dull using a simple, but powerful, technique called "histogram stretching" (also called min-max normalisation).

Today we will:

1. Install OpenCV if needed:
    - Either use C/C++, or,
    - Python.
2. Load an image.
3. Display an image.
4. Convert a RGB image in a greyscale image.
5. Find the smallest and largest pixel values in an image.
6. Improve the contrast of an image:
    - by hand using the equation seen in the lecture,
    - using OpenCV's function.
7. Change the dynamic range using a log transform.
8. Blend two images in a for loop to create an animation.


## 1. Preliminaries: Install OpenCV if needed

Ask yourself if you prefer to write code using C, C++ or Python.
Have you installed OpenCV for your favourite language? If not, refer to [Lab 0](../Lab-00).
For the lab machines, it should be done, at least for the C and C++ language.

- [Click here for instructions in C/C++](C-CXX.md)
- [Click here for instructions in Python](Python.md)

## Don't forget

To complete the lab report and to submit it.

## Next week

We will use spatial filters to blur an image, find edges, etc.
