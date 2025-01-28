import json
from pathlib import Path

from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"

with open(data_path / "jokes.json") as f:
    data = json.load(f)

app = Application(broker_address="127.0.0.1:9092", consumer_group="text-splitter")

topic_jokes = app.topic(name="jokes", value_deserializer="json")


def main():
    with app.get_producer() as p:
        for item in data:
            kafka_msg = topic_jokes.serialize(key=item["joke_id"], value=item)
            print(f"{kafka_msg.key=}, {kafka_msg.value=}")

            p.produce(topic="jokes", key=str(kafka_msg.key), value=kafka_msg.value)


if __name__ == "__main__":
    main()
