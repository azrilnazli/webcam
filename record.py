"""
To automate webcam recording using FFMPEG
Webcam device listed by vfwcap
RAM limited to 2GB
Output video name is output.mkv
"""
import os
import subprocess
from datetime import datetime

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
command = "ffmpeg -hide_banner -y -f vfwcap -t 10 -re -rtbufsize 2147.48M -i 0 %s/%s_%s.mkv" % (folder, 'CAM001', curr_datetime)

#print(command)
# Run the command
subprocess.run(command)

# Convert the recorded video to H264 Video Codec
#command = "ffmpeg -i videos/out.mkv"