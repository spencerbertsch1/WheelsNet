from picamera import PiCamera

camera = PiCamera()

pic_path = "tmp/img.png"
camera.capture(pic_path, format="png")

camera.close()
