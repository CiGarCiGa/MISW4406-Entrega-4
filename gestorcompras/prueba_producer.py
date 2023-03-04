import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('persistent://public/default/comando_reservar_producto1')

producer.send('Hello Pulsar'.encode('utf-8'))

client.close()