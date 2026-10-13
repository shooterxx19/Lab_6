import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Cola", "Chips", "Milk", "Juice", "Cookies", "Yogurt", "Soda", "Nuts", "Cheese", "Water"],
    "Category": ["beverages ", "SNACKS", " Dairy", "beverages", "Snacks", "Dairy ", "BEVERAGES", "SNACKS", " dairy", "beverages"],
    "Price": ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 1,800", "Rs. 200", "Rs. 150", "Rs. 600", "Rs. 850", "Rs. 50"],
    "Stock": [40, 120, 60, 80, 50, 90, 110, 45, 30, 150]
}

df = pd.DataFrame(data)

# (a) Clean Category
df["Category"] = df["Category"].str.strip().str.title()

# (b) Clean Price
df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False).str.replace(",", "").astype(float)

# (c) Label encode Category
df["Category_Code"] = df["Category"].astype("category").cat.codes
print("Cleaned Inventory DataFrame:")
print(df)

# (d) Subplots
avg_price = df.groupby("Category")["Price"].mean()
total_stock = df.groupby("Category")["Stock"].sum()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(avg_price.index, avg_price.values, color=["#4C78A8", "#F58518", "#54A24B"])
axes[0].set_title("Average Price per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")

axes[1].pie(total_stock.values, labels=total_stock.index, autopct="%1.1f%%", startangle=90, colors=["#4C78A8", "#F58518", "#54A24B"])
axes[1].set_title("Stock Share by Category")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()
