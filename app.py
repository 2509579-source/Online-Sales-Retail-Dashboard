from flask import Flask, render_template, request
import pandas as pd

df = pd.read_csv("data/retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])

category_sales = df.groupby("category")["sales"].sum()

monthly_sales = df.groupby(df["date"].dt.to_period("M"))["sales"].sum()

payment_sales = df.groupby("payment_method")["sales"].sum()


import matplotlib.pyplot as plt

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

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/charts")
def charts():
    return render_template("charts.html")


@app.route("/search")
def search():
    category = request.args.get("category", "")

    results = None

    if category:
        results = df[df["category"].str.contains(category, case=False, na=False)]

    return render_template("search.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
