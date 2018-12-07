# Dartmouth College, Winter 2018/2019

# --------------------------- IMPORTS --------------------------- #
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time
import web
import subprocess
#camera = PiCamera()
#camera.resolution = (720, 720)
led = 5
button = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#RUNS AT BEGINNING 
start_server = "mkdir /tmp/stream; raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &"
subprocess.call(start_server, shell = True)

start_stream = "LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i \"input_file.so -f /tmp/stream -n pic.jpg\" -o \"output_http.so -w /usr/local/www\" &"
subprocess.call(start_stream, shell = True)


#Commands to start and stop stream
#start_server_command = "raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0"
start_stream_command = "LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i \"input_file.so -f /tmp/stream -n pic.jpg\" -o \"output_http.so -w /usr/local/www\" &"
kill_server_command = "pkill raspistill"
kill_stream_command = "pkill mjpg_streamer"
stream_flag = 0


# --------------------------- FUNCTIONS --------------------------- #
#def start_stream():
    #print("Starting stream...")
    #global stream_flag
    #stream_flag = 1
    #camera.rotation = 180
    #camera.start_preview(fullscreen = False, window = (0, 0, 720, 720))
    #subprocess.call(start_server_command, shell = True)
    #subprocess.call(start_stream_command, shell = True)
    
def end_stream():
    print("Ending stream...")
    stream_flag = 1
    subprocess.call(kill_stream_command, shell = True)
    subprocess.call(kill_server_command, shell = True)
    #camera.stop_preview()

def take_picture():
    print("Taking picture...")
    #NOT STARTING STREAM AGAIN
    #camera.rotation = 180
    #camera.start_preview(fullscreen = False, window = (0, 0, 720, 720))
    #camera.capture('/home/pi/Desktop/testresize.jpg', resize = (360, 360))
    #camera.capture('/home/pi/Desktop/test.jpg')

# --------------------------- WEB --------------------------- #
try: 
    web.server_start()
    web.arbitrary_html( "<br/>" )
    web.arbitrary_html( "<img src='https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fcbsnews1.cbsistatic.com%2Fhub%2Fi%2Fr%2F2013%2F04%2F24%2F5e4d566c-c41a-11e2-a43e-02911869d855%2Fthumbnail%2F620x350%2Ffbec6f2b9675ed568f6dc091e178c4c2%2Fdartmouth_college_generic_1088711_fullwidth.jpg&f=1'> </img>" )
    
    #Display Stream
    web.arbitrary_html( "<br/>" )
    web.arbitrary_html( "<img src='http://10.81.13.74:8080/?action=stream'> </img>" )

    #Buttons
    web.register( "<button>End Stream</button>", end_stream )
    web.register( "<button>Recognize!!</button>", take_picture )

    while True:
        A=1

except: 
    pass

# the program is finished, we put things back in their original state
print ("> finishing...")
#camera.close()
subprocess.call(kill_stream_command, shell = True)
subprocess.call(kill_server_command, shell = True)
web.server_stop()





