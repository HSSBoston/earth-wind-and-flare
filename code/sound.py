# Library to beep and play musical tones with PyAudio
# Oct 18, 2022 v0.10
# Jun Suzuki (https://github.com/jxsboston)
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/
#
# PyAudio's web page: https://people.csail.mit.edu/hubert/pyaudio/

import pyaudio, wave, numpy as np
from typing import Optional

audio = pyaudio.PyAudio()

# Default sampling date: 16,000.
# Default # of channels: 1
# Default sound format: paFloat32
SAMPLING_RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paFloat32
SAMPLE_WIDTH = audio.get_sample_size(FORMAT)

# Function to initizalize PyAudio with pre-fixed default settings
# and open a new audio stream
#   Returns a new audio stream. 
#
def init() -> pyaudio.Stream:
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=SAMPLING_RATE,
                        frames_per_buffer=1024,
                        output=True)
    return stream

# Function to generate a sine curve and make samples on the curve
#   frequency (float):
#   duration (float):
#   gain (float): Optional. Default gain is 1.0.
#
#   Returns a set of sound wave samples (sine curve samples) as a numpy.ndarray
#
def makeSinCurveSamples(*, frequency: float, duration: float, gain: float = 1.0) ->np.ndarray:
    sampleSize = int(duration * SAMPLING_RATE)
    factor = float(frequency) * np.pi * 2 / SAMPLING_RATE
    return np.sin(np.arange(sampleSize) * factor) * float(gain)

# Function to play a musical tone
#   stream (pyaudio.Stream): a stream to be used for playing a tone
#   frequency (float):
#   duration (float):
#   gain (float): Optional. Default gain is 1.0.
#
def playTone(stream: pyaudio.Stream, frequency: float, duration: float, gain: float = 1.0) -> np.ndarray:
    if type(frequency) is list:
        print("A float value should have been passed as a frequency to sound.playTone().")
        return None
    if frequency >= 20000: frequency = 20000
    if frequency < 20: frequency = 20
    samples = makeSinCurveSamples(frequency=frequency, duration=duration, gain=gain)
    stream.write(samples.astype(np.float32).tobytes())
    return samples

# Function to play multiple musical tones at the same time
#   stream (pyaudio.Stream): a stream to be used for playing a tone
#   frequencyList (list): List of frequency (float) values
#   duration (float):
#   gain (float): Optional. Default gain is 1.0.
#
def playTones(stream, frequencyList, duration, gain = 1.0):
    if type(frequencyList) is not list:
        print("A list of frequency values should have been passed to sound.playTones().")
        return None
    sampleSize = int(duration * SAMPLING_RATE)
    samples = [0] * sampleSize
    freqCount = len(frequencyList)
    for freq in frequencyList:
        if freq >= 20000: freq = 20000
        if freq < 20: freq = 20
        samples += makeSinCurveSamples(frequency=freq, duration=duration, gain=(gain/freqCount))
    stream.write(samples.astype(np.float32).tobytes())
    return samples

# Function to beep
#   stream (pyaudio.Stream): A stream to be used for playing a tone
#   duration (float): Duration of a beep
#   frequency (float): Optional. Default frequency is 523.251 Hz (C5 tone).
#
def beep(stream: pyaudio.Stream, duration: float, frequency: float = 523.251) ->np.ndarray:
    return playTone(stream, frequency, duration)

# Function to concatnate 2 sound wave samples
#   samples1 (numpy.ndarray): A list of sound wave samples
#   samples2 (numpy.ndarray): A list of sound wave samples
#
#   Returns a concatnated list as a numpy.ndarray.
#
def concatnateSamples(samples1, samples2):
    if type(samples1) is np.ndarray and type(samples2) is np.ndarray:
        return np.concatenate((samples1, samples2), axis=None)
    else:
        print("Provided sound wave samples are not in numpy.ndarray.")
        return None


# Function to save sound wave samples as a WAV file.
#   samples (numpy.ndarray): A list of sound wave samples
#   outputFileName (string): Name of the output WAV file
#
def saveSamplesAsWav(samples, outputFileName):
    if type(samples) is not np.ndarray:
        print("Provided sound wave samples are not in numpy.ndarray.")
    else:
        bData = b""
        bSamples = samples.astype(np.float32).tobytes()
        bData += bSamples
        w = wave.Wave_write(outputFileName)
        params = (CHANNELS, SAMPLE_WIDTH, SAMPLING_RATE, len(bData), "NONE", "not compressed")
        w.setparams(params)
        w.writeframes(bData)
        w.close()
