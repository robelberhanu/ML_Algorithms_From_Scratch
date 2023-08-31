import matplotlib.pyplot as plt

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
        values = line.split()
        if len(values) == 2:
            freq, amp = values
            
            # Convert strings to float
            freq = float(freq)
            amp = float(amp)
            
            # Only append values if amplitude is less than or equal to 0.8
            if amp <= 0.9:
                freqs.append(freq)
                amplitudes.append(amp)

# Plotting
plt.figure(figsize=(12, 8))  # Specify the DPI here
plt.plot(freqs, amplitudes, '-', markersize=4, color='navy')  # using navy blue for the line and markers

# Setting label sizes and boldness, and adding units to amplitude
plt.xlabel("Frequency (Hz)", fontsize=25, fontweight='bold')
plt.ylabel("Amplitude (m)", fontsize=25, fontweight='bold')  # Amplitude units added here
plt.title("Frequency vs Amplitude", fontsize=26, fontweight='bold')

# Adjusting tick size for readability and setting font size to 14
plt.xticks(fontsize=24, fontweight='bold')
plt.yticks(fontsize=24, fontweight='bold')

plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
plt.tight_layout()

# Save the figure in SVG format
plt.savefig("filtered_freq_plot.svg", format='svg')

plt.show()
