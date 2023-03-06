import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('topic-inicio-flujo-consolidador')

producer.send('Iniciar flujo!'.encode('utf-8'))

client.close()