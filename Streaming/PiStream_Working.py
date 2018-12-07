# Dartmouth College, Winter 2018/2019

# --------------------------- IMPORTS --------------------------- #
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time
import web
import subprocess
from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types
import io
import time

from lcd import LCD

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

display = LCD()
creds = service_account.Credentials.from_service_account_file('./.google-cloud-creds.json')
client = vision.ImageAnnotatorClient(credentials=creds)

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

def recognize():
    display.clear()
    display.display_message("Recognizing...", row=0)

    with io.open("/tmp/stream/pic.jpg", 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content = content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    for label in labels:
        display.clear()
        display.display_message(label.description, row=0)
        display.display_message(" (" + str(round(label.score * 100)) + "%)", row=1)
        time.sleep(2)
    
    display.default_message()

    #NOT STARTING STREAM AGAIN
    #camera.rotation = 180
    #camera.start_preview(fullscreen = False, window = (0, 0, 720, 720))
    #camera.capture('/home/pi/Desktop/testresize.jpg', resize = (360, 360))
    #camera.capture('/home/pi/Desktop/test.jpg')

# --------------------------- WEB --------------------------- #
try: 
    web.server_start()
    web.arbitrary_html( "<img src='https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fcbsnews1.cbsistatic.com%2Fhub%2Fi%2Fr%2F2013%2F04%2F24%2F5e4d566c-c41a-11e2-a43e-02911869d855%2Fthumbnail%2F620x350%2Ffbec6f2b9675ed568f6dc091e178c4c2%2Fdartmouth_college_generic_1088711_fullwidth.jpg&f=1'> </img>" )
    
    #Display Stream
    web.arbitrary_html( "<br/>" )
    web.arbitrary_html( "<img src='http://10.81.11.186:8080/?action=stream'> </img>" )

    #Buttons
    web.arbitrary_html( "<br/>" )
    web.register( "<button>End Stream</button>", end_stream )
    web.register( "<button>Recognize!!</button>", recognize )

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

