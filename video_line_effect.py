import os
import cv2
import numpy as np
import time

video_file_name = "video.mp4"


#video settings to be made
width = 1280
hieght = 720
channel = 3
fps = 30
sec = 20 #!!!!


# Video to frames
os.mkdir("frames")
import cv2
vidcap = cv2.VideoCapture(video_file_name)
success,image = vidcap.read()
count = 0
os.chdir("frames")
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('save frame')
  count += 1
os.chdir("../")
time.sleep(2)



# Apply Effect to Frames
os.mkdir("final_frames")
frames = sorted(os.listdir("frames"), key=len)
value = 0
for i in frames:
    img = cv2.imread("frames/"+i, 0) 
    img = cv2.Canny(img,100,50)
    cv2.imwrite("final_frames\zzz"+str(value)+".png",img)
    print("apply effect")
    value += 1
time.sleep(2)




# Create Video
fourcc = cv2.VideoWriter_fourcc(*'MP42')
video = cv2.VideoWriter('image_to_video_result.avi', fourcc, float(fps), (width, hieght))
directry = 'final_frames'
img_name_list = sorted(os.listdir(directry),key=len)
counter = 0
for frame_count in range(fps*sec):
    if counter < len(os.listdir("final_frames")): 
        img_name = img_name_list[counter]
        img_path = os.path.join(directry, img_name)
        img = cv2.imread(img_path)
        kernel = np.ones((2,2),np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        img = cv2.dilate(img,kernel,iterations = 1)
        video.write(img)
        counter +=1
video.release()
print("video done")
