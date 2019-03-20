""" The purpose of this script is to stitch together both the frames from the video files as well as 
    seperately stitch together the individual jpg plots from the R script. The two videos should be overlayed in video software."""

import cv2
import glob
import os

input_path=input("path to frames? ")
file_type=input("file type? (jpg,png,etc): ")
export_path_name=input("export file name? ")

if __name__ == '__main__':

    files = glob.glob(input_path+'*.'+file_type)
    files.sort(key=os.path.getmtime)
    img_array = []
    for filename in files:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    video = cv2.VideoWriter(export_path_name, -1, 1, (width, height))
    for frame in img_array:
        video.write(frame)
    cv2.destroyAllWindows()
    video.release()










