import time
import requests
from constants import COINMARKETCAP_API_KEY, KAFKA_HOST, KAFKA_PORT
from quixstreams import Application
from requests import Session

API_KEY = COINMARKETCAP_API_KEY
API_ENDPOINT = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

SYMBOL: str = "BTC"
CONVERT: str = "EUR"

app = Application(
    broker_address=f"{KAFKA_HOST}:{KAFKA_PORT}",
    consumer_group="coin",
)

topic_coins = app.topic(
    "coins",
    value_deserializer="json",
)


def get_quote(session: Session, symbol="BTC", convert="USD") -> tuple[str, dict]:
    try:
        response = session.get(
            API_ENDPOINT,
            params={
                "symbol": symbol,
                "convert": convert,
            },
            headers={
                "Accepts": "application/json",
                "X-CMC_PRO_API_KEY": API_KEY,
            },
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(e)

    data = next(iter(response.json().get("data").get(symbol, [])), None)
    if not data:
        raise ValueError(f"Symbol not found: '{symbol}'")
    return symbol, data.get("quote")


def main() -> None:
    s = Session()

    with app.get_producer() as p:
        while True:
            coin, quote = get_quote(s, SYMBOL, CONVERT)
            msg = topic_coins.serialize(key=coin, value=quote)

            print(f"{msg.key=}, {msg.value=}")
            p.produce(
                topic="coins",
                key=msg.key,
                value=msg.value,
            )

            time.sleep(10)


if __name__ == "__main__":
    main()
