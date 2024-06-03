import numpy as np
from scipy import signal
from scipy.signal import remez, filtfilt
import matplotlib.pyplot as plt
from scipy.io import wavfile
from PIL import Image

def filterAudio(path):
    sample_rate, data = wavfile.read(path)
    duration = int(len(data)/sample_rate)

    cutoff = 4000

    samples = sample_rate * duration
    bands = [0, cutoff, cutoff + 1000, samples/2]
    fir_coeff = remez(101, bands, [1,0], Hz=samples)
    filtered_signal = filtfilt(fir_coeff, 1.0, data, axis=0)

    plt.plot(filtered_signal)
    plt.title("Filtered Audio Signal")
    plt.savefig("filtered_audio.png")
    plt.clf()

    plot_image = Image.open("filtered_audio.png")

    return plot_image

def plotAudio(path):
    sample_rate, data = wavfile.read(path)

    plt.plot(data)
    plt.title("Original Audio Signal")
    plt.savefig("original_audio.png")
    plt.clf()

    plot_image = Image.open("original_audio.png")
    
    return plot_image

# wavfile.write("out44k.wav", sample_rate, filtered_signal.astype(np.int16))

