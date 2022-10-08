## Data, Colors and Icons Displayed on our LED Panel

Our LED panel displays earth weather information on its upper half and space weather information on its bottom half.

<p align="center">
<img src="../images/panel.jpg" width="500"></a>
</p>

Our Raspberry Pi Python program gets the current date and time with Python's [datetime module](https://docs.python.org/3/library/datetime.html) and displays them at the top of the panel.

### Earth Weather Data

Our Python program downloads the current and forecast weather data from [OpenWeatherMap](https://openweathermap.org/) and displays them at the upper right portion of the panel.  

- Current temperature (Fahrenheit/Celsius)
- Maximum and minimum temperature in the next 24 hours (Fahrenheit/Celsius)
- Average humidity in the next 24 hours (%)

Also, our program downloads the [current weather condition](https://openweathermap.org/weather-conditions) from OpenWeatherMap and displays an icon for the condition at the upper left portion of the panel. It displays one of the following icons:

| Icon      | Weather |
| :----:      | :---      |
| <img src="../images/01d@2x.png" width="50"> | clear sky|
| <img src="../images/02d@2x.png" width="50"> | Few clouds |
| <img src="../images/03d@2x.png" width="50"> | Scattered clouds |
| <img src="../images/04d@2x.png" width="50"> | Broken clouds |
| <img src="../images/09d@2x.png" width="50"> | Shower rain |
| <img src="../images/10d@2x.png" width="50"> | Rain |
| <img src="../images/11d@2x.png" width="50"> | Thunderstorm |
| <img src="../images/13d@2x.png" width="50"> | Snow |
| <img src="../images/50d@2x.png" width="50"> | Mist |


### Space Weather Data

Our Python program downloads the current space weather data from a variety of international sources and displays them at the bottom right portion of the panel.

- Geomagnetic disturbance (K-index) in the US:
  - Downloaded from [NOAA Space Weather Prediction Center's FTP server](ftp://ftp.swpc.noaa.gov/pub/lists/geomag/AK.txt)
- Geomagnetic disturbance (K-index) in Japan:
   - Downloaded from the [Web site of Kakioka Geomagnetic Observatory](https://www.kakioka-jma.go.jp/)
- Planetary geomagnetic disturbance (Kp-index):
   - Downloaded from [NOAA Space Weather Prediction Center's FTP server](ftp://ftp.swpc.noaa.gov/pub/lists/geomag/AK.txt)
   - Downloaded from the [Web site of German Research Center for Geosciences](https://www-app3.gfz-potsdam.de/kp_index/Kp_ap_nowcast.txt)
- Solar wind speed:
   - Downloaded from [NOAA Space Weather Prediction Center's FTP server](ftp://ftp.swpc.noaa.gov/pub/lists/ace2/noaaSolarWind_ace_swepam_1h.txt). This data is what NASA’s Advanced Composition Explorer (ACE) satellite has measured.
- Next encounter day (perihelion day) of Parker Solar Probe (PSP):
   - Downloaded from the [Web site of Johns Hopkins University Applied Physics Laboratory](http://parkersolarprobe.jhuapl.edu/The-Mission/index.php#Timeline)

K- and Kp-index values are colored based on the [NOAA scape weather scale](https://www.swpc.noaa.gov/noaa-scales-explanation):

| Planetary geomagnetic disturbance (Kp-index)| NOAA Scale| Color|
| :---    | :--- | :--- |
| Kp <= 4 | 0 | Green |
| Kp == 5 | 1 | Yellow |
| Kp == 6 | 2 | Dark yellow |
| Kp == 7 | 3 | Orange |
| Kp == 8 | 4 | Severe |
| Kp == 9 | 5 | Extreme |


Also, our program displays an icon for the current Kp-index value at the bottom left portion of the panel. It displays one of the following icons:

| Planetary geomagnetic disturbance (Kp-index) | NOAA Scale| Icon|
| :---      | :---      | :----: |
| Kp <= 4 | 0 | <img src="../code/spacewheter_0_green.png" width="75"> |
| Kp == 5 | 1 |<img src="../code/spacewheter_1_yellow.png" width="75"> |
| Kp == 6 | 2 | <img src="../code/spacewheter_2_lightorange.png" width="75"> |
| Kp == 7 | 3 | <img src="../code/spacewheter_3_darkorange.png" width="75"> |
| Kp == 8 | 4 | <img src="../code/spacewheter_4_red.png" width="75"> |
| Kp == 9 | 5 | <img src="../code/spacewheter_5_darkred.png" width="75"> |
