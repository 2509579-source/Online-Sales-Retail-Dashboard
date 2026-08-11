# Online Retail Sales Dashboard

## Project Description

This project is an Online Retail Sales Dashboard built with Python, Flask, Pandas, and Matplotlib.

The dashboard analyzes online retail transactions and presents sales information through charts and a category search feature.

## Features

- View the online retail sales dashboard.
- View total sales by product category.
- View monthly sales trends.
- View payment-method sales distribution.
- Search and filter transactions by product category.

## Dataset

The project uses a CSV dataset containing online retail transactions.

The dataset includes:

- Transaction ID
- Date
- Category
- Product
- Quantity
- Unit Price
- Sales
- Payment Method

The dataset contains 60 transactions across 5 product categories.

## Technologies Used

- Python 3
- Flask
- Pandas
- Matplotlib
- HTML
- Jinja2

## Requirements

- Python 3
- Flask
- Pandas
- Matplotlib
- NumPy

## Project Structure

```text
Online-Sales-Retail-Dashboard/
│
├── data/
│   └── retail_sales.csv
│
├── static/
│   ├── category_sales.png
│   ├── monthly_sales.png
│   └── payment_sales.png
│
├── templates/
│   ├── base.html
│   ├── charts.html
│   ├── index.html
│   └── search.html
│
├── app.py
├── generate_data.py
├── requirements.txt
├── README.md
└── .gitignore

## Running the Application

After activating the virtual environment and installing the requirements, run:

python app.py

Then open http://127.0.0.1:5000/ in your browser.

## Project Routes

- `/` — Dashboard home page
- `/charts` — Displays the sales charts
- `/search` — Search and filter transactions by category