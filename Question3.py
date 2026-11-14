import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

#Step 1: Load Data
data_2018 = pd.read_csv("data/life_expectancy_2018.csv")
data_2020 = pd.read_csv("data/life_expectancy_2020.csv")

#Step 2: Analyze the data from each year 
def analyze_year(data, year):
  #Remove the US data from the dataset
  data = data[data["State"] != "United States"].copy()
  #Organize by state and sex
  pivot = data.pivot(index="State", columns="Sex", values="LEB")
  #Calculate life expectancy gap 
  pivot["Gap"] = pivot["Female"] - pivot["Male"]
  pivot = pivot.dropna(subset=["Total", "Gap"])
  #Graph variables 
  x = pivot["Total"]
  y = pivot["Gap"]

#Step 3: Calculate 
regression = linregress(x,y)
print("\n=====")
print("Results for", year)
print("=====")
print("Number of states:", len(pivot))
print("Average overall life expectancy:", round(x.mean(), 3), "years")
print("Average overall life expectancy:", round(y.mean(), 3), "years")
print("correlation coefficient (r):", round(regression.rvalue, 4))
print("R-squared:", round(regression.rvalue**2, 4))
print("Regression slope:", round(regression.slope, 4))
print("regression intercept:", round(regression.intercept, 4))

#Step 4: Create scatter plot
plt.figure(figsize=(10,6))
plt.scatter(x,y,label="Individual States")
#Create regression line
x_line = np.linspace(x.min(), x.max(), 100)
y_line = (regression.slope*x_line + regression.intercept)
plt.plot(x_line, y_line, label="Linear Regression")
#Add labels 
plt.title(f"Gender Life Expectancy Gap vs Overall Life Expectancy ({year})")
plt.xlabel("Overal Life Expectancy (years)")
plt.ylabel("Female - Male LIfe Expectancy Gap (years)")
plt.legend
plt.grid(True)
plt.tight_layout()
plt.savefig(f"plots/question3_{year}.png", dpi=300)
plt.show()
return regression

#Step 5: Compare 2018 and 2020
results_2018 = analyze_year(data_2018, 2018)
results_2020 = analyze_year(data_2020, 2020)
print("\n=====")
print("Comparison: 2018 vs 2020")
print("=====")
print("Change in correlation:", round(results_2020.rvalue - results_2018.rvalue, 4))
print("Change in regression slope:", round(results_2020.slope - results_2018.slope, 4))
print("Change in R-squared:", round(results_2020.rvalue**2 - results_2018.rvalue**2, 4))
