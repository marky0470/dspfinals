import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

def lowpass_filter(input_wav_path, output_lowpass_path, cutoff_freq):
    # Read the input WAV file
    fs, sound_wave = wavfile.read(input_wav_path)
    
    # Check if the audio is stereo and convert to mono if needed
    if sound_wave.ndim > 1:
        sound_wave = sound_wave.mean(axis=1)
    
    # Design a lowpass filter
    b_low, a_low = signal.butter(4, cutoff_freq / (0.5 * fs), btype='low')
    
    # Apply the lowpass filter to the sound wave
    sound_wave_lowpass = signal.filtfilt(b_low, a_low, sound_wave)
    
    # Normalize the filtered signal to prevent distortion
    sound_wave_lowpass = np.int16(sound_wave_lowpass / np.max(np.abs(sound_wave_lowpass)) * 32767)
    
    # Save the lowpass filtered sound wave to a new WAV file
    wavfile.write(output_lowpass_path, fs, sound_wave_lowpass)
    
    # Frequency response of the lowpass filter
    w, h = signal.freqz(b_low, a_low)
    
    # Plot the original and lowpass filtered signals
    time = np.linspace(0, len(sound_wave) / fs, num=len(sound_wave))
    
    plt.figure(figsize=(10, 6))
    
    plt.subplot(3, 1, 1)
    plt.plot(time, sound_wave)
    plt.title('Original Sound Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    plt.subplot(3, 1, 2)
    plt.plot(time, sound_wave_lowpass)
    plt.title('Lowpass Filtered Sound Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    plt.subplot(3, 1, 3)
    plt.plot(w * fs / (2 * np.pi), 20 * np.log10(np.abs(h)))
    plt.title('Lowpass Filter Frequency Response')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain (dB)')
    plt.grid()
    
    plt.tight_layout()
    plt.savefig('lowpass.png')
