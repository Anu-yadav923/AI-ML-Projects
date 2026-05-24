import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv(r"netflix_titles.csv")
print(df.head())

print(df.columns)

print(df.info())

print(df.isnull().sum())

df = df.dropna()

print(df.info())

movies = df[df["type"] == "Movie"]

print(movies.head())

print(df["type"].value_counts())

print(df["country"].value_counts().head())

print(df.groupby("release_year").size())

df["type"].value_counts().plot(kind="bar")
plt.show()