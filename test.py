import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file.
netflix_df = pd.read_csv("netflix_data.csv")

# Subset all the rows with the column duration.
# Add all the subset rows, then divide with the total no. of rows.
# Convert into integer.
duration = int(sum(netflix_df.loc[:, "duration"]) / len(netflix_df))
print(duration)

# plt.hist(netflix_df["duration"])
# plt.savefig("plot.png")

# Subset all the rows with the column duration.
# Compare the subset rows with duration.
# Store the length of the result
short_movie_count = len(netflix_df[netflix_df["duration"] < duration])
print(short_movie_count)