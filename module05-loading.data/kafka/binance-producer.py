import asyncio
import json
from ensurepip import bootstrap

import websockets
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))


async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame)
        print(trade)
        producer.send("stockmarket", value=trade)


async def connect():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect())
    loop.run_forever()
