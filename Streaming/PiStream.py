# Dartmouth College, Winter 2019


# --------------------------- IMPORTS --------------------------- #
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time
import web
import subprocess
camera = PiCamera()
camera.resolution = (720, 720)
led = 5
button = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Commands to start and stop stream
start_server_command = "raspistill -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0"
kill_server_command = "pkill raspistill"
stream_flag = 0


# --------------------------- FUNCTIONS --------------------------- #
def start_stream():
    print("Starting stream...")
    global stream_flag
    stream_flag = 1
    camera.start_preview(fullscreen = False, alpha = 0, window = (0, 0, 720, 720))
    subprocess.call(start_server_command, shell = True) 

def end_stream():
    print("Ending stream...")
    stream_flag = 1
    subprocess.call(kill_server_command, shell = True) 
    camera.stop_preview()

def take_picture():
    print("Taking picture...")
    camera.start_preview(fullscreen = False, window = (0, 0, 720, 720))
    camera.capture('/home/pi/Desktop/testresize.jpg', resize = (360, 360))
    camera.capture('/home/pi/Desktop/test.jpg')

# --------------------------- WEB --------------------------- #
try: 
    web.server_start()
    web.arbitrary_html( "<br/>" )
    web.arbitrary_html( "<img src='https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fcbsnews1.cbsistatic.com%2Fhub%2Fi%2Fr%2F2013%2F04%2F24%2F5e4d566c-c41a-11e2-a43e-02911869d855%2Fthumbnail%2F620x350%2Ffbec6f2b9675ed568f6dc091e178c4c2%2Fdartmouth_college_generic_1088711_fullwidth.jpg&f=1'> </img>" )
    
    web.register( "<button>Start Stream</button>", start_stream )
    web.register( "<button>End Stream</button>", end_stream )
    web.register( "<button>Take Picture</button>", take_picture )


    #Display Stream
    

    while True:
        A=1

except: 
    pass

# the program is finished, we put things back in their original state
print ("> finishing")
web.server_stop()
