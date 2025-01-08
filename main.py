import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file.
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the rows with the column type movie and get the duration.
# Add the total duration of movies divided with the total count of movies.
# Convert into integer.
duration = int(sum(netflix_df.loc[netflix_df["type"] == "Movie", "duration"]) / len(netflix_df[netflix_df["type"] == "Movie"]))
print(duration)

# plt.hist(netflix_df["duration"])
# plt.savefig("plot.png")

# Subset the rows with column type and genre.
short_movie_count = len(netflix_df[(netflix_df["type"] == "Movie") & (netflix_df["genre"] == "Action") & (netflix_df["duration"] < 90) & (netflix_df["release_year"].between(1990, 1999))])
print(short_movie_count)