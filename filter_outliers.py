import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import iirnotch, lfilter

# File name
filename = "frequency_graph.txt"

# Lists to store values
freqs = []
amplitudes = []

# Read data from file
with open(filename, 'r') as file:
    # Skip the header
    next(file)
    
    # Read each line
    for line in file:
        # Split values at whitespace
        freq, amp = line.split()
        
        # Convert strings to float and append to lists
        freqs.append(float(freq))
        amplitudes.append(float(amp))

# Define the sample rate and the frequency to be notched out
fs = 2.0  # Sample rate. This should be adjusted based on your data.
f0 = 0.5  # Frequency to be removed. Adjust based on your specific requirements.
Q = 100.0  # Quality factor. Higher values mean narrower notch.

# Design the notch filter
b, a = iirnotch(f0, Q, fs)

# Apply the filter
filtered_amplitudes = lfilter(b, a, amplitudes)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(freqs, filtered_amplitudes, '-o', markersize=4)

# Setting label sizes and boldness
plt.xlabel("Frequency (Hz)", fontsize=14, fontweight='bold')
plt.ylabel("Amplitude", fontsize=14, fontweight='bold')
plt.title("Frequency vs Amplitude (Filtered)", fontsize=16, fontweight='bold')

# Increasing tick size for readability
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

plt.grid(True)
plt.tight_layout()
plt.show()
