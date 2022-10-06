## LED Panel Prototypes

We made 5 prototypes in this project.

### Prototype 1

This prototype is wall-mounted. A 64x64 LED matrix board and Raspberry Pi are attached to a backer board.

<p align="center">
<img src="../images/p1-wall.jpg" width="350">
</p>

This prototype can replay GIF animation videos after showing earth and space weather information. See the following demonstration video.

<p align="center">
<a href="https://youtu.be/fdgn-TWUL5k"><img src="../images/p1-video.jpg" width="500"></a>
</p>

To decorate this prototype, we made origami crafts that model the Sun, clouds and lightning.

<p align="center">
<img src="../images/p1-origami.jpg" width="500">
</p>

### Prototype 2

This prototype is motion-activated. Raspberry Pi is connected with a 64x64 LED matrix board and a motion sensor (Passive InfaRed sensor: PIR sensor). It turns on the board when the sensor detects nearby motion, and turns off the board if no motion is detected for a while. This way, it can better interact with panel viewers while saving power consumption.

<p align="center">
<img src="../images/p2.jpg" width="500">
</p>

Watch the following demonstration video to see how this prototype works with a motion sensor.

<p align="center">
<a href="https://youtu.be/U0wvPAjHJDc"><img src="../images/p2-video.jpg" width="500"></a>
</p>



### Prototype 3

This prototype uses a 64x32 (rectangular) LED matrix board. Our Python program can run for 64x32 boards as well as 64x64 boards. Since the 64x32 board size is too small to show both earth and space weather, it displays the two weather information in turn.

<p align="center">
<img src="../images/p3-eweather.jpg" width="400">
<img src="../images/p3-sweather.jpg" width="400">
</p>

Our Python program implements imperial and metric units, and it can switch one unit system to another:

- Fahrenheit for temperature and miles per hour (MPH) for solar sind speed.
- Celsius for temperature and Kilometers per hour (KPH) for solar wind speed.

Since this prototype was built in Japan, it shows the K-index value that a Japanese geomagnetic observatory measured.

Watch the following demonstration video to see how this prototype works.

<p align="center">
<a href="https://youtu.be/jJMIJQfBOQI"><img src="../images/p3-video.jpg" width="500"></a>
</p>


### Prototype 4

This prototype connects Raspberry Pi with a 64x64 LED matrix board and a Bluetooth speaker. Our Python program produces a piece of “music” with downloaded Kp-index values (planetary geomagnetic disturbance data) and plays it with a speaker. See [this page](../kp-music) for more details about how to map Kp-index values to musical elements. 

<p align="center">
<img src="../images/p4.jpg" width="500">
</p>

See the following demonstration video to hear how solar wind sings.

<p align="center">
<a href="https://youtu.be/4N0SlPaT1-U"><img src="../images/p4-video.jpg" width="500"></a>
</p>

We also decorated this prototype with [Zome](https://www.zometool.com).

<p align="center">
<img src="../images/p4-decoration1.jpg" width="500">

<img src="../images/p4-decoration2.jpg" width="300">
</p>
