import pandas as pd
import matplotlib.pyplot as plt

# 1. Dataset
data = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

# (a) Clean Name using string methods
df["Name"] = df["Name"].str.strip().str.title()

# (b) Convert Marks to numeric and fill "absent" with mean
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# (c) Print cleaned DataFrame
print("Cleaned DataFrame:")
print(df)

# (d) Draw bar plot and save
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"], color="skyblue", edgecolor="black")
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("marks_bar.png")
plt.show()
