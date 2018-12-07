# WheelsNet

Dartmouth College, Winter 2018/2019 

A fun image recognition robot on wheels! 

In this project, we used a Raspberry Pi 3 as a local server to stream live video from a small, mounted camera. <br>

The pi and camera were mounted onto a remote control truck chasis, streaming back live feed of the truck's view to a computer. <br>

Live video could then be viewed through a custom web interface and still images could be captured through a GUI. <br>

Google cloud API was used to send captured images to Google's image recognition cloud based platform, and results were then sent back and displayed on the webpage. <br>

The truck could recognize objects such as chairs and tables, the presence of humans, and even haircuts. (Thanks to the help of the engineers over at Google!) 

# Software Installation
Run on the Raspberry Pi

1. Run `pip install .`
2. run `sudo raspi-config`
3. in the interface, go to "Interfacing Options"
4. turn on Camera and LCD
5. run `reboot` in your terminal

# Streaming

For this project, a Raspberry Pi 3b+ was used as a server to stream video from an onboard camera to a remote host.

Code in this folder was used to allow the pi to stream live video to another machine. 

# Streaming Installation

SOURCE: https://blog.miguelgrinberg.com/post/how-to-build-and-run-mjpg-streamer-on-the-raspberry-pi


----------- Steps to start stream with custom GUI --------------

1. Open terminal

2. Navigate to desktop by running the command: cd ~/Desktop

3. Run the python file 'PiStream.py' by running the command: python PiStream.py

4. Start a browser and navigate to the Pi's IP address: http://IP_ADDRESS:5005      <---where IP_ADDRESS should be a sequence of numbers separated by periods

5. Clean up by going back to the terminal and running the command: Ctrl-c
This stops the program and cleans up everything running in the background. 


----------- Steps to start stream without custom GUI --------------

1. Open Terminal and enter: raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0

2. Open a new window in the terminal and enter: LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www"

3. Watch the stream from another computer in your network by using -  http://<IP-address>:8080

4. Kill the stream by opening a new terminal and entering: pkill raspistill

# Google Credentials
Go to cloud.google.com/vision/docs/quickstart-client-libraries and follow the instructions to get credentials for the API. Place the credentials in the root directory of this repo with the title `.google-cloud-creds.json`.

# To Run:
`$ python main.py`
