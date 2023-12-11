# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read data from Microsoft Excel file. The path of particular file need to change according to the places you save.
df = pd.read_excel("/Users/yeetengm/Library/CloudStorage/OneDrive-UNIVERSITYUTARAMALAYSIA/yeetengm's mac/SEM 7/Business Analytics/Group Assignment/Final Version/Modified 1.31.xlsx", sheet_name="Sheet1")

# Extract used data from Excel file for plotting.
# 1. Year
year = df["Year"]
print(year)

# 2. Total Fund
fund = list(df["Fund"])
fund = [round(value, 2) for value in fund]  # Round off values to 2 decimal places
print(fund)

# Plotting the bar chart
plt.figure(figsize=(10, 6))

# Bar chart for Total Fund
bars = plt.bar(df["Year"], df["Fund"], width=0.5, color="#8DA66C")

# Label x-axis
plt.xlabel("Year", fontsize=12, color="#388497", fontweight="bold")
plt.tick_params(axis='x', labelcolor="#388497") 

# Label y-axis 
plt.ylabel("RM billion", fontsize=12, color="#388497", fontweight="bold")
plt.ylim((0, 12000))
plt.gca().tick_params(axis='y',labelcolor="#388497")

# Label title
plt.title("Total Fund From 2012 to 2022", fontsize=18, color="#388497", fontweight="bold", weight = 600)

# Set font color for bar labels
for bar, value in zip(bars, fund):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f"{round(value, 2)}", 
             ha='center', va='bottom', color="#566357")

# Set background color
plt.gca().set_facecolor("#F2F2C5")

# et x-axis ticks to show all years
plt.xticks(df["Year"])

# Save chart as png.
plt.savefig("Total Fund from 2012 to 2022.png")

# Show the plot
plt.tight_layout()
plt.show()
