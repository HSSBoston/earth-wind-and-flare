# Library to access and use OpenWeatherMap
# Sept 21, 2022 v0.05
# Hanna Suzuki (https://github.com/hssboston)
# Jun Suzuki (https://github.com/jxsboston)
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/
#
# This library uses OpenWeather's One Call API 1.0 and
# Geocoding API:
#   https://openweathermap.org/api/one-call-api
#   https://openweathermap.org/api/geocoding-api
# OpenWeather's Geocoding API uses ISO 3166 country code:
#   https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
# As for weather conditions ("main" and "description"), see:
#   https://openweathermap.org/weather-conditions

import requests, json
from PIL import Image
from io import BytesIO
# from geopy.geocoders import Nominatim
# 
# nominatimAppName = "iot" + os.uname()[1]
# geolocator = Nominatim(user_agent=nominatimAppName)

def getLatLonWeather(lat, lon, unit, apiKey):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + \
              str(lat) + "&lon=" + str(lon) + \
              "&exclude=minutely,hourly" + \
              "&appid=" + apiKey + "&units=" + unit
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getUsWeather(cityName, stateCode, unit, apiKey):
    lat, lon = getUsLatLon(cityName, stateCode, apiKey)
    if lat is not None or lon is not None: 
        return getLatLonWeather(lat, lon, unit, apiKey)
    else:
        print("Geocoding failed: Invalid Lat/lon.")
        return None
        

def getIntlWeather(cityName, countryCode, unit, apiKey):
    lat, lon = getIntlLatLon(cityName, countryCode, apiKey)
    if lat is not None or lon is not None: 
        return getLatLonWeather(lat, lon, unit, apiKey)
    else:
        print("Geocoding failed: Invalid Lat/lon.")
        return None

def getZipWeather(zipCode, countryCode, unit, apiKey):
    lat, lon = getZipLatLon(zipCode, countryCode, apiKey)
    if lat is not None or lon is not None: 
        return getLatLonWeather(lat, lon, unit, apiKey)
    else:
        print("Geocoding failed: Invalid Lat/lon.")
        return None

def getCurrentTempHumidity(response):
    if response == None:
        return (None, None, None)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            temp = currentDict["temp"]
            feelsLike = currentDict["feels_like"]
            humidity = currentDict["humidity"]
            return (temp, feelsLike, humidity)
        else:
            return (None, None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return (None, None, None)

def getCurrentRain(response):
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "rain" in currentDict:
                rainDict = currentDict["rain"]
                rain1h = rainDict["rain.1h"]
                return rain1h
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentSnow(response): 
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "snow" in currentDict:
                rainDict = currentDict["snow"]
                snow1h = rainDict["snow.1h"]
                return snow1h
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentWind(response): 
    if response == None:
        return None
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "wind_speed" in currentDict:
                windSpeed = currentDict["wind_speed"]
            else:
                windSpeed = None
            if "wind_deg" in currentDict:
                windDeg = currentDict["wind_deg"]
            else:
                windDeg = None
            if "wind_gust" in currentDict:
                windGust = currentDict["wind_gust"]
            else:
                windGust = None
            return (windSpeed, windDeg, windGust)
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentWeatherCondition(response):
    if response == None:
        return (None, None, None)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "weather" in currentDict:
                weatherDict = currentDict["weather"][0]
                main = weatherDict["main"]
                description = weatherDict["description"]
                iconId = weatherDict["icon"]
                return (main, description, iconId)
            else:
                return (None, None, None)
        else:
            return (None, None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentAtmosphericPressure(response):
    if response == None:
        return None
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "pressure" in currentDict:
                return currentDict["pressure"]
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentUvi(response): 
    if response == None:
        return None
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "uvi" in currentDict:
                return currentDict["uvi"]
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getCurrentCloudiness(response):
    if response == None:
        return None
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "current" in responseDict:
            currentDict = responseDict["current"]
            if "clouds" in currentDict:
                return currentDict["clouds"]
            else:
                return None
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None

def getWeatherIconImage(iconId, size):
    if iconId == None:
        return None
    if size != "2x" and size != "4x":
        return None
    url = "http://openweathermap.org/img/wn/" + \
              iconId + "@" + size +".png"
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        if image != None:
            return image
        else:
            print("Donwnloaded icon not valid.")
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None
        

def getTempHumidityToday(response):
    return getTempHumidityForecast(response, 0)

def getTempHumidityTomorrow(response):
    return getTempHumidityForecast(response, 1)

def getTempHumidityForecast(response, daysLater):
    if response == None:
        return (None, None, None, None)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "daily" in responseDict:
            forecast = responseDict["daily"][daysLater]
            dayTemp = forecast["temp"]["day"]
            minTemp = forecast["temp"]["min"]
            maxTemp = forecast["temp"]["max"]
            humidity = forecast["humidity"]
            return (dayTemp, minTemp, maxTemp, humidity)
        else:
            return (None, None, None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return (None, None, None, None)

def getFeelsLikeToday(response):
    return getFeelsLikeForecast(response, 0)

def getFeelsLikeTomorrow(response):
    return getFeelsLikeForecast(response, 1)

def getFeelsLikeForecast(response, daysLater):
    if response == None:
        return (None, None, None, None)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "daily" in responseDict:
            forecast = responseDict["daily"][daysLater]
            morningTemp = forecast["feels_like"]["morn"]
            dayTemp = forecast["feels_like"]["day"]
            eveTemp = forecast["feels_like"]["eve"]
            nightTemp = forecast["feels_like"]["night"]
            return (morningTemp, dayTemp, eveTemp, nightTemp)
        else:
            return (None, None, None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return (None, None, None, None)

def getWeatherConditionToday(response):
    return getWeatherConditionForecast(response, 0)

def getWeatherConditionTomorrow(response):
    return getWeatherConditionForecast(response, 1)

def getWeatherConditionForecast(response, daysLater):
    if response == None:
        return (None, None, None)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "daily" in responseDict:
            forecast = responseDict["daily"][daysLater]
            weather = forecast["weather"][0]
            main = weather["main"]
            description = weather["description"]
            iconId = weather["icon"]
            return (main, description, iconId)
        else:
            return (None, None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return (None, None, None)

def getCloudinessToday(response):
    return getCloudinessForecast(response, 0)

def getCloudinessTomorrow(response):
    return getCloudinessForecast(response, 1)

def getCloudinessForecast(response, daysLater):
    if response == None:
        return None
    if daysLater > 5:
        return None
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "daily" in responseDict:
            forecast = responseDict["daily"][daysLater]
            cloudiness = forecast["clouds"]
            return cloudiness
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None


def getUsLatLon(cityName, stateCode, apiKey):
    url = "http://api.openweathermap.org/geo/1.0/direct?q=" + \
              cityName + "," + stateCode + "," + "US" + \
              "&appid=" + apiKey
    return getLatLon(url)

def getIntlLatLon(cityName, countryCode, apiKey):
    url = "http://api.openweathermap.org/geo/1.0/direct?q=" + \
              cityName + ",," + countryCode + \
              "&appid=" + apiKey
    return getLatLon(url)

def getZipLatLon(zipCode, countryCode, apiKey):
    url = "http://api.openweathermap.org/geo/1.0/zip?zip=" + \
              zipCode + "," + countryCode + \
              "&appid=" + apiKey
    response = requests.get(url)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "lat" in responseDict and "lon" in responseDict:
            lat = responseDict["lat"]
            lon = responseDict["lon"]
            return (lat, lon)
        else:
            print("OpenWeather Response Invalid: Lat/Lon Not Available.")
            return (None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return (None, None)

def getLatLon(url):
    response = requests.get(url)
    if response.status_code == 200:
        responseList = json.loads(response.text)
        firstResponse = responseList[0]
        if "lat" in firstResponse and "lon" in firstResponse:
            lat = firstResponse["lat"]
            lon = firstResponse["lon"]
            return (lat, lon)
        else:
            print("OpenWeather Response Invalid: Lat/Lon Not Available.")
            return (None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return (None, None)

# def getUsCityWeather(cityName, stateCode, unit, apiKey):
#     structuredQuery = {"city" : cityName,
#                        "state" : stateCode,
#                        "country" : "United States"}
#     location = geolocator.geocode(query=structuredQuery)
#     locationDataset = location.raw
#     return getLatLonWeather(locationDataset["lat"], locationDataset["lon"], unit, apiKey)
# 
# 
# def getUsTownWeather(townName, stateCode, unit, apiKey):
#     structuredQuery = {"town" : townName,
#                        "state" : stateCode,
#                        "country" : "United States"}
#     location = geolocator.geocode(query=structuredQuery)
#     locationDataset = location.raw
#     return getLatLonWeather(locationDataset["lat"], locationDataset["lon"], unit, apiKey)
# 
# def getIntlCityWeather(cityName, countryCode, unit, apiKey):
#     structuredQuery = {"city" : cityName,
#                        "country" : countryCode}
#     location = geolocator.geocode(query=structuredQuery)
#     locationDataset = location.raw
#     return getLatLonWeather(locationDataset["lat"], locationDataset["lon"], unit, apiKey)
