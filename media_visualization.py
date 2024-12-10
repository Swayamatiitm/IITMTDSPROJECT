# Generate and save a sample visualization for Media dataset
import matplotlib.pyplot as plt

# Example Media dataset (replace this with actual data during execution)
data = {"Media Type": ["Social Media", "TV", "News", "Gaming"], "Usage": [40, 30, 20, 10]}

plt.figure(figsize=(8, 5))
plt.pie(data["Usage"], labels=data["Media Type"], autopct="%1.1f%%", startangle=140, colors=["blue", "orange", "green", "red"])
plt.title("Proportion of Media Usage Types")
plt.savefig("media_visualization.png")
plt.close()
