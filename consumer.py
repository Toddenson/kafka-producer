from json import loads

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'topic1',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='fooGroup')

for message in consumer:
    print(message.value)

