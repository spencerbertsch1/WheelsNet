# WheelsNet

Dartmouth College, Winter 2018/2019 

A fun image recognition robot on wheels! 

In this project, we used a Raspberry Pi 3 as a local server to stream live video from a small, mounted camera. <br>

The pi and camera were mounted onto a remote control truck chasis and was then piloted, streaming back live feed of the truck's view to a computer. <br>

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
