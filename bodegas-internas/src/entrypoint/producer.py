import pulsar

client = pulsar.Client('pulsar://broker:6650')
print(client)
producer = client.create_producer('my-topic')

for i in range(10):
    producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

client.close()