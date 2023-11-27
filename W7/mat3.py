
# Histogram

import matplotlib.pyplot as plt
# Data to plot
values = [1, 2, 2, 3, 3, 3, 4, 4,
4, 4, 5, 5, 5, 5, 5]
# Create the histogram plot 
plt.hist(values, bins=5)
# by default bin is 10
# Show the plot
plt.show()