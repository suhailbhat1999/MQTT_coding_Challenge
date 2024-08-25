import asyncio
from gmqtt import Client as MQTTClient

loop = asyncio.get_event_loop()

client = MQTTClient("mqtt_client")


def on_message(client, topic, payload, qos, properties):
    try:
        print(f"Received message on topic {topic}: {payload.decode()}")
    except Exception as e:
        print(f"Error while receiveing the message : {e}")


def on_connect(client, flags, rc, properties):
    try:
        print("Connected to MQTT Broker")
        client.subscribe('/events')

    except Exception as e:
        print(f"Error while reading the message : {e}")


client.on_connect = on_connect
client.on_message = on_message


async def main():
    try:
        await client.connect('localhost', port=1883, keepalive=60)
        await asyncio.sleep(1)
        await client.disconnect()
    except Exception as e:
        print(f"Error while connecting to MQTT: {e}")


loop.run_until_complete(main())
loop.run_forever()
