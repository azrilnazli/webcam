"""
To automate webcam recording using FFMPEG
Webcam device listed by vfwcap
RAM limited to 2GB
Output video name is output.mkv
"""
import subprocess

# FFMPEG command
command = "ffmpeg -hide_banner -y -f vfwcap -t 10 -re -rtbufsize 2147.48M -i 0 videos/out.mkv"

# Run the command
subprocess.run(command)