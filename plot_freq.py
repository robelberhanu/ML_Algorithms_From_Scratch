import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"


# File name
filename = "stack_frequency_data/reprocessed_sill_frequency.txt"

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
            
            # Convert strings to float and append to lists
            freqs.append(float(freq))
            amplitudes.append(float(amp))

# Plotting
plt.figure(figsize=(12, 8))  # Specify the DPI here
plt.plot(freqs, amplitudes, '-', markersize=4, color='navy')  # using navy blue for the line and markers

# Setting label sizes and boldness
plt.xlabel("Frequency (Hz)", fontsize=25, fontweight='bold')
plt.ylabel("Amplitude (m)", fontsize=25, fontweight='bold')
plt.title("Frequency vs Amplitude (Legacy Stack)", fontsize=26, fontweight='bold')

# Increasing tick size for readability
plt.xticks(fontsize=23, fontweight='bold')
plt.yticks(fontsize=23, fontweight='bold')

plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
plt.tight_layout()

# Save the figure in SVG format
plt.savefig("reprocessed_sill_frequency_plot.svg", format='svg')

plt.show()
