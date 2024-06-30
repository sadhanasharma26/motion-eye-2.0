import cv2
import os

video_path = '/Users/sadhanasharma/motion-eye/road Texture For Hot wheels on mobile copy.mp4'
output_folder = 'images'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

vidcap = cv2.VideoCapture(video_path)
success, image = vidcap.read()
count = 0

while success:
    cv2.imwrite(os.path.join(output_folder, "frame%d.jpg" % count), image) 
    success, image = vidcap.read()
    count += 1