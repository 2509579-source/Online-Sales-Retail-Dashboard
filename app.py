from flask import Flask, render_template, request
import pandas as pd

"""
Online Retail Sales Dashboard

A Flask web application that analyzes retail sales data
and displays sales charts and category search results.
"""


# Load and prepare the retail sales dataset
df = pd.read_csv("data/retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])


# Calculate sales totals for each chart
category_sales = df.groupby("category")["sales"].sum()

monthly_sales = df.groupby(df["date"].dt.to_period("M"))["sales"].sum()

payment_sales = df.groupby("payment_method")["sales"].sum()


import matplotlib.pyplot as plt

# Generate the sales charts
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("static/category_sales.png")
plt.close()

payment_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Payment Method")
plt.ylabel("")
plt.tight_layout()
plt.savefig("static/payment_sales.png")
plt.close()

# Monthly Sales Chart
monthly_sales.index = monthly_sales.index.astype(str)

monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("static/monthly_sales.png")
plt.close()

navigation = [
    {"name": "Home", "url": "/"},
    {"name": "Charts", "url": "/charts"},
    {"name": "Search", "url": "/search"}
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", navigation=navigation)


@app.route("/charts")
def charts():
    return render_template("charts.html", navigation=navigation)


@app.route("/search")
def search():
    # Get the category entered by the user
    category = request.args.get("category", "")

    results = None
    
    
# Filter transactions when a category is provided
    if category:
        results = df[df["category"].str.contains(category, case=False, na=False)]

    return render_template("search.html", results=results, navigation=navigation)


if __name__ == "__main__":
    app.run(debug=True)
