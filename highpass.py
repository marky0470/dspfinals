import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

def highpass_filter(input_wav_path, output_highpass_path, cutoff_freq):
    # Read the input WAV file
    fs, sound_wave = wavfile.read(input_wav_path)
    
    # Check if the audio is stereo and convert to mono if needed
    if sound_wave.ndim > 1:
        sound_wave = sound_wave.mean(axis=1)
    
    # Design a highpass filter
    b_high, a_high = signal.butter(4, cutoff_freq / (0.5 * fs), btype='high')
    
    # Apply the highpass filter to the sound wave
    sound_wave_highpass = signal.filtfilt(b_high, a_high, sound_wave)
    
    # Save the highpass filtered sound wave to a new WAV file
    wavfile.write(output_highpass_path, fs, sound_wave_highpass.astype(np.int16))
    
    # Frequency response of the highpass filter
    w, h = signal.freqz(b_high, a_high, fs=fs)
    
    # Plot the original and highpass filtered signals
    time = np.linspace(0, len(sound_wave) / fs, num=len(sound_wave))
    
    plt.figure(figsize=(10, 6))
    
    plt.subplot(3, 1, 1)
    plt.plot(time, sound_wave)
    plt.title('Original Sound Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    plt.subplot(3, 1, 2)
    plt.plot(time, sound_wave_highpass)
    plt.title('Highpass Filtered Sound Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    plt.subplot(3, 1, 3)
    plt.plot(w, 20 * np.log10(abs(h)))
    plt.title('Highpass Filter Frequency Response')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain (dB)')
    plt.grid()
    
    plt.tight_layout()
    plt.savefig('highpass.png')
