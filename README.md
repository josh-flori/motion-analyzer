# Abstract / Intro
One of the ways to create beautiful art forms is to exaggerate linear motion and make it non-linear. Give it a heart. Make it bounce. Don’t just show something to the viewer, show it with feeling. This repo allows us to analyze how Disney animations follow this principle. Read more at: https://medium.com/@joshuaflori/how-does-disney-create-magical-animations-4880af66cbfb

# Requirements 
* A video editor (https://fxhome.com/express)
* R
* Python

 # Steps
 Download some video file(s). Run as many videos as desired through tracking.py. This generates a list of centroid values (x/y position of tracked subject) which you will put into a csv. It also outputs frames of the input video with the bounding box and framerate on top of the frame. 
 
 Paste all centroid values into a csv formatted per description in video.R
 
 Load csv into video.R, adjust values to your liking, and run the for loop to create frames of the plot. This is slow, it takes several minutes to generate 1,000 frames.
 
 Stitch the frames output by tracking.py as well as video.R using stitching.py to create output .avi files. On my machine they came out many many times slower than the desired framerate. I had to speed them up in the video editor by many hundreds of percents.
 
