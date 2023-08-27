import matplotlib.pyplot as plt

# Read data from the .txt file
file_path = "C:\Users\Wits_User\Desktop\Robel\python\frequency_graph.txt"
freq = []
amplitude = []

with open(file_path, 'r') as file:
    next(file)  # Skip the header
    for line in file:
        tokens = line.strip().split()
        freq.append(float(tokens[0]))
        amplitude.append(float(tokens[1]))

# Create the plot
plt.plot(freq, amplitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency vs Amplitude')
plt.grid(True)
plt.show()
