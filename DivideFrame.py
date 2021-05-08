import cv2
from glob import glob

count=1
video_list=glob("*.mp4");
for i in video_list:
    cap = cv2.VideoCapture(i)
    while (cap.isOpened()):
        ret, frame=cap.read()
        if ret:
            cv2.imwrite(str(count)+".jpg",frame)
            count+=1
        else:
            break
    cap.release()
