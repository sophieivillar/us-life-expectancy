import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Step 1: Load the datasets
data_2018 = pd.read_csv(Path("data/life_expectancy_2018.csv"))
data_2020 = pd.read_csv(Path("data/life_expectancy_2020.csv"))

# Step 2: Keep overall life expectancy for each state
total_2018 = data_2018[data_2018["Sex"] == "Total"][["State", "LEB"]]
total_2020 = data_2020[data_2020["Sex"] == "Total"][["State", "LE"]]

# Remove the national total so we compare states and D.C.
total_2018 = total_2018[total_2018["State"] != "United States"]
total_2020 = total_2020[total_2020["State"] != "United States"]

# Step 3: Rename columns and combine datasets
total_2018 = total_2018.rename(columns={"LEB": "2018"})
total_2020 = total_2020.rename(columns={"LE": "2020"})
comparison = pd.merge(total_2018, total_2020, on="State", validate="one_to_one")

# Step 4: Calculate changes and rankings
comparison["Change"] = comparison["2020"] - comparison["2018"]
comparison["Rank 2018"] = comparison["2018"].rank(ascending=False, method="min").astype(int)
comparison["Rank 2020"] = comparison["2020"].rank(ascending=False, method="min").astype(int)
comparison["Rank Change"] = comparison["Rank 2018"] - comparison["Rank 2020"]

# Step 5: Print statistics
for year in ["2018", "2020"]:
    print("\n" + year + " Results:")
    print("Average:", round(comparison[year].mean(), 2), "years")
    print("Standard deviation:", round(comparison[year].std(), 2), "years")
    print("Minimum:", comparison.loc[comparison[year].idxmin(), "State"],
          comparison[year].min(), "years")
    print("Maximum:", comparison.loc[comparison[year].idxmax(), "State"],
          comparison[year].max(), "years")

print("\nAverage change:", round(comparison["Change"].mean(), 2), "years")
print("\nFive largest drops:")
print(comparison.nsmallest(5, "Change")[["State", "Change"]].to_string(index=False))
print("\nFive smallest drops or largest gains:")
print(comparison.nlargest(5, "Change")[["State", "Change"]].to_string(index=False))
print("\nLargest improvements in ranking:")
print(comparison.nlargest(5, "Rank Change")[["State", "Rank 2018", "Rank 2020", "Rank Change"]].to_string(index=False))
print("\nLargest declines in ranking:")
print(comparison.nsmallest(5, "Rank Change")[["State", "Rank 2018", "Rank 2020", "Rank Change"]].to_string(index=False))

# Step 6: Create graphs
Path("plots").mkdir(exist_ok=True)

# Graph 1: Changes in life expectancy by state
sorted_data = comparison.sort_values("Change")
plt.figure(figsize=(12, 12))
plt.barh(sorted_data["State"], sorted_data["Change"], color="steelblue")
plt.title("Change in State Life Expectancy: 2018 to 2020")
plt.xlabel("Change in Life Expectancy (Years)")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("plots/question2_state_changes.png", dpi=200)
plt.show()

# Graph 2: Compare distributions across years
plt.figure(figsize=(7, 5))
plt.boxplot([comparison["2018"], comparison["2020"]], tick_labels=["2018", "2020"])
plt.title("State Life Expectancy Distributions")
plt.ylabel("Life Expectancy (Years)")
plt.tight_layout()
plt.savefig("plots/question2_boxplot.png", dpi=200)
plt.show()

# Graph 3: Compare state rankings
ranked = comparison.sort_values("Rank 2018")
plt.figure(figsize=(9, 7))
plt.scatter(ranked["Rank 2018"], ranked["Rank 2020"], color="teal")
plt.plot([1, 51], [1, 51], "--", color="gray")
plt.title("State Life Expectancy Rankings: 2018 vs. 2020")
plt.xlabel("2018 Rank (1 = Highest)")
plt.ylabel("2020 Rank (1 = Highest)")
plt.tight_layout()
plt.savefig("plots/question2_rankings.png", dpi=200)
plt.show()
  
