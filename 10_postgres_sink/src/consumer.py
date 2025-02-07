from constants import (
    KAFKA_HOST,
    KAFKA_PORT,
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
)
from quixstreams import Application
from quixstreams.sinks.community.postgresql import PostgreSQLSink

app = Application(
    broker_address=f"{KAFKA_HOST}:{KAFKA_PORT}",
    consumer_group="coin",
    auto_offset_reset="earliest",
)

topic_coins = app.topic(
    "coins",
    value_deserializer="json",
)

sink_pg = PostgreSQLSink(
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    dbname=POSTGRES_DB,
    table_name="crypto_quote",
)


def remap_quote(data: dict) -> dict:
    currency = next(iter(data.get("quote", {})))
    quote = data.get("quote", {}).get(currency, {})
    return {
        "coin": data.get("name"),
        "price": quote.get("price"),
        "currency": currency,
        "volume": quote.get("volume_24h"),
        "timestamp": quote.get("last_updated"),
    }


df = app.dataframe(topic_coins)
df = df.apply(lambda x: remap_quote(x))
df.update(lambda x: print(x))
df.sink(sink=sink_pg)

if __name__ == "__main__":
    app.run()
