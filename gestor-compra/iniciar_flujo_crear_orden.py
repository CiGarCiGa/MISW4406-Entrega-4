import pulsar

client = pulsar.Client('pulsar://broker:6650')

producer = client.create_producer('topic-inicio-flujo-crear-orden')

producer.send('Iniciar flujo!'.encode('utf-8'))

client.close()