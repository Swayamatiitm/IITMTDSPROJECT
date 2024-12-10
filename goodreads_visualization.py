# Generate and save a sample visualization for Goodreads dataset
import matplotlib.pyplot as plt
import pandas as pd

# Example Goodreads dataset (replace this with actual data during execution)
data = {"Rating": [4.1, 3.9, 4.2, 4.5, 3.8], "Books": ["Book A", "Book B", "Book C", "Book D", "Book E"]}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.bar(df["Books"], df["Rating"], color="skyblue")
plt.title("Distribution of Book Ratings")
plt.xlabel("Books")
plt.ylabel("Rating")
plt.savefig("goodreads_visualization.png")
plt.close()
