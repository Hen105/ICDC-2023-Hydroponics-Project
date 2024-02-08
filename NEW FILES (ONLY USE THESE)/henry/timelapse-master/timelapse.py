from picamera import PiCamera
from os import system
import datetime
from time import sleep

tlminutes = 0.01 #set this to the number of minutes you wish to run your timelapse camera
secondsinterval = 0.01 #number of seconds delay between each photo taken
fps = 0.1 #frames per second timelapse video
numphotos = int((tlminutes*60)/secondsinterval) #number of photos to take


dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Desktop/snapshots/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, datetimeformat))
#system('rm /home/pi/Pictures/*.jpg')
print('Timelapse video is complete. Video saved as /home/pi/Videos/{}.mp4'.format(datetimeformat))
