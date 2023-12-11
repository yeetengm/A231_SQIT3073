
# Ratio of Loan, Fund and Equity from 2012 to 2022
# Horizontal Stack Bar Chart

# Import numpy, matplotlib, pandas library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read data from Microsoft Excel file. The path of particular file need to change according to the places you save.
df = pd.read_excel("/Users/yeetengm/Library/CloudStorage/OneDrive-UNIVERSITYUTARAMALAYSIA/yeetengm's mac/SEM 7/Business Analytics/Group Assignment/Final Version/Modified 1.31.xlsx",sheet_name="Sheet1")

# Extract used data from Excel file for ploting.
# 1. Year
year = list(df.Year)
print(year)

# 2. Fund
fund = list(df.Fund_Total)
fund = [round(value, 2) for value in fund]
print(fund)

# 3. Equity
equity = list(df.Equity_total)
equity = [round(value, 2) for value in equity]
print(equity)

# 4. Loan
loan = list(df.Loan_Total)
loan = [round(value, 2) for value in loan]
print(loan)

# `fe` is for adding the previos column value for plotting STACK bar chart.
fe = list(np.add(fund, equity))
fe = [round(value, 2) for value in fe]
print(fe)

# Plotting for chart.
p1 = plt.barh(year, fund, height=0.7, label="Fund", color="palevioletred")              # Plot Horizontal stack bar chart for Fund.
p2 = plt.barh(year, equity, height=0.7, left=fund, label="Equity", color="salmon")   # Plot Horizontal stack bar chart for Equity.
p3 = plt.barh(year, loan, height=0.7, left=fe, label="Loan", color="lightsalmon")             # Plot Horizontal stack bar chart for Loan.

# Label x-axis
plt.xlabel("Percentage (%)", color = "maroon",family = "monospace")
plt.xlim(0, 100)
plt.gca().tick_params(axis='x', colors='maroon')

# Label y-axis
plt.ylabel("Year", color = "maroon",family = "monospace")
plt.yticks(year, color = "maroon",family = "monospace")

# Label title
plt.title("Ratio of Loan, Fund and Equity from 2012 to 2022", loc ="left", family = "monospace",weight = 600, color = "maroon")

# Label each of the bar
plt.bar_label(p1, label_type='center', fontsize=7.5,color = 'snow')
plt.bar_label(p2, label_type='center', fontsize=7.5,color = 'snow')
plt.bar_label(p3, label_type='center', fontsize=7.5,color = 'snow')

# Label legend
plt.legend(loc=(0.65,1.075), ncol=3,fontsize=7.5)

# Set background color with color 
plt.gca().set_facecolor('linen')

# For saving chart as png.
plt.savefig('Ratio of Loan, Fund and Equity from 2012 to 2022.png', bbox_inches='tight')

# Show the graph.
plt.show()
