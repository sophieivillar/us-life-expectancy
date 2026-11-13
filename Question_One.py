### Step 1: Import Libraries:
# organize and analyze data using pandas, which will read and manipulate the data
import pandas as pd
# create visualizations using matplotlib, which will create plots and charts
import matplotlib.pyplot as plt
# work with file locations using pathlib, which will locate the data files 
from pathlib import Path

### Step 2: Load, Read, and Store the Data:
# tell pandas to read the 2018 data and store it in a variable
data_2018 = pd.read_csv(Path("./data/life_expectancy_2018.csv"))
# tell pandas to read the 2020 data and store it in a variable
data_2020 = pd.read_csv(Path("./data/life_expectancy_2020.csv"))

### Step 3: Manipulate the Data to Address Question 1: 
data_2018 = data_2018[["State", "Sex", "LEB"]]
data_2020 = data_2020[["State", "Sex", "LE"]]
# remove the overall United States data so we can analyze the individual states
data_2018 = data_2018[data_2018["State"] != "United States"]
data_2020 = data_2020[data_2020["State"] != "United States"]
# separate the male and female data for each year into their own variables
male_2018 = data_2018[data_2018["Sex"] == "Male"][["State", "LEB"]]
female_2018 = data_2018[data_2018["Sex"] == "Female"][["State", "LEB"]]
male_2020 = data_2020[data_2020["Sex"] == "Male"][["State", "LE"]]
female_2020 = data_2020[data_2020["Sex"] == "Female"][["State", "LE"]]
# rename the column headers so both years use the same term for life expectancy
male_2018 = male_2018.rename(columns={"LEB": "Male"})
female_2018 = female_2018.rename(columns={"LEB": "Female"})
male_2020 = male_2020.rename(columns={"LE": "Male"})
female_2020 = female_2020.rename(columns={"LE": "Female"})
# combine the male and female data based on the state
gap_2018 = pd.merge(male_2018, female_2018, on="State")
gap_2020 = pd.merge(male_2020, female_2020, on="State")
# calculate the gender gap in life expectancy
gap_2018["Gender Gap"] = gap_2018["Female"] - gap_2018["Male"]
gap_2020["Gender Gap"] = gap_2020["Female"] - gap_2020["Male"]

### Step 4: Calculate the Statistics Related to Question 1:
# calculate average male and female life expectancy
avg_male_LE_2018 = gap_2018["Male"].mean()
avg_female_LE_2018 = gap_2018["Female"].mean()
avg_male_LE_2020 = gap_2020["Male"].mean()
avg_female_LE_2020 = gap_2020["Female"].mean()
# calculate average gender gap
avg_gap_2018 = gap_2018["Gender Gap"].mean()
avg_gap_2020 = gap_2020["Gender Gap"].mean()
# calculate standard deviation
std_2018 = gap_2018["Gender Gap"].std()
std_2020 = gap_2020["Gender Gap"].std()
# identify the row number with the minimum and maximum gender gaps
min_gap_2018 = gap_2018.loc[gap_2018["Gender Gap"].idxmin()]
max_gap_2018 = gap_2018.loc[gap_2018["Gender Gap"].idxmax()]
min_gap_2020 = gap_2020.loc[gap_2020["Gender Gap"].idxmin()]
max_gap_2020 = gap_2020.loc[gap_2020["Gender Gap"].idxmax()]
# compare the average gender gaps
change = avg_gap_2020 - avg_gap_2018

### Step 5: Print the Results to answer Quesiton 1:
print("2018 Results:")
print("Average Male Life Expectancy:", round(avg_male_LE_2018, 2))
print("Average Female Life Expectancy:", round(avg_female_LE_2018, 2))
print("Average Gender Gap:", round(avg_gap_2018, 2))
print("Standard Deviation:", round(std_2018, 2))
print("Minimum Gender Gap:", round(min_gap_2018["Gender Gap"], 2), "years in", min_gap_2018["State"])
print("Maximum Gender Gap:", round(max_gap_2018["Gender Gap"], 2), "years in", max_gap_2018["State"])

print("\n2020 Results:")
print("Average Male Life Expectancy:", round(avg_male_LE_2020, 2))
print("Average Female Life Expectancy:", round(avg_female_LE_2020, 2))
print("Average Gender Gap:", round(avg_gap_2020, 2))
print("Standard Deviation:", round(std_2020, 2))
print("Minimum Gender Gap:", round(min_gap_2020["Gender Gap"], 2), "years in", min_gap_2020["State"])
print("Maximum Gender Gap:", round(max_gap_2020["Gender Gap"], 2), "years in", max_gap_2020["State"])

print("\nComparison Between 2018 and 2020:")
print("Change in Average Gender Gap:", round(change, 2), "years")
if change > 0:
    print("The average gender gap increased from 2018 to 2020.")
elif change < 0:
    print("The average gender gap decreased from 2018 to 2020.")
else:
    print("The average gender gap remained the same.")

### Step 6: Generate Plots to Visualize the Results for Quesiton 1:
# create a folder to hold the plots in the repository
Path("plots").mkdir(exist_ok=True)
# create plot 1 to compare the average gender gap between 2018 and 2020
years = ["2018", "2020"]
avg_gaps = [avg_gap_2018, avg_gap_2020]
plt.bar(years, avg_gaps, color="teal")
plt.title("Average Gender Life Expectancy Gap: 2018 vs. 2020")
plt.xlabel("Year")
plt.ylabel("Average Gender Gap (Years)")
plt.ylim(0, max(avg_gaps)+1)
plt.savefig("plots/average_gender_gap.png")
plt.show
# create plot 2 to compare gender gaps across individual states
# combine and sort the two years into a single dataframe
comparison = pd.merge(gap_2018[["State", "Gender Gap"]], gap_2020[["State", "Gender Gap"]], 
                       on = "State", suffixes = ("_2018", "_2020")).sort_values("State")
# use the pandas plotting to create a grouped bar chart
comparison.plot(x="State", y=["Gender Gap_2018", "Gender Gap_2020"], kind="bar", 
                color=["skyblue", "salmon"])
plt.title("Gender Life Expectancy Gap By State: 2018 vs. 2020")
plt.xlabel("State")
plt.ylabel("Gender Gap (Years)")
plt.legend(["2018", "2020"])
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("plots/state_gender_gaps.png")
plt.show()