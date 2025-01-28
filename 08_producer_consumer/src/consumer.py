from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter-v1",
    auto_offset_reset="earliest",
)

topic_jokes = app.topic(name="jokes")
df_streaming = app.dataframe(topic_jokes)

df_streaming = df_streaming.update(lambda input_message: print(f"{input_message=}"))

df_streaming = df_streaming.apply(
    lambda x: [{"word": word} for word in x["joke_text"].split()],
    expand=True,
)

df_streaming["len"] = df_streaming["word"].apply(lambda x: len(x))

df_streaming = df_streaming.update(lambda x: print(x))

if __name__ == "__main__":
    app.run()
