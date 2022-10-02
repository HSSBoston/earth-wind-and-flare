from weatherpanelutils import getCurrentTime, tempSymbol
from PIL import Image, ImageDraw, ImageFont
from openweather import *

imageFileName = "eweather.png"
earthWeatherIconFileName = "eweatherIcon.png"

def getWeatherInfo(zipCode, countryCode, metric, weatherApiKey):
    weatherData = getZipWeather(zipCode, countryCode, metric, weatherApiKey)

    ShortCond, longCond, iconId = getCurrentWeatherCondition(weatherData)
    iconImage = getWeatherIconImage(iconId, "4x")
    iconImage.save(earthWeatherIconFileName)
    
    temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)
    daytimeTemp, minTemp, maxTemp, avgHumidity = getTempHumidityToday(weatherData)
    return (str(round(temp)), str(round(minTemp)),
            str(round(maxTemp)), str(round(avgHumidity)))


def get64x32Image(zipCode, countryCode, metric, weatherApiKey):
    cols, rows = (64, 32)
    year, month, day, hr, min = getCurrentTime()
    temp, minTemp, maxTemp, humidity = getWeatherInfo(zipCode, countryCode, metric, weatherApiKey)
    
    image = Image.new("RGB", (cols, rows), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    ### weather icon
    weatherIcon = Image.open("earthWeatherIcon.png")
    resizedWeatherIcon = weatherIcon.resize((20, 20))
    image.paste(resizedWeatherIcon, (0,12))
    
    ### month and day
    font = ImageFont.load_default()
    draw.text((1, 0), month+"/"+day, fill=(112,128,144), font=font)
    draw.text((33, 0), hr+":"+min, fill=(255, 255, 255), font=font)

    ### current temp
    draw.text((32, 10), temp, fill=(255, 178, 102), font=font)

    ### metric: F or C
    tempImage = tempSymbol(metric)
    image.paste(tempImage, (46, 13))

    ### min temp in the next 24 hrs
    draw.text((24, 21), minTemp, fill=(135,206,250), font=font)

    ### vertical separator
    draw.text((34, 21), "|", fill=(16,16,16), font=font)

    ### max temp in the next 24 hrs
    draw.text((38, 21), maxTemp, fill=(255,99,71), font=font)

    ### vertical separator
    draw.text((48, 21), "|", fill=(16,16,16), font=font)

    ### avg humidity in the next 24 hrs
    draw.text((52, 21), humidity, fill=(0, 128, 255), font=font)
    
    draw.line((0, 32, 64, 32), fill=(16, 16, 16), width=1)

    ### horizontal separator
    image.save("eweather.png")
    
    return image



