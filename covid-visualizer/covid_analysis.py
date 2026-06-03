import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("owid-covid-data.csv")
#print(df.head())
#print(df.columns)
#print(df.isnull().sum())

df = df[["location","date","total_cases","total_deaths","new_cases"]]
print(df.columns)
df = df.dropna()
india = df[df["location"] == "India"]
usa = df[df["location"] == "United States"]
print(india.head())

plt.plot(
    india["date"],
    india["new_cases"]
)

plt.title("India COVID Daily Cases")
plt.xlabel("Date")
plt.ylabel("new Cases")
plt.xticks(rotation=45)
plt.show()

plt.plot(
    india["date"],
    india["new_cases"],
    label="INDIA"
)

plt.plot(
    usa["date"],
    usa["new_cases"],
    label="USA"
)

plt.legend()
plt.show()

india["death_rate"] = (
    india["total_deaths"]
    /
    india["total_cases"]
) * 100

print(india[["date", "death_rate"]].head())

plt.plot(
    india["date"],
    india["death_rate"]
)

plt.title("India Covid Death Rate")
plt.xlabel("Date")
plt.ylabel("Death Rate (%)")
plt.xticks(rotation=45)
plt.show()

highest_cases = india["new_cases"].max()
print(highest_cases)

peak_day = india[
    india["new_cases"] == highest_cases
]

print(
    peak_day[[
        "date","new_cases"
    ]]
)

top_days = india.sort_values(
    by="new_cases",
    ascending=False
)

print(top_days[["date", "new_cases"]].head())