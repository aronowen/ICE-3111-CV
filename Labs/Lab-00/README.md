---
title: Lab 0 -- Installing all the tools needed for ICE-3111 Computer Vision.
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision 202122
date: Sept 26th, 2022
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

# Introduction

The purpose of this lab is to install all the tools needed on your computer (at home).

# Supported programming languages

I am happy to accept assignments in C/C++ or Python.
I use both, pretty much on a daily basis.
They are now the most common programming languages used in computer vision.
Java and JavaScript are not suitable languages for this module.

# Supported platform

You can use the lab machines or your own computer.
I do not mind.
I am familiar with GNU/Linux (my primary computers at work and home), MacOS (my laptop), and MS Windows.
Everything we do in this module can be done on any of these operating systems.

# ImageJ/Fiji

We will use Fiji ![(logo)](icons/fiji.png) to visualise images.
It corresponds to ImageJ ![(logo)](icons/imagej.png) with a lot of plugins already installed.
This is probably the most commonly used software in the scientific community to process and analyse images.
I use it on a daily basis.
**I mean it.**
Just download the archive corresponding to your operating system, and extract it somewhere in your home directory.
You'll find the program at https://imagej.net/Fiji/Downloads](https://imagej.net/Fiji/Downloads) or below:

- [![https://downloads.imagej.net/fiji/latest/fiji-win64.zip](icons/windows.png)](https://downloads.imagej.net/fiji/latest/fiji-win64.zip)
- [![https://downloads.imagej.net/fiji/latest/fiji-macosx.zip](icons/macos.png)](https://downloads.imagej.net/fiji/latest/fiji-macosx.zip)
- [![https://downloads.imagej.net/fiji/latest/fiji-linux64.zip](icons/linux.png)](https://downloads.imagej.net/fiji/latest/fiji-linux64.zip)

# Python

I assume Python is already installed on your computer.
The packages we are likely to use are:

- OpenCV,
- Numpy,
- Scikit-image, and
- Matplotlib.

Installation from binaries:

- PIP: `pip install --user opencv-python numpy scikit-image matplotlib`
- Anaconda: `conda install -c conda-forge opencv-python numpy scikit-image matplotlib`

# C/C++

Do you want to use C/C++? You'll need:

- [![OpenCV](icons/OpenCV_logo_black_.png)](https://www.opencv.org/)
- [![CMake](icons/Cmake-logo-header.png)](https://www.cmake.org/)
- A ![C/C++](icons/ISO_C++_Logo.png) compiler

## MS Windows

- As of today (26/09/2022), the latest version of ![CMake](icons/Cmake-logo-header.png)
can be found at: [https://github.com/Kitware/CMake/releases/download/v3.24.2/cmake-3.24.2-windows-x86_64.msi](https://github.com/Kitware/CMake/releases/download/v3.24.2/cmake-3.24.2-windows-x86_64.msi)
- ![](icons/BrandVisualStudioWin2019-3.png) MS Visual Studio Community 2022 is available at: [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false)

- As of today, the latest version of ![OpenCV](icons/OpenCV_logo_black_.png)
can be found at: [https://sourceforge.net/projects/opencvlibrary/files/4.6.0/opencv-4.6.0-vc14_vc15.exe/download](https://sourceforge.net/projects/opencvlibrary/files/4.6.0/opencv-4.6.0-vc14_vc15.exe/download)

## GNU/Linux

- ![CMake](icons/Cmake-logo-header.png): Use your package manager
- ![GCC](icons/GNU_Compiler_Collection_logo.png): Use your package manager
- ![OpenCV](icons/OpenCV_logo_black_.png): Use your package manager. Make sure to install the development package!

## MacOS

- ![CMake](icons/Cmake-logo-header.png):
    - Use [homebrew](https://brew.sh/) (package manager)
    - or manual install ([https://cmake.org](https://cmake.org))
- ![XCode](icons/Xcode_icon.png): Use the App store and look for XCode to install the C/C++ compiler
- ![OpenCV](icons/OpenCV_logo_black_.png):
    - Use [homebrew](https://brew.sh/) (package manager)
    - or manual install ([https://www.opencv.org](https:/www.opencv.org))
