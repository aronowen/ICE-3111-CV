# ICE3111 -- Computer Vision -- Lab 8 -- Lab report

(worth 50% of Assignment 2)

- Deadline: 15/12/2021 at 23:59

- Your name: \_\_\_\_\_\_\_\_\_\_\_\_\_
- Your user ID: \_\_\_\_\_\_\_\_\_\_\_\_\_


**NOTE: When you add a listing in a report, you must format it properly!**
- Use a monotype font so that it is easily readable (e.g. Lucida Sans Console or Courier New). This means that all letters take up the same space on the page;
- Indent the code; and
- Use (colour) syntax highlighting.
- Show line numbers (optional)

<!-- **NOTE: I want you to provide the command line arguments to show the effects of various parameters.** -->

<br/>

<br/>

<br/>

# Complete the lab

- You must test your code with 3 sets of images. Two are already provided for your convenience. You can use them here.
- Each iteration of the stitching will create 7 images:
    - Left image,
    - Right image,
    - All the matches (image created using `drawMatches`),
    - Good matches only (image created using `drawMatches`),
    - Right image after transformation (i.e. the result of `warpPerspective`),
    - Stitching before cropping, and
    - Stitching after cropping.
- You must provide these images in your lab report to demonstrate
    - that you tested the code
    - what works, and if needed what doesn't.
- Make sure you label each image in your report so that it's clear what's what.
- If applicable, for each test, provide the command line arguments.

## Test 1 [10]

## Test 2 [10]

## Test 3 [20] (assuming this test uses more than two images)

# Critical analysis [20]

Discuss here the pros and cons of your implementation. For example
    - Is there any deficiency?
    - Does everything look perfect or is there anything we would need to address?

# Source code [40]

- Marks will be allocated for
    - comments (quality, quantity, and usefulness).
    - the use of the command line instead of hard-coding filenames.
    - the use of a slider to tune the threshold.
    - being able to stitch more than two images.
- **DO NOT FORGET TO ADD A PREAMBLE**.
    - If there is a bug, discuss it in a todo-list in the preamble.
    - If the code is incomplete, discuss it in a todo-list in the preamble.
