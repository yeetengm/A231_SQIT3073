
# Total Amount of Fund, Equity, and Loan from 2012 to 2022
# Line Chart

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import YearLocator, DateFormatter

# Read data from Microsoft Excel file. The path of particular file need to change according to the places you save.
df = pd.read_excel("/Users/yeetengm/Library/CloudStorage/OneDrive-UNIVERSITYUTARAMALAYSIA/yeetengm's mac/SEM 7/Business Analytics/Group Assignment/Final Version/Modified 1.31.xlsx",sheet_name="Sheet2")

# Extract used data from Excel file for plotting.  
# 1. Year
year = list(df["Year"])
print(year)

# Convert timestamp objects to strings and extract the year
year_str = [str(date.year) for date in year]

# 2. Fund 
fund = list(df["Fund"])
fund = [round(value, 2) for value in fund] # Round off values to 2 decimal places
print(fund)

# 3. Equity
equity = list(df["Equity"])
equity = [round(value, 2) for value in equity] # Round off values to 2 decimal places
print(equity)

# 4. Loan
loan = list(df["Loan"])
loan = [round(value, 2) for value in loan] # Round off values to 2 decimal places
print(loan)

# Plotting for line chart
plt.figure(figsize=(10,6))

# Line plot for Fund
plt.plot(year, fund, color="blueviolet", marker="x", markersize=2, linestyle="-", linewidth="2.5",label="Fund")      

# Line plot for Equity
plt.plot(year, equity, color="mediumvioletred", marker="x", markersize=2, linestyle="-", linewidth="2.5",label="Equity") 

# Line plot for Loan
plt.plot(year, loan, color="mediumorchid", marker="x", markersize=2, linestyle="-", linewidth="2.5",label="Loan")   

# Label x-axis
plt.xlabel("Year", fontsize=12, color="rebeccapurple", fontweight="bold")
plt.gca().tick_params(axis="x", color="rebeccapurple", labelcolor="rebeccapurple")

# Label y-axis
plt.ylabel("RM billion", fontsize=12, color="rebeccapurple", fontweight="bold")
plt.ylim((0, 2500))
plt.gca().tick_params(axis="y", color="rebeccapurple", labelcolor="rebeccapurple")

# Label title
plt.title("Total Amount of Fund, Equity, and Loan from 2012 to 2022", fontsize=18, color="rebeccapurple", fontweight="bold")

# Set x-axis ticks at 12-month intervals
plt.xticks(year[::12])

# Format x-axis to display only years
plt.gca().xaxis.set_major_locator(YearLocator())
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y'))

# Label legend
plt.legend(fontsize=10, loc="upper left")

# Add grid lines
plt.grid(True, linestyle='-', alpha=0.7, color='lightsteelblue')

# Add background color
plt.gca().set_facecolor("lavenderblush")

# For saving chart as png.
plt.savefig("Total Amount of Fund, Equity, and Loan from 2012 to 2022.png")

# Show the graph.
plt.show()

