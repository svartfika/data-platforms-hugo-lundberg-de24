FROM python:3.11.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/exercise_3_2_consumer.py /usr/src/app/src/consumer.py

COPY src/exercise_3_2_producer.py /usr/src/app/src/producer.py