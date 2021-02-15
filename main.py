import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io import wavfile 

sampling_freq, signal = wavfile.read('test.wav') 
signal = signal / (2 ** 15)

len_signal = len(signal) 
len_half = (len_signal + 1) // 2

freq_signal = np.fft.fft(signal) 

freq_signal = np.abs(freq_signal[0:len_half]) / len_half
signal_power = 20 * np.log10(freq_signal)
x_axis = np.linspace(0, sampling_freq / 2 / 1000.0, len(signal_power))

plt.figure() 
plt.plot(x_axis, signal_power, color='black') 
plt.xlabel('Frequency (kHz)') 
plt.ylabel('Signal power (dB)') 
plt.show()

plt.figure() 
plt.xscale('log')
plt.plot(x_axis, signal_power, color='black') 
plt.xlabel('Frequency (kHz)') 
plt.ylabel('Signal power (dB)') 
plt.show()