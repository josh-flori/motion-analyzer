# Abstract / Intro
The purpose of this project is to visualize the cadence of motion of a tracked video subject in a single dimension (x or y). This allows one to see the degree of linearity or non-linearity in motion of a particular subject. In the case of animation, this is a useful study tool as one can isolate a dimension of movement and better learn the established art form. 

# Finished Example
https://www.youtube.com/watch?v=R-_Po6Wv7Fo

# Requirements 
* A video editor (https://fxhome.com/express)
* R
* Python

 # Steps
 Download some video file(s). Run as many videos as desired through tracking.py. This generates a list of centroid values (x/y position of tracked subject) which you will put into a csv. It also outputs frames of the input video with the bounding box and framerate on top of the frame. 
 Paste all centroid values into a csv formatted per description in video.R
 Load csv into video.R, adjust values to your liking, and run the for loop to create frames of the plot. This is slow, it takes several minutes to generate 1,000 frames.
 Stitch the frames output by tracking.py as well as video.R using stitching.py to create output .avi files. On my machine they came out many many times slower than the desired framerate. I had to speed them up in the video editor by many hundreds of percents.
 
