# Generate and save a sample visualization for Happiness dataset
import matplotlib.pyplot as plt
import pandas as pd

# Example Happiness dataset (replace this with actual data during execution)
data = {"Year": [2015, 2016, 2017, 2018, 2019], "Happiness Score": [7.2, 7.3, 7.4, 7.5, 7.6]}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.plot(df["Year"], df["Happiness Score"], marker="o", linestyle="-", color="green")
plt.title("Happiness Scores Over Years")
plt.xlabel("Year")
plt.ylabel("Happiness Score")
plt.savefig("happiness_visualization.png")
plt.close()
