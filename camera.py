from picamera import PiCamera

from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types
import io

class Camera:
    def __init__(self):
        self.camera = PiCamera()
        self.pic_path = "tmp/img.png" 

    def snap_photo(self):
        self.camera.capture(self.pic_path, format="png")

    def __del__(self):
        self.camera.close()

cam = Camera()
cam.snap_photo()

creds = service_account.Credentials.from_service_account_file('./.google-cloud-creds.json')
client = vision.ImageAnnotatorClient(credentials=creds)

with io.open(cam.pic_path, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content = content)

response = client.label_detection(image=image)
labels = response.label_annotations

print "Labels:"
for label in labels:
    print label.description + " (" + str(label.score) + "%)"
