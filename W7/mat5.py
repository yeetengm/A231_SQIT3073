
# Histogram Chart with with error bar represent S.D

import matplotlib.pyplot as plt
import numpy as np

# Data to plot
values = np.random.normal(0, 1, 1000)

# Calculate the mean and standard deviation
mean = np.mean(values)
std = np.std(values)

# Create the histogram plot
plt.hist(values, bins=50)

# Add error bars representing the standard deviation
plt.errorbar(mean, 0, xerr=std, fmt='o')

# Show the plot
plt.show()