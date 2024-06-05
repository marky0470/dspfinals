import numpy as np
from scipy import signal
from scipy.signal import remez, filtfilt
import matplotlib.pyplot as plt
from scipy.io import wavfile
from PIL import Image

def filterAudio(path, passType, cutoff, taps):
    sample_rate, data = wavfile.read(path)
    duration = int(len(data)/sample_rate)

    samples = sample_rate * duration

    if passType == "low":
        bands = [0, cutoff, cutoff + 1000, samples/2]
        fir_coeff = remez(taps, bands, [1,0], Hz=samples)
    elif passType == "high":
        bands = [0, cutoff - 1000, cutoff, samples / 2]
        fir_coeff = remez(taps, bands, [0,1], Hz=samples)

    filtered_signal = filtfilt(fir_coeff, 1.0, data, axis=0)

    plt.figure(figsize=(4, 3))
    plt.plot(filtered_signal)
    plt.title("Filtered Audio Signal")
    plt.savefig("filtered_audio.png")
    plt.clf()

    with Image.open("filtered_audio.png") as plot_image:
        plot_image = Image.open("filtered_audio.png")

    return plot_image

def plotAudio(path):
    sample_rate, data = wavfile.read(path)

    plt.figure(figsize=(4, 3))
    plt.plot(data)
    plt.title("Original Audio Signal")
    plt.savefig("original_audio.png")
    plt.clf()

    with Image.open("original_audio.png") as plot_image:
        plot_image = Image.open("original_audio.png")
    
    return plot_image


# wavfile.write("out44k.wav", sample_rate, filtered_signal.astype(np.int16))

