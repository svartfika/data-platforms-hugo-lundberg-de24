from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="product_orders",
)

topic_product_orders = app.topic(name="product_orders")
streaming_df = app.dataframe(topic_product_orders)

streaming_df = streaming_df.update(
    lambda product: print(
        f"Product: {product['name']}\tQuantity: {product['quantity']}\tPrice: {product['price']}"
    )
)

if __name__ == "__main__":
    app.run()
