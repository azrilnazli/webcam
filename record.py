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

# FFMPEG command
command = "ffmpeg -hide_banner -y -f vfwcap -t 10 -re -rtbufsize 2147.48M -i 0 videos/%s_%s.mkv" % ('CAM001', curr_datetime)

#print(command)
# Run the command
subprocess.run(command)

# Convert the recorded video to H264 Video Codec
#command = "ffmpeg -i videos/out.mkv"