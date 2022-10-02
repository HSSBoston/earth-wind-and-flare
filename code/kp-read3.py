import sound, random
from itertools import groupby
from time import sleep

# Musical notes and their frequencies
C3,Cs3,D3,Ds3,E3,F3,Fs3,G3,Gs3,A3,As3,B3 =(
    130.8128, 138.5913, 146.8324, 155.5635,
    164.8138, 174.6141, 174.6141, 195.9977,
    207.6523, 220.0000, 233.0819, 246.9417)
C4,Cs4,D4,Ds4,E4,F4,Fs4,G4,Gs4,A4,As4,B4 = (
    261.6256, 277.1826, 293.6648, 311.1270,
    329.6276, 349.2282, 369.9944, 391.9954,
    415.3047, 440.0000, 466.1638, 493.8833)
C5,Cs5,D5,Ds5,E5,F5,Fs5,G5,Gs5,A5,As5,B5 = (
    523.2511, 554.3653, 587.3295, 622.2540,
    659.2551, 698.4565, 739.9888, 783.9909,
    830.6094, 880.0000, 932.3275, 987.7666)
C6,Cs6,D6,Ds6,E6,F6,Fs6,G6,Gs6,A6,As6,B6 = (
    1046.502, 1108.731, 1174.659, 1244.508,
    1318.510, 1396.913, 1479.978, 1567.982,
    1661.219, 1760.000, 1864.655, 1975.533)
C7,Cs7,D7,Ds7,E7,F7,Fs7,G7,Gs7,A7,As7,B7 = (
    2093.005, 2217.461, 2349.318, 2489.016,
    2637.020, 2793.826, 2959.955, 3135.963,
    3322.438, 3322.438, 3729.310, 3951.066)
C8,Cs8,D8,Ds8,E8,F8,Fs8,G8,Gs8,A8,As8,B8 = (
    4186.009, 4434.922, 4698.636, 4978.032,
    5274.041, 5587.652, 5919.911, 6271.927,
    6644.875, 7040.000, 7458.620, 7902.133)

cMajorScale = [C4, D4, E4, F4, G4, A4, B4,
               C5, D5, E5, F5, G5, A5, B5,
               C6, D6, E6, F6, G6, A6, B6,
               C7, D7, E7, F7, G7, A7, B7]
gMajorScale = [G4, A4, B4, C5, D5, E5, Fs5,
               G5, A5, B5, C6, D6, E6, Fs6,
               G6, A6, B6, C7, D7, E7, Fs7,
               G7, A7, B7, C8, D8, E8, Fs8]
bfMajorScale = [As3, C4, D4, E4, F4, G4, A4,
                As4, C5, D5, E5, F5, G5, A5,
                As5, C6, D6, E6, F6, G6, A6,
                As6, C7, D7, E7, F7, G7, A7]
aMinorScale = [A3, B3, C4, D4, E4, F4, G4,
               A4, B4, C5, D5, E5, F5, G5,
               A5, B5, C6, D6, E6, F6, G6,
               A6, B6, C7, D7, E7, F7, G7]
cMinorMelodicScale = [C4, D4, Ds4, F4, G4, A4, B4,
                      C5, D5, Ds5, F5, G5, A5, B5,
                      C6, D6, Ds6, F6, G6, A6, B6,
                      C7, D7, Ds7, F7, G7, A7, B7]
cMajorPentatonicScale = [C3, D3, E3, G3, A3,
                         C4, D4, E4, G4, A4,
                         C5, D5, E5, G5, A5,
                         C6, D6, E6, G6, A6,
                         C7, D7, E7, G7, A7,
                         C8, D8, E8, G8, A8]
cBluesScale = [C3, Ds3, F3, Fs3, G3, As3,
               C4, Ds4, F4, Fs4, G4, As4,
               C5, Ds5, F5, Fs5, G5, As5,
               C6, Ds6, F6, Fs6, G6, As6,
               C7, Ds7, F7, Fs7, G7, As7,
               C8, Ds8, F8, Fs8, G8, As8]

cMajorChordScale = [
    [C4,E4,G4], [D4,F4,A4], [E4,G4,B4], [F4,A4,C5], [G4,B4,D5], [A4,C5,E5], [B4,D5,F5],
    [C5,E5,G5], [D5,F5,A5], [E5,G5,B5], [F5,A5,C6], [G5,B5,D6], [A5,C6,E6], [B5,D6,F6],
    [C6,E6,G6], [D6,F6,A6], [E6,G6,B6], [F6,A6,C7], [G6,B6,D7], [A6,C7,E7], [B6,D7,F7],
    [C7,E7,G7], [D7,F7,A7], [E7,G7,B7], [F7,A7,C8], [G7,B7,D8], [A7,C8,E8], [B7,D8,F8]]


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
with open("./2022-09.txt") as file:
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

def scaleTonesWithLongTonesRests(kpValues):
    adjustedKpList = [(kpValue, list(group)) for kpValue, group in groupby(kpValues)]
    # e.g., [('1-', ['1-']), ('0+', ['0+', '0+']), ...]
    for (kpValue, group) in adjustedKpList:
        try:
            if kpValue == "0 ":
                sleep(eNote * len(group))
            else:
                sound.playTone(stream, cMajorScale[ kp.index(kpValue) ], eNote * len(group))
        except KeyboardInterrupt:
            break

def scaleTonesWithLongTonesRestsIntensity(kpValues):
    adjustedKpList = [(kpValue, list(group)) for kpValue, group in groupby(kpValues)]
    # e.g., [('1-', ['1-']), ('0+', ['0+', '0+']), ...]
    fiveOrHigherKp = ["5-", "5 ", "5+", "6-", "6 ", "6+", "7-", "7 ", "7+", "8-", "8 ", "8+", "9-", "9"]
    for (kpValue, group) in adjustedKpList:
        try:
            if kpValue == "0 ":
                sleep(eNote * len(group))
            else:
                if kpValue in fiveOrHigherKp:
                    print(kpValue)
                    sound.playTone(stream, cMajorScale[ kp.index(kpValue) ], eNote * len(group))
                else:
                    sound.playTone(stream, cMajorScale[ kp.index(kpValue) ], eNote * len(group), 0.5)
        except KeyboardInterrupt:
            break

def scaleChordToneWithLongTonesRestsIntensity(kpValues):
    adjustedKpList = [(kpValue, list(group)) for kpValue, group in groupby(kpValues)]
    # e.g., [('1-', ['1-']), ('0+', ['0+', '0+']), ...]
    fiveOrHigherKp = ["5-", "5 ", "5+", "6-", "6 ", "6+", "7-", "7 ", "7+", "8-", "8 ", "8+", "9-", "9"]
    for (kpValue, group) in adjustedKpList:
        try:
            if kpValue == "0 ":
                sleep(eNote * len(group))
            else:
                if kpValue in fiveOrHigherKp:
                    print(kpValue)
                    sound.playChordTone(stream, cMajorChordScale[ kp.index(kpValue) ], eNote * len(group))
                else:
                    sound.playChordTone(stream, cMajorChordScale[ kp.index(kpValue) ], eNote * len(group), 0.5)
        except KeyboardInterrupt:
            break

#scaleTones(kpValues)
#scaleTonesWithLongTonesRests(kpValues)
#scaleTonesWithLongTonesRestsIntensity(kpValues)
scaleChordToneWithLongTonesRestsIntensity(kpValues)

stream.close()
