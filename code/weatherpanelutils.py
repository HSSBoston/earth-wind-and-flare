import subprocess
from PIL import Image, ImageDraw
from datetime import datetime

def verticalConcat(ewImage, swImage):
    cols, rows = (64, 64)
    panelImage = Image.new("RGB", (cols, rows))
    panelImage.paste(ewImage, (0, 0))
    panelImage.paste(swImage, (0, 32))
    return panelImage

def getCurrentTime():
    doubleDigitHr = doubleDigitMin = "00"
    dt = datetime.now()
    if dt.hour // 10 == 0:
        doubleDigitHr = "0" + str(dt.hour)
    else:
        doubleDigitHr = str(dt.hour)
    if dt.minute // 10 == 0:
        doubleDigitMin = "0" + str(dt.minute)
    else:
        doubleDigitMin = str(dt.minute)
    return (str(dt.year), str(dt.month), str(dt.day), doubleDigitHr, doubleDigitMin)

def tempSymbol(metric):
    image = Image.new("RGB", (5, 6))
    color = (255, 178, 102)
    draw = ImageDraw.Draw(image)
    if metric == "imperial":
        draw.line((0, 0, 0, 5), fill=color, width=1)
        draw.line((1, 0, 3, 0), fill=color, width=1)
        draw.line((1, 2, 2, 2), fill=color, width=1)
    else:
        draw.line((0, 1, 0, 4), fill=color, width=1)
        draw.line((1, 0, 3, 0), fill=color, width=1)
        draw.line((4, 1, 4, 1), fill=color, width=1)
        draw.line((1, 5, 3, 5), fill=color, width=1)
        draw.line((4, 4, 4, 4), fill=color, width=1)
    return image

def getKUnit(color):
    image = Image.new("RGB", (4, 6))
    draw = ImageDraw.Draw(image)
    draw.line((0, 0, 0, 5), fill=color, width=1)
    draw.line((1, 2, 3, 0), fill=color, width=1)
    draw.line((1, 2, 3, 4), fill=color, width=1)
    draw.line((3, 5, 3, 5), fill=color, width=1)
    return image

def getKpUnit(color):
    image = Image.new("RGB", (9, 6))
    draw = ImageDraw.Draw(image)
    # K
    draw.line((0, 0, 0, 5), fill=color, width=1)
    draw.line((1, 2, 3, 0), fill=color, width=1)
    draw.line((1, 2, 3, 4), fill=color, width=1)
    draw.line((3, 5, 3, 5), fill=color, width=1)

    # P
    draw.line((5, 0, 5, 5), fill=color, width=1)
    draw.line((6, 0, 7, 0), fill=color, width=1)
    draw.line((8, 1, 8, 2), fill=color, width=1)
    draw.line((6, 3, 7, 3), fill=color, width=1)

    return image

def getColorForKIndex(k):
    green = (128, 255, 0)
    yellow = (255, 255, 0)
    lightOrange = (255, 204, 153)
    darkOrange = (255, 128, 0)
    red = (255, 102, 102)
    darkRed = (204, 0, 0)

    if k == 0: # green
        return green
    elif k == 1: # yellow
        return yellow
    elif k == 2: # light orange
        return lightOrange
    elif k == 3: # dark orange
        return darkOrange
    elif k == 4: # red
        return red
    elif k == 5: # dark red
        return darkRed
    return green

def displayImages(images, cols, rows, interval):
#    for i in range(int(60/(len(images) * interval))):
    while True: 
        imageFiles = " ".join(images)
        command1 = "sudo ~/iot-python/rpi-rgb-led-matrix/utils/led-image-viewer "
        command2 = "--led-no-hardware-pulse --led-cols " + str(cols) + " "
        command3 = "--led-rows " + str(rows) + " "
        command4 = "--led-brightness 75 "
        command5 = "--led-slowdown-gpio 2 "
        command6 = "-C -w" + str(interval) + " "
        command = command1 + command2 + command3 + command4 + command5 +\
                      command6 + imageFiles
        print(command)
        subprocess.run(command, shell=True)
