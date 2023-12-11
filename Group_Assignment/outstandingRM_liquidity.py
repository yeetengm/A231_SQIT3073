
# Outstanding Ringgit Liquidity placed with Bank Negara Malaysia
# (Stack Bar with Line Chart)

# Import numpy, matplotlib, pandas library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read data from Microsoft Excel file. The path of particular file need to change according to the places you save.
df= pd.read_excel("/Users/yeetengm/Library/CloudStorage/OneDrive-UNIVERSITYUTARAMALAYSIA/yeetengm's mac/SEM 7/Business Analytics/Group Assignment/Final Version/Modified 1.31.xlsx",sheet_name="Sheet1")

# Extract used data from Excel file for ploting.
# 1. Year
year = list(df.Year)
print(year)

# 2. MMB = Money Market Borrowings (excluding repos)
mmb = list(df.MMB)
mmb = [round(value, 2) for value in mmb]        # Round off the value to 2 decimal places.
print(mmb)

# 3. Repo
repo = list(df.Repo)
repo = [round(value, 2) for value in repo]
print(repo)

# 4. securities = BNM Debt Securities
securities = list(df.BNM_Debt_Securities)
securities = [round(value, 2) for value in securities]
print(securities)

# 5. SRR
srr = list(df.SRR)
srr = [round(value, 2) for value in srr]
print(srr)

# 6. Others
others = list(df.Others)
others = [round(value, 2) for value in others]
print(others)

# 7. Total = Total Outstanding Ringgit Liquidity placed with Bank Negara Malaysia
total = list(df.Total)
total = [round(value, 2) for value in total]
print(total)

# `fe` is for adding the previous column value for plotting STACK bar chart.
fe = list(np.add(mmb, repo))
fe = [round(value, 2) for value in fe]
print(fe)

fe2 = list(np.add(fe,securities))
fe2 = [round(value, 2) for value in fe2]
print(fe2)

fe3 = list(np.add(fe2,srr))
fe3 = [round(value, 2) for value in fe3]
print(fe3)

fe4 = list(np.add(fe3,others))
fe4 = [round(value, 2) for value in fe3]
print(fe3)

# Plotting for chart
p1 = plt.bar(year, mmb, width=0.5, label="Money Market Borrowing", color="lightsteelblue")           # Bar plot for MMB
p2 = plt.bar(year, repo, bottom=mmb, width=0.5, label="Repo", color="powderblue")                    # Bar plot for Repo
p3 = plt.bar(year, securities, bottom=fe, width=0.5, label="Securities", color="cornflowerblue")     # Bar plot for Securities
p4 = plt.bar(year, srr, bottom=fe2, width=0.5, label="SRR", color="steelblue")                       # Bar plot for SRR            
p5 = plt.bar(year, others, bottom=fe3, width=0.5, label="Others", color="royalblue")                 # Bar plot for Others
p6 = plt.plot(year,total,label = "Total", color = "maroon",linestyle = "-",linewidth = '3.9' )       # Line plot for Total Outstanding Ringgit Liquidity placed with BNM

# Label y-axis
plt.ylabel("RM billion", color = "navy",family = "monospace")
plt.ylim((0, 5500))
plt.gca().tick_params(axis='y', colors='navy')

# Label x-axis
plt.xlabel("Year", color = "navy",family = "monospace")
plt.xticks(year,color = "navy",family = "sans" )

# Label title
plt.title("Outstanding Ringgit Liquidity placed with Bank Negara Malaysia", family = "normal",weight = 600, color = "navy")

# Label legend
plt.legend(loc='upper right', ncol=2,fontsize="7")

# Set background color as lavender color.
plt.gca().set_facecolor('lavender')  

# For saving chart as png.
plt.savefig('Outstanding Ringgit Liquidity placed with Bank Negara Malaysia.png', bbox_inches='tight')

# Show the graph       
plt.show()
