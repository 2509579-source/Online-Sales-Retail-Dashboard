import csv
import random
from datetime import date, timedelta

categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Beauty",
    "Sports"
]

payment_methods = [
    "Cash",
    "Card",
    "Mobile Money"
]

products = {
    "Electronics": ["Headphones", "Keyboard", "Mouse", "Speaker"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers"],
    "Home & Kitchen": ["Blender", "Kettle", "Pan", "Coffee Maker"],
    "Beauty": ["Perfume", "Face Cream", "Shampoo", "Lipstick"],
    "Sports": ["Football", "Yoga Mat", "Dumbbells", "Running Shoes"]
}

start_date = date(2026, 1, 1)

with open("data/retail_sales.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "transaction_id",
        "date",
        "category",
        "product",
        "quantity",
        "unit_price",
        "sales"
        "payment_method"
    ])

    for transaction_id in range(1, 61):
        category = random.choice(categories)
        product = random.choice(products[category])
        quantity = random.randint(1, 5)
        unit_price = random.randint(500, 15000)
        sales = quantity * unit_price
        transaction_date = start_date + timedelta(
            days=random.randint(0, 364)
        )
        payment_method = random.choice(payment_methods)

        writer.writerow([
            transaction_id,
            transaction_date,
            category,
            product,
            quantity,
            unit_price,
            sales,
            payment_method
        ])

print("Dataset created successfully!")