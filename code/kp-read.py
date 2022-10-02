import sound, random
from itertools import groupby
from time import sleep

# Musical notes and their frequencies
C4,CS4,D4,DS4,E4,F4,FS4,G4,GS4,A4,AS4,B4 = (
    261.6256, 277.1826, 293.6648, 311.1270,
    329.6276, 349.2282, 369.9944, 391.9954,
    415.3047, 440.0000, 466.1638, 493.8833)
C5,CS5,D5,DS5,E5,F5,FS5,G5,GS5,A5,AS5,B5 = (
    523.2511, 554.3653, 587.3295, 622.2540,
    659.2551, 698.4565, 739.9888, 783.9909,
    830.6094, 880.0000, 932.3275, 987.7666)
C6,CS6,D6,DS6 =(
    1046.502, 1108.731, 1174.659, 1244.508)

# Mapping of Kp values to musical notes
kpToNote = { "0 ": C4,
             "0+": CS4,
             "1-": D4,
             "1 ": DS4,
             "1+": E4,
             "2-": F4,
             "2 ": FS4,
             "2+": G4,
             "3-": GS4,
             "3 ": A4,
             "3+": AS4,
             "4-": B4,
             "4 ": C5,
             "4+": CS5,
             "5-": D5,
             "5 ": DS5,
             "5+": E5,
             "6-": F5,
             "6 ": FS5,
             "6+": G5,
             "7-": GS5,
             "7 ": A5,
             "7+": AS5,
             "8-": B5,
             "8 ": C6,
             "8+": CS6,
             "9-": D6,
             "9 ": DS6 }

cMajorScale = [C4, D4, E4, F4, G4, A4, B4,
               C5, D5, E5, F5, G5, A5, B5,
               C6, D6, E6, F6, G6, A6, B6,
               C7, D7, E7, F7, G7, A7, B7]

kp = ["0 ", "0+", "1-", "1 ", "1+", "2-", "2 ", "2+",
      "3-", "3 ", "3+", "4-", "4 ", "4+", "5-", "5 ", "5+",
      "6-", "6 ", "6+", "7-", "7 ", "7+", "8-", "8 ", "8+",
      "9-", "9"]



# Beats per minute
BPM = 120
# Duration of whole, half, quarter and eighth notes
wNote = (60/BPM) * 4
hNote, qNote, eNote = (wNote/2, wNote/4, wNote/8)
notes =[wNote, hNote, qNote, eNote]

stream = sound.init()

kpValues = []
with open("./kp2021-orig.txt") as file:
    for index, line in enumerate(file):
        if index != 0:
            for charIndex in range(9,25,2):
                kpValues.append(line[charIndex : charIndex+2])
#print(kpValues)
print("Kp value count: " + str(len(kpValues)))

def scaleTones(kpValues):
    for kpValue in kpValues:
        try:
            sound.playTone(stream, cMajorScale[ kp.index(kpValue) ], eNote)
        except KeyboardInterrupt:
            break


def basicTones(kpValues):
    for kp in kpValues:
        try:
            sound.playTone(stream, kpToNote[kp], eNote)
        except KeyboardInterrupt:
            break
        
def basicTonesWithRests(kpValues):
    for kp in kpValues:
        try:
            sound.playTone(stream, kpToNote[kp], qNote/2)
            sleep(qNote/2)
        except KeyboardInterrupt:
            break

def basicTonesWithLongTones(kpValues):
    adjustedKpList = [(kp, list(group)) for kp, group in groupby(kpValues)]
    # [('1-', ['1-']), ('0+', ['0+', '0+']), ...]
    for (kp, group) in adjustedKpList:
        try:
            sound.playTone(stream, kpToNote[kp], eNote * len(group))
        except KeyboardInterrupt:
            break

def basicTonesWithLongTonesRests(kpValues):
    adjustedKpList = [(kp, list(group)) for kp, group in groupby(kpValues)]
    # [('1-', ['1-']), ('0+', ['0+', '0+']), ...]
    for (kp, group) in adjustedKpList:
        try:
            if kp == "0 ":
                sleep(eNote * len(group))
            else:
                sound.playTone(stream, kpToNote[kp], eNote * len(group))
        except KeyboardInterrupt:
            break

#basicTones(kpValues)
#basicTonesWithRests(kpValues)
#basicTonesWithLongTones(kpValues)
#basicTonesWithLongTonesRests(kpValues)
scaleTones(kpValues)

stream.close()
