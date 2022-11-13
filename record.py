"""
To automate webcam recording using FFMPEG
Webcam device listed by vfwcap
RAM limited to 2GB
Output video name is output.mkv
"""
import os
import subprocess
from datetime import datetime
from time import sleep
from threading import Thread

# Get the current date and
# time from system
# and use strftime function
# to format the date and time.
#curr_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
curr_datetime = datetime.now().strftime('%Y%m%d%H%M%S')

# check in videos folder if current date folder was created ?
# if not,create the date folder
folder =  'videos/' + datetime.now().strftime('%Y%m%d') # Ymd format
if not os.path.exists(folder):
    os.mkdir(folder)

# FFMPEG command
# command = "ffmpeg -hide_banner -y -f vfwcap -t 10 -re -rtbufsize 2147.48M -i 0 %s/%s_%s.mkv" % (folder, 'CAM001', curr_datetime)

# -f vfwcap -i "Integrated Camera"


def CAM001():
    print('CAM001 : start recording...')
    #command = "ffmpeg -hide_banner -y -t 10 -re -rtbufsize 2147.48M  -f dshow -i video=\"Webcam C170\"   %s/%s_%s.mkv" % (folder, 'CAM001', curr_datetime)
    command = "ffmpeg -f dshow -framerate 30 -i video=\"Webcam C170\"  -c:v libx264 -g 30 -c:a aac -preset veryfast -segment_time 10 -segment_wrap 24 -f segment  %s/%s_%s_%s.mp4" % (folder, 'CAM001', curr_datetime, '%03d')
    subprocess.run(command)
    print('CAM001 : done')

def CAM002():
    print('CAM002 : start recording...')
    #command = "ffmpeg -hide_banner -y -t 10 -re -rtbufsize 2147.48M  -f dshow -i video=\"USB Video Device\"  %s/%s_%s.mkv" % (folder, 'CAM002', curr_datetime)
    command = "ffmpeg -f dshow -framerate 30 -i video=\"USB Video Device\"  -c:v libx264 -g 30 -c:a aac -preset veryfast -segment_time 10 -segment_wrap 24 -f segment  %s/%s_%s_%s.mp4" % (folder, 'CAM002', curr_datetime, '%03d')
   
    subprocess.run(command)
    print('CAM002 : done')

# create two new threads
t1 = Thread(target=CAM001)
t2 = Thread(target=CAM002)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()