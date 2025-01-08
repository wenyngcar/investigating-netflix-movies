import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the csv file.
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the rows with the column duration.
# Add all the subset rows, then divide with the total no. of rows.
# Convert into integer.
duration = int(sum(netflix_df.loc[:, "duration"]) / len(netflix_df))
print(duration)

# plt.hist(netflix_df["duration"])
# plt.savefig("plot.png")

# Subset the rows with column type and genre.
action_movie = np.logical_and(netflix_df["type"] == "Movie", netflix_df["genre"] == "Action")

# Subset the rows with the column duration less than 90 and is a action movie .
short_action_movie = np.logical_and(action_movie, netflix_df["duration"] < 90)

# Store the length.
short_movie_count = len(netflix_df[short_action_movie])
print(short_movie_count)