import sys, eweather, sweather
from PIL import Image, ImageDraw
from weatherpanelutils import verticalConcat, displayImages

cols = 64
rows = 64
weatherApiKey = ""
zipCode = "01730"
countryCode = "US"
metric = "imperial"

extra64x64images = []
# Example: extra64x64images = ["anim1.gif", "anim2.gif", "anim3.gif"]
extra64x32images = []
# Example: extra64x64images = ["anim1.gif", "anim2.gif", "anim3.gif"]
imageToImageInterval = 5

if countryCode not in ("US", "JP"):
    print("Invalid country code:", countryCode, "Choose US or Japan.")
    sys.exit()
if metric not in ("imperial", "metric"):
    print("Invalid unit:", metric, "Choose imperial or metric")
    sys.exit()

while True:
    try:
        if cols==64 and rows==64:
            weatherFile = "64x64_es_weather.png"
            ewImage = eweather.get64x32Image(zipCode, countryCode, metric, weatherApiKey)
            swImage = sweather.get64x32Image(countryCode, metric)
            panelImage = verticalConcat(ewImage, swImage)
            panelImage.save(weatherFile)
            displayImages([weatherFile] + extra64x64images, 64, 64, imageToImageInterval)
        elif cols==64 and rows==32:
            eWeatherFile = "64x32_e_weather.png"
            sWeatherFile = "64x32_s_weather.png"
            ewImage = eweather.get64x32Image(zipCode, countryCode, metric, weatherApiKey)
            ewImage.save(eWeatherFile)
            swImage = sweather.get64x32Image(countryCode, metric)
            swImage.save(sWeatherFile)
            displayImages([eWeatherFile, sWeatherFile] + extra64x32images,
                          64, 32, imageToImageInterval)
        else:
            print("Invalid cols/rows:", (cols, rows), "Choose 64x64 or 64x32")
            break
    except KeyboardInterrupt:
        break
