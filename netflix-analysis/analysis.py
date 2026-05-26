import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv(r"netflix_titles.csv")
print(df.head())

print(df.columns)

print(df.info())

print(df.isnull().sum())

# df = df.dropna()

print(df.info())

movies = df[df["type"] == "Movie"]

print(movies.head())

print(df["type"].value_counts())

print(df["country"].value_counts().head())

print(df.groupby("release_year").size())

#df["type"].value_counts().plot(kind="bar")
#plt.show()

df["country"] = df["country"].fillna("unknown")
df["director"] = df["director"].fillna("unknown")
print(df.info())

type_counts = df["type"].value_counts()
print(type_counts)

#type_counts.plot(kind="pie", autopct = "%1.1f%%")
#plt.show()

year_data = df.groupby("release_year").size()
print(year_data)

year_data.plot(kind="line")
plt.title("Netflix Releases Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Releases")
plt.show()

top_directors = df["director"].value_counts().head(10)
print(top_directors)

top_directors.plot(kind="bar")
plt.title("Top Directors on Netflix")
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.show()

print(df["listed_in"].head())
print(df["listed_in"].value_counts().head(10))

top_countries = df["country"].value_counts().head(10)
print(top_countries)

top_countries.plot(kind="bar")
plt.title("Top countries producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("count")
plt.show()

print(df["duration"].head())
movies = df[df["type"] == "Movie"]
movies["duration"] = movies["duration"].str.replace("min", "")
movies["duration"] = movies["duration"].fillna(0).astype(int)
longest_movie = movies["duration"].max()
print(longest_movie)

movies["duration"].plot(kind="hist")
plt.title("Movie Duration Distribution")
plt.xlabel("Minutes")
plt.show()

latest_movies = df.sort_values(by="release_year", ascending=False)
print(latest_movies[["title", "release_year"]].head())