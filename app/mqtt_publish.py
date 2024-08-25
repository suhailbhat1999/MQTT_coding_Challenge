
TOPIC = 'testtopic/TOPIC'

def on_connect(client, flags, rc, properties):
    client.subscribe(TOPIC, qos=1)
    print('Connected')

def on_message(client, topic, payload, qos, properties):
    print('RECV MSG:', topic, payload.decode(), properties)

async def main(broker_host, token):
    client = MQTTClient('asdfghjk')
    client.on_message = on_message
    client.on_connect = on_connect
    client.set_auth_credentials(token, None)
    await client.connect(broker_host, 1883, keepalive=60)
    client.publish(TOPIC, 'Message payload', response_topic='RESPONSE/TOPIC')

    await STOP.wait()
    await client.disconnect()