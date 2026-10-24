import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta

random.seed(42)

products = {
    "Laptop": ("Electronics", 45000, 75000),
    "Headphones": ("Electronics", 800, 5000),
    "T-Shirt": ("Clothing", 300, 1200),
    "Shoes": ("Clothing", 1000, 4000),
    "Book": ("Books", 150, 800),
    "Bottle": ("Accessories", 200, 700)
}

payment_methods = ["UPI", "Card", "Cash", "Net Banking"]
genders = ["Male", "Female"]

rows = []
start_date = datetime(2025, 1, 1)

for i in range(1, 1001):
    product = random.choice(list(products.keys()))
    category, min_price, max_price = products[product]

    quantity = random.randint(1, 3)
    price = random.randint(min_price, max_price)
    date = start_date + timedelta(days=random.randint(0, 364))

    rows.append({
        "OrderID": f"ORD{i:04d}",
        "OrderDate": date.strftime("%Y-%m-%d"),
        "CustomerID": f"CUST{random.randint(1, 200):03d}",
        "Gender": random.choice(genders),
        "Age": random.randint(18, 60),
        "Product": product,
        "Category": category,
        "Quantity": quantity,
        "UnitPrice": price,
        "TotalAmount": quantity * price,
        "PaymentMethod": random.choice(payment_methods)
    })

df = pd.DataFrame(rows)

Path("data").mkdir(exist_ok=True)
df.to_csv("data/customer_sales.csv", index=False)

print("Dataset created successfully!")
print("Total transactions:", len(df))
print(df.head())