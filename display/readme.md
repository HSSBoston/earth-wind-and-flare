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

| Icon      | Weather |
| :----:      | :---      |
| <img src="../code/spacewheter_0_green.png" width="75"> | clear sky|
| <img src="../code/spacewheter_1_yellow.png" width="75"> | Few clouds |
| <img src="../code/spacewheter_2_lightorange.png" width="75"> | Scattered clouds |
| <img src="../code/spacewheter_3_darkorange.png" width="75"> | Broken clouds |
| <img src="../code/spacewheter_4_red.png" width="75"> | Shower rain |
| <img src="../code/spacewheter_5_darkred.png" width="75"> | Rain |


space weather (geomagnetic disturbance in Kp-index). K- and Kp-index values are colored on the panel based on the NOAA scale.
