---
title: Lab 6 -- Background subtraction, motion detection, and motion estimation in C/C++
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision
date: Week 7
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

# Introduction to background subtraction and motion detection in C/C++

We'll create 4 programs today.
I suggest that you create a new folder for this week. Create the following files:

- `readWebcam.cxx`,
- `saveWebcam.cxx`,
- `readVideoFile.cxx`,
- `motionDetection.cxx`, and
- `CMakeLists.txt`.

For each `.cxx` files, add a preamble using C++ comments. Each preamble must describe the program:

1. the author of the program (you),
2. the date,
3. the purpose of the file (inc. the command line options),
4. the todo-list if anything is missing.

For now create dummy OpenCV programs. We just want them to compile without any error. Add in each file the following code:

```cpp
#include <exception> // Header for catching exceptions
#include <iostream>  // Header to display text in the console
#include <opencv2/opencv.hpp> // Main OpenCV header


using namespace std;
using namespace cv;


//-----------------------------
int main(int argc, char** argv)
//-----------------------------
{
    try
    {
        // Write your own code here
        //....
        //....
        //....
    }
    // An error occured
    catch (const std::exception& error)
    {
        // Display an error message in the console
        cerr << error.what() << endl;
    }
    catch (const std::string& error)
    {
        // Display an error message in the console
        cerr << error << endl;
    }
    catch (const char* error)
    {
        // Display an error message in the console
        cerr << error << endl;
    }
    catch (...)
    {
        // Display an error message in the console
        cerr << "Unnown error caught" << endl;
    }

#ifdef WIN32
#ifdef _DEBUG
    system("pause");
#endif
#endif

    return 0;
}
```

**Make sure you downloaded the video files** I provided and that they are in the same folder as `CMakeLists.txt`. **It's very important** as CMake is going to copy the files so that they are easily accessible by your programs. The corresponding `CMakeLists.txt` file is:

```cmake
CMAKE_MINIMUM_REQUIRED(VERSION 3.1)
PROJECT(ICE-3111-Lab-Week7)

set (CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

IF (WIN32)
    SET (CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} "D:\\opencv\\build")
    SET (CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} "C:\\opencv\\build")
ENDIF (WIN32)

FIND_PACKAGE(OpenCV REQUIRED)

ADD_EXECUTABLE (readWebcam   readWebcam.cxx)
TARGET_INCLUDE_DIRECTORIES(readWebcam PUBLIC ${OpenCV_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES (readWebcam   ${OpenCV_LIBS})

ADD_EXECUTABLE (saveWebcam   saveWebcam.cxx)
TARGET_INCLUDE_DIRECTORIES(saveWebcam PUBLIC ${OpenCV_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES (saveWebcam   ${OpenCV_LIBS})

ADD_EXECUTABLE (readVideoFile   readVideoFile.cxx)
TARGET_INCLUDE_DIRECTORIES(readVideoFile PUBLIC ${OpenCV_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES (readVideoFile   ${OpenCV_LIBS})

ADD_EXECUTABLE (motionDetection   motionDetection.cxx)
TARGET_INCLUDE_DIRECTORIES(motionDetection PUBLIC ${OpenCV_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES (motionDetection   ${OpenCV_LIBS})

FILE (COPY "${CMAKE_CURRENT_SOURCE_DIR}/one_moving_object.avi"
      DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/")

FILE (COPY "${CMAKE_CURRENT_SOURCE_DIR}/change_of_lighting_conditions.avi"
      DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/")

FILE (COPY "${CMAKE_CURRENT_SOURCE_DIR}/two_moving_objects.avi"
      DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/")

SET (CV_VERSION_STRING ${OpenCV_VERSION_MAJOR}${OpenCV_VERSION_MINOR}${OpenCV_VERSION_PATCH})
IF (WIN32)
    IF ( ${OpenCV_VERSION_MAJOR} EQUAL 4)
        IF (EXISTS "${OpenCV_DIR}/x64/vc15/bin/opencv_videoio_ffmpeg${CV_VERSION_STRING}_64.dll")
            FILE (COPY        "${OpenCV_DIR}/x64/vc15/bin/opencv_videoio_ffmpeg${CV_VERSION_STRING}_64.dll"
                  DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/")
        ELSE ()
            MESSAGE (WARNING "opencv_videoio_ffmpeg${CV_VERSION_STRING}_64.dll is not in ${OpenCV_DIR}/x64/vc15/bin/, you have to make sure is it in the PATH or to copy it manually in your project binary directory")
        ENDIF ()
  ELSE ()
        IF (EXISTS "${OpenCV_DIR}/x64/vc15/bin/opencv_ffmpeg${CV_VERSION_STRING}_64.dll")
            FILE (COPY        "${OpenCV_DIR}/x64/vc15/bin/opencv_ffmpeg${CV_VERSION_STRING}_64.dll"
                  DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/")
        ELSE ()
            MESSAGE (WARNING "opencv_ffmpeg${CV_VERSION_STRING}_64.dll is not in ${OpenCV_DIR}/x64/vc15/bin/, you have to make sure is it in the PATH or to copy it manually in your project binary directory")
        ENDIF ()
  ENDIF ()

    IF (EXISTS "${OpenCV_DIR}/x64/vc15/bin/opencv_videoio_msmf${CV_VERSION_STRING}_64.dll")
        FILE (COPY        "${OpenCV_DIR}/x64/vc15/bin/opencv_videoio_msmf${CV_VERSION_STRING}_64.dll"
              DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/")
    ELSE ()
        MESSAGE (WARNING "opencv_videoio_msmf${CV_VERSION_STRING}_64.dll is not in ${OpenCV_DIR}/x64/vc15/bin/, you have to make sure is it in the PATH or to copy it manually in your project binary directory")
    ENDIF ()

    IF (EXISTS "${OpenCV_DIR}/x64/vc15/bin/opencv_videoio_msmf${CV_VERSION_STRING}_64d.dll")
        FILE (COPY        "${OpenCV_DIR}/x64/vc15/bin/opencv_videoio_msmf${CV_VERSION_STRING}_64d.dll"
              DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/")
    ELSE ()
        MESSAGE (WARNING "opencv_videoio_msmf${CV_VERSION_STRING}_64d.dll is not in ${OpenCV_DIR}/x64/vc15/bin/, you have to make sure is it in the PATH or to copy it manually in your project binary directory")
    ENDIF ()

    IF (EXISTS "${OpenCV_DIR}/x64/vc15/bin/opencv_world${CV_VERSION_STRING}.dll")
        FILE (COPY        "${OpenCV_DIR}/x64/vc15/bin/opencv_world${CV_VERSION_STRING}.dll"
              DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/")
    ELSE ()
        MESSAGE (WARNING "opencv_world${CV_VERSION_STRING}.dll is not in ${OpenCV_DIR}/x64/vc15/bin/, you have to make sure is it in the PATH or to copy it manually in your project binary directory")
    ENDIF ()

    IF (EXISTS "${OpenCV_DIR}/x64/vc15/bin/opencv_world${CV_VERSION_STRING}d.dll")
        FILE (COPY        "${OpenCV_DIR}/x64/vc15/bin/opencv_world${CV_VERSION_STRING}d.dll"
              DESTINATION "${CMAKE_CURRENT_BINARY_DIR}/")
    ELSE ()
        MESSAGE (WARNING "opencv_world${CV_VERSION_STRING}d.dll is not in ${OpenCV_DIR}/x64/vc15/bin/, you have to make sure is it in the PATH or to copy it manually in your project binary directory")
    ENDIF ()
ENDIF (WIN32)
```

## Contents

1. [Read a video from the webcam](#1-read-a-video-from-the-webcam)
2. [Save a video](#2-save-a-video)
3. [Read a video from a file](#3-read-a-video-from-a-file)
4. [Motion detection](#4-motion-detection)

# 1. Read a video from the webcam

- Edit `readWebcam.cxx`.
- To use the webcam,  you need to create a `cv::VideoCapture` object and pass `0` as the constructor argument to use the camera.

    ```cpp
    VideoCapture video_input(0);
    ```

- Once the object is instantiated, make sure the camera is actually open. Yes, we must check if errors occur so that the program does not crash.
    - If the camera is not open, throw an error,
    - Else proceed.

    ```cpp
    if (!video_input.isOpened())
        throw "Cannot open the video stream";
    ```

- Now we can display the images from the camera. We must use a while loop. It's very similar to what we have done so far, except that at each iteration of the loop, we:

    - Grab a new frame,
    - Check if a new image was loaded from the camera,
    - Display it.

    ```cpp
    Mat frame;
    int key = -1;
    while (key != 27 && key != 'q')
    {
        video_input >> frame;

        if (frame.empty())
        {
            throw "Cannot grab frame from camera";
        }

        imshow("Input video", frame);

        key = waitKey(1);
    }
    destroyAllWindows(); // Destroy all the created windows
    video_input.release(); // We are now done with the camera, stop it
    ```

- Make sure you comment your code to show your understanding. Marks will be allocated to comments.
- In your report, add your code and add evidence of testing, e.g. a few screenshots of your window.

# 2. Save a video

- Copy `readWebcam.cxx` into `saveWebcam.cxx`.
- The command line for this program is: `readWebcam <output_video_file.avi>`
- The first thing you need to do in the `try` block is check the command line arguments.
    - Is the number of arguments `argc` equal to 2?
    - If no, then throw a suitable error message and exit,
    - If yes, `argv[1]` is the filename of the output.
- Before the while loop, we need to create an instance of `cv::VideoWriter`. The parameters of the constructor are:
    1. The file name, here `argv[1]`,
    2. The codec to encode the videos (your best bet is `cv::VideoWriter::fourcc('M', 'J', 'P', 'G')` as it is included in OpenCV),
    3. The framerate in frames per second. You can use the same one as the one from the input video, i.e. `video_input.get(CAP_PROP_FPS)`
        - However, sometimes it may not work, and
        - we may have to force another value, e.g. 30.
    4. The size of the image. You need to grab a frame with `video_input >> frame;` (make sure `frame` is declare above, you may have to move the declaration).

    ```cpp
    Mat frame;
    video_input >> frame; // To retrieve the size of a frame

    int fps = video_input.get(CAP_PROP_FPS); // Get the framerate from the camera

    if (fps == 0) fps = 30; // If it has failed, use 30

    float frame_delay_in_sec = 1.0 / fps; // Time between two frame acquisitions in sec
    float frame_delay_in_ms = frame_delay_in_sec  * 1000; // Time between two frame acquisitions in ms

    // Open the video output
    VideoWriter video_output(argv[1],
        VideoWriter::fourcc('M', 'J', 'P', 'G'),
        fps,
        Size(frame.cols, frame.rows));
    ```

- Check if the video writer is open,
    - If yes, proceed;
    - If not, throw an error message

    ```cpp
    if (!video_output.isOpened())
        throw "Cannot open the video output";
    ```

- In the loop, after grabbing a new frame, add it to the video output:

    ```cpp
    video_output << frame;
    ```

- At the end of the `while` loop, replace `key = waitKey(1);` with `key = waitKey(frame_delay_in_ms);`
- After the while loop, you may call `video_output.release();` although this is optional as the destructor of the object will take care of closing the output video file.

- Make sure you comment your code to show your understanding. Marks will be allocated to comments.
- In your report, add your code and add evidence of testing, e.g. a screenshot of the command line, of the file in the file explorer, and the file playing in a video player.

# 3. Read a video from a file

- Copy `readWebcam.cxx` into `readVideoFile.cxx`.
- The command line for this program is: `readVideoFile <input_video_file.avi>`
- The first thing you need to do in the `try` block is check the command line arguments.
    - Is the number of arguments `argc` equal to 2?
    - If no, then throw a suitable error message and exit,
    - If yes, `argv[1]` is the filename of the input.
- Before the while loop
    - Replace `0` in `VideoCapture video_input(0);` with `argv[1]`.
    - Retrieve the framerate of the `VideoCapture` in frames per second using `int fps = video_input.get(CAP_PROP_FPS)`.
    - From this number, compute the time delay between two successive frames: `float frame_delay_in_sec = 1.0 / fps;`
    - Convert this number in milliseconds: `float frame_delay_in_ms = frame_delay_in_sec  * 1000;`.
- In the while loop:
    - You can replace `"Input video"` in `imshow("Input video", frame);` with `argv[1]`.
    - At the end of the `while` loop, replace `key = waitKey(1);` with `key = waitKey(frame_delay_in_ms);`
- Voila, you created a program to read video files.

- Make sure you comment your code to show your understanding. Marks will be allocated to comments.
- In your report, add your code and add evidence of testing, e.g. a screenshot of the command line, and of your window.

# 4. Motion detection

- Copy `saveWebcam.cxx` into `motionDetection.cxx`.
- The command line for this program is: `motionDetection <input_video_file.avi> <output_video_file.avi>`
- The first thing you need to do in the `try` block is check the command line arguments.
    - Is the number of arguments `argc` equal to 3?
    - If no, then throw a suitable error message and exit,
    - If yes, `argv[1]` is the filename of the input, and `argv[2]` is the filename of the output.
    - **MAKE SURE YOU UPDATE THE INITIALISATION OF `video_input` and `video_output` ACCORDINGLY.**
- Before the while loop, create a new image called `background` (the type in `Mat`).
- Initialise `background` with the first frame of the video.
- Convert `background` into a grey scale image.
- In the while loop, convert the current `frame` into a grey scale image.
- Still in the while loop, create a new image `foreground`. It is equal to the absolute difference between the current `frame` and `background`:

    ```cpp
    Mat foreground = cv::abs(background - frame);
    ```
- Show `foreground` in a new window using `imshow` and test your code with the videos I provided.
- Only large variations correspond to the moving object(s). Apply a threshold to generate the foreground mask (declare a new image `foreground_mask`):

    ```cpp
    int threshold_value = 128;
    Mat foreground_mask;
    threshold(foreground, foreground_mask, threshold_value, 255, THRESH_BINARY);
    ```

- Show `foreground_mask` in a new window using `imshow` and test your code with the videos I provided.
- If 128 is too high, lower its value, e.g. try 64.

- Instead of save `frame` into `video_output`, save `foreground_mask` (just before you save the image, you must convert it to RGB with `cv::cvtColor(foreground_mask, foreground_mask, COLOR_GRAY2BGR);`).

- Make sure you comment your code to show your understanding. Marks will be allocated to comments.
- In your report, add your code and add evidence of testing, e.g. a screenshot of the command line, and of your windows.
- You must test your code with several video files.
- In your report, provide a critical analysis of the imaging pipeline we got so far.
    - Does it work well?
    - Does it has deficiencies?
        - If it has deficiencies, what are they?
