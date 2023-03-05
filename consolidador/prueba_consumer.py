import pulsar

client = pulsar.Client('pulsar://0.0.0.0:6650')

consumer = client.subscribe('persistent://public/default/comando_reservar_producto1', 'my-subscription1')

while True:
    msg = consumer.receive()
    try:
        print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
        # Acknowledge successful processing of the message
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()