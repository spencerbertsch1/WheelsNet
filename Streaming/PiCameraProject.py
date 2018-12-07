# Spencer Bertsch
# Dartmouth College, Winter 2019
# Raspberry Pi IOT Short Course
# Pi Camera Project
#

# --------------------------- IMPORTS --------------------------- #
from picamera import PiCamera
from time import sleep
import time


# --------------------------- DEFINE CAMERA --------------------------- #
camera = PiCamera()

# --------------------------- TEST CAMERA --------------------------- #
camera.rotation = 180
camera.start_preview(alpha=200) #<-- Changes image transparency
camera.start_preview()
sleep(10)
camera.stop_preview()

# --------------------------- TAKING PHOTOS --------------------------- #
#camera.rotation = 180
#camera.start_preview()
#sleep(5)
#camera.capture('/home/pi/Desktop/IMAGE_DATA/img1.png')
#camera.stop_preview()


# --------------------------- TAKE 5 PHOTOS --------------------------- #
#camera.rotation = 180
#camera.start_preview()
#for i in range(5):
#    sleep(1)
#    camera.capture('/home/pi/Desktop/IMAGE_DATA/image%s.jpg' % i)
#camera.stop_preview()

