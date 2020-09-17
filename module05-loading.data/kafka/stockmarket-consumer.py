import json

from kafka import KafkaConsumer

consumer = KafkaConsumer('stockmarket', bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='stockmarket-group',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    trade = message.value
    print(trade)
