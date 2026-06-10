
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")


print(matches.head())

print(deliveries.head())


print(matches.info())

print(deliveries.info())

print(deliveries.batsman)

top_batsmen = deliveries.groupby("batsman")["batsman_runs"].sum()

top_batsmen = top_batsmen.sort_values(ascending=False)

print(top_batsmen.head(10))

#top_batsmen.head(10).plot(kind="bar")

plt.title("Top IPL Run Scorers")

plt.xlabel("Batsman")

plt.ylabel("Runs")
plt.show()

balls = deliveries.groupby("batsman").size()
runs = deliveries.groupby("batsman")["batsman_runs"].sum()

strike_rate = (runs/balls)*100
strike_rate = strike_rate[balls > 500]

print(strike_rate.sort_values(ascending=False).head(10))

sixes = deliveries[deliveries["batsman_runs"] == 6] 

top_sixes = sixes.groupby("batsman").size()
top_sixes = top_sixes.sort_values(ascending=False)

print(top_sixes.head(10))

team_wins = matches["winner"].value_counts()
print(team_wins)


team_wins.plot(kind="bar")

plt.title("IPL Team Wins")

plt.xlabel("Team")

plt.ylabel("Wins")

plt.show()

matches["toss_match_win"] = (matches["toss_winner"] == matches["winner"])
print(matches["toss_match_win"].value_counts())

top_players = matches["player_of_match"].value_counts()
print(top_players.head(10))

venues = matches["venue"].value_counts()
print(venues.head(10))