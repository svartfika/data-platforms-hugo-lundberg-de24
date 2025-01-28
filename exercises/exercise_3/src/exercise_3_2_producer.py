import random
import time
from itertools import cycle
from pathlib import Path

import pandas as pd
from quixstreams import Application

PATH_DATA = Path(__file__).parents[1] / "data" / "orders.json"

app = Application(
    broker_address="127.0.0.1:9092",
    consumer_group="product_orders",
)

topic_product_orders = app.topic(name="product_orders")


def main():
    df_products = pd.read_json(Path(PATH_DATA))["products"].explode()

    with app.get_producer() as p:
        for product in cycle(df_products):
            kafka_msg = topic_product_orders.serialize(
                key=product["name"], value=product
            )
            print(f"{kafka_msg.value=}")

            p.produce(
                topic="product_orders",
                key=kafka_msg.key,
                value=kafka_msg.value,
            )

            time.sleep(random.uniform(0.5, 2.5))


if __name__ == "__main__":
    main()
