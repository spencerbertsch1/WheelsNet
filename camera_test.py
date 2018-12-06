from picamera import PiCamera
from RPi import GPIO
import time

camera = PiCamera()

button = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

try:
    while True:
        if GPIO.input(button) == 0:
            print "Button pressed!"
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

