
# Overlap graph

import matplotlib.pyplot as plt
import numpy as np
# Data to plot
x = np.random.normal(0, 1, 1000)

# Calculate the histogram bins and midpoints
hist, bins = np.histogram(x, bins=50)
midpoints = (bins[:-1] + bins[1:]) / 2

# Create the figure
fig, ax1 = plt.subplots()

# Create the histogram plot 
ax1.hist(x, bins=50, alpha=0.5)

# Overlap the line plot 
ax1.plot(midpoints, hist, 'r--')

# Show the plot
plt.show()