import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

# Set the global font to be Times New Roman
plt.rcParams["font.family"] = "Times New Roman"

# File names
filename1 = "stack_frequency_data/legacy_end_frequency.txt"
filename2 = "stack_frequency_data/reprocessed_end_frequency.txt"

# Function to extract data from file
def extract_data(filename):
    freqs = []
    amplitudes = []

    with open(filename, 'r') as file:
        # Skip the header
        next(file)

        # Read each line
        for line in file:
            # Split values at whitespace
            values = line.split()
            if len(values) == 2:
                freq, amp = values

                # Convert strings to float
                freq = float(freq)
                amp = float(amp)

                # Only append values if amplitude is less than or equal to 0.8
                if amp <= 0.8:
                    freqs.append(freq)
                    amplitudes.append(amp)

    return freqs, amplitudes

# Extract data from the two files
freqs1, amplitudes1 = extract_data(filename1)
freqs2, amplitudes2 = extract_data(filename2)

# Use UnivariateSpline to smoothen data from the second source
spline = UnivariateSpline(freqs2, amplitudes2, s= 0.2)
freqs2_smooth = np.linspace(min(freqs2), max(freqs2), 700)
amplitudes2_smooth = spline(freqs2_smooth)

# Plotting
fig = plt.figure(figsize=(12, 7), dpi=300)

# Plot data from the first file
plt.plot(freqs1, amplitudes1, '-', markersize=4, color='navy', label='Legacy')

# Plot smooth data from the second file
plt.plot(freqs2_smooth, amplitudes2_smooth, '-', color='green', label='Reprocessed')

# Setting label sizes, boldness, and adding units to amplitude
plt.xlabel("Frequency (Hz)", fontsize=14, fontweight='bold', labelpad=15)  
plt.ylabel("Amplitude (m)", fontsize=14, fontweight='bold', labelpad=15)
plt.title("Frequency vs Amplitude", fontsize=16, fontweight='bold')

# Adjusting tick size for readability and setting font size to 14
plt.xticks(fontsize=14, fontweight='bold', rotation=45)  # Rotate x-axis labels
plt.yticks(fontsize=14, fontweight='bold')

plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')

# Add legend to differentiate between the two datasets
plt.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))


plt.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig("output_plot.svg", format='svg')
plt.show()
