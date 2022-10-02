import ftplib, requests, datetime
from weatherpanelutils import getCurrentTime, getColorForKIndex, getKUnit, getKpUnit
from PIL import Image, ImageDraw, ImageFont

noaaFtpHost = "ftp.swpc.noaa.gov"
port = 21
user = passwd = "anonymous"
noaaGeomagDir = "pub/lists/geomag/"
kFileNameToDownload = "AK.txt"
kIndexFileName = "noaaGeomagAK.txt"
noaaSolarWindDir = "pub/lists/ace2/"
solarWindFileName = "noaaSolarWind_ace_swepam_1h.txt"
kakiokaUrl = "http://www.kakioka-jma.go.jp/kansokuka/auto1hk.js"
imageFileName = "sweather.png"

fontBIG = ImageFont.load_default()
fontUnit = font = ImageFont.load_default()

def getKandNoaaScale(countryCode):
    k = kp = noaaScaleK = noaaScaleKp = 0
    planetaryKs = []

    with ftplib.FTP() as ftp:
        try:
            ftp.connect(noaaFtpHost, port)
            ftp.login(user, passwd)
            ftp.cwd(noaaGeomagDir)
            with open(kIndexFileName, "wb") as f:
                ftp.retrbinary("RETR " + kFileNameToDownload, f.write)
        except ftplib.all_errors as e:
            print("FTP error: ", e)
    
    with open(kIndexFileName) as f:
        lines = f.readlines()
    
    for line in lines:
        if line.startswith("Planetary"):
            planetaryKs = planetaryKs + line.split()[3:]
    try:
        planetaryK = planetaryKs[ planetaryKs.index("-1") - 1 ]
        print("Kp: ", planetaryK)
        kp = int(planetaryK)
    except ValueError:
        print("Kp not found. Using Kp=0.")
    
    if kp < 5:
        noaaScaleKp = 0
    else:
        noaaScaleKp = kp - 4
    print("Kp NOAA scale", noaaScaleKp)

    if countryCode == "US":
        boulderKs = []
        for line in lines:
            if line.startswith("Boulder"):
                boulderKs = boulderKs + line.split()[5:]
        try:
            boulderK = boulderKs[ boulderKs.index("-1") - 1 ]
            print("Boulder (US) K: ", boulderK)
            k = int(boulderK)
        except ValueError:
            print("Boulder (US) K not found. Using K=0.")
    elif countryCode == "JP":
        response = requests.get(kakiokaUrl)
        kakiokaWebPage = response.text
        kakiokaK = kakiokaWebPage[ kakiokaWebPage.find("</a>=") + 5 ]
        print("Kakioka (JP), K: ", kakiokaK)
        k = int(kakiokaK)
    else:
        print("Wrong country code specified")

    if k < 5:
        noaaScaleK = 0
    else:
        noaaScaleK = k - 4
    print("K NOAA scale", noaaScaleK)
        
    return k, noaaScaleK, kp, noaaScaleKp


def getSolarWindData(metric):
    solarWindSpeed = "0"
    year, month, day, hr, min = getCurrentTime()   
    if int(month) // 10 == 0:
        month = "0" + str(month)
    solarWindFileNameToDownload = year + month + "_ace_swepam_1h.txt"
    
    with ftplib.FTP() as ftp:
        try:
            ftp.connect(noaaFtpHost, port)
            ftp.login(user, passwd)
            ftp.cwd(noaaSolarWindDir)
            with open(solarWindFileName, "wb") as f:
                ftp.retrbinary("RETR " + solarWindFileNameToDownload, f.write)
        except ftplib.all_errors as e:
            print("FTP error: ", e)
    
    with open(solarWindFileName) as f:
        lines = f.readlines()

    lineIndex = len(lines) - 1
    while not lines[lineIndex].startswith("#"):
        speed = lines[lineIndex].split()[8]
        if speed != "-9999.9":
            solarWindSpeed = speed
            break
        else:
            lineIndex = lineIndex - 1

    solarWindSpeed = float(solarWindSpeed) 
    if metric == "imperial":
        solarWindSpeed = solarWindSpeed * 1.609
        solarWindSpeed = int(solarWindSpeed)
        print("Solar wind speed (mph): ", solarWindSpeed)
    elif metric == "metric":
        solarWindSpeed = int(solarWindSpeed)    
        print("Solar wind speed (kph): ", solarWindSpeed)
    return solarWindSpeed


def get64x32Image(countryCode, metric):
    cols, rows = (64, 33)
    k, noaaScaleK, kp, noaaScaleKp = getKandNoaaScale(countryCode)
    solarWindSpeed = getSolarWindData(metric)
    
    image = Image.new("RGB", (cols, rows), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Test different k/kp values
    # k = 5
    # kp = 5
    
    kcolor = getColorForKIndex(kp)
    kImage = getKUnit(kcolor)
    kpImage = getKpUnit(kcolor)
    kphImage = Image.open("kph.png")
    mphImage = Image.open("mph.png")
    pspImage = Image.open("pspday.png")

    ### K and its unit
    draw.text((32, 0), str(k), fill=kcolor, font=fontBIG)
    image.paste(kImage, (40,3))

    ### Kp and its unit
    draw.text((47, 0), str(kp), kcolor, font=fontBIG)
    image.paste(kpImage, (55,3))

    ### Solar wind speed
    draw.text((32, 10), str(solarWindSpeed), fill=(135,206,250), font=font)
    if metric == "imperial":
        image.paste(mphImage, (51, 14))
    else:
        image.paste(kphImage, (51, 14))

    if k == 0: # green
        icon = Image.open("spacewheter_0_green.png")
    elif k == 1: # yellow
        icon = Image.open("spacewheter_1_yellow.png")
    elif k == 2: # light orange
        icon = Image.open("spacewheter_2_lightorange.png")
    elif k == 3: # dark orange
        icon = Image.open("spacewheter_3_darkorange.png")
    elif k == 4: # red
        icon = Image.open("spacewheter_4_red.png")
    elif k == 5: # dark red
        icon = Image.open("spacewheter_5_darkred.png")

    image.paste(icon, (0, 0))

    ### E-Day (Encounter day)
    image.paste(pspImage, (31, 22))
    # draw.text((10, 20), "PSP 12/11", fill=(112,128,144), font=font)

    image.save(imageFileName)
    return image


### Test
#print(getKandNoaaScale("US"))
#print(getKandNoaaScale("JP"))

#print( getSolarWindData("imperial") )
#print( getSolarWindData("metric") )
