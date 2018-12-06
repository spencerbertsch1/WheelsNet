from picamera import PiCamera

from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types

camera = PiCamera()

pic_path = "tmp/img.png"
camera.capture(pic_path, format="png")

camera.close()

creds = service_account.Credentials.from_service_account_file('./google-cloud-creds.json')
client = vision.ImageAnnotatorClient(credentials=creds)

with io.open(pic_path, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content = content)

response = client.label_detection(image=image)
labels = response.label_annotations

print "Labels:"
for label in labels:
    print label
