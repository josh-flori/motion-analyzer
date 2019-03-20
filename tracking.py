import cv2
import sys
import numpy as np

""" This script takes a video file, allows you to draw an initial bounding box of the item you wish to track, and tracks the item.
    It prints out the bounding box's centroid value in whichever axis you specify (x or y)."""

# the base path to your video (inlcude trailing '/')
video_file_path = ""
# where you want the frames of your tracked video to be saved (inlcude trailing '/')
output_file_path = ""
# video filename 
file_name = input("filename? ")
movement_axis = input("movement axis? ")
# by default, cv2 reads pixels such that 0 = top of image and 100% = bottom of image. So if you have a sequence like 0,1,2,3,4 that would indicate a descending path. for the purposes of the supplied R script, this is not the desired state. we will want to flip the sequence (by multiplying by -1) and normalize so that the first number in the sequence starts at 0 (by subtracting the first value from all values in the sequence)
normalize_data = input("normalize? (y/n): ")



# TO DO: append values to a specified csv so user doesn't have to manually copy things out of the terminal.
#        don't export frames, export video.      



if __name__ == '__main__':

    # to hold all tracked pixel values which will be used for plotting purposes.
    centroid_values=[]
    # Set up tracker. Uncomment out trackers depending on which one works for your need. There are others available per documentation. These are just what worked for me.
    tracker_type = 'CSRT'
    tracker = cv2.TrackerCSRT_create()
    # tracker_type ='MEDIANFLOW'
    # tracker = cv2.TrackerMedianFlow_create()
    # tracker_type ='MOSSE'
    # tracker = cv2.TrackerMOSSE_create()
    # tracker_type ='MIL'
    # tracker = cv2.TrackerMIL_create()

    # Read video
    video = cv2.VideoCapture(video_file_path + file_name)

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()

    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    i = 0
    while True:

        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break

        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            x = [p1[0], p2[0]]
            y = [p1[1], p2[1]]
            centroid = (int(sum(x) / 2), int(sum(y) / 2))

            if movement_axis == "y":
                centroid_values.append(centroid[1])
            else:
                centroid_values.append(centroid[0])

            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display result
        cv2.imshow("Tracking", frame)

        cv2.imwrite(output_file_path + file_name + str(i) + '.png', frame)
        i += 1

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27: break
        
    if normalize_data.lower() =="t":
        u_centroid_values = np.multiply(np.subtract(centroid_values,centroid_values[0]),-1)
        for i in u_centroid_values:
            print(i)
    for i in centroid_values:
        print(i)