import pulsar

client = pulsar.Client('pulsar://broker:6650')
consumer = client.subscribe('my-topic', "my-subscription",
                            properties={
                                "consumer-name": "test-consumer-name",
                                "consumer-id": "test-consumer-id"
                            })

while True:
    msg = consumer.receive()
    print("Received message '{0}' id='{1}'".format(msg.data().decode('utf-8'), msg.message_id()))
    consumer.acknowledge(msg)

client.close()