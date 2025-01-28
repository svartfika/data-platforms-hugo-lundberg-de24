import random
import time
from itertools import cycle
from pathlib import Path

import pandas as pd

PATH_DATA = Path(__file__).parents[1] / "data" / "orders.json"


# using while-loop with modulus reset
def main1():
    df_products = pd.read_json(PATH_DATA)["products"].explode()

    i = 0
    while True:
        product = df_products.iloc[i]
        print(product)

        time.sleep(random.uniform(0.1, 0.5))
        i = (i + 1) % len(df_products)


# using built-in itertools cycle() on df series
def main():
    df_products = pd.read_json(Path(PATH_DATA))["products"].explode()

    for product in cycle(df_products):
        print(product)

        time.sleep(random.uniform(0.1, 0.5))


if __name__ == "__main__":
    main()
