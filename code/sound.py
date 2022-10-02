# Library to beep and play musical tones with PyAudio
# Sept 28, 2022 v0.08
# Jun Suzuki (https://github.com/jxsboston)
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/
#
# PyAudio's web page: https://people.csail.mit.edu/hubert/pyaudio/

import pyaudio, numpy as np
from typing import Optional

# Function to initizalize PyAudio with pre-fixed default settings
# and open a new audio stream
#   samplingRate (int): Optional. Sampling rate to be used.
#
#   Returns a new audio stream. 
#
# Default sampling rate: 16,000 Hz (configurable)
# Default sound format: paFloat32
# Default # of channels: 1
#
def init(*, samplingRate: int = 16000) -> pyaudio.Stream:
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=samplingRate,
                        frames_per_buffer=1024,
                        output=True)
    return stream

# Function to generate a sine curve and make samples on the curve
#   frequency (float):
#   duration (float):
#   samplingRate (int): Optional. Default sapmling rate is 16,000.
#   gain (float): Optional. Default gain is 1.0.
#
#   Returns a set of sound samples (sine curve samples) as a numpy.ndarray
#
def makeSinCurveSamples(*, frequency: float, duration: float,
                        samplingRate: int = 16000, gain: float = 1.0) ->np.ndarray:
    sampleSize = int(duration * samplingRate)
    factor = float(frequency) * np.pi * 2 / samplingRate
    return np.sin(np.arange(sampleSize) * factor) * gain

# Function to play a musical tone
#   stream (pyaudio.Stream): a stream to be used for playing a tone
#   frequency (float):
#   duration (float):
#   gain (float): Optional. Default gain is 1.0.
#
def playTone(stream: pyaudio.Stream, frequency: float, duration: float, gain: float = 1.0) -> np.ndarray:
    if frequency >= 20000: frequency = 20000
    if frequency < 20: frequency = 20
    samples = makeSinCurveSamples(frequency=frequency, duration=duration, gain=float(gain))
    stream.write(samples.astype(np.float32).tobytes())
    return samples

def playChordTone(stream, frequencyList, duration, gain = 1.0):
    sampleSize = int(duration * 16000)
    samples = [0] * sampleSize
    freqCount = len(frequencyList)
    for freq in frequencyList:
        if freq >= 20000: freq = 20000
        if freq < 20: freq = 20
        samples += makeSinCurveSamples(frequency=freq, duration=duration, gain=float(gain/freqCount))
#     for sample in samples:
#         adjustedSamples.append(sample/freqCount)
    stream.write(samples.astype(np.float32).tobytes())
    return samples

# Function to beep
#   stream (pyaudio.Stream): A stream to be used for playing a tone
#   duration (float): Duration of a beep
#   frequency (float): Optional. Default frequency is 523.251 Hz (C5 tone).
#
def beep(stream: pyaudio.Stream, duration: float, frequency: float = 523.251) ->np.ndarray:
    return playTone(stream, frequency, duration)


