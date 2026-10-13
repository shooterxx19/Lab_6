import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Date": ["2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05", 
             "2026-03-06", "2026-03-07", "2026-03-08", "2026-03-09", "2026-03-10", 
             "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-01"],
    "City": [" Lahore ", "lahore", "LAHORE", "Lahore", " lahore", 
             "Lahore ", "LAHORE", "lahore", "Lahore", " lahore", 
             "Lahore", "LAHORE", "lahore", "Lahore ", "Lahore", " Lahore "],
    "Temperature": ["32C", "30C", "28C", "25C", "27C", 
                    "31C", "33C", "35C", "29C", "26C", 
                    "24C", "28C", "30C", "34C", "32C", "32C"],
    "Humidity": [45.0, 50.0, np.nan, 65.0, 60.0, 
                 np.nan, 40.0, 35.0, 55.0, np.nan, 
                 70.0, 58.0, 52.0, 38.0, 44.0, 45.0],
    "Condition": ["sunny", " Rainy", "CLOUDY ", "Rainy", "cloudy", 
                  "Sunny", "SUNNY", "sunny ", "Cloudy", " rainy", 
                  "Rainy", "cloudy", "sunny", "Sunny", "CLOUDY", "sunny"]
}

df = pd.DataFrame(data)

# (a) Data wrangling
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
df["Temperature"] = df["Temperature"].str.replace("C", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])

df = df.drop_duplicates()
print("Rows after dropping duplicates:", len(df))

median_humidity = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(median_humidity)
print("Missing Humidity filled with median:", median_humidity)

# (b) One-hot encoding & Correlation
df_encoded = pd.get_dummies(df, columns=["Condition"], dtype=int)
print("\nEncoded Condition Columns:")
print(df_encoded.filter(like="Condition_").head())

corr = df["Temperature"].corr(df["Humidity"])
print(f"\nCorrelation (Temperature, Humidity): {corr:.2f}")

cond_counts = df["Condition"].value_counts()

# (c - f) 2x2 Subplots Dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Line plot
axes[0, 0].plot(df["Date"].dt.strftime("%d-%b"), df["Temperature"], marker="o", color="crimson")
axes[0, 0].set_title("Temperature Over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (°C)")
axes[0, 0].tick_params(axis="x", rotation=45)

# Scatter plot
axes[0, 1].scatter(df["Temperature"], df["Humidity"], color="teal", s=60)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (°C)")
axes[0, 1].set_ylabel("Humidity (%)")

# Pie chart
axes[1, 0].pie(cond_counts.values, labels=cond_counts.index, autopct="%1.1f%%", startangle=90)
axes[1, 0].set_title("Condition Distribution")

# Histogram
axes[1, 1].hist(df["Temperature"], bins=5, color="seagreen", edgecolor="white")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (°C)")
axes[1, 1].set_ylabel("Days")

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()
