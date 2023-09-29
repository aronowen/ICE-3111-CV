---
title: Lab 5 -- Introduction to Spatial Filtering: Application to sharpening.
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision
date: Week 5
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

# Lab 5 -- Introduction to Spatial Filtering: Application to sharpening


- (worth 60% of Assignment 1)
- Deadline: 10/11/2022 at 23:59
- Write your answers in the template provided: [questionnaire.docx](https://github.com/effepivi/ICE-3111-Computer_Vision/raw/main/Labs/Lab-05/questionnaire.docx)

# Introduction

Look at the ellipses in the mindmap. It illustrates which concepts we are discussing this week.

![Week 5 mindmap](mindmap.png)

Last week we studied spatial filtering, inc. low-pass filters, high-pass filters, convolution (linear filtering) and median filter. We applied some of them to reduce noise (low-pass filters), and to sharpen blurry images.
This week we focused of the edge detection. It uses a combination of linear filtering (high-pass filters), point operators (blending to compute the gradient magnitude, and threshold segmentation). We'll implement such techniques in the lab this week but to sharpen an image. Details on image sharpening can be found in Slide in the lecture of Week 4.

Today we will write three programs:

1. Blur an input image with a Gaussian filter,
2. Enhance a blurry image with the image sharpening technique seen in the lecture, and
<!-- 3. Find edges in an image. -->

- [Click here for instructions in C/C++](C-CXX.md)
- [Click here for instructions in Python](Python.md)

# Don't forget

To complete the lab report and to submit it.

# Next week

We will use spatial filters to blur an image, find edges, etc.
