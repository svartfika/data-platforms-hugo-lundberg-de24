import json
from pathlib import Path

import pandas as pd

PATH_DATA = Path(__file__).parents[1] / "data" / "orders.json"


# print details using python built-ins
with open(PATH_DATA) as f:
    data = json.load(f)

for product in [product for record in data for product in record["products"]]:
    print(
        f"Product: {product['name']}\tQuantity: {product['quantity']}\tPrice: {product['price']}"
    )


# print details using pandas
df = pd.read_json(PATH_DATA)

for product in df["products"].explode():
    print(
        f"Product: {product['name']}\tQuantity: {product['quantity']}\tPrice: {product['price']}"
    )
