import numpy as np
import matplotlib.pyplot as plt
import heartpy as hp

# Reads the file into a numpy array
data = hp.get_data('capture01_250Hz.txt')
# Create a time vector
Fs = 250  # Sampling rate (samples per second)
time = np.arange(len(data)) / Fs

# Plot the whole data in a graphical figure
plt.figure(figsize=(12, 4))
plt.plot(time, data)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (uint16)')
plt.show()


# Random seed based on the last four digits of the student ID number
np.random.seed(5548)
t0 = np.random.randint(30, 100)
print(f'Segment starts from: {t0} s')

# Select a segment
i = (t0 < time) & (time < t0 + 60)
data2 = data[i]
time2 = time[i]

# Plot the selected segment
plt.figure(figsize = (12, 4))
plt.plot(time2, data2)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (uint16)')
plt.show()

# run the analysis
wd, m = hp.process(data2, sample_rate = Fs, report_time = True)

plt.figure(figsize = (12, 4))

# call plotter
hp.plotter(wd, m)
#  measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))

