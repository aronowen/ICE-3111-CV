---
title: Lab 6 -- Background subtraction and motion detection in Python
author: Dr Franck P. Vidal
subtitle: ICE-3111 Computer Vision
date: Week 7
keywords: ICE3111, Computer Vision, C/C++, python, image processing, OpenCV, Bangor University, School of Computer Science and Electronic Engineering
institute: School of Computer Science and Electronic Engineering, Bangor University
---

# Introduction to background subtraction and motion detection

We'll create 4 programs today.
I suggest that you create a new folder for this week. Create the following files:

- `readWebcam.py`,
- `saveWebcam.py`,
- `readVideoFile.py`,and
- `motionDetection.py`.

For each `.py` files, add a preamble using Python comments. Each preamble must describe the program:

1. the author of the program (you),
2. the date,
3. the purpose of the file (inc. the command line options),
4. the todo-list if anything is missing.

## Contents

1. [Read a video from the webcam](#1-read-a-video-from-the-webcam)
2. [Save a video](#2-save-a-video)
3. [Read a video from a file](#3-read-a-video-from-a-file)
4. [Motion detection](#4-motion-detection)

# 1. Read a video from the webcam

- Edit `readWebcam.py`.
- Make sure you import OpenCV's package, sys for the command line, and numpy.

    ```python
    import sys # to read the command line arguments
    import cv2 # cv2 library
    import numpy as np # numpy library
    ```

- To use the webcam,  you need to create a `cv2.VideoCapture` object and pass `0` as the constructor argument to use the camera.

    ```python
    video_input = cv2.VideoCapture(0)
    ```

- Once the object is instantiated, make sure the camera is actually open. Yes, we must check if errors occur so that the program does not crash.
    - If the camera is not open, raise an error,
    - Else proceed.

    ```python
    if not video_input.isOpened():
        raise IOError("Cannot open the video stream")
    ```

- Now we can display the images from the camera. We must use a while loop. It's very similar to what we have done so far, except that at each iteration of the loop, we:

    - Grab a new frame,
    - Check if a new image was loaded from the camera,
    - Display it.

    ```python
    key = -1;
    while key != 27 and key != 'q':

        ret, frame = video_input.read()

        if frame is None:
            raise IOError("Cannot grab frame from camera")

        cv2.imshow("Input video", frame);

        key = cv2.waitKey(1);

    cv2.destroyAllWindows(); # Destroy all the created windows
    video_input.release(); # We are now done with the camera, stop it
    ```

- Make sure you comment your code to show your understanding. Marks will be allocated to comments.
- In your report, add your code and add evidence of testing, e.g. a few screenshots of your window.

# 2. Save a video

- Copy `readWebcam.py` into `saveWebcam.py`.
- The command line for this program is: `python3 readWebcam.py <output_video_file.avi>`
- The first thing you need to do is check the command line arguments.
    - Is the number of arguments `len(sys.argv)` equal to 2?
    - If no, then throw a suitable error message and exit,
    - If yes, `sys.argv[1]` is the filename of the output.
- Before the while loop, we need to create an instance of `cv2.VideoWriter`. The parameters of the constructor are:
    1. The file name, here `sys.argv[1]`,
    2. The codec to encode the videos (your best bet is `cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')` as it is included in OpenCV),
    3. The framerate in frames per second. You can use the same one as the one from the input video, i.e. `video_input.get(CAP_PROP_FPS)`
        - However, sometimes it may not work, and
        - we may have to force another value, e.g. 30.
    4. The size of the image. You need to grab a frame with `ret, frame = video_input.read()`.

    ```python
    ret, frame = video_input.read() # To retrieve the size of a frame

    fps = video_input.get(cv2.CAP_PROP_FPS); # Get the framerate from the camera

    if fps == 0: # If it has failed, use 30
        fps = 30

    frame_delay_in_sec = 1.0 / fps # Time between two frame acquisitions in sec
    frame_delay_in_ms = int(frame_delay_in_sec  * 1000) # Time between two frame acquisitions in ms

    video_output = cv2.VideoWriter(sys.argv[1],
                             cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                             fps,
                             (frame.shape[1], frame.shape[0]))
    ```

- Check if the video writer is open,
    - If yes, proceed;
    - If not, throw an error message

    ```python
    if not video_output.isOpened():
        raise IOError("Cannot open the video output")
    ```

- In the loop, after grabbing a new frame, add it to the video output:

    ```python
    video_output.write(frame)
    ```

- At the end of the `while` loop, replace `key = cv2.waitKey(1)` with `key = cv2.waitKey(frame_delay_in_ms)`
- After the while loop, you may call `video_output.release()` although this is optional as the destructor of the object will take care of closing the output video file.

- Make sure you comment your code to show your understanding. Marks will be allocated to comments.
- In your report, add your code and add evidence of testing, e.g. a screenshot of the command line, of the file in the file explorer, and the file playing in a video player.

# 3. Read a video from a file

- Copy `readWebcam.py` into `readVideoFile.py`.
- The command line for this program is: `python3 readVideoFile.py <input_video_file.avi>`
- The first thing you need to do is check the command line arguments.
    - Is the number of arguments `len(sys.argv)` equal to 2?
    - If no, then throw a suitable error message and exit,
    - If yes, `sys.argv[1]` is the filename of the input.
- Before the while loop
    - Replace `0` in `video_input = cv2.VideoCapture(0);` with `sys.argv[1]`.
    - Retrieve the framerate of the `VideoCapture` in frames per second using `fps = video_input.get(cv2.CAP_PROP_FPS)`.
    - From this number, compute the time delay between two successive frames: `frame_delay_in_sec = 1.0 / fps`
    - Convert this number in milliseconds: `frame_delay_in_ms = int(frame_delay_in_sec  * 1000)`.
- In the while loop:
    - You can replace `"Input video"` in `imshow("Input video", frame);` with `sys.argv[1]`.
    - At the end of the `while` loop, replace `key = cv2.waitKey(1);` with `key = cv2.waitKey(frame_delay_in_ms);`
- Voila, you created a program to read video files.

- Make sure you comment your code to show your understanding. Marks will be allocated to comments.
- In your report, add your code and add evidence of testing, e.g. a screenshot of the command line, and of your window.



# 4. Motion detection

- Copy `saveWebcam.py` into `motionDetection.py`.
- The command line for this program is: `python3 motionDetection.py <input_video_file.avi> <output_video_file.avi>`
- The first thing you need to do is check the command line arguments.
    - Is the number of arguments `len(sys.argc)` equal to 3?
    - If no, then throw a suitable error message and exit,
    - If yes, `sys.argv[1]` is the filename of the input, and `sys.argv[2]` is the filename of the output.
    - **MAKE SURE YOU UPDATE THE INITIALISATION OF `video_input` and `video_output` ACCORDINGLY.**
- Before the while loop, create a new image called `background` and initialise it with the first frame of the video.
- Convert `background` into a grey scale image and into floating-point numbers.
- In the while loop, convert the current `frame` into a grey scale image and into floating-point numbers.
- Still in the while loop, create a new image `foreground`. It is equal to the absolute difference between the current `frame` and `background`:

    ```python
    foreground = np.abs(background - frame).astype(np.uint8)
    ```
- Show `foreground` in a new window using `imshow` (e.g. `cv2.imshow("foreground", foreground)`) and test your code with the videos I provided.
- Only large variations correspond to the moving object(s). Apply a threshold to generate the foreground mask (declare a new image `foreground_mask`):

    ```python
    threshold_value = 128
    ret, foreground_mask = cv2.threshold(foreground, threshold_value, 255, cv2.THRESH_BINARY)
    ```

- Show `foreground_mask` in a new window using `imshow` and test your code with the videos I provided.
- If 128 is too high, lower its value, e.g. try 64.

- Instead of save `frame` into `video_output`, save `foreground_mask` (just before you save the image, you must convert it to RGB with `foreground_mask = cv2.cvtColor(foreground_mask, cv2.COLOR_GRAY2BGR)`).

- Make sure you comment your code to show your understanding. Marks will be allocated to comments.
- In your report, add your code and add evidence of testing, e.g. a screenshot of the command line, and of your windows.
- You must test your code with several video files.
- In your report, provide a critical analysis of the imaging pipeline we got so far.
    - Does it work well?
    - Does it has deficiencies?
        - If it has deficiencies, what are they?
