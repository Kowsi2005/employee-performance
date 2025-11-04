# 📊 Sales Data Visualization using Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
data = pd.read_csv("sales_data.csv")

# Step 2: Display the data
print("Sales Data:")
print(data)

# Step 3: Plot a line chart for Sales and Profit
plt.figure(figsize=(8,5))
plt.plot(data["Month"], data["Sales"], marker='o', label='Sales', color='b')
plt.plot(data["Month"], data["Profit"], marker='s', label='Profit', color='g')

plt.title("Monthly Sales and Profit Trend", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Amount (₹)")
plt.legend()
plt.grid(True)
plt.show()

# Step 4: Create a bar chart
plt.figure(figsize=(8,5))
plt.bar(data["Month"], data["Sales"], color='skyblue')
plt.title("Monthly Sales Comparison", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Sales Amount (₹)")
plt.xticks(rotation=30)
plt.show()

# Step 5: Create a pie chart
plt.figure(figsize=(6,6))
plt.pie(data["Sales"], labels=data["Month"], autopct='%1.1f%%', startangle=90)
plt.title("Sales Contribution by Month")
plt.show()
